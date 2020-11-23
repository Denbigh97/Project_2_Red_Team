# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# import datetime
# import os
# from config import URI 
# import pandas as pd
# from sqlalchemy import create_engine


# app = Flask(__name__)

# # nba = []

# app.config["SQLALCHEMY_DATABASE_URI"] = URI


# db = SQLAlchemy(app)

# ROOT = "./Data"
# CONN = os.getenv("CONN")
# print(CONN) 
# engine = create_engine(CONN)

# for file in os.listdir(ROOT):
#     filepath = os.path.join(ROOT, file)
#     table_name = os.path.splitext(file)[0]
#     print(filepath)
#     print(table_name)
#     pd.read_csv(filepath).to_sql(table_name, con=engine, index=False, if_exists="replace")

# # class teams(db.Model):
# #     season_id = db.Column(db.Float)
# #     team_id= db.Column(db.Float)
# #     team_abbreviation = db.Column(db.String(10)) 
# #     team_name = db.Column(db.String(30)) 
# #     game_id = db.Column(db.Integer, primary_key=True) 
# #     game_date = db.Column(db.Date) 
# #     matchup = db.Column(db.String(30)) 
# #     wl = db.Column(db.String(10)) 
# #     min = db.Column(db.Float) 
# #     pts = db.Column(db.Float) 
# #     fgm = db.Column(db.Float) 
# #     fga = db.Column(db.Float)
# #     fg_pct = db.Column(db.Float) 
# #     fg3m = db.Column(db.Float) 
# #     fg3a = db.Column(db.Float)
# #     fg3_pct = db.Column(db.Float)
# #     ftm = db.Column(db.Float)
# #     fta = db.Column(db.Float) 
# #     ft_pct = db.Column(db.Float) 
# #     oreb = db.Column(db.Float)
# #     dreb = db.Column(db.Float) 
# #     reb = db.Column(db.Float) 
# #     ast = db.Column(db.Float) 
# #     stl = db.Column(db.Float) 
# #     blk = db.Column(db.Float)
# #     tov = db.Column(db.Float)
# #     pf = db.Column(db.Float)
# #     plus_minus = db.Column(db.Float)
# #     is_win = db.Column(db.Float)
# #     is_loss = db.Column(db.Float)
# #     home_away = db.Column(db.String(10))
# #     opponent = db.Column(db.String(10))

# #     # def to_dict(self):
# #     #     return {
# #     #         column.name: getattr(self, column.name)
# #     #         if not isinstance(
# #     #             getattr(self, column.name), (datetime.datetime, datetime.date)
# #     #         )
# #     #         else getattr(self, clomun.name).isoformat()
# #     #         for column in self. __table__.columns
# #     #     }

# # class season_atl(db.Model):
# #     season_id = db.Column(db.Float)
# #     team_id= db.Column(db.Float)
# #     team_abbreviation = db.Column(db.String(10)) 
# #     team_name = db.Column(db.String(30)) 
# #     game_id = db.Column(db.Integer, primary_key=True) 
# #     game_date = db.Column(db.Date) 
# #     matchup = db.Column(db.String(30)) 
# #     wl = db.Column(db.String(10)) 
# #     min = db.Column(db.Float) 
# #     pts = db.Column(db.Float) 
# #     fgm = db.Column(db.Float) 
# #     fga = db.Column(db.Float)
# #     fg_pct = db.Column(db.Float) 
# #     fg3m = db.Column(db.Float) 
# #     fg3a = db.Column(db.Float)
# #     fg3_pct = db.Column(db.Float)
# #     ftm = db.Column(db.Float)
# #     fta = db.Column(db.Float) 
# #     ft_pct = db.Column(db.Float) 
# #     oreb = db.Column(db.Float)
# #     dreb = db.Column(db.Float) 
# #     reb = db.Column(db.Float) 
# #     ast = db.Column(db.Float) 
# #     stl = db.Column(db.Float) 
# #     blk = db.Column(db.Float)
# #     tov = db.Column(db.Float)
# #     pf = db.Column(db.Float)
# #     plus_minus = db.Column(db.Float)
# #     is_win = db.Column(db.Float)
# #     is_loss = db.Column(db.Float)
# #     home_away = db.Column(db.String(10))
# #     opponent = db.Column(db.String(10))

# #     # def to_dict(self):
# #     #     return {
# #     #         column.name: getattr(self, column.name)
# #     #         if not isinstance(
# #     #             getattr(self, column.name), (datetime.datetime, datetime.date)
# #     #         )
# #     #         else getattr(self, clomun.name).isoformat()
# #     #         for column in self. __table__.columns
# #     #     }


# # class season_gsw(db.Model):
# #     season_id = db.Column(db.Float)
# #     team_id= db.Column(db.Float)
# #     team_abbreviation = db.Column(db.String(10)) 
# #     team_name = db.Column(db.String(30)) 
# #     game_id = db.Column(db.Integer, primary_key=True) 
# #     game_date = db.Column(db.Date) 
# #     matchup = db.Column(db.String(30)) 
# #     wl = db.Column(db.String(10)) 
# #     min = db.Column(db.Float) 
# #     pts = db.Column(db.Float) 
# #     fgm = db.Column(db.Float) 
# #     fga = db.Column(db.Float)
# #     fg_pct = db.Column(db.Float) 
# #     fg3m = db.Column(db.Float) 
# #     fg3a = db.Column(db.Float)
# #     fg3_pct = db.Column(db.Float)
# #     ftm = db.Column(db.Float)
# #     fta = db.Column(db.Float) 
# #     ft_pct = db.Column(db.Float) 
# #     oreb = db.Column(db.Float)
# #     dreb = db.Column(db.Float) 
# #     reb = db.Column(db.Float) 
# #     ast = db.Column(db.Float) 
# #     stl = db.Column(db.Float) 
# #     blk = db.Column(db.Float)
# #     tov = db.Column(db.Float)
# #     pf = db.Column(db.Float)
# #     plus_minus = db.Column(db.Float)
# #     is_win = db.Column(db.Float)
# #     is_loss = db.Column(db.Float)
# #     home_away = db.Column(db.String(10))
# #     opponent = db.Column(db.String(10))
    
# # db.create_all()



# # Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
# # engine = sqlalchemy.create_engine(URI)
# # con = engine.connect()

# # # Verify that there are no existing tables
# # print(engine.table_names())

# # table_name = 'teams'
# # df.to_sql(table_name, con)

# @app.route("/")
# def main():
#     return "NBA DATA ANALYTICS"

# # @app.route("/Atlanta_Hawks")
# # def show_atl():
# #     seasons_atl = season_atl.query.all() 
# #     return jsonify([{"season_id":  season_atl.season_id, "team_id": season_atl.team_id,
# #     "team_abbreviation": season_atl.team_abbreviation, 
# #     "team_name": season_atl.team_name, 
# #     "game_id": season_atl.game_id, 
# #     "game_date": season_atl.game_date, 
# #     "matchup": season_atl.matchup, 
# #     "wl": season_atl.wl, 
# #     "min": season_atl.min, 
# #     "pts": season_atl.pts, 
# #     "fgm": season_atl.fgm, 
# #     "fga": season_atl.fga,
# #     "fg_pct": season_atl.fg_pct, 
# #     "fg3m": season_atl.fg3m, 
# #     "fg3a": season_atl.fg3m,
# #     "fg3_pct": season_atl.fg3_pct,
# #     "ftm": season_atl.ftm,
# #     "fta": season_atl.fta, 
# #     "ft_pct": season_atl.ft_pct, 
# #     "oreb": season_atl.oreb,
# #     "dreb": season_atl.dreb, 
# #     "reb": season_atl.reb, 
# #     "ast": season_atl.ast, 
# #     "stl": season_atl.stl, 
# #     "blk": season_atl.blk,
# #     "tov": season_atl.tov,
# #     "pf": season_atl.pf,
# #     "plus_minus": season_atl.plus_minus,
# #     "is_win": season_atl.is_win,
# #     "is_loss": season_atl.is_loss,
# #     "home_away": season_atl.home_away,
# #     "opponent": season_atl.opponent} for season_atl in seasons_atl])




# # @app.route("/search")
# # def query_by_age():

# #     min_age = request.args.get("min_age")
# #     max_age = request.args.get("max_age")
# #     name = request.args.get("name")

# #     q = Pet.query

# #     if min_age:
# #         q = q.filter(Pet.age >= int(min_age))

# #     if max_age:
# #         q = q.filter(Pet.age <= int(max_age))

# #     if name:
# #         q = q.filter(Pet.name == name)

# #     pets = q.all()
# #     return jsonify([pet.to_dict() for pet in pets])


# if __name__ == "__main__":
#     app.run(debug=True)

