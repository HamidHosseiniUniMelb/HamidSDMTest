import duckdb

# Create/connect to a DuckDB database
con = duckdb.connect(r"D:\temp\my_spatial_db.duckdb")

# spatial=============================================================
# Install and load the spatial extension (only need to INSTALL once)
con.execute("INSTALL spatial;")
con.execute("LOAD spatial;")

# Select all rows
rows = con.execute("SELECT id, city, ST_AsText(ST_GeomFromWKB(location)) FROM us_cities").fetchall()
print(rows)

# Check column info for a table
result = con.execute("PRAGMA table_info('us_cities')").fetchall()
print(result)





