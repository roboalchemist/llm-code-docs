# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/cassandra-output/options-cassandra-output/write-options-tab/pre-insert-cql.md

# Pre-Insert CQL

You have the option of executing an arbitrary set of CQL statements prior to inserting the first incoming PDI row. It is useful for creating or dropping secondary indexes on columns. Clicking **CQL to execute before inserting first row** opens a CQL editor. You can enter multiple CQL statements as long as each is terminated by a semicolon, as shown in the following example:

![Cassandra Output CQL Pre-Insert dialog](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-6cab8b576a29fe3b2dc5b73d900d7f48c21e7576%2FPDI_TransStep_Cassandra_Output_CQL_Insert_dialog.png?alt=media)

Pre-insert CQL statements are executed after any table metadata updates for new incoming fields, and before the first row is inserted. This allows for indexes to be created for columns corresponding new incoming fields.
