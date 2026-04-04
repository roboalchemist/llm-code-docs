# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-row-decoder-pdi/options-hbase-row-decoder-step/createedit-mappings-tab-hbase-row-decoder-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hbase-row-decoder-pdi/options-hbase-row-decoder-step/createedit-mappings-tab-hbase-row-decoder-step.md

# Create/Edit mappings tab

Most HBase data is stored as raw bytes. PDI uses mapping to decode values and execute meaningful comparisons for column-based result set filtering. Use the **Create/Edit mapping** tab to define metadata about the values that are stored in an HBase table.

Perform the following tasks before writing a value to HBase:

* Configure a connection by using the Hadoop cluster properties.
* Define which column family the value belongs to and its type.
* Specify type information about the key of the table.

![Create/Edit mappings tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-13367df96b6bf44bba6bc3eb91fc7a0940af6f34%2FPDI_HbaseRowDecoder_CreateEditMappings_DialogBox.png?alt=media)

Select the name of an existing mapping to load the fields defined in that mapping into the key field table. Alternatively, you can create a new HBase table and mapping simultaneously by configuring the fields of the mapping and naming the table in the **HBase table name** list.

This tab includes the following options:

| Option                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Hadoop Cluster**           | <p>Select an existing Hadoop cluster configuration from the drop-down box.</p><p>If you do not have an existing connection, click <strong>New</strong>. If you need to modify an existing connection, click <strong>Edit</strong>. See <a href="../../../advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article">Connect to a Hadoop cluster with the PDI client</a> for instructions.</p> |
| **HBase table name**         | Select the source HBase table name that has a defined mapping from the drop-down list of displayed names. Connection information must be valid and complete for this list to populate. Select a table to populate the **Mapping name** drop-down box with the names of available mappings for that table.                                                                                                                                        |
| **Get table names** (button) | Click to retrieve a list of all existing table names for the **HBase table name** field. The table names display the namespace, followed by a colon, then the table name. See [Namespaces](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hbase-input-cp-main-page/namespaces).                                                                                                |
| **Mapping name**             | Select the name of an existing map for the source table. The drop-down list is empty when no mappings are defined for the selected table. You can define multiple mappings on the same HBase table using different subsets of columns.                                                                                                                                                                                                           |
