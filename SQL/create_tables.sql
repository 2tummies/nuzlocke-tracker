DROP TABLE IF EXISTS pokemon_encounters;
DROP TABLE IF EXISTS versions_regions;
DROP TABLE IF EXISTS versions;
DROP TABLE IF EXISTS time_of_day;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS encounter_methods;
DROP TABLE IF EXISTS pokemon;
DROP TABLE IF EXISTS regions;

CREATE TABLE regions (
        region_id SMALLINT PRIMARY KEY,
        region_name TEXT UNIQUE NOT NULL
);

CREATE TABLE versions (
        version_id SMALLINT PRIMARY KEY,
        version_name TEXT UNIQUE NOT NULL
);

CREATE TABLE versions_regions (
        version_id SMALLINT REFERENCES versions,
        region_id SMALLINT REFERENCES regions,
        
        PRIMARY KEY (version_id, region_id)
);

CREATE TABLE locations (
        location_id SMALLINT PRIMARY KEY,
        location_name TEXT NOT NULL,
        region_id SMALLINT REFERENCES regions
);

CREATE TABLE encounter_methods (
        method_id SMALLINT PRIMARY KEY,
        method_name TEXT UNIQUE NOT NULL,
        nat_dex BOOLEAN
);

CREATE TABLE pokemon (
        dex_number SMALLINT PRIMARY KEY,
        pokemon_name TEXT UNIQUE NOT NULL
);

CREATE TABLE time_of_day (
        time_of_day_id SMALLINT PRIMARY KEY,
        time_of_day_name TEXT UNIQUE NOT NULL
);

CREATE TABLE pokemon_encounters (
        location_id SMALLINT REFERENCES locations,
        pokemon_id SMALLINT REFERENCES pokemon,
        method_id SMALLINT REFERENCES encounter_methods,
        nat_dex BOOLEAN,
        version_exclusive_id SMALLINT REFERENCES versions,
        time_of_day_id SMALLINT REFERENCES time_of_day,
        
        PRIMARY KEY(location_id, pokemon_id, method_id)
);
