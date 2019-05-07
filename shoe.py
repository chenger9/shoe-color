from PIL import Image
from pylab import *

shoe = array(Image.open("shoe.jpg"))

a = 0
b = 0
c = 0
d = 96 * 96

for i in range (95):
    for j in range (95):
        a += shoe[i, j][0]
        b += shoe[i, j][1]
        c += shoe[i, j][2]

print(int(a/d),int(b/d),int(c/d))

