# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/read-metadata-pdi-step/options-read-metadata-step/specific-resources-read-metadata-step.md

# Specific Resources

Select **Specific Resources** if you know the unique identification key that Data Catalog assigned to a data resource.

![Search for specific resources](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-1f88b82f42e2278e629c88c167feda55a922246a%2Fpdi_read_catalog_metadata_specific_resources_tab.png?alt=media)

Type the identification key into the **ID** field and click **Add**. The data resource must be profiled in Data Catalog to be available.

The metadata for each ID you add populates the **Selected Files** table. The metadata may include some or all the following metadata types:

| Field               | Description                                                                                                                                                                   |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Resource Name**   | Displays the name of the resource in Data Catalog.                                                                                                                            |
| **ID**              | Displays the Data Catalog resource identification key.                                                                                                                        |
| **Resource Type**   | Displays the type of the data type associated with the resource in Data Catalog.                                                                                              |
| **Origin**          | Displays the origin of the resource in Data Catalog, related to its linage or its point of origin in the cluster.                                                             |
| **Delete** (button) | Delete a line item from the **Selected Files** table by clicking the line item, then click **Delete**.                                                                        |
| **Edit** (button)   | Select a line item to edit in the **Selected Files** table by clicking the line item, then click **Edit**. The **ID** is inserted into the ID field, where you can modify it. |

If you have restricted access to a data resource or a specific data type, PDI notifies you.
