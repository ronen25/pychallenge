import urllib.request
import pickle

SOURCE = r'http://www.pythonchallenge.com/pc/def/banner.p'

def main():
    # Get data in binary form
    with urllib.request.urlopen(SOURCE) as r:
        data = r.read()

    coords = pickle.loads(data)

    # Go through and print everything
    for l in coords:
        for c, times in l:
            for i in range(0, times):
                print(c, end='')
        print()

    print('Final URL:')
    print(r'http://www.pythonchallenge.com/pc/def/channel.html')

if __name__ == '__main__':
    main()
