# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-hortonworks-cluster/edit-the-configuration-files-for-users-hdp/edit-mapred-site-xml-file-hdp.md

# Edit Mapred site XML file

If you are using MapReduce, you must edit the `mapred-site.xml` file to indicate where the job history logs are stored and to allow MapReduce jobs to run across platforms.

Perform the following steps to edit the `mapred-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `mapred-site.xml` file.
2. Add the following values:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>mapreduce.jobhistory.address</strong></td><td>Set this to the folder where you want to store the job history logs.</td></tr><tr><td><strong>mapreduce.application.classpath</strong></td><td><p>Add classpath information. Here is an example:```xmlmapreduce.application.classpath$PWD/mr-framework/hadoop/share/hadoop/mapreduce/*<br>:$PWD/mr-framework/hadoop/share/hadoop/mapreduce/lib/*<br>:$PWD/mr-framework/hadoop/share/hadoop/common/<em>:$PWD/mr-framework/hadoop/share/hadoop/common/lib/</em><br>:$PWD/mr-framework/hadoop/share/hadoop/yarn/<em>:$PWD/mr-framework/hadoop/share/hadoop/yarn/lib/</em><br>:$PWD/mr-framework/hadoop/share/hadoop/hdfs/<em>:$PWD/mr-framework/hadoop/share/hadoop/hdfs/lib/</em><br>:/usr/hdp/${hdp.version}/hadoop/lib/hadoop-lzo-0.6.0.${hdp.version}.jar:/etc/hadoop/conf/secure</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;tr>&#x3C;td>

**mapreduce.application.framework.path**

\</td>\<td>

Set the framework path. Here is an example:\`\`\`xml
\<property>
\<name>mapreduce.application.framework.path\</name>
\<value>/hdp/apps/${hdp.version}/mapreduce/mapreduce.tar.gz#mr-framework\</value>
\</property> </code></pre></td></tr></tbody></table>

3\. Verify the \*\*mapreduce.app-submission.cross-platform\*\* property is in the \`mapred-site.xml\` file. If it is not in the file, add it as follows.

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>mapreduce.app-submission.cross-platform</strong></td><td><p>Add this property to allow MapReduce jobs to run on either Windows client or Linux server platforms.```xmlmapreduce.app-submission.cross-platformtrue</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;/tbody>
&#x3C;/table>4.  Save and close the file.

</code></pre></td></tr></tbody></table>
