#!/usr/bin/env python3
import argparse
import json
import os
import requests
import urllib.parse
from collections import defaultdict
from bs4 import BeautifulSoup

# --- Configuration ---
USER_ID = "acct:asmacdo@hypothes.is"
API_TOKEN = os.environ.get("HYPOTHESIS_API_TOKEN")
if not API_TOKEN:
    raise ValueError("Please set the HYPOTHESIS_API_TOKEN environment variable.")
API_BASE_URL = "https://api.hypothes.is/api/search"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

def fetch_annotations(tag):
    """Fetch annotations for a given tag."""
    params = {
        "user": USER_ID,
        "tag": tag,
        "limit": 200  # adjust limit as needed
    }
    response = requests.get(API_BASE_URL, headers=HEADERS, params=params)
    if response.status_code != 200:
        print("Error fetching annotations:", response.status_code, response.text)
        return []
    data = response.json()
    return data.get("rows", [])

def fetch_source_text(uri):
    """Fetch and process source text from a URL using BeautifulSoup."""
    try:
        response = requests.get(uri)
        if response.status_code != 200:
            print(f"Error fetching source {uri}: {response.status_code}")
            return None
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        return text
    except Exception as e:
        print(f"Exception fetching source {uri}: {e}")
        return None

def find_annotation_positions(source_text, annotation):
    """
    Locate the annotated text within source_text using the TextQuoteSelector.
    Returns a tuple (start_idx, end_idx) or None if not found.
    """
    targets = annotation.get("target", [])
    if not targets:
        return None
    selectors = targets[0].get("selector", [])
    tqs = None
    for selector in selectors:
        if selector.get("type") == "TextQuoteSelector":
            tqs = selector
            break
    if not tqs:
        return None

    exact = tqs.get("exact", "")
    prefix = tqs.get("prefix", "")
    # First, try to locate the combination of prefix + exact
    start_idx = source_text.find(prefix + exact)
    if start_idx != -1:
        start_idx += len(prefix)
    else:
        # Fall back to finding the exact text alone
        start_idx = source_text.find(exact)
    if start_idx == -1:
        return None
    end_idx = start_idx + len(exact)
    return (start_idx, end_idx)

def insert_annotations(source_text, annotations):
    """
    Insert annotation markers into the source text.
    For each annotation, insert a start marker before and an end marker after the annotated snippet.
    Handles multiple annotations by collecting all insertion operations and applying them in descending order.
    """
    # List of (position, marker) tuples.
    inserts = []
    for ann in annotations:
        pos = find_annotation_positions(source_text, ann)
        if pos is None:
            print("Warning: Could not locate annotation in source for ID:", ann.get("id"))
            continue
        start_idx, end_idx = pos
        comment = ann.get("text", "")
        marker_start = f"[[ANNOTATION: {comment}]]"
        marker_end = "[[/ANNOTATION]]"
        # Record the operations; they are computed relative to the original text.
        inserts.append((start_idx, marker_start))
        inserts.append((end_idx, marker_end))

    # Sort operations by position descending so that later insertions don't affect earlier offsets.
    inserts.sort(key=lambda x: x[0], reverse=True)
    modified_text = source_text
    for pos, marker in inserts:
        modified_text = modified_text[:pos] + marker + modified_text[pos:]
    return modified_text

def sanitize_filename(uri):
    """Create a safe filename from a URI."""
    parsed = urllib.parse.urlparse(uri)
    # Combine netloc and path, replacing slashes with underscores.
    filename = (parsed.netloc + parsed.path).replace("/", "_")
    if not filename:
        filename = "source"
    return filename + "_annotated.txt"

def main():
    parser = argparse.ArgumentParser(
        description="Retrieve Hypothes.is annotations by tag, embed them into the source text, and save to files."
    )
    parser.add_argument("tag", help="Tag to search for annotations.")
    args = parser.parse_args()

    tag = args.tag
    annotations = fetch_annotations(tag)
    if not annotations:
        print("No annotations found for tag:", tag)
        return

    # Group annotations by their source URI.
    grouped = defaultdict(list)
    for ann in annotations:
        uri = ann.get("uri")
        if uri:
            grouped[uri].append(ann)

    # Process each source only once.
    for uri, anns in grouped.items():
        print(f"Processing source: {uri} with {len(anns)} annotation(s)")
        source_text = fetch_source_text(uri)
        if source_text is None:
            continue
        modified_text = insert_annotations(source_text, anns)
        filename = sanitize_filename(uri)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(modified_text)
        print(f"Saved annotated source to {filename}")

if __name__ == "__main__":
    main()

