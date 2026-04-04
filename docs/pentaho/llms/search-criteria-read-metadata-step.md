# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/read-metadata-pdi-step/options-read-metadata-step/search-criteria-read-metadata-step.md

# Search Criteria

Select **Search Criteria** if you know general information about the data resource. The search filters all the results by the criteria selected. Type a keyword in the **Keyword** field or select criteria from the drop-down menus, then click **ADD** to include it in the search.

**Note:** If missing or incomplete data is returned, use **Advanced Search** or change the default limit for returned results. See [Data Catalog searches returning incomplete or missing data](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/lumada-data-catalog-searches-returning-incomplete-or-missing-data) for information.

![Specify search criteria to find a data resource](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-b72f02da566488864cd21628f231d918a30c17d4%2Fpdi_read_catalog_metadata_search_criteria_tab.png?alt=media)

| Field               | Description                                                                                                                                                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Keyword**         | Enter a Data Catalog keyword to use for the search.                                                                                                                                                                                        |
| **Tags**            | Select a Data Catalog tag or tags that might be assigned to the data resource.                                                                                                                                                             |
| **Virtual Folders** | Select a Data Catalog virtual folder in which the data resource is or might be included.                                                                                                                                                   |
| **Data Sources**    | Select a Data Catalog data source that might be associated with the data resource.                                                                                                                                                         |
| **Resource Type**   | Select a resource type to search using the drop-down menu.                                                                                                                                                                                 |
| **Files Size**      | Select a file size range to search using the drop-down menu.                                                                                                                                                                               |
| **File Format**     | Select a specific file format to search for using the drop-down menu. The menu includes CSV and Parquet file formats to read the file format metadata within a transformation that includes a Catalog Input step or a Catalog Output step. |

If you have restricted access to a data resource or a specific data type, PDI notifies you.
