# Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/importing_data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Importing Data

> Import external data into Data Manager from various sources for analysis and integration with existing datasets.

If you already have data collected somewhere else for your form and want to bring everything together in your Curator
table, use the Data Manager Batch Import option.

## Using Batch Import

In the backend, you need an administrator account with Data Manager privileges.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings > Data Manager > Manage Data** section from the left-hand menu.
3. Click on the Batch Import above the overview table.
4. Click on Schedule Import.
5. Select the Data Group for which the data should be imported.
6. Select the CSV file that holds your data.
7. Decide whether or not to trim white-spaces around the string values.
8. Click Import.

If you want to enable your frontend users to upload data:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Settings > Data Manager > Data Groups** section from the left-hand menu.
3. Select the Data Group for which frontend users should be able to import data.
4. Enable **Batch Import** by using the toggle.
5. On the front end, a new section **Batch Import** appears. Click on it to expand the section.
6. Select the CSV file that holds the data.

### Format your CSV

* Add the headers of your table as the first row of your CSV file. Make sure it:
  1. Only has the Data Groups attributes' name in it.
  2. Uses the very same spelling.
  3. Has no spaces around the single attribute names.
* Have one row in the CSV for each row of data. Make sure it:
  1. Has as many attributes as defined in the Data Group.
  2. Has two consecutive commas, if you want to add a blank value.
  3. Do not add any quotes around the values.
