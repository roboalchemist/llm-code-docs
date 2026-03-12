# Source: https://docs.pentaho.com/pdia-admin/administer/troubleshoot-the-pentaho-system/legacy-troubleshooting-pages/archived-content/fixing-jtds-varchar-max-limitations-in-mssql-2005.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/general-issues/fixing-jtds-varchar-max-limitations-in-mssql-2005.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/general-issues/fixing-jtds-varchar-max-limitations-in-mssql-2005.md

# Fixing JTDS varchar(Max) limitations in MSSQL 2005

Creating a report that uses a column of type varchar(MAX) may result in a `net.sourceforge.jtds.jdbc.ClobImpl@83cf00` error when using the JTDS SQL Server driver. This is caused by inherent limitations in older versions of the JTDS driver. Additionally, the SQL Server JDBC driver version 1.2.2828 also has issues accessing a varchar(MAX) column.

The solution is to upgrade the MSSQL 2005 JDBC driver to version 1.0.809.102 or later. Download and install the <http://msdn.microsoft.com/en-us/sqlserver/aa937724> file from Microsoft.com, then restart your MSSQL server.
