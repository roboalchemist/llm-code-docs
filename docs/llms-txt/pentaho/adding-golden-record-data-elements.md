# Source: https://docs.pentaho.com/pentaho-data-mastering/setting-up-business-domains/adding-golden-record-data-elements.md

# Adding golden record data elements

Add Golden Record data elements to a business domain to control how that data is processed in the Master Records before the Master Records can be transformed into Golden Records.

**Note:** At least one source record data element is added when you create the business domain.

Complete the following steps to add more Golden Record data elements to a business domain:

1. On the left navigation menu, click **Master Data**. The **Master Data** page opens.
2. In the Business Domains card, click **Business Domains**.

   The Business Domain page opens with the business domains shown in a table.
3. In the row that contains the business domain you want to add Golden Record data elements to, click the more actions icon and select **View Details**.

   The Edit Business Domain page opens.
4. Click the **Golden Record** tab.

   The Golden Record Data Elements page is shown with the Golden Record data elements shown in a table.
5. Click **Add Golden Record Data Element** > **Create new**.

   The Create Golden Record Data Element page opens.
6. Specify the following information:

| Field                     | Description                                                                                                                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**\*                | Name of the source record data element.                                                                                                                                                                                                |
| **Column Name**\*         | Column name for the source record data element.                                                                                                                                                                                        |
| **Column Data Type**      | Type of data in the column. For example, text, numeric, date, or Boolean.                                                                                                                                                              |
| **Merge Rule**            | The rule that applies to the Golden Record data element during merging of records.                                                                                                                                                     |
| **Linked source columns** | The section where you can drag and drop source record data elements to change the order that they are shown in the Golden Record Data Elements table.                                                                                  |
| **Source Value**          | Determines how the value from one or more sources is selected to use in the Golden Record data element of the Golden Record table.**Tip:** If you select the Evaluated with expression option, you can enter multiple SQL expressions. |
| **Resolved Value**        | Controls whether a mandatory value that you specified in an SQL expression is needed for the column.                                                                                                                                   |
| **UI Width**              | Width of a data element in pixels, on the user interface.                                                                                                                                                                              |
| **UI Fixed**              | A list of options to select whether a column is fixed from the left, right, or both sides of the column. Fixed columns cannot be resized.                                                                                              |
| **Enabled**               | Checkbox that controls whether the data element is enabled.                                                                                                                                                                            |
| **Editable**              | Checkbox that controls whether the data element is editable on the Master Records table.                                                                                                                                               |
| **Searchable**            | Checkbox that controls whether the data element is searchable using global search.                                                                                                                                                     |
| **Reviewable**            | Checkbox that controls whether further review of the data element is required.                                                                                                                                                         |
| \* Mandatory Field        |                                                                                                                                                                                                                                        |

7\. Click \*\*Create Golden Record Data Element\*\*.

```
A confirmation message is shown in the top-right corner of the page and the Golden Record Data Elements page is opened.
```

8\. At the end of the row that contains the Golden Record data element that you created, click the more options icon and select **Add Sources**.

```
The Link Source Columns window opens and shows the available source record data elements.
```

9\. Select the checkbox for one or more source record data elements that you want to link to the Golden Record data element.

10. (Optional) In the Linked source columns, drag and drop the selected source record data elements to change the order they are shown in.
11. Click **Link** .

    The confirmation dialog box appears.
12. Click **Confirm**.

    The source record data elements are now linked to the Golden Record data element and the Golden Record Data Elements page is opened.
13. (Optional) Change the order of the Golden Data element by completing the following steps:

    1. Click the **General** tab.
    2. In the Order of displaying Data Elements section, drag and drop the data elements to change the order the data elements are shown in.

    **Tip:** You can hide a source record data element from the table by dragging and dropping it under Hidden Source Data Elements.
14. Click **Run MDM Engine**.

    The Run MDM Engine for dialog box opens, showing the values for Engine State, Started At, and Finished At parameters from the last time the engine ran.
15. On the Run MDM Engine for dialog box, click **Run MDM Engine**.

    The values are updated for the Engine State, Started At, and Finished At parameters.
16. Close the Run MDM Engine for dialog box.
