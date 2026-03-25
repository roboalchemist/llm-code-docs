# Source: https://docs.pentaho.com/pdia-admin/administer/troubleshoot-the-pentaho-system/legacy-troubleshooting-pages/archived-content/data-conversion-issues-with-mysql-driver-5.0.8.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/general-issues/data-conversion-issues-with-mysql-driver-5.0.8.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/general-issues/data-conversion-issues-with-mysql-driver-5.0.8.md

# Data conversion issues with MySQL driver 5.0.8

The MySQL JDBC driver version 5.0.8 may cause data conversion errors in the Pentaho Server. For example, SQL statements that convert a numeric field to a string are returned as a string in version 5.0.7, but return as a byte array in version 5.0.8.

To solve this problem, you must replace the `mysql-connector-java-5.0.8.jar` with the `mysql-connector-java-5.0.7.jar` in your client tool or application server's `lib` folder
