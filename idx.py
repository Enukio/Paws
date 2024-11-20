import os
import re
import requests
import logging
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Custom logging formatter with colors
class ColorFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, name="Paws"):
        super().__init__(fmt, datefmt)
        self.name = name  # Set custom name

    def format(self, record):
        # Define color styles for log levels
        level_color = {
            'INFO': Fore.CYAN,          # INFO: Cyan
            'WARNING': Fore.MAGENTA,    # WARNING: Magenta
            'ERROR': Fore.YELLOW,       # ERROR: Yellow
            'CRITICAL': Fore.RED + Style.BRIGHT  # CRITICAL: Bright Red
        }.get(record.levelname, Fore.WHITE)  # Default to white

        # Add color to the log level
        record.levelname = f"{level_color}{record.levelname}{Style.RESET_ALL}"
        record.botname = f"{Fore.RED}[{self.name}]{Style.RESET_ALL}"
        record.msg = f"{Style.BRIGHT}{record.msg}{Style.RESET_ALL}"
        return super().format(record)

# Configure logger
formatter = ColorFormatter('%(botname)s | %(asctime)s | %(levelname)s | %(message)s', '%Y-%m-%d %H:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger('[{self.name}]')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Variable definitions
BASE_URL = "https://app.paws.community"  # Replace with your target URL
OUTPUT_FILE = "./paws"  # Output file

# Function to save filenames to a file
def storage(filenames, output_file):
    try:
        with open(output_file, 'w') as f:
            f.write(','.join(filenames))
        logger.info(f"Saved {len(filenames)} filenames to {output_file} in specific order.")
    except Exception as e:
        logger.error(f"Failed to save filenames to {output_file}: {e}")

# Function to fetch and process JavaScript file names from the base URL
def get_main_js_format(base_url, output_file="./paws"):
    try:
        print(f"{Fore.CYAN}Fetching base URL: {Style.BRIGHT}{base_url}{Style.RESET_ALL}")
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
            print(f"{Fore.GREEN}Found {len(matches)} JavaScript files matching the patterns.{Style.RESET_ALL}")
            matches = sorted(set(matches), key=lambda x: (not x.startswith('_app'), x))
            filenames = [os.path.basename(match) for match in matches]

            # Save the filenames to the output file in the specified order
            storage(filenames, output_file)
            print(f"{Fore.YELLOW}Filenames saved to: {Style.BRIGHT}{output_file}{Style.RESET_ALL}")
            return filenames
        else:
            print(f"{Fore.MAGENTA}No matching JavaScript files found.{Style.RESET_ALL}")
            return None
    except requests.RequestException as e:
        print(f"{Fore.RED}Error fetching the base URL: {e}{Style.RESET_ALL}")
        return None

# Main block for execution
if __name__ == "__main__":
    # Simulate the JavaScript file fetching process
    filenames = get_main_js_format(BASE_URL, OUTPUT_FILE)
    if not filenames:
        print(f"{Fore.RED}No filenames were saved.{Style.RESET_ALL}")
