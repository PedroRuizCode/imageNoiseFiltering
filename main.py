'''         Image processing and computer vision
              Alejandra Avendaño y Pedro Ruiz
               Electronic engineering students
              Pontificia Universidad Javeriana
                      Bogotá - 2020
'''
import cv2 #import openCV library
import numpy as np #import numpy library
from time import time #import time library
from noise import * #import noise class
if __name__ == '__main__':
    path = 'C:/Users/pedro.ruiz/Documents/GitHub/imageNoiseFiltering/lena.png' #path of the ubication of the image
    image = cv2.imread(path) #Save the image in 'image'
    a = noise() #call noise class
    gen_noise = input('What kind of noise do you want to generate? The options are: gauss and syp ')#Ask ...
    #... for noise type
    if gen_noise == 'gauss': #The input is gauss
        lena_gauss_noisy = a.noisy("gauss", image).astype(np.uint8) #call function and save
        filt = input('What filter do you want to use? Options are: gaussian, median, bilateral, and nlm ')#Ask...
        #... for filter type
        if filt == 'gaussian': #The input is gaussian
            ti = time() #Current time
            image_gauss_gauss = cv2.GaussianBlur(lena_gauss_noisy, (7, 7), 1.5, 1.5) #Gaussian filtering
            tf = time() #Current time
            tt = tf - ti #Total time
            print('The filter execution time is: ', tt,' ms') #Print execution time
            a.show(image, lena_gauss_noisy, image_gauss_gauss) #Call function to show processed images
        elif filt == 'median': #The input is median
            ti = time() #Current time
            image_gauss_median = cv2.medianBlur(lena_gauss_noisy, 7) #Filtering by median method
            tf = time() #Current time
            tt = tf - ti #Total time
            print('The filter execution time is: ', tt,' ms') #Print execution time
            a.show(image, lena_gauss_noisy, image_gauss_median) #Call function to show processed images
        elif filt == 'bilateral': #The input is bilateral
            ti = time() #Current time
            image_gauss_bilateral = cv2.bilateralFilter(lena_gauss_noisy, 15, 25, 25) #Bilateral filtering
            tf = time() #Current time
            tt = tf - ti #Total time
            print('The filter execution time is: ', tt,' ms') #Print execution time
            a.show(image, lena_gauss_noisy, image_gauss_bilateral) #Call function to show processed images
        elif filt == 'nlm': #The input is nlm
            ti = time() #Current time
            image_gauss_nlm = cv2.fastNlMeansDenoising(lena_gauss_noisy, 5, 15, 25) #NLM filtering
            tf = time() #Current time
            tt = tf - ti #Total time
            print('The filter execution time is: ', tt,' ms') #Print execution time
            a.show(image, lena_gauss_noisy, image_gauss_nlm) #Call function to show processed images
        else: #The input is another
            print('Invalid input') #Print string
    elif gen_noise == 'syp': #The input is syp
        lena_sp_noisy = a.noisy("s&p", image).astype(np.uint8) #call function and save
        filt = input('What filter do you want to use? Options are: gaussian, median, bilateral, and nlm ')#Ask...
        #... for filter type
        if filt == 'gaussian': #The input is gaussian
            ti = time() #Current time
            image_sp_gauss = cv2.GaussianBlur(lena_sp_noisy, (7, 7), 1.5, 1.5) #Gaussian filtering
            tf = time() #Current time
            tt = tf - ti #Total time
            print('The filter execution time is: ', tt,' ms') #Print execution time
            a.show(image, lena_sp_noisy, image_sp_gauss) #Call function to show processed images
        elif filt == 'median': #The input is median
            ti = time() #Current time
            image_sp_median = cv2.medianBlur(lena_sp_noisy, 7) #Filtering by median method
            tf = time() #Current time
            tt = tf - ti #Total time
            print('The filter execution time is: ', tt,' ms') #Print execution time
            a.show(image, lena_sp_noisy, image_sp_median) #Call function to show processed images
        elif filt == 'bilateral': #The input is bilateral
            ti = time() #Current time
            image_sp_bilateral = cv2.bilateralFilter(lena_sp_noisy, 15, 25, 25) #Bilateral filtering
            tf = time() #Current time
            tt = tf - ti #Total time
            print('The filter execution time is: ', tt,' ms') #Print execution time
            a.show(image, lena_sp_noisy, image_sp_bilateral) #Call function to show processed images
        elif filt == 'nlm': #The input is nlm
            ti = time() #Current time
            image_sp_nlm = cv2.fastNlMeansDenoising(lena_sp_noisy, 5, 15, 25) #NLM filtering
            tf = time() #Current time
            tt = tf - ti #Total time
            print('The filter execution time is: ', tt,' ms') #Print execution time
            a.show(image, lena_sp_noisy, image_sp_nlm) #Call function to show processed images
        else: #The input is another
            print('Invalid input') #Print string
    else: #The input is another
        print('Invalid input') #Print string