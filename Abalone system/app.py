from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

#loading the trained model
with open('dt_tuned.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    sex_encoded = data['sex']
    
    #Dataframe with column names
    input_df = pd.DataFrame([{
        'Sex': sex_encoded,
        'Length': data['length'],
        'Diameter': data['diameter'],
        'Height': data['height'],
        'Whole weight': data['whole_weight'],
        'Whole weight.1': data['whole_weight_1'],
        'Whole weight.2': data['whole_weight_2'],
        'Shell weight': data['shell_weight']
    }])
    
    # using the dataframe for prediction
    prediction = model.predict(input_df)[0]
    
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)

