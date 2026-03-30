# Source: https://docs.pentaho.com/pba-report-designer/connect-report-designer-to-a-data-source-cp/add-a-jndi-data-source-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/connect-report-designer-to-a-data-source-cp/add-a-jndi-data-source-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp/add-a-jndi-data-source-connecting-to-a-data-source-in-prd.md

# JNDI

You should already have established a JNDI data connection in your application server before continuing.

Follow this procedure to establish a connection to a JNDI data source.

1. Quit Report Designer if it is currently running.
2. Edit the `.pentaho/simple-jndi/default.properties` file.

   The `.pentaho` directory is in the home or user directory of the user account that runs Report Designer. If you have multiple copies of Report Designer installed to multiple user accounts, each `default.properties` file will have to be edited.
3. Add your JNDI connection information, beginning with the JNDI name on each line, as shown in the example below:

   ```
   SampleData/type=javax.sql.DataSource
   SampleData/driver=org.hsqldb.jdbcDriver
   SampleData/url=jdbc:hsqldb:hsql://localhost/sampledata
   SampleData/user=pentaho_user
   SampleData/password=password
   ```
4. Save and close the file, then start Report Designer.
5. To add this data source to a report, add a JDBC data source, choose **JNDI** as the connection type, and type in the JNDI name in the appropriate field.

Report Designer can now access your JNDI data sources.
