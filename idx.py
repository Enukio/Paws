import os
import re
import requests
import logging
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Custom logging formatter with colors
class ColorFormatter(logging.Formatter):
    def format(self, record):
        # Define color styles for log levels
        level_color = {
            'INFO': Fore.CYAN,          # INFO: Cyan
            'WARNING': Fore.MAGENTA,    # WARNING: Magenta
            'ERROR': Fore.YELLOW,       # ERROR: Yellow
            'CRITICAL': Fore.RED + Style.BRIGHT  # CRITICAL: Bright Red
        }.get(record.levelname, Fore.WHITE)  # Default to white

        # Add color to the log level and "[Not pixel]"
        record.levelname = f"{level_color}{record.levelname}{Style.RESET_ALL}"
        record.notpixel = f"{Fore.RED}[Not pixel]{Style.RESET_ALL}"  # [Not pixel] in red
        record.msg = f"{Style.BRIGHT}{record.msg}{Style.RESET_ALL}"
        return super().format(record)

# Configure logger
formatter = ColorFormatter('%(notpixel)s | %(asctime)s | %(levelname)s | %(message)s', '%Y-%m-%d %H:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger('[Not pixel]')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def save_filename_to_paws(filenames, output_file):
    """
    Save the list of JavaScript filenames to a px file.

    :param filenames: List of JavaScript filenames to save.
    :param output_file: Path to the px file where filenames will be saved.
    """
    try:
        # Write filenames as a single comma-separated line
        with open(output_file, 'w') as f:
            f.write(','.join(filenames))
        logger.info(f"Saved {len(filenames)} filenames to {output_file} in specific order.")
    except Exception as e:
        logger.error(f"Failed to save filenames to {output_file}: {e}")

def get_main_js_format(base_url, output_file="./paws"):
    """
    Scrape the base page to find JavaScript files matching the pattern and save filenames.

    :param base_url: The URL of the webpage to scrape.
    :param output_file: The file to save the list of JavaScript filenames (as file).
    :return: A list of filenames or None if no matches are found.
    """
    try:
        logger.info(f"Fetching base URL: {base_url}")
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        content = response.text

        # Use regex to find JavaScript file paths for both patterns
        patterns = [
            r'src="(/.*?_app.*?\.js)"',    # Pattern 1 
            r'src="(/.*?/index.*?\.js)"'   # Pattern 2
        ]

        matches = []
        for pattern in patterns:
            matches += re.findall(pattern, content)

        if matches:
            logger.info(f"Found {len(matches)} JavaScript files matching the patterns.")
            matches = sorted(set(matches), key=lambda x: (not x.startswith('_app'), x))
            filenames = [os.path.basename(match) for match in matches]

            # Save the filenames to the output file in the specified order
            save_filename_to_paws(filenames, output_file)
            return filenames
        else:
            logger.warning("No matching JavaScript files found.")
            return None
    except requests.RequestException as e:
        logger.error(f"Error fetching the base URL: {e}")
        return None

# Main block for execution
if __name__ == "__main__":
    # Simulate the JavaScript file fetching process
    BASE_URL = "https://app.paws.community"  # Replace with your target URL
    OUTPUT_FILE = "./paws"  # Save all filenames to this px file
    filenames = get_main_js_format(BASE_URL, OUTPUT_FILE)
    if not filenames:
        logger.info("No filenames were saved.")