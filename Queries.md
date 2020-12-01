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

    # season_id = Column(Integer)
    # team_id = Column(Integer)
    # team_abbreviation = Column(String(10)) 
    # team_name = Column(String(30)) 
    # game_id = Column(Integer, primary_key=True) 
    # game_date = Column(String) 
    # matchup = Column(String(30)) 
    # wl = Column(String(10)) 
    # min = Column(Integer) 
    # pts = Column(Integer) 
    # fgm = Column(Integer) 
    # fga = Column(Integer)
    # fg_pct = Column(Float) 
    # fg3m = Column(Integer) 
    # fg3a = Column(db.Integer)
    # fg3_pct = Column(Float)
    # ftm = Column(Integer)
    # fta = Column(Integer) 
    # ft_pct = Column(Float) 
    # oreb = Column(Integer)
    # dreb = Column(Integer) 
    # reb = Column(Integer) 
    # ast = Column(Integer) 
    # stl = Column(Integer) 
    # blk = Column(Integer)
    # tov = Column(Integer)
    # pf = Column(Integer)
    # plus_minus = Column(Float)
    # is_win = Column(Integer)
    # is_loss = Column(Integer)
    # home_away = Column(String(10))
    # opponent = Column(String(10))

db.create_all()
    

@app.route("/")
def main():
    return "NBA DATA ANALYTICS"

@app.route("/data")
def data():
    data = db.seasons.query.all()
    return jsonify([d.to_dict() for d in data])

if __name__ == "__main__":
    app.run(debug=True)