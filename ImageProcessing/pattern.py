import numpy as np
import cv2
from itertools import combinations

from PIL import Image

def testar(roi, template, imagem, report_path):
    resultado = False
    #print(template_path)
    #template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]

    roi_upper_left_x = roi[0]
    roi_upper_left_y = roi[1]
    roi_lower_right_x = roi[2]
    roi_lower_right_y = roi[3]

    ### GRAVAR TEMPLATE ###
    #cropped_image = imagem[roi_upper_left_y:roi_lower_right_y, roi_upper_left_x:roi_lower_right_x]
    #cv2.imshow('aaa',cropped_image)
    #cv2.imwrite(report_path+'cadeado_aberto.jpg', cropped_image)
    #######################

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(imagem_cinza, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        if (pt[0] >= roi_upper_left_x and pt[1] >= roi_upper_left_y and pt[0] + w <= roi_lower_right_x and pt[1] + h <= roi_lower_right_y):
            cv2.rectangle(imagem, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            resultado = True
            break
        else:
            resultado = False
    cv2.rectangle(imagem, (roi_upper_left_x, roi_upper_left_y), (roi_lower_right_x, roi_lower_right_y), (255, 0, 0),2)
    cv2.imwrite(report_path +'.jpg', imagem)

    return resultado