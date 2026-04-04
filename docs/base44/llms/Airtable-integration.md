# Source: https://docs.base44.com/Integrations/Airtable-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Airtable Integration

> Connect your Base44 app to Airtable to bring your live data into dashboards, tools, and workflows.

<Info>
  <u>Note</u>: Airtable integration is available on Builder tier and above. If you're on the Free tier, you'll need to upgrade your app to use backend functions and payment features.
</Info>

# Step by step setup:

## Part 1: The Airtable side

If you already have a Airtable API token and Base ID, feel free to skip ahead to [**Part 2: The Base44**](https://docs.base44.com/Integrations/Airtable-integration#part-2%3A-the-base44-side) side.

<Steps>
  <Step title="Create a Personal Access Token">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/AirtableBuilderHub.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=76937cf25bdd1fd4c0c868b440a75a8d" alt="Airtable Builder Hub Pn" width="1901" height="944" data-path="images/AirtableBuilderHub.png" />

    * Go to [<u>Airtable’s token creation page</u>](https://airtable.com/create/tokens/new) .
    * Under "Scopes," create a token scoped to the correct workspace/base with at least:
      * `data.records:read`
      * `schema.bases:read`  *(optional but helpful for testing)*
    * Name your token, set a credit limit if you use them, and copy the token somewhere safe.
  </Step>

  <Step title="Find your Base ID">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/HRTable.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=b08891d38f2972511b423d5bf467a005" alt="HR Table Pn" width="1891" height="944" data-path="images/HRTable.png" />

    1. Open your Airtable base in a browser.
    2. Look at the URL and copy the string starting with "**app**" as this is your Base ID

       Example: `https://airtable.com/app123XYZ/...`
  </Step>
</Steps>

***

## Part 2: The Base44 side

Once you have your API token and Base ID, you can connect it to Base44 in two different ways:

<CardGroup cols={2}>
  <Card icon="sparkle" href="https://docs.base44.com/Integrations/Airtable-integration#option-a%3A-ready-made-integration-create-a-new-app" title="Option A: Ready-made integration (preferred)">
    * Choose this path if you are starting a new app from scratch.
  </Card>

  <Card icon="bolt" href="https://docs.base44.com/Integrations/Airtable-integration#option-b%3A-add-airtable-as-an-instant-integration" title="Option B: Instant integration">
    * Choose this path if you are already in the midst of building and would like to integrate Airtable into an existing app.
  </Card>
</CardGroup>

### Option A: Ready-made integration (create a new app)

<Steps>
  <Step title="Add Airtable from the Integrations Catalog">
        <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Integrations.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=16ac71b185167177ef260be7c92b0339" alt="Integrations Pn" width="1570" height="652" data-path="images/Integrations.png" />

    * In the integrations catalog, select Airtable
    * Then click "Use this integration"

      <img src="https://mintcdn.com/base44/-Vklow6W-uVvNnvR/images/image7.png?fit=max&auto=format&n=-Vklow6W-uVvNnvR&q=85&s=041a8013c65236fe5f17e3d7303461ab" alt="Image7 Pn" width="1877" height="878" data-path="images/image7.png" />
  </Step>

  <Step title="Paste your secrets">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/B44AirtableIntegration.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=591c4433e5721fab7cbb0b82c6d847a9" alt="B44airtable Integration Pn" width="1877" height="867" data-path="images/B44AirtableIntegration.png" />

    * When prompted, paste:
      * `AIRTABLE_API_KEY`
      * `AIRTABLE_BASE_ID`
  </Step>

  <Step title="Build your app">
    * Here's a sample prompt you can use:

      `“Build an internal dashboard. We will connect to my Airtable base and show real records. Include a Sync Status page and start by letting me choose a table before building visuals.”`
    * The app runs a test call to Airtable and lists your tables
    * You select one
    * It fetches real records and shows a raw data table so that the schema is clear
  </Step>

  <Step title="Sync status page">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/HRDashboardSync.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=b381c4548b5efb2c3135ad1df01d02e3" alt="HR Dashboard Sync Pn" width="1873" height="869" data-path="images/HRDashboardSync.png" />

    You’ll get a page with the following:

    * A **Check Connection** button to re-run the test
    * Table list
    * Last check time
    * Connection status
  </Step>
</Steps>

***

### **Option B: Add Airtable as an Instant integration**

Choose this path if you already have an app in progress.

<Steps>
  <Step title="Access your existing app">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/HRDashboard.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=8409b5ee99da7d9ff4dc41c36adbfff4" alt="HR Dashboard Pn" width="1876" height="871" data-path="images/HRDashboard.png" />

    * Here's the prompt that we typed out in the AI chat to build our sample app:

      `“Build an internal dashboard. Let me pick a data source later.”`
  </Step>

  <Step stepNumber={2} title="Connect to Airtable through the AI chat">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/ConnectAirtableApp.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=124a38233bf1d5dba4f7df5365c14142" alt="Connect Airtable App Pn" width="1874" height="868" data-path="images/ConnectAirtableApp.png" />

    * Here's a sample prompt that we pasted in our AI chat:

      `Connect this app to Airtable. Ask me for AIRTABLE_API_KEY and AIRTABLE_BASE_ID and save them as Secrets. Add a backend function that can test the connection and fetch records. Create a Sync Status page with a Check Connection button.`
    * Click on "**Set secrets**" in the AI chat
    * Paste your **API Key** and **Base ID** when prompted
  </Step>

  <Step stepNumber={3} title="Fetch tables and show data">
    * Prompt the AI chat to show you the data
    * Here's a sample prompt that we used for our app:

      `Run the connection test to list my tables, let me pick one, then fetch records and show a raw table view before any visuals.`
  </Step>

  <Step stepNumber={4} title="Test your app">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/HRDashboardSync.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=b381c4548b5efb2c3135ad1df01d02e3" alt="HR Dashboard Sync Pn" width="1873" height="869" data-path="images/HRDashboardSync.png" />

    * Open **Sync Status** and click **Check Connection**
    * Choose a table and confirm you see live rows
  </Step>
</Steps>

***

## **Troubleshooting**

* **403 or connection failed** – Token scope is wrong. Make sure data.records:read is enabled. Add schema.bases:read if table listing fails.
* **Wrong Base ID** – Double-check you copied the app… string from the URL.
* **No data shown** – Make sure the base actually has records and the token has access.
* **Public preview vs builder session** – Stay logged into the builder while testing Sync Status.

***

## **Common use cases**

Here are a few ways teams often use Airtable with Base44:

* **Dashboards** – Pull in Airtable data and visualize it in real time.
* **Data management** – Give teammates a friendly UI for viewing or checking Airtable records.
* **Sync monitors** – Create a Sync Status page to quickly test connections and confirm updates.
* **Internal tools** – Build lightweight apps (like CRM views or content trackers) on top of Airtable without custom code.


Built with [Mintlify](https://mintlify.com).