import requests
from bs4 import BeautifulSoup
import sys

URL = 'https://browser.geekbench.com/processor-benchmarks'
res = requests.get(URL)

if res.status_code !=200:
    sys.exit(1)

soup = BeautifulSoup(res.content, 'html.parser')

all_tds = soup.find_all('td', {'class': 'name'})
cpu_names = []
for td in all_tds:
    cpu_names.append(td.find('a').text)

with open('cpus.txt', 'w') as fh:
    for cpu in cpu_names:
        fh.write(cpu)
