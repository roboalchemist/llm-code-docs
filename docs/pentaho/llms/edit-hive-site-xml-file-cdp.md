# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/edit-configuration-files-for-users-cdp/edit-hive-site-xml-file-cdp.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/edit-configuration-files-for-users-cdp/edit-hive-site-xml-file-cdp.md

# Edit Hive site XML file

If you are using Hive, follow these instructions to set the location of the hive metastore in the `hive-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `hive-site.xml` file.
2. Add the following values:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>hive.metastore.uris</strong></td><td>Set this to the location of your hive metastore if it differs from what is on your instance of CDP.</td></tr><tr><td><strong>hive.server2.enable.impersonation</strong></td><td><p>Add this property if you are using impersonation for security.```xmlhive.server2.enable.impersonationtrue</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;tr>&#x3C;td>

**hive.server2.enable.doAs**

\</td>\<td>

Add this property if you are using impersonation for security.`xml
&#x3C;property>
      &#x3C;name>hive.server2.enable.doAs&#x3C;/name> 
      &#x3C;value>true&#x3C;/value> 
   &#x3C;/property> </code></pre></td></tr><tr><td><strong>tez.lib.uris</strong></td><td><p>Add this property if you are using Hive3 on Tez.`xmltez.lib.uris/user/tez/0.9.1.7.1.4.0-203/tez.tar.gz</p><pre><code>
\</td>\</tr>\</tbody>
\</table>3.  Save and close the file.

</code></pre></td></tr></tbody></table>
