# Source: https://docs.xano.com/the-database/migrating-your-data/google-sheets-to-xano.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Sheets to Xano

# Overview

This guide walks you through exporting data from **Google Sheets** and importing it into **Xano**, where you can manage your data as structured database tables and expose it through APIs.

***

## 1. Prepare Your Google Sheets Data

### 1.1 Clean & Organize

Before exporting:

* Ensure each sheet represents a single logical dataset (e.g., `Users`, `Orders`, `Products`).
* Confirm that the **first row contains column headers**.
* Remove blank rows, merged cells, or formulas that may cause import issues.

<Callout type="tip">
  Xano supports CSV files. If you have multiple sheets, export each one
  individually or as separate CSVs.
</Callout>

### 1.2 Export as CSV

For each sheet:

1. Open your Google Sheet.
2. Go to **File → Download → Comma-separated values (.csv)**.
3. Save each sheet as a separate `.csv` file.

***

## 2. Import CSV Files into Xano

For each collection:

1. Open the database in Xano.
2. Click **Add Table** → **Import Data** → **CSV Import**.
3. Upload the matching CSV file.
4. Click **Import** and wait for the confirmation message.

***

## 3. Validate Your Data

After importing:

* Open each Xano table and check that record counts match the rows in your Google Sheet.
* Spot-check a few records for accuracy and formatting.


Built with [Mintlify](https://mintlify.com).