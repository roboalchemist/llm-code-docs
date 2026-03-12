# Source: https://docs.pentaho.com/pentaho-data-mastering/setting-up-business-domains/adding-source-record-data-elements.md

# Adding source record data elements

Add source record data elements to tie the source record to the Golden Record and to control how the data is processed in the Master Records.

**Note:** At least one source record data element is added when you create the business domain.

Complete the following steps to add more source record data elements to a business domain:

1. On the left navigation menu, click **Master Data**. The **Master Data** page opens.
2. In the Business Domains card, click **Business Domains**.

   The Business Domain page opens with the business domains shown in a table.
3. In the row that contains the business domain you want to add source record data elements to, click the more actions icon and select **View Details**.

   The Edit Business Domain page opens.
4. Click the **Source Record** tab.

   The Source Record Data Elements page is shown with the source record data elements shown in a table.
5. Click **Add Source Record Data Element** > **Create new**.

   The Create Source Record Data Element page opens.
6. Specify the following information:

   | Field                | Description                                                                                                                               |
   | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
   | **Name**\*           | Name of the source record data element.                                                                                                   |
   | **Column Name**\*    | Column name for the source record data element.                                                                                           |
   | **Column Data Type** | Type of data in the column, which includes text, numeric, date, and Boolean.                                                              |
   | **UI Width**         | Width of the source record data element in pixels, on the user interface.                                                                 |
   | **UI Fixed**         | A list of options to select whether a column is fixed from the left, right, or both sides of the column. Fixed columns cannot be resized. |
   | **Enabled**          | Checkbox that indicates whether the data element is enabled or not.                                                                       |
   | **Choosable**        | Checkbox that indicates if the source record value can be selected on the Master Records table to use in the Master Record.               |
   | **Searchable**       | Checkbox that indicates if the data element is searchable by using the global search.                                                     |
   | \* Mandatory Field   |                                                                                                                                           |
7. Click **Create Source Record Data Element**. A confirmation message is shown in the top-right corner of the page.
