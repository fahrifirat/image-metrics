import os
import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np



    # Load the high-resolution, downsampled, and super-resoluted images
hr_folder = 'hr/'
sr_folder = 'sr/'
lr_folder = 'lr/'
    # Calculate the PSNR of the high-resolution and super-resoluted images

i=0
total_psnr=0
total_ssim=0




for hr_img in os.listdir(hr_folder):


    hr_path = os.path.join(hr_folder, hr_img)

    #change sr image names accordingly (i.e:1.png for hr and lr,  1_sr.png)
    sr_path = os.path.join(sr_folder, hr_img.replace('.png', '_sr.png'))
   
    name_path = os.path.join(hr_folder, hr_img.replace('.png', ''))
    
    hr_img = cv2.imread(hr_path)
    sr_img = cv2.imread(sr_path)
   

 

   
    
    psnr = cv2.PSNR(hr_img, sr_img)
    ssim_val = ssim(hr_img, sr_img, multichannel=True)
   
    print(f'image: {name_path}, PSNR: {psnr:.2f}, SSIM: {ssim_val:.2f}')

    total_psnr=total_psnr+psnr
    total_ssim=total_ssim+ssim_val
 
    i=i+1
    

avg_psnr=total_psnr/i
avg_ssim=total_ssim/i


print(f'avg psnr: {avg_psnr:.2f}, avg ssim: {avg_ssim:.2f}')   
 