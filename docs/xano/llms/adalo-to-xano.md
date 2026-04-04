# Source: https://docs.xano.com/the-database/migrating-your-data/adalo-to-xano.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adalo to Xano

> A step-by-step guide to move your collections, records, and relationships from an Adalo app into a Xano backend.

# Overview

This guide shows how to export your data from **Adalo** and import it into **Xano**, preserving collections, fields, and relationships.\
By the end, your Xano database will contain the same records that powered your Adalo app, ready for scalable APIs.

***

## 1. Prepare Your Adalo Data

### 1.1 Identify Collections

In the Adalo builder:

1. Go to **Database** → **Collections**.
2. List every collection you want to migrate (e.g., `Users`, `Orders`, `Products`).

### 1.2 Export as CSV

For each collection:

* Click **⋮** next to the collection name.
* Select **Export CSV**.
* Save the `.csv` file to a folder on your computer.

<Callout type="info">
  Keep each file name clear (e.g., `users.csv`) to make mapping easier later.
</Callout>

***

## 2. Import CSV Files into Xano

For each collection:

1. Open the database in Xano.
2. Click **Add Table** → **Import Data** → **CSV Import**.
3. Upload the matching CSV file.
4. Click **Import** and wait for the confirmation message.

<Callout type="warning">
  If you have foreign key relationships (e.g., `Orders` → `Users`), these will
  need to be resolved either manually or with a workflow.
</Callout>

***

## 3. Validate Your Data

After all imports:

1. Browse each Xano table and confirm record counts match your Adalo CSVs.
2. Spot-check a few records to verify data and data types, especially long text fields or special characters.


Built with [Mintlify](https://mintlify.com).