CREATE OR REPLACE FUNCTION assign_idnr()
RETURNS TRIGGER AS $$
BEGIN
    NEW.idnr := nextval('location_id_seq');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER assign_idnr_trigger
BEFORE INSERT ON Locations
FOR EACH ROW EXECUTE FUNCTION assign_idnr();