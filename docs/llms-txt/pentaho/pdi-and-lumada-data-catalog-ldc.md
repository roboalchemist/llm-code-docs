# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pdi-and-lumada-data-catalog-ldc.md

# PDI and Data Catalog

If you are a Pentaho Data Catalog user, you can now work with your Data Catalog metadata and data resources using PDI transformations.

[Pentaho Data Catalog](https://www.hitachivantara.com/en-us/products/data-management-analytics/lumada-data-services/lumada-data-catalog.html) lets data engineers, data scientists, and business users accelerate metadata discovery and data categorization, and permits data stewards to manage sensitive data. Data Catalog collects metadata for various types of data assets and points to the asset's location in storage. Data assets registered in Data Catalog are known as data resources.

For example, you might create a PDI transformation that reads the location of a data resource from Data Catalog, retrieves the data and transforms it, and then writes a data file back to the cluster as a new or existing file. You can then register that file’s location in Data Catalog as a new data resource along with descriptive metadata tags to describe the transformed contents of the file.

There are four PDI steps for building PDI transformations that work with Data Catalog metadata and data resources:

* [**Read Metadata**](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/read-metadata-pdi-step)

  This step provides a way to search Data Catalog’s existing metadata for specific data resources, including their storage location. The metadata associated with an identified data resource can then be passed along to another step within a PDI transformation.
* [**Write Metadata**](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/write-metadata)

  With this step, you can revise the existing Data Catalog tags associated with an existing data resource. In a transformation that includes the Catalog Output step, you can also create the metadata for a new data resource that you created and registered in Data Catalog.
* [**Catalog Input**](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/catalog-input)

  This step reads the CSV text file types or Parquet data formats of a Data Catalog data resource that is stored in a Hadoop or S3 ecosystem and outputs the data payload in the form of rows to use in a transformation. You can also use Catalog Input with the [Catalog Output](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/catalog-output) step to gather data from Data Catalog data resources and move that data into Hadoop or S3 storage.
* [**Catalog Output**](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/catalog-output)

  This step encodes CSV text file types or Parquet data formats using the schema defined in PDI to create a new data resource or to replace or update an existing data resource in Data Catalog. Metadata can be added. The data is saved in the selected Hadoop or S3 ecosystem and registered as a data resource in Data Catalog.

All four steps support the Pentaho engine. Neither the Pentaho Adaptive Execution Layer (AEL) nor metadata injection (MDI) are currently supported in the steps.
