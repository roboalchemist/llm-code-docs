# Source: https://docs.pentaho.com/pba-report-designer/connect-report-designer-to-a-data-source-cp/other-data-sources-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/connect-report-designer-to-a-data-source-cp/other-data-sources-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp/other-data-sources-connecting-to-a-data-source-in-prd.md

# Other Data Sources

The following data sources require additional knowledge and skills:

* **JDBC Custom**

  This is much like a standard JDBC connection, except you create a formula-based query through the Master Report's Attributes pane instead. See the [Query attribute reference](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/attributes-reference-cp-prd/query-prd-attributes) for more information.
* **Scriptable**

  Select your language, then add a query by clicking the round green **+** button, give your query a name, then type in your script in the **Query** field.
* **External**

  This data source is used when a report (`.prpt` - simple reporting component) is used in an .xaction. In the report, you must specify the result-set name for the `query name` attribute on the report. Also, you must add a **report** parameter using the same name as the **result-set** name and set the parameter to the **tablemodel** parameter type. The `.xaction` **result-set** can be MQL, SQL, MDX or JavaScript.

```
org.pentaho.reporting.engine.classic.core.modules.misc.datafactory.​StaticDataFactorySample#createSubQuery(${Var1})
```
