# Source: https://docs.xano.com/the-database/migrating-your-data/csv-import-and-export.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CSV Import & Export

## Export a Table or View

Click the <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c2073af7-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=ffb4db2de3e6d5bc3f88d57967279972" className="inline m-0" width="27" height="31" data-path="images/c2073af7-image.jpeg" /> icon and choose **Export CSV** from the dropdown menu.

Check the <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/bfa16808-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=f70f22a8fe89f167787fff783b5c8ec2" className="inline m-0" width="252" height="45" data-path="images/bfa16808-image.jpeg" /> option to export only the currently selected [database view](/the-database/database-basics/database-views).

You will receive an email once your export is complete.

## Export Specific Records

Check the box next to the records you want to export and click the  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2f7ab94b-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=29a54e9c89a0451620b52dd96cbe4490" className="inline m-0" width="77" height="35" data-path="images/2f7ab94b-image.jpeg" /> button.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2f1e41c4-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=775ad8e9199abcf1ee1798fcc1b6f064" width="599" height="420" data-path="images/2f1e41c4-image.jpeg" />
</Frame>

Your export may take a few moments depending on the size, but should download automatically.

## Importing a CSV

Xano's CSV file import is ultra-robust. Import your file with confidence, even if you have millions of records. The import process runs on Xano's special import service, which has dedicated resources separate from your instance, so it can handle all of your data no matter how large it is.

The CSV file import allows you to create a brand new table from scratch and will generate the schema automatically.

Additionally, you can edit existing records if the file can be mapped to a primary key or append data to an existing table.

Uploads of over 5,000 records will be performed in the background. You can easily monitor the import's progress in the settings of your workspace and will be notified on Xano and via email when the import is complete.

### Add a New Table

From the database select Add Table.

<Frame caption="Select Add Table and Select Import Data.">
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b06083d5-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=e26acd0f4bdaa2e5cd9c62bba5eb6a39" width="1483" height="292" data-path="images/b06083d5-image.jpeg" />
</Frame>

When the right panel opens up, select **Import Data** and choose the **CSV** file option.

<Frame caption="Select import data from CSV.">
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/c7e372d5-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=922171ec1012816883d429f146fb2e9c" width="404" height="289" data-path="images/c7e372d5-image.jpeg" />
</Frame>

Next, drag and drop a CSV file onto the uploader or browse the files on your computer for the file you wish to upload.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2f14d5d5-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=b9f22d6ea97fbd6abb6e691b2582ef2b" width="2304" height="464" data-path="images/2f14d5d5-image.jpeg" />
</Frame>

Once you select a CSV file, the preview of your CSV will open up. The preview will display the first 100 rows of your file. You can make any final adjustments to the data types, primary key, or table name here before beginning the import.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0d68827b-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=960c4a0f8cdca4c0497746435c5e22c4" width="2304" height="1073" data-path="images/0d68827b-image.jpeg" />
</Frame>

Xano will try to automatically detect a primary key field. Currently, only integers are supported for the primary key field. The drop-down will show any fields compatible to be a primary key. If there is no primary key, then Xano will create the primary key automatically.

Once you are ready, click Upload . If you are uploading over 5,000 records, then your upload will be performed in the background. You can monitor the progress of your upload from the settings page of your workspace. Once your background upload is complete a green banner will appear notifying you to refresh your browser and an email notification will be sent with confirmation of a successful import.

<Info>
  **Add to an Existing Table**

  You can import a CSV to an existing table if you'd like to add records to it. The process is the same as importing to a new table — just access the import option from inside of the database table you want to add to.

  <Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b79145d5-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=366e308216202a87a53c8656749185a7" width="900" height="207" data-path="images/b79145d5-image.jpeg" />
  </Frame>

  During the import, make sure to review the columns and make sure they are mapped to the right columns that already exist in your database table.

  <Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/9070f054-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=53bbdf0a2933dc08e9e39705813ff433" width="900" height="457" data-path="images/9070f054-image.jpeg" />
  </Frame>
</Info>

<Info>
  **Edit Records in an Existing Table**

  Just like adding records to an existing table, you can also use a CSV upload to **edit records** in a table.

  The only difference between adding a new table or adding to an existing table is that you'll need to make sure your CSV contains an `id` field. This is what Xano will use to find the records to apply changes to.
</Info>

### Valid CSV Format

It's important that you use a valid CSV file format in order to successfully import your data. If there is an issue with initiating the upload then this could likely be the issue.

#### What is a valid CSV file format?

A CSV stands for a comma-separate file, which is a\*\* \*\*delimited text file that uses a **comma** to separate values. The importer does not support other separators, such as semicolons. Each line of the file is a data record. Each record consists of one or more fields, separated by commas.

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

<Card title="Xano-Sample-CSV.csv" icon="file-arrow-down" href="https://3699875497-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tWsL4o1vHmDGb2UAUDD%2Fuploads%2FTcftKcnn1uEplLEXG1qg%2FXano-Sample-CSV.csv?alt=media&token=f037ad45-d0ca-4962-a338-a0b8e0a28776">
  Here is a sample CSV file demonstrating both the proper separator and enclosure characters.
</Card>

#### How can I check my CSV file format?

You can review the format of your CSV file format in a number of ways. Open the file in Text Editor, Visual Studio Code, or another code editor. You can also do an online search for CSV file format validators and use an online service.

**How can I edit my CSV file format?**

Tools like Text Editor, Visual Studio Code, and other code editors allow you to make any necessary edits to your file and save the changes. When opening the file from your computer, right click and choose open with to choose from the different options available on your computer.


Built with [Mintlify](https://mintlify.com).