import urllib.request
import bz2
from PIL import Image, ImageDraw

USERNAME = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
PASSWORD = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

def main():
    decomp = bz2.BZ2Decompressor()
    passDecomp = bz2.BZ2Decompressor()
    
    print('Username: ')
    print(decomp.decompress(USERNAME))
    print('Password: ')
    print(passDecomp.decompress(PASSWORD))

    # Print final url
    print('Final URL:')
    print('http://www.pythonchallenge.com/pc/return/good.html')

if __name__ == '__main__':
    main()
