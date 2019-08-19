from PIL import Image
import pytesseract

s = pytesseract.image_to_string("test.png").strip()
print(s)
x = [0]*2
if (s[s.find('+')] == '+'):
    x=list(map(int,s.split('+')))
    print(x[0]+x[1])
if (s[s.find('-')] == '-'):
    x=list(map(int,s.split('-')))
    print(x[0]-x[1])
if (s[s.find('*')] == '*'):
    x=list(map(int,s.split('*')))
    print(x[0]*x[1])
if (s[s.find('/')] == '/'):
    x=list(map(int,s.split('/')))
    print(x[0]/x[1])
