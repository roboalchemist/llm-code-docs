# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-google-dataproc/edit-configuration-files-for-users-cp-gdp/edit-mapred-site-xml-file-gdp.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-google-dataproc/edit-configuration-files-for-users-cp-gdp/edit-mapred-site-xml-file-gdp.md

# Edit the XML file for MapReduce

If you are using MapReduce, you wil need to edit the `mapred-site.xml` file to indicate where the job history logs are stored and to allow MapReduce jobs to run across platforms.

Perform the following steps to edit the `mapred-site.xml` file.

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `mapred-site.xml` file.
2. Add the following values for the parameter:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>mapreduce.app-submission.cross-platform</strong></td><td><p>This property is only needed to run MapReduce jobs on Windows platforms.```xmlmapreduce.app-submission.cross-platformtrue</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;/tbody>
&#x3C;/table>3.  Save and close the file.

</code></pre></td></tr></tbody></table>
