
CREATE SEQUENCE location_id_seq START 1;

CREATE TABLE Locations(
    idnr INT NOT NULL DEFAULT nextval('location_id_seq'),
    lon DECIMAL(10,7) NOT NULL, 
    lat DECIMAL(10,7) NOT NULL, 
    PRIMARY KEY(idnr), 
    UNIQUE(lon,lat) 
);



-- CREATE TABLE Fountains(
--     idnr INT PRIMARY KEY REFERENCES Locations(idnr),
--     name TEXT, 
--     lon DECIMAL(10,7) NOT NULL,
--     lat DECIMAL(10,7) NOT NULL,  
--     FOREIGN KEY (lon, lat) REFERENCES Locations(lon, lat)
-- );