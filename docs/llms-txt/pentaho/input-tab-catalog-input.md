# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/catalog-input/general-catalog-input/input-tab-catalog-input.md

# Input tab

Use the **Input** tab to specify the search method used to find the metadata about the payload to read from Data Catalog. Searches are performed on the schema of a supported format type according to the selected method.

![Input tab](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-3e1e0c1333d2598023634542522b93384fc8769e%2FPDI_CatalogInput_Input.png?alt=media)

Select **Specific Resources** if you know the key value of the data resource.

![Specific Resources method](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-12b7d9ad4346a99c4d701a4a0b0c96d63ec7408e%2FPDI_CatalogInput_Input_SpecificResources.png?alt=media)

| Field               | Description                                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| **ID**              | Enter the Data Catalog resource identifier. The resource must be profiled in Data Catalog to be available. |
| **Add** (button)    | Click to retrieve the profiled data associated with the **Resource ID** in Data Catalog.                   |
| **Delete** (button) | Removes a selected resource from the **Selected Files** table.                                             |
| **Edit** (button)   | Allows you to edit a selected resource from the **Selected Files** table.                                  |

Results of the search are displayed in the **Selected Files** table, which provides details about the resources that were found. You can use the **Edit** button to modify a resource detail or **Delete** to remove a resource from the search.

| Column            | Description                                                                      |
| ----------------- | -------------------------------------------------------------------------------- |
| **Resource Name** | Displays the name of the resource in Data Catalog.                               |
| **ID**            | Displays the Data Catalog resource identifier.                                   |
| **Resource Type** | Displays the type of the data type associated with the resource in Data Catalog. |
| **Origin**        | Displays the origin of the resource in Data Catalog.                             |

Select **Search Criteria** if you know general information about the resource. The search filters all the results by the criteria selected. Enter a keyword in the **Keyword** field or select criteria from a drop-down menu, then click **ADD** to include it in the search.

![Search Criteria method](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-6d7d209acf03501d32a1aed83bb4fe904de8ebeb%2FPDI_CatalogInput_Input_SearchCriteria.png?alt=media)

| Field               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Keyword**         | Enter a keyword to use for the search.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Tags**            | Select a tag or tags to search for using the drop-down menu.                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Virtual Folders** | Select a virtual folder to search using the drop-down menu.**Note:** If missing or incomplete data is returned, you can use **Advanced Search** or you may need to change the default limit for returned results. See [Data Catalog searches returning incomplete or missing data](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/lumada-data-catalog-searches-returning-incomplete-or-missing-data) for information. |
| **Data Sources**    | Select a data source to search using the drop-down menu.**Note:** If missing or incomplete data is returned, you can use **Advanced Search** or you may need to change the default limit for returned results. See [Data Catalog searches returning incomplete or missing data](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/lumada-data-catalog-searches-returning-incomplete-or-missing-data) for information.    |
| **Resource Type**   | Select a resource type to search using the drop-down menu.**Note:** If missing or incomplete data is returned, you can use **Advanced Search** or you may need to change the default limit for returned results. See [Data Catalog searches returning incomplete or missing data](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/lumada-data-catalog-searches-returning-incomplete-or-missing-data) for information.  |
| **Files Size**      | Select a file size range to search using the drop-down menu.                                                                                                                                                                                                                                                                                                                                                                                                       |
| **File Format**     | Select a specific file format to search for using the drop-down menu. Note that CSV or Parquet file formats are currently supported.                                                                                                                                                                                                                                                                                                                               |

Select \*\*Advanced Search\*\* to search using a JSON string. For more information, see \[Lumada Data Catalog REST API]\(<https://docs2019.waterlinedata.com/latest/apidocs/index.html>). The search filters all the results by the query parameters.

![Advanced Search method](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-fadc29a69e05d9ad4f249fd5a4d69cf28c571c77%2FPDI_CatalogInput_Input_AdvancedSearch.png?alt=media)

| Field               | Description                                                                       |
| ------------------- | --------------------------------------------------------------------------------- |
| **Advanced Search** | Enter a JSON string of API-specific query parameters to run against Data Catalog. |
