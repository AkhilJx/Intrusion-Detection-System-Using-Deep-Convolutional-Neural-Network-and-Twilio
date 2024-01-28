# Intrusion-Detection-System-Using-Deep-Convolutional-Neural-Network-and-Twilio
DETECTION AND INTIMATION OF ANIMALS/BIRDS FROM LIVE VIDEOS TO AID THE FARMERS AND FOREST OFFICERS IN TAKING THE PRECAUTIONARY MEASURES TO PROTECT THEIR LIVES AND ASSETS

This Project was published on springer site ( https://link.springer.com/chapter/10.1007/978-981-19-8086-2_27 ) under the conference "Seventh International Conference on “Emerging Research in Computing, Information, Communication and Applications” - ERCICA – 2022, 25th & 26th February 2022"

# PROBLEM STATEMENT
Animal and bird intrusion in forest areas and crop fields is very common nowadays. Many systems exist in reality that helps in solving the issue. But all the system affects the intruder either mentally or physically or they might be costlier. 
It is crucial to have a system that monitor animal/bird intrusion and report it to the forest offices / farmers at the earliest so that they can take the precautionary measures to save their assts in such a way that it doesn’t affect the intruders in any manner. 
Hence, we would like to develop a system that detects the presence of intruder/intruders in live video from original scenarios and classifies what animal it is or whether it’s a bird. upon classification, it intimate the authorities via SMS and also plays a sound to keep the intruder away. It can be used for monitoring and reducing the human-animal conflicts.

# Project Architecture
The proposed system provided in this project also has two phases. 
         1. The Training phase where the images are trained to get a model 
         2. The Testing phase where the intruder is detected based on the trained model. 

The steps involved in the Training part are as follows:

1. Data collection: The images of various wild animals and birds whose presence is being noticed is collected from the google 
                    Later these data will be used for the training and model building of the project. 

2.Data Pre-Processing: * For improvement of the image data. 
                       
		       * Suppresses the unwanted distortions or enhances some image features.

		       * There are basically 2 processes involved in pre-processing: 
                       
			 1. Mean Subtraction: Used to help combat illumination changes in the input images in our dataset. 
					      Used to make sure all dataset images are in the same size before feeding to the algorithm.
                         
			 2. Data Scaling or normalization: for making model data in a standard format so that the training is improved, accurate, and faster.

3.Feature Extraction: * Focuses on identifying inherent features of the objects present within an image. 
                      
		      * These inherited features are then converted into pixel values later during training and then these pixel values are compared with the image pixel value (input) and based on this comparison                         classification is performed.

4.Training and Model Building: * In the project we make use of CNN algorithm for model building Since CNN algorithm work fine with image files.  
                          
			       * So, we make use of YoloV3 method in combination with darknet to build the model.   
