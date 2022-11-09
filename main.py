#from gettext import npgettext
import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request
from Medical_insurance.utils import MedicalInsurance
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Pridict premium of insurance")    
    return render_template("index.html")

@app.route('/predict_premium', methods = ["POST"])
def get_insurance_premium():

 
        data = request.form
        print("Data::",data)

        # age = eval(data['age'])
        # sex = data['sex']
        # bmi = eval(data['bmi'])
        # children = eval(data['children'])
        # smoker = data['smoker']
        # region = data['region']

    #     age = eval(request.args.get("age"))
    #     sex = request.args.get("sex")
    #     bmi = eval(request.args.get("bmi"))
    #     children = request.args.get("children")
    #     smoker = request.args.get("smoker")
    #     region = request.args.get("region")

    #     print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)
 
    #     life_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    #     premium = life_ins.get_predicted_premium()

    #     return render_template("index.html",prediction = premium)
    #     #return jsonify({"Result" : f"Predicted Insurance Premium is {premium}/- Rs. Only"})

    # else:

        #print("We are using POST Method")

        age = eval(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = eval(request.form.get("bmi"))
        children = request.form.get("children")
        smoker = request.form.get("smoker")
        region = request.form.get("region")

        print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)
 
        life_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        premium = life_ins.get_predicted_premium()   

        #return jsonify({"Result" : f"Predicted Insurance Premium is {premium}/- Rs. Only"})
        return render_template("index.html", prediction = premium)

     

    
if __name__ == "__main__":
    app.run(host='0.0.0.0' , port = config.PORT_NUMBER, debug=True)