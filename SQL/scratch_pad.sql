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