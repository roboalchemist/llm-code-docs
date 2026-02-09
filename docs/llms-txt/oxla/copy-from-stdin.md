# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-from/copy-from-stdin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# COPY FROM STDIN

## Overview

The `COPY FROM STDIN` command imports data directly from the client into a table. It simplifies the copy process by eliminating the need to transfer files to the server.

## Syntax

The syntax for this function is as follows:

```sql  theme={null}
COPY table_name FROM STDIN;
```

## Parameters

* `table_name`: table where the data will be imported
* `stdin`: data coming from the standard input (client application)

When it comes to file format, only CSV files are supported and the default delimiter for this format is a comma `,`.

### Additional Options

**1. Listing Column Names**

You can specify the columns into which the data should be imported.

```sql  theme={null}
COPY table_name (column1, column2) FROM stdin;
```

**2. Options**

You can include additional options following `FROM stdin` to customize the import process.

```sql  theme={null}
COPY table_name FROM STDIN WITH (FORMAT csv, DELIMITER ',');
```

## Examples

### Importing Data Manually

1. Ensure the table exists in your database. If it doesn’t, create one using the following command:

```sql  theme={null}
CREATE TABLE film (
    title text NOT NULL,
    length int,
    rating text
    );
```

You should see the output indicating that the table has been created.

2. Initiate the import operation by running the following command:

```sql  theme={null}
COPY film FROM stdin;
```

3. You will be prompted to enter your data. There will be a message as shown below:

```sql  theme={null}
Enter data to be copied followed by a newline.
End with a backslash and a period on a line by itself, or an EOF signal.
>> 
```

4. Paste the data directly from your CSV file into the prompt:

   ```sql  theme={null}
   ATTRACTION NEWTON,83,PG-13
   CHRISTMAS MOONSHINE,150,NC-17
   DANGEROUS UPTOWN,121,PG
   KILL BROTHERHOOD,54,G
   HALLOWEEN NUTS,47,PG-13
   HOURS RAGE,122,NC-17
   PIANIST OUTFIELD,136,NC-17
   PICKUP DRIVING,77,G
   INDEPENDENCE HOTEL,157,NC-17
   PRIVATE DROP,106,PG
   SAINTS BRIDE,125,G
   FOREVER CANDIDATE,131,NC-17
   MILLION ACE,142,PG-13
   SLEEPY JAPANESE,137,PG
   WRATH MILE,176,NC-17
   YOUTH KICK,179,NC-17
   CLOCKWORK PARADISE,143,PG-13
   ```

If the import is successful, you will see `IMPORT 0` at the end of the line.

<Tip>To end the import process, for Unix-like systems press Ctrl + D.</Tip>

5. Verify the imported data by querying the table in a following way:

```sql  theme={null}
SELECT * FROM film;
```

The output from that query should be as follows:

```sql  theme={null}
    title          | length | rating 
--------------------+--------+--------
ATTRACTION NEWTON   |     83 | PG-13
CHRISTMAS MOONSHINE |    150 | NC-17
DANGEROUS UPTOWN    |    121 | PG
KILL BROTHERHOOD    |     54 | G
HALLOWEEN NUTS      |     47 | PG-13
HOURS RAGE          |    122 | NC-17
PIANIST OUTFIELD    |    136 | NC-17
PICKUP DRIVING      |     77 | G
INDEPENDENCE HOTEL  |    157 | NC-17
PRIVATE DROP        |    106 | PG
SAINTS BRIDE        |    125 | G
FOREVER CANDIDATE   |    131 | NC-17
MILLION ACE         |    142 | PG-13
SLEEPY JAPANESE     |    137 | PG
WRATH MILE          |    176 | NC-17
YOUTH KICK          |    179 | NC-17
CLOCKWORK PARADISE  |    143 | PG-13
(17 rows)
```

### Direct CSV File Import

Use the following steps to import a CSV file directly into your Oxla instance. This method bypasses the need to manually enter data by reading the file and importing it directly into Oxla. After launching the `psql` client application and creating the `film` table, download the <a href="/assets/film-dataset.csv" download="film-dataset.csv"> film-dataset.csv </a> file and execute the following query:

```sql  theme={null}
COPY table_name FROM '/local/path/to/file' WITH (FORMAT CSV, HEADER);
```

* Replace `table_name` with your target table name
* Replace `/path/to/file` with the full path to your CSV file
* Use `HEADER` if your CSV file includes column headers

### Importing Data Using `cat` Method

Ensure your dataset is in a valid CSV format. After creating a table using `psql`, please follow the following steps:

1. Type `\q` followed by `Enter` to exit `psql`
2. Import the CSV File:

```bash  theme={null}
cat /local/path/to/file | psql -h localhost -U oxla oxla -c "COPY film FROM STDIN WITH (FORMAT csv, HEADER ',');"
```

This command reads the contents of <a href="/assets/film-dataset.csv" download="film-dataset.csv"> film-dataset.csv </a> file and passes it directly to the `COPY` command.
