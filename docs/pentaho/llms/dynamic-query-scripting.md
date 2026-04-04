# Source: https://docs.pentaho.com/pba-report-designer/create-queries-report-designer-cp/dynamic-query-scripting.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-queries-report-designer-cp/dynamic-query-scripting.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/dynamic-query-scripting.md

# Dynamic query scripting

For all JDBC, Metadata, and OLAP data sources, you can create a dynamic query through a Groovy or JavaScript script.

The two following scripting extensions are available in Report Designer:

* **Global**

  used to define shared functions or global variables that are available to all query scripts, and to dynamically change the data source configuration via the `init()` function.
* **Per-Query**

  used to customize a query string, calculate the "additional fields" information for query-caching, and post-process the returned table model.

A template for the two scripting languages is supported by default (JavaScript and Groovy). The template contains some guidance and instructions, as well as empty declarations for the functions to call. You can safely delete any function you do not need. If deleted, Report Designer ignores them. You can also load scripts from external sources, but you must ensure that they are available to the report at runtime.

**CAUTION:**

Since most production environments separate the server from the design tools, an external script that is local to Report Designer will probably not be local to the Pentaho Server. If you publish a report to the server, you must either change the path to the external script so that it will work on the server, or find a way to include it in the correct relative path on the Pentaho Server.

**Note:** The scripting backend uses the JSR-223 (javax.script) scripting system. By default, Pentaho only ships with JavaScript and Groovy support. Many more JSR-223 enabled languages are not included but will work in Report Designer. To add support for other languages, you must add the appropriate JAR to both the Pentaho Server and the Pentaho Report Designer classpaths. Despite this capability, Pentaho's support and services contracts do not cover any extra scripting language JARs.
