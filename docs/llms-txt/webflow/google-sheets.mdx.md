# Source: https://developers.webflow.com/browser/data-exports/destinations/google-sheets.mdx

***

title: Google Sheets
slug: data-exports/destinations/google-sheets
description: Configure Google Sheets as a destination for Data Exports
----------------------------------------------------------------------

This guide walks you through configuring Google Sheets as a destination for your Webflow Analyze and Optimize data export.

<Warning>
  **Google Sheets destination limitations**

  Due to inherent limitations of Google Sheets, this destination is capped at 400,000 rows or 10 million cells for the entire spreadsheet (across all tabs). Any transfer attempting to write more rows to a given sheet will fail. For such cases, we recommend using a different destination instead.
</Warning>

## Configuration steps

<Steps>
  ### Create a new Google Sheet and share with the Webflow Data Sync service account

  1. Navigate to the your Google Drive or the Google Sheets homepage and create a new Google Sheet in a folder of your choice.
  2. In the Google Sheet menu, click **Share** in the top right corner, and enter the Webflow Data Sync Service Account email: `datasync-webflow@prql-prod.iam.gserviceaccount.com`. Grant the Service Account **Editor** permission, and click **Send**.

  ### Add your destination

  Test your connection and save the destination to complete the connection. During the initial sync, data tables will be loaded as individual tabs, and refreshed at the designated frequency.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49269483498643)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271476563091)
</Steps>

## FAQ

<Accordion title="How is the Google Sheets connection secured?">
  The integration uses a dedicated service account identity to access your spreadsheet. You grant access by sharing the specific Google Sheet (or a restricted folder) with the Webflow Data Sync service account email. Access is controlled by Google Drive sharing permissions (no personal user credentials are required) and can be revoked at any time by removing the service account from the Share menu.
</Accordion>
