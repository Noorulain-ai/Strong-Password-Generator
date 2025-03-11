import streamlit as st
import matplotlib.pyplot as plt

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="Graphical Unit Converter", page_icon="📏", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
        /* Title Styling */
        .title {
            color: #FF5733;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            font-family: 'Arial', sans-serif;
            text-decoration: underline;
        }
        /* Sidebar Styling */
        .sidebar .sidebar-content {
            background-color: #1E1E1E !important;
            color: white;
        }
        /* Labels */
        label {
            font-weight: bold;
            font-size: 16px;
            color: #EFC4C4 !important;
        }
        /* Result Box */
        .result-box {
            background-color: #1E88E5;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 20px;
            color: #ffffff;
        }
        /* Footer */
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 20px;
            color: #D49DA4;
        }
    </style>
""", unsafe_allow_html=True)

# --- Conversion Functions ---
def convert_temperature(value, from_unit, to_unit):
    conversions = {
        "Celsius": {"Fahrenheit": (value * 9/5) + 32, "Kelvin": value + 273.15},
        "Fahrenheit": {"Celsius": (value - 32) * 5/9, "Kelvin": (value - 32) * 5/9 + 273.15},
        "Kelvin": {"Celsius": value - 273.15, "Fahrenheit": (value - 273.15) * 9/5 + 32}
    }
    return conversions[from_unit].get(to_unit, value) if from_unit != to_unit else value

def convert_length(value, from_unit, to_unit):
    length_units = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Inches": 39.3701}
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274}
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_distance(value, from_unit, to_unit):
    distance_units = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Yards": 1.09361}
    return value * (distance_units[to_unit] / distance_units[from_unit])

def convert_speed(value, from_unit, to_unit):
    speed_units = {"m/s": 1, "km/h": 3.6, "mph": 2.237}
    return value * (speed_units[to_unit] / speed_units[from_unit])

def convert_time(value, from_unit, to_unit):
    time_units = {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600}
    return value * (time_units[to_unit] / time_units[from_unit])

# --- UI Header ---
st.markdown('<p class="title">⚡ GRAPHICAL UNIT CONVERTER</p>', unsafe_allow_html=True)

st.write("Convert **Temperature 🌡️, Length 📏, Weight ⚖️, Distance 🚀, Speed 🏎️, and Time ⏳** effortlessly!")

# --- Sidebar Selection ---
category = st.sidebar.radio("📌 Select a category:", ["🌡️ Temperature", "📏 Length", "⚖️ Weight", "🚀 Distance", "🏎️ Speed", "⏳ Time"])

# --- UI Layout ---
col1, col2 = st.columns(2)

with col1:
    from_unit, to_unit = None, None
    units = {
        "🌡️ Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "📏 Length": ["Meters", "Kilometers", "Miles", "Inches"],
        "⚖️ Weight": ["Grams", "Kilograms", "Pounds", "Ounces"],
        "🚀 Distance": ["Meters", "Kilometers", "Miles", "Yards"],
        "🏎️ Speed": ["m/s", "km/h", "mph"],
        "⏳ Time": ["Seconds", "Minutes", "Hours"]
    }
    
    from_unit = st.selectbox(f"{category} Convert from:", units[category])
    to_unit = st.selectbox(f"{category} Convert to:", units[category])
    value = st.number_input("🔢 Enter Value:", min_value=0.0, format="%.2f")

# --- Conversion Logic ---
result = None
if from_unit and to_unit:
    conversion_functions = {
        "🌡️ Temperature": convert_temperature,
        "📏 Length": convert_length,
        "⚖️ Weight": convert_weight,
        "🚀 Distance": convert_distance,
        "🏎️ Speed": convert_speed,
        "⏳ Time": convert_time
    }
    result = conversion_functions[category](value, from_unit, to_unit)

# --- Display Result and Graph ---
with col2:
    if st.button("🔄 Convert"):
        st.markdown(f'<p class="result-box">✅ {value} {from_unit} = <strong>{result:.2f} {to_unit}</strong></p>', unsafe_allow_html=True)
        
        # --- Graphical Representation ---
        fig, ax = plt.subplots()
        ax.bar([from_unit, to_unit], [value, result], color=['#1E88E5', '#E53935'])
        ax.set_ylabel("Value")
        ax.set_title("Unit Conversion Representation")
        st.pyplot(fig)

# --- Footer ---
st.markdown('<p class="footer">🚀 Developed by <b>Noor Ul Ain</b> using Python & Streamlit</p>', unsafe_allow_html=True)
