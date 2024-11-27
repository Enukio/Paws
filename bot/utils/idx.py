import os
import sys
import re
import requests
from loguru import logger

# Constants
BASE_URL = "https://app.paws.community"  # Replace with your target URL
OUTPUT_FILE = "./paws"  # Save all filenames to this file

# Configure logger
logger.remove()
logger.add(
    sink=sys.stdout,
    format="<r>[Not Pixel]</r> | <white>{time:YYYY-MM-DD HH:mm:ss}</white> | "
           "<level>{level}</level> | <cyan>{line}</cyan> | {message}",
    colorize=True
)
logger = logger.opt(colors=True)

# Function to save filenames to a file
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
        logger.info(f"Saved {len(filenames)} filenames to <green>{output_file}</green>")
    except Exception as e:
        logger.error(f"Failed to save filenames: {e}")

# Function to fetch JavaScript file names from a URL
def get_main_js_format(base_url, output_file="./paws"):
    if not base_url.startswith(('http://', 'https://')):
        logger.error(f"Invalid URL: {base_url}")
        return None
    
    try:
        logger.info(f"Fetching URL: <green>{base_url}</green>")
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

# Main execution
if __name__ == "__main__":
    filenames = get_main_js_format(BASE_URL, OUTPUT_FILE)
    if filenames is None:
        logger.info("No filenames were saved.")
    else:
        logger.info(f"Filenames processed: <green>{filenames}</green>")

        # Return to main.py
        print("\n🔄 Returning to Menu in 2 seconds...\n")
        if os.path.exists("main.py"):
            os.system(f'"{sys.executable}" main.py')
        else:
            logger.error("main.py not found. Exiting.")
