# Source: https://docs.base44.com/Building-your-app/Managing-your-app-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing your app data

> Stay organized and power your app with easy, flexible data management.

***

In Base44, your app’s data is the information that brings everything to life. It includes all the information that your app holds, such as people who sign in, the content you show, orders you process, and the activities that happen in your app.

<Frame caption="An example of an app's data with sample data entities including Child, Task and Reward.">
    <img src="https://mintcdn.com/base44/hRVAQC-epRy8MmTv/images/2025-10-12_16-56-08.png?fit=max&auto=format&n=hRVAQC-epRy8MmTv&q=85&s=211d47d70c86dfc7a1ada0f993adc8f1" alt="An example of an app's data with sample data entities including Child, Task and Reward." width="1388" height="329" data-path="images/2025-10-12_16-56-08.png" />
</Frame>

***

## Understanding your data

All of your app's data is organized in tables, just like a spreadsheet. Each table groups one type of info (such as people or products) and sorts it into columns called fields, such as names, dates, or prices.

For example, if you create an app to run your shop’s business, you can use the data tables in Base44 to keep everything organized. You might have a **Users** data table to store your customers' names and email addresses, a **Products** table listing what you sell, and an **Orders** table to track every purchase.

Each new customer, product, or order is automatically added as a new row in the right table, so you can quickly find, update, or manage your shop’s information.

<div style={{ display:"flex",justifyContent:"center" }}>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/IIESzXPt4Lg?si=v4tQRxEkuvtDG190" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</div>

***

## Data field types

When you, or the AI, add a field (column) to your table, you choose what type of information it stores. Some common field types include:

* **Text:** For words, phrases, or descriptions (such as customer names or product details)
* **Number:** For prices, quantities, or measurements
* **Yes/No (Boolean):** For fields that are true or false (such as “Is active?”)
* **Date/Time:** To save dates such as sign-up day, order date, or event time
* **File:** For images, documents, or other files
* **Reference:** To link this table to another table (for example, linking each order to the right customer)
* **Object:** For advanced cases, this lets you add structured information such as a JSON object

***

## Accessing your app's data

It is easy to see all the information your app collects. You can view your data at any time from the dashboard, where each table gives you a clear, organized look at your people, products, orders, and more. This helps you track what is happening in your app and keep everything up to date.

### Viewing your app's data

1. Click **Dashboard** in your app editor.
2. Click **Data**.
3. Select the relevant data set (table).

<Frame caption="Accessing your app data from your app's dashboard">
    <img src="https://mintcdn.com/base44/1jZm1sK8B6PTUNJ5/accessingdata.png?fit=max&auto=format&n=1jZm1sK8B6PTUNJ5&q=85&s=434610d47298e01b6b7d1fcf17d8be0a" alt="Accessing your app data from your app's dashboard" width="1287" height="716" data-path="accessingdata.png" />
</Frame>

### Searching for specific data

Use the search bar above the table to quickly find relevant rows. The search looks through all text fields in your data, so you can jump straight to a specific row instead of scrolling.

**To search for data:**

1. Click **Dashboard** in your app editor.
2. Click **Data**.
3. Enter a word, number or phrase in the search bar above the table.

<Frame caption="Searching your data with the search bar">
    <img src="https://mintcdn.com/base44/vOZyx5RR9AYtChJ8/images/search-2.png?fit=max&auto=format&n=vOZyx5RR9AYtChJ8&q=85&s=4808a7377f17f78f416ca5593978a398" alt="Search 2" width="1000" height="555" data-path="images/search-2.png" />
</Frame>

### Filtering your data

Use filters to turn a long table into a focused view, for example to see only shipped features, items owned by your team, or work planned for a specific quarter.

The filters displayed come from the fields in your data set, so each table has its own relevant list of filter options.

**To filter your data:**

1. Click **Dashboard** in your app editor.
2. Click **Data**.
3. Click **Filters** in the top right of the table and select your filters.

<Frame caption="Using the filters to find specific data">
    <img src="https://mintcdn.com/base44/Jm_JWuHs1y2NOICT/images/filters-2.png?fit=max&auto=format&n=Jm_JWuHs1y2NOICT&q=85&s=d769656b5baf8409545e652681c1ad58" alt="Filters 2" width="1000" height="559" data-path="images/filters-2.png" />
</Frame>

***

## Adding and updating data

Base44 automatically collects and updates your app’s data as people interact with your app. The AI sets up your tables so the right information is saved and kept up to date for you. However, if you want to manually add information (for example, add a product, update a record, or input test data), you can do it easily from your app’s dashboard inside your app editor.

### Manually adding data

1. Click **Dashboard** in your app editor.
2. Click **Data**.
3. Select the relevant data set (table).
4. Click **Add**.
5. Enter the data and click **Submit**.

<img src="https://mintcdn.com/base44/6P44SXvF1rla5XC7/images/adddatabase44.png?fit=max&auto=format&n=6P44SXvF1rla5XC7&q=85&s=9be74d656985780e83fcc02e6ded92af" alt="Adding data in Base44" width="1385" height="377" data-path="images/adddatabase44.png" />

### Editing data

To edit a data record, click the row of the table that you want to edit, complete the details and click **Submit**.

### Deleting data

Delete your app's data at any time.

<Note>
  **Note:** You can view and restore recently deleted records from any data table. Deleted records are kept for 30 days, so you have time to recover information if needed. Click the **More Actions** icon <Icon icon="ellipsis" /> on the top of the data table and click **Recently Deleted** to see and restore deleted records. After 30 days the data is permanently deleted and cannot be restored.
</Note>

To delete a single record, click the **Delete** icon on the relevant row of the table.

<img src="https://mintcdn.com/base44/6P44SXvF1rla5XC7/images/deletingdatainbase44.png?fit=max&auto=format&n=6P44SXvF1rla5XC7&q=85&s=bb54280410ff1d68530c86fbd7102bc9" alt="Deleting data in Base44" width="1385" height="377" data-path="images/deletingdatainbase44.png" />

To delete all the records in a table, click the **More Actions** icon <Icon icon="ellipsis" /> on the data entity and click **Delete All**.

You can also ask the AI chat to delete records for you. The AI prepares the delete action and asks for your approval before anything is removed.

**To delete data with the AI chat:**

1. Open the AI chat in your app editor.
2. Describe what you want to delete, for example: `Delete the data for Italy in the TripItem entity.`
3. Review the delete request that the AI suggests, including the entity name.
4. Click **Approve** to confirm the deletion, or **Reject** to cancel.

<Frame caption="Asking the AI chat to delete data">
    <img src="https://mintcdn.com/base44/hGe-Ql9GXLBIhxFk/images/deletedata.png?fit=max&auto=format&n=hGe-Ql9GXLBIhxFk&q=85&s=dd48ef090c08dfcbdbb5593b786b305e" alt="Asking the AI chat to delete data" width="1178" height="504" data-path="images/deletedata.png" />
</Frame>

***

## Exporting data

You might want to take your app's data out for backup, analysis, or to use in other tools. To do this, you can use the **Export** option. For example, you might want to export your store orders or people lists to share with your accountant, or use the data to create custom reports.

Your data downloads as a CSV file you can open in spreadsheet software such as Excel or Google Sheets.

**To export your app's data:**

1. Click **Dashboard** in your app editor.
2. Click **Data**.
3. Select the relevant data set (table).
4. Click the **More Actions** icon <Icon icon="ellipsis" /> and click **Export**.

<Frame caption="Exporting data from your app's dashboard">
    <img src="https://mintcdn.com/base44/XtjNWvgxMN6xIAI7/images/exportdata2-1.png?fit=max&auto=format&n=XtjNWvgxMN6xIAI7&q=85&s=42ab59ee5f290a31acc6529a02b0d0c5" alt="Exporting data from your app's dashboard" width="1411" height="399" data-path="images/exportdata2-1.png" />
</Frame>

***

## Importing data

Sometimes you want to bring in lots of information to your app at once. You can import data in 2 ways, depending on whether you want to work directly in the dashboard or ask the AI chat to help.

<Note>
  **Note:** Imports add new rows to your tables. They do not update or overwrite existing records.\
  If you want your file to replace the data in a table, first delete the current records in that table, then run the import again with your file.
</Note>

### Using the AI chat

Use this option when you want the AI to help you set up tables, map fields, or import complex data. You can upload structured data files such as CSV, Excel or JSON in the AI chat and ask it to create or update entities for you.

Supported formats for importing data with the AI chat include CSV (.csv), Excel (.xlsx, .xls) and JSON (.json). If you upload an Excel file with multiple sheets, you can ask the AI to import a single sheet or import all sheets into their matching entities.

<Warning>
  **Important:** This feature is in the process of being released and is not available to all accounts yet.
</Warning>

**To use the AI chat to import data:**

1. Open the AI chat in your app editor.
2. Click the **Upload files** icon and select your data file.
3. Ask the AI to import the data.
4. Review the response and approve the import in the chat.

<Frame caption="Approving an import of data in the AI chat">
  <img src="https://mintcdn.com/base44/s5ffECMyaO66Tzol/images/approveimport.png?fit=max&auto=format&n=s5ffECMyaO66Tzol&q=85&s=55000885c4c1cbf741e07300a8fbd8ab" alt="Approving import of data in the AI chat" title="Approving import of data in the AI chat" className="mx-auto" style={{ width:"60%" }} width="494" height="846" data-path="images/approveimport.png" />
</Frame>

Example prompts you can use:

* `Import this data into the Customers entity.`
* `Import this JSON file into my Orders entity.`
* `Import the ‘Orders’ sheet into the Orders entity.`
* `Here is a CSV of my Products. Create a Products entity with matching fields and import these rows.`

When you import data this way, Base44 analyzes your file structure, maps columns to your entity fields, and can create or update entities if your schema needs to change. This means it can add new entities or fields, or adjust field types to match your file. It does not update or overwrite existing records in that entity. It always appends new rows.

If something does not match, the AI updates the schema where it is safe to do so, then retries the import so you do not need to fix everything manually.

<Note>
  **Note:** For file size limits and more details about uploading files to the AI chat, see [Uploading and managing files](/Building-your-app/Using-media).
</Note>

**To use the AI chat to replace existing data:**

If you want the content of a file to replace all the current records in an entity, you need to clear the entity first, then import the new rows from your file.

1. Ask the AI chat to delete the records in the relevant entity (for example, `Delete all records from the Orders entity.`).
2. Confirm that you want to delete the records.
3. Click the **Upload files** icon and select your data file.
4. Ask the AI chat to import the file into the same entity.

<Tip>
  **Tip:** Before you delete records, consider exporting the table so you have a backup copy of your original data.
</Tip>

### Directly in the dashboard

Use this option when you already have a CSV that matches your table and you simply want the rows to appear in your data. Dashboard imports currently support CSV (.csv) files.

<Frame caption="Importing data from your app's dashboard">
    <img src="https://mintcdn.com/base44/PJDSkWp1vwFhxR97/images/importdata-1.png?fit=max&auto=format&n=PJDSkWp1vwFhxR97&q=85&s=6e6fdb9d71dab304a915a959641dc4a2" alt="Importing data from your app's dashboard" width="1411" height="399" data-path="images/importdata-1.png" />
</Frame>

**To import data from the dashboard:**

1. Click **Dashboard** in your app editor.
2. Click **Data**.
3. Select the relevant data set (table).
4. Click the **More Actions** icon and click **Import**.
5. Choose your CSV file and click **Open**.

<Note>
  **Note:** Imports from the dashboard also add new rows only. They do not update or overwrite existing records. If you want to replace everything in a table with the content of a CSV file, first click **Delete All** on that table to clear the records, then import the CSV.
</Note>

Example: Export your customer list from another tool as a CSV, adjust the columns to match your **Customers** table, then import the file so you can manage those customers directly in Base44.

***

## Changing data permissions

Each data table has its own security settings, controlling who can **read** and **write** its data.

**Read Access**: Who can view records\
**Write Access**: Who can create, update, or delete records

<Note>
  **Note:** For more detailed explanations, see the [Managing security settings guide](/Setting-up-your-app/Managing-security-settings).
</Note>

**To change the permissions for your data:**

1. Click **Dashboard** in your app editor.
2. Click **Security**.
3. Click the relevant data entity and set the permissions.

<img src="https://mintcdn.com/base44/6P44SXvF1rla5XC7/images/dataentitypermissions.png?fit=max&auto=format&n=6P44SXvF1rla5XC7&q=85&s=f995a6648bbe3bb34a015413028b3eac" alt="Editing data permissions in Base44" width="1380" height="443" data-path="images/dataentitypermissions.png" />

***

## Connecting your data to another app

You can let another app read or write data from your Base44 app. This is useful if you want to sync information, automate tasks, or give access to outside tools.

1. Click **Dashboard** in your app editor.
2. Click **API**.
3. Select the relevant data entity from the drop-down menu.
4. Choose which code sample you need (for example, JavaScript or Python).
5. Copy the provided code for reading or updating data.
6. Paste this code into the other app or tool, so it knows how to connect to your table.

<img src="https://mintcdn.com/base44/hRVAQC-epRy8MmTv/images/2025-10-12_16-53-28.png?fit=max&auto=format&n=hRVAQC-epRy8MmTv&q=85&s=624022ca02c21810252f0b1a2d475512" alt="Getting code examples for data entities in Base44" width="1388" height="493" data-path="images/2025-10-12_16-53-28.png" />

***

## FAQs

Select a question below to learn more about your app's data.

<AccordionGroup>
  <Accordion title="Can I merge my apps together?">
    It is not currently possible to automatically merge two separate apps into a single app in Base44. Each app is managed as an independent project with its own codebase, settings, permissions, and integrations.

    If you want to combine the features of two apps, you need to manually recreate or copy code, components, and settings from one app to the other. After combining the code and functionality, thoroughly test the new app to make sure everything works as expected.
  </Accordion>

  <Accordion title="Can I delete all the data I created while I was testing my app?">
    Yes, to delete your data, go to **Data** in your app's dashboard. On the relevant data tab, click **More Actions** and then **Delete All**. You can access and restore the deleted data for 30 days but after that it is permanently deleted.

        <img src="https://mintcdn.com/base44/aY6VhQ9_9JTKTSpT/images/2025-10-05_11-29-40.png?fit=max&auto=format&n=aY6VhQ9_9JTKTSpT&q=85&s=bced613d1bc4121461e542263a5580db" alt="Delete data entities in Base44" width="1363" height="285" data-path="images/2025-10-05_11-29-40.png" />
  </Accordion>

  <Accordion title="Can I recover my data after deletion?">
    You can access and restore your deleted data for 30 days. After that, deleted data is permanently removed and cannot be restored.
  </Accordion>

  <Accordion title="Is it safe to let the AI add test data?">
    Yes. You can safely ask the AI chat to add mock data for testing. By default, it adds new records without changing or removing existing ones, so your important information stays protected.

    For structured testing, it is better to use the built-in test data feature instead of adding ad hoc mock records to your live tables. Test data lets you quickly generate, reset, and remove sample records without affecting your real production data. Learn more in [Testing your data](/documentation/managing-app-data/testing-your-data).

    If you do choose to add test records directly to a table with the AI chat, you can clear them later from the dashboard by deleting those records.
  </Accordion>

  <Accordion title="Can the AI chat delete my existing data?">
    The AI chat focuses on adding and importing data. It does not remove records unless you clearly ask it to delete data from a specific entity and confirm the action.

    If you want to replace all data in an entity with the content of a file, the safe pattern is:

    * Export the current table if you want a backup.
    * Ask the AI chat to delete the records in the relevant entity.
    * Upload your file and ask the AI chat to import it into the same entity.

    This makes sure the entity is cleared first, then filled with the new rows from your file.
  </Accordion>

  <Accordion title="Can I change the table structure (data schema)?">
    If you want to add a new column (field) or make other changes to your data tables, ask the AI chat to do it for you. The AI chat handles updates to your data schema, you just need to describe what you want to change.

    For example, if you want to add a "Notes" column to one of your data tables, prompt the chat to add it. It is best if you use Discuss mode in the chat to help the AI decide how to go about the change before implementing it.
  </Accordion>

  <Accordion title="Is there a limit to how many items I can pull with one data request?">
    Starting November 27, 2025, there is a limit of 5,000 items per request to help keep performance fast, stable, and reliable.

    If your app currently pulls everything in one large request, you may need to update it to load data in smaller pieces. Once this change goes live, double-check your flows to make sure everything still works as expected.

    <Tip>
      **Tip:** To make sure you are within the limitation, you can paste this message into the Base44 AI chat: “Make sure all data pull requests are limited to 5,000 items.”
    </Tip>
  </Accordion>

  <Accordion title="Why do I only see some of my data? Have I lost the rest?">
    You have not lost your data. When a collection has more than 5,000 records, the system limits how many items can load at once to protect performance. What you see depends on where you are looking:

    * **In your dashboard**: The data table only shows up to 5,000 items, even if your collection contains more. All of your records are still stored. To review everything, export the collection to CSV from the dashboard so you can see all items outside the table view.
    * **In your app pages**: Pages that try to fetch the entire collection in one request also only show up to 5,000 items. The rest of the records are still there, but they are not loaded on that page. Set up pagination so your app loads data in smaller chunks, for example 50 to 200 items at a time. You can ask the AI chat to add pagination for you.
  </Accordion>

  <Accordion title="Can I build custom roles and hierarchies (for example, managers and teams) in my app?">
    Yes. You can build a full role and hierarchy system in your app, including managers, teams, and even separate spaces for each customer if you are building a SaaS app.

    At a high level, the pattern works like this:

    * People sign up and sign in through the normal Base44 login flow. Their account details are stored in the built-in **User** entity. You do not change the security rules of this entity.
    * You create your own entities to model your business, for example Company, Team, and TeamMember.
    * Each record in these entities links back to a User record using a reference field, such as userId. This lets you connect login accounts with your own business roles.
    * You use data permissions and row-level security on your entities so each person only sees the records they should see.

    For example:

    * In a SaaS app, each Company record can represent one of your customers. Data permissions make sure people from one company cannot see another company’s data.
    * Within each company, TeamMember records can store fields such as role, manager, and team. You can then set rules so managers see all records for their team, while individual team members only see their own records or items assigned to them.
    * Global admins in your app can have a role that allows them to see and manage all records across companies and teams.

    This approach lets you support complex, multi-level apps (sometimes called “User of User” or UoU) while Base44 continues to manage login and the core User entity securely. To design the exact rules, use the data permissions and row-level security options described in the [Managing security settings](/Setting-up-your-app/Managing-security-settings) guide.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).