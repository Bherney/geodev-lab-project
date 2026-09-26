# Month 1 summary

## My question
Which wards in Ibadan North are furthest from a health facility, and how many people live in them?

## What I did
I loaded the ward boundaries, the population table and the facility points into QGIS. I fixed the ward names so the population table would join, joined it to the wards, counted facilities in each ward with Count Points in Polygon, and exported the attribute table as ibadan_north_wards.csv. Then I made the map ibadan_north_wards_map.png.

## What I found
Five wards have no facility inside them at all: Oke-Are, Basorun, Ashi, Samonda and Agbowo. Agbowo has the largest population of all twelve wards. Sabo has the most facilities, nine.

## What surprised me
The join failed the first time. Three ward names were written differently in the population table, and QGIS did not warn me. It just left those wards empty.

## What I still need
Counting points inside a ward is not the same as distance. A ward with no facility inside it might still have one just across the boundary. I need to measure the distance from each ward to its nearest facility.
