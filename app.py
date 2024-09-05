import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Load model
with open('model_huber.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)


# Menambahkan gambar header untuk branding
header_image = Image.open('Fossil (1).png')
st.image(header_image, use_column_width=True)


st.title('Fossil Age Prediction')
st.markdown(
"""
Welcome to the **Fossil Age Prediction** web app. This tool utilizes a **Huber Regression** model to predict the age of fossils based on various geological and chemical parameters. Simply input the required data, and let the model do the rest!
"""
)

# Sidebar for additional settings
st.sidebar.header("Customization")
theme = st.sidebar.selectbox("Choose Theme:", ['Default', 'Dark', 'Light Blue'])
st.sidebar.markdown("Customize your experience by selecting a theme from the options above.")

# Pengaturan Input
st.markdown("## Input Fossil Parameters")

uranium_lead_ratio = st.slider('Rasio Uranium-Lead', min_value=0.000241, max_value=1.533270, step=0.000001)
carbon_14_ratio = st.slider('Rasio Carbon-14', min_value=0.000244, max_value=1.000000, step=0.000001)
radioactive_decay_series = st.slider('Deret Peluruhan Radioaktif', min_value=0.000076, max_value=1.513325, step=0.000001)
stratigraphic_layer_depth = st.slider('Kedalaman Lapisan Stratigrafi', min_value=0.130000	, max_value=494.200000, step=0.01)

# Kolom 2 untuk input tambahan
col3, col4 = st.columns(2)
with col3:
    geological_period = st.selectbox('Periode Geologi', ['Cretaceous', 'Cambrian', 'Permian', 'Devonian', 'Jurassic', 'Neogene', 'Triassic', 'Paleogene', 'Ordovician', 'Carboniferous', 'Silurian'])
    stratigraphic_position = st.selectbox('Posisi Stratigrafi', ['Middle', 'Top', 'Bottom'])

with col4:
    paleomagnetic_data = st.selectbox('Data Paleomagnetik', ['Normal polarity', 'Reversed polarity'])
    fossil_size = st.slider('Ukuran Fosil', min_value=0.130000, max_value=216.390000, step=0.01)

# Memisahkan prediksi dengan section yang menarik
st.markdown("---")
st.markdown("<style>div.row-widget.stSlider { margin-bottom: -15px; }</style>", unsafe_allow_html=True)
st.image('Untitled design (18).png', use_column_width=True)
st.markdown("## Predict Fossil Age")

# Tombol untuk melakukan prediksi dengan tampilan interaktif
if st.button('🔍 Make a Prediction'):
    new_data = pd.DataFrame({
        'uranium_lead_ratio': [uranium_lead_ratio],
        'carbon_14_ratio': [carbon_14_ratio],
        'radioactive_decay_series': [radioactive_decay_series],
        'stratigraphic_layer_depth': [stratigraphic_layer_depth],
        'geological_period': [geological_period],
        'paleomagnetic_data': [paleomagnetic_data],
        'stratigraphic_position': [stratigraphic_position],
        'fossil_size': [fossil_size]
    })

    # Prediksi
    prediction = loaded_model.predict(new_data)

    # Menampilkan hasil prediksi dengan card-style dan animasi
    st.markdown(f"""
    <div style="background-color:#f9f9f9;padding:10px;border-radius:10px;text-align:center;">
        <h2 style="color:#007bff;">Predicted Fossil Age</h2>
        <p style="font-size:24px;font-weight:bold; color:black;">{int(prediction[0])} years old</p> </div>
    """, unsafe_allow_html=True)

    st.success("Prediction successfully completed!")
    st.balloons()

    # Menampilkan beberapa detail output dengan sedikit lebih terstruktur
    st.markdown("### Fossil Analysis Summary")
    st.write("Here is a summary of the input data used for the prediction:")
    st.write(new_data)

# Sidebar footer info
st.sidebar.markdown("---")
st.sidebar.markdown("""
**Developed by Fossil AI Team**  
Contact us for inquiries and collaborations:  
[Contact Us](https://example.com/contact)
""")

# Styling untuk menyesuaikan tampilan dengan tema yang dipilih
if theme == 'Dark':
    st.markdown("""
    <style>
        body { background-color: #2b2b2b; color: white; }
        .stSlider label { color: white; }
        h2 { color: #FFA500; }
    </style>
    """, unsafe_allow_html=True)

elif theme == 'Light Blue':
    st.markdown("""
    <style>
        body { background-color: #e0f7fa; color: #00796b; }
        .stSlider label { color: #00796b; }
        h2 { color: #007bff; }
    </style>
    """, unsafe_allow_html=True)

# Footer styling
st.markdown("<footer><p style='text-align:center;'>Powered by FossilAI | All rights reserved 2024</p></footer>", unsafe_allow_html=True)