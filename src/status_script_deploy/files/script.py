import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

status_codes = [200, 201, 306, 404, 500]
base_url = "https://httpstat.us/"

for code in status_codes:
    url = f"{base_url}{code}"
    try:
        response = requests.get(url)
        status = response.status_code

        if 100 <= status < 400:
            logging.info(f"Response from {url}: Status {status}, Body: {response.text}")
        elif 400 <= status < 600:
            raise Exception(f"Error response from {url}: Status {status}")
        else:
            logging.warning(f"Unexpected status code from {url}: {status}")
    except Exception as e:
        logging.error(e)
