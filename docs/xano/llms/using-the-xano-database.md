# Source: https://docs.xano.com/the-database/database-basics/using-the-xano-database.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using The Xano Database

<Info>
  **Hint**

  Use the ✨[**AI Database Assistant**](/xano-ai/ai-database-assistant) to create and update tables for you!
</Info>

## 👨‍🏭 Create a Database Table

<Frame>
  <iframe src="https://demo.arcade.software/lYQQDmkQE0whqrIzhV98?embed" title="https://demo.arcade.software/lYQQDmkQE0whqrIzhV98?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" />
</Frame>

<Steps>
  <Step title="Head to the database">
    Click **Database** in the left hand menu.
  </Step>

  <Step title="Add a new table">
    Click **Add Table** in the top right corner.

    Choose **Import Data** to [import data from a CSV file](/the-database/migrating-your-data/csv-import-and-export), or **Enter Data Manually** to start with an empty table where you can add your own data later, or generate sample data automatically.

    <Tip>
      If you're just starting out, we'd recommend choosing **Enter Data Manually** and using the sample data generator. You can always import data later.
    </Tip>

    In the panel that opens, give your table a <Tooltip tip="When naming your table, it's considered best practice to use camelCase for multiple words, and to not use plurals in the table name. For example, a table of dog breeds would be named dogBreed">name</Tooltip> and a <Tooltip tip="The description is just for you to make notes on what this table will contain, notable data constraints, or any other information you'd like to store.">description</Tooltip>
  </Step>

  <Step title="Give your table a name and a description.">
    When naming your table, it's considered best practice to use camelCase for multiple words, and to not use plurals in the table name. For example, a table of dog breeds would be named `dogBreed`

    The description is just for you to make notes on what this table will contain, notable data constraints, or any other information you'd like to store.
  </Step>

  <Step title="Choose your primary key type.">
    The primary key is the ID of each record. Xano offers two types of primary keys to choose from.

    <Info>
      **When should you use Sequential, and when should you use UUID?**

      When designing your database structure in Xano, choosing the right identifier type is an important decision. Here's a straightforward guide to help you decide:

      **Sequential IDs are best for:**

      * Performance-sensitive operations - they're faster to index and query
      * Human-friendly references - easier to communicate ("Please check record #42")
      * Storage efficiency - they consume less space in your database
      * When chronological order matters - the sequence reveals creation order
      * Single-database applications where centralized ID generation works well
      * Systems that benefit from predictable numbering patterns

      **Common use cases:** Customer IDs, order numbers, ticket systems, invoice numbers, internal record tracking

      **UUIDs are best for:**

      * Distributed systems where multiple services create records independently
      * Data synchronization across different databases or systems
      * Preventing ID guessing or enumeration attacks
      * Frontend-first workflows where IDs need to be generated before server contact
      * Multi-region deployments with separate databases
      * When you don't want to expose information about record counts
      * Scenarios where data privacy is paramount

      **Common use cases:** User accounts in modern applications, cross-system record tracking, session management, event logging in distributed architectures
    </Info>

    <Info>
      Please note that there is **no support** for converting tables to / from different primary key types. However, this can be done with a manual migration to a new table.
    </Info>

    <AccordionGroup>
      <Accordion title="Sequential (1, 2, 3...)">
        A sequential identifier is just a sequence of whole numbers (1, 2, 3, etc...).

        Think of sequential IDs like numbered tickets at a deli counter. They start at 1 and count up one by one (2, 3, 4...). Just like how the first customer gets ticket #1, the first row in your database gets ID #1. This system is straightforward but requires coordination - just as you can't have two deli counters giving out the same numbers (it would confuse customers), you need to ensure you're not creating duplicate IDs across different parts of your system.
      </Accordion>

      <Accordion title="UUID">
        A UUID is like the serial number on your electronics - something like "550e8400-e29b-41d4-a716-446655440000". It's longer and looks random, similar to how no two iPhone serial numbers are alike, even if they were made in different factories. This makes UUIDs particularly useful when you have data coming from multiple sources or need to merge databases - you don't have to worry about ID conflicts, just like how Apple doesn't need to check with Samsung about what serial numbers they're using.

        Some users feel that using UUIDs is also more secure. UUIDs do provide some security benefits through obscurity - you can't easily guess other valid IDs by simply incrementing a number. If a website shows you order #1234, you might guess that order #1235 exists. But if you see order 550e8400-e29b-41d4-a716-446655440000, you can't easily guess other valid orders.

        However, it's crucial to understand that using UUIDs is not a replacement for proper security measures. You should never rely on the difficulty of guessing IDs as your only security mechanism. Proper authentication and authorization should be in place regardless of ID type.
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Add some tags.">
    Tags in Xano can be applied to any object (tables, APIs, functions, etc...) and are used to easily find related objects when searching your workspace.
  </Step>

  <Step title="Choose to add basic CRUD endpoints.">
    Xano can provide you with some standard pre-built APIs for basic operations against this table. If you choose this option, you'll also want to supply an **API Group** for those endpoints to live in. You can always choose to generate these endpoints later, too.
  </Step>

  <Step title="Confirm your choices.">
    Once you've confirmed all of your settings are as you want them to be, click **Add Table**.
  </Step>
</Steps>

***

## ℹ️ Navigating the Table View

Let's start with the top control bar.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/27e4c105-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=9be34eb2438751a0d30a1192406e243b" alt="" width="1352" height="260" data-path="images/27e4c105-image.jpeg" />
</Frame>

<AccordionGroup>
  <Accordion title="🧭 Navigation Controls">
    <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2ea9f3b7-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=d958ddcd1c861229ee7afa4b4dba30a9" className="inline m-0" width="191" height="71" data-path="images/2ea9f3b7-image.jpeg" />

    Table name, ID, description, and tags

    <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/31ccddbe-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=4b1c3bea2e8eadb4164df30fb4a20b6c" className="inline m-0" width="90" height="40" data-path="images/31ccddbe-image.jpeg" />

    Go back to your list of database tables.

    <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/9e804b80-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=5b3c9132d0514e833e2c269fbd05dc74" className="inline m-0" width="39" height="42" data-path="images/9e804b80-image.jpeg" />

    Refresh the list of records

    <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/5f45aee1-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=fafbde053f93e1c1b6353abbfee6365b" className="inline m-0" width="161" height="44" data-path="images/5f45aee1-image.jpeg" />

    Change the database view
  </Accordion>

  <Accordion title="🔎 Searching, Filtering, and Sorting">
    <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e2e62295-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=37937e90354b96acacfa9e56e7acd699" className="inline m-0" width="106" height="39" data-path="images/e2e62295-image.jpeg" />

    Search for specific records

    <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/91e478a9-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=9e3924d4c66717edb2e8858564219336" className="inline m-0" width="91" height="41" data-path="images/91e478a9-image.jpeg" />

    Filter your records by certain conditions, such as "all records with an ID greater than 100"

    <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/94ae896f-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=50d48f85e74775f7334c0a8895306916" className="inline m-0" width="88" height="47" data-path="images/94ae896f-image.jpeg" />

    Sort your database records

    <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f05b837a-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=8e8a34b4441708423fb57a12c7e69b65" className="inline m-0" width="142" height="42" data-path="images/f05b837a-image.jpeg" />

    Hide database fields from view
  </Accordion>

  <Accordion title="🧰 Tools and Advanced Controls">
    <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b1408a40-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=6b29df475a4337efd515b801625e50cb" className="inline m-0" width="283" height="53" data-path="images/b1408a40-image.jpeg" />

    Cut, Copy, Paste, Undo, and Redo

    <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/7da638c8-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=9763e67ee9d73a56f843609ae3c670a9" className="inline m-0" width="37" height="40" data-path="images/7da638c8-image.jpeg" />

    Show Schema

    <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5571e534-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=7f62dcd4d7f23dc3a7a2db56a16f6e9d" className="inline m-0" width="39" height="40" data-path="images/5571e534-image.jpeg" />

    Show References

    <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b3505084-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=65a52f57a97e27ea48bd5cc4494ac282" className="inline m-0" width="42" height="41" data-path="images/b3505084-image.jpeg" />

    Indexes

    <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f6488769-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=c2911eb55cb3f7fe6cccba28abc07471" className="inline m-0" width="41" height="37" data-path="images/f6488769-image.jpeg" />

    Review available keyboard shortcuts for the database view
  </Accordion>
</AccordionGroup>

Just below the control bar, you'll see your database records.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/045856d6-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=30c79926de48e540a2f15a7918ca599b" alt="" width="1834" height="362" data-path="images/045856d6-image.jpeg" />
</Frame>

Use your mouse or arrow keys to navigate between records and individual cells.

To modify data, just select the cell and make your desired changes. They will be saved automatically.

<Frame>
  !\[]\(/images/image (1).gif)
</Frame>

<img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e67f5881-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=866d0b845d57fd800deb2efaa4eba7fb" className="inline m-0" width="41" height="44" data-path="images/e67f5881-image.jpeg" />

Select one or more records by checking these boxes

<img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/348a9b2e-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=34539258f3bd1968538d1a77d2d8f901" className="inline m-0" width="154" height="105" data-path="images/348a9b2e-image.jpeg" />

Open a card view of the selected record

<img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2d0ec65f-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=e4d4a48518dd5e60f0a6fb9a4c4f25ba" className="inline m-0" width="106" height="51" data-path="images/2d0ec65f-image.jpeg" />

Add a new field

***

## ➕ Adding a new field

<Warning>
  **When Working in Large Tables**

  Making changes to your schema, such as renaming or adding fields in a extremely large table requires significant server resources. Please contact support if you encounter any issues.
</Warning>

Click the plus sign to add a new field, and choose the [type of field](/the-database/database-basics/field-types) you want to add from the panel that opens.

After you've selected your desired field type, you will be presented with a number of options. You can review each one of them and what they mean below.

| Setting               | Required? | Description                                                                                                                                                                                                                                                                                       |
| --------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                  | ☑️        | The name of the field you are creating                                                                                                                                                                                                                                                            |
| Description           | ☐         | Add additional details here                                                                                                                                                                                                                                                                       |
| Data Structure        | ☑️        | **Single** - Each record will only store one value in this field. This is the more common selection. **List** - Each record can hold multiple values in this field. For example, if this was a table of authors, we might have a field that can store multiple books for each author.             |
| Allow Nullable Values | ☐         | A `null` value is similar to an empty value in that it represents "nothing is here", but it's still an actual value written to the record. Useful if you need to specifically check whether or not that field has data stored.                                                                    |
| Format                | ☐         | For some field types, you can specify a format. This does not change the actual data being stored and is only used to enable easier viewing and editing for you inside of the table view.                                                                                                         |
| Default Value         | ☐         | When adding new records, you can automatically populate a default value \*\*Note: \*\*If your field allows nullable values, they will auto-apply null to new records as a default value. Adding 'null' to the default value field manually will be processed as text and have unintended results. |

<Info>
  **Note**

  The settings listed below only impact your API endpoints that utilize the database link feature. This means that it is possible to make changes that break these rules via the database table view.
</Info>

| Setting                | Required? | Description                                                                                                                                                          |
| ---------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Required               | ☐         | Determines whether or not this field is required when adding a record                                                                                                |
| Sensitive Data         | ☐         | Hide the contents of this field from certain areas, such as request history                                                                                          |
| Column Visibility      | ☐         | **Public** - The field will be available as an input **Private** - This field will not appear in inputs **Internal** - Hide this field from API inputs and responses |
| Custom Rules & Filters | ☐         | See below.                                                                                                                                                           |

#### Custom Rules & Filters

For each field, you can apply various rules and filters to ensure that the data is stored in the format that you expect.

| Filter Name | Purpose                                          |
| ----------- | ------------------------------------------------ |
| min         | Enforces a minimum number of required characters |
| max         | Enforces a maximum number of required characters |
| startsWith  | Enforces a prefix                                |
| endsWith    | Enforces a suffix                                |
| prevent     | Blacklists phrases                               |
| lower       | Stores the value in all lowercase                |
| upper       | Stores the value in all uppercase                |
| alphaOk     | Whitelist certain alphanumeric characters        |
| digitOk     | Whitelist certain numbers                        |
| ok          | Whitelist certain characters                     |
| pattern     | Enforce a regex pattern                          |

***

\##⚙️ Field Options

Right-click on the header of a field to access field-related settings and make adjustments to the options already detailed above, as well as some additional controls.

<img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/396c3c92-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=8f9aa7c0da8469b3d3154b95f260e7b6" className="inline m-0" width="38" height="37" data-path="images/396c3c92-image.jpeg" />

Rename this field

<Warning>
  Please note that renaming a field should be handled with care, as it may impact any function steps that reference that field.

  You can click the plug icon when viewing a database table to open **Referenced By** and view any database operations that utilize that column first to understand where changes need to be made. In the screenshot below, we know we want to update the name column, so we can use **Referenced By** to find where it's used beforehand.

  <Frame>
        <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/7ee073d7-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=fdbe8ce18e24d85ee4747d032483e95f" alt="" width="443" height="542" data-path="images/7ee073d7-image.jpeg" />
  </Frame>
</Warning>

<img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/bb40c834-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=96345a1751cbbdb8e0bd59ee3bf04641" className="inline m-0" width="36" height="37" data-path="images/bb40c834-image.jpeg" />

Access field settings (the options detailed earlier in this document)

<img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4d7abcde-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=da9f509fc38107a3061ec2546a597001" className="inline m-0" width="39" height="36" data-path="images/4d7abcde-image.jpeg" />

Make a copy of this column

<img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/00d882ca-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=a20b4643721e8e5436331abfd54072b3" className="inline m-0" width="31" height="38" data-path="images/00d882ca-image.jpeg" />

Insert a new column directly after the selected column

<img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b0bcd717-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=1b8b9972304098812de51cfa08e6938e" className="inline m-0" width="22" height="21" data-path="images/b0bcd717-image.jpeg" />

Reorder your database fields. This does not impact how the data is returned in your function stacks.

<img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/20f51e76-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=94b9836d0d9a412f3abf8bdba0b244bf" className="inline m-0" width="41" height="43" data-path="images/20f51e76-image.jpeg" />

Change the data type of the column

<Warning>
  Xano will attempt to convert the data in the column to the new data type, but because of potential variations between data types, and the specific data being converted, this may not always be successful. It is **always** recommended to create a new column instead.
</Warning>

<img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/13867846-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=f2857c589ce06997984a2fb4a9c679f7" className="inline m-0" width="46" height="42" data-path="images/13867846-image.jpeg" />

Delete the column

<Warning>
  Deleting a column is irreversible. Proceed with caution.
</Warning>

***

## 🔢 Adding Data

### Generate Test Data using AI

After you've created your database <Tooltip tip="Schema is just another way to refer to the collection of fields you've added to your database, and the type of data they expect.">schema</Tooltip>, you can generate some sample data to use right away by clicking **Generate Records**. This option is located at the **bottom** of your database records — so, if you have no records, you should see it right at the top.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a48209cc-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=9c0c46ad71670a30ab01a5a4c5e51b28" alt="" width="1051" height="230" data-path="images/a48209cc-image.jpeg" />
</Frame>

The record generation will look at the name and the data type for each of your fields and try to auto-suggest what they should be filled with.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3907a803-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=ca3d427c7f8f85da6e4134bd3b922de2" alt="" width="873" height="440" data-path="images/3907a803-image.jpeg" />
</Frame>

You can click on one of those data types to change what that field is populated with, or specific settings related to that data type.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/6ee0b56f-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=4f3c16f3ac19d67d358738305d1393a1" alt="" width="729" height="619" data-path="images/6ee0b56f-image.jpeg" />
</Frame>

In the bottom-right corner, you can change the number of records generated, up to 100 at a time.

When you're ready, click "Generate" and you should see your new sample data populated. You can always generate more records if you'd like.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/43b546eb-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=5d2373765174ce66e865df5f0c677eba" alt="" width="881" height="792" data-path="images/43b546eb-image.jpeg" />
</Frame>

<Tip>
  **Hint**

  Want to clear out all of the sample data? There's a quick "Clear All Records" shortcut in the upper-right settings menu. **This will delete all records in the table in one swing.**
</Tip>

### Adding Data Manually

Click \*\*Add New Record \*\*at the bottom of your existing records (if any) to add a new record.

The record will be created using any default values you've specified in the field options, and you can click on each cell to fill it in manually.

You can also click the two arrows icon to open up the card view and fil in multiple, or all fields at once when creating a new record.

***

\##⚙️ Additional Table Settings

Click the settings icon in the top-right corner to access table settings after creation, including both settings detailed earlier in this document, as well as some additional options.

| Setting Name      | Description                                                                                                                                                                                                                                                                                                                                                       |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication    | Determines whether or not this table is used for [user authentication](/building-backend-features/user-authentication-and-user-data).                                                                                                                                                                                                                             |
| Security          | Change the table GUID.                                                                                                                                                                                                                                                                                                                                            |
| Versions          | Xano maintains a version history of your table schema. You can roll back to a previous version of your schema if you've made changes that you want to undo. **Note**: This does not change the data in your table, only the fields. If you need to restore a backup of your table data, see [this document](/xano-features/instance-settings/backup-and-restore). |
| Triggers          | Access your database triggers.                                                                                                                                                                                                                                                                                                                                    |
| Auto-complete     | Access your auto-complete settings.                                                                                                                                                                                                                                                                                                                               |
| Clear all records | Deletes all records in the table. You can also choose to reset the primary ID back to 1 on tables that use a sequential ID.                                                                                                                                                                                                                                       |
| Clone table       | Cloning copies the table schema. Cloning **does not** copy existing data.                                                                                                                                                                                                                                                                                         |
| Export data       | Export your table data using the current view as a CSV                                                                                                                                                                                                                                                                                                            |
| Import data       | Import records from a CSV 📖[**Learn More**](/the-database/migrating-your-data/csv-import-and-export)                                                                                                                                                                                                                                                             |

***

## Table Format

<Info>
  **Table Formats - Only relevant for direct database connections**

  As of our **1.68 release (5/27/25)**, all new workspaces will default to the standard SQL column format for tables. For all workspaces created prior to that, read below.
</Info>

Your tables can be created using one of two formats:

* **JSONB format**
  * This creates your tables with two columns:
    * `id` - the ID of the record
    * `jsonb` - contains a JSON representation of the entire record
* **Standard SQL format**
  * This creates a more standard table layout. Instead of a jsonb column, each column is written separately.

If you are using the [Direct Database Connector](/xano-features/instance-settings/direct-database-connector), Standard SQL format is usually recommended.

### **When to Convert to Standard SQL Format:**

* You need direct database connections with third-party tools that aren't friendly to JSONB format, such as Tableau or PowerBI
* You want faster performance for non-indexed queries
* You're frequently adding new fields (faster column additions)
* You plan to use SQL analytics tools or run complex reports directly against your database

### **When to Keep JSONB Format:**

* You're satisfied with current performance
* You don't need direct database connections

### Converting Tables from JSONB to standard SQL

<Warning>
  This change is **permanent**. Most users will not need to adjust these settings, and they only impact your experience if you are connecting to your database directly via third-party tools.
</Warning>

<Steps>
  <Step title="From your workspace dashboard, click the settings icon in the upper-right corner, and click Settings." />

  <Step title="Scroll down to the Database Preferences section, and check the option to 'Use standard SQL columns for new tables'">
    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/eb6ad281-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=46618b9fb76997b2da5873a1cd2bb54d" alt="" width="689" height="203" data-path="images/eb6ad281-image.jpeg" />
    </Frame>

    This setting must be enabled before you can convert existing tables to the new format.
  </Step>

  <Step title="Convert your table(s) from your workspace settings, or the settings of any table.">
    From the migration panel, select any of the tables you'd like to convert, and confirm your choices. The migration will begin immediately.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/727090c5-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=b221e9dbfd6e8bb8ab6eba835bd292c8" alt="" width="763" height="1415" data-path="images/727090c5-image.jpeg" />
    </Frame>
  </Step>
</Steps>

***

## Custom SQL Table Names

From your Workspace settings, you can enable **Custom SQL Table Names**.

By default, Xano assigns each table a SQL name in the format mvpw\_ (e.g., mvpw1\_3). This identifier works for direct access, but can be difficult to read or use with direct queries and database tools.

You can replace this with a custom SQL name to make queries more intuitive and improve compatibility with external connectors.

If you change a table's SQL name, be sure to update any queries that reference the old name to avoid breaking functionality.

Once you've enabled **Custom SQL Table Names**, head to any database table's settings, and click Manage next to SQL Table Name.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e3e08966-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=8b411bca8716c88da4700cee2b8e57fd" alt="" width="745" height="188" data-path="images/e3e08966-image.jpeg" />
</Frame>

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/65aa79c8-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=dddc2fb2296af151ba47dd06794c7022" alt="" width="516" height="784" data-path="images/65aa79c8-image.jpeg" /> | - Leave the SQL Table Name field blank to use Xano’s default SQL table name, which follows the format mvpw\<workspaceID>\_\<tableID> (e.g., mvpw1\_3).<br />- SQL table names must be globally unique across all workspaces. **Hint**: Use the Custom Prefix to ensure uniqueness across workspaces.<br />- Datasources automatically add a suffix based on their environment. For example, **users** becomes **users\_test** in the test datasource.\* To reuse the same base name across workspaces, use a workspace<br />-specific prefix (e.g., projA\_users, projB\_users). |


Built with [Mintlify](https://mintlify.com).