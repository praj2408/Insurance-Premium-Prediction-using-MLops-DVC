import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    os.path.join(".github", "workflow"),
    "data_given",
    "reports",
    "prediction_service",
    "notebooks",
    "saved_models",
    "src",
    "saved_models",
    "tests",
    "webapp",
    os.path.join("webapp", "static", "css"),
    os.path.join("webapp", "static", "scripts"),
    os.path.join("webapp", "templates"),
     
]


for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


files =  [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    "app.py",
    "requirements.txt",
    "setup.py",
    "tox.ini",


    os.path.join("src","__init__.py"),
    os.path.join("src","get_data.py"),
    os.path.join("src","load_data.py"),
    os.path.join("src","split_data.py"),
    os.path.join("src","train_and_evaluate.py"),


    os.path.join("prediction_service","__init__.py"),    
    os.path.join("prediction_service","prediction.py"), 
    
    
    os.path.join("report","params.json"), 
    os.path.join("report","scores.json"),

    os.path.join("tests","__init__.py"),
    os.path.join("tests","conftest.py"),
    os.path.join("tests","test_config.py"),



]

for file in files:
    with open(file, "w") as f:
        pass