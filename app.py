from langchain.llms import VertexAI
import os
import streamlit as st
import requests
import pandas as pd
from google.cloud import translate_v2 as translate
import google.cloud.texttospeech as tts
import wave
import time
import folium
#import gTTS


#from fpdf import FPDF   
#from streamlit_folium import st_folium, folium_static
#from st_audiorec import st_audiorec
#from google.cloud import language_v1

img = "Radar.png"

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

#vertexai.init(project="speechrec-396114", location="us-central1")

supported_languages = {
    "af": "Afrikaans",
    "sq": "Albanian",
    "am": "Amharic",
    "ar": "Arabic",
    "az": "Azerbaijani",
    "eu": "Basque",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "ca": "Catalan",
    "zh-CN": "Chinese (Simplified)",
    "zh-TW": "Chinese (Traditional)",
    "hr": "Croatian",
    "cs": "Czech",
    "da": "Danish",
    "nl": "Dutch",
    "en": "English",
    "et": "Estonian",
    "tl": "Filipino",
    "fi": "Finnish",
    "fr": "French",
    "gl": "Galician",
    "ka": "Georgian",
    "de": "German",
    "el": "Greek",
    "gu": "Gujarati",
    "he": "Hebrew",
    "hi": "Hindi",
    "hu": "Hungarian",
    "is": "Icelandic",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "kn": "Kannada",
    "ko": "Korean",
    "ku": "Kurdish (Kurmanji)",
    "ky": "Kyrgyz",
    "lo": "Lao",
    "la": "Latin",
    "lv": "Latvian",
    "lt": "Lithuanian",
    "mk": "Macedonian",
    "ms": "Malay",
    "ml": "Malayalam",
    "mn": "Mongolian",
    "ne": "Nepali",
    "no": "Norwegian",
    "pa": "Punjabi",
    "fa": "Persian",
    "pl": "Polish",
    "pt-BR": "Portuguese (Brazil)",
    "pt-PT": "Portuguese (Portugal)",
    "ro": "Romanian",
    "ru": "Russian",
    "sr": "Serbian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sl": "Slovenian",
    "es": "Spanish",
    "su": "Sundanese",
    "sw": "Swahili",
    "sv": "Swedish",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    "cy": "Welsh",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "yo": "Yoruba",
    "zu": "Zulu"
}

pref_lang = st.sidebar.selectbox(label="Choose Language", options=list(supported_languages.values()), index=15)

def translating(text,lang):
    translate_client = translate.Client()
    #text = ans
    if isinstance(text, bytes):
        text = text.decode("utf-8")
    get = list(supported_languages.values()).index(lang)
    value = list(supported_languages.keys())[get]
    result = translate_client.translate(text, target_language=value)

    return result["translatedText"]


counties = pd.read_csv("city_data/countries.csv")
cities = pd.read_csv("city_data/cities.csv")
states = pd.read_csv("city_data/states.csv")

df_countries = counties["name"].tolist()


llm = VertexAI(
    model_name="text-bison@001",
    max_output_tokens=512,
    temperature=0.1,
    top_p=0.8,
    top_k=40,
    verbose=True,
    )
#vc = st.sidebar.button("Voice Search")


trans_result = translating("வணக்கம்", "English")
print(trans_result)

st.title(':violet[Travel] :red[Guide]')

pref_country = st.selectbox(label="Choose Country", options=df_countries)

states = states.loc[states['country_name'] == pref_country]['name'].tolist()
pref_state = st.selectbox(label="Choose State", options=states)

cities = cities.loc[cities['state_name'] == pref_state]['name'].tolist()
pref_city = st.selectbox(label="Choose City", options=cities)

pref_timing  = st.selectbox(label="Choose Timing", options=["Morning", "Afternoon", "Evening", "Night"])
pref_budget = st.slider(label="Choose Budget", min_value=0, max_value=10000, step=10)

pref_weather = st.selectbox(label="Choose Weather", options=["Sunny", "Rainy", "Snowy", "Cloudy"])
pref_alegeric = st.text_input(label="Any Health Issues?")
pref_food = st.text_input(label="Any Food Preferences?")

cities = pd.read_csv("city_data/cities.csv")

lat = cities.loc[cities['name'] == pref_city]['latitude'].tolist()
long = cities.loc[cities['name'] == pref_city]['longitude'].tolist()
print(lat,long)
places = []

#cb = st.sidebar.button("Chatbot")
language = st.sidebar.selectbox("Select Language for Audio", ["English", "Tamil"])


question=True
if st.button("Ask"):
    if question:
        #index = create_langchain_index(input_text)

        data = {'lat': lat, 'lon': long}
        df = pd.DataFrame(data)

        st.map(df)
        response = llm.predict(
            text=f"Can you recommend some notable attractions to visit in {pref_city} during {pref_timing}? Please explain why these attractions are worth visiting during this time of the year. Additionally, could you suggest some local restaurants that fit within a {pref_budget} budget? and consider the weather to be {pref_weather} and consider am i perfect to visit the place since i have this problem {pref_alegeric} and my food preference is {pref_food} and suggest the ways to travel there via Flight , Train and Bus and also give me a budget plan on this {pref_budget}budget?",
            #text = "what is the date today ? "
        )
        trans_result = translating(response,pref_lang)
        st.write(trans_result)
        places.extend(response.split("restaurant"))
        #st.write("Wanna do car pooling ? Check out uber pool")
        response = response.replace("*", "")
  

    
        if language == "English":
            audio_file = open("en-IN-Wavenet-C.wav", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/wav")
        elif language == "Tamil":
            audio_file = open("ta-IN-Wavenet-C.wav", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/wav")
    else:
        st.warning("Please enter a question.")

query = st.sidebar.text_input("Any Queries ?")
#submit = st.button("Submit")
if st.sidebar.button("Submit"):
    st.write(llm.predict(query + "answer , consider your self as toursit guide ")) 


