# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/install-jdbc-driver-as-a-module-in-jboss/step-1-create-module-file-for-pentaho-repository-database.md

# Step 1: Create module file for Pentaho Repository database

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

   The [JDBC drivers reference](https://docs.pentaho.com/install/9.3-install/jdbc-drivers-reference) has a list of supported drivers.
4. Within that directory, perform the following steps.
   1. Use an editor to create a text file named `module.xml`.
   2. Copy the appropriate code into the `module.xml` file, then modify it so that the name of the JDBC driver you just downloaded appears.
   3. Save and close the `module.xml` file.

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Repository Type</td><td>Module code</td></tr><tr><td>PostgreSQL</td><td><pre class="language-xml"><code class="lang-xml">
&#x3C;?xml version="1.0" encoding="UTF-8"?>
    &#x3C;module xmlns="urn:jboss:module:1.0" name="org.postgresql">
        &#x3C;resources>
            &#x3C;resource-root path="[Name of JDBC Jar You Downloaded Here]"/>
        &#x3C;/resources>
        &#x3C;dependencies>&#x3C;module name="javax.api"/>&#x3C;/dependencies>
    &#x3C;/module>

</code></pre></td></tr><tr><td>MySQL</td><td><pre class="language-xml"><code class="lang-xml">
\<?xml version="1.0" encoding="UTF-8"?>
\<module xmlns="urn:jboss:module:1.0" name="org.mysql">
\<resources>
\<resource-root path="\[Name of JDBC Jar You Downloaded Here]"/>
\</resources>
\<dependencies>\<module name="javax.api"/>\</dependencies>
\</module>

</code></pre></td></tr><tr><td>Oracle</td><td><pre class="language-xml"><code class="lang-xml">
\<?xml version="1.0" encoding="UTF-8"?>
\<module xmlns="urn:jboss:module:1.0" name="org.oracle">
\<resources>
\<resource-root path="\[Name of JDBC Jar You Downloaded Here]"/>
\</resources>
\<dependencies>\<module name="javax.api"/>\</dependencies>
\</module>

</code></pre></td></tr><tr><td>MS SQL Server</td><td><pre class="language-xml"><code class="lang-xml">
\<?xml version="1.0" encoding="UTF-8"?>
\<module xmlns="urn:jboss:module:1.0" name="org.sqlserver">
\<resources>
\<resource-root path="\[Name of JDBC Jar You Downloaded Here]"/>
\</resources>
\<dependencies>\<module name="javax.api"/>\</dependencies>
\</module>

</code></pre></td></tr></tbody></table>
