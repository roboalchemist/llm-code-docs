# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server/install-jdbc-driver-as-a-module-in-jboss/define-jndi-database-connection-information-in-jboss.md

# Define JNDI database connection information in JBoss

JNDI is used to specify port, driver, user name, and password information for the Audit and Quartz databases that are housed on your Pentaho Repository database. This section shows you how to define your JNDI database connection information.

**Note:** If you have a different database than PostgreSQL, or if you are using a different port, password, user, driver class information, or IP address, make sure that you adjust the examples in this section to match the ones in your environment.

1. Copy the `pentaho-style.war` and `pentaho.war` files into the `pentaho/server/pentaho-server/*your jboss installation directory*/standalone/deployment` directory, or verify that the files are already there, as in PostgreSQL.
2. Locate the `pentaho/server/pentaho-server/<your jboss installation directory>/standalone/configuration/standalone.xml` file and open it with a text editor.
3. Insert these lines after the definition for `ExampleDS` data source.

   ```xml
   <datasource jndi-name="java:jboss/datasources/Hibernate" pool-name="hibpool"enabled="true" jta="true" use-java-context="true" use-ccm="true">
                           <connection-url>
                               jdbc:postgresql://localhost:5432/hibernate
                           </connection-url>
                           <driver-class>
                               org.postgresql.Driver
                           </driver-class>
                           <driver>
                               org.postgresql
                           </driver>
                           <pool>
                               <prefill>
                                   false
                               </prefill>
                               <use-strict-min>
                                   false
                               </use-strict-min>
                               <flush-strategy>
                                   FailingConnectionOnly
                               </flush-strategy>
                           </pool>
                           <security>
                               <user-name>
                                   hibuser
                               </user-name>
                               <password>
                                   password
                               </password>
                           </security>
                       </datasource>
                       <datasource jndi-name="java:jboss/datasources/Quartz" pool-name="quartzpool" enabled="true" jta="true" use-java-context="true" use-ccm="true">
                           <connection-url>
                               jdbc:postgresql://localhost:5432/quartz
                           </connection-url>
                           <driver-class>
                               org.postgresql.Driver
                           </driver-class>
                           <driver>
                               org.postgresql
                           </driver>
                           <pool>
                               <prefill>
                                   false
                               </prefill>
                               <use-strict-min>
                                   false
                               </use-strict-min>
                               <flush-strategy>
                                   FailingConnectionOnly
                               </flush-strategy>
                           </pool>
                           <security>
                               <user-name>
                                   pentaho_user
                               </user-name>
                               <password>
                                   password
                               </password>
                           </security>
                       </datasource>
                       <datasource jndi-name="java:jboss/datasources/Audit" pool-name="auditpool" enabled="true" jta="true" use-java-context="true" use-ccm="true">
                           <connection-url>
                               jdbc:postgresql://localhost:5432/hibernate
                           </connection-url>
                           <driver-class>
                               org.postgresql.Driver
                           </driver-class>
                           <driver>
                               org.postgresql
                           </driver>
                           <pool>
                               <prefill>
                                   false
                               </prefill>
                               <use-strict-min>
                                   false
                               </use-strict-min>
                               <flush-strategy>
                                   FailingConnectionOnly
                               </flush-strategy>
                           </pool>
                           <security>
                               <user-name>
                                   pentaho_user
                               </user-name>
                               <password>
                                   password
                               </password>
                           </security>
                       </datasource>
                   
                       <datasource jndi-name="java:jboss/datasources/pentaho_operations_mart" pool-name="pentahooperationsmartpool" enabled="true" jta="true" use-java-context="true" use-ccm="true">
                            <connection-url>
                                jdbc:postgresql://localhost:5432/hibernate
                            </connection-url>
                            <driver-class>
                           org.postgresql.Driver
                            </driver-class>
                            <driver>
                                org.postgresql
                            </driver>
                            <pool>
                              <prefill>
                               false
                              </prefill>
                           <use-strict-min>
                               false
                           </use-strict-min>
                           <flush-strategy>
                               FailingConnectionOnly
                           </flush-strategy>
                       </pool>
                       <security>
                           <user-name>
                               hibuser
                           </user-name>
                           <password>
                               password
                           </password>
                       </security>
                   </datasource>
                       <datasource jndi-name="java:jboss/datasources/PDI_Operations_Mart"pool-name="PDI_Operations_Mart" enabled="true" jta="true" use-java-context="true" use-ccm="true">
                            <connection-url>
                                 jdbc:postgresql://localhost:5432/hibernate
                            </connection-url>
                            <driver-class>
                            org.postgresql.Driver
                            </driver-class>
                            <driver>
                                 org.postgresql
                            </driver>
                            <pool>
                                <prefill>false</prefill>
                                <use-strict-min>false</use-strict-min>
                                <flush-strategy>FailingConnectionOnly</flush-strategy>
                            </pool>
                            <security>
                                <user-name>hibuser</user-name>
                                <password>password</password>
                            </security>
                   </datasource>
   ```
4. Add the driver definition in the driver section of the file. Here is an example of the PostgreSQL driver definition. If you are using another database, modify the driver name, module, and data source class accordingly.

   ```xml
   <driver name="org.postgresql" module="org.postgresql">
   <xa-datasource-class>org.postgresql.xa.PGXADataSource</xa-datasource-class>
   </driver>
   <driver name="org.hsqldb" module="org.hsqldb">
   <driver-class>org.hsqldb.jdbcDriver</driver-class>
   </driver>
   ```
5. Save and close the `standalone.xml` file.
