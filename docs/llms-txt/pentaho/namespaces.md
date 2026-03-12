# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-input-cp-main-page/select-an-engine-hbase-input/using-hbase-input-step-on-the-pentaho-engine-cp/namespaces.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hbase-input-cp-main-page/namespaces.md

# Namespaces

You can use namespaces in the **HBase table name** field to create a logical grouping of your tables. For example, you can use one namespace for your development environment and another namespace for your production environment.

You must create a namespace before you can write to it. If you do not enter a namespace when creating a mapping, Pentaho uses the default namespace which is named `default`. See <https://hbase.apache.org/book.html#_namespace> for information on creating namespaces.

You can also use a variable for a namespace, which provides an easy way to move a transformation from your development environment to your production environment without having to change anything except the parameters. You can use transformation-level or system-level variables for a namespace.

The variable format is `${nsvarname}:`

**Note:** Every namespace has a `pentaho_mappings` table that stores the mappings metadata for the columns. This table is created automatically when you create mappings.
