# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server/install-jdbc-driver-as-a-module-in-jboss/update-jndi-data-source-references-to-conform-to-jboss-standards.md

# Update JNDI data source references to conform to JBoss standards

Update these files so that referenced JNDI datasources conform to JBoss standards.

1. Use a text editor to open the `pentaho/server/pentaho-server/pentaho-solutions/system/quartz/quartz.properties` file. Change the `org.quartz.dataSource.myDS.jndiURL` value to `jboss/datasources/Quartz`, then save and close the file.
2. Use a text editor to open the `pentaho/server/pentaho-server/pentaho-solutions/system/audit_sql.xml` file. Change the JNDI value to `jboss/datasources/Hibernate`, then save and close the file.
3. Use a text editor to open the `pentaho/server/pentaho-server/pentaho-solutions/system/data-access/settings.xml` file. Change the `data-access-staging-jndi` value to `jboss/datasources/Hibernate`, then save and close the file.
4. Open the `pentaho/server/pentaho-server/pentaho-solutions/system/audit/dialects/h2` directory.

   Make sure you open the file from the correct folder.
5. Use the text editor to open each file in the H2 directory and make the following changes:
   1. Change `<database>Audit</database>` to `<database>jboss/datasources/Audit</database>`.
   2. Change `<database>Hibernate</database>` to `<database>jboss/datasources/Hibernate</database>`.
