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
    accessible_urls_url = "https://raw.githubusercontent.com/Monkfishare/test/main/accessible_urls.txt"
    accessible_urls = fetch_urls(accessible_urls_url)

    # Filter URLs based on criteria (contain "tz2", "samdec", or "samenc")
    filtered_accessible_urls = [url for url in accessible_urls if any(keyword in url for keyword in ["tz2", "samdec", "samenc"])]

    # Combine the filtered lists and remove duplicates
    combined_filtered_urls = list(set(models + filtered_accessible_urls))

    # Sort the combined URLs in sequence order A to Z
    combined_filtered_urls.sort()

    # Write the combined and sorted URLs to models.txt
    with open("models.txt", 'w') as output_file:
        output_file.write('\n'.join(combined_filtered_urls))

    # Generate README.md
    with open("README_TEMPLATE.md", "r") as template_file:
        template_content = template_file.read()

        # Generate models table content with auto-generated sequential numbering
        models_table_content = ""
        for num, url in enumerate(combined_filtered_urls, start=1):
            models_table_content += f"| {num} | {url} |\n"

        # Replace placeholders with actual content
        template_content = template_content.replace('TOPAZ_VERSION', '2.2.2')  # Replace with actual version
        template_content = template_content.replace('BILIBILI_TUTORIAL_LINK', "https://www.bilibili.com/read/cv25993828")
        template_content = template_content.replace('ARCHIVED_TUTORIAL_LINK', "https://archive.ph/HfQIm")
        template_content = template_content.replace('MODELS_TABLE_CONTENT', models_table_content)

    # Save the generated content to README.md
    with open("README.md", 'w') as readme_file:
        readme_file.write(template_content)

if __name__ == "__main__":
    main()
