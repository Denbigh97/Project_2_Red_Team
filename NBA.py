from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import Session

Base = declarative_base()

class NBA(Base):
    __tablename__ = "seasson"
    
    SEASON_ID = Column(Integer, primary_key=True)
    TEAM_ID = Column(Integer, primary_key=True)
    TEAM_ABBREVIATION = Column(String(10)) 
    TEAM_NAME = Column(String(30)) 
    GAME_ID = Column(Float) 
    GAME_DATE = Column(Date) 
    MATCHUP = Column(String(30)) 
    WL = Column(String(10)) 
    MIN = Column(Float) 
    PTS = Column(Float) 
    FGM = Column(Float) 
    FGA = Column(Float)
    FG_PCT = Column(Float) 
    FG3M = Column(Float) 
    FG3A = Column(Float)
    FG3_PCT = Column(Float)
    FTM = Column(Float)
    FTA = Column(Float) 
    FT_PCT = Column(Float) 
    OREB = Column(Float)
    DREB = Column(Float) 
    REB = Column(Float) 
    AST = Column(Float) 
    STL = Column(Float) 
    BLK = Column(Float)
    TOV = Column(Float)
    PF = Column(Float)
    PLUS_MINUS = Column(Float)
    
engine = create_engine("postgres://postgres:Carlos@0000@35.192.83.205:5432/NBA_db")

Base.metadata.create_all(engine)

session = Session(bin=engine)

# def create_NBA(SEASON_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, GAME_ID, GAME_DATE, MATCHUP, WL, MIN, PTS, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PLUS_MINUS, ):
#     new_NBA = NBA(url TBD)

# session.add(NBA)
# session.commit()

#create_NBA(url TBD)