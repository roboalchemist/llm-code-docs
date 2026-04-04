# Source: https://docs.xano.com/the-database/migrating-your-data/connect-to-an-external-database.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to an External Database

> Learn how to connect to and migrate your data from an external database to Xano

Xano lets you securely connect to external databases, run SQL queries, and migrate data into your own Xano database using bulk operations.\
This page provides a **basic overview** of the process and links to the full documentation for each step.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/X5xVK0Xhc4s?si=jwn_pcZfrpa9_S3j" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

***

## 1. Connect to Your External Database

Use the **External Database Query** function to create a connection to your external database.\
Xano supports **PostgreSQL**, **MS SQL**, **Oracle**, **MySQL**, and **Snowflake**.

* Add a new function in your Function Stack → **Database Operations → External Database Query**.
* Enter a **connection string** with your database details (host, port, username, password).
* Save to test and establish the connection.

***

## 2. Build and Run SQL Queries

Once connected, use the **Direct Database Query** function to run SQL statements against your external database.

* Add a new function → **Database Operations → Direct Database Query**.
* Write SQL in the **Code** field or use the SQL Query Wizard.
* Use **Statement Args** (`?`) to safely insert dynamic variables.
* Return either a single record or a list of records.

***

## 3. Migrate Data into Xano

After retrieving data, use **Bulk Operations** to insert or update records inside your Xano database.

* Add a **Bulk Operations** function to your Function Stack.
* Map the retrieved data from your query to the fields in your Xano table.
* Run the function to perform a fast, large-scale migration.

***

## Quick Links

Use the cards below to dive into the full documentation for each feature:

<Card title="External Database Query" href="/the-function-stack/functions/database-requests/external-database-query">
  Learn how to connect to PostgreSQL, MS SQL, Oracle, MySQL, or Snowflake and generate a
  connection string.
</Card>

<Card title="Direct Database Query" href="/the-function-stack/functions/database-requests/direct-database-query">
  Write and run SQL queries, use statement arguments, and leverage the SQL Query
  Wizard.
</Card>

{" "}

<Card title="Bulk Operations" href="/the-function-stack/functions/database-requests/bulk-operations">
  Insert, update, or upsert large amounts of data efficiently inside Xano.
</Card>


Built with [Mintlify](https://mintlify.com).