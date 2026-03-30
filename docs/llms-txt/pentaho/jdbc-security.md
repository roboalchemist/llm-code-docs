# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/advanced-security-providers/jdbc-security.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security/advanced-security-providers/jdbc-security.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/advanced-security-providers/jdbc-security.md

# JDBC security

You must have existing security tables in a relational database in order to proceed with this task.

## Switch to JDBC security

Follow the instructions below to switch from Pentaho default security to JDBC security, which will allow you to use your own security tables.

If you want to use encrypted passwords for JDBC security as explained in the **Install Pentaho Data Integration and Analytics** document, use the encrypted password for all **password** values.

If you are using the Pentaho Server and choose to switch to a JDBC security shared object, you will no longer be able to use the role and user administration settings in the Administration portion of the User Console.

1. Stop the Pentaho Server.
2. Open `/pentaho-solutions/system/security.properties` with a text editor.
3. Change the value of the provide property to `jdbc`.
4. Set up the connection to the database that holds the users and authorities:
   1. Open the `/pentaho-solutions/system/applicationContext-spring-security-jdbc.properties` file with a text editor. Find the following two lines and change the `jdbcDriver` and `URL` to the appropriate values.

      ```
      datasource.driver.classname=org.hsqldb.jdbcDriver
      ```

      ```
      datasource.url=jdbc:hsqldb:hsql://localhost:9002/userdb
      ```
   2. Change the user name and password by editing the following two items:

      ```
      \datasource.username=sa, datasource.password=
      ```
   3. Set the **validation.query** by editing its row. Examples of different validation queries are shown in the file.

      ```
      datasource.validation.query=SELECT 1 FROM INFORMATION_SCHEMA.SYSTEM_USERS
      ```
   4. Set the `wait timeout, max pool,` and `max idle` by editing the following three items to change the defaults.

      ```
      datasource.pool.max.wait=-1, datasource.pool.max.active=8, datasource.max.idle=4
      ```
   5. Save the file and close the editor.
5. If needed, modify the user queries that pull information about users and authorities:
   1. Open `/pentaho-solutions/system/applicationContext-spring-security-jdbc.xml` with a text editor.
   2. Find the following line and change the SQL query returning the user and roles for which the user is a member to the appropriate statement:

      ```xml
      <value>
          <[SELECT username, authority FROM GRANTED_AUTHORITIES WHERE username = ? ORDER BY authority]>
      </value>
      ```
   3. Find the following line and change the SQL query that determines the user, password, and whether they can log in to the appropriate statement:

      ```xml
      <value>
          <[SELECT username, password, enabled FROM USERS WHERE username = ? ORDER BY username]>
      </value>
      ```
6. If needed, modify the following role queries that pull information about users and authorities.
   1. Open the `/pentaho-solutions/system/applicationContext-pentaho-security-jdbc.xml` file with a text editor.
   2. Find the following line and change the SQL query showing the roles for security on objects to the appropriate statement:

      ```xml
      <value>
          <[SELECT distinct(authority) as authority FROM AUTHORITIES ORDER BY authority]>
      </value>
      ```
   3. Find the following line and change the SQL query that returns all users in a specific role to the appropriate statement:

      ```xml
      <value>
          <[SELECT distinct(username) as username FROM GRANTED_AUTHORITIES where authority = ? ORDER BY username]>
      </value>
      ```
   4. Find the following line and change the SQL query that returns all users by order to the appropriate statement:

      ```xml
      <value>
          <[SELECT distinct(username) as username FROM USERS ORDER BY username]>
      </value>
      ```
   5. Save the file and close the editor.
7. Update the default Pentaho admin user on the system to map to your JDBC admin user:
   1. Open the `/pentaho-solutions/system/repository.spring.properties` file with a text editor.
   2. Find the following lines and change the default value from \<admin> to map to your *\<admin username>* in your JDBC system:

      ```
      singleTenantAdminUserName=<Admin User>
      ```
   3. Save the file and close the editor.
8. To fully map the JDBC's admin role to other configuration files, specify the name of the administrator role for your JDBC authentication database in the `applicationContext-pentaho-security-jdbc.xml` file.
   1. Open the `/pentaho-solutions/system/applicationContext-pentaho-security-jdbc.xml` file with a text editor.
   2. Find the following lines and change the entry key to the key assigned to the administrator role in your JDBC authentication database:

      ```xml
      <!-- map ldap role to pentaho security role -->
      <util:map id="jdbcRoleMap">
         <entry key="Admin" value="Administrator"/>
      </util:map>
      ```
   3. Save and close the file.
9. Start the Pentaho Server.

   The server is configured to authenticate users against the specified database.

## Manual LDAP/JDBC hybrid configuration

You might need to create a hybrid between an LDAP security solution and a JDBC security table for role definitions. This is common in situations where LDAP roles can't be redefined for Pentaho Server use. These instructions help you switch the Pentaho Server's authentication back-end from the Pentaho data access object to an LDAP/JDBC hybrid.

Before you begin configuring LDAP and JDBC for the Pentaho Server, you will need to verify a couple of things.

| Task                                                  | Description                                                                                                              |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Verify Successful Default Pentaho Security Deployment | Make sure your Pentaho Server has been successfully deployed using default Pentaho Security (Jackrabbit authentication). |
| Configure Pentaho for LDAP Authentication             | Verify that your Pentaho system is configured for LDAP authentication.                                                   |
| Verify Database with User Roles                       | Verify that you have a database populated with your user roles.                                                          |

After you finish the prerequisite tasks above, there are a few things that you need to do in order set up a hybrid LDAP/JDBC configuration successfully. The table structure described here is for example purposes.

These sections will guide you through the remaining steps of this process:

* [Step 1: Create user/authorities database tables](#step-1-create-user-authorities-database-tables)
* [Step 2: Set up inserts for tables](#step-2-update-user-and-role-values-for-tables)
* [Step 3: Update JDBC security queries](#step-3-update-jdbc-security-queries)
* [Step 4: Enable JDBC authorization beans](#step-4-enable-jdbc-authorization-beans)
* [Step 5: Verify LDAP/JDBC configuration](#step-5-verify-ldap-jdbc-configuration)

### Step 1: Create user/authorities database tables

You will need to create a few database tables in order to get LDAP and JDBC to work together.

1. Create a table called `USERS` and populate it with the following values:

   | Column Name | Column Type  | Column Description                                                  |
   | ----------- | ------------ | ------------------------------------------------------------------- |
   | username    | VARCHAR(50)  | The User name.                                                      |
   | password    | VARCHAR(50)  | This column value is not considered in a hybrid LDAP/JDBC solution. |
   | enables     | VARCHAR(100) | Set to `true` if user is enables; `false` if not enabled.           |
2. Create a table called `AUTHORITIES` and populate it with the following values:

   | Column Name | Column Type | Column Description                                           |
   | ----------- | ----------- | ------------------------------------------------------------ |
   | authority   | VARCHAR(50) | The Pentaho role, such as Administrator, Report Author, etc. |
3. Create a table called `GRANTED_AUTHORITIES` and populate it with the following values:

   | Column Name | Column Type | Column Description       |
   | ----------- | ----------- | ------------------------ |
   | username    | VARCHAR(50) | The User name.           |
   | authority   | VARCHAR(5)  | Associated Pentaho role. |

### Step 2: Update user and role values for tables

Next, you will need to perform a series of updates for the tables you just created. Users will be authenticated using their Active Directory password.

**Note:** Some syntax examples are provided here for you to customize with your own values.

1. Update usernames and passwords in the USERS table as shown:

   ```xml
   INSERT INTO USERS VALUES('username','Password1','1',NULL)
   ```
2. Update roles in the AUTHORITIES table as shown:

   ```xml

   INSERT INTO AUTHORITIES VALUES('DBPentAdmins','Super User')
   INSERT INTO AUTHORITIES VALUES('DBPentHR','HR Users')
   INSERT INTO AUTHORITIES VALUES('DBPentFinance','Finance Users')
   INSERT INTO AUTHORITIES VALUES('DBPentUsers','User has not logged in')

   ```
3. Update users with their associated roles in the GRANTED\_AUTHORITIES table as shown:

   ```xml

   INSERT INTO GRANTED_AUTHORITIES VALUES('admin','DBPentAdmins')
   INSERT INTO GRANTED_AUTHORITIES VALUES('admin','DBPentUsers')
   INSERT INTO GRANTED_AUTHORITIES VALUES('tiffany','DBPentUsers')
   INSERT INTO GRANTED_AUTHORITIES VALUES('tiffany','DBPentFinance')
   INSERT INTO GRANTED_AUTHORITIES VALUES('pat','DBPentUsers')
   INSERT INTO GRANTED_AUTHORITIES VALUES('pat','DBPentHR')

   ```

### Step 3: Update JDBC security queries

You might have different names for your created tables than are provided in these examples. If so, after you have updated your user and role values in your tables, you need to update a couple of queries and other items to match your system names.

1. Locate the `/pentaho-server/pentaho-solutions/system` directory and update these two files with the noted information.
   1. `applicationContext-pentaho-security-jdbc.xml`
   2. `applicationContext-spring-security-jdbc.xml`
2. Update the **query**, as well as field names such as **username**, **password**, and **enabled** that are expected by spring framework security. Be sure to use an alias if you are using different field names.

   ```

   SELECT userid as username, 'password' as password, 'enabled' as enabled FROM USERS_ROLES WHERE userid= ? ORDER BY userid

   ```
3. Stop the Pentaho Server.
4. Copy your respective database JDBC driver to the `tomcat/lib` directory.

   See the **JDBC drivers reference** in the Try Pentaho Data Integration and Analytics document for information on supported drivers.

### Step 4: Enable JDBC Authorization beans

Last, you will need to enable some JDBC Authorization beans.

#### Update security properties file

Perform the following steps to update the `security.properties` file:

1. Stop the Pentaho Server.
2. Locate the `pentaho-server/pentaho-solutions/system` directory.
3. Open the `security.properties` file with any text editor.
   1. Locate the LDAP property bean and add the role provider as shown here:

      ```xml
      provider=ldap
      role.provider=jdbc
      ```
4. Save and close the file.

#### Update spring security-jdbc properties file

Perform the following steps to update the `applicationContext-spring-security-jdbc.properties` file:

1. Open the `applicationContext-spring-security-jdbc.properties` file.
2. Add or update this database information with your system values.

   | Database Setting                | Description                                                                                                                                                                                                   |
   | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **datasource.driver.classname** | Fully-qualified Java class name of the JDBC driver you are using.                                                                                                                                             |
   | **datasource.url**              | Connection URL to be passed to your JDBC driver to establish a connection.                                                                                                                                    |
   | **datasource.username**         | Connection username to be passed to our JDBC driver to establish a connection                                                                                                                                 |
   | **datasource.password**         | Connection password to be passed to our JDBC driver to establish a connection                                                                                                                                 |
   | **datasource.validation.query** | SQL query that is used to validate connections from this pool before returning them to the caller. This query must be a SELECT statement that returns at least one row.                                       |
   | **datasource.pool.max.wait**    | Maximum number of milliseconds that the pool will wait when there are no available connections. For a connection to be returned before throwing an exception, or `<= 0`, to wait indefinitely. Default is -1. |
   | **datasource.pool.max.active**  | Maximum number of active connections that can be allocated from this pool at the same time, or negative for no limit. Default value is 8.                                                                     |
   | **datasource.max.idle**         | Maximum number of connections that can remain idle in the pool, without extra ones being destroyed, or negative for no limit. Default value is 8.                                                             |
   | **datasource.min.idle**         | Minimum number of active connections that can remain idle in the pool, without extra ones being created when the evictor runs, or `0` to create none. Default value is 0.                                     |
3. Save and close the file.

#### Update the pentaho-security-jdbc file

Perform the following steps to update the `applicationContext-pentaho-security-jdbc.xml` file:

1. Open the `applicationContext-pentaho-security-jdbc.xml` file.
2. Change the entry key to show your admin role for your database.

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>From:</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;util:map id="jdbcRoleMap">
&#x3C;entry key="Admin" value="Administrator"/>
&#x3C;/util:map>
</code></pre></td></tr><tr><td>To:</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;util:map id="jdbcRoleMap">
&#x3C;entry key="DBPentAdmins" value="Administrator"/>
&#x3C;/util:map>
</code></pre></td></tr></tbody></table>

3\. Save and close the file.

#### Update the pentahoObjects spring file

Perform the following steps to update the `pentahoObjects.spring.xml` file:

1. Open the `pentahoObjects.spring.xml` file.
2. Change these beans as shown, then save and close the file.

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>From:</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;pen:bean id="activeUserRoleListService" class="org.pentaho.platform.api.engine.IUserRoleListService">
&#x3C;pen:attributes>
&#x3C;pen:attr key="providerName" value="${security.provider}"/>
&#x3C;/pen:attributes>
&#x3C;/pen:bean>
</code></pre></td></tr><tr><td>To:</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;pen:bean id="activeUserRoleListService" class="org.pentaho.platform.api.engine.IUserRoleListService">
&#x3C;pen:attributes>
&#x3C;pen:attr key="providerName" value="jdbc"/>
&#x3C;/pen:attributes>
&#x3C;/pen:bean>
</code></pre></td></tr></tbody></table>

#### Update spring security-ldap file

Perform the following steps to update the `applicationContext-spring-security-ldap.xml` file:

1. Open the `applicationContext-spring-security-ldap.xml` file.
2. Remove the bean for `org.springframework.security.ldap.populator.DefaultLdapAuthoritiesPopulator` and replace it with this one:

   ```xml
   <bean id="populator" class="org.springframework.security.ldap.authentication.UserDetailsServiceLdapAuthoritiesPopulator">
   <constructor-arg ref="jdbcUserDetailsService" />
   </bean>
   ```
3. Save and close the file.

#### Update the repository spring properties file

Perform the following steps to update the `repository.spring.properties` file:

1. Open the `repository.spring.properties` file.
2. Locate the value for the `singleTenantAdminUserName` and make sure that it points to the correct admin user for your system.
3. Restart the Pentaho Server.

### Step 5: Verify LDAP/JDBC Configuration

Pentaho should now be successfully configured with hybrid authentication. Users are authenticated through LDAP, and the roles are authorized through JDBC. You can verify this by logging into PUC as an admin and checking in the Users & Roles tab in the Administration perspective.
