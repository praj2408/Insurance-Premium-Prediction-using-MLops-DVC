
# Internship - Ineuron
## Insurance Premium Prediction Using MLOps & CiCd
The goal of this project is to give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. This can assist a person in concentrating on the health side of an
insurance policy rather than the ineffective part.

## Website Link
https://insurance-premium-price-prediction.onrender.com/

![](https://github.com/praj2408/Insurance-Premium-Prediction-cicd/blob/main/static/img/Insurance%20Premium%20Prediction.gif)
### Dataset
[Dataset](https://www.kaggle.com/noordeen/insurance-premium-prediction) is provided by Ineuron

## MLOps Level 1: ML Pipeline Automation Architecture
The goal of level 1 is to perform continuous training of the model by automating the ML pipeline; this lets you achieve continuous delivery of model prediction service. To automate the process of using new data to retrain models in production, you need to introduce automated data and model validation steps to the pipeline, as well as pipeline triggers and metadata management.

The following figure is a schematic representation of an automated ML pipeline for CT.
![](https://github.com/praj2408/ETE-Protect/blob/main/images/ML%20pipeline%20automation.jpg)

## MLOps Level 2: CI/CD pipeline automation
For a rapid and reliable update of the pipelines in production, you need a robust automated CI/CD system. This automated CI/CD system lets your data scientists rapidly explore new ideas around feature engineering, model architecture, and hyperparameters. They can implement these ideas and automatically build, test, and deploy the new pipeline components to the target environment.

The following diagram shows the implementation of the ML pipeline using CI/CD, which has the characteristics of the automated ML pipelines setup plus the automated CI/CD routines.
![](https://github.com/praj2408/ETE-Protect/blob/main/images/cicd%20pipeline%20automation.jpg)


## Model information
The machine learning model used in this project is a catboost regression model, which was trained using scikit-learn. The model takes in demographic and medical information about an individual and predicts their insurance premium.

## Results and analysis

After training the model, we achieved an R-squared value of 0.88 (88% accuracy) on the test data, indicating a moderate level of predictive power. We also created visualizations to explore the relationships between different features and insurance premiums.

## Installation
To run the code, first clone this repository and navigate to the project directory:
```
git clone https://github.com/your-username/insurance-premium-prediction.git
```
Create a virtual environment
```
conda create -p venv python==3.8 -y
conda activate venv/
```
To run this project, you will need python packages present in the requirements file
```
pip install -r requirements.txt
```

Then, run the `app.py` file to start the Flask web application:
```
python app.py
```
### Tox Command
Tox aims to automate and standardize testing in Python. It is part of a larger vision of easing the packaging, testing and release process of Python
```bash
[tox]
   envlist=py37
   [testenv]
   deps=pytest
   command=pytest -v
```
### For rebuilding
``` tox -r ```

### Pytest
```pytest -v```
Used for testing purposes. You can use pip install pytest and pip install tox

### Setup
```pip install -e```

### Package building
``` python setup.py sdist bdist_wheel```

### Hands on commands for testing
```dvc repro```
```dvc metrics show```
Use logging libraries for making logs

### Testing
while testing your file names must contains the word test in it. For ex: xyztest.py or configtest.py

After writing code, run pytest -v and see all test cases done

### Web deployment
Flask for backend and HTML, CSS, for frontend
all the code are given in app.py

## Contributions
Contributions to this project are welcome! To contribute, please follow the standard GitHub workflow for pull requests.

## Contact information
If you have any questions or comments about this project, feel free to contact the project maintainer at prajwalgbdr03@gmail.com.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Run the project
- Clone the project
- pip install -r requirements.txt
- python app.py
Enjoy the project in a local host
