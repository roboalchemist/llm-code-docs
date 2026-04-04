# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/change-the-location-of-the-server-log-file.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-location-of-the-server-log-file.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-location-of-the-server-log-file.md

# Change the location of the server log file

## Windows server log file location

To change the location of the `pentaho.log` file, edit `log4j2.xml` in `/pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes/`.

Modify the location as shown in the following sample, using the appropriate path to your installation:

```xml
<RollingFile name="PENTAHOFILE" fileName="../logs/pentaho.log" filePattern="../logs/pentaho.log.%d{yyyy-MM-dd}">
```

## Linux server log file location

If you are using Linux, the `log4j2.xml` file is in `/pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes/`.

Modify the location as shown in the following sample, using the appropriate path to your installation:

```xml
<RollingFile name="PENTAHOFILE" fileName="../logs/pentaho.log" filePattern="../logs/pentaho.log.%d{yyyy-MM-dd}">
```
