
from flask import Flask, request, render_template
import numpy as np
import flasgger 
from flasgger import Swagger



import pickle 
from pickle import load


app = Flask(__name__)
Swagger(app)

model = load(open('best_model.pkl','rb')) 
poly = load(open('poly.pkl','rb'))
sc = load(open('scaler.pkl','rb'))


@app.route('/',methods = ['GET'])


def home():

    return render_template('index.html')



@app.route('/predict',methods = ['GET'])
def predict():
 
    int_feature = [float(x)  for x in request.form.values()] 

    final_feature = [np.array(int_feature)]
    arr = poly.transform(final_feature)

    scaler = sc.transform(arr)


    predict = model.predict(scaler)

    output = round(predict[0][0],3)

    return render_template('index.html', predict_text ='Prediction Will be {}'.format(output))


if __name__ == '__main__':

    app.run(debug= True)
