import streamlit as st
import numpy as np
import joblib

# Load the saved model
model2 = joblib.load("food_order_prediction_beta.pkl")


st.title("Will the Customer Order Again? 🍕🍔🍟🌭")
# Create a container to center the image
container = st.container()

# Add logo image in the center
with container:
    st.image("logo2.jpg", width=100, use_column_width=True)


st.subheader("_Online Food Delivery Order Prediction based various attributes related to Occupation, Family Size, Feedback etc.._")



# Create a form for the user to input their details
st.write("**Enter Customer Details:**")

# Add input fields for each feature
age = st.slider("Age:", 0, 100, 30)

gender_option = st.radio("Gender:", options=["Male", "Female"])
gender = 1 if gender_option == "Male" else 0

marital_status_option = st.radio("Marital Status:", options=["Single", "Married", "Not Revealed"])
if marital_status_option == "Single":
    marital_status = 1
elif marital_status_option == "Married":
    marital_status = 2
else:
    marital_status = 3  # Not Revealed

occupation_option = st.radio("Occupation:", options=["Student", "Employee", "Self Employed", "House wife"])
if occupation_option == "Student":
	occupation = 1
elif occupation_option == "Employee":
	occupation = 2
elif occupation_option == "Self Employed":
	occupation = 3
# else occupation_option == "House wife":
# 	occupation = 4
else:
	occupation = 4

monthly_income = st.slider("Monthly Income:", 0, 500000, 5000)

education_option = st.selectbox("Educational Qualification:", options=["Graduate", "Post Graduate", "Ph.D", "School", "Uneducated"])
if education_option == "Graduate":
	education = 1
elif education_option == "Post Graduate":
	education = 2
elif education_option == "Ph.D":
	education = 3
elif education_option == "School":
	education = 4
# else education_option == "Uneducated":
# 	education = 5
else:
	education = 5

family_size = st.slider("Family Size:", 0, 10, 3)

pin_code = st.text_input("Pin Code:")

feedback_option = st.radio("Review of the Last Order:", options=["Positive", "Negative"])
if feedback_option == "Positive":
	feedback = 1
# else feedback_option == "Negative":
# 	feedback = 0
else:
	feedback = 0

# Convert the input values to a numpy array
try:
    pin_code = float(pin_code)
    features = np.array([[age, gender, marital_status, occupation, monthly_income, education, family_size, pin_code, feedback]])

    # Use the loaded model to predict if the customer will order again
    prediction = model2.predict(features)
    # if prediction == "Yes":
    # 	prediction_result = "Yes, there is a high chance that the customer will order again! 😊👌"
    # else:
    # 	prediction_result = "No, there is a low chance that the customer will order again 😓🙁"

    # # Display the prediction result
    # st.write("**Finding if the customer will order again:** ")
    # st.subheader(prediction_result)

    if prediction == "Yes":
    	prediction_result = "Yes, there is a high chance that the customer will order again! 😊👌"
    	reason = "Based on the provided details, the model predicts that the customer is likely to order again due to their favorable demographic characteristics and positive feedback from the last order."
    else:
    	prediction_result = "No, there is a low chance that the customer will order again 😓🙁"
    	reason = "The model predicts that the customer is less likely to order again, possibly due to factors such as age, marital status, or previous negative feedback."

    # Display the prediction result and reasoning
    st.write("**Finding if the customer will order again:** ")
    st.subheader(prediction_result)
    st.write("**Reasoning:**")
    st.write(reason)



except ValueError:
    pass

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write("👨🏻‍💻Developed By: **Anirban Bhattacharjee**")
st.write("**Contact:**")
st.write("**📩 Email:** [anirban8472@gmail.com](mailto:anirban8472@gmail.com)")
st.write("**🖥️LinkedIn:** [Anirban Bhattacharjee](https://www.linkedin.com/in/anirban-bhattacharjee-10063a150/)")
# About Me section
st.header("About Me")
st.write("Here you can find more information about me.")

with open("anirban_cv_2024_new_V3.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download My Resume",
                    data=PDFbyte,
                    file_name="anirban_cv_2024_new_V3.pdf",
                    mime='application/octet-stream')