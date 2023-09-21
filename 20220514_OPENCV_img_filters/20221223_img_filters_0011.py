import cv2
# import matplotlib.pyplot as plt
import math

INPUTFILE_PATH = "/home/user7/TEST_IMAGE.jpg"
OUTPUT_PATH = "/OUTPUT/" + INPUTFILE_PATH.split('/')[-2].split(".")[0] + "_001.jpg"
INIT_IMG = cv2.imread(INPUTFILE_PATH)
# INIT_IMG = cv2.cvtColor(INIT_IMG, cv2.COLOR_BGR2RGB)

out_img = INIT_IMG.copy()

def img_colorshift_area(img, colorshift=20, area='Bright'):
    OUTPUT_IMG = img.copy()

    if area == 'Dark':
        mask = img < colorshift
        OUTPUT_IMG[mask] = OUTPUT_IMG[mask] + math.floor((1*colorshift))
    elif area == 'Bright':
        colorshift = 255 - colorshift
        mask = img > colorshift
        OUTPUT_IMG[mask] = OUTPUT_IMG[mask] + math.floor((1*colorshift))
    else:
        return 
    
    return OUTPUT_IMG

FVAL = 0
while FVAL < 256:
    out_img = img_colorshift_area(INIT_IMG,FVAL)
    print(f'OUTPUT/FVAL-{FVAL}.jpg')
    cv2.imwrite(f'20220514_OPENCV_img_filters/OUTPUT/img_colorshift_area.area-Bright_colorshift-{FVAL}.jpg', out_img)
    FVAL += 5
