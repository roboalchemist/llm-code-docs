# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-amazon-emr-cluster/edit-configuration-files-for-users-emr/verify-or-edit-core-site-xml-file.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-amazon-emr-cluster/edit-configuration-files-for-users-emr/verify-or-edit-core-site-xml-file.md

# Verify or edit core-site XML file

**Note:** If you plan to run MapReduce jobs on an Amazon EMR cluster, make sure you have read, write, and execute access to the S3 Buffer directories specified in the `core-site.xml` file on the EMR cluster.

You must edit the `core-site.xml` file to add information about your AWS Access Key ID, your Access key, and your LZO compression setting.

Perform the following steps to edit your `core-site.xml`:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `core-site.xml` file.
2. Add the following values:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Values</td></tr><tr><td><strong>fs.s3.awsAccessKeyId</strong></td><td><p>​Value of your S3 AWS Access Key ID.```xml<br>fs.s3.awsAccessKeyId<br><em>[INSERT YOUR VALUE HERE]</em></p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;tr>&#x3C;td>

**fs.s3.awsSecretAccessKey**

\</td>\<td>

Value of your AWS secret access key.\`\`\`xml
\<property>\
\<name>fs.s3.awsSecretAccessKey\</name>\
\<value>*\[INSERT YOUR VALUE HERE]*\</value>
\</property> </code></pre></td></tr></tbody></table>

3\. If needed, enter the AWS Access Key ID and Access Key for S3N like this:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Values</td></tr><tr><td><strong>fs.s3n.awsAccessKeyId</strong></td><td><p>Value of your S3N AWS Access Key ID.```xmlfs.s3n.awsAccessKeyId<em>[INSERT YOUR VALUE HERE]</em></p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;tr>&#x3C;td>

**fs.s3n.awsSecretAccessKey**

\</td>\<td>

Value of your S3N AWS secret access key.\`\`\`xml
\<property>
\<name>fs.s3n.awsSecretAccessKey\</name>
\<value>\[INSERT YOUR VALUE HERE]\</value>
\</property> </code></pre></td></tr></tbody></table>

4\. Add the following values:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Values</td></tr><tr><td><strong>fs.s3n.impl</strong></td><td><pre class="language-xml"><code class="lang-xml">&#x3C;property>
   &#x3C;name>fs.s3n.impl&#x3C;/name>
   &#x3C;value>org.apache.hadoop.fs.s3native.NativeS3FileSystem&#x3C;/value>
&#x3C;/property>
</code></pre></td></tr><tr><td><strong>fs.s3.impl</strong></td><td><pre class="language-xml"><code class="lang-xml">&#x3C;property>
   &#x3C;name>fs.s3.impl&#x3C;/name>
   &#x3C;value>org.apache.hadoop.fs.s3.S3FileSystem&#x3C;/value>
&#x3C;/property>
</code></pre></td></tr><tr><td><strong>fs.s3a.impl</strong></td><td><pre class="language-xml"><code class="lang-xml">&#x3C;property>
   &#x3C;name>fs.s3a.impl&#x3C;/name>
   &#x3C;value>org.apache.hadoop.fs.s3a.S3AFileSystem&#x3C;/value>
&#x3C;/property>
</code></pre></td></tr></tbody></table>

5\. LZO is a compression format that Amazon EMR supports. If you want to configure for LZO compression, you need to download a JAR file. If you do not, you need to remove a parameter from the \`core-site.xml\` file.

```
-   If you are not using LZO compression, remove any references to the **iocompression** parameter in the `core-site.xml` file: **com.hadoop.compression.lzo.LzoCodec**
-   If you are not using LZO compression, download the LZO JAR and add it to `pentaho-big-data-plugin/hadoop-configurations/emr3x/lib` directory. The LZO JAR can be found here: [http://maven.twttr.com/com/hadoop/gplcompression/hadoop-lzo/0.4.19/](http://maven.twttr.com/com/hadoop/gplcompression/hadoop-lzo/0.4.19/).
```

6\. Save and close the file.
