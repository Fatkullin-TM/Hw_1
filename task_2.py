# -*- coding: utf-8 -*-

"""
Программа делает копию изображения (file_name), преобразует копию в оттенки
серого и сохраняет результат в той же директории.

"""

import numpy as np
from scipy.misc import imread, imsave

# %% объявление функций

def image_to_grey (name: str):
    """
    Функция преобразует цветное изображение (name) в оттенки серого.
    
    """
    
    assert ('' != name)
    
    img = imread(name=name)
    img_grey = np.zeros(img.shape[:2])
    
    vector_coeff = np.array([0.299, 0.587, 0.114])
    for i in range(3):
        img_grey += vector_coeff[i] * img[:, :, i]
        
    return img_grey

# %% тело программы

if __name__ == '__main__':
    
    file_name = 'Korolev_Martian crater.jpg'
    imsave(file_name[:-4] + '_grey' + file_name[-4:],
           image_to_grey(name=file_name))