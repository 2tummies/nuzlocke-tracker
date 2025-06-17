SELECT * FROM pokemon;
SELECT * FROM pokemon WHERE pokemon_name ILIKE '%QUI%';

SELECT * FROM regions;
SELECT * FROM regions WHERE region_name ILIKE '%nov%';

SELECT * FROM versions;

SELECT * FROM versions_regions;

SELECT regions.region_name FROM versions
JOIN versions_regions ON versions.version_id = versions_regions.version_id
JOIN regions ON regions.region_id = versions_regions.region_id
WHERE version_name = '';

SELECT regions.region_name FROM regions
JOIN versions_regions ON regions.region_id = versions_regions.region_id
WHERE version_id = 5;

SELECT DISTINCT locations.location_id, locations.location_name FROM locations
JOIN locations_regions ON locations.location_id = locations_regions.location_id
JOIN regions ON locations_regions.region_id = regions.region_id
JOIN versions_regions ON versions_regions.region_id = versions_regions.region_id
JOIN versions ON versions.version_id = versions_regions.version_id
WHERE versions.version_id = 5 AND regions.region_id = 2
ORDER BY locations.location_id;

SELECT * FROM locations;