from PIL import Image,ImageDraw,ImageFont
import os 

# Text Logo To Image
def TextLogoToImage(text:str,image_path:str,second_text:str="t.me/Join_KingZ",font_name:str="chant___.ttf",font_link_name:str="FrontPageNeue.otf",font_size_auto:bool=True,font_size:int=80,position:str="right bottom",save:bool=True,folder_name_for_finished:str="Finished",color:tuple=(255,255,255),watermark=True):
    position_options = ["left top","left bottom","right top","right bottom","center","center left","center right","center top","center bottom"]
    if position in position_options:
        try: 
            img = Image.open(image_path)

            width,height = img.size

            draw = ImageDraw.Draw(img)

            if font_size_auto == False:
                font = ImageFont.truetype(font_name,font_size)
                font_link = ImageFont.truetype(font_link_name,font_size - int(font_size / 4))
            
            font = ImageFont.truetype(font_name,int(width / 12))
            font_link = ImageFont.truetype(font_link_name,int(width / 32))

            text_w , text_h = draw.textsize(text,font)      
            text_link_w , text_link_h = draw.textsize(second_text,font_link)

            link_x = 10
            link_y = height - text_link_h - 8

            if position == "left top":
                x = 10
                y = 0

            elif position == "left bottom":
                x = 10
                y = height - text_h - 15

            elif position == "right top":
                x = width - text_w - 15
                y = 0
                
            elif position == "right bottom":
                x = width - text_w - 10
                y = height - text_h - 15

            elif position == "center":
                x = width / 2 - (text_w / 2)
                y = height / 2 - (text_h / 2)

            elif position == "center top":
                x = width / 2 - (text_w / 2)
                y = 0
                
            elif position == "center bottom":
                x = width / 2 - (text_w / 2)
                y = height - text_h - 10

            elif position == "center left":
                x = 10
                y = height / 2 - (text_h / 2)

            elif position == "center right":
                x = width - text_w - 10
                y = height / 2 - (text_h / 2)

            else:
                return "NO_OPTION"

            if watermark == True:
                draw.text((x,y),text,font=font,fill=color)
                draw.text((link_x,link_y),second_text,font=font_link,fill=color)

            if save:
                img_info = image_path.split(".")
                i = img_info[0].split("/")[-1]
                
                if not os.path.exists(f"./{folder_name_for_finished}"):
                    os.mkdir(f"./{folder_name_for_finished}")
                
                if watermark == False:
                    name = f"./{folder_name_for_finished}/{i}.{img_info[1]}"
                else:
                    name = f"./{folder_name_for_finished}/{i}_watermarked.{img_info[1]}"
                img.save(name)
                print(f"{folder_name_for_finished}/{i}_watermarked.{img_info[1]}")
            else:
                img.show()
        
        except Exception as e:
            print("Error")  
            print(e)  

    else:
        print(f"Error please use these keywords to positions : {position_options}")


# Convert Webp To PNG
def Convert2PNG(input_file):
    img = Image.open(input_file)
    new_ = img.convert("RGBA")
    ext = "png"
    info = input_file.split("/")[-1].split(".")
    name = info[0]

    if not os.path.exists("./PNG"):
        os.mkdir("./PNG")

    print(new_.mode)
    new_.save(f"./PNG/{name}.{ext}")

# Convert Webp To JPG
def Convert2JPG(input_file):
    img = Image.open(input_file)
    new_ = img.convert("RGB")
    ext = "jpg"
    info = input_file.split("/")[-1].split(".")
    name = info[0]

    if not os.path.exists("./JPG"):
        os.mkdir("./JPG")

    print(new_.mode)
    new_.save(f"./JPG/{name}.{ext}")


if __name__ == "__main__":
    print("TextLogoMerger Custom Module")
