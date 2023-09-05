from TextLogoMerger import TextLogoToImage,Convert2PNG,Convert2JPG

import os

if __name__ == "__main__":
    images = os.listdir("Pictures")

    for img in images:
        ext = img.split(".")[-1]
        img_path = f"Pictures/{img}"
        if ext != "jpg":
            Convert2JPG(img_path)
            img_path = f"JPG/{img.split('.')[0]}.jpg"
        
        TextLogoToImage("Custom Text",img_path,watermark=True)

