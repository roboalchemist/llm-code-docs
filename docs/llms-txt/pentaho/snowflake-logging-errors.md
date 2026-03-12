# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/security-issues/snowflake-logging-errors.md

# Snowflake logging errors

Snowflake users see the warning message `WARNING: Connect strings must start with jdbc:snowflake://` while connecting to Snowflake.

Pentaho 9.5 upgraded the Snowflake JDBC driver version to 3.13.29 to address security concerns.

To resolve this warning message, download the Snowflake JDBC driver version 3.13.30 from <https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/3.13.30/snowflake-jdbc-3.13.30.jar> and replace the jar in the server: `pentaho-server/tomcat/webapps/pentaho/WEB-INF/lib/` directory.
