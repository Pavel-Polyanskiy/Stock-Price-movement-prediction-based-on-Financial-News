 # Import the python file containing the ML model
from flask import Flask, request, render_template # Import flask libraries
import pickle
from python_version import get_all_data
model = pickle.load(open('binary_model.sav', 'rb'))
threshold = 0.36448651000920534 
import warnings
warnings.filterwarnings('ignore')
# Initialize the flask class and specify the templates directory
app = Flask(__name__,template_folder = "templates")
# Default route set as 'home'
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['GET'])
def predict_type():
    try:
        ticker = request.args.get('ticker') # Get parameters for sepal ticker
        company_name = request.args.get('company_name') # Get parameters for name
        data = get_all_data(ticker, company_name)
        res = model.predict_proba(data)[::, 1] > threshold
        if res[0] == False:
            binary_prediction = '"Fall"'
            proba = model.predict_proba(data)[::, 0][0].round(2)
        else: 
            binary_prediction = '"Rise"'
            proba = model.predict_proba(data)[::, 1][0].round(2)
        return render_template('home.html', prediction = binary_prediction, proba = proba)

    except:
         return render_template('home.html', prediction = 'Oops, check the spelling of the ticker and try again!')
if __name__=='__main__':
    app.run(port=7000)