from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
import pickle
app= Flask (__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def index():
    if request.method=='POST':
        try:
            pro_temp=float(request.form['Process temp in K'])
            file='linear_task.sav'
            saved_model=pickle.load(open(file,'rb'))
            prediction=saved_model.predict([[pro_temp]])
            print('prediction is', prediction)
            return render_template('results.html',prediction=prediction)
        except Exception as e:
            print('The Exception message is',e)
            return 'Something went wrong'
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)






