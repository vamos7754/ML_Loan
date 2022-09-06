from re import L
import pandas as pd
import numpy as np
import json
import pickle
import sys
sys.path.append(r"D:\Velocity\DataScience\Datasets\Classification\ML_Loan_Prediction")
import config
import os
import warnings
warnings.filterwarnings('ignore')

class Loan():
    def __init__(self,credit_policy,purpose ,int_rate ,installment ,log_annual_inc ,dti ,fico ,days_with_cr_line ,
    revol_bal ,revol_util , inq_last_6mths,delinq_2yrs,pub_rec):

        self.credit_policy = credit_policy
        self.purpose = purpose
        self.int_rate = int_rate
        self.installment = installment
        self.log_annual_inc = log_annual_inc
        self.dti = dti
        self.fico = fico
        self.days_with_cr_line = days_with_cr_line
        self.revol_bal = revol_bal
        self.revol_util = revol_util
        self.inq_last_6mths = inq_last_6mths
        self.delinq_2yrs = delinq_2yrs
        self.pub_rec = pub_rec

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_result(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.credit_policy
        test_array[1] = self.json_data['purpose'][self.purpose]
        test_array[2] = self.int_rate
        test_array[3] = self.installment
        test_array[4] = self.log_annual_inc
        test_array[5] = self.dti
        test_array[6] = self.fico
        test_array[7] = self.days_with_cr_line
        test_array[8] = self.revol_bal
        test_array[9] = self.revol_util
        test_array[10] = self.inq_last_6mths
        test_array[11] = self.delinq_2yrs
        test_array[12] = self.pub_rec

        predict_result = self.model.predict([test_array])
        return predict_result

if __name__ == "__main__":
    credit_policy = 1
    purpose = 'debt_consolidation'
    int_rate = 0.2189
    installment = 829.1
    log_annual_inc = 11.350
    dti = 19.48
    fico = 737
    days_with_cr_line = 5639.95
    revol_bal = 28854
    revol_util = 52.1
    inq_last_6mths = 0
    delinq_2yrs = 0
    pub_rec = 0

    object = Loan(credit_policy,purpose ,int_rate ,installment ,log_annual_inc ,dti ,fico ,days_with_cr_line ,
    revol_bal ,revol_util , inq_last_6mths,delinq_2yrs,pub_rec)
    print(object.get_result())



