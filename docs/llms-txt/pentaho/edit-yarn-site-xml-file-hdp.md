# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-hortonworks-cluster/edit-the-configuration-files-for-users-hdp/edit-yarn-site-xml-file-hdp.md

# Edit YARN site XML file

If you are using YARN, you must verify that the following parameters are set in the `yarn-site.xml` file.

Perform the following steps to edit the `yarn-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `yarn-site.xml` file.
2. Add these values:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>yarn.application.classpath</strong></td><td><p>​Add the classpaths needed to run YARN applications, as shown in the following example:```xmlyarn.application.classpath$HADOOP_CONF_DIR,/usr/hdp/current/hadoop-client/<em>,</em><br><em>/usr/hdp/current/hadoop-client/lib/</em>,/usr/hdp/current/hadoop-hdfs-client/<em>,</em><br><em>/usr/hdp/current/hadoop-hdfs-client/lib/</em>,/usr/hdp/current/hadoop-yarn-client/<em>,</em><br><em>/usr/hdp/current/hadoop-yarn-client/lib/</em></p><pre><code>
 Use commas to separate multiple paths.

\</td>\</tr>\<tr>\<td>

**yarn.resourcemanager.hostname**

\</td>\<td>

Update the hostname in your environment or use the default: sandbox.hortonworks.com

\</td>\</tr>\<tr>\<td>

**yarn.resourcemanager.address**

\</td>\<td>

Update the hostname and port for your environment.

\</td>\</tr>\<tr>\<td>

**yarn.resourcemanager.admin.address**

\</td>\<td>

Update the hostname and port for your environment.

\</td>\</tr>\</tbody>
\</table>3.  Save and close the file.

</code></pre></td></tr></tbody></table>
