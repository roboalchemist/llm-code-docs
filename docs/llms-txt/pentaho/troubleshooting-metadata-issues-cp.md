# Source: https://docs.pentaho.com/pba-metadata-editor/troubleshooting-metadata-issues-cp.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/troubleshooting-metadata-issues-cp.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/troubleshooting-metadata-issues-cp.md

# Metadata issues

Follow the suggestions in these topics to help resolve common issues with Pentaho metadata including the Pentaho Metadata Editor and the Pentaho User Console components which auto-generate metadata models:

* Managing multiple outer-joins
* Slow responses or inconsistent results in reports

## Managing multiple outer-joins

When you have three or more tables that require outer joins, the order in which the tables are joined is critical. Consider the example below:

![Joined database tables](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-8a0c918408aa0968c01e8cf44a0ceedb3e5cb864%2F48_outer_joins.png?alt=media)

In the sample Examine preview data below, the entries, 1, 2 ,3, and 4 listed under in TABLE4 are taken and outer-joined with the records in the two other tables. The three other tables contain fewer records. The relationships are defined, but now the order of execution is critical. Relationship A is executed first, followed by B, and then C.

![Examination of example table joins](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-3fddcb6e832b1ec4ae076a55c3085e1282d4f119%2F49_execution_of_joins.png?alt=media)

Below is the query that is generated:

![SQL code of resulting joins](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-00c4bbda21b5a979742596ff42bce4774c25198f%2F50_query_outer_joins.png?alt=media)

The nested join syntax that is generated forces the order of execution:

* Join TABLE1 and TABLE2 (shown in red)
* Join TABLE3 and A = B (shown in blue)
* Join TABLE4 with B = Result

Other orders of execution are just as valid depending on the business context to which they are applied. Another order of execution will generate a different result. To allow business model designers to ensure that user selections are executed in a specific way, a **Join Order Key** is added to the Relationship Properties dialog box.

![](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-b12cf69f17de62ca1f4170839885a556eb6e34eb%2F51_relationship_properties_dialog_box.png?alt=media)

The join order key is relevant only in instances in which outer joins are deployed in business models. To make the importance of the execution order apparent, this information is displayed in the graphical view of the model.

**Note:** It is not mandatory to use uppercase letters, (A, B, C, as shown in the first image), to set the order in which tables are executed. Any alphanumeric characters (0-9, A-Z) can be used. The system will calculate the ASCII values of each character; the values are then used to determine the order of execution. In the example, A, B, C, AA, AB, Pentaho Metadata Editor will execute the table relationships in the following order: A, AA, AB, B, C.

To force conditions that would ordinarily be processed in the `JOIN` condition to be processed in the `WHERE` clause, follow the directions below to create a **delay\_outer\_join\_conditions** custom property.

1. Right-click on a business model and select **Edit**.
2. Add a property by clicking the **green + icon**.
3. Select **Add a Custom Property** and set its ID to `delay_outer_join_conditions` and select **boolean** for the **Type**, then click **OK**.
4. Select the newly-created **delay\_outer\_join\_conditions** property, then click the checkbox for **delay\_outer\_join\_conditions** under the **Custom** heading on the right side of the window, then click **OK**.

Instead of the conditions being rolled into the `JOIN` clause, they will be allowed to roll down into the `WHERE` clause.

## Slow responses or inconsistent results in reports

Your reports may produce slow responses or generate inconsistent results. If a report contains inconsistent or incorrect results, and the SQL command contains several joins, make sure the join order has been specified for that report.

Beginning in version 5.0, inner joins are resolved before outer joins. If you have several tables that require outer joins, the order in which the tables are joined is critical because different join orders produce different results. To make the join order consistent, set the **Join Order Key** field in the Relationship Properties window. For more information, see: [Managing multiple outer-joins](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/broken-reference).
