# Source: https://docs.pentaho.com/pdia-admin/administer/troubleshoot-the-pentaho-system/legacy-troubleshooting-pages/archived-content/jdbc-driver-issues.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/general-issues/jdbc-driver-issues.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/general-issues/jdbc-driver-issues.md

# JDBC driver issues

Before you begin troubleshooting suspected JDBC driver issues, make sure that the correct JDBC driver JARs are installed in the correct locations. You could install your drivers with our JDBC Distribution Tool to ensure they are placed in the correct locations. Also, make sure there are no conflicting driver versions installed. Confirm with your database or driver vendor if you suspect you have JDBC driver compatibility issues. See the **Install Pentaho Data Integration and Analytics** document for details.

The Pentaho Server needs the appropriate driver to connect to the database that stores your data. You can download drivers from your database vendor's website. Check the **JDBC drivers reference** in the Try Pentaho Data Integration and Analytics document for a list of supported drivers and links to vendor websites.

Perform the following steps to install the appropriate driver for your Pentaho Server:

1. Stop the Pentaho Server.
2. Copy your driver into this location: `<pentaho-install-directory>/server/pentaho-server/tomcat/lib`.
3. Start the Pentaho Server.
