import re
import zipfile
from collections import defaultdict

SOURCE = r'C:\Users\Tmicha\Downloads\channel\{}.txt'
FILE_SOURCE = '{}.txt'
PATTERN = re.compile('(\d+)', re.MULTILINE | re.DOTALL)
FIRST_NUMBER = '90052'

# NOTE: FIRST NUMBER IS 90052.
# After solving, solve the small riddle to receive this:
# http://www.pythonchallenge.com/pc/def/oxygen.html

def main():
    number = FIRST_NUMBER
    comments = ''
    
    # Open zip
    with zipfile.ZipFile(r'C:\Users\Tmicha\Downloads\channel.zip') as zf:
        try:
            while True:
                filename = FILE_SOURCE.format(number)
                
                with zf.open(filename) as f:
                    print('Visiting {}...'.format(number))
                    fullData = f.read().decode('utf-8')
                        
                    # Get page number
                    result = PATTERN.search(fullData)
                    number = result.groups(1)[0]

                    # Get file comment
                    info = zf.getinfo(filename)
                    comments += info.comment.decode('utf-8')
        except:
            print(comments)

    # Print
    print('Final URL:')
    print(r'http://www.pythonchallenge.com/pc/def/hockey.html')

if __name__ == '__main__':
    main()
