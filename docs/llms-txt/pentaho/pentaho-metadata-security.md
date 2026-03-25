# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/multi-tenancy/pentaho-metadata-security.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/multi-tenancy/pentaho-metadata-security.md

# Pentaho metadata security

The easiest way to implement multi-tenancy is to use a global security constraint in the data model. The advantage to this approach is that there is no code to maintain, making it simple for non-developers to implement. However, there are several disadvantages to this approach, such as that complex constraints can be difficult to model and not all constraints can be modeled. This approach also applies to all queries which may result in unnecessary joins. Finally, each model has to be constrained, whereas the SQL Generator can be applied to all models with one piece of code.

## Set the global constraint

To set the global constraint:

1. Edit the data model.
2. Set a constraint on the business model to be constrained using available formulas.

   ```javascript
   [BT_EMPLOYEES_EMPLOYEES].[BC_EMPLOYEES_OFFICECODE]="SESSION("officeCode")"
   ```

   See the **Pentaho Metadata Editor** document for details.
3. Repeat for all tables and models as necessary.

See **Edit the properties file for Metadata Editor** in the **Install Pentaho Data Integration and Analytics** document for more information on setting Pentaho metadata security.

## SQL generator

The SQL Generator is a special class that is called when Pentaho metadata queries the database. There are two methods that can be overwritten: `preprocessQueryModel()` and `processGeneratedSql()`.

* **`preprocessQueryModel()`**

  The recommended method to overwrite. It is called before the SQL is generated. To overwrite, add an `AND` condition to the query to restrict data.
* **`processGeneratedSql()`**

  The method called after the SQL is generated. While it is possible to modify this query, it would involve parsing and modifying the string query.

The following example shows the `preprocessQueryModel()` for a class that extends the `SqlGenerator` class. The first loop gathers all of the columns to see which ones need to be constrained to avoid duplicate checks. The second loop adds a `WHERE` clause to the query. Only `AND` conditions can be used. Because you cannot add parentheses, using `AND` conditions can cause problems if the model already has an `OR` condition in the `WHERE` clause.

```java
@Override
protected void preprocessQueryModel(SQLQueryModel query, List<Selection> selections, Map<LogicalTable, String> tableAliases, DatabaseMeta databaseMeta) {
    Set<LogicalTable> selectedLogicalTables = new HashSet<LogicalTable>();
    // Get the users productline from the session
    IPentahoSession session = PentahoSessionHolder.getSession();
    String productline = (String)session.getAttribute("productline");
    //Object territory = "NA" ;
    // Figure out and gather up the selected logical tables. We need to
    // know if the CUSTOMER_W_TER table is included in the
    // query...
    if(selections!=null && !selections.isEmpty()) {
        for(Selection selection:selections) {
            LogicalColumn column = selection.getLogicalColumn();
            LogicalTable table = column.getLogicalTable();
            selectedLogicalTables.add(table);
        }
    }
    // We now find the column to constrain, and add our where
    // clause, using a dialect specific where clause...
    for(LogicalTable table:selectedLogicalTables) {
        List<LogicalColumn> logicalColumns=table.getLogicalColumns();
        for(LogicalColumn logicalColumn:logicalColumns) {
            if(logicalColumn.getId().equalsIgnoreCase("BC_PRODUCTS_PRODUCTLINE")) {
                String tableAlias = tableAliases.get(table);
                String columnName = (String) logicalColumn.getPhysicalColumn().
                getProperty("target_column");
                query.addWhereFormula(tableAlias + "." +
                columnName + " = '" + productline + "', AND");
            }
        }
    }
}
```

Once the code has been compiled and placed in a JAR file, it should be deployed to `webapps/pentaho/WEB-INF/lib`. Then two files need to be modified:

* **`pentaho-solutions/system/pentahoObjects.spring.xml`**

  should be modified to change the class defined for the `sqlGenerator` bean. The following shows an example of the bean mapping:

  ```xml
  <bean id="sqlGenerator" class="org.myorganization.MySqlGenerator" scope="prototype"/>
  ```
* **`webapps/pentaho/WEB-INF/classes/classic-engine.properties`**

  should be modified by defining a new parameter:

  ```java
  org.pentaho.reporting.engine.classic.extensions.datasources.pmd.SqlGeneratorClass=org.myorganization.MySqlGenerator
  ```

One way to debug `SQLGenerator` functionality is to view the generated SQL statements. A common method is to use logging statements within `processGeneratedSql` and increase the log level of `SQLGenerator` in `log4j.xml` file under `webapps/pentaho/WEB-INF/classes`.

```xml
<category name="org.pentaho.metadata.query.impl.sql.SqlGenerator">
    <priority value="DEBUG"/>
  </category>
  <category name="org.myorganization.MySqlGenerator">
    <priority value="DEBUG"/>
  </category>
```

#### Reference

SQLGenerator JavaDoc: <https://github.com/pentaho/pentaho-metadata/blob/10.2.0.0-218/src/main/java/org/pentaho/metadata/query/impl/sql/SqlGenerator.java>
