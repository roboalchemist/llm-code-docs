# Source: https://docs.pentaho.com/pentaho-data-mastering/setting-up-business-domains/adding-a-business-domain.md

# Adding a business domain

Add a business domain so that you can work with a specified category of data.

You must have admin privileges to add a business domain.

Perform the following steps to add a business domain:

1. On the left navigation menu, click **Master Data**. The **Master Data** page opens.
2. Click **Add Business Domain** > **Create New**.

   The Create Business Domain page opens.
3. Click the General tab.
4. Specify the following information:

   | Field                           | Description                                                                                                                                                                                                                                   |
   | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | General                         |                                                                                                                                                                                                                                               |
   | **Code**\*                      | Unique identifier for a business domain. For example, USR is the code for Users.                                                                                                                                                              |
   | **Name**\*                      | Name of the business domain.                                                                                                                                                                                                                  |
   | **UI Position**\*               | Position of a business domain in the business domains table.                                                                                                                                                                                  |
   | **Description**                 | Description of the business domain.                                                                                                                                                                                                           |
   | **Enabled**                     | Checkbox that indicates whether a business domain is usable or not.                                                                                                                                                                           |
   | Source Record Table             |                                                                                                                                                                                                                                               |
   | **Local**                       | Checkbox that indicates whether a business domain is local or not. Local business domain data is stored in the PostgreSQL database.                                                                                                           |
   | **External Data source**\*      | External source of the incoming data. External business domain data is stored in a database other than the PostgreSQL database used by local business domains. For a local business domain, the External Data source field is not applicable. |
   | **Table name**                  | Name of the source record table.                                                                                                                                                                                                              |
   | **Schema name**\*               | Database schema name of the source record table, regardless of whether the table is local or external.                                                                                                                                        |
   | **Key column name**\*           | Name of the Key column.                                                                                                                                                                                                                       |
   | **Check table availability**    | Button that validates whether the source record table name is available. If the table name is in use, an error is shown.                                                                                                                      |
   | Golden Record Table             |                                                                                                                                                                                                                                               |
   | **Local**                       | Checkbox that indicates whether a business domain is local or not.                                                                                                                                                                            |
   | **Table name**                  | Name of the Golden Record table.                                                                                                                                                                                                              |
   | **Schema name**\*               | Database schema name of the Golden Record table regardless of whether the table is local or external.                                                                                                                                         |
   | **Key column name**\*           | Key column name of the Golden Record table.                                                                                                                                                                                                   |
   | **Key column value template**\* | Name of the Key column value template . The value template controls how the text in the Key column is formatted.                                                                                                                              |
   | **Data source**                 | Local source of the incoming data.                                                                                                                                                                                                            |
   | \* Mandatory Field              |                                                                                                                                                                                                                                               |
5. Click **Create Business Domain** to create the new business domain.

   A confirmation message is shown in the top-right corner of the page and the **Source Record** and **Golden Record** tabs are made available so that you can add more source record data elements and golden record data elements to the business domain.

* [Adding source record data elements](https://docs.pentaho.com/pentaho-data-mastering/setting-up-business-domains/adding-source-record-data-elements)
* [Adding golden record data elements](https://docs.pentaho.com/pentaho-data-mastering/setting-up-business-domains/adding-golden-record-data-elements)
