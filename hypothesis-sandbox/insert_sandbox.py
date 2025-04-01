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
url = f"https://hypothes.is/api/annotations/{annotation_id}"
params = {"user": user_id, "tag": "yoda"}
response = requests.get(url, headers=headers, params=params)

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

# Use BeautifulSoup to extract text (adjust extraction logic as needed)
soup = BeautifulSoup(source_response.content, "html.parser")
source_text = soup.get_text(separator="\n", strip=True)

# --- Find the TextPositionSelector ---
text_position = None
for selector in annotation["target"][0]["selector"]:
    if selector.get("type") == "TextPositionSelector":
        text_position = selector
        break

if not text_position:
    print("No TextPositionSelector found in annotation.")
    exit()

start_index = text_position.get("start")
end_index = text_position.get("end")
annotation_comment = annotation.get("text")

# --- Implant markers into the source text ---
# Define markers to show the annotation. These can be customized.
marker_start = f"[[ANNOTATION: {annotation_comment}]]"
marker_end = f"[[/ANNOTATION]]"

# Note: Inserting markers changes text positions. For a single annotation, this simple approach works.
modified_text = (
    source_text[:start_index]
    + marker_start
    + source_text[start_index:end_index]
    + marker_end
    + source_text[end_index:]
)

# --- Output the modified text ---
# This output is now in a form that can be uploaded to an AI chatbot as context.
print(modified_text)

