# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/install-jdbc-driver-as-a-module-in-jboss/step-4-define-jndi-database-connection-information-in-jboss.md

# Step 4: Define JNDI database connection information in JBoss

JNDI is used to specify port, driver, user name, and password information for the Audit and Quartz databases that are housed on your Pentaho Repository database.

This section shows you how to define your JNDI database connection information.

**CAUTION:**

If you have a different database than PostgreSQL, or if you are using a different port, password, user, driver class information, or IP address, make sure that you adjust the examples in this section to match the ones in your environment.

1. Navigate to the `pentaho/server/pentaho-server/*&lt;your jboss installation directory&gt;*/standalone/configuration` directory and open the `standalone.xml` file with any text editor.
2. Insert these lines after the definition for **ExampleDS** data source.

   ```xml
   <datasource jndi-name="java:jboss/datasources/Hibernate" pool-name="hibpool" enabled="true" jta="true" use-java-context="true" use-ccm="true">
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
       <datasource jndi-name="java:jboss/datasources/PDI_Operations_Mart" pool-name="PDI_Operations_Mart" enabled="true" jta="true" use-java-context="true" use-ccm="true">
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
       <datasource jndi-name="java:jboss/datasources/Jackrabbit" pool-name="jcr_pool" enabled="true" jta="true" use-java-context="true" use-ccm="true">
            <connection-url>jdbc:postgresql://localhost:5432/jackrabbit</connection-url>
   	     <driver-class>org.postgresql.Driver</driver-class>
   	     <driver>org.postgresql</driver>
   	     <pool>
   	         <prefill>false</prefill>
   	         <use-strict-min>false</use-strict-min>
   	         <flush-strategy>FailingConnectionOnly</flush-strategy>
   	     </pool>
   	     <security>
   	         <user-name>jcr_user</user-name>
   	         <password>password</password>
   	     </security>
   </datasource>
   ```
3. Add the driver definition in the driver section of the file.

   Here is an example of the PostgreSQL driver definition. If you are using another database, modify the driver name, module, and data source class accordingly.

   ```xml
   <driver name="org.postgresql" module="org.postgresql"> 
   <xa-datasource-class>org.postgresql.xa.PGXADataSource</xa-datasource-class> 
   </driver> 
   <driver name="org.hsqldb" module="org.hsqldb"> 
   <driver-class>org.hsqldb.jdbcDriver</driver-class> 
   </driver>

   ```
4. Save and close the `standalone.xml` file.
