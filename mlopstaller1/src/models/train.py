from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import make_pipeline
import pandas as pd
import joblib
import os

DATA_PATH = '../../data/penguins_lter.csv'
COLUMS_TO_USE =  ["Species","Culmen Length (mm)",
                  "Culmen Depth (mm)","Flipper Length (mm)",
                  "Body Mass (g)","Sex", "Delta 15 N (o/oo)",
                  "Delta 13 C (o/oo)"]
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def train():
  print(print(os.getcwd()))
  data = pd.read_csv(DATA_PATH)
  data = data[COLUMS_TO_USE]
  data.dropna(inplace=True)
  label_encoder = LabelEncoder()
  sex_encoder = LabelEncoder()
  data['Sex'] = sex_encoder.fit_transform(data['Sex'])
  data['Species'] = label_encoder.fit_transform(data['Species'])

  X = data.drop('Species', axis=1)
  y = data['Species']

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=42)

  pipeline_RF = make_pipeline(
    StandardScaler(),
    RandomForestClassifier(n_estimators=100, random_state=42)
  )  

  pipeline_GB = make_pipeline(
    StandardScaler(), 
    GradientBoostingClassifier()
  )

  print("Training Random Forest Classifier"+
        "\n______________________________________________________________________________")
  pipeline_RF.fit(X_train, y_train)
  y_pred_rf = pipeline_RF.predict(X_test)

  report_RF = classification_report(y_test, y_pred_rf, target_names=label_encoder.classes_)

  print(report_RF)

  print("_______________________________________________________________________________\n")
  print("Training Gradient Boosting Classifier"+
        "\n_______________________________________________________________________________")

  pipeline_GB.fit(X_train, y_train)
  y_pred_gb = pipeline_GB.predict(X_test)

  report_GB = classification_report(y_test, y_pred_gb, target_names=label_encoder.classes_)

  print(report_GB)
  print("_______________________________________________________________________________\n")
  
  joblib.dump(sex_encoder, 'sex_encoder.joblib')
  joblib.dump(label_encoder, 'label_encoder.joblib')
  joblib.dump(pipeline_GB, 'gradient_boosting_model.joblib')
  joblib.dump(pipeline_RF, 'random_forest_model.joblib')
  
if __name__ == "__main__":
  train()