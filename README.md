# Hw9 API Creation with Flask and SQL Alchemy
In this project, the goal is to explore precipitation and temperature data from Honolulu, Hawaii and perform some data analysis and visualization.

The technology used include: Python, Flask, Pandas, Matplotlib, and  SQL Alchemy.

Step 1 - Data Engineering The climate data for Hawaii is provided through two CSV files. The data was inspected and cleaned using Python. Data_engineering.ipynb contains the completed code. The cleaned csv files were saved with a "clean_" prefix.

Step 2 - Database Engineering With the cleaned data in the clean_ .csv files, using SQLAlchemy and it's declarative_base function, the table schemas were created ( ORM classes were created for Measurements and for stations) and the tables were stored in a sqlite database (hawaii.sqlite). Database_engineering.ipynb contains the completed code.

Step 3 - Climate Analysis and Visualization Creation. All of the following analysis was completed using SQLAlchemy ORM queries (create_engine, automap_base), Pandas, and Matplotlib using a two week vacation period with arbitrary start dates.

Step 4 - Created a simple app API (app.py) with Flask, which contains some information regarding the climate analysis.
