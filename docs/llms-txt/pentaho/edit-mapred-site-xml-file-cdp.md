# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/edit-configuration-files-for-users-cdp/edit-mapred-site-xml-file-cdp.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/edit-configuration-files-for-users-cdp/edit-mapred-site-xml-file-cdp.md

# Edit Mapred site XML file

If you are using MapReduce, you must edit the `mapred-site.xml` file to indicate where the job history logs are stored and to allow MapReduce jobs to run across platforms.

Perform the following steps to edit the `mapred-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `mapred-site.xml` file.
2. Verify the **mapreduce.jobhistory.address** and **mapreduce.app-submission.cross-platform** properties are in the `mapred-site.xml` file. If they are not in the file, add them as follows.

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>mapreduce.jobhistory.address</strong></td><td>Set this to the place where job history logs are stored.</td></tr><tr><td><strong>mapreduce.app-submission.cross-platform</strong></td><td><p>Add this property to allow MapReduce jobs to run on either Windows client or Linux server platforms.</p><pre class="language-xml"><code class="lang-xml">&#x3C;property>
   &#x3C;name>mapreduce.app-submission.cross-platform&#x3C;/name>
   &#x3C;value>true&#x3C;/value>
&#x3C;/property>
</code></pre></td></tr></tbody></table>

3\. Save and close the file.
