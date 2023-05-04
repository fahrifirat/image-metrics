import cv2
import numpy as np


from PIL import Image, ImageDraw, ImageFont

# this code takes frames for making video
# gets 400x400 images from 3 different images (1024x1024) and puts them side by side. then adds text to each image.

img1 = cv2.imread("  ")
img2 = cv2.imread(" ")
img3 =cv2.imread("  ")



# adds line between
line = 255 * np.ones((400, 5, 3), dtype=np.uint8)


output_path="frames/"




for x in range(623):
        # gets frames
        side_by_side = cv2.hconcat([img1[:400, 0+x:x+400], line ,img2[:400, 0+x:x+400], line, img3[:400, 0+x:x+400]])
        filename = f"frames/{x:03}.png" 
        cv2.imwrite(filename, side_by_side)


        # adds texts
#         background_image = Image.open(f'frames/{x:03}.png')
#         text_image = Image.new('RGB', (90, 40), color='black')
#         draw = ImageDraw.Draw(text_image)
#         font = ImageFont.truetype('arial.ttf', 24)
#         text = 'HR'
#         text_size = draw.textsize(text, font=font)
#         position = ((text_image.width - text_size[0]) // 2, (text_image.height - text_size[1]) // 2)
#         draw.text(position, text, font=font, fill='white')
#         background_image.paste(text_image, (150, 10))


#         text_image2 = Image.new('RGB', (90, 40), color='black')
#         draw = ImageDraw.Draw(text_image2)
#         font = ImageFont.truetype('arial.ttf', 24)
#         text2 = '3As'
#         text_size = draw.textsize(text2, font=font)
#         position = ((text_image.width - text_size[0]) // 2, (text_image.height - text_size[1]) // 2)
#         draw.text(position, text2, font=font, fill='white')
#         background_image.paste(text_image2, (555, 10))

#         text_image3 = Image.new('RGB', (90, 40), color='black')
#         draw = ImageDraw.Draw(text_image3)
#         font = ImageFont.truetype('arial.ttf', 24)
#         text3 = 'EFM'
#         text_size = draw.textsize(text3, font=font)
#         position = ((text_image.width - text_size[0]) // 2, (text_image.height - text_size[1]) // 2)
#         draw.text(position, text3, font=font, fill='white')
#         background_image.paste(text_image3, (960, 10))

# # 
#         background_image.save(f'frames/{x+623:03}.png')       



        # cv2.imshow("", side_by_side)
        # cv2.waitKey(10)

print("done")
