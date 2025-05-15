### Description of `odesli.py`

**odesli.py** is a command-line Python script that retrieves song links from the Odesli (Songlink) API. It takes a music URL (or multiple URLs) as input and fetches corresponding links for the song across various music platforms, such as Spotify, Apple Music, Tidal, and more. Users can provide a single URL or a text file containing multiple URLs, filter the results to specific services, specify a country code for region-specific links, and optionally save the output to a file.

#### What the Command Does
- Queries the Odesli API to fetch song links for a given music URL or a list of URLs.
- Supports multiple music platforms and displays links for each available service.
- Allows filtering of results to include only selected music services.
- Prints the links to the console and can save them to an output file if specified.

#### How to Use It
Run the script from the command line using the following syntax:

```
./odesli.py [--url <url> | --file <file>] [--country <country_code>] [--songIfSingle <True|False>] [--select <service1> <service2> ...] [--output <file>]
```

- You must provide either `--url` or `--file` (but not both).
- Additional options can be added as needed.

#### Options
- **`--url <url>`**: Specifies a single song URL (e.g., a Spotify track URL).
- **`--file <file>`**: Specifies a text file containing one song URL per line.
- **`--country <country_code>`**: (Optional) Sets the user's country code (e.g., "US") to retrieve region-specific links.
- **`--songIfSingle <True|False>`**: (Optional) If `True`, treats singles as songs; defaults to `False`.
- **`--select <service1> <service2> ...`** or **`-s <service1> <service2> ...`**: (Optional) Filters the output to include only the specified music services (e.g., `tidal`, `spotify`). Services are space-separated.
- **`--output <file>`** or **`-o <file>`**: (Optional) Saves the fetched links to the specified file instead of just printing them to the console.

#### Requirements
To run `odesli.py`, you need to install the following Python packages using `pip`:

```
pip install requests colorama
```

- **`requests`**: Used to make HTTP requests to the Odesli API.
- **`colorama`**: Enables colored output in the console for better readability.

No additional installations are required, as other dependencies (`argparse` and `json`) are part of Python's standard library.

#### Example Usage
1. **Fetch links for a single URL**:
   ```
   ./odesli.py --url https://open.spotify.com/track/3P2zU7XZBK5g6IYENRSTyj
   ```
   This retrieves and displays links for the specified Spotify track across available platforms.

2. **Fetch links for multiple URLs from a file**:
   ```
   ./odesli.py --file urls.txt
   ```
   Assumes `urls.txt` contains one URL per line (e.g., Spotify or YouTube links).

3. **Fetch links for specific services and save to a file**:
   ```
   ./odesli.py --file urls.txt --select tidal spotify --output links.txt
   ```
   Filters the results to Tidal and Spotify links and saves them to `links.txt`.

#### Output
- **Console Output**: The script prints the song URL followed by available links for each service. If `--select` is used, only the specified services are shown.
- **File Output**: If `--output` is provided, links are written to the specified file, one link per line.
- **Errors**: If no links are found or an error occurs (e.g., network issues), a message is displayed in the console.

