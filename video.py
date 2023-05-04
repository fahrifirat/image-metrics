import cv2
import os

# set the folder path containing the images
folder_path = "frames/"

# get a list of all image files in the folder
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')]

# sort the image files by filename (assuming filenames are numbered in sequence)
image_files = sorted(image_files, key=lambda x: int(x.split('/')[-1].split('.')[0]))

# set video parameters (codec, resolution, and FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
resolution = (1210, 400)
fps = 60

# initialize the video writer object
video_writer = cv2.VideoWriter('video output/output.mp4', fourcc, fps, resolution)

# loop through each image and write it to the video writer object
for image_file in image_files:
    img = cv2.imread(image_file)
    video_writer.write(img)

# release the video writer object to save the video file
video_writer.release()
print("done")