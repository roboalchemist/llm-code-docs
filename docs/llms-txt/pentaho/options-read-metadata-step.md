# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/read-metadata-pdi-step/options-read-metadata-step.md

# Options

Use the Read Metadata step to search for data resources and associated metadata from the search criteria you specify. You can search for Data Catalog data resources in multiple ways:

* **Specific Resources**

  Searches Data Catalog using the unique resource ID that is associated with a data resource.
* **Search Criteria**

  Narrows Data Catalog searches for specific data resources using criteria that you select from lists of the existing metadata available in your instance of Data Catalog.
* **Advanced Search**

  Creates a JSON script that finds the Data Catalog tags for specific data resources. For more information, see the [Lumada Data Catalog REST API](https://docs2019.waterlinedata.com/2019.3/apidocs/).

**Note:** In some cases, if missing or incomplete search data is returned, you may need to change the default limit for returned results. See [Data Catalog searches returning incomplete or missing data](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/lumada-data-catalog-searches-returning-incomplete-or-missing-data) for information.
