import numpy as np
from PIL import Image
temp = Image.open('Naruto_r2.png').convert("RGB")
image = np.array(temp)
r = 0
g = 0
b = 0
blured = []
for i in range(len(image)):
    if (i % 2 == 1):continue
    else:
        iblu = []
        for j in range(len(image[i] )- 1):
            if (j % 2 == 1):continue
            else:
                r = (int(image[i][j][0]) + int(image[i][j+1][0]) + int(image[i+1][j][0]) + int(image[i+1][j+1][0]))//4
                g = (int(image[i][j][1]) + int(image[i][j+1][1]) + int(image[i+1][j][1]) + int(image[i+1][j+1][1]))//4
                b = (int(image[i][j][2]) + int(image[i][j+1][2]) + int(image[i+1][j][2]) + int(image[i+1][j+1][2]))//4
                iblu.append([r, g, b])
        blured.append(iblu)

# Ниже уже делаем серым

for i in range(len(blured)):
    for j in range(len(blured[i])):
        t = image[i][j][0] + blured[i][j][1] + blured[i][j][2]
        tcolor = t/3
        blured[i][j][0] = tcolor
        blured[i][j][1] = tcolor
        blured[i][j][2] = tcolor
        t = 0

# Ниже заменяю на символы

last = []
for n in range(len(blured)):
    fix_err = []
    for o in range(len(blured[n])):
        blured[n][o][0] = int(blured[n][o][0] / 255 * 68 // 1)
        fix_err.append(blured[n][o][0])
    last.append(fix_err)

s_mas = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^'. "

for h1 in range(len(last)):
    for h2 in range(len(last[h1])):
        for h3 in range(len(s_mas)):
            if (last[h1][h2] == h3):
                last[h1][h2] = s_mas[h3]
for rn in range(len(last)):
    print(last[rn])