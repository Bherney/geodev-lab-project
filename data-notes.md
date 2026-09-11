# Data notes

Note: this demonstration project uses the GeoDev Lab Africa teaching dataset. The ward names are real Ibadan North ward names. The shapes, facility locations and population figures were generated for teaching. Do not quote any figure here as a fact about Ibadan.

## Ward boundaries
Source: GeoDev Lab Africa teaching dataset. 12 wards of Ibadan North LGA, drawn as equal squares.
Format: polygon layer, WGS 84 (EPSG:4326).
Quality: the shapes are simplified, so every ward has the same area. Fine for learning, not for planning.

## Population
Source: teaching dataset, ward population table (2024 estimate).
Quality: ward names do not match the boundary layer exactly (AGODI in capitals, Oke Aremo without a hyphen, Sabo with a trailing space). I fixed the names before joining. Inalende has no population figure, so I left it empty rather than putting zero.

## Health facilities
Source: teaching dataset, 41 facilities with latitude and longitude.
Quality: the type column is inconsistent (Primary Health Centre and PHC mean the same thing).

## Coordinate reference system
Everything is in WGS 84. For areas and distances I use WGS 84 / UTM zone 31N (EPSG:32631), the UTM zone that covers Ibadan.
