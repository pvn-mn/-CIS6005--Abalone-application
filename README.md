### CIS6005--Abalone-application

# Abalone Ring Count Prediction
This project is a simple web application that predicts the ring count (and hence the age) of abalone based on various physical measurements. 
The application is built using Flask for the backend and Streamlit for the frontend.


### Prerequisites

Python 3.12.4

pip 24.0


**Install Dependencies (in virtual env):**

pip install -r requirements.txt
If you don't have a requirements.txt file, you can manually install the necessary packages:

pip install Flask streamlit scikit-learn



### Running the Application


The pre-trained model file **(.pkl file)** has to be imported into the root directory before executing the application

Step 1: Start the Flask Backend - **python app.py**

Step 2: Open a new terminal  & Start the Streamlit Frontend - **streamlit run forms.py**


**How to Use**

Once both the Flask backend and Streamlit frontend are running, you can interact with the application through the Streamlit interface.
Select the Sex of the abalone and adjust the sliders for various features like Length, Diameter, Height, etc.
Click on the "Predict Ring Count" button.
The predicted ring count will be displayed on the screen.

