# import streamlit as st
# import pandas as pd
# import joblib
# from utils import preprocessor

# def run():
#     model = joblib.load(open('model.joblib', 'rb'))

#     st.title("Sentiment Analysis")
#     st.text("Basic app to detect the sentiment of text.")
#     st.text("")
#     userinput = st.text_input('Enter text below, then click the Predict button.', placeholder='Input text HERE')
#     st.text("")
#     predicted_sentiment = ""
#     if st.button("Predict"):
#         predicted_sentiment = model.predict(pd.Series(userinput))[0]
#         if predicted_sentiment == 1:
#             output = 'positive 👍'
#         else:
#             output = 'negative 👎'
#         sentiment=f'Predicted sentiment of "{userinput}" is {output}.'
#         st.success(sentiment)

# if __name__ == "__main__":
#     run()
import streamlit as st

def detect_language(text):
    # Simple keywords for each language
    english_keywords = ['the', 'is', 'it', 'hello', 'how', 'are']
    spanish_keywords = ['el', 'es', 'hola', 'como', 'estoy']
    french_keywords = ['le', 'est', 'bonjour', 'comment', 'je']

    # Convert the input text to lowercase for basic comparison
    text = text.lower()

    # Count the occurrence of keywords for each language
    english_count = sum(word in text for word in english_keywords)
    spanish_count = sum(word in text for word in spanish_keywords)
    french_count = sum(word in text for word in french_keywords)

    # Determine the language based on the highest count
    if english_count > spanish_count and english_count > french_count:
        return "English 🇬🇧"
    elif spanish_count > english_count and spanish_count > french_count:
        return "Spanish 🇪🇸"
    elif french_count > english_count and french_count > spanish_count:
        return "French 🇫🇷"
    else:
        return "Unable to determine language"

def run():
    st.title("Language Detection")
    st.text("Basic app to detect the language of the text.")
    st.text("")
    
    userinput = st.text_input('Enter text below, then click the Detect button.', placeholder='Input text HERE')
    st.text("")
    detected_language = ""
    
    if st.button("Detect"):
        if userinput:
            detected_language = detect_language(userinput)
            language_message = f'The detected language of "{userinput}" is {detected_language}.'
            st.success(language_message)
        else:
            st.error("Please enter some text to detect the language.")

if __name__ == "__main__":
    run()
