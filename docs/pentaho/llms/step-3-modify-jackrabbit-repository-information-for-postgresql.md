# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/configure-postgresql-pentaho-repository-database/step-3-modify-jackrabbit-repository-information-for-postgresql.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/configure-postgresql-pentaho-repository-database/step-3-modify-jackrabbit-repository-information-for-postgresql.md

# Step 3: Modify Jackrabbit repository information for PostgreSQL

Edit the following code to change the default Jackrabbit repository to PostgreSQL.

1. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system/jackrabbit` and open the `repository.xml` file with any text editor.
2. In each of the sections, comment out any resource references that refer to other databases.

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Item</td><td>Code Section</td></tr><tr><td>Repository</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;FileSystem class="org.apache.jackrabbit.core.fs.db.DbFileSystem">
    &#x3C;param name="driver" value="javax.naming.InitialContext"/>
    &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
    &#x3C;param name="schema" value="postgresql"/>
    &#x3C;param name="schemaObjectPrefix" value="fs_repos_"/>
  &#x3C;/FileSystem>
</code></pre></td></tr><tr><td>DataStore</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;DataStore class="org.apache.jackrabbit.core.data.db.DbDataStore">
    &#x3C;param name="driver" value="javax.naming.InitialContext"/>
    &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
    &#x3C;param name="databaseType" value="postgresql"/>
    &#x3C;param name="minRecordLength" value="1024"/>
    &#x3C;param name="maxConnections" value="3"/>
    &#x3C;param name="copyWhenReading" value="true"/>
    &#x3C;param name="tablePrefix" value=""/>
    &#x3C;param name="schemaObjectPrefix" value="ds_repos_"/>
  &#x3C;/DataStore>
</code></pre></td></tr><tr><td>Workspaces</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;FileSystem class="org.apache.jackrabbit.core.fs.db.DbFileSystem">
      &#x3C;param name="driver" value="javax.naming.InitialContext"/>
      &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
      &#x3C;param name="schema" value="postgresql"/>
      &#x3C;param name="schemaObjectPrefix" value="fs_ws_"/>
    &#x3C;/FileSystem>
</code></pre></td></tr><tr><td>PersistenceManager (1st part)</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;PersistenceManager class="org.apache.jackrabbit.core.persistence.bundle.PostgreSQLPersistenceManager">
      &#x3C;param name="driver" value="javax.naming.InitialContext"/>
      &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
      &#x3C;param name="schema" value="postgresql"/>
      &#x3C;param name="schemaObjectPrefix" value="${wsp.name}_pm_ws_"/>
    &#x3C;/PersistenceManager>
</code></pre></td></tr><tr><td>Versioning</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;FileSystem class="org.apache.jackrabbit.core.fs.db.DbFileSystem">
      &#x3C;param name="driver" value="javax.naming.InitialContext"/>
      &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
      &#x3C;param name="schema" value="postgresql"/>
      &#x3C;param name="schemaObjectPrefix" value="fs_ver_"/>
    &#x3C;/FileSystem>
</code></pre></td></tr><tr><td>PersistenceManager (2nd part)</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;PersistenceManager class="org.apache.jackrabbit.core.persistence.bundle.PostgreSQLPersistenceManager">
      &#x3C;param name="driver" value="javax.naming.InitialContext"/>
      &#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
      &#x3C;param name="schema" value="postgresql"/>
      &#x3C;param name="schemaObjectPrefix" value="pm_ver_"/>
    &#x3C;/PersistenceManager>
</code></pre></td></tr><tr><td>DatabaseJournal</td><td><pre class="language-xml"><code class="lang-xml">&#x3C;Journal class="org.apache.jackrabbit.core.journal.DatabaseJournal">
	&#x3C;param name="revision" value="${rep.home}/revision.log" />
	&#x3C;param name="driver" value="javax.naming.InitialContext"/>
	&#x3C;param name="url" value="java:comp/env/jdbc/jackrabbit"/>
	&#x3C;param name="schema" value="postgresql"/>
	&#x3C;param name="schemaObjectPrefix" value="cl_j_"/>
	&#x3C;param name="janitorEnabled" value="true"/>
	&#x3C;param name="janitorSleep" value="86400"/>
	&#x3C;param name="janitorFirstRunHourOfDay" value="3"/>
     &#x3C;/Journal>
</code></pre></td></tr></tbody></table>
