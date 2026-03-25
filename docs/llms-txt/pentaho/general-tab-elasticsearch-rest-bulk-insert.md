# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert/options-elasticsearch-rest-bulk-insert/general-tab-elasticsearch-rest-bulk-insert.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert/options-elasticsearch-rest-bulk-insert/general-tab-elasticsearch-rest-bulk-insert.md

# General tab

![Elasticsearch REST bulk insert step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-2bab1adcb5a43c2011c42ad5481a523ee8ebfc4f%2FPDI_Elasticsearch_REST_bulk_insert.png?alt=media)

Use the **General** tab set connections for the Elastic nodes and set options for the destination index.

Specify the **Connection** options for each server in the table of the **Servers** tab. The following table describes these connection options:

| Column      | Description                                                                                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **#**       | Number of the field’s entry.                                                                                                                                              |
| **Address** | Enter the hostname (optionally specified with a variable) of the node you want to connect to.                                                                             |
| **Port**    | Enter the port (optionally specified with a variable) of the Elastic REST interface.                                                                                      |
| **Scheme**  | Enter the scheme or protocol (optionally specified with a variable) to use when performing REST communication, which is usually http, or https for secured Elastic nodes. |

Set user verification options the **Authentication** tab to choose and test a verification method for the Elastic node user. The following table describes these user verification options:

| Field              | Description                                                                                                                                                                                                                                                                                                                                                             |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Authentication** | <p>Select the authentication method for the Elastic nodes:</p><ul><li><strong>None</strong></li></ul><p>Specify this method if you do not want to authenticate when connecting.</p><ul><li><strong>Basic</strong></li></ul><p>Specify the <strong>Username</strong> and <strong>Password</strong> to use basic authentication when connecting to the Elastic nodes.</p> |
| **Test**           | Click to test the connection and authentication settings.                                                                                                                                                                                                                                                                                                               |

Use the \*\*Index\*\* options to name and test the output Elastic index.

| Field      | Description                                                                                                                                                                                                          |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Index**  | Specify the name of the target index for the documents submitted by bulk insert requests. This value can be specified as a variable. If an index with that name does not yet exist in Elasticsearch, it creates one. |
| **Test**   | Click to test the connectivity to the desired output index.                                                                                                                                                          |
| **Create** | Click to create the index if it does not exist.                                                                                                                                                                      |
