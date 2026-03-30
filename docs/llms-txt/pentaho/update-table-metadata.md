# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/cassandra-output/options-cassandra-output/write-options-tab/update-table-metadata.md

# Update table metadata

Selecting the **Update table meta data** option will result in the table metadata getting updated with information on incoming fields not already present. If this option is not selected, any unknown incoming fields are ignored unless **Insert fields not in column meta data** is selected. If the latter is selected, then any incoming fields that are not present in the table metadata will be inserted with respect to the default table validator. This option has no effect if **Update table meta data** is selected.

**Note:** Cassandra Output does not check the types of incoming columns against matching columns in the Cassandra metadata. Incoming values are formatted into appropriate string values for use in a textual CQL `INSERT` statement according to PDI's field meta data. If resulting values cannot be parsed by the Cassandra column validator for a particular column, then an error will occur.
