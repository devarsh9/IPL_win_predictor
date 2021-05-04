#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
print("working")

#default page of our web-app
@app.route('/')
def home():
    print("working good")
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print("Reached")
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    # output = round(prediction[0], 2)
    output = prediction[0]
    print(output)
    #  return render_template('index.html', prediction_text='The second batting team will  :{}'.format(output))
    if(output == 1):
        return render_template('index.html', prediction_text='The second batting team will win the match')
    else:
        return render_template('index.html', prediction_text='The second batting team will lose the match')
         
if __name__ == "__main__":
    app.run(debug=True)