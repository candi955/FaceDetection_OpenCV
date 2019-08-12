# References utilized for this project (initially):
# https://realpython.com/face-recognition-with-python/
# haar model resources:
# http://alereimondo.no-ip.org/OpenCV/34/
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# https://stackoverflow.com/questions/11537585/where-can-i-find-haar-cascades-xml-files
# 8/12/2019 6:30am I have started my programming for face detection, and am initially going to try Microsoft CV.  I
# estimate this to take in total approximately 8 hours.
# 7:50am I am having trouble accessing my Microsoft keys with my student account.  I am going to switch to
# OpenCV instead.
# 11:41am (took approximately a three hour break for family doctor appt), was able to get my code to through OpenCV
# detect a face. I'm considering creating a 'photo input' choice by user.  I'm not sure if it will work, but worth
# a 'shot' (pun wasn't intended, but worked).
# 13:16pm User-input plan is successful.  The user can now input the picture name, faces are detected,
# the photo 'prints' to the screen for the user, showing detected faces, and then also 'prints' to a file
# located in the program files, with the detection on it. I have now begun to utilize the following resource
# to attempt to add emotion detection to the face detection:
# http://www.paulvangent.com/2016/04/01/emotion-recognition-with-python-opencv-and-a-face-dataset/
# importing glob in addition to cv2 for the emotion detection attempt
# It looks like it is standard with Python:
# https://stackoverflow.com/questions/42964691/how-to-install-the-glob-module
# 13:45 added exception prevention in case no faces are in a picture... it works :)
# Reference to the Creative Commons picture I used for the plant to test it out:
# https://ccsearch.creativecommons.org/photos/739aff35-de39-43e4-b211-c05c906f4eeb
# 14:48 I think I am going to give it different options and choices for age and emotion.  I am switching the file
# to a new project called FaceDetection_OpenCV.
# Installed opencv-python

def main():

    menuChoice = input('Press 1 to detect faces\n' +
                       'Press 2 to detect emotion\n' +
                       'Press 3 to detect age\n' +
                       'Press 4 to exit\n\n' +
                       'Please enter your answer here: ')


    if menuChoice == '1':
        import GeneralDetection

    if menuChoice == '2':
        import Emotion

    if menuChoice == '3':
        import Age

    if menuChoice == '4':
        exit()

main()
