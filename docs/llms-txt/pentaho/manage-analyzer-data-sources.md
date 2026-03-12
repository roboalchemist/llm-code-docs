# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/configure-mondrian-engine/manage-analyzer-data-sources.md

# Manage Analyzer data sources

In order to use a properly prepared data source with Pentaho Analyzer, it must be established in either the User Console as a Native (JDBC) data source, or in your Web application server as a JNDI data source.

Whichever method you choose, you will have to know the name of the data source later on when you are asked to supply it in the Pentaho Schema Workbench. See the **Pentaho Schema Workbench** document for details.

**Note:** Schema Workbench can only work with one data source for each Mondrian schema; this is a structural limitation in the software that will be remedied at a later time. You can have multiple JNDI or Native (JDBC) data sources established, but only one at a time can be used with Schema Workbench.
