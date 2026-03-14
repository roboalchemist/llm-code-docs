# Source: https://docs.acceldata.io/documentation/postgresql.md

# PostgreSQL

PostgreSQL is an open-source relational database that stores data in tables (rows and columns) and you use SQL (Structured Query Language) to read and write data.

## Prerequisite

Ensure the following requirements are met before you connect PostGreSQL as a data sourcee:

- A PostgreSQL instance you can connect to (host, port, credentials).
- The name(s) of the schema(s) you want to monitor. A _schema_ in PostgreSQL is like a namespace to group tables.
- Access rights: the username/password used should have reading privileges on those schemas.
- If you want query-analysis, ensure the PostgreSQL environment captures query logs or has necessary permissions.
- For integration with ADOC, a Data Plane ready (either preexisting or newly created).

## Add PostGreSQL as a Data Source

### Step 1: Start Setup

1. Click **Register** from the left main menu.
2. Select **Add Data Source** -&gt; **Azure Data Lake** from the list of data sources.
3. On the **Data Source Details** page:
    1. Name the data source.
    2. Add a short description (optional).
    3. Ensure the **Data Reliability** toggle is enabled and select your **data plane** from the dropdown.

4. Select **Next**.

### Step 2: Add Connection Details

1. Enter PostgreSQL connection details:
    1. **PostGreSQL URL** (host, port, database)
    2. **Username**
    3. **Password**

2. Click **Test Connection** to validate access. If your credentials are valid, you receive a **Connected** message. If you get an error message, validate the PostgreSQL credentials you entered.
3. Click **Next**.

### Step 3: Set Up Observability

In the Observability Set Up page, perform the following:

1. Turn on **Query Analysis Service** (named “Torch Query Analysis Service” in UI) if you want insight into query performance.
2. Specify which **schema(s)** to monitor. You can add more than one schema.
3. Select the **PostgreSQL Environment** — e.g. dev, staging, production.
4. Optionally enable **Crawler Execution Schedule**: set up when (time, time zone) the crawler should run automatically.
5. Click **Submit**.

After this, PostgreSQL is added as a data source. You can choose to run the crawler right away or run on schedule.

## After Setup

Once PostgreSQL is connected and crawling is complete:

- A card for this PostgreSQL source will appear on the Register page. This card shows basics like: 
    - The monthly cost incurred so far (if applicable) 
    - Status of the crawler (running / scheduled / error) 
    - Other metadata (e.g. when it was last crawled)

- In **Data Reliability &gt; Discover Assets**, you can see assets (schemas, tables) from your monitored schemas.
- Query performance metrics, if query analysis is enabled — e.g. which queries are expensive or which tables are accessed most.

## What’s Next

- Once basic monitoring is working, explore setting up **alerts** in ADOC — so you get notified if data quality drops or queries misbehave.
- Use the lineage or data flow capabilities (if available) to see how tables/tables are related or how data moves among tables.
- Periodically review schemas included and remove ones no longer needed.
- Use the insights from query analysis & schemata changes to tune database performance: e.g. add indexes, rewrite queries, or archive old data.