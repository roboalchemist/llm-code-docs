# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/mondrian-role-mapping-in-the-pentaho-server.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/analysis-schema-security/mondrian-role-mapping-in-the-pentaho-server.md

# Mondrian role mapping in the Pentaho Server

The role mapper connects user role restrictions defined in a Mondrian schema to user roles defined in the Pentaho Server. This enables BI developers to set schema access controls in a single place, rather than in many places across different parts of Business Analytics. If you do not configure the role mapper, then none of the roles defined in your schema will restrict access in the Pentaho Server.

The role mapper is configured through the Pentaho Server in the `pentaho-solutions/system/pentahoObjects.spring.xml` file. There are three mapper implementations available, each with disabled example configurations in `pentahoObjects.spring.xml`.
