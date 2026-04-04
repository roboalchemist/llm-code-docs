# Source: https://docs.replit.com/getting-started/quickstarts/google-sheets-integration.md

# Create a Google Sheets integration

> Build an app that connects to Google Sheets using Python. Learn how to fetch and process spreadsheet data on Replit.

Learn how to create an application that interacts with Google Sheets. This guide shows you how to access and display spreadsheet data using Python and pandas.

## What you'll learn

<CardGroup cols={2}>
  <Card title="Google Sheets" icon="table">
    Connect to spreadsheet data
  </Card>

  <Card title="Data Processing" icon="database">
    Work with pandas dataframes
  </Card>

  <Card title="API Integration" icon="plug">
    Use Google's API services
  </Card>

  <Card title="Authentication" icon="lock">
    Handle OAuth and service accounts
  </Card>
</CardGroup>

## Create your app

<Steps>
  <Step title="Fork the template">
    Sign in to Replit and fork the [Google Sheets to HTML Renderer](https://replit.com/@replit-matt/Google-Sheets-to-API#README). Select **+ Use Template** and follow the prompts to create your Replit App.
  </Step>

  <Step title="Configure for public sheets">
    1. Open `main.py`
    2. Replace `WORKSHEET_URL` with your Google Sheet URL
    3. Set `require_auth=False` for public sheets

    <Tip>
      A worksheet refers to a single tab in a Google Sheet. Make sure to use the correct tab's URL.
    </Tip>
  </Step>

  <Step title="Configure for private sheets">
    1. Enable Google Sheets API access:

       * Enable Drive and Spreadsheets APIs
       * Follow the [API setup guide](https://gspread.org/en/v6.0.0/oauth2.html#enable-api-access-for-a-project)

    2. Create a [service account](https://gspread.org/en/v6.0.0/oauth2.html#for-bots-using-service-account)

    3. Add the service account JSON to your Replit App's Secrets as `SERVICE_ACCOUNT_JSON`

    4. Share your sheet with the service account email

    <Note>
      Service accounts provide secure, automated access to your sheets.
    </Note>
  </Step>
</Steps>

## Publish your app

<Steps>
  <Step title="Set up publishing">
    1. Select **Publish** in the workspace header
    2. Choose **Reserved VM** deployment
    3. Select **Publish**
  </Step>

  <Step title="Test">
    Your app will be live in a few minutes. Test it by accessing the HTML endpoint in your browser.
  </Step>
</Steps>

## Customization options

<CardGroup cols={2}>
  <Card title="Data Processing">
    * Modify data transformations
    * Add filtering options
    * Create custom views
  </Card>

  <Card title="Display">
    * Customize HTML rendering
    * Add interactive features
    * Style your output
  </Card>
</CardGroup>

## Next steps

<CardGroup cols={3}>
  <Card title="FastAPI" icon="bolt" href="/getting-started/quickstarts/fastapi-service">
    Create an API service
  </Card>

  <Card title="Databases" icon="database" href="/cloud-services/storage-and-databases/sql-database/">
    Add persistent storage
  </Card>
</CardGroup>

## Related guides

<CardGroup cols={2}>
  <Card title="Create a Slack bot" icon="slack" href="/getting-started/quickstarts/webscrape-and-slack-notifications">
    Build a Slack integration
  </Card>

  <Card title="Build with AI" icon="wand-magic-sparkles" href="/getting-started/quickstarts/build-with-ai">
    Create apps using Agent
  </Card>
</CardGroup>

<Note>
  Want to learn more about API integrations? Check out our [publishing documentation](/category/replit-deployments).
</Note>
