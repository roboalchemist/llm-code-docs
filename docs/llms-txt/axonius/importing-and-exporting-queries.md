# Source: https://docs.axonius.com/docs/importing-and-exporting-queries.md

# Importing and Exporting Queries

You can import and export queries and their folder format to and from Axonius.  Queries are exported from Axonius in JSON file format. Exported queries can be imported. This makes it easy to move queries from one Axonius environment to another.

When you export a query this includes the folder structure in which it is located.  Queries with access permissions of **Public**, **Private** or **All Data Scopes** can be imported and exported. However, private queries become public queries  and they are imported together with their folder structure to the Public Queries folder.

* Note that you can only import queries that were exported using this Export Query functionality (not exported using API). Queries that were exported using this button can't be imported using the API.
* Roles that are unrestricted and have the following permissions can import and export queries:
  * Export Queries

  * Import Queries

  * Add or edit query

  * Add or edit for all data scopes

For more information about Data Scopes, see [Data Scope Management](/docs/data-scope-management).

## Exporting Queries

**To export  Queries**

1. Select one or more queries, and from the action menu choose **Export Queries**. To export the complete query table, choose Select All and from the action menu choose **Export Queries**. Note that you can't export pre-defined queries (even if selected they are not exported). You can only export queries that you are authorized to see.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExportMenu.png)

2. The queries are downloaded to your local computer as a JSON file.

## Importing Queries

**To import Queries**

1. From the right side, above the **Query** Table Select **Import**. A browse dialog opens.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ImportQueryButton.png)

2. Navigate to the location of the query JSON file and select it.

3. Click **Open**. The queries and their whole folder structure are imported to the query page. If the folder already exists, then the query is imported to the existing folder; if the folder does not exist, then the folder and all of its parent folders are created.
   * If a query of the same name already exists, the imported query overwrites it.
   * Note that when you import queries, their access is changed to 'Public' and they are granted the same data scopes that the importing user can access.
   * If a query was imported from a folder that was private, or defined for a specific data scope, they are then moved to the main Public folder.

<Callout icon="📘" theme="info">
  Notes

  * When a query is imported with the same name as an existing query, the existing query **will be overwritten**. Rename queries in advance if required to prevent this

  * The system imports the query and related queries if it uses other queries.
</Callout>