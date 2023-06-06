from distutils.log import debug
from re import template
from urllib import response
from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import numpy as np
import pandas as pd
import logging
from src.get_data import read_params
import inflect

logging.basicConfig(format='%(message)s', level=logging.INFO)
params_path = 'params.yaml'
webapp_root = 'webapp'
# static folder
static_dir = os.path.join(webapp_root, 'static')
template_dir = os.path.join(webapp_root, 'templates')

logging.info("directory management snippet")
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def predict(data):
    try:
        config = read_params(params_path)
        model_dir_path = config["webapp_model_dir"]
        model = joblib.load(model_dir_path)
        prediction = model.predict(data)
        print(prediction)
        return prediction
    except Exception as e:
        logging.info("Error is detected ", str(e))

logging.info("predictive model demonstration")


def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response": response}
        return jsonify(response)

    except Exception as e:
        print(e)
        error = {"error": "something went wrong"}
        return error

logging.info("start flask app")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        try:
           if request.form:

                age = int(request.form.get("age"))
                sex = (request.form.get("sex"))
                if(sex == "female"):
                    sex = 0
                else:
                    sex = 1
                bmi = float(request.form.get("bmi"))
                children = request.form.get("children")
                smoker = request.form.get("smoker")
                if(smoker == "no"):
                     smoker = 0
                else:
                    smoker = 1
                region = request.form.get("region")
                if region == "SouthWest":
                    region = 0
                elif region == "SouthEast":
                    region = 1
                elif region == "NorthWest":
                    region = 2
                else:
                    region = 3

                response = predict(pd.DataFrame([[age, sex, bmi, children, smoker, region]], columns=[
                                   'age', 'sex', 'bmi', 'children', 'smoker', 'region']))
                final_val = "{:.2f}".format(response[0])
                ans = inflect.engine()
                final_ans=ans.number_to_words(final_val)

                return render_template("home.html", response_int=final_val,response=str(final_ans))
           elif request.json:
                response = api_response(request)
                # converted into json format
                return jsonify(response)

           

        except Exception as e:
            print(e)
            error = {"error":"Something went wrong"}
            error = {"error":e}

            return render_template("error.html",error=error)

    else:
        return render_template('home.html')
logging.info("run the flask app")
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)

# Workflows. A workflow is a configurable automated process that will run one or more jobs. 
# Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository,
#  or they can be triggered manually, or at a defined schedule.

# mkdit .github/workflows