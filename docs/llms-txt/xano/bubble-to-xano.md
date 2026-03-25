# Source: https://docs.xano.com/the-database/migrating-your-data/bubble-to-xano.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bubble to Xano

# Overview

This guide explains how to export data from **Bubble** and import it into **Xano**, so you can take advantage of Xano’s scalable backend and API-first architecture.\
By the end, your Xano database will contain the same records that powered your Bubble app.

***

## CSV Import

## 1. Prepare Your Bubble Data

### 1.1 Identify Data Types

In your Bubble editor:

1. Navigate to **Data** → **Data Types**.
2. List each type (e.g., `Users`, `Orders`, `Products`) you plan to migrate.

### 1.2 Export as CSV

For each data type:

1. Go to **Data** → **App Data**.
2. Select the relevant data type from the dropdown.
3. Click **Export** (CSV).
4. Save the `.csv` file to your computer.

<Callout type="info">
  If you have privacy rules restricting access, ensure you have the proper
  permissions to export all records.
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

# Bubble Data API


Built with [Mintlify](https://mintlify.com).