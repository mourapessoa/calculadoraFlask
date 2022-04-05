import flask

from flask import Flask,render_template

app=Flask(__name__)

@app.route('/matheus', methods=['GET'])

def calculate():

   if soma(v1, v2):
      return v1+v2 
   elif subtracao(v1, v2):
      return v1-v2
   elif divisao(v1, v2):
        return v1/v2 
   elif multiplicacao(v1, v2): 
      return v1*v2
      
    else:  return render_template("calculadora.html")