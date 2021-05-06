from flask import Flask, request, render_template
import numpy as np
import flasgger 
from flasgger import Swagger



import pickle


app = Flask(__name__)
Swagger(app)

model = pickle.load(open('best_model.pkl','rb')) 
poly = pickle.load(open('poly.pkl', 'rb'))
sc = pickle.load(open('scaler.pkl','rb'))



@app.route('/')





@app.route('/',methods = ['GET'])
def predict():
 
    l=[]

    i1 = request.args.get('Frequency ')
    l.append(i1)

    i2 = request.args.get('Angle ')
    l.append(i2)

    i3 = request.args.get('Chord Length')
    l.append(i3)

    i4 = request.args.get('Velocity ')
    l.append(i4)

    i5 = request.args.get('Sucction')
    l.append(i5)

    arr = np.array([l])
    print('3')
    arr = poly.transform(arr)
    print('4')
    scale_arr = sc.transform(arr)
    print('5')
    p = round(model.predict(scale_arr)[0][0],2)
    print('&')

    return ('Pressue level is : '+str(p) )





if __name__ == '__main__':

    app.run(debug= True)



from flask import Flask, request, render_template
import numpy as np
import flasgger 
from flassgger import Swagger



import pickle


app = Flask(__name__)
Swagger(app)

model = pickle.load(open('best_model.pkl','rb')) 
poly = pickle.load(open('poly.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl'),'rb')



@app.route('/')


def home():

    return render_template('index.html')



@app.route('/predict',methods = ['POST'])
def predict():
 
    int_feature = [float(x)  for x in request.form.values()] 

    final_feature = [np.array(int_feature)]



    predict = model.predict(final_feature)

    output = round(predict[0],3)

    return render_template('index.html', predict_text ='Prediction Will be {}'.format(output))


if __name__ == '__main__':

    app.run(debug= True)
