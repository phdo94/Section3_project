import joblib
import pandas as pd

df = pd.read_csv('/Users/parkheondo/Downloads/test_scores.csv')

new_df = df.drop(['posttest', 'student_id'], axis=1)

my_model = joblib.load('/Users/parkheondo/Desktop/Codestates_AI/AI_02S3/Section3_project/flask_app/project.pkl')

sample = pd.DataFrame(new_df.iloc[1]).transpose()

predict = my_model.predict(sample)

print(round(float(predict), 2))