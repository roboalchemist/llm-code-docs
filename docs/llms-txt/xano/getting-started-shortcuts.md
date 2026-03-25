# Source: https://docs.xano.com/the-database/getting-started-shortcuts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started Shortcuts

## Getting Started Shortcuts

When entering the database in Xano, you're presented with some quick shortcuts to get started faster. This section of our documentation is designed to accompany those shortcuts.

<CardGroup cols={2}>
  <Card>
    ✨ **Modify your table schema with AI**
  </Card>

  <Card>
    📔 **Import data from a CSV**
  </Card>

  <Card>
    **Import data from Airtable**
  </Card>

  <Card>
    🪄 **Generate test records for table**
  </Card>

  <Card>
    💡 **Create flows from database triggers**
  </Card>
</CardGroup>

## Modify your table schema with AI

<Steps>
  <Step title="Choosing this option opens our AI Database Assistant.">
    The database assistant can be used to modify your database schema. You can prompt it to add or edit existing tables, delete tables, and help you design your database while following best practices.
  </Step>

  <Step title="Prompting the AI Database Assistant">
    Your prompts to the assistant can be as simple or as complex as necessary. Here's a quick example:

    <Frame caption>
            <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/69545139-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=75fcc8d52cd7887354c3a4535a29cde3" alt="" width="796" height="242" data-path="images/69545139-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Approving Changes">
    Each change that the assistant suggests will need to be approved individually. This ensures that no changes are made that you do not explicitly review first. In addition, some changes rely on the previous change being completed — the assistant will notify you of this as you continue.

    For each table being created, you can choose to just create the table, or create the table and [default CRUD API endpoints](/the-function-stack/building-with-visual-development/apis#auto-generated-apis) at the same time.

    <Frame caption>
            <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d3789573-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=60b84db07250d39572d1f0681d689b9b" alt="" width="426" height="165" data-path="images/d3789573-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Review and Iterate">
    You can leave and return to the Database Assistant at any time. Here's the final schema we ended up with using the above example of an Airbnb-style application.

    <Frame caption>
            <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/975db15d-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=820585530d2bcf09504d42c8bc12d263" alt="" width="2211" height="1217" data-path="images/975db15d-image.jpeg" />
    </Frame>
  </Step>
</Steps>

***

## Import data from a CSV

Xano's CSV file import is ultra-robust. Import your file with confidence, even if you have millions of records. The import process runs on Xano's special import service, which has dedicated resources separate from your instance, so it can handle all of your data no matter how large it is.

The CSV file import allows you to create a brand new table from scratch and will generate the schema automatically.

Additionally, you can edit existing records if the file can be mapped to a primary key or append data to an existing table.

Uploads of over 5,000 records will be performed in the background. You can easily monitor the import's progress in the settings of your workspace and will be notified on Xano and via email when the import is complete.

### Add a New Table

From the database select Add Table.

<Frame caption="Select Add Table and Select Import Data.">
    <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b06083d5-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=e26acd0f4bdaa2e5cd9c62bba5eb6a39" alt="" width="1483" height="292" data-path="images/b06083d5-image.jpeg" />
</Frame>

When the right panel opens up, select **Import Data** and choose the **CSV** file option.

<Frame caption="Select import data from CSV.">
    <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/c7e372d5-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=922171ec1012816883d429f146fb2e9c" alt="" width="404" height="289" data-path="images/c7e372d5-image.jpeg" />
</Frame>

Next, drag and drop a CSV file onto the uploader or browse the files on your computer for the file you wish to upload.

<Frame caption>
    <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2f14d5d5-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=b9f22d6ea97fbd6abb6e691b2582ef2b" alt="" width="2304" height="464" data-path="images/2f14d5d5-image.jpeg" />
</Frame>

Once you select a CSV file, the preview of your CSV will open up. The preview will display the first 100 rows of your file. You can make any final adjustments to the data types, primary key, or table name here before beginning the import.

<Frame caption>
    <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0d68827b-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=960c4a0f8cdca4c0497746435c5e22c4" alt="" width="2304" height="1073" data-path="images/0d68827b-image.jpeg" />
</Frame>

Xano will try to automatically detect a primary key field. Currently, only integers are supported for the primary key field. The drop-down will show any fields compatible to be a primary key. If there is no primary key, then Xano will create the primary key automatically.

Once you are ready, click Upload . If you are uploading over 5,000 records, then your upload will be performed in the background. You can monitor the progress of your upload from the settings page of your workspace. Once your background upload is complete a green banner will appear notifying you to refresh your browser and an email notification will be sent with confirmation of a successful import.

<Info>
  Add to an Existing Table

  You can import a CSV to an existing table if you'd like to add records to it. The process is the same as importing to a new table — just access the import option from inside of the database table you want to add to.

  <Frame caption>
        <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b79145d5-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=366e308216202a87a53c8656749185a7" alt="" width="900" height="207" data-path="images/b79145d5-image.jpeg" />
  </Frame>

  During the import, make sure to review the columns and make sure they are mapped to the right columns that already exist in your database table.

  <Frame caption>
        <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/9070f054-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=53bbdf0a2933dc08e9e39705813ff433" alt="" width="900" height="457" data-path="images/9070f054-image.jpeg" />
  </Frame>
</Info>

<Info>
  Edit Records in an Existing Table

  Just like adding records to an existing table, you can also use a CSV upload to **edit records** in a table.

  The only difference between adding a new table or adding to an existing table is that you'll need to make sure your CSV contains an `id` field. This is what Xano will use to find the records to apply changes to.
</Info>

### Valid CSV Format

It's important that you use a valid CSV file format in order to successfully import your data. If there is an issue with initiating the upload then this could likely be the issue.

#### What is a valid CSV file format?

A CSV stands for a comma-separate file, which is a delimited text file that uses a **comma** to separate values. The importer does not support other separators, such as semicolons. Each line of the file is a data record. Each record consists of one or more fields, separated by commas.

* The first row must contain the column names - not the file name or any other data.
* The second row begins the values. They should be in the same order as the columns they belong to.
* Each row should have the same amount of values as there are columns.
* **Enclosure characters** are required when working with text strings that contain quotation marks. This is because if a quotation mark is detected, this is typically something that would mark the beginning or end of a value. You can use a **double quote ("")** to dictate if a value should contain this quotation mark somewhere inside the value.
* CSV files should be UTF-8 encoded. If you're having trouble importing your CSV properly in Xano and have determined you are using both the proper separator and enclosure characters, please make sure your file us UTF-8 encoded. This ensures that there are no special characters that might not be supported in Xano.

<AccordionGroup>
  <Accordion title="UTF-8 Encoding in Notepad (Windows)">
    1. Open your file in Notepad.
    2. Click File > Save As...
    3. Click "Save As Type", and choose All Files.
    4. Click "UTF-8" in the Encoding dropdown.
    5. Save the file.
  </Accordion>

  <Accordion title="UTF-8 Encoding in Google Sheets (All platforms)">
    1. Open your file in Google Sheets
    2. Click File > Download > Comma separated values (CSV)
    3. The file will be downloaded in CSV format using UTF-8 encoding.
  </Accordion>

  <Accordion title="UTF-8 Encoding in Numbers (Mac)">
    1. Open your file in Numbers
    2. Click File > Export To... > CSV
    3. In the "Text Encoding" dropdown, choose UTF-8
    4. Save the file.
  </Accordion>
</AccordionGroup>

<Card title="Xano-Sample-CSV.csv" icon="file-arrow-down" horizontal href="https://3699875497-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tWsL4o1vHmDGb2UAUDD%2Fuploads%2FTcftKcnn1uEplLEXG1qg%2FXano-Sample-CSV.csv?alt=media\&token=f037ad45-d0ca-4962-a338-a0b8e0a28776">
  160B

  **Here is a sample CSV file demonstrating both the proper separator and enclosure characters.**
</Card>

#### How can I check my CSV file format?

You can review the format of your CSV file format in a number of ways. Open the file in Text Editor, Visual Studio Code, or another code editor. You can also do an online search for CSV file format validators and use an online service.

**How can I edit my CSV file format?**

Tools like Text Editor, Visual Studio Code, and other code editors allow you to make any necessary edits to your file and save the changes. When opening the file from your computer, right click and choose open with to choose from the different options available on your computer.

***

## Import data from Airtable

<Steps>
  <Step title="Head to the database and click + Add table" />

  <Step title="In the new table menu, choose Import Data > Import From Airtable" />

  <Step title="Provide your Airtable personal access token">
    You can generate a personal access token in Airtable by heading to your account settings, and from there visiting the **Developer Hub**.

    Choose **Personal Access Tokens** from the left-side navigation, and create a token with the following scopes:

    ```
    data:base.read
    schema:base.read
    ```
  </Step>

  <Step title="Select the tables and/or views you want to import into Xano, and confirm your selection" />
</Steps>

***

### Rebuilding Automations

While there is no direct migration of your Airtable automations to Xano, we want to make it as easy as possible to rebuild. Please see the table and linked resources below for common Airtable -> Xano functionality translations. Click on the Xano Function name to be taken to Xano's documentation, or review the video examples provided.

| Airtable Function      | Xano Function                                                                            | Video Example                                 |
| ---------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------- |
| Create Record          | [Add Record](/the-function-stack/functions/database-requests/add-record)                 | [Video Example](https://youtu.be/k0GpUdsRkL0) |
| Update record          | [Edit record](/the-function-stack/functions/database-requests/edit-record)               | [Video Example](https://youtu.be/rTeJamc_MYE) |
| Find records           | [Query all records](/the-function-stack/functions/database-requests/query-all-records)   | [Video Example](https://youtu.be/-XjcXEtPNmk) |
| Conditional logic      | [Conditional statement](/the-function-stack/functions/data-manipulation/conditional)     | [Video Example](https://youtu.be/QR4UJ2GpYDo) |
| Repeating group        | [For each loop](/the-function-stack/functions/data-manipulation/loops)                   | [Video Example](https://youtu.be/AGe5JN0rZ2M) |
| At scheduled time      | [Background task](/the-function-stack/building-with-visual-development/background-tasks) | [Video Example](https://youtu.be/SDXWVhBGKmQ) |
| Link to another record | [Table reference](/the-database/database-basics/field-types#table-reference)             | [Video Example](https://youtu.be/z-TwxiQOIBs) |
| Lookup                 | [Addons](/the-function-stack/functions/database-requests/query-all-records#using-addons) | [Video Example](https://youtu.be/z-TwxiQOIBs) |

***

## Generate test records for table

After you've created your database schema, you can generate some sample data to use right away by clicking 🪄**Generate Records**

This option is located at the **bottom** of your database records — so, if you have no records, you should see it right at the top.

<Frame caption>
    <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a48209cc-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=9c0c46ad71670a30ab01a5a4c5e51b28" alt="" width="1051" height="230" data-path="images/a48209cc-image.jpeg" />
</Frame>

The record generation will look at the name and the data type for each of your fields and try to auto-suggest what they should be filled with.

<Frame caption>
    <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3907a803-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=ca3d427c7f8f85da6e4134bd3b922de2" alt="" width="873" height="440" data-path="images/3907a803-image.jpeg" />
</Frame>

You can click on one of those data types to change what that field is populated with, or specific settings related to that data type.

<Frame caption>
    <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/6ee0b56f-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=4f3c16f3ac19d67d358738305d1393a1" alt="" width="729" height="619" data-path="images/6ee0b56f-image.jpeg" />
</Frame>

In the bottom-right corner, you can change the number of records generated, up to 100 at a time.

When you're ready, click "Generate" and you should see your new sample data populated. You can always generate more records if you'd like.

<Frame caption>
    <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/43b546eb-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=5d2373765174ce66e865df5f0c677eba" alt="" width="881" height="792" data-path="images/43b546eb-image.jpeg" />
</Frame>

<Check>
  **Hint**

  Want to clear out all of the sample data? There's a quick "Clear All Records" shortcut in the upper-right settings menu. **This will delete all records in the table in one swing.**
</Check>

***

## Create flows from database triggers

You can find database triggers on each table by clicking the settings icon in the top-right corner.

Click + Add Database Trigger to create a new database trigger.

You can specify what [Data Sources](/the-database/database-basics/data-sources) the trigger will execute on. If no data source is set, then it will execute on all data sources.

Select the **actions** that will activate this trigger.

**Inserts** Any time a record is added to the table

**Updates** Any time a record is edited

**Deletes** Any time a record is deleted

**Truncates** When the content of the database table is cleared

Finally, you can set up custom filters so that the trigger only runs if the record matches certain conditions. For example, if you only want the trigger to run if a new order is created for a user, or a new user is created with a certain role.

***

Database triggers have predefined inputs that contain all of the information you'll need to build a workflow based on the database event.

`new` This is the contents of the new record — if you're adding a record, this will contain the contents of the new record, and if you're updating a record, this will contain the contents of the updated record. On deletes and truncates, this will be empty.

`old` This is the contents of the old record — if you're deleting or editing a record, this will contain the contents of the record before the change. On inserts and truncates, this will be empty.

`action` The action that activated the trigger

`data source` The datasource this trigger has been executed against


Built with [Mintlify](https://mintlify.com).