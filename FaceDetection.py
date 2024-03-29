# Face detection page utilizing OpenCV

import cv2

def main():

    while True:
        try:
            # Requesting user-input on which picture will have face detection performed on it
            # https://stackoverflow.com/questions/29824194/setting-user-input-to-variable-name
            imagePath = input('\n\nPlease enter the name of the image you would like to detect a face from here.\n' +
                              'Capitalization and spelling of the name will make a difference. Also, the file extension\n' +
                              'will make a difference, and should be added to the image name.\n\n' +
                              'Please enter the database picture name for emotion/age detection:\n\n' +
                              'AllTheKids.jpg\n' +
                              'CodyTrip.jpg\n' +
                              'MeAndEllie.jpg\n' +
                              'MeAndSteph.jpg\n' +
                              'MeAndStephAgain.jpg\n' +
                              'NashvilleTrip.jpg\n' +
                              'child_angry_neutral.JPG\n' +
                              'child_happy.JPG\n' +
                              'neutralChildFace.JPG\n' +
                              'neutral.JPG\n' +
                              'neutral_glasses.JPG\n' +
                              'surpriseFace.JPG\n' +
                              'disgust_neutral.JPG\n' +
                              'smileFace.JPG\n' +
                              'sadFace.JPG\n' +
                              'JaneMansfield_Happy.JPG\n' +
                              'RitaHayworth_Neutral.JPG\n' +
                              'ElvisPresley_neutral.JPG\n' +
                              '\n' +
                              'Please enter the name of your image here: ')
        except ValueError:
            (print("The answer did not compute properly.  Make sure you typed the file extension in correctly.\n" +
                   "The program will bring you to the beginning to try again.\n"))
            main()
        else:
            break


    # creating variable for haar cascade, see reference below for haar files downloaded via zip file,
    # which I extracted to my program files.
    # reference: http://alereimondo.no-ip.org/OpenCV/34/
    cascPath = "./haarcascade_frontalface_alt.xml"


    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    # Original reference: https://realpython.com/face-recognition-with-python/
    # reference to correct cv issue appears due to CV3 now:
    # https://stackoverflow.com/questions/36242860/attribute-error-while-using-opencv-for-face-recognition

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(faces) == 0:
        print("There are no faces in this picture.  Please try again with a different picture.")
        main()

    if len(faces) > 0:

        # Reference used to fix this for python:
        # https://akshaysin.github.io/facerecog.html#.XVGxjehKjIU
        print('Found {0} faces!'.format(len(faces)))

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # showing face detection and also saving to a file
        cv2.imshow("Faces found", image)

        # Reference utilized for next portion: https://akshaysin.github.io/facerecog.html#.XVGxjehKjIU
        status = cv2.imwrite(imagePath + 'saved.jpg', image)
        print('Image written to file-system: ', status)
        cv2.waitKey(0)

        print('\n\n')


        # Offering the user menu choices to continue or exit program
        menuChoice = input('Press 1 to detect a face or faces in an image again\n' +
                           'Press 2 to detect facial emotion and age from a picture\n' +
                           'Press 3 to return to the program main menu\n' +
                           'Press 4 to exit\n\n' +
                           'Please enter your answer here: ')

        while True:
            try:
                if menuChoice == '1':
                    main()

                if menuChoice == '2':
                    import EmotionAndAge

                if menuChoice == '3':
                    import mainPage

                if menuChoice == '4':
                    exit()

            except ValueError:
                print("Let's try again. The program will bring you to the beginning of the menu.")
                main()
            else:
                break
main()
