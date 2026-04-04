# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server/install-jdbc-driver-as-a-module-in-jboss/create-module-file-for-pentaho-repository-database.md

# Create module file for Pentaho Repository database

You need to create a file for the database that hosts the Pentaho Repository (either PostgreSQL, MySQL, or Oracle), as well as for HSQLDB.

1. Locate the `pentaho/server/pentaho-server/<your jboss installation directory>/modules/system/layers/base/org` folder and create one of the following paths for the database on which you are hosting the Pentaho Repository.
   * PostgreSQL: `postgresql/main`
   * MySQL: `mysql/main`
   * Oracle: `oracle/main`
   * MS SQL Server: `sqlserver/main`
2. Create these two paths in the same directory.
   * HSQLDB: `hsqldb/main`
   * H2: `h2/main`
3. Download the supported JDBC driver for your Pentaho Repository database to the directory that you just created.
4. Within that directory, do the following things:
   1. Use an editor to create a text file named `module.xml`.
   2. Copy the appropriate code into the `module.xml` file, then modify it so that the name of the JDBC driver you just downloaded appears.

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Repository Type</td><td>Module Code</td></tr><tr><td>PostgreSQL</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;?xml version="1.0" encoding="UTF-8"?>
    &#x3C;module xmlns="urn:jboss:module:1.0"name="org.postgresql">
        &#x3C;resources>
            &#x3C;resource-root path="[Name of JDBC Jar You Downloaded Here]"/>
        &#x3C;/resources>
        &#x3C;dependencies>&#x3C;module name="javax.api"/>&#x3C;/dependencies>7
    &#x3C;/module>
</code></pre></td></tr><tr><td>MySQL</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;?xml version="1.0" encoding="UTF-8"?>
    &#x3C;module xmlns="urn:jboss:module:1.0"name="org.mysql">
        &#x3C;resources>
            &#x3C;resource-root path="[Name of JDBC Jar You Downloaded Here]"/>
        &#x3C;/resources>
        &#x3C;dependencies>&#x3C;module name="javax.api"/>&#x3C;/dependencies>
    &#x3C;/module>
</code></pre></td></tr><tr><td>Oracle</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;?xml version="1.0" encoding="UTF-8"?>
    &#x3C;module xmlns="urn:jboss:module:1.0"name="org.oracle">
        &#x3C;resources>
            &#x3C;resource-root path="[Name of JDBC Jar You Downloaded Here]"/>
        &#x3C;/resources>
        &#x3C;dependencies>&#x3C;module name="javax.api"/>&#x3C;/dependencies>
    &#x3C;/module>
</code></pre></td></tr><tr><td>MS SQL Server</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;?xml version="1.0" encoding="UTF-8"?>
    &#x3C;module xmlns="urn:jboss:module:1.0"name="org.sqlserver">
        &#x3C;resources>
            &#x3C;resource-root path="[Name of JDBC Jar You Downloaded Here]"/>
        &#x3C;/resources>
        &#x3C;dependencies>&#x3C;module name="javax.api"/>&#x3C;/dependencies>
    &#x3C;/module>
</code></pre></td></tr></tbody></table>

3\. Save and close the \`module.xml\` file.
