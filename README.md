
# Internship - Ineuron
## Insurance Premium Prediction Using MLOps & CiCd
The goal of this project is to give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. This can assist a person in concentrating on the health side of an
insurance policy rather than the ineffective part.

## Website Link
https://insurance-premium-price-prediction.onrender.com/

![](https://github.com/praj2408/Insurance-Premium-Prediction-cicd/blob/main/static/img/Insurance%20Premium%20Prediction.gif)
### Dataset
[Dataset](https://www.kaggle.com/noordeen/insurance-premium-prediction) is provided by Ineuron

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

## Model information
The machine learning model used in this project is a catboost regression model, which was trained using scikit-learn. The model takes in demographic and medical information about an individual and predicts their insurance premium.

## Results and analysis

After training the model, we achieved an R-squared value of 0.88 (88% accuracy) on the test data, indicating a moderate level of predictive power. We also created visualizations to explore the relationships between different features and insurance premiums.

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
