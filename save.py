import sys
from os.path import isfile, join
import requests
import os
import json


root_dir = '.'
url = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'

parts = url.split('/')
print parts

folder_levels = parts[3:-1]
print folder_levels

folder = '/'.join(folder_levels)
print folder

if not os.path.exists(join(root_dir, folder)):
    os.makedirs(join(root_dir, folder))
	
#response = requests.get(url)
#with open(join(root_dir, folder, parts[-1]), 'wb') as f:
#    f.write(response.content)

response = requests.get(url, stream=True)
chunk_size = 1024*1024
with open(join(root_dir, folder, parts[-1]), 'wb') as f:
    for chunk in response.iter_content(chunk_size):
        f.write(chunk)