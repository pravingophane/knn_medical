import json
import pickle
import pandas as pd
import numpy as np
import config


class MedicalInsurance():
    def __init__(self, age, sex, bmi, children, smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = "region_" + region


    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.ori_model =  pickle.load(f)

        with open(config.SCALAR_FILE_PATH, "rb") as f:
            self.scalar =  pickle.load(f)    
        
        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_predicted_premium(self):

        self.load_model()

        region_index = self.json_data['columns'].index(self.region)

        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.age
        array[1] = self.json_data['sex'][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.json_data['smoker'][self.smoker]
        array[region_index] = 1
        
        print("Test array-->\n",array)
        test_array = self.scalar.transform([array])
        print("test array",test_array)


        predicted_premium = self.ori_model.predict([array])[0]
        print("Predicted_premium", predicted_premium)
        return np.around(predicted_premium,2)


if __name__ == "__main__":

    age = 45
    sex = 'male'
    bmi = 22.3
    children = 3
    smoker = 'no'
    region = 'southwest'

    life_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    premium = life_ins.get_predicted_premium()
    print()
    print(f"Predicted Insurance Premium is {premium}/- Rs. Only")