import time
import concurrent.futures
import os
from PIL import Image, ImageFilter


img_names = []
for names_imgs in os.listdir("./imgs"):
    img_names.append("imgs/" + names_imgs)

t1 = time.perf_counter()

size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f"processed/{img_name.replace('imgs/','')}")
    print(f"{img_name} was processed...")


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


t2 = time.perf_counter()

print(f"Finished in {t2-t1} seconds")
