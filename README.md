# GeoDev Lab Africa project: health facility access in Ibadan North

Which wards in Ibadan North are furthest from a health facility, and how many people live in them?

Built over twelve months with GeoDev Lab Africa, Cohort One.

This is a demonstration repository used in mentor walkthrough videos. Its data is the GeoDev Lab Africa teaching dataset: the ward names are real, but the shapes, facility locations and population figures were generated for teaching. Do not quote any figure here as a fact about Ibadan.

## Month 1: GIS foundations

- Week 1: Project brief. My question, why it matters and the data I need are in project-brief.md.
- Week 2: Data. Every dataset, its source and its quality are in data-notes.md.
- Week 3: Preparation. Fixed the ward names so the population table joins, set the CRS, counted facilities per ward and exported ibadan_north_wards.csv.
- Week 4: Analysis and map. ibadan_north_wards_map.png shows population and facilities. What I found is in month-1-summary.md.

## Month 2: Python foundations

- Week 5: Terminal and VS Code. Ran my first script, hello.py, from the VS Code terminal.
- Week 6: Environments and uv. Created a uv project and added pandas. use_pandas.py reads my Month 1 ward table.
- Week 7: Python basics. analyse.py reads wards.csv, converts each area to hectares and classifies each ward as large or small.
- Week 8: Files and data. inspect_data.py reads my Month 1 ward table with csv.DictReader and reports the smallest, largest and count of a column, skipping empty cells.
- Week 9: Refactoring. summary.py splits the inspection into read_rows, clean_values and summarise, and summarise_all reports every number column in my ward table.

Proof each script ran is in screenshots/.

## Month 3: Geospatial Python Automation
- Week 10:  GeoPandas. Loaded, checked, joined and mapped my [layer name] in code