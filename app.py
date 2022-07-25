import sys
from flask import Flask
from insurance.logger import logging
from insurance.exception import InsuranceException
app=Flask(__name__)

@app.route("/", methods=['GET','POST'])

def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        insurance = InsuranceException(e,sys)
        #raise InsuranceException (e,sys) from e
        logging.info(insurance.error_message)
        logging.info("We are testing logging module")
    return "Starting Insurance Prediction ML Project"

if __name__=="__main__":
    app.run(debug=True)