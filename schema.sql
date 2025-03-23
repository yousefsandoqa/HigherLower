DROP TABLE IF EXISTS Team CASCADE;
CREATE TABLE Team (
    t_index INT NOT NULL,
    abr VARCHAR(8) NOT NULL UNIQUE,
    name VARCHAR(64),
    city VARCHAR(64),
    champs INT,
    PRIMARY KEY (t_index)
);

DROP TABLE IF EXISTS Player CASCADE;
CREATE TABLE Player (
    p_index INT NOT NULL,
    name VARCHAR(32),
    college VARCHAR(64),
    country VARCHAR(32),
    draft_year VARCHAR(9),
    PRIMARY KEY (p_index)
);

DROP TABLE IF EXISTS Player_Season CASCADE;
CREATE TABLE Player_Season (
    p_index INT NOT NULL,
    t_index INT NOT NULL,
    year VARCHAR(9) NOT NULL,
    team_abr VARCHAR(8) NOT NULL,
    name VARCHAR(32),
    age INT,
    usg_pct FLOAT,
    ts_pct FLOAT,
    ppg FLOAT,
    rpg FLOAT,
    apg FLOAT,
    bpg FLOAT,
    spg FLOAT,
    games_played INT,
    PRIMARY KEY (p_index, year),
    FOREIGN KEY (p_index) REFERENCES Player(p_index) ON DELETE CASCADE,
    FOREIGN KEY (t_index) REFERENCES Team(t_index) ON DELETE CASCADE,
    FOREIGN KEY (team_abr) REFERENCES Team(abr) ON DELETE CASCADE
);

DROP TABLE IF EXISTS Career_Stats CASCADE;
CREATE TABLE Career_Stats (
    p_index INT NOT NULL,
    years_played INT,
    ppg FLOAT,
    rpg FLOAT,
    apg FLOAT,
    bpg FLOAT,
    spg FLOAT,
    PRIMARY KEY (p_index),
    FOREIGN KEY (p_index) REFERENCES Player(p_index) ON DELETE CASCADE
);

DROP TABLE IF EXISTS Accolades CASCADE;
CREATE TABLE Accolades (
    p_index INT NOT NULL,
    year VARCHAR(16) NOT NULL,
    award VARCHAR(32) NOT NULL,
    PRIMARY KEY (award, year),
    FOREIGN KEY (p_index) REFERENCES Player(p_index) ON DELETE CASCADE
);

DROP TABLE IF EXISTS User_Data CASCADE;
CREATE TABLE User_Data (
    index INT NOT NULL,
    name VARCHAR(32),
    score INT,
    PRIMARY KEY (index)
);