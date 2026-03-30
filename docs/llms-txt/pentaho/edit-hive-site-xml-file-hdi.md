# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi/edit-hive-site-xml-file-hdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi/edit-hive-site-xml-file-hdi.md

# Edit Hive site XML file

If you are using Hive, follow these instructions to set the location of the hive metastore in the `hive-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `hive-site.xml` file.
2. Add the following values:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>hive.metastore.uris</strong></td><td>Set this to the location of your hive metastore if it differs from what is on your instance of HDI.</td></tr><tr><td><strong>fs.azure.account.keyprovider.eastorageacct2.blob.core.windows.net</strong></td><td><p>Add this property for security.```xmlfs.azure.account.keyprovider.eastorageacct2.blob.core.windows.nethive/<em>&#x3C;Kerberos principal realm@example.com></em></p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;/tbody>
&#x3C;/table>3.  Save and close the file.

</code></pre></td></tr></tbody></table>
