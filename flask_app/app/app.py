
from flask import Flask, abort, jsonify, request, render_template
from sklearn.externals import joblib
import numpy as np
import json
import pandas as pd
# load the built-in model 


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/getdelay', methods=['POST','GET'])
def get_delay():
    result=request.form
    int_rate=result['int_rate']
    annual_inc=result['annual_inc']
    term_60_months=result['term_ 60 months']
    tot_cur_bal=result['tot_cur_bal']
    total_rev_hi_lim=result['total_rev_hi_lim']
    grade_B=result['grade_B']
    grade_D=result['grade_D']
    grade_E=result['grade_E']
    grade_F=result['grade_F']
    verification_status_Verified=result['verification_status_Verified']
    inq_last_6mths=result['inq_last_6mths']
    initial_list_status_w=result['initial_list_status_w']
    loan_income_ratio=result['loan_income_ratio']
    user_input={'int_rate':int_rate,'term_ 60 months':term_60_months,'loan_income_ratio':loan_income_ratio,'initial_list_status_w':initial_list_status_w,'annual_inc':annual_inc,'tot_cur_bal':tot_cur_bal,'total_rev_hi_lim':total_rev_hi_lim,'grade_B':grade_B,'grade_D':grade_D,'grade_E':grade_E,'grade_F':grade_F,'verification_status_Verified':verification_status_Verified,'inq_last_6mths':inq_last_6mths,'initial_list_status_w':initial_list_status_w}
    log_model = joblib.load('Log.pkl')
    df=pd.DataFrame(data=user_input,index=[0])
    prediction=log_model.predict(df)
    if prediction ==1:
       return render_template('result.html')
    if prediction ==0:
       return render_template('result2.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)