# import matplotlib.pyplot as plt
import math
import cv2

INPUTFILE_PATH = "/home/user7/TEST_IMAGE.jpg"
OUTPUT_PATH = "/OUTPUT/" + INPUTFILE_PATH.split('/')[-2].split(".")[0] + "_001.jpg"
INIT_IMG = cv2.imread(INPUTFILE_PATH)
# INIT_IMG = cv2.cvtColor(INIT_IMG, cv2.COLOR_BGR2RGB)

out_img = INIT_IMG.copy()

def img_colorshift_area (img, colorshift=20.0, area='DARK'):
    """shift color values in bright or dark areas of an image with Numpy

    Args:
        img (ndarray): image to process
        colorshift (float, optional): Choose max of pixel value to shift.   For best try 0< colorshift < 50-100.       Defaults to 20.0.
        area (str, optional):'DARK'' to process from dark pixels to brighter.
                                            'BRIGHT' to process from bright pixels to darker. 

    Returns:
        ndarray: image with shifted pixels in area of max _colorshift
    """
    _area = area.upper()
    if colorshift < -100 or colorshift> 100:
        return img
    else:
        _colorshift = math.floor( colorshift*0.01*255)           #(0,100) normalized to (0,255)
        _output_img = img.copy()
            
    if _area == 'DARK':
        mask = img < _colorshift%255
        _output_img[mask] = _output_img[mask] - math.floor((1*_colorshift))
    elif _area == 'BRIGHT':
        _colorshift = (255 - _colorshift)%255
        mask = img > _colorshift
        _output_img[mask] = _output_img[mask] + math.floor((1*_colorshift))
    else:
        return

    return _output_img

def img_blur(img,ksize=10):
    """blur image with OpenCv

    Args:
        img (ndarray): image to process
        ksize (int, optional): Kernel size of blured pixels. For best try:   0 < ksize < 50-100.     Defaults to 10.

    Returns:
        ndarray: blurred image
    """
    if  ksize >= -2 and ksize <=2:
        return img
    else:
        if ksize <-100 or ksize>100: 
            _output_img = img.copy()
            _ksize = 100
        else:
            _output_img = img.copy()
            _ksize= (ksize/4).__abs__().__round__()
    
    _output_img= cv2.blur(_output_img,  (_ksize, _ksize))
    
    return _output_img


def img_get_red_channel(img):
    """_summary_

    Args:
        img (ndarry): image to process
    """
    
    

#---------------------------------------------------------------------------------#
# while True:
#     VALUE_01 = int(input('Give VALUE_01 . -100 < VALUE_01 < +100 : \t\t'))
#     out_img = img_colorshift_area(INIT_IMG, VALUE_01)
#     print(VALUE_01)

    
#     # VALUE_01 = VALUE_01
#---------------------------------------------------------------------------------#

VALUE_01 = -100

while VALUE_01 < 100:
    out_img = img_colorshift_area(INIT_IMG,VALUE_01)
    # cv2.imwrite(f'20220514_OPENCV_img_filters/OUTPUT/img_colorshift_area_area-DARK_colorshift-{VALUE_01}.jpg', out_img)
    # out_img = img_blur(INIT_IMG, ksize=VALUE_01)
    # cv2.imwrite(f'20220514_OPENCV_img_filters/OUTPUT/AAA_img_blur_ksize-{VALUE_01}.jpg', out_img)

    VALUE_01 += 5
