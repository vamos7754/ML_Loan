import re
from flask import Flask,jsonify,render_template,redirect,request,url_for
from project_data.utils import Loan
import numpy as np
import pickle 
import json
import config

app = Flask(__name__)

# *****************Login API*******************************
# @app.route('/')
# def hello_flask():
#     print("Hello Flask")
#     return jsonify({"Flask":"API"})

# # *************************Postman Check******************

# @app.route('/predict_result',methods=['POST','GET'])
# def get_result():
#     data = request.form
#     credit_policy = eval(data['credit_policy'])
#     purpose = data['purpose']
#     int_rate = eval(data['int_rate'])
#     installment = eval(data['installment'])
#     log_annual_inc = eval(data['log_annual_inc'])
#     dti = eval(data['dti'])
#     fico = eval(data['fico'])
#     days_with_cr_line = eval(data['days_with_cr_line'])
#     revol_bal = eval(data['revol_bal'])
#     revol_util = eval(data['revol_util'])
#     inq_last_6mths = eval(data['inq_last_6mths'])
#     delinq_2yrs = eval(data['delinq_2yrs'])
#     pub_rec = eval(data['pub_rec'])

#     object = Loan(credit_policy,purpose ,int_rate ,installment ,log_annual_inc ,dti ,fico ,days_with_cr_line ,
#     revol_bal ,revol_util , inq_last_6mths,delinq_2yrs,pub_rec)

#     result = object.get_result()
#     return jsonify({'Resutt':f"Predicted class for loan default is : {result}"})

# **********************HTML Check********************************
@app.route('/')
def main():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        credit_policy =  request.form['credit_policy']
        purpose = request.form['purpose']
        int_rate = request.form['int_rate']
        installment = request.form['installment']
        log_annual_inc = request.form['log_annual_inc']
        dti = request.form['dti']
        fico = request.form['fico']
        days_with_cr_line = request.form['days_with_cr_line']
        revol_bal = request.form['revol_bal']
        revol_util = request.form['revol_util']
        inq_last_6mths = request.form['inq_last_6mths']
        delinq_2yrs = request.form['delinq_2yrs']
        pub_rec = request.form['pub_rec']

        object = Loan(credit_policy,purpose ,int_rate ,installment ,log_annual_inc ,dti ,fico ,days_with_cr_line ,
        revol_bal ,revol_util , inq_last_6mths,delinq_2yrs,pub_rec)
        result = object.get_result()
        return render_template("result.html",result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
