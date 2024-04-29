import pickle
import json
import numpy as np
import config

class autism_prediction():
    def __init__(self,A1, A2, A3, A4, A5, A6, A7, A8, A9, A10,age, gender, jaundice, Family_mem_with_ASD):
        self.A1=A1
        self.A2=A2
        self.A3=A3
        self.A4=A4
        self.A5=A5
        self.A6=A6
        self.A7=A7
        self.A8=A8
        self.A9=A9
        self.A10=A10
        self.age=age
        self.gender=gender
        self.jaundice=jaundice
        self.Family_mem_with_ASD=Family_mem_with_ASD
       
        
    def load_model(self):
       
        with open(config.model_file_path,"rb") as file:
                self.model=pickle.load(file)

        with open(config.json_file_path,"r") as file:
            self.json_data=json.load(file)

    def get_prediction(self):
        self.load_model() #calling the above function
        test_a=np.zeros(len(self.json_data["columns"])) #calling the json_data_columns
        test_a[0]=self.A1
        test_a[1]=self.A2
        test_a[2]=self.A3
        test_a[3]=self.A4
        test_a[4]=self.A5
        test_a[5]=self.A6
        test_a[6]=self.A7
        test_a[7]=self.A8
        test_a[8]=self.A9
        test_a[9]=self.A10
        test_a[10]=self.age
        test_a[11]=self.gender
        test_a[12]=self.jaundice
        test_a[13]=self.Family_mem_with_ASD
       

        predict_autism=self.model.predict([test_a])
        return predict_autism