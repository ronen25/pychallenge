import urllib.request
import re

SOURCE_URL = '''http://www.pythonchallenge.com/pc/def/equality.html'''
FILTER_CHARS = '!@#$%^&*()_=+-{}[]\n'
PATTERN = re.compile('<!--.*-->.*<!--(.*)-->', re.MULTILINE | re.DOTALL)
LETTER_PATTERN = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', re.MULTILINE | re.DOTALL)

finalResult = ''

def download_page():
    data = None
    
    with urllib.request.urlopen(SOURCE_URL) as r:
        data = r.read()

    return data.decode('utf-8')

def print_letters(data):
    global finalResult
    
    # Clean HTML stuff
    cleanedData = PATTERN.search(data).groups(1)[0]

    # Find three bodyguards around letters
    for result in LETTER_PATTERN.findall(cleanedData):
        finalResult += result

def main():
    print_letters(download_page())

    print('Final result:')
    print(finalResult)

    print('Final URL:')
    print('http://www.pythonchallenge.com/pc/def/linkedlist.html')

if __name__ == '__main__':
    main()
