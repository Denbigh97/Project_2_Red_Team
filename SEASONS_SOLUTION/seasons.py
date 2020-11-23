from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
from config import URI  
import pandas as pd
from sqlalchemy import create_engine


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = URI

db = SQLAlchemy(app)

ROOT = "./Data"
CONN = os.getenv("CONN")
print(CONN)
engine = create_engine(CONN)

for file in os.listdir(ROOT):
    filepath = os.path.join(ROOT, file)
    table_name = os.path.splitext(file) [0]
    print(filepath)
    print(table_name)
    pd.read_csv(filepath).to_sql(table_name, con=engine, index=False, if_exists="replace")



@app.route("/")
def main():
    return "NBA DATA ANALYTICS"



if __name__ == "__main__":
    app.run(debug=True)