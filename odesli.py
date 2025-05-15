#!/usr/bin/python3
#############################
#                           #
#                           #
#         The Doll          #
#                           #
#                           #
#############################
import requests
import argparse
import json
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def normalize_service_names(links):
    normalized_links = {}
    for service, info in links.items():
        normalized_service = service.lower().replace(" ", "_")
        normalized_links[normalized_service] = info
    return normalized_links

def fetch_links(url, country, song_if_single):
    base_url = "https://api.song.link/v1-alpha.1/links"
    params = {'url': url, 'userCountry': country, 'songIfSingle': song_if_single}
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    
    if 'linksByPlatform' not in data:
        return None
    
    return normalize_service_names(data['linksByPlatform'])

def print_links(url, links, selected_services=None):
    print(Style.BRIGHT + f"\nResults for URL: {url}")
    print(Style.BRIGHT + "Available Links:")
    print("-" * 40)
    
    filtered_links = links
    if selected_services:
        filtered_links = {k: v for k, v in links.items() if k in selected_services}
    
    for service, info in filtered_links.items():
        normalized_service = normalize_service_name(service)
        print(f"{normalized_service}: {info['url']}")
    
    print("-" * 40)
    return filtered_links

def normalize_service_name(service):
    service_colors = {
        "spotify": Fore.GREEN,
        "itunes": Fore.CYAN,
        "apple_music": Fore.RED,
        "youtube": Fore.YELLOW,
        "youtube_music": Fore.YELLOW + Style.BRIGHT,
        "google": Fore.BLUE,
        "google_store": Fore.BLUE,
        "pandora": Fore.MAGENTA,
        "deezer": Fore.BLUE,
        "tidal": Fore.MAGENTA,
        "amazon_store": Fore.YELLOW,
        "amazon_music": Fore.YELLOW,
        "soundcloud": Fore.CYAN,
        "napster": Fore.YELLOW,
        "yandex": Fore.LIGHTYELLOW_EX,
        "spinrilla": Fore.GREEN,
        "audius": Fore.LIGHTCYAN_EX,
        "anghami": Fore.LIGHTYELLOW_EX,
        "boomplay": Fore.GREEN,
        "audiomack": Fore.GREEN,
    }
    return service_colors.get(service, Fore.WHITE) + service.replace("_", " ").title() + Style.RESET_ALL

def main():
    parser = argparse.ArgumentParser(description="Fetch song links from Odesli API.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--url', type=str, help="Single song URL")
    group.add_argument('--file', type=str, help="Text file containing URLs")
    
    parser.add_argument('--country', type=str, help="User country code")
    parser.add_argument('--songIfSingle', type=bool, help="Treat singles as songs")
    parser.add_argument('--select', '-s', nargs='+', help="Services to save (e.g., tidal)")
    parser.add_argument('--output', '-o', type=str, help="Output file to save links")

    args = parser.parse_args()
    
    selected_services = {s.strip().lower().replace(' ', '_') for s in args.select} if args.select else None
    output_file = open(args.output, 'w') if args.output else None

    try:
        urls = []
        if args.file:
            with open(args.file, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
        else:
            urls = [args.url]

        for url in urls:
            try:
                links = fetch_links(url, args.country, args.songIfSingle)
                if not links:
                    print(f"{Fore.YELLOW}No links found for {url}")
                    continue

                filtered_links = print_links(url, links, selected_services)
                
                if output_file and filtered_links:
                    for info in filtered_links.values():
                        output_file.write(f"{info['url']}\n")

            except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
                print(f"{Fore.RED}Error processing {url}: {str(e)}")

    finally:
        if output_file:
            output_file.close()

if __name__ == "__main__":
    main()
