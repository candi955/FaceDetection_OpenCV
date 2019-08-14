# Emotion and Age detection page
# References to create this page:
# https://blog.algorithmia.com/emotion-recognition-api-analyzing-facial-expressions/
# https://algorithmia.com

from PIL import Image
import Algorithmia

def main():
    # Asking the user to enter the name of the data file (image) he or she wishes to see emotion and age detection of.
    # It must be listed in the data format to be called from storage in Algorithmia API

    userInput = (input("\n\nPlease enter the database picture name for emotion/age detection:\n\n" +
                       'data://#####/EmotionAndAge/child_angry_neutral.JPG\n' +
                       'data://#####/EmotionAndAge/child_happy.JPG\n' +
                       'data://#####/EmotionAndAge/neutralChildFace.JPG\n' +
                       'data://#####/EmotionAndAge/neutral.JPG\n' +
                       'data://#####/EmotionAndAge/neutral_glasses.JPG\n' +
                       'data://#####/EmotionAndAge/surpriseFace.JPG\n' +
                       'data://#####/EmotionAndAge/disgust_neutral.JPG\n' +
                       'data://#####/EmotionAndAge/smileFace.JPG\n' +
                       'data://#####/EmotionAndAge/sadFace.JPG\n' +
                       'data://#####/EmotionAndAge/JaneMansfield_Happy.JPG\n' +
                       'data://#####/EmotionAndAge/RitaHayworth_Neutral.JPG\n' +
                       'data://#####/EmotionAndAge/ElvisPresley_neutral.JPG\n' +
                       '\n' +
                       "Enter your choice in the format data://example, here: "))

    # entering Algorithmia API client key
    client = Algorithmia.client("insertAPIkeyhere")

    # defining what the image input will be
    input1 = {"image": userInput, "numResults": 7}

    # calling on API for emotion recognition from the image (7 different types), and then assigning the actual
    # emotion recognition to a variable called Emotionresult
    algo = client.algo('deeplearning/EmotionRecognitionCNNMBP/0.1.2')
    emotionResult = algo.pipe(input1).result

    # calling on API for age recognition from the image (7 different types), and then assigning the actual
    # age recognition to a variable called ageResult
    algo = client.algo('deeplearning/AgeClassification/2.0.0')
    ageResult = algo.pipe(input1).result

    while True:
        try:

            # printing Emotion and Age results, and also showing the image chosen in a separate window that opens
            print('\n\nThe result of facial emotion detection on this picture is:\n')
            print(emotionResult)

            print('\n\nThe result of facial age detection on this picture is:\n')
            print(ageResult)

        # Attempting exception prevention
        except ValueError:
            print('The results do not appear to be configuring correctly.  The program will bring you back to the ' +
                  'main menu to start over.')
            import mainPage

        # Showing the user the actual image that was chosen
        # using if-statements to make sure the correct image is shown, which correlates with the user's original choice
        if userInput == "data://candi955/EmotionAndAge/child_angry_neutral.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("child_angry_neutral.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/child_happy.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("child_happy.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/neutralChildFace.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("neutralChildFace.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/neutral.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("neutral.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/neutral_glasses.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("neutral_glasses.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/surpriseFace.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("surpriseFace.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/disgust_neutral.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("disgust_neutral.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/smileFace.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("smileFace.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/sadFace.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("sadFace.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/JaneMansfield_Happy.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("JaneMansfield_Happy.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/RitaHayworth_Neutral.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("RitaHayworth_Neutral.JPG")
            showImage.show()

        if userInput == "data://candi955/EmotionAndAge/ElvisPresley_neutral.JPG":
            print('\nPlease view image file in new window.\n')
            showImage = Image.open("ElvisPresley_neutral.JPG")
            showImage.show()

        while True:
            try:

                # Offering the user menu choices to continue or exit program
                menuChoice = input('Press 1 to detect facial emotion and age from a picture again\n' +
                                   'Press 2 to detect a face or faces in an image \n' +
                                   'Press 3 to return to the program main menu\n' +
                                   'Press 4 to exit\n\n' +
                                   'Please enter your answer here: ')

                if menuChoice == '1':
                    main()

                if menuChoice == '2':
                    import FaceDetection

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

