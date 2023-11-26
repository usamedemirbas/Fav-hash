import requests
import mmh3
import base64
import argparse

def get_favicon_hash(favicon_url):
    response = requests.get(favicon_url)

    if response.status_code == 200:
        favicon_content = response.content
        favicon_hash = mmh3.hash(base64.b64encode(favicon_content))
        print("Shodan Query: http.favicon.hash:" + str(favicon_hash))
    else:
        print("Failed to fetch favicon.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="#####Generate mmh3 hash for a favicon and create a Shodan query.######")
    parser.add_argument("favicon_url", help="URL of the favicon to hash")

    args = parser.parse_args()

    if args.favicon_url == "--help":
        print("Usage: python script_name.py <favicon_url>")
    else:
        get_favicon_hash(args.favicon_url)
