import urllib.request
import re

# NOTE: FIRST NUMBER IS 12345.
# After that, the loop stops at 16044. After that, next number is 8022.
# After 82683 we must go back to 82682 to find out that the correct
# number is 63579.
# Loop then finally stops at 66381

SOURCE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
PATTERN = re.compile('(\d+)', re.MULTILINE | re.DOTALL)
FIRST_NUMBER = '63579'

def main():
    number = FIRST_NUMBER
    
    while True:
        # Get page data
        with urllib.request.urlopen(SOURCE_URL.format(number)) as r:
            print('Visiting {}...'.format(number))
            fullData = r.read().decode('utf-8')
            
        # Get page number
        result = PATTERN.search(fullData)
        number = result.groups(1)[0]

    print('Final URL: ')
    print('http://www.pythonchallenge.com/pc/def/peak.html')

if __name__ == '__main__':
    main()
