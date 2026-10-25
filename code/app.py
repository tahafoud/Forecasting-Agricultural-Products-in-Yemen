import streamlit as st
import pandas as pd
import pickle

# Load encoder, scaler, and model
encoder = pickle.load(open("./outputs/encoder.pkl", 'rb'))
scaler = pickle.load(open("./outputs/scaler.pkl", 'rb'))  # Ensure this file exists
model_gbc = pickle.load(open("./outputs/model_gbc.pkl", 'rb'))

# Prediction function
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_df = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                            columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    input_scaled = scaler.transform(input_df)
    prediction_encoded = model_gbc.predict(input_scaled)
    prediction = encoder.inverse_transform(prediction_encoded)
    return prediction[0]

# Streamlit UI


# إعداد خلفية بألوان علم الجمهورية اليمنية
st.markdown("""
<style>
/* خلفية التطبيق: أحمر، أبيض، أسود */
.stApp {
    background: linear-gradient(
        to bottom,
        #CE1126 0%,
        #CE1126 33.33%,
        #FFFFFF 33.33%,
        #FFFFFF 66.66%,
        #000000 66.66%,
        #000000 100%
    );
    background-attachment: fixed;
}

/* مساحة المحتوى */
.block-container {
    background-color: rgba(255, 255, 255, 0.94);
    padding: 2rem;
    border-radius: 15px;
    margin-top: 20px;
}

/* تنسيق العنوان */
.yemen-title {
    color: #CE1126;
    font-size: 2.2rem;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
}

/* تنسيق العنوان الفرعي */
.yemen-subtitle {
    color: #222222;
    text-align: center;
    font-size: 1rem;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# شعار الجمهورية اليمنية
coat_of_arms_url = (
    "yemen.png"



    # "https://commons.wikimedia.org/wiki/Special:Redirect/file/"
    # "Emblem_of_Yemen_%282%29.svg"
)

# عرض الشعار والعنوان
st.markdown(
    f"""
    <div style="text-align:center;">
        <img src="{coat_of_arms_url}"
             alt="Official Yemen Coat of Arms"
             style="width:150px; max-width:40%; height:auto;">
        <div class="yemen-title">
            Crop Recommendation System
        </div>
        <div class="yemen-subtitle">
            Official Yemen Coat of Arms
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# st.title('🌾 Crop Recommendation System - Official Yemen Coat of Arms')

# st.markdown("#### Please enter the soil and environmental values:")

col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0, value=50.0)
    P = st.number_input("Phosphorous (P)", min_value=0.0, value=50.0)
    K = st.number_input("Potassium (K)", min_value=0.0, value=50.0)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)

with col2:
    temperature = st.number_input("Temperature (°C)", min_value=-10.0, value=25.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, value=80.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=100.0)

# Predict button
if st.button('🌱 Recommend'):
    crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
    st.success(f"✅ Recommended Crop: **{crop}**")