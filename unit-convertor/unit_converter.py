import streamlit as st

# Conversion factors
conversion_factors = {
    "Length": {
        "meters": {"kilometers": 0.001, "centimeters": 100, "inches": 39.3701, "feet": 3.28084},
        "kilometers": {"meters": 1000, "miles": 0.621371},
        "miles": {"kilometers": 1.60934, "meters": 1609.34},
    },
    "Weight": {
        "kilograms": {"grams": 1000, "pounds": 2.20462},
        "grams": {"kilograms": 0.001, "milligrams": 1000},
        "pounds": {"kilograms": 0.453592, "ounces": 16},
    },
    "Temperature": {
        "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
        "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: (f - 32) * 5/9 + 273.15},
        "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32},
    },
    "Volume": {
        "liters": {"milliliters": 1000, "gallons": 0.264172},
        "milliliters": {"liters": 0.001},
        "gallons": {"liters": 3.78541},
    }
}

st.title("Google-style Unit Converter")

# Select category
category = st.selectbox("Select a category", list(conversion_factors.keys()))

# Select units
units = list(conversion_factors[category].keys())
from_unit = st.selectbox("From:", units)
to_unit = st.selectbox("To:", units)

# Input value
value = st.number_input(f"Enter value in {from_unit}:", min_value=0.0, step=0.01)

# Convert function
def convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if category in conversion_factors and from_unit in conversion_factors[category]:
        conversions = conversion_factors[category][from_unit]
        if to_unit in conversions:
            conversion = conversions[to_unit]
            return conversion(value) if callable(conversion) else value * conversion
    return "Conversion not available"

# Display result
if st.button("Convert"):
    result = convert(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result} {to_unit}")
