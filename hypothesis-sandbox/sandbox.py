import json
import requests
import urllib

# Hypothes.is API search endpoint
# url = "https://api.hypothes.is/users"

# Your Hypothes.is userid
user_id = "acct:asmacdo@hypothes.is"
api_token = "6879-L9jjIBp8WFo8c3p0Rc3AzlY5BbwKhdytF7Eln7S8HN4"
# URL-encode the userid
encoded_user_id = urllib.parse.quote(user_id, safe='')

# Construct the endpoint URL
# url = f"https://hypothes.is/api/users/{encoded_user_id}"
# url = f"https://hypothes.is/api/users/asmacdo"  #Jk:{encoded_user_id}"
url = f"https://hypothes.is/api/search"

annotation_id = "zcPjfAw9EfCHAfPyCu-ayw"
# url = f"https://hypothes.is/api/annotations/{annotation_id}"

# Optionally, add authentication headers if needed (replace YOUR_API_TOKEN)
headers = {
    "Authorization": f"Bearer {api_token}"
}

params = {
    "user": user_id,
    "tag": "api_test",
    # "id": "bRJD1gwiEfC4CbsJ3SYaFg",
}
response = requests.get(url, headers=headers, params=params)


# Parameters for the API call: for instance, get up to 5 annotations for a given URL
# params = {}
#     "user": "acct:asmacdo@hypothes.is",
#     # "uri": "https://example.com",  # Replace with the target URL
#     "limit": 5                     # Number of annotations to retrieve
# }

# Make the GET request to the Hypothes.is API
# response = requests.get(url)

if response.status_code == 200:
    annotations = response.json()
    # print("Annotations retrieved:")
    print(json.dumps(annotations))
else:
    print(response.status_code)
    print(response.text)
    print()
    # print("Error fetching annotations. Status code:", response.status_code)

