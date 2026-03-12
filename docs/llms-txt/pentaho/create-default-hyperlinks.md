# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/advanced-topics/defining-hyperlinks-cp/create-default-hyperlinks.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/defining-hyperlinks-cp/create-default-hyperlinks.md

# Create default hyperlinks

You can specify a default hyperlink for a dimension in a report, instead of going to each report containing that dimension and enabling the hyperlink functionality. Default hyperlinks are configured in the schema.

Perform the following steps to create default hyperlinks:

1. Open the Mondrian schema file in which you want to activate the hyperlink feature.

   **Note:** The Schema Workbench tool is recommended for editing schemas.

   ![Schema workbench](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-7b9fdfb5c5c8a566d3a39ed49cb2d8b02c06b14d%2FPAZ%20Schema%20workbench.png?alt=media)
2. In your chosen dimension, add a new annotation named `AnalyzerHyperlink`.
3. Insert the desired hyperlink for the selected dimension as the CDATA attribute.
4. Save your changes to the schema file.

**Note:** In this example an annotation was created on the `Customer` dimension, and the hyperlink associated with that dimension is `http://search.yahoo.com/search?p={Customer}` Dimension values are case sensitive, so the dynamic value needs to exactly match the dimension. In this example `customer` will not work.
