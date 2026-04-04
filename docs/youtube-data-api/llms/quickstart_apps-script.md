# Source: https://developers.google.com/youtube/v3/quickstart/apps-script.md.txt

# Google Apps Script Quickstart

Complete the steps described in the rest of this page, and in just a few
minutes you'll have a simple [Google Apps Script](https://developers.google.com/apps-script/overview)
that makes requests to the YouTube Data API.

The sample application demonstrates how to add YouTube channel data to a
spreadsheet.

## Prerequisites

To run this quickstart, you'll need:

- Access to the internet and a web browser.
- A Google account.
- Access to Google Drive.

## Step 1: Create the script

1. Open [Google Drive](https://drive.google.com) in your web browser.
2. Click **New** \> **Google Sheets**.
3. In the new spreadsheet, click **Extensions** \> **Apps Script**.
4. Replace the contents of the script editor with the following code:  

   ```gdscript
   // Note: Apps Script automatically requests authorization
   // based on the API's used in the code.

   function channelsListByUsername(part, params) {
     var response = YouTube.Channels.list(part,
                                          params);
     var channel = response.items[0];
     var dataRow = [channel.id, channel.snippet.title, channel.statistics.viewCount];
     SpreadsheetApp.getActiveSpreadsheet().appendRow(dataRow);
   }

   function getChannel() {
     var ui = SpreadsheetApp.getUi();
     var channelName = ui.prompt("Enter the channel name: ").getResponseText();
     channelsListByUsername('snippet,contentDetails,statistics',
                            {'forUsername': channelName});
   }

   function getGoogleDevelopersChannel() {
     channelsListByUsername('snippet,contentDetails,statistics',
                            {'forUsername': 'GoogleDevelopers'});
   }

   function onOpen() {
     var firstCell = SpreadsheetApp.getActiveSheet().getRange(1, 1).getValue();
     if (firstCell != 'ID') {
       var headerRow = ["ID", "Title", "View count"];
       SpreadsheetApp.getActiveSpreadsheet().appendRow(headerRow);
     }
     var ui = SpreadsheetApp.getUi();
     ui.createMenu('YouTube Data')
     .addItem('Add channel data', 'getChannel')
     .addSeparator()
     .addItem('Add GoogleDevelopers data', 'getGoogleDevelopersChannel')
     .addToUi();
   }
   https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/apps-script/quickstart.gs
   ```
5. Click Save ![](https://fonts.gstatic.com/s/i/googlematerialicons/save/v6/24px.svg).
6. Click **Untitled project** at the top left, type **Quickstart** , and click **Rename**.

## Step 2: Turn on the YouTube Data API

1. At the left, click **Editor** code.
2. At the left, next to "Services," click Add a service add.
3. Click **YouTube Data API** , then click **Add**.

## Step 3: Run the sample

1. Reload your spreadsheet. If it is the first time you are loading the spreadsheet after adding the code, the first row should populate with **ID** , **Title** , and **View count** headers.
2. In the menu bar, click **YouTube Data** \> **Add GoogleDevelopers data**
   to add information about the GoogleDevelopers channel to your spreadsheet.
   (The YouTube Data menu should appear next to the standard menus --
   File, Edit, View, etc.)

   <br />


   The first time you run the sample, it will prompt you to authorize access:

   1. Click **Review permissions**.
   2. Choose an account.
   3. Click **Allow**.
3. In the menu bar, click **YouTube Data** \> **Add channel data** to add data
   for a channel of your choice. When prompted, enter the channel name
   (e.g. "GoogleDevelopers" or "SaturdayNightLive") and click **OK**. The
   script retrieves data for that channel and adds it to the spreadsheet.

It worked! **Great!** Check out the further reading section below to learn more.
I got an error **Bummer.** Check out our [troubleshooting](https://developers.google.com/youtube/v3/quickstart/apps-script#troubleshooting) section below for some common errors and solutions. Thanks for letting us know and we'll work to fix this quickstart.

## Further reading

- [Google Apps Script Advanced Services documentation](https://developers.google.com/apps-script/guides/services/advanced)
- [YouTube Data API reference documentation](https://developers.google.com/youtube/v3/docs)

## Troubleshooting

#### ReferenceError: "\[API NAME\]" is not defined

This error occurs when the API hasn't been toggled on in the Apps Script code
editor. Revisit Step 2.b and ensure the corresponding toggle is set to **on**.