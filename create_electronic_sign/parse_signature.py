from PIL import Image
import numpy as np
import argparse
import os

def read_img(img_path):
    image = Image.open(img_path)
    image = image.convert('RGBA')
    size = image.size
    image = np.array(image)
    return size, image

def get_elesign(size, image):
    """
    signature is black, RGB near 0
    """
    points = []
    for j in range(size[0]):
        for i in range(size[1]):
            if image[i][j][0]>100 and image[i][j][1]>100 and image[i][j][2]>100:
                image[i][j][3] = 0
            else:
                image[i][j][0], image[i][j][1], image[i][j][2] = 0,0,0
                points.append((i,j))
    return points, image

def clip_image(points, image, save_path, offset=5):
    points = np.array(points).reshape((-1,2))
    min_value = np.min(points, axis=0)
    x1,y1 = min_value[0]-offset, min_value[1]-offset
    max_value = np.max(points, axis=0)
    x2,y2 = max_value[0]+offset, max_value[1]+offset
    sign_area = image[x1:x2, y1:y2]
    sign_area = Image.fromarray(sign_area)
    sign_area.save(save_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a digital handwriting signature. By Roundofthree.")
    parser.add_argument("--image_path", type=str, help="Source image location")
    parser.add_argument("--offset", type=int, default=5, help="Border size")
    arg = parser.parse_args()
    user_give = arg.image_path
    offset = arg.offset
    if os.path.isdir(user_give):
        imgs_name = os.listdir(user_give)
        for i,name in enumerate(imgs_name):
            if os.path.splitext(name)[-1] in [".jpeg",".JPG",".PNG",".jpg",".png"]:
                basename = os.path.splitext(name)[0]
                img_path = os.path.join(user_give,name)
                save_path = "sign_" + basename + "_%d.png"%i
                size, image = read_img(img_path)
                points, image = get_elesign(size, image)
                clip_image(points, image, save_path, offset)
    elif os.path.isfile(user_give):
        img_path = user_give
        save_path = "sign.png"
        size, image = read_img(img_path)
        points, image = get_elesign(size, image)
        clip_image(points, image, save_path, offset)
