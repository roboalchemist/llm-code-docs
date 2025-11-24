# Source: https://docs.apify.com/academy/node-js/scraping-urls-list-from-google-sheets.md

# Scraping a list of URLs from a Google Sheets document

You can export URLs from https://workspace.google.com/products/sheets/ such as https://docs.google.com/spreadsheets/d/1-2mUcRAiBbCTVA5KcpFdEYWflLMLp9DDU3iJutvES4w directly into an https://docs.apify.com/platform/actors.md's Start URLs field.

1. Make sure the spreadsheet has one sheet and a simple structure to help the Actor find the URLs.

2. Add the `/gviz/tq?tqx=out:csv` query parameter to the Google Sheet URL base, right after the long document identifier part. For example, https://docs.google.com/spreadsheets/d/1-2mUcRAiBbCTVA5KcpFdEYWflLMLp9DDU3iJutvES4w/gviz/tq?tqx=out:csv. This automatically exports the spreadsheet to CSV format.

3. In the Actor's input, click Link remote text file and paste the URL there:

![List of URLs](/assets/images/gsheets-url-27adbc7f89057db71fc4d2f03a65cedf.png)

IMPORTANT: Make sure anyone with the link can view the document. Otherwise, the Actor will not be able to access it.

![Link sharing](/assets/images/anyone-with-link-38a1b714c55ca2b0f1ee21c9adaed0a3.png)
