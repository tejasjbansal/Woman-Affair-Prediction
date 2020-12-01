#Let's start with importing necessary libraries
import pickle
import numpy as np
import pandas as pd

class predObj:

    def predict_log(self, dict_pred):

        with open("modelForPrediction.sav", 'rb') as f:
            model = pickle.load(f)

        predict = model.predict(dict_pred)
        predict2 = model.predict_proba(dict_pred)
        if predict[0] ==1 :
            result = "Positive!! You have an Affair with probability of {} ".format(predict2[0][1])
        else:
            result ="Negative!! You don't have any affair with probability of {} ".format(predict2[0][0])

        return result



