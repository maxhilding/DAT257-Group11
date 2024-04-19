CREATE OR REPLACE FUNCTION assign_idnr()
RETURNS TRIGGER AS $$
DECLARE cnt INT;
BEGIN
    SELECT COUNT(*) INTO cnt FROM Locations;
    NEW.idnr = cnt + 1;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER assign_idnr_trigger
BEFORE INSERT ON Locations
FOR EACH ROW EXECUTE FUNCTION assign_idnr();