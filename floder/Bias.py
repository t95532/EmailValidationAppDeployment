import streamlit as st
from preprocess import preprocess_text
import pickle

# Streamlit app
def main():
    st.title("Text Prediction App")

    label = {0: 'center', 1: 'lean left', 2: 'lean right', 3: 'left', 4: 'right'}

    # Text input
    text_input = st.text_input("Enter your text:")

    if st.button("Predict"):
        if text_input:
            # Run the prediction function
            tx = preprocess_text(text_input)

            #passing the text to the model
            model = pickle.load(open('model.pkl', 'rb')) # Load the model

            prediction = model.predict([tx])[0]

            # Map the prediction to the output value
            output_value = label.get(prediction, "Unknown")
            
            # Display the output value
            st.write(f"Prediction: {output_value}")
        else:
            st.write("Please enter some text.")

if __name__ == "__main__":
    main()