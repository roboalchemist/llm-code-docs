# Source: https://docs.apify.com/platform/integrations/drive.md

# Google Drive integration

**Learn how to integrate your Apify Actors with Google Drive. This article shows you how to automatically save results to your drive when an Actor run succeeds.**

***

## Get started

To use the Apify integration for Google Drive, you will need:

* An [Apify account](https://console.apify.com/).
* A Google account
* A saved Actor Task

## Set up Google Drive integration

1. Head over to **Integrations** tab in your saved task and click on the **Upload file** integration.

   ![Google Drive integration](/assets/images/google-integrations-add-7548d11ef631c30f63f9f06733f5c34e.png)

2. Click on **Connect with Google** button and select the account with which you want to use the integration.

   ![Google Drive integration](/assets/images/google-integrations-connect-drive-836e2e2e4618baefb146659112e6bb4a.png)

3. Set up the integration details. You can choose the **Filename** and **Format** , which can make use of available variables. The file will be uploaded to your Google Drive account to `Apify Uploads` folder. By default, the integration is triggered by successful runs only.

   ![Google Drive integration](/assets/images/google-integrations-details-drive-a5ac7880e4d742e2cefe11efaa3e247f.png)

4. Click on **Save** & enable the integration.

Once this is done, run your Actor to test whether the integration is working.

You can manage your connected accounts at **[Settings > API & Integrations](https://console.apify.com/settings/integrations)**.

![Google Drive integration](/assets/images/google-integrations-accounts-95c33e6e7c658a29a5b87f4a4c65a653.png)
