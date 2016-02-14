import urllib.request
from PIL import Image, ImageDraw

SOURCE_IMAGE = r'http://www.pythonchallenge.com/pc/def/oxygen.png'
DELTA = 7

def download_image():
    with urllib.request.urlopen(SOURCE_IMAGE) as fin, open('image.png', 'wb') as fout:
        fout.write(fin.read())

def main():
    coords = (0, 47)
    # Download image first. Uncheck to actually do it (not needed every time).
    # download_image()

    # Open image
    im = Image.open('image.png')

    for i in range(0, im.size[0], DELTA):
        # Update coords
        coords = (i, 47)

        # Get pixel value
        values = im.getpixel(coords)
        print(chr(values[0]), end='')

    # Decode the rest of the values
    print()
    print('Final:')
    lettersList = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    for letter in lettersList:
        print(chr(letter), end='')

if __name__ == '__main__':
    main()
