# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/table-input/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/switch-case/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/row-flattener/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-output/options-mongodb-output/mongo-document-fields-tab/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/execute-sql-script-cp/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/add-a-checksum/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/query-a-pentaho-data-service/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/table-input/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/switch-case/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/row-flattener/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-output/options-mongodb-output/mongo-document-fields-tab/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/execute-sql-script-cp/example.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/query-a-pentaho-data-service/example.md

# Example

The following example of a SQL query shows how to include a parameter. The example queries the **employeeList** data service for records, and when the data service transformation is executed, any use of the parameter **employeeRegion** in it will be substituted with the value *USA EAST*. This parameter can be in any transformation step that allows variable or parameter substitution.

You can also assign a value to the parameter in the Connection Properties window.

Using the following sample syntax:

```sql
SELECT * FROM '<*data service name*>' WHERE PARAMETER('<*parameter\_name*>') = '<*parameter\_value*>'
```

The following query would be used for our example:

```sql
view sourceprint
   SELECT * FROM '*employeeList*' WHERE PARAMETER('*employeeRegion*')='*USA EAST*'
```
