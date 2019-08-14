# Emotion and Age detection page
# References to create this page:
# https://blog.algorithmia.com/emotion-recognition-api-analyzing-facial-expressions/
# https://algorithmia.com

# Asking the user to enter the name of the data file (image) he or she wishes to see emotion and age detection of.
# It must be listed in the data format to be called from storage in Algorithmia API

userInput = (input("\n\nPlease enter the database picture name for emotion/age detection.\n\n" +
                                    "Enter your choice in the format data://example, here: "))
# I had to import Algorithmia after my initial statement as it was causing string and user-input issues otherwise
import Algorithmia

# entering Algorithmia API client key
client = Algorithmia.client("simU4C7yBisFy1s7U07hKOYNOit1")

# defining what the image input will be
input = {"image": userInput, "numResults": 7}

# calling on API for emotion recognition from the image (7 different types), and then assigning the actual
# emotion recognition to a variable called Emotionresult
algo = client.algo('deeplearning/EmotionRecognitionCNNMBP/0.1.2')
emotionResult = algo.pipe(input).result

# calling on API for age recognition from the image (7 different types), and then assigning the actual
# age recognition to a variable called ageResult
algo = client.algo('deeplearning/AgeClassification/2.0.0')
ageResult = algo.pipe(input).result

print('\n\nThe result of facial emotion detection on this picture is:\n')
print(emotionResult)

print('\n\nThe result of facial age detection on this picture is:\n')
print(emotionResult)

print('\n\n')



