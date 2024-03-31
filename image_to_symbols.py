from PIL import Image

symbols = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

def image_to_ascii(img_path, width=100): 
    img = Image.open(img_path)

    wpercent = (width / float(img.size[0]))
    img_height = int((float(img.size[1]) * float(wpercent)) / 2) 
    img = img.resize((width, img_height), Image.NEAREST)
    img = img.convert('L')

    ascii_image = ""

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel_value = img.getpixel((x, y))
            symbol_index = pixel_value // 25 - 1  
            ascii_image += symbols[symbol_index]
        ascii_image += '\n'

    return ascii_image

image_path = "images/cool_emoji.png"  # Path to your image
width = 100 # Higher width = bigger image

print(image_to_ascii(image_path, width))
