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
from langdetect import detect

def run():
    st.title("Language Detection")
    st.text("Basic app to detect the language of the text.")
    st.text("")
    
    userinput = st.text_input('Enter text below, then click the Detect button.', placeholder='Input text HERE')
    st.text("")
    detected_language = ""
    
    if st.button("Detect"):
        try:
            # Detect the language of the input text
            detected_language_code = detect(userinput)
            
            # Map the detected language code to its full name
            if detected_language_code == 'en':
                detected_language = "English 🇬🇧"
            elif detected_language_code == 'es':
                detected_language = "Spanish 🇪🇸"
            elif detected_language_code == 'fr':
                detected_language = "French 🇫🇷"
            else:
                detected_language = f"Detected language code: {detected_language_code}"
            
            language_message = f'The detected language of "{userinput}" is {detected_language}.'
            st.success(language_message)
        except Exception as e:
            st.error(f"Error detecting language: {e}")

if __name__ == "__main__":
    run()
