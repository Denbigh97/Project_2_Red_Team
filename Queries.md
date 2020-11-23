-- Sum of Win for each season

SELECT season_id, sum(is_win) as num_win_by_season
FROM season_atl
GROUP BY season_id
ORDER BY num_win_by_season DESC;

-- Sum of Loss for each season

SELECT season_id, sum(is_loss) as num_loss_by_season
FROM season_atl
GROUP BY season_id
ORDER BY num_loss_by_season DESC;

-- Sum of win home_away

SELECT home_away, sum(is_win) as num_win
FROM season_bkn
GROUP BY home_away
ORDER BY num_win DESC;

--Sum of win grouped by season_id and home_away

SELECT season_id, home_away, sum(is_win) as win_quantities
FROM season_bkn
GROUP BY season_id, home_away, is_win
ORDER BY win_quantities DESC; 

--Sum of win grouped by season_id and opponent

SELECT season_id, opponent, sum(is_win) as win_quantities
FROM season_bkn
GROUP BY season_id, opponent, is_win
ORDER BY win_quantities DESC; 

Sum of points per each game

SELECT season_id, team_abbreviation, team_name, opponent, wl, home_away, game_date, sum(pts) as total_points
FROM season_bkn
GROUP BY season_id, team_abbreviation, team_name, opponent, wl, home_away, game_date

ORDER BY total_points DESC; 

SELECT opponent, home_away, season_id, sum(is_loss) as total_games_loss 
FROM season_bkn
WHERE season_id IN ('22018')
GROUP BY season_id, home_away, opponent
ORDER BY total_games_loss DESC;


 -- Average points in each season


Count oof Win and Loss for each season
Score with each oponent for each season

- DROP TABLE public."Cleaned_data11.21";

CREATE TABLE public."Cleaned_data11.21"
(
    "SEASON_ID" bigint,
    "TEAM_ID" bigint,
    "TEAM_ABBREVIATION" text COLLATE pg_catalog."default",
    "TEAM_NAME" text COLLATE pg_catalog."default",
    "GAME_ID" bigint,
    "GAME_DATE" text COLLATE pg_catalog."default",
    "MATCHUP" text COLLATE pg_catalog."default",
    "WL" text COLLATE pg_catalog."default",
    "MIN" bigint,
    "PTS" bigint,
    "FGM" bigint,
    "FGA" bigint,
    "FG_PCT" double precision,
    "FG3M" bigint,
    "FG3A" bigint,
    "FG3_PCT" double precision,
    "FTM" bigint,
    "FTA" bigint,
    "FT_PCT" double precision,
    "OREB" bigint,
    "DREB" bigint,
    "REB" bigint,
    "AST" bigint,
    "STL" bigint,
    "BLK" bigint,
    "TOV" bigint,
    "PF" bigint,
    "PLUS_MINUS" double precision,
    "Is_Win" bigint,
    "Is_Loss" bigint,
    "Home_Away" text COLLATE pg_catalog."default",
    "Opponent" text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public."Cleaned_data11.21"
    OWNER to postgres;