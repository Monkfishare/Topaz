def fetch_urls(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Failed to fetch URLs from {url}: {e}")
	@@ -27,10 +27,28 @@ def main():
    # Sort the combined URLs in sequence order A to Z
    combined_filtered_urls.sort()

    # Output the result to a text file
    output_file_path = "models.txt"
    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(combined_filtered_urls))
