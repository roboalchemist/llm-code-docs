# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-cloudera-cluster/edit-the-configuration-files-for-users-cloudera/edit-mapred-site-xml-file.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-amazon-emr-cluster/edit-configuration-files-for-users-emr/edit-mapred-site-xml-file.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-amazon-emr-cluster/edit-configuration-files-for-users-emr/edit-mapred-site-xml-file.md

# Edit mapred-site XML file

If you are using MapReduce, you must edit the `mapred-site.xml` file to indicate where the job history logs are stored and to allow MapReduce jobs to run across platforms.

Perform the following steps to edit the `mapred-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `mapred-site.xml` file.
2. Add the following values:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>mapreduce.app-submission.cross-platform</strong></td><td><p>This property allows MapReduce jobs to run on either Windows client or Linux server platforms.```xmlmapreduce.app-submission.cross-platformtrue</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;/tbody>
&#x3C;/table>3.  Save and close the file.

</code></pre></td></tr></tbody></table>
