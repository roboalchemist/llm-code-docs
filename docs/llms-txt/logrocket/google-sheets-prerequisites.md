# Source: https://docs.logrocket.com/docs/google-sheets-prerequisites.md

# Google Sheets Prerequisites

Configure your Google Sheets destination.

> 🚧 Google Sheets Row Limit
>
> A maximum of 400,000 events can be exported to a Google Sheet. This is a software limitation imposed by Google. In most cases, the output of Streaming Data Export will hit this limit very quickly (sometimes in minutes). For any purpose other than basic testing, it is recommended to use one of the other supported destination types: [https://docs.logrocket.com/docs/data-warehouse-configuration-guides](https://docs.logrocket.com/docs/data-warehouse-configuration-guides)

## Step 1: Create a new Google Sheet

1. Navigate to your Google Drive or Google Sheets homepage and create a new Google Sheet in the folder of your choosing.
2. Visit the [LogRocket Streaming Data Export settings page](https://app.logrocket.com/r/settings/streaming-data-export) to begin the setup. Note: You will need to save the service account provided in this step for later!
3. Return to the Google Sheet you created. In the Google Sheet menu, click **Share** in the top right corner, and enter the Service Account email address generated in the previous step. Grant the Service Account **Editor** permission, and click **Send**.