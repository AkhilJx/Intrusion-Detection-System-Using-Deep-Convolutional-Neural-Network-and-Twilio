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

1. Data collection:
The images of various wild animals and birds whose presence is being noticed is collected from the google. Later these data will be used for the training and model building of the project. 

2. Data Pre-Processing: For improvement of the image data. Suppresses the unwanted distortions or enhances some image features.
There are basically 2 processes involved in pre-processing: 
(i). Mean Subtraction: Used to help combat illumination changes in the input images in our dataset. Used to make sure all dataset images are in the same size before feeding to the algorithm.
(ii).Data Scaling or normalization: for making model data in a standard format so that the training is improved, accurate, and faster.

3. Feature Extraction: 
Focuses on identifying inherent features of the objects present within an image. These inherited features are then converted into pixel values later during training and then these pixel values are compared with the image pixel value (input) and based on this comparison classification is performed.

4. Training and Model Building: 
In the project we make use of CNN algorithm for model building Since CNN algorithm work fine with image files. So, we make use of YoloV3 method in combination with darknet to build the model.   



The steps involved in the *Testing part* are as follows:

1. Image Acquisition: 
The initial step involved in the testing part in which the real-world sample is recorded in its digital form using a digital camera. The input video is first converted into frames before giving to the CNN algorithm as CNN works well with images. This is done by reading the video frame by frame (by looping) using read fn in OpenCV. The image is captured, scanned, and converted into a manageable entity. This process is known as image acquisition.

2. Image Pre-processing and feature extraction: 
OpenCV provides a function (cv2.dnn.blobFromImage) to facilitate image preprocessing and feature extraction for deep learning classification. The cv2.dnn.blobFromImages function returns a blob i.e., input image after mean subtraction, normalizing, and channel swapping. Blob stands for Binary Large Object and refers to the connected pixel in the binary image.

3. Classification: 
Here the detected intruder is identified and classified as birds or animals like a tiger, lion, etc. The blob created after pre-processing and feature extraction will be fed into the algorithm and the algorithm compares this blob with the model and based on that it predicts the detection of the intruder. i.e., Based on the similarities in the pixel value obtained after pre-processing and feature extraction with the respective pre-defined pixel value of the corresponding animal/ bird, it classifies the intruder as birds/animal.

4. Intimation, playing sound, and log file creation: 
The final step in the testing part, where the user (farmers or forest officers) gets the alert/ threat about the intruder. 
The intimation to the authorities is done through Twilio messenger where the alert will be sent in the form of SMS with the aid of the internet. 
Similarly, when an intruder is detected, the system plays a sound (the sound of some creatures which the intruders are generally scared of ) to keep the intruder away. 
In this study, we took the sound of a tiger for animal detection whereas the sound of a hawk for bird detection. 
This can be connected to a speaker or an amplifier to enhance the sound frequency if required. 
Finally, a CSV file is created to store all the log/history of the animal detected with names, accuracies, and timestamps as parameters. 
Once the CSV file is created, we can fetch the details of animals detected within a timeline along with accuracies so that we can be aware of the frequency of intruder arrival and seasonal arrival of the intruder if any. 
In this study, we have provided the user to choose from 3 timeline analyses namely date wise, month wise, and year wise statistics. 
Based on the user selection, the user will get the details of the value counts of the intruder in the given timeline so that the user gets to know about the seasonal arrival of the intruder and the frequencies of their arrivals. 

![image](https://github.com/AkhilJx/Intrusion-Detection-System-Using-Deep-Convolutional-Neural-Network-and-Twilio/assets/78065413/1cec59c4-4316-477d-9927-7e5ee272c563)

# Project Implementation

The steps involved in the implementation are:
1. Collecting images of animals as a database which is used for training of the program.
2. Based on the database, a model is being created for testing.
3. The Image/video acquisition from the camera is done and is fed as input to the system.                                    
4. Once input is fed to the system, the Conversion of video to frames is carried out. 
5. We use the imread function to read the camera captured frame (image) if it is fetching video stored in a hard disk or cv2.videocapture() if the camera is directly connected to the computer. After this Preprocessing is done on that image/ frame. 
6. After pre-processing of the camera captured image, a comparison of this frame with the model created is carried out. I.e., The system checks if matching is found or not.
7. If matching is found, intimation to the concerned person about the animal is done. Else it continues from step 3.


# Results

1. Detecting Intruder (Bird) with accuracy and timestamp

![image](https://github.com/AkhilJx/Intrusion-Detection-System-Using-Deep-Convolutional-Neural-Network-and-Twilio/assets/78065413/94c967ee-7eb2-483d-9a7f-c4be7a28f1b4)

2. Detecting Intruder ( Animal - Giraffe ) with accuracy and timestamp

![image](https://github.com/AkhilJx/Intrusion-Detection-System-Using-Deep-Convolutional-Neural-Network-and-Twilio/assets/78065413/1cfcf1ad-504c-464e-988f-a19ac90c75a8)

3. Intimating the user via SMS

![image](https://github.com/AkhilJx/Intrusion-Detection-System-Using-Deep-Convolutional-Neural-Network-and-Twilio/assets/78065413/24d4a664-9f4d-4016-800f-fe0c433abf20)

4. Log file Output

![image](https://github.com/AkhilJx/Intrusion-Detection-System-Using-Deep-Convolutional-Neural-Network-and-Twilio/assets/78065413/207b775a-a228-4e9b-a876-a8b6060ccf80)
![image](https://github.com/AkhilJx/Intrusion-Detection-System-Using-Deep-Convolutional-Neural-Network-and-Twilio/assets/78065413/f4710d03-63e9-446f-9bfb-2c109625010b)

