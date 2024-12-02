import streamlit as st
import pandas as pd
import joblib
import base64

# Function to encode the image to Base64
def get_base64_of_bin_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load the saved model
best_model = joblib.load('carbon_emission_model.pkl')

# Function to predict the carbon footprint
def predict_carbon_footprint(input_data):
    input_df = pd.DataFrame([input_data])  # Convert input_data to DataFrame
    predicted_value = best_model.predict(input_df)  # Use the model to predict
    return predicted_value[0]

# Embed the background image using Base64
base64_image = get_base64_of_bin_file(r'C:\Users\adity\PycharmProjects\Carbon_Footprint_Calculator\background.jpg')

# Embed the external background image using CSS
st.markdown(f"""
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: url("https://wallpapers.com/images/hd/environment-background-wz742ofb7mv20diy.jpg") no-repeat center center fixed;
            background-size: cover;
        }}
        .title {{
            text-align: center;
            font-size: 32px;
            color: #ffffff;
            margin-top: 20px;
            text-shadow: 2px 2px 4px #000000;
        }}
        .subtitle {{
            text-align: center;
            font-size: 18px;
            color: #dddddd;
            text-shadow: 1px 1px 3px #000000;
        }}
        .footer {{
            text-align: center;
            color: #cccccc;
            font-size: 12px;
            margin-top: 50px;
            text-shadow: 1px 1px 2px #000000;
        }}
        .container {{
            background: rgba(255, 255, 255, 0.85);
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .result-card {{
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #ddd;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }}
        .result-card h4 {{
            color: #f44336;
        }}
        .result-card h3 {{
            color: #4CAF50;
        }}
    </style>
""", unsafe_allow_html=True)


# App header
st.markdown("<h1 class='title'>Carbon Emission Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Estimate your carbon footprint based on lifestyle factors.</p>", unsafe_allow_html=True)

# Add a section about the app
st.markdown("""
    <div class='container'>
        <h2 style='text-align: center; color: #4CAF50;'>About the App</h2>
        <p style='text-align: center; color: #555; font-size: 16px;'>
            This app helps you predict your carbon emissions based on your lifestyle choices. By understanding your carbon footprint, 
            you can take steps towards a more sustainable future.
        </p>
    </div>
""", unsafe_allow_html=True)

# Streamlit input form for prediction
def get_user_input():
    st.markdown("""
        <div class='container'>
            <h2 style='text-align: center; color: #4CAF50;'>Lifestyle Details</h2>
        </div>
    """, unsafe_allow_html=True)

    # Using columns with balanced content
    col1, col2 = st.columns(2)

    with col1:
        body_type = st.selectbox('Body Type', ['Average', 'Obese', 'Slim'])
        sex = st.selectbox('Sex', ['Male', 'Female'])
        diet = st.selectbox('Diet', ['Omnivore', 'Vegetarian', 'Vegan'])
        heating_energy_source = st.selectbox('Heating Energy Source', ['Gas', 'Electric'])
        transport = st.selectbox('Transport', ['Car', 'Public', 'Bike'])
        vehicle_type = st.selectbox('Vehicle Type', ['Petrol', 'Diesel', 'Electric'])
        social_activity = st.slider('Social Activity (1-5)', 1, 5)

    with col2:
        shower_freq = st.slider('How Often Shower (times per week)', min_value=0, max_value=7)
        grocery_bill = st.number_input('Monthly Grocery Bill ($)', min_value=0)
        travel_air_freq = st.slider('Frequency of Traveling by Air (times per year)', min_value=0, max_value=12)
        vehicle_distance = st.number_input('Vehicle Monthly Distance (Km)', min_value=0)
        waste_bag_size = st.selectbox('Waste Bag Size', ['Small', 'Medium', 'Large'])
        waste_bag_count = st.slider('Waste Bag Weekly Count', min_value=0, max_value=7)
        tv_pc_hours = st.slider('How Long TV/PC Daily (hours)', min_value=0, max_value=12)
        new_clothes_month = st.slider('How Many New Clothes Monthly', min_value=0, max_value=10)
        internet_hours = st.slider('How Long Internet Daily (hours)', min_value=0, max_value=12)
        energy_efficiency = st.selectbox('Energy Efficiency', ['Yes', 'No'])
        recycling = st.selectbox('Recycling', ['Yes', 'No'])
        cooking_with = st.selectbox('Cooking With', ['Gas', 'Electric'])

    input_data = {
        'Body Type': body_type,
        'Sex': sex,
        'Diet': diet,
        'How Often Shower': shower_freq,
        'Heating Energy Source': heating_energy_source,
        'Transport': transport,
        'Vehicle Type': vehicle_type,
        'Social Activity': social_activity,
        'Monthly Grocery Bill': grocery_bill,
        'Frequency of Traveling by Air': travel_air_freq,
        'Vehicle Monthly Distance Km': vehicle_distance,
        'Waste Bag Size': waste_bag_size,
        'Waste Bag Weekly Count': waste_bag_count,
        'How Long TV PC Daily Hour': tv_pc_hours,
        'How Many New Clothes Monthly': new_clothes_month,
        'How Long Internet Daily Hour': internet_hours,
        'Energy efficiency': energy_efficiency,
        'Recycling': recycling,
        'Cooking_With': cooking_with
    }

    return input_data


# Display the input form
input_data = get_user_input()

# Predict the carbon footprint using the model
st.markdown("""
    <div class='container'>
        <h2 style='text-align: center; color: #4CAF50;'>Prediction Results</h2>
    </div>
""", unsafe_allow_html=True)

if st.button('Predict Carbon Emission'):
    predicted_carbon_emission = predict_carbon_footprint(input_data)
    st.markdown(f"""
        <div class="result-card">
            <h3>Predicted Carbon Emission:</h3>
            <h4>{predicted_carbon_emission:.2f} kg CO2</h4>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Built with ❤️ using Streamlit</div>", unsafe_allow_html=True)
