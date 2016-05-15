a = [1, 11, 21, 1211, 111221, 312211, 13112221]
b = [1]

def look_and_say(num):
    result = ''
    count = 1
    i = 1
    _next = num[1]
    
    for c in num:
        if c == _next:
            count += 1
        else:
            result += '{}{}'.format(count, c)
            count = 1

        i += 1

        if i >= len(num):
            result += '{}{}'.format(count, _next)
            return result
        
        _next = num[i]

    return result

item = '11'
for i in range(0, 29):
    item = look_and_say(item)

print('Item length: {}'.format(len(item)))
print('FINAL URL: http://www.pythonchallenge.com/pc/return/5808.html')

