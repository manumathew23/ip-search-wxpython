import concurrent.futures

import requests

from constants import *

def download_data(rir_entry):
    rir = rir_entry[0]
    link = rir_entry[1]
    print("Fetching data for %s" % rir)
    data = requests.get(link)
    if data.status_code == 200:
        print("Writing %s data into file" % rir)
        file_name = rir + ".csv"
        with open(file_name, mode='wb') as file:
            file.write(data.content)
    else:
        print("Error fetching data for %s" % rir)

print("Hold on, This might take a while to load")

with concurrent.futures.ThreadPoolExecutor(max_workers=len(RIR_URL_MAPPING)) as executor:
    executor.map(download_data, RIR_URL_MAPPING.items())

print("All regional registry data loaded")