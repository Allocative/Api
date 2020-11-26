from flask import Flask,request,jsonify

app = Flask(__name__)

app.debug = True


@app.route('/')
def MainMethod():
   data =  {
       'data':'Machine Learning Model Training'
   }
   return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)