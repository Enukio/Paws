import re
from ua_generator import generate
from ua_generator.options import Options
from ua_generator.data.version import VersionRange


def generate_random_user_agent(device_type='android', browser_type='chrome'):
    try:
        chrome_version_range = VersionRange(min_version=117, max_version=130)
        options = Options(version_ranges={browser_type: chrome_version_range})
        ua = generate(platform=device_type, browser=browser_type, options=options)
        return ua.text
    except Exception as e:
        
        print(f"Error generating User-Agent: {e}")
        return None


def fetch_version(ua):
    if not ua:
        print("User-Agent is empty or None.")
        return None

    match = re.search(r"Chrome/(\d+)", ua)
    if match:
        return match.group(1)
    else:
        print("Chrome version not found in the User-Agent.")
        return None


if __name__ == "__main__":
    
    user_agent = generate_random_user_agent()
    if user_agent:
        print(f"Generated User-Agent: {user_agent}")
        
        version = fetch_version(user_agent)
        if version:
            print(f"Chrome major version: {version}")
