import requests

def fetch_urls(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Failed to fetch URLs from {url}: {e}")
        return []

def main():
    # Load models URLs from the file obtained in the GitHub Actions workflow
    with open("models.txt", "r") as models_file:
        models = models_file.read().splitlines()

    # Fetch accessible URLs from an external source
    accessible_urls_url = "https://raw.githubusercontent.com/Monkfishare/test/main/models.txt"
    accessible_urls = fetch_urls(accessible_urls_url)

    # Filter URLs based on criteria (contain "tz2", "samdec", or "samenc")
    filtered_accessible_urls = [url for url in accessible_urls if any(keyword in url for keyword in ["tz2", "samdec", "samenc"])]

    # Combine the filtered lists and remove duplicates
    combined_filtered_urls = list(set(models + filtered_accessible_urls))

    # Sort the combined URLs in sequence order A to Z
    combined_filtered_urls.sort()

    # Output the result to a text file
    output_file_path = "models.txt"
    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(combined_filtered_urls))

if __name__ == "__main__":
    main()
