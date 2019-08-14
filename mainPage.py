# Main-menu page for Face/Emotion/Age detection project utilizing OpenCV and Algorithmia
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
# 13:45pm added exception prevention in case no faces are in a picture... it works :)
# Reference to the Creative Commons picture I used for the plant to test it out:
# https://ccsearch.creativecommons.org/photos/739aff35-de39-43e4-b211-c05c906f4eeb
# 14:48pm I think I am going to give it different options and choices for age and emotion.  I am switching the file
# to a new project called FaceDetection_OpenCV.
# Installed opencv-python
# Attempting to import user-input image variable from GeneralDetection file to Emotion and Age files using reference:
# https://stackoverflow.com/questions/17255737/importing-variables-from-another-file
# 17:40pm I am continuing to try to make the Emotion portion work.  I have run into some issues with it.
# 21:00pm I spoke to the instructor, and it seems that there is some issue with the code.  We were both
# trying to figure out what it might be.
# 8/13/2019 @ 13:52pm After some time this morning of continuing my experiments with the current code, I have decided
# to try a different API.  I am going to do some research on it.
# 14:31pm I came across the Algorithmia API.  It looks like it might be promising.  Am going to try it out.
# 18:02pm I am going to go with Algorithmia.  I've combined the emotion/age page to EmotionAndAge.py.  The face
# detection is now on a FaceDetection.py page, with the main program menu on mainPage.py.
# 19:05pm Although Algorithmia works beautifully, it doesn't allow me to easily pull pictures from my own files.
# It does have it's own storage on the application, however.  I am going to use this, and give the user a list of
# data that can be pulled.
# 8/14/2019 @ 1:03am I have finished my program.  I attempted to add exception prevention, and menus on each page.
# However, due to only a certain amount of credits on the API, I'm not going to check quite as much as I normally would.
# I'm need to create my video still.  I will do that right now. I would say this actually took me approximately
# 16 hours in total.  I definitely underestimated the length of time it would take.  The facial detection I found to
# be much easier than the emotion and age detection.  Algorithmia definitely made that process much smoother, but
# does charge after a certain amount of credits.  However, they don't ask for financial information ahead of time,
# so I felt comfortable at least trying it out.  If I had more time with this project, I would definitely make it
# GUI, with user-choice lists instead of the user having to type or copy/paste the choices in.  I did find where
# Algorithmia's algorithm picked up two faces on one picture, and also labeled a neutral-appearing face as sad or angry
# a few times.  Super-star pictures appear to be marked as young, such as 12 years old, more often than other pictures.
# However, it overall appears to work well, and often makes one think about how we as human-beings actually process and
# assign certain qualities to certain body language, etc.  It has been a very interesting project.

def main():

    print('Welcome to the main menu for the Face Detection program.  Please enter a choice below.')

    while True:
        try:

            menuChoice = input('Press 1 to detect a face or multiple faces from a picture\n' +
                               'Press 2 to detect emotion and age within an image\n' +
                               'Press 3 to exit\n\n' +
                               'Please enter your answer here: ')


            if menuChoice == '1':
                import FaceDetection

            if menuChoice == '2':
                import EmotionAndAge

            if menuChoice == '3':
                exit()
        except ValueError:
            print("Let's try again. The program will bring you to the beginning of the menu.")
            main()
        else:
            break

main()
