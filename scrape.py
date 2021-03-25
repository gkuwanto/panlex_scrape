from sys import argv
import bs4
import requests as req
from tqdm import tqdm

# Get Arguments
if len(argv)<3:
    print("Usage: python scrape.py <language-code-1> <language-code-2>")
    exit()
source_lang_code = argv[1]
target_lang_code = argv[2]


# HTTP Request
page = 1
res = req.get(f'https://vocab.panlex.org/{source_lang_code}/{target_lang_code}?page={page}')
web_page = bs4.BeautifulSoup(res.text, features='lxml')

# Get Number of Pages
last_page = int(web_page.find_all('a')[-1].text)

# Parsing Row
def parse(row):
    if row.find('details'):
        source = row.find('td').text.strip()
        targets = (str(row.find('details').find('summary').text).strip())
    else:
        source, target = row.find_all('td')
        source = source.text.strip()
        targets = target.text.strip()
    return source, targets

# Loop over all Pages
word_list = []
for i in tqdm(range(page, last_page+1)):
    res = req.get(f'https://vocab.panlex.org/{source_lang_code}/{target_lang_code}?page={i}')
    web_page = bs4.BeautifulSoup(res.text, features='lxml')
    word_list += [parse(row) for row in web_page.find('tbody').find_all('tr')]

# Create File
with open(f'{source_lang_code}-{target_lang_code}.dict', 'w+') as f:
    for a, b in word_list:
        if len(b.strip())>0:
            print(f'{a}\t{b}', file=f)