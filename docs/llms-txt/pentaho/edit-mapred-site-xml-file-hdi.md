# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi/edit-mapred-site-xml-file-hdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi/edit-mapred-site-xml-file-hdi.md

# Edit Mapred site XML file

If you are using MapReduce, edit the `mapred-site.xml` file to indicate where the job history logs are stored and to allow MapReduce jobs to run across platforms.

Perform the following steps to edit the `mapred-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `mapred-site.xml` file.
2. Verify that the **mapreduce.jobhistory.address** and **mapreduce.job.hdfs-servers** properties are in the `mapred-site.xml` file. If they are not in the file, you can add them as follows:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>mapreduce.jobhistory.address</strong></td><td><p>Set this property to the place where job history logs are stored, as shown in the following example:```xmlmapreduce.jobhistory.address<em>&#x3C;active node name in the cluster></em>:10020</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;tr>&#x3C;td>

**mapreduce.job.hdfs-servers**

\</td>\<td>

Add this property for YARN:

```xml
&#x3C;property>
   &#x3C;name>mapreduce.job.hdfs-servers&#x3C;/name>
   &#x3C;value>hdfs://*&#x26;lt;active node name in the cluster&#x26;gt;*:8020&#x3C;/value>
&#x3C;/property>
</code></pre></td></tr></tbody></table>

3\. Optionally, to allow YARN containers to launch on JDK11.x nodes, add the \*\*mapreduce.jvm.add-opens-as-default\*\* property to the \`mapred-site.xml\` file, as shown below. All MapReduce jobs require this property to be added in \`mapred-site.xml\` to run successfully on JDK11.x machines as JAVA 11 does not require \*\*ADD\\\_OPENS\*\* JVM arguments by default.

```

**Note:** Do not add this property to containers using JDK17.x nodes.

````

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>mapreduce.jvm.add-opens-as-default</strong></td><td><p>Add this property for YARN to launch on JDK11.x nodes:```xmlmapreduce.jvm.add-opens-as-default false</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;/tbody>
&#x3C;/table>4.  Save and close the file.


</code></pre></td></tr></tbody></table>
````
