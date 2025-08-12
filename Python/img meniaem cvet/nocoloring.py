import numpy as np
from PIL import Image
temp = Image.open('vremennaia.jpg').convert("RGB")
image = np.array(temp)
for i in range(len(image)):
    for j in range(len(image[i])):
        t = image[i][j][0] + image[i][j][1] + image[i][j][2]
        tcolor = t/3
        image[i][j][0] = tcolor
        image[i][j][1] = tcolor
        image[i][j][2] = tcolor
        t = 0
        print(image[i][j])