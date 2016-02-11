import urllib.request
import re

SOURCE_URL = '''http://www.pythonchallenge.com/pc/def/ocr.html'''
FILTER_CHARS = '!@#$%^&*()_=+-{}[]\n'
PATTERN = re.compile('<!--.*-->.*<!--(.*)-->', re.MULTILINE | re.DOTALL)

def download_page():
    data = None
    
    with urllib.request.urlopen(SOURCE_URL) as r:
        data = r.read()

    return data.decode('utf-8')

def clean_data(data):
    
    # Clean HTML stuff
    result = PATTERN.search(data)

    for c in result.groups(1)[0]:
        if c not in FILTER_CHARS:
            print(c, end=' ')

def main():
    data = clean_data(download_page())

    print('Final URL:')
    print('http://www.pythonchallenge.com/pc/def/equality.html')

if __name__ == '__main__':
    main()
