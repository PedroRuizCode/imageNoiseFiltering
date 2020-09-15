'''         Image processing and computer vision
              Alejandra Avendaño y Pedro Ruiz
               Electronic engineering students
              Pontificia Universidad Javeriana
                      Bogotá - 2020
'''
import cv2 #import openCV library
import numpy as np #import numpy library
class noise: #Create the class
    def noisy(self, noise_typ, image): #create the method noisy
        if noise_typ == "gauss": #The input is gauss
            row,col,ch= image.shape #Save image size data
            mean = 0 #Assign a value to the mean
            var = 0.5 #Assign a value to the variance
            sigma = var**0.5 #Sigma calculation
            gauss = np.random.normal(mean,sigma,(row,col,ch)) #Generate random data with normal distribution
            gauss = gauss.reshape(row,col,ch) #Reorder data
            noisy_gauss = image + gauss #Generate the noisy image
            return noisy_gauss #Return the noisy image
        elif noise_typ == "s&p": #The input is s&p
            #row,col,ch = image.shape #Save image size data
            s_vs_p = 0.5 #salt to pepper ratio
            amount = 0.004 #Number of points to number of pixels ratio
            out = np.copy(image) #Create a copy of the original image
            # Salt mode
            num_salt = np.ceil(amount * image.size * s_vs_p) #Number of points
            coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape] #Coordinates for salt
            out[tuple(coords)] = 1 #Salt is 1
            # Pepper mode
            num_pepper = np.ceil(amount* image.size * (1. - s_vs_p)) #Number of points
            coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape] #Coordinates for pepper
            out[tuple(coords)] = 0 #Salt is 0
            return out #Return the noisy image

    def show(self, Im_original, Im_noisy, Im_filt): #create the method show
        emc = np.sum((Im_original.astype('float') - Im_filt.astype('float')) ** 2) #Summation of the EMC equation
        emc /= float(Im_original.shape[0] * Im_original.shape[1]) #Division of the EMC equation
        semc = np.sqrt(emc) #Square root of EMC
        image_noise_r = np.abs(Im_noisy - Im_original) #Generated noise
        image_noise = np.abs(Im_noisy - Im_filt) #Estimated noise
        print('The square root of the EMC is: ', semc) #Print the square root of the EMC
        cv2.imshow('Original', Im_original) #Show original image
        cv2.imshow('Noisy', Im_noisy) #Show noisy image
        cv2.imshow('Filtered', Im_filt) #Show filtered image
        cv2.imshow('Real noise', image_noise_r) #Show real noise
        cv2.imshow('Noise estimation', image_noise) #Show estimated noise
        #To save the images uncomment the following 5 lines and adjust the path
        #cv2.imwrite('C:/Users/pedro.ruiz/Documents/GitHub/imageNoiseFiltering/original.png', Im_original)
        #cv2.imwrite('C:/Users/pedro.ruiz/Documents/GitHub/imageNoiseFiltering/noisy.png', Im_noisy)
        #cv2.imwrite('C:/Users/pedro.ruiz/Documents/GitHub/imageNoiseFiltering/filtered.png', Im_filt)
        #cv2.imwrite('C:/Users/pedro.ruiz/Documents/GitHub/imageNoiseFiltering/noiReal.png', image_noise_r)
        #cv2.imwrite('C:/Users/pedro.ruiz/Documents/GitHub/imageNoiseFiltering/noiEst.png', image_noise)
        cv2.waitKey(0) #Indefinite delay to display images