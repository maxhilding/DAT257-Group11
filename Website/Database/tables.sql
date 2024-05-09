
CREATE SEQUENCE location_id_seq START 1;

CREATE TABLE Locations(
    idnr INT NOT NULL DEFAULT nextval('location_id_seq'),
    lon DECIMAL(10,7) NOT NULL, 
    lat DECIMAL(10,7) NOT NULL,
    address TEXT,
    working BOOLEAN DEFAULT 'true',
    
    PRIMARY KEY(idnr), 
    UNIQUE(lon,lat) 
);

