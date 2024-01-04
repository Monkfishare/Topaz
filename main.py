import requests

def fetch_urls(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print(f"Failed to fetch URLs from {url}")
        return []

# Load models URLs from the file obtained in the GitHub Actions workflow
with open("models.txt", "r") as models_file:
    models = models_file.read().splitlines()

# Fetch accessible URLs from an external source
accessible_urls_url = "https://raw.githubusercontent.com/Monkfishare/test/main/accessible_urls.txt"
accessible_urls = fetch_urls(accessible_urls_url)

# Filter URLs based on criteria (contain "tz2", "samdec", or "samenc")
filtered_accessible_urls = [url for url in accessible_urls if "tz2" in url or "samdec" in url or "samenc" in url]

# Combine the filtered lists and remove duplicates
combined_filtered_urls = list(set(models + filtered_accessible_urls))

# Sort the combined URLs in sequence order A to Z
combined_filtered_urls.sort()

# Output the result to a text file
output_file_path = "models.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write('\n'.join(combined_filtered_urls))
