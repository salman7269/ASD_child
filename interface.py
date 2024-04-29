from flask import Flask,request,jsonify,render_template
import config
from utils import autism_prediction
import numpy as np

app=Flask(__name__)
@app.route("/")
def get_homepage():
    return render_template("homepage.html")

@app.route("/prediction",methods= ["POST","GET"])
def get_prediction():
    if request.method == "POST":
        data = request.form
        print("User Input Data: ",data)
        A2=data.get("A2")
        A1=data.get("A1")
        A3=data.get("A3")
        A4=data.get("A4")
        A5=data.get("A5")
        A6=data.get("A6")
        A7=data.get("A7")
        A8=data.get("A8")
        A9=data.get("A9")
        A10=data.get("A10")
        age=eval(data.get("age"))
        gender=(data.get("gender"))
        jaundice=(data.get("jaundice"))
        Family_mem_with_ASD=str((data.get("Family_mem_with_ASD")))  
        # Score=int(data.get("Score"))
        
        obj=autism_prediction(A1, A2, A3, A4, A5, A6, A7, A8, A9, A10,age, gender, jaundice, Family_mem_with_ASD)
        autism=obj.get_prediction()
        autism_lst=autism.tolist()
        return  jsonify({"Result":f"Predicted: {autism_lst}"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT_NUMBER, debug=False)


