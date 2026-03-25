# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security.md

# Analysis schema security

You can restrict portions of your OLAP schema from being viewed by certain user roles defined within your schema definition, and then map those role restrictions to the Pentaho Server so that when you publish the schema, its security restrictions are obeyed in Analyzer and Dashboard Designer (or any other Pentaho Server-based dashboard). If you do this, only the permissible parts of the schema will be available to the specified roles. Pentaho offers several unique paths to accomplish role-based security, all of which are explained later in this section.

Refer to the subsections below that apply to your situation.

**Note:** Changes to a OLAP schema should be done with Schema Workbench. If you change a schema, you must republish it to the Pentaho Server in order for the modifications to take effect. Changes to XML configuration files (such as those that contain core Pentaho Server and Mondrian engine settings or properties) can be done with any text editor.

* [Restrict Access to Specific Members](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/restrict-access-to-specific-members)
* [Mondrian Role Mapping in the Pentaho Server](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/mondrian-role-mapping-in-the-pentaho-server)
