from PIL import Image, ImageStat
import os

def getRGB_Average(path):
    r, b, g = [], [], []
    image = Image.open(path)
    rgb_im = image.convert('RGB')
    for x in range(rgb_im.width):
        for y in range(rgb_im.height):
            rgb = rgb_im.getpixel((x,y))
            r.append(rgb[0])
            g.append(rgb[1])
            b.append(rgb[2])
    r_mean = round(sum(r) / len(r))
    g_mean = round(sum(g) / len(g))
    b_mean = round(sum(b) / len(b))
    print(r_mean, g_mean, b_mean, imagename)
    return r_mean, g_mean, b_mean

if __name__ == '__main__':
    paths = {
        'forest': './Pics/forest/',
        'field': './Pics/field/',
        'lake': './Pics/lake/',
        'mountain': './Pics/mountain/',
    }

    with (open('dataset.csv', 'w')) as dataset:
        for path in paths.values():
            for imagename in os.listdir(path):
                r, b, g = [], [], []
                image = Image.open(path + "/" + imagename)
                rgb_im = image.convert('RGB')
                for x in range(rgb_im.width):
                    for y in range(rgb_im.height):
                        rgb = rgb_im.getpixel((x,y))
                        r.append(rgb[0])
                        g.append(rgb[1])
                        b.append(rgb[2])
                r_mean = round(sum(r) / len(r))
                g_mean = round(sum(g) / len(g))
                b_mean = round(sum(b) / len(b))
                print(r_mean, g_mean, b_mean, imagename)
                dataset.write(f'{path.split("/")[-2]};{r_mean};{g_mean};{b_mean}\n')

