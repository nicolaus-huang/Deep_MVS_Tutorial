import cv2
import glob
# All files ending with .txt
image_list = glob.glob("/mnt/PatchmatchNet/original/outputs_2/images/*.jpg")
for image_file in image_list:
    img = cv2.imread(image_file, cv2.IMREAD_UNCHANGED)
    width = 2400
    height = 1350
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print(img.shape)
    cv2.imwrite(image_file, resized)