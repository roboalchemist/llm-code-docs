# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi/edit-core-site-xml-file-hdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi/edit-core-site-xml-file-hdi.md

# Edit Core site XML file

If you are using a secured instance of HDI, follow these instructions to update the `core-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `core-site.xml` file.
2. Add the following storage values defined for your storage type.
   * If you are using WASB storage:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>fs.AbstractFileSystem.wasb.impl</strong></td><td><p>Add this property to associate your WASB storage with the file system.```xmlfs.AbstractFileSystem.wasb.implorg.apache.hadoop.fs.azure.Wasb</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;tr>&#x3C;td>

**pentaho.runtime.fs.default.name**

\</td>\<td>

Add this property to specify the container and storage names.\`\`\`xml
\<property>
\<name>pentaho.runtime.fs.default.name\</name>
\<value>wasb://*\&lt;container name associated with cluster\&gt;*@*\&lt;storage account name\&gt;.blob.core.windows.net*\</value>
\</property> </code></pre></td></tr></tbody></table>

\- If you are using ADLS storage:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>pentaho.runtime.fs.default.name</strong></td><td><p>Add this property to specify the container and storage names.```xmlpentaho.runtime.fs.default.nameabfs://<em>&#x3C;container name associated with cluster></em>@<em>&#x3C;storage account name></em>.dfs.core.windows.net</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;/tbody>
&#x3C;/table>3.  Save and close the file.

</code></pre></td></tr></tbody></table>
