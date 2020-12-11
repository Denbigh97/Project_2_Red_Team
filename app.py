from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_cors import CORS
import csv
import os
# from config import URI  
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__, template_folder="templates")
# app = Flask(__name__)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

URI = os.getenv("URI")

app.config["SQLALCHEMY_DATABASE_URI"] = URI

db = SQLAlchemy(app)

# ROOT = "./Data"
# CONN = os.getenv("CONN")

# engine = create_engine(CONN)


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
    __tablename__ = "cleaned_data1121"
    
    season_id = db.Column(db.Integer)
    team_id = db.Column(db.Integer)
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

    
@app.route("/")
def home():
    """Serve homepage template."""
    return render_template("index.html")   

@app.route("/templates/analysis.html")
def analysis():
    return render_template("analysis.html")

@app.route("/templates/team.html")
def team():
    return render_template("team.html")   

@app.route("/templates/hawks.html")
def hawks():
    return render_template("hawks.html")

@app.route("/templates/celtics.html")
def celtics():
    return render_template("celtics.html")

@app.route("/templates/nets.html")
def nets():
    return render_template("nets.html")

@app.route("/templates/hornets.html")
def hornets():
    return render_template("hornets.html")

@app.route("/templates/bulls.html")
def bulls():
    return render_template("bulls.html")

@app.route("/templates/cavaliers.html")
def cavaliers():
    return render_template("cavaliers.html")

@app.route("/templates/mavericks.html")
def mavericks():
    return render_template("mavericks.html")

@app.route("/templates/nuggets.html")
def nuggets():
    return render_template("nuggets.html")

@app.route("/templates/pistons.html")
def pistons():
    return render_template("pistons.html")

@app.route("/templates/warriors.html")
def warriors():
    return render_template("warriors.html")

@app.route("/templates/rockets.html")
def rockets():
    return render_template("rockets.html")

@app.route("/templates/pacers.html")
def pacers():
    return render_template("pacers.html")

@app.route("/templates/clippers.html")
def clippers():
    return render_template("clippers.html")

@app.route("/templates/lakers.html")
def lakers():
    return render_template("lakers.html")

@app.route("/templates/grizzlies.html")
def grizzlies():
    return render_template("grizzlies.html")

@app.route("/templates/heat.html")
def heat():
    return render_template("heat.html")

@app.route("/templates/bucks.html")
def bucks():
    return render_template("bucks.html")

@app.route("/templates/timberwolves.html")
def timberwolves():
    return render_template("timberwolves.html")

@app.route("/templates/pelicans.html")
def pelicans():
    return render_template("pelicans.html")

@app.route("/templates/knicks.html")
def knicks():
    return render_template("knicks.html")

@app.route("/templates/thunder.html")
def thunder():
    return render_template("thunder.html")

@app.route("/templates/magic.html")
def magic():
    return render_template("magic.html")

@app.route("/templates/76ers.html")
def Phi():
    return render_template("76ers.html")

@app.route("/templates/suns.html")
def suns():
    return render_template("suns.html")

@app.route("/templates/blazers.html")
def blazers():
    return render_template("blazers.html")

@app.route("/templates/kings.html")
def kings():
    return render_template("kings.html")

@app.route("/templates/spurs.html")
def spurs():
    return render_template("spurs.html")

@app.route("/templates/raptors.html")
def raptors():
    return render_template("raptors.html")

@app.route("/templates/jazz.html")
def jazz():
    return render_template("jazz.html")

@app.route("/templates/wizards.html")
def wizards():
    return render_template("wizards.html")

@app.route("/templates/Players2015_2016.html")
def player1():
    return render_template("Players2015_2016.html")

@app.route("/templates/Players2016_2017.html")
def player2():
    return render_template("Players2016_2017.html")

@app.route("/templates/Players2017_2018.html")
def player3():
    return render_template("Players2017_2018.html")

@app.route("/templates/Players2018_2019.html")
def player4():
    return render_template("Players2018_2019.html")

@app.route("/templates/Players2019_2020.html")
def player5():
    return render_template("Players2019_2020.html")

@app.route("/templates/season_15_16.html")
def season1():
    return render_template("season_15_16.html") 

@app.route("/templates/season_16_17.html")
def season2():
    return render_template("season_16_17.html") 

@app.route("/templates/season_17_18.html")
def season3():
    return render_template("season_17_18.html") 

@app.route("/templates/season_18_19.html")
def season4():
    return render_template("season_18_19.html") 

@app.route("/templates/season_19_20.html")
def season5():
    return render_template("season_19_20.html") 





# @app.route("/data")
# def data():
#     data = seasons.query.all()
#     return jsonify([{"season_id": season.season_id, "team_id": season.team_id} for season in data])


@app.route("/HOU_Away")
def query_by_hou_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(  
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Houston Rockets"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/HOU_Home")
def query_by_hou_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Houston Rockets"
            and season.home_away == "Home"
           
                        
        ]
        
    )


@app.route("/LAC_Away")
def query_by_lac_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Los Angeles Clippers"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/LAC_Home")
def query_by_lac_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Los Angeles Clippers"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/POR_Away")
def query_by_por_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Portland Trail Blazers"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/POR_Home")
def query_by_por_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Portland Trail Blazers"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/WAS_Away")
def query_by_was_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Washington Wizards"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/WAS_Home")
def query_by_was_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Washington Wizards"
            and season.home_away == "Home"
           
                        
        ]
        
    )
@app.route("/BOS_Away")
def query_by_bos_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Boston Celtics"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/BOS_Home")
def query_by_bos_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Boston Celtics"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/LAL_Away")
def query_by_lal_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Los Angeles Lakers"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/LAL_Home")
def query_by_lal_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Los Angeles Lakers"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/CLE_Away")
def query_by_cle_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Cleveland Cavaliers"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/CLE_Home")
def query_by_cle_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Cleveland Cavaliers"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/DLA_Away")
def query_by_dla_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Dallas Mavericks"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/DLA_Home")
def query_by_dla_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Dallas Mavericks"
            and season.home_away == "Home"
           
                        
        ]
        
    )
@app.route("/NJN_Away")
def query_by_njn_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "New Jersey Nets"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/NJN_Home")
def query_by_njn_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "New Jersey Nets"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/IND_Away")
def query_by_ind_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Indiana Pacers"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/IND_Home")
def query_by_ind_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Indiana Pacers"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/MEM_Away")
def query_by_mem_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Memphis Grizzlies"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/MEM_Home")
def query_by_mem_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Memphis Grizzlies"
            and season.home_away == "Home"
           
                        
        ]
        
    )   

@app.route("/MIN_Away")
def query_by_min_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Minnesota Timberwolves"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/MIN_Home")
def query_by_min_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Minnesota Timberwolves"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/DET_Away")
def query_by_det_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Detroit Pistons"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/DET_Home")
def query_by_det_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Detroit Pistons"
            and season.home_away == "Home"
           
                        
        ]
        
    )


@app.route("/NOH_Away")
def query_by_noh_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "New Orleans Hornets"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/NOH_Home")
def query_by_noh_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "New Orleans Hornets"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/NYK_Away")
def query_by_nyk_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "New York Knicks"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/NYK_Home")
def query_by_nyk_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "New York Knicks"
            and season.home_away == "Home"
           
                        
        ]
        
    )
@app.route("/ATL_Away")
def query_by_atl_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Atlanta Hawks"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/ATL_Home")
def query_by_atl_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Atlanta Hawks"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/DEN_Away")
def query_by_den_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Denver Nuggets"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/DEN_Home")
def query_by_den_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Denver Nuggets"
            and season.home_away == "Home"
           
                        
        ]
        
    )


@app.route("/MIA_Away")
def query_by_mia_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Miami Heat"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/MIA_Home")
def query_by_mia_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Miami Heat"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/ORL_Away")
def query_by_orl_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Orlando Magic"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/ORL_Home")
def query_by_orl_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Orlando Magic"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/PHX_Away")
def query_by_phx_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Phoenix Suns"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/PHX_Home")
def query_by_phx_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Phoenix Suns"
            and season.home_away == "Home"
           
                        
        ]
        
    )
@app.route("/SAS_Away")
def query_by_sas_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "San Antonio Spurs"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/SAS_Home")
def query_by_sas_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "San Antonio Spurs"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/OKC_Away")
def query_by_okc_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Oklahoma City Thunder"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/OKC_Home")
def query_by_okc_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Oklahoma City Thunder"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/TOR_Away")
def query_by_tor_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Toronto Raptors"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/TOR_Home")
def query_by_tor_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Toronto Raptors"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/GSW_Away")
def query_by_gsw_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Golden State Warriors"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/GSW_Home")
def query_by_gsw_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Golden State Warriors"
            and season.home_away == "Home"
           
                        
        ]
        
    )
@app.route("/SAC_Away")
def query_by_sac_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Sacramento Kings"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/SAC_Home")
def query_by_sac_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Sacramento Kings"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/CHA_Away")
def query_by_cha_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Charlotte Bobcats"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/CHA_Home")
def query_by_cha_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Charlotte Bobcats"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/UTA_Away")
def query_by_uta_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Utah Jazz"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/UTA_Home")
def query_by_uta_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Utah Jazz"
            and season.home_away == "Home"
           
                        
        ]
        
    )   

@app.route("/CHI_Away")
def query_by_chi_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Chicago Bulls"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/CHI_Home")
def query_by_chi_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Chicago Bulls"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/MIL_Away")
def query_by_mil_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Milwaukee Bucks"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/MIL_Home")
def query_by_mil_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Milwaukee Bucks"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/PHI_Away")
def query_by_phi_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Philadelphia 76ers"
            and season.home_away == "Away"
           
                        
        ]
        
    )

@app.route("/PHI_Home")
def query_by_phi_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "pts": season.pts, 
                "matchup": season.matchup, 
                "reb": season.reb, 
                "ast": season.ast, 
                "stl": season.stl,
                "fg_pct": season.fg_pct,
                "ft_pct": season.ft_pct,
                "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            if season.wl == "W"
            if season.team_name == "Philadelphia 76ers"
            and season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/WL_Opponent")
def query_by_wl_opponent():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                # "pts": season.pts,
                # "is_win": season.is_win, 
                # "is_loss": season.is_loss,  
                # "matchup": season.matchup, 
                # "reb": season.reb, 
                # "ast": season.ast, 
                # "stl": season.stl,
                # "fg_pct": season.fg_pct,
                # "ft_pct": season.ft_pct,
                # "fg3_pct": season.fg3_pct,
                # "home_away": season.home_away,
                "wl": season.wl,
                "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            # if season.wl == "W"
            # if season.team_name == "Philadelphia 76ers"
            # and season.home_away == "Home"
           
                        
        ]
        
    )
@app.route("/WL_Home")
def query_by_wl_home():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                # "pts": season.pts,
                # "is_win": season.is_win, 
                # "is_loss": season.is_loss,  
                # "matchup": season.matchup, 
                # "reb": season.reb, 
                # "ast": season.ast, 
                # "stl": season.stl,
                # "fg_pct": season.fg_pct,
                # "ft_pct": season.ft_pct,
                # "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                # "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            # if season.wl == "W"
            # if season.team_name == "Philadelphia 76ers"
            if season.home_away == "Home"
           
                        
        ]
        
    )


@app.route("/WL_Away")
def query_by_wl_away():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                # "pts": season.pts,
                # "is_win": season.is_win, 
                # "is_loss": season.is_loss,  
                # "matchup": season.matchup, 
                # "reb": season.reb, 
                # "ast": season.ast, 
                # "stl": season.stl,
                # "fg_pct": season.fg_pct,
                # "ft_pct": season.ft_pct,
                # "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                # "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            # if season.wl == "W"
            # if season.team_name == "Philadelphia 76ers"
            if season.home_away == "Away"
           
                        
        ]
        
    )
@app.route("/WL_Overall")
def query_by_wl_overhall():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                # "game_date": season.game_date,
                # "pts": season.pts,
                # "is_win": season.is_win, 
                # "is_loss": season.is_loss,  
                # "matchup": season.matchup, 
                # "reb": season.reb, 
                # "ast": season.ast, 
                # "stl": season.stl,
                # "fg_pct": season.fg_pct,
                # "ft_pct": season.ft_pct,
                # "fg3_pct": season.fg3_pct,
                "home_away": season.home_away,
                "wl": season.wl,
                # "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            # if season.wl == "W"
            # if season.team_name == "Philadelphia 76ers"
            # if season.home_away == "Home"
           
                        
        ]
        
    )

@app.route("/WL_Per_Game")
def query_by_wl_per_game():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "game_date": season.game_date,
                # "pts": season.pts,
                # "is_win": season.is_win, 
                # "is_loss": season.is_loss,  
                "matchup": season.matchup, 
                # "reb": season.reb, 
                # "ast": season.ast, 
                # "stl": season.stl,
                # "fg_pct": season.fg_pct,
                # "ft_pct": season.ft_pct,
                # "fg3_pct": season.fg3_pct,
                # "home_away": season.home_away,
                "wl": season.wl,
                # "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            # if season.wl == "W"
            # if season.team_name == "Philadelphia 76ers"
            # if season.home_away == "Home"
           
                        
        ]
        
    )


@app.route("/Points_Per_Game")
def query_by_points_per_game():
    team_name = request.args.get("team_name")
    q = seasons.query
    
    return jsonify(
        [
            {
                "season_id": season.season_id,
                "team_name": season.team_name,
                "game_date": season.game_date,
                "pts": season.pts,
                # "is_win": season.is_win, 
                # "is_loss": season.is_loss,  
                "matchup": season.matchup, 
                # "reb": season.reb, 
                # "ast": season.ast, 
                # "stl": season.stl,
                # "fg_pct": season.fg_pct,
                # "ft_pct": season.ft_pct,
                # "fg3_pct": season.fg3_pct,
                # "home_away": season.home_away,
                # "wl": season.wl,
                # "opponent": season.opponent
            } 
            
            for season in q
            # if season.season_id == 2009
            # if season.wl == "W"
            # if season.team_name == "Philadelphia 76ers"
            # if season.home_away == "Home"
           
                        
        ]
        
    )

if __name__ == "__main__":
    app.run(debug=True)