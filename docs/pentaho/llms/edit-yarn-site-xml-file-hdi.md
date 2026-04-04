# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi/edit-yarn-site-xml-file-hdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi/edit-yarn-site-xml-file-hdi.md

# Edit YARN site XML file

If you are using YARN, set the following parameters in the `yarn-site.xml` file.

Perform the following steps to edit the `yarn-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `yarn-site.xml` file.
2. Add the following values:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>yarn.resourcemanager.hostname</strong></td><td><p>Set this property to the hostname of the resource manager in your environment, as shown in the following example.```xmlyarn.resourcemanager.hostnamehdfs://<em>&#x3C;active node name in the cluster></em></p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;tr>&#x3C;td>

**yarn.resourcemanager.address**

\</td>\<td>

Set this poperty to the hostname and port for your environment. For example, `&#x3C;value>hdfs://*&#x26;lt;active node name in the cluster&#x26;gt;*:8050&#x3C;/value>`

\</td>\</tr>\<tr>\<td>

**yarn.resourcemanager.admin.address**

\</td>\<td>

Set this property to the hostname and port for your environment. For example, `&#x3C;value>hdfs://*&#x26;lt;active node name in the cluster&#x26;gt;*:8141&#x3C;/value>`

\</td>\</tr>\</tbody>
\</table>3.  Save and close the file.

</code></pre></td></tr></tbody></table>
