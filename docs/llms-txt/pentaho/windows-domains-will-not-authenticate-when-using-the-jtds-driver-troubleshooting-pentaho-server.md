# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/pentaho-server-issues/windows-domains-will-not-authenticate-when-using-the-jtds-driver-troubleshooting-pentaho-server.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-server-issues/windows-domains-will-not-authenticate-when-using-the-jtds-driver-troubleshooting-pentaho-server.md

# Windows domains will not authenticate when using the JTDS driver

If you are using a JTDS JDBC driver and you want to use a Windows domain user to authenticate to a Microsoft SQL Server, the Windows syntax will not work for specifying the domain and user.

The domain must be appended to the end of the URL with a semicolon, as shown in the following example:

```
jdbc:jtds:sqlserver://svn-devel.example.com:1533/reportsInProgress;domain=testdomain
```
