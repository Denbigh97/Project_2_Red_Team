from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_cors import CORS
import csv
import os
from config import URI  
import pandas as pd
from sqlalchemy import create_engine


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

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
    
class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }
class seasons(db.Model, DictMixIn):
    __tablename__ = "Cleaned_data11.21"
    
    season_id = db.Column(db.Integer)
    team_id= db.Column(db.Integer)
    team_abbreviation = db.Column(db.String(10)) 
    team_name = db.Column(db.String(30)) 
    game_id = db.Column(db.Integer, primary_key=True) 
    game_date = db.Column(db.String) 
    matchup = db.Column(db.String(30)) 
    wl = db.Column(db.String(10)) 
    min = db.Column(db.Integer) 
    pts = db.Column(db.Integer) 
    fgm = db.Column(db.Integer) 
    fga = db.Column(db.Integer)
    fg_pct = db.Column(db.Float) 
    fg3m = db.Column(db.Integer) 
    fg3a = db.Column(db.Integer)
    fg3_pct = db.Column(db.Float)
    ftm = db.Column(db.Integer)
    fta = db.Column(db.Integer) 
    ft_pct = db.Column(db.Float) 
    oreb = db.Column(db.Integer)
    dreb = db.Column(db.Integer) 
    reb = db.Column(db.Integer) 
    ast = db.Column(db.Integer) 
    stl = db.Column(db.Integer) 
    blk = db.Column(db.Integer)
    tov = db.Column(db.Integer)
    pf = db.Column(db.Integer)
    plus_minus = db.Column(db.Float)
    is_win = db.Column(db.Integer)
    is_loss = db.Column(db.Integer)
    home_away = db.Column(db.String(10))
    opponent = db.Column(db.String(10))

db.create_all()
    

@app.route("/")
def main():
    return "NBA DATA ANALYTICS"

@app.route("/data")
def data():
    data = seasons.query.all()
    return jsonify([{"season_id": Cleaned_data1121.season_id, "team_id": Cleaned_data1121.team_id} for seasons in data])

if __name__ == "__main__":
    app.run(debug=True)