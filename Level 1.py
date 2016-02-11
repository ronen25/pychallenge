preTranslatedText = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
lmu ynnjw ml rfc spj.
'''

SOURCE_URL = '''http://www.pythonchallenge.com/pc/def/map.html'''

transTable = preTranslatedText.maketrans(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB')

print(preTranslatedText.translate(transTable))

print("URL:")
print(SOURCE_URL.translate(transTable))

print('Final URL: ')
print('http://www.pythonchallenge.com/pc/def/ocr.html')
