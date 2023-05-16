import os
import cv2
import numpy as np



#takes patch from each image and puts them side by side



hr_folder = 'hr/'
sr_folder = 'sr/'
lr_folder = 'lr/'
output_folder='cat/'

for hr_img in os.listdir(hr_folder):


    hr_path = os.path.join(hr_folder, hr_img)
    sr_path = os.path.join(sr_folder, hr_img.replace('.png', '_sr.png'))
    lr_path = os.path.join(lr_folder, hr_img)
    output_path = os.path.join(output_folder, hr_img)
    
    hr_img = cv2.imread(hr_path)
    sr_img = cv2.imread(sr_path)
    lr_img= cv2.imread(lr_path)


#4x umpsamples lr image
    upsampled_img = cv2.resize(lr_img, None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST)

    h, w, c = hr_img.shape

    line = 255 * np.ones((h-624, 5, c), dtype=np.uint8)

    side_by_side = cv2.hconcat([hr_img[:h-624, :w-624], line ,upsampled_img[:h-624, :w-624], line, sr_img[:h-624, :w-624]])

    
    cv2.imwrite(output_path, side_by_side)



