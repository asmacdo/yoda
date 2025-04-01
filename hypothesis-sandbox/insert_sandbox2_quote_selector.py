import json
import requests
import urllib
from bs4 import BeautifulSoup

# --- Configuration ---
user_id = "acct:asmacdo@hypothes.is"
api_token = "6879-L9jjIBp8WFo8c3p0Rc3AzlY5BbwKhdytF7Eln7S8HN4"
annotation_id = "zcPjfAw9EfCHAfPyCu-ayw"
headers = {"Authorization": f"Bearer {api_token}"}

# --- Retrieve the annotation ---
annotation_url = f"https://hypothes.is/api/annotations/{annotation_id}"
params = {"user": user_id, "tag": "yoda"}
response = requests.get(annotation_url, headers=headers, params=params)

if response.status_code != 200:
    print("Error retrieving annotation:", response.status_code)
    print(response.text)
    exit()

annotation = response.json()

# --- Retrieve the primary source text ---
source_url = annotation.get("uri")
print("Fetching source text from:", source_url)
source_response = requests.get(source_url)
if source_response.status_code != 200:
    print("Error fetching source:", source_response.status_code)
    print(source_response.text)
    exit()

# Extract text using BeautifulSoup (adjust extraction as needed)
soup = BeautifulSoup(source_response.content, "html.parser")
source_text = soup.get_text(separator="\n", strip=True)

# --- Locate the TextQuoteSelector ---
tqs = None
for selector in annotation["target"][0]["selector"]:
    if selector.get("type") == "TextQuoteSelector":
        tqs = selector
        break

if not tqs:
    print("No TextQuoteSelector found in annotation.")
    exit()

exact = tqs.get("exact")
prefix = tqs.get("prefix", "")
suffix = tqs.get("suffix", "")

# --- Find the annotated text within the source ---
# Try to locate the occurrence using prefix+exact
start_idx = source_text.find(prefix + exact)
if start_idx != -1:
    # Adjust start index to point to the exact text
    start_idx += len(prefix)
else:
    # Fall back to searching for exact text alone
    start_idx = source_text.find(exact)

if start_idx == -1:
    print("Could not locate the annotated text in the source.")
    exit()

end_idx = start_idx + len(exact)
annotation_comment = annotation.get("text", "")

# --- Implant markers into the source text ---
marker_start = f"[[ANNOTATION: {annotation_comment}]]"
marker_end = "[[/ANNOTATION]]"

modified_text = (
    source_text[:start_idx]
    + marker_start
    + source_text[start_idx:end_idx]
    + marker_end
    + source_text[end_idx:]
)

print(modified_text)

