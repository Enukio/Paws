import os
import re
import requests
import logging
from colorama import init, Fore, Style

init(autoreset=True)

class ColorFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, name="Paws"):
        super().__init__(fmt, datefmt)
        self.name = name
        
    def format(self, record):
        level_color = {
            'INFO': Fore.CYAN,
            'WARNING': Fore.MAGENTA,
            'ERROR': Fore.YELLOW,
            'CRITICAL': Fore.RED + Style.BRIGHT
        }.get(record.levelname, Fore.WHITE)
        
        record.colored_levelname = f"{level_color}{record.levelname}{Style.RESET_ALL}"
        record.botname = f"{Fore.RED}[{self.name}]{Style.RESET_ALL}"
        record.msg = f"{Style.BRIGHT}{record.msg}{Style.RESET_ALL}"
        return super().format(record)

# Configure logger
formatter = ColorFormatter('%(botname)s | %(asctime)s | %(colored_levelname)s | %(message)s', '%Y-%m-%d %H:%M:%S', "Paws")
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger("Paws")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def storage(filenames, output_file):
    if not isinstance(filenames, list) or not all(isinstance(item, str) for item in filenames):
        logger.error("Invalid input: filenames must be a list of strings.")
        return
    
    try:
        dir_name = os.path.dirname(output_file)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(','.join(filenames))
        logger.info(f"Saved {len(filenames)} filenames to {Fore.GREEN}{output_file}{Style.RESET_ALL}.")
    except Exception as e:
        logger.error(f"Failed to save filenames: {e}")

def get_main_js_format(base_url, output_file="./paws"):
    if not base_url.startswith(('http://', 'https://')):
        logger.error(f"Invalid URL: {base_url}")
        return None
    
    try:
        logger.info(f"Fetching URL: {Fore.GREEN}{base_url}{Style.RESET_ALL}")
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        content = response.text

        # Use regex to find JavaScript file paths for both patterns
        patterns = [r'src="(/.*?_app.*?\.js)"', r'src="(/.*?/index.*?\.js)"']
        matches = []
        for pattern in patterns:
            matches += re.findall(pattern, content)
        
        if matches:
            logger.info(f"Found {len(matches)} JavaScript files.")
            matches = sorted(set(matches), key=lambda x: (not x.startswith('_app'), x))
            filenames = [os.path.basename(match) for match in matches]
            storage(filenames, output_file)
            return filenames
        else:
            logger.warning("No matching files found.")
            return None
    except requests.Timeout:
        logger.error(f"Request timed out for {base_url}")
    except requests.ConnectionError:
        logger.error(f"Connection error for {base_url}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    return None

# Main block for execution
BASE_URL = "https://app.paws.community"  # Replace with your target URL
OUTPUT_FILE = "./paws"  # Save all filenames to this file

# Let's run the function and capture filenames
filenames = get_main_js_format(BASE_URL, OUTPUT_FILE)
if filenames is None:
    logger.info(f"{Fore.YELLOW}No filenames were saved.{Style.RESET_ALL}")
else:
    logger.info(f"Filenames processed: {Fore.GREEN}{filenames}{Style.RESET_ALL}")

    # Return to main.py
    print("\n🔄 Returning to Menu in 2 seconds...\n")
    if os.path.exists("main.py"):
        os.system(f'"{sys.executable}" main.py')
    else:
        logger.error("main.py not found. Exiting.")
