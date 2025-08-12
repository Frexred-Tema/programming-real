import numpy as np
from PIL import Image
temp = Image.open('vremennaia.jpg').convert("RGB")
image = np.array(temp)
r = 0
g = 0
b = 0
blured = []
for i in range(len(image)):
    if (i % 2 == 1):continue
    else:
        iblu = []
        for j in range(len(image[i])):
            if (j % 2 == 1):continue
            else:
                r = (int(image[i][j][0]) + int(image[i][j+1][0]) + int(image[i+1][j][0]) + int(image[i+1][j+1][0]))//4
                g = (int(image[i][j][1]) + int(image[i][j+1][1]) + int(image[i+1][j][1]) + int(image[i+1][j+1][1]))//4
                b = (int(image[i][j][2]) + int(image[i][j+1][2]) + int(image[i+1][j][2]) + int(image[i+1][j+1][2]))//4
                iblu.append([r, g, b])
        blured.append(iblu)

blured = np.array(blured)
blured = Image.fromarray(blured.astype(np.uint8)) 
blured.show()
        