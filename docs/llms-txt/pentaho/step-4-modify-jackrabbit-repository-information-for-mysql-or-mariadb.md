# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-mysql-or-mariadb-as-your-repository-database-manual-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-4-modify-jackrabbit-repository-information-for-mysql-or-mariadb.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-4-modify-jackrabbit-repository-information-for-mysql-or-mariadb.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-4-modify-jackrabbit-repository-information-for-mysql-or-mariadb.md

# Step 4: Modify Jackrabbit repository information for MySQL or MariaDB

Edit the following code to change the default Jackrabbit repository to MySQL. This can also be used for MariaDB.

1. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system/jackrabbit` and open the `repository.xml` file with any text editor.
2. As shown in the table below, locate and verify or change the code so that the MySQL lines are not commented out, but the MS SQL Server, Oracle, and PostgreSQL lines are commented out.

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Item</td><td>Code Section</td></tr><tr><td>Repository</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;FileSystem class="org.apache.jackrabbit.core.fs.db.DbFileSystem">
    &#x3C;param name="driver" value="javax.naming.InitialContext"/>
    &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
    &#x3C;param name="schema" value="mysql"/>
    &#x3C;param name="schemaObjectPrefix" value="fs_repos_"/>
  &#x3C;/FileSystem>
</code></pre></td></tr><tr><td>DataStore</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;DataStore class="org.apache.jackrabbit.core.data.db.DbDataStore">
    &#x3C;param name="driver" value="javax.naming.InitialContext"/>
    &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
    &#x3C;param name="databaseType" value="mysql"/>
    &#x3C;param name="minRecordLength" value="1024"/>
    &#x3C;param name="maxConnections" value="3"/>
    &#x3C;param name="copyWhenReading" value="true"/>
    &#x3C;param name="tablePrefix" value=""/>
    &#x3C;param name="schemaObjectPrefix" value="ds_repos_"/>
  &#x3C;/DataStore>
</code></pre></td></tr><tr><td>Workspaces</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;FileSystem class="org.apache.jackrabbit.core.fs.db.DbFileSystem">
      &#x3C;param name="driver" value="javax.naming.InitialContext"/>
      &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
      &#x3C;param name="schema" value="mysql"/>
      &#x3C;param name="schemaObjectPrefix" value="fs_ws_"/>
    &#x3C;/FileSystem>
</code></pre></td></tr><tr><td>PersistenceManager (1st part)</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;PersistenceManager class="org.apache.jackrabbit.core.persistence.bundle.MySqlPersistenceManager">
      &#x3C;param name="driver" value="javax.naming.InitialContext"/>
      &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
      &#x3C;param name="schema" value="mysql"/>
      &#x3C;param name="schemaObjectPrefix" value="${wsp.name}_pm_ws_"/>
    &#x3C;/PersistenceManager>
</code></pre></td></tr><tr><td>Versioning</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;FileSystem class="org.apache.jackrabbit.core.fs.db.DbFileSystem">
      &#x3C;param name="driver" value="javax.naming.InitialContext"/>
      &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
      &#x3C;param name="schema" value="mysql"/>
      &#x3C;param name="schemaObjectPrefix" value="fs_ver_"/>
    &#x3C;/FileSystem>
</code></pre></td></tr><tr><td>PersistenceManager (2nd part)</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;PersistenceManager class="org.apache.jackrabbit.core.persistence.bundle.MySqlPersistenceManager">
      &#x3C;param name="driver" value="javax.naming.InitialContext"/>
      &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
      &#x3C;param name="schema" value="mysql"/>
      &#x3C;param name="schemaObjectPrefix" value="pm_ver_"/>
    &#x3C;/PersistenceManager>
</code></pre></td></tr><tr><td>DatabaseJournal</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;Journal class="org.apache.jackrabbit.core.journal.DatabaseJournal">
	&#x3C;param name="revision" value="${rep.home}/revision.log"/>
	&#x3C;param name="driver" value="javax.naming.InitialContext"/>
	&#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
	&#x3C;param name="schema" value="mysql"/>
	&#x3C;param name="schemaObjectPrefix" value="J_C_"/>
	&#x3C;param name="janitorEnabled" value="true"/>
	&#x3C;param name="janitorSleep" value="86400"/>
	&#x3C;param name="janitorFirstRunHourOfDay" value="3"/>
     &#x3C;/Journal>
</code></pre></td></tr></tbody></table>
