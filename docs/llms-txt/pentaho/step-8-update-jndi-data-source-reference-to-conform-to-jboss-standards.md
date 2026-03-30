# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/install-jdbc-driver-as-a-module-in-jboss/step-8-update-jndi-data-source-reference-to-conform-to-jboss-standards.md

# Step 8: Update JNDI data source reference to conform to JBoss standards

Update these files so that referenced JNDI datasources conform to JBoss standards.

1. Use a text editor to open the `pentaho/server/pentaho-server/pentaho-solutions/system/quartz/quartz.properties` file. Change the **org.quartz.dataSource.myDS.jndiURL** value to **jboss/datasources/Quartz**, then save and close the file.
2. Use a text editor to open the `pentaho/server/pentaho-server/pentaho-solutions/system/audit_sql.xml` file. Change the JNDI value to **jboss/datasources/Hibernate**, then save and close the file.
3. Use a text editor to open the `pentaho/server/pentaho-server/pentaho-solutions/system/data-access/settings.xml` file. Change the **data-access-staging-jndi** value to **jboss/datasources/Hibernate**, then save and close the file.
4. Open the `pentaho/server/pentaho-server/pentaho-solutions/system/audit/dialects/h2` directory, making sure to open the file from the correct folder.

   Use the text editor to open each file in the `H2` directory and make the following changes:

   * Change **\<database>Audit\</database>** to **\<database>jboss/datasources/Audit\</database>**.
   * Change **\<database>Hibernate\</database>** to **\<database>jboss/datasources/Hibernate\</database>**.
5. Navigate to the `server/pentaho-server/pentaho-solutions/system/hibernate` directory and open the `.hibernate.cfg.xml` file corresponding to your repository database with any text editor.

   For the default PostgreSQL database, the file is `postgresql.hibernate.cfg.xml`.
6. Revise the `<property name="hibernate.connection.datasource">java:comp/env/jdbc/Hibernate</property>` entry to the value `<property name=“hibernate.connection.datasource”>java:jboss/datasources/Hibernate</property>`.
7. Save and close the file.
