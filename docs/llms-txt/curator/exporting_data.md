# Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/exporting_data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting Data

> Export data collected by Data Manager using various export options including CSV downloads for backend users.

You can export the data collected by the Data Manager by using the Data Manager Export options.

## Download as CSV - Backend Users Only

In the backend, you need an administrator account with Data Manager privileges.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Data Manager > Data Groups** section from the left-hand menu.
3. Click on the Data Group you want to export the data from.
4. Click **Download as CSV** to trigger the manual export.

## Download as CSV - Frontend Users

In the backend, you need an administrator account with Data Manager privileges.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to **Data Manager > Data Groups** section from the left-hand menu.
3. Click on the Data Group you want to export the data from.
4. Toggle on **Allow CSV Export on frontend** to enable the export feature on the front end.
5. Make sure the toggle **Hide List** is off.
6. Save.

Once the feature is enabled, as a frontend user:

1. Login to the front end (e.g. `http://curatorexample.com/`).
2. Navigate to the Data Group (aka form) that you want to export the data from
   (e.g. `https://www.curatorexample.com/data/your-data-group`).
3. Open the section Your Data Group List.
4. Click the **CSV** button to trigger the manual export.
