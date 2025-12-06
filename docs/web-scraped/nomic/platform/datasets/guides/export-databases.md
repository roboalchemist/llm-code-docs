# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/guides/export-databases

Atlas is useful for analyzing database exports, as it helps teams discover patterns and relationships across large volumes of structured data. By visualizing database records in Atlas's interactive maps, teams can uncover hidden clusters, outliers, and trends that may not be apparent through traditional SQL queries or table views. This semantic analysis of database content can surface insights about user behavior, system performance, or business metrics that inform data-driven decisions.

## SQL Databases​

- PostgreSQL
```
psql -d database_name -c "COPY (SELECT * FROM table_name) TO STDOUT WITH CSV HEADER" > output.csv
```

- MySQL
```
mysql -u username -p database_name -e "SELECT * FROM table_name" > output.csv
```

## MongoDB​

The mongoexport tool exports data from a MongoDB database into JSON or CSV format. This command-line utility is part of the MongoDB Database Tools package.

```
mongoexport
```

Basic JSON export with one document per line:

```
mongoexport --db=database_name --collection=collection_name --out=output.json
```

CSV export (you must specify the fields to include):

```
mongoexport --db=database_name --collection=collection_name --type=csv --fields=name,age,email --out=output.csv
```

Mongoexport usage documentation

## Snowflake​

Snowflake uses a concept called "unloading" to export data, which differs from traditional databases. Data must first be unloaded to a stage (internal or external) before being downloaded. Snowflake supports multiple file formats including:

- Structured: CSV, TSV, and other delimited formats
- Semi-structured: JSON (NDJSON format), Parquet
Basic CSV Export:

```
CREATE OR REPLACE FILE FORMAT my_csv_format    TYPE = 'CSV'    FIELD_DELIMITER = ','    NULL_IF = ('NULL', 'null')    EMPTY_FIELD_AS_NULL = TRUE;CREATE OR REPLACE STAGE my_export_stage;COPY INTO @my_export_stage/export.csvFROM (SELECT * FROM table_name)FILE_FORMAT = my_csv_format;GET @my_export_stage/export.csv file:///path/to/local/export.csv;DROP STAGE my_export_stage;
```

JSON Export:

```
CREATE OR REPLACE FILE FORMAT my_json_format    TYPE = 'JSON';COPY INTO @my_export_stage/export.jsonFROM (SELECT * FROM table_name)FILE_FORMAT = my_json_format;GET @my_export_stage/export.json file:///path/to/local/export.json;
```

Snowflake export documentation

- SQL Databases
- MongoDB
- Snowflake
