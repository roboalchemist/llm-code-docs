# Source: https://docs.pentaho.com/pdc-admin/ldc-manage-data-sources-cp/adding-a-data-source-ldc-manage-data-sources-ag.md

# Adding a data source

If your role has permission to administer data sources, you can add and edit data sources.

The number of data sources you can add is determined by your license agreement. You receive a message when you have reached 75% of your data source creation quota.

If you have reached the limit of data sources allowed by your license agreement, the **Add Data Source** button on the **Resources** card is unavailable, and a message appears when you hover your cursor over the button.

{% hint style="info" %}
If you encounter an error while connecting to a data source, refer to the documentation of the specific data source provider for more information about the error.
{% endhint %}

## Active Directory as a data source

Data Catalog supports integration with both Windows-based Active Directory (AD) and Azure Active Directory (Azure AD). You can add Active Directory as a data source to import file system security identifiers (SIDs), GUIDs, and security descriptors, and map them to user identities. With this integration, Data Catalog displays the ownership and group information for files and folders from SMB, CIFS, and NFS data sources in Data Canvas.

Perform the following steps to add Active Directory as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Active Directory** in the **Data Source Type** field.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.</p></div>
5. Specify the following additional connection information.

   <table><thead><tr><th width="209.88885498046875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Configuration Method</strong></td><td><p></p><p>Select the method used to connect to Active Directory. Options include:</p><ul><li><strong>LDAP</strong>: Establishes a standard, non-encrypted connection.</li><li><strong>Secure LDAP</strong>: Establishes an encrypted connection using SSL/TLS. When you select Secure LDAP, two additional fields appear: <strong>Certificate File</strong> and <strong>Certificate Password</strong><em>.</em></li></ul></td></tr><tr><td><strong>Host</strong></td><td>The fully qualified domain name (FQDN) or IP address of the Active Directory server.</td></tr><tr><td><strong>Port</strong></td><td>The port number used to connect to the Active Directory server. The default port is usually 389 for LDAP or 636 for LDAPS (secure LDAP).</td></tr><tr><td><strong>Domain</strong></td><td>The domain name associated with the Active Directory environment.</td></tr><tr><td><strong>User Name</strong></td><td>The username that has permission to query the Active Directory. Include the domain if you have not provided the domain name.</td></tr><tr><td><strong>Password</strong></td><td>The password associated with the username. This credential is used to authenticate the connection to the AD server.</td></tr><tr><td><strong>Certificate File</strong><br>(Visible only when <strong>Configuration Method</strong> is <strong>Secure LDAP</strong>)</td><td>Upload the SSL certificate file (in <code>.crt</code> or <code>.pem</code> format) required to establish a secure connection.</td></tr><tr><td><strong>Certificate Password</strong><br>(Visible only when <strong>Configuration Method</strong> is <strong>Secure LDAP</strong>)</td><td>Specify the password associated with the uploaded certificate file, if applicable.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.
7. Click **Create Data Source** to establish your data source connection.
8. Click **Import Users**.

   This process imports file system security identifiers (SIDs), GUIDs, and security descriptors, and maps them to user identities, which helps to display ownership and group information for files and folders from SMB and CIFS data sources in Data Canvas. You can also monitor the status of the job on the Workers page

You have successfully created a connection to Active Directory as a data source in Data Catalog.

After completing the Import Users job, you can run the **Metadata Ingest** process for SMB and CIFS data sources to see the user information in the **Properties** panel. For more information, see the **Processing unstructured data** topic in the **Explore your data** section in the [**Use Pentaho Data Catalog**](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/) document. Additionally, you can see the list of users who have access to a particular file or folder. For more information, see the **Users with Access** topic in the **Use Pentaho Data Catalog** document.

## Amazon Redshift data source

Amazon Redshift is a fully managed, petabyte-scale data warehouse solution offered by Amazon Web Services (AWS). It allows users to run complex queries and perform real-time data analytics on large datasets by utilizing massively parallel processing (MPP) technology. Integrating Amazon Redshift as a data source within Data Catalog, you can access and manage metadata from the Amazon Redshift database. It enables data discovery to search, explore, and understand Amazon Redshift data. Additionally, it enhances data lineage and compliance by providing detailed tracking of data movements.

Perform the following steps to add Amazon Redshift as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the connection information, select **Redshift** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="241">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td>Select <strong>Credentials</strong>, or <strong>URI</strong> as a configuration method.</td></tr><tr><td><strong>Driver</strong></td><td>If you select the configuration method as <strong>Credentials</strong> or <strong>URI</strong>, then you must use the driver. Select an existing driver or upload a new driver to ensure efficient, secure communication between the application and the database that meets the required standards.<br>To upload a new driver, click <strong>Manage Drivers</strong>, and click <strong>Add New</strong>, upload the driver, and then click <strong>Add Driver</strong>.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The fully qualified Java class name of the JDBC driver.</td></tr><tr><td><strong>User Name</strong></td><td>The username required to authenticate to the Amazon Redshift database. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password associated with the specified Redshift user account. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains the Redshift credentials (username and password). When provided, Data Catalog retrieves the credentials securely from Secret Manager instead of requiring manual entry.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secret versions from Secret Manager. This role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the Redshift secret is stored in Secret Manager. Data Catalog uses this region to access the correct Secret Manager endpoint.</td></tr><tr><td><strong>Host</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The address of the machine where the Amazon Redshift database server is running. It can be an IP address or a domain name.</td></tr><tr><td><strong>Port</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The port number on which the Amazon Redshift server is listening for incoming connections.</td></tr><tr><td><strong>URI</strong><br>(Only for the <strong>URI</strong> method)</td><td>URIs are used to access and manage various objects and services within the Amazon Redshift environment. For example, URL would look like `<code>jdbc:redshift://:/</code>`.</td></tr><tr><td><strong>Database Name</strong></td><td>The name of the database within the Amazon Redshift server that you want to connect with.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select them, then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   **Note:** To use storage optimization options, you need a Pentaho Data Optimizer license.

   <table><thead><tr><th width="250">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created the connection to the Amazon Redshift as a data source.

## Apache Iceberg data source

Apache Iceberg is an open table format designed to manage large analytic datasets in modern data lake architectures. It provides a standardized way to define table metadata, track schema and partition changes, and manage transactional updates independently of the underlying storage systems and query engines.

In Data Catalog, you can configure Apache Iceberg as a data source to discover, catalog, and govern Iceberg-managed tables. This integration allows Data Catalog to connect directly to an Iceberg catalog and ingest table metadata based on Iceberg’s native metadata model, rather than relying on file system structures or inferred schemas.

The Apache Iceberg connector in Pentaho Data Catalog supports Iceberg warehouses deployed on AWS, HDFS, and Azure Data Lake. Perform the following steps to add Apache Iceberg as a data source in Data Catalog:

> ▶️ **Watch a walkthrough**
>
> You can watch a guided walkthrough that demonstrates [how to configure an Apache Iceberg data source in Pentaho Data Catalog](https://assets.demos.hitachivantara.com/psl/erh011s).
>
> {% embed url="<https://assets.demos.hitachivantara.com/psl/erh011s>" %}

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Apache Iceberg** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="204.00006103515625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>URI</strong></td><td>URL to the Apache Iceberg catalog service.<br>For example, URL would look like <code>http://&#x3C;ip_address_or_hostname_of_iceberg_catalog:8181</code></td></tr><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Warehouse</strong></td><td>This is where data and metadata are stored.<br>Currently, Data Catalog supports <strong>AWS</strong>, <strong>Azure Data Lake</strong>, and <strong>HDFS</strong>.</td></tr></tbody></table>

   \
   Based on the **Warehouse** selected, provide the additional connection details:

{% tabs %}
{% tab title="AWS" %}

<table><thead><tr><th width="194">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Region</strong></td><td>The AWS region where the S3 bucket hosting the Iceberg warehouse is located.</td></tr><tr><td><strong>Endpoint</strong></td><td><p>The S3-compatible endpoint used to access the Iceberg warehouse.</p><p>Example: <code>http://&#x3C;ip_address_or_hostname_of_warehouse_location:9000</code></p></td></tr><tr><td><strong>Access Key</strong></td><td>User credentials to access data in Iceberg Catalog. This key authenticates your access to the S3 bucket.</td></tr><tr><td><strong>Secret Access Key</strong></td><td>Password credential to access data on Iceberg Catalog. This key authenticates your access to the S3 bucket.</td></tr><tr><td><strong>Path Style Access</strong></td><td><p><strong>True</strong> when the user is accessing resources via a path-style access.</p><p>For example, <code>/user/home/resource</code> . </p><p>If using an alternate access style, then <strong>False</strong>.</p></td></tr></tbody></table>
{% endtab %}

{% tab title="HDFS" %}

<table><thead><tr><th width="128.66668701171875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Endpoint</strong></td><td>The HDFS NameNode or service endpoint used to access the Iceberg warehouse stored in HDFS.</td></tr><tr><td><strong>Port</strong></td><td>The port used to connect to the HDFS endpoint.</td></tr><tr><td><strong>Path</strong></td><td>The HDFS path where the Iceberg warehouse data is stored.</td></tr></tbody></table>
{% endtab %}

{% tab title="Azure Data Lake" %}

<table><thead><tr><th width="163.33331298828125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Account Name</strong></td><td>The Azure Data Lake Storage account name that hosts the Iceberg warehouse.</td></tr><tr><td><strong>Endpoint</strong></td><td>The Azure Data Lake endpoint used to access the storage account.</td></tr><tr><td><strong>Default Endpoint Protocol</strong></td><td>The protocol HTTP or HTTPS used to access the Azure Data Lake endpoint.</td></tr><tr><td><strong>Account Key</strong></td><td>The storage credentials to access data in the Iceberg Catalog. This key authenticates your access to the Azure Data Lake Storage.</td></tr></tbody></table>
{% endtab %}
{% endtabs %}

6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens.
   1. You can search and select schemas using the search bar at the top (starts with or using regular expressions), then click **Next**.
   2. On the **Ingest Schema** dialog box, add include or exclude patterns to filter the tables to be ingested, and then click **Ingest** to load the database schema and related metadata.\
      **Note**: Although you can select all schemas, it is a best practice to avoid selecting specific system-related schemas that are unnecessary for your needs.
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="250">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to Apache Iceberg as a data source.

## AWS S3 data source

Perform the following steps to add AWS S3 as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **AWS S3** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="211.7777099609375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Region</strong><sup>1</sup></td><td><p>The geographical location where AWS maintains a cluster of data centers.</p><ul><li>If connecting directly to S3, enter the region where the S3 bucket resides.</li><li>If using Secrets Manager, enter the region where the Secrets Manager key resides.</li></ul></td></tr><tr><td><strong>Bucket Name</strong><sup>1</sup></td><td><p>Enter the name of the Amazon S3 bucket where your data resides. </p><p>For S3 access from non-EMR environments, Data Catalog uses the AWS Command Line Interface (CLI) to connect to S3 using your access credentials (Access Key and Secret Access Key).</p><p>If you are connecting to <strong>Hadoop Distributed File System (HDFS)</strong> or <strong>MapR</strong>, provide the logical root directory name defined in the <code>hdfssite.xml</code> configuration file using the <code>dfs.nameservices</code> property.</p><p>For MapR file systems, identify the root using the <code>maprfs:///</code> URI scheme.</p></td></tr><tr><td><strong>Access Key</strong><sup>3</sup></td><td><p>User credentials to access data on the bucket.</p><ul><li>If connecting <strong>directly to S3</strong>, this key authenticates your access to the S3 bucket.</li><li>If using <strong>Secrets Manager</strong>, this key authenticates your access to the Secrets Manager key so you can retrieve the S3 bucket credentials.</li></ul></td></tr><tr><td><strong>Secret Access Key</strong><sup>3</sup></td><td><p>Password credential to access data on the bucket.</p><ul><li>If connecting directly to S3, this key authenticates your access to the S3 bucket.</li><li>If using <strong>Secrets Manager</strong>, this key authenticates your access to the Secrets Manager key so you can retrieve the S3 bucket credentials.</li></ul></td></tr><tr><td><strong>Secret Manager Key</strong><sup>2</sup></td><td>Name of the AWS Secrets Manager key to retrieve the credentials securely, instead of specifying them here.</td></tr><tr><td><strong>AWS role</strong></td><td>ARN of the AWS IAM Role to assume when accessing the S3 bucket, allowing cross-account or role-based access.</td></tr><tr><td><strong>Endpoint</strong></td><td>Location of the bucket. For example, <code>s3.&#x3C;region containing S3 bucket>.amazonaws.com</code></td></tr><tr><td><strong>Path</strong></td><td>The directory where this data source is included.</td></tr></tbody></table>

   \ <sup>1</sup> These fields are mandatory.\ <sup>2</sup> When using Secrets Manager, you must provide:\
    • the **Region** where the Secrets Manager key resides\
    • the **Secret Manager Key**\
    • and the **Access Key** and **Secret Access Key** (to retrieve the S3 bucket credentials from Secrets Manager). In this case, the access keys authenticate your access to Secrets Manager, not directly to the S3 bucket.\ <sup>3</sup> When not using Secrets Manager, you must provide the **Access Key** and **Secret Access Key** to access the S3 bucket directly.
6. (Optional) Select **Skip SSL validation** if the data source uses a self-signed SSL certificate and you do not want to import the certificate into Data Catalog.\
   This option bypasses SSL certificate validation for the data source. Although supported in any environment, it is not recommended for production use. To enable SSL validation, import the self-signed certificate into Data Catalog. For more information, see *Install user-provided SSL certificates.*
7. Click **Test Connection** to test your connection to the specified data source.
8. Click **Scan Files**. \
   The **Scan Files** dialog box appears. Here you can refine metadata ingestion using the following options.&#x20;

   1. **Delete Empty Folders**: When selected, it deletes folders without any child entities from the Data Catalog metadata store. This option is intended only for full metadata scans.
   2. **Incremental Ingest**: Ingests data for filesystems or object stores where files or objects **created** or **modified** **time stamps** match the time period selected. This doesn't remove any existing data from previous ingests and can be used when you only want to ingest data from a particular timeframe. Available time periods are (Last) **12 Hours**, **24 Hours**, **1 Week**, **1 Month,** and **3 Months**.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>You cannot select <strong>Delete Empty Folders</strong> and <strong>Incremental Ingest</strong> at the same time. The <strong>Delete Empty Folders</strong> option applies only to full metadata scans and is not supported for incremental ingest operations.</p></div>
   3. **Include and Exclude Patterns:** This feature enables you to specify which folders or files should be scanned or excluded. By applying these filters, you can shorten scan duration and control the scope of metadata ingestion. For more information, see the feature walkthrough [Include or exclude patterns](https://hitachi-vantara.navattic.com/9ai0dle?g=cmfw350z4000004kzb74neovt\&s=0).

   This process loads files and folders into the system. You can monitor the status of the file scan on the **Workers** page.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a message will appear in the upper corner of the screen.</p></div>
9. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
10. (Optional) Configure the following storage optimization options for the data source.

    **Note:** To use storage optimization options, you need a Pentaho Data Optimizer license.

    | Field                       | Description                                                                                                                            |
    | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
    | **Available for Migration** | Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities. |
    | **Available for Writing**   | Enables or disables writing capabilities for the data source and enables migration when turned on.                                     |
11. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
12. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
13. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
14. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the AWS S3 data source.

<details>

<summary><strong>Feature walkthrough: Support for Secret Manager</strong></summary>

▶️ [Launch the Support for Secret Manager walkthrough](https://hitachi-vantara.navattic.com/sja09sn)&#x20;

This interactive walkthrough demonstrates how to configure **Secret Manager** in Pentaho Data Catalog.\
It covers:

* Storing and managing sensitive credentials in Secret Manager
* Configuring PDC to securely fetch these credentials for AWS S3 and other data sources
* Reducing manual handling of secrets during data source setup

</details>

## Azure Blob Storage data source

Perform the following steps to add Azure Blob Storage as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Azure Blob Storage** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="215.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>The <strong>Default</strong> setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td><strong>Shared Key</strong> (default)</td></tr><tr><td><strong>Account Name</strong></td><td>Name of an Azure storage account contains all of your Azure Storage data objects.</td></tr><tr><td><strong>Shared Key</strong></td><td>A password-like credential that gives full access to an Azure storage account's data and configuration.</td></tr><tr><td><strong>Container</strong></td><td>The top-level object that logically groups blob data that holds an unlimited number of large object data.</td></tr><tr><td><strong>Path</strong></td><td>Folder where this data source is included.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.
7. Click **Scan Files**. \
   The **Scan Files** dialog box appears. Here you can refine metadata ingestion using the following options.&#x20;

   1. **Delete Empty Folders**: When selected, it deletes folders without any child entities from the Data Catalog metadata store. This option is intended only for full metadata scans.
   2. **Incremental Ingest**: Ingests data for filesystems or object stores where files or objects **created** or **modified** **time stamps** match the time period selected. This doesn't remove any existing data from previous ingests and can be used when you only want to ingest data from a particular timeframe. Available time periods are (Last) **12 Hours**, **24 Hours**, **1 Week**, **1 Month,** and **3 Months**.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>You cannot select <strong>Delete Empty Folders</strong> and <strong>Incremental Ingest</strong> at the same time. The <strong>Delete Empty Folders</strong> option applies only to full metadata scans and is not supported for incremental ingest operations.</p></div>
   3. **Include and Exclude Patterns:** This feature enables you to specify which folders or files should be scanned or excluded. By applying these filters, you can shorten scan duration and control the scope of metadata ingestion. For more information, see the feature walkthrough [Include or exclude patterns](https://hitachi-vantara.navattic.com/9ai0dle?g=cmfw350z4000004kzb74neovt\&s=0).

   This process loads files and folders into the system. You can monitor the status of the file scan on the **Workers** page.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a message will appear in the upper corner of the screen.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   **Note:** To use storage optimization options, you need a Pentaho Data Optimizer license.

   <table><thead><tr><th width="224.4444580078125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.
14. Specify the following additional connection information.

    <table><thead><tr><th width="215.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>The <strong>Default</strong> setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td><strong>Shared Key</strong> (default)</td></tr><tr><td><strong>Account Name</strong></td><td>Name of an Azure storage account contains all of your Azure Storage data objects.</td></tr><tr><td><strong>Shared Key</strong></td><td>A password-like credential that gives full access to an Azure storage account's data and configuration.</td></tr><tr><td><strong>Container</strong></td><td>The top-level object that logically groups blob data that holds an unlimited number of large object data.</td></tr><tr><td><strong>Path</strong></td><td>Folder where this data source is included.</td></tr></tbody></table>
15. Click **Test Connection** to test your connection to the specified data source.

You have successfully created the connection to the Azure Blob Storage data source.

## Databricks data source

You can configure Databricks as a data source in Data Catalog to discover, catalog, and govern data stored in Databricks SQL warehouses and the underlying Delta Lake storage layer. This integration enables Pentaho Data Catalog to connect to Databricks using JDBC and ingest metadata for data identification, profiling, and governance. By adding Databricks as a data source, organizations gain centralized visibility into Databricks-managed data and can support governed analytics, machine learning, and AI workflows across structured, semi-structured, unstructured, and streaming data.

Perform the following steps to add Databricks as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

> ▶️ **Watch a walkthrough**
>
> You can watch a guided walkthrough that demonstrates [how to configure a Databricks data source in Pentaho Data Catalog](https://assets.demos.hitachivantara.com/psl/mqz04ro).
>
> {% embed url="<https://assets.demos.hitachivantara.com/psl/mqz04ro>" %}

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.

2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>

3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>

4. After you have specified the basic connection information, select **Databricks** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.

5. Specify the following additional connection information.

   <table><thead><tr><th width="227.3333740234375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration method</strong></td><td>The method is used to configure the connection. The only option is <strong>Credentials</strong>.</td></tr><tr><td><strong>Driver</strong></td><td>Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.To upload a new driver, click <strong>Manage Drivers</strong>, and click <strong>Add New</strong>, upload the driver, and then click <strong>Add Driver</strong>.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The Java class name corresponding to the selected Databricks driver. </td></tr><tr><td><strong>Host</strong></td><td>The Databricks workspace hostname. This value identifies the Databricks compute resource. Example: <code>https://dbc-xxxx.cloud.databricks.com</code>.</td></tr><tr><td><strong>Port</strong></td><td>The port used to connect to the Databricks workspace.</td></tr><tr><td><strong>Path</strong></td><td>The HTTP path of the Databricks SQL warehouse. Pentaho Data Catalog appends this value to the host and port to form the JDBC connection URL. Example: <code>/sql/1.0/warehouses/&#x3C;warehouse-id></code>.</td></tr><tr><td><strong>Catalog name</strong></td><td>A user-defined name to identify the Databricks data source within Pentaho Data Catalog.</td></tr><tr><td><strong>Personal access token</strong></td><td>A Databricks personal access token (PAT) used to authenticate the connection. The token must have permission to access the specified SQL warehouse.</td></tr></tbody></table>

6. Click **Test Connection** to test your connection to the specified data source. \
   A **Test Connection** confirmation message window opens.

7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens.
   1. You can search and select schemas using the search bar at the top (starts with or using regular expressions), then click **Next**.
   2. On the **Ingest Schema** dialog box, add include or exclude patterns to filter the tables to be ingested, and then click Ingest to load the database schema and related metadata.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting specific system-related schemas that are unnecessary for your needs.</p></div>

8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.

9. (Optional) Configure the following storage optimization options for the data source.

   **Note:** To utilize storage optimization options, a Pentaho Data Optimizer license is required.

   <table><thead><tr><th width="251.1112060546875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>

10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.

11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.

12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.

13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the Databricks data source.

## Denodo data source

Perform the following steps to add Denodo as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Denodo** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="227.3333740234375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration method</strong></td><td>By default, it is a <strong>URI</strong>, as the connection is configured using a URL.</td></tr><tr><td><strong>Driver</strong></td><td>Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.To upload a new driver, click <strong>Manage Drivers</strong>, and click <strong>Add New</strong>, upload the driver, and then click <strong>Add Driver</strong>.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The Java class name corresponding to the selected Denodo driver. </td></tr><tr><td><strong>User Name</strong></td><td>The username required to authenticate to the Denodo environment. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password associated with the Denodo user account. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains the Denodo connection credentials. When this field is provided, Data Catalog securely retrieves credentials from Secret Manager, eliminating the need to enter the username and password manually.</td></tr><tr><td><strong>Region</strong></td><td>The region where the Denodo secret is stored in Secret Manager. Data Catalog uses this region to connect to the correct Secret Manager endpoint.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secret versions from Secret Manager. The role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>URI</strong></td><td>URIs are used to access and manage various objects and services within the Denodo environment. For example, the URI would look like <code>jdbc:vdb://&#x3C;denodo-host>:&#x3C;port>/&#x3C;database-name>?publishCatalogsAsSchemas=true</code><br>Example: <code>jdbc:vdb://ec2-1-2-3-4.compute-1.amazonaws.com:49999/mydatabase?publishCatalogsAsSchemas=true</code></td></tr><tr><td><strong>Database Name</strong></td><td>The name of the data sources within the Denodo environment that contain the data you want to access.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before finalizing and saving your new data source configuration, you must perform a process called 'Scan files'. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas in the search bar at the top, using starts-with or regular expressions. Once you have located the relevant schemas, select the schemas and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting specific system-related schemas that are unnecessary for your needs. </p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   **Note:** To utilize storage optimization options, a Pentaho Data Optimizer license is required.

   <table><thead><tr><th width="251.1112060546875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the Denodo data source.

## DynamoDB data source

Perform the following steps to add Amazon DynamoDB as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Active Directory** in the **Data Source Type** field.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.</p></div>
5. Specify the following additional connection information.

   <table><thead><tr><th width="172.88885498046875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Region</strong></td><td>Geographical location where AWS maintains a cluster of data centers.</td></tr><tr><td><strong>Access Key</strong> and <strong>Secret Access Key</strong></td><td>AWS Access Key ID and Secret Access Key that are used for authentication and authorization when interacting with DynamoDB.</td></tr><tr><td><strong>Role</strong></td><td>The AWS IAM Role that the Pentaho Data Catalog assumes to access DynamoDB securely. Use this field when authentication is performed through AWS IAM Role-based access instead of (or in addition to) Access Key credentials.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.jkljk
7. Click **Scan Files**. \
   The **Scan Files** dialog box appears. Here you can refine metadata ingestion using the following options.&#x20;

   1. **Delete Empty Folders**: When selected, it deletes folders without any child entities from the Data Catalog metadata store. This option is intended only for full metadata scans.
   2. **Incremental Ingest**: Ingests data for filesystems or object stores where files or objects **created** or **modified** **time stamps** match the time period selected. This doesn't remove any existing data from previous ingests and can be used when you only want to ingest data from a particular timeframe. Available time periods are (Last) **12 Hours**, **24 Hours**, **1 Week**, **1 Month,** and **3 Months**.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>You cannot select <strong>Delete Empty Folders</strong> and <strong>Incremental Ingest</strong> at the same time. The <strong>Delete Empty Folders</strong> option applies only to full metadata scans and is not supported for incremental ingest operations.</p></div>
   3. **Include and Exclude Patterns:** This feature enables you to specify which folders or files should be scanned or excluded. By applying these filters, you can shorten scan duration and control the scope of metadata ingestion. For more information, see the feature walkthrough [Include or exclude patterns](https://hitachi-vantara.navattic.com/9ai0dle?g=cmfw350z4000004kzb74neovt\&s=0).

   This process loads files and folders into the system. You can monitor the status of the file scan on the **Workers** page.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a message will appear in the upper corner of the screen.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="212.2222900390625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created the connection to the Amazon DynamoDB data source.

## Google Cloud Storage data source

Google Cloud Storage (GCS) is a storage service that enables the storage, retrieval, and management of unstructured data, including files, images, videos, and large datasets. By integrating GCS as a data source within Data Catalog, you can access and manage the metadata of files stored. You can perform data discovery to search, explore, and understand your Google Cloud Storage data. Additionally, it enhances data lineage and compliance by providing detailed tracking of data movements.

Perform the following steps to add Google Cloud Storage as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Google Object Store** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="239">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Bucket Name</strong></td><td>The name of the Google Cloud Storage bucket in which the data resides.</td></tr><tr><td><strong>Path</strong></td><td>The path within the bucket where the files are stored.</td></tr><tr><td><strong>Key Path</strong></td><td>The authentication key file, which is used to connect to Google Cloud Storage (a JSON file).</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.
7. Click **Scan Files**. \
   The **Scan Files** dialog box appears. Here you can refine metadata ingestion using the following options.&#x20;

   1. **Delete Empty Folders**: When selected, it deletes folders without any child entities from the Data Catalog metadata store. This option is intended only for full metadata scans.
   2. **Incremental Ingest**: Ingests data for filesystems or object stores where files or objects **created** or **modified** **time stamps** match the time period selected. This doesn't remove any existing data from previous ingests and can be used when you only want to ingest data from a particular timeframe. Available time periods are (Last) **12 Hours**, **24 Hours**, **1 Week**, **1 Month,** and **3 Months**.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>You cannot select <strong>Delete Empty Folders</strong> and <strong>Incremental Ingest</strong> at the same time. The <strong>Delete Empty Folders</strong> option applies only to full metadata scans and is not supported for incremental ingest operations.</p></div>
   3. **Include and Exclude Patterns:** This feature enables you to specify which folders or files should be scanned or excluded. By applying these filters, you can shorten scan duration and control the scope of metadata ingestion. For more information, see the feature walkthrough [Include or exclude patterns](https://hitachi-vantara.navattic.com/9ai0dle?g=cmfw350z4000004kzb74neovt\&s=0).

   This process loads files and folders into the system. You can monitor the status of the file scan on the **Workers** page.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a message will appear in the upper corner of the screen.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="213.3333740234375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to Google Cloud Storage as a data source in Data Catalog.

## Google BigQuery data source

Google BigQuery is a serverless, highly scalable, and cost-effective multi-cloud data warehouse designed for analytics. Integrating BigQuery as a data source within Data Catalog, you can access and manage metadata from the BigQuery database. It enables data discovery to search, explore, and understand BigQuery data. Additionally, it enhances data lineage and compliance by providing detailed tracking of data movements.

Perform the following steps to add BigQuery as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Google BigQuery** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="156.22222900390625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Driver</strong></td><td><p>The standard used to establish communication between the application and the database.Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.</p><p>To upload a new driver, click <strong>Manage Drivers</strong>, and click <strong>Add New</strong>, upload the driver, and then click <strong>Add Driver</strong>.</p></td></tr><tr><td><strong>Host</strong></td><td>The Google BigQuery API endpoint. By default, the host is set to <code>https://www.googleapis.com/bigquery/v2</code>, which communicates with BigQuery's REST API for data processing.</td></tr><tr><td><strong>Port</strong></td><td>The port number to connect to the BigQuery data source. The default port for HTTPS connections is <code>443</code>.</td></tr><tr><td><strong>Project</strong></td><td>The Google Cloud project ID that contains the BigQuery datasets you want to access.</td></tr><tr><td><strong>Database Name</strong></td><td>The name of the dataset within the BigQuery that you want to connect with.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name of the secret stored in Secret Manager that contains your Google Cloud service account key (in JSON format). When provided, Data Catalog retrieves the key securely from Secret Manager instead of using a local key file.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants access to read secret versions from Secret Manager. This role must include permissions such as <code>secretmanager.versions.access</code> so that Data Catalog can retrieve the service account key.</td></tr><tr><td><strong>Region</strong></td><td>The region where the secret is stored in Secret Manager. Data Catalog uses this region to connect to the correct Secret Manager endpoint.</td></tr><tr><td><strong>Key Path</strong></td><td>The file path to your Google Cloud service account's key (a JSON file).</td></tr><tr><td><strong>Oauth Type</strong></td><td>The authentication method to connect to BigQuery. By default, it is <strong>Service-based</strong>. It uses a service account and a key file for authentication.</td></tr><tr><td><strong>Client Email</strong></td><td>The email associated with your Google Cloud service account for service-based OAuth. The service account email is usually in the format <code>your-service-account@your-project-id.iam.gserviceaccount.com</code>.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before you finalize and save your new data source configuration, you need to perform a process called <strong>Scan files</strong>. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To utilize storage optimization options, a Pentaho Data Optimizer license is required. </p></div>

   <table><thead><tr><th width="254.4444580078125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.
14. Specify the following additional connection information.

    <table><thead><tr><th width="156.22222900390625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Driver</strong></td><td><p>The standard used to establish communication between the application and the database.Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.</p><p>To upload a new driver, click <strong>Manage Drivers</strong>, and click <strong>Add New</strong>, upload the driver, and then click <strong>Add Driver</strong>.</p></td></tr><tr><td><strong>Host</strong></td><td>The Google BigQuery API endpoint. By default, the host is set to <code>https://www.googleapis.com/bigquery/v2</code>, which communicates with BigQuery's REST API for data processing.</td></tr><tr><td><strong>Port</strong></td><td>The port number to connect to the BigQuery data source. The default port for HTTPS connections is <code>443</code>.</td></tr><tr><td><strong>Project</strong></td><td>The Google Cloud project ID that contains the BigQuery datasets you want to access.</td></tr><tr><td><strong>Database Name</strong></td><td>The name of the dataset within the BigQuery that you want to connect with.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name of the secret stored in Secret Manager that contains your Google Cloud service account key (in JSON format). When provided, Data Catalog retrieves the key securely from Secret Manager instead of using a local key file.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants access to read secret versions from Secret Manager. This role must include permissions such as <code>secretmanager.versions.access</code> so that Data Catalog can retrieve the service account key.</td></tr><tr><td><strong>Region</strong></td><td>The region where the secret is stored in Secret Manager. Data Catalog uses this region to connect to the correct Secret Manager endpoint.</td></tr><tr><td><strong>Key Path</strong></td><td>The file path to your Google Cloud service account's key (a JSON file).</td></tr><tr><td><strong>Oauth Type</strong></td><td>The authentication method to connect to BigQuery. By default, it is <strong>Service-based</strong>. It uses a service account and a key file for authentication.</td></tr><tr><td><strong>Client Email</strong></td><td>The email associated with your Google Cloud service account for service-based OAuth. The service account email is usually in the format <code>your-service-account@your-project-id.iam.gserviceaccount.com</code>.</td></tr></tbody></table>
15. Click **Test Connection** to test your connection to the specified data source.\
    A Test Connection confirmation message window opens.\
    **Note:** Before you finalize and save your new data source configuration, you need to perform a process called **Scan files**. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.
16. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas, and then click **Ingest** to load the database schema and related metadata.\
    **Note**: Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.
17. (Optional) In the **Physical Location** field, specify the physical location details of the data source.

You have successfully created a connection to the BigQuery data source.

## HCP data source

You can add data to Data Catalog from Hitachi Content Platform (HCP) by adding HCP as data source. Perform the following steps to add HCP as data source:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **HCP** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="171.77777099609375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Region</strong></td><td>Geographical location where HCP maintains data centers.</td></tr><tr><td><strong>Endpoint</strong></td><td>Location of the bucket. hostname or IP address</td></tr><tr><td><strong>Access Key</strong></td><td>The access key of the S3 credentials to access the bucket.</td></tr><tr><td><strong>Secret Access Key</strong></td><td>The secret key of the S3 credentials to access the bucket.</td></tr><tr><td><strong>Bucket Name</strong></td><td>The name of the S3 bucket in which the data resides.</td></tr><tr><td><strong>Path</strong></td><td>Directory where this data source is included.</td></tr></tbody></table>
6. (Optional) Select **Skip SSL validation** if the data source uses a self-signed SSL certificate and you do not want to import the certificate into Data Catalog.\
   This option bypasses SSL certificate validation for the data source. Although supported in any environment, it is not recommended for production use. To enable SSL validation, import the self-signed certificate into Data Catalog. For more information, see *Install user-provided SSL certificates.*
7. Click **Test Connection** to test your connection to the specified data source.
8. Click **Scan Files**. \
   The **Scan Files** dialog box appears. Here you can refine metadata ingestion using the following options.&#x20;

   1. **Delete Empty Folders**: When selected, it deletes folders without any child entities from the Data Catalog metadata store. This option is intended only for full metadata scans.
   2. **Incremental Ingest**: Ingests data for filesystems or object stores where files or objects **created** or **modified** **time stamps** match the time period selected. This doesn't remove any existing data from previous ingests and can be used when you only want to ingest data from a particular timeframe. Available time periods are (Last) **12 Hours**, **24 Hours**, **1 Week**, **1 Month,** and **3 Months**.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>You cannot select <strong>Delete Empty Folders</strong> and <strong>Incremental Ingest</strong> at the same time. The <strong>Delete Empty Folders</strong> option applies only to full metadata scans and is not supported for incremental ingest operations.</p></div>
   3. **Include and Exclude Patterns:** This feature enables you to specify which folders or files should be scanned or excluded. By applying these filters, you can shorten scan duration and control the scope of metadata ingestion. For more information, see the feature walkthrough [Include or exclude patterns](https://hitachi-vantara.navattic.com/9ai0dle?g=cmfw350z4000004kzb74neovt\&s=0).

   This process loads files and folders into the system. You can monitor the status of the file scan on the **Workers** page.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a message will appear in the upper corner of the screen.</p></div>
9. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
10. (Optional) Configure the following storage optimization options for the data source.

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license. </p></div>

    <table><thead><tr><th width="221.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr></tbody></table>
11. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
12. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
13. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
14. Click **Create Data Source** to establish your data source connection.

You have successfully created the connection to the HCP data source.

## HDFS data source

Hadoop Distributed File System (HDFS) is a scalable, fault-tolerant storage system for big data, designed to distribute and manage large datasets across a cluster of commodity hardware within the Apache Hadoop framework. You can create a data source using HDFS with the local file system path by mounting data as a local file system to either the remote or local worker.

The HDFS protocol uses a client-server model where the server provides the shared file system, and the client mounts the file system to access the shared files as if they were on a local disk. You can add data to Data Catalog from any file-sharing network system if it is transferable using HDFS.

Perform the following steps to add HDFS as a data source:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, specify the following additional connection information to access the HDFS data source.

   <table><thead><tr><th width="225.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td>By default, it is <strong>URI</strong>.</td></tr><tr><td><strong>HDFS Version</strong></td><td>Select the Hadoop version of the cluster that you want to run.</td></tr><tr><td><strong>URI</strong></td><td>URIs are used to identify and locate resources on the internet or within a network. For example, the URI would look like <code>hdfs://&#x3C;name node>:8020</code>. The <code>&#x3C;name node></code> address can be a variable name for high availability.</td></tr><tr><td><strong>Path</strong></td><td>HDFS directory path for the data source. It can be the root (/) or a specific high-level directory based on your access control needs. For example, the path would look like <code>/user/demodata/</code>.</td></tr><tr><td><strong>Credential Type</strong></td><td>Select the credential type to connect to the HDFS data source.</td></tr></tbody></table>
5. Click **Test Connection** to test your connection to the specified data source.
6. Click **Scan Files**. \
   The **Scan Files** dialog box appears. Here you can refine metadata ingestion using the following options.&#x20;

   1. **Delete Empty Folders**: When selected, it deletes folders without any child entities from the Data Catalog metadata store. This option is intended only for full metadata scans.
   2. **Incremental Ingest**: Ingests data for filesystems or object stores where files or objects **created** or **modified** **time stamps** match the time period selected. This doesn't remove any existing data from previous ingests and can be used when you only want to ingest data from a particular timeframe. Available time periods are (Last) **12 Hours**, **24 Hours**, **1 Week**, **1 Month,** and **3 Months**.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>You cannot select <strong>Delete Empty Folders</strong> and <strong>Incremental Ingest</strong> at the same time. The <strong>Delete Empty Folders</strong> option applies only to full metadata scans and is not supported for incremental ingest operations.</p></div>
   3. **Include and Exclude Patterns:** This feature enables you to specify which folders or files should be scanned or excluded. By applying these filters, you can shorten scan duration and control the scope of metadata ingestion. For more information, see the feature walkthrough [Include or exclude patterns](https://hitachi-vantara.navattic.com/9ai0dle?g=cmfw350z4000004kzb74neovt\&s=0).

   This process loads files and folders into the system. You can monitor the status of the file scan on the **Workers** page.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a message will appear in the upper corner of the screen.</p></div>
7. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
8. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="214.4444580078125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr></tbody></table>
9. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
10. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
11. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
12. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the HDFS data source.

## IBM Db2 data source

Perform the following steps to add IBM Db2 as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the connection information, select **IBM DB2** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="258.4444580078125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td>Select <strong>Credentials</strong>, or <strong>URI</strong> as a configuration method.</td></tr><tr><td><strong>Driver</strong></td><td>If you select a configuration method of Credentials or URI, you must use the driver. Select an existing driver or upload a new one to ensure that communication between the application and the database is efficient, secure, and compliant with the required standards.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The Java class name corresponding to the selected driver.</td></tr><tr><td><strong>User Name</strong></td><td>The username required to authenticate to the IBM Db2 database. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password required to authenticate to the IBM Db2 database. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains the IBM Db2 credentials (username and password). When provided, Data Catalog retrieves credentials securely from Secret Manager instead of requiring manual entry.</td></tr><tr><td><strong>Region</strong></td><td>The region where the secret is stored in Secret Manager. Data Catalog uses this region to access the correct Secret Manager endpoint.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secrets from Secret Manager. The role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Host</strong><br>(only for the <strong>Credential</strong> method)</td><td>The address of the machine where the IBM Db2 database server is running. It can be an IP address or a domain name.</td></tr><tr><td><strong>Port</strong><br>(only for the <strong>Credential</strong> method)</td><td>The port number on which the IBM Db2 server is listening for incoming connections.</td></tr><tr><td><strong>URI</strong><br>(only for <strong>URI</strong> method)</td><td>URIs are used to access and manage various objects and services within the IBM Db2 environment. For example, the URL would look like <code>jdbc:db2://&#x3C;HOSTNAME or IP_ADDRESS>:&#x3C;PORT>/&#x3C;DATABASE_NAME></code>.</td></tr><tr><td><strong>Database Name</strong></td><td>The name of the database within the IBM Db2 server that you want to connect with.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, with options including 'starts with' or regular expressions. Once you have located the relevant schemas, select the schemas, and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting specific system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To utilize storage optimization options, a Pentaho Data Optimizer license is required.</p></div>

   <table><thead><tr><th width="261.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created the connection to the IBM Db2 data source.

## InfluxDB data source

InfluxDB is a time-series database designed for handling high volumes of time-stamped data, such as monitoring, IoT applications, real-time analytics, and event-driven architectures. By integrating InfluxDB as a data source within Data Catalog, you can manage and utilize time-series data. It enables data discovery to search, explore, and understand InfluxDB data. Additionally, it enhances data lineage and compliance by providing detailed tracking of data movements.

Perform the following steps to add InfluxDB as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **InfluxDB** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="204.00006103515625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration method</strong></td><td>The method is used to configure the connection. The only option is <strong>Credentials</strong>.</td></tr><tr><td><strong>Driver</strong></td><td>The standard used to establish communication between the application and the database. Select <strong>Default</strong>, which is an existing driver, to ensure that communication between the application and the database is efficient, secure, and compliant with the required standards.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The Java class name associated with the selected InfluxDB driver.</td></tr><tr><td><strong>Host</strong></td><td>The address of the machine where the InfluxDB database server is running. It can be an IP address or a domain name.</td></tr><tr><td><strong>Port</strong></td><td>The port number to connect to the InfluxDB data source.</td></tr><tr><td><strong>Username</strong></td><td>User name that provide access to the InfluxDB database.</td></tr><tr><td><strong>Token</strong></td><td>The authentication token provided by the InfluxDB instance to authenticate and authorize access to the specified data source.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains the InfluxDB credentials (username and token). When provided, Data Catalog securely retrieves the credentials from Secret Manager, eliminating the need to manually enter the username and token.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that permits Data Catalog to read secret versions from Secret Manager. The role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the InfluxDB secret is stored in Secret Manager. Data Catalog uses this region to access the correct Secret Manager endpoint.</td></tr><tr><td><strong>Bucket Name</strong></td><td>The name of the bucket in the InfluxDB instance that contains the data you want to connect with.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before finalizing and saving your new data source configuration, you must perform a process called 'Scan files'. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** \
   The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using the 'starts with' or regular expressions. Once you have located the relevant schemas, select the schemas and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p> Although you can select all schemas, it is a best practice to avoid selecting specific system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To utilize storage optimization options, a Pentaho Data Optimizer license is required.</p></div>

   <table><thead><tr><th width="245.5556640625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the InfluxDB as a data source.

## Local File System data source

You can add data to Data Catalog from your local file system by adding Local File System as a data source.

To access files on your local system, make the following changes to the `vendor/docker-compose.yml` file to ensure that it is accessible by the `ws-default` container.

1. Open the `vendor/docker-compose.yml` file and add the following lines under the `ws-default` service.

   ```
   services:
     ws-default:
       volumes:
         - /my/path/to/file:/tmp/my-path
   ```

   You can also include a remote file share as a Local File System. As an example, refer to the following code snippet for adding `cifs-share` to the Local File System.

   ```
   services:
     ws-default:
       volumes:
         - cifs-share:/cifs-share
         
         // Following are optional settings to add cifs share to local file system
         - cifs-share:/cifs-share //Remote file share
   volumes:
     cifs-share:
       driver_opts:
         type: cifs
         o: "username=<user1>,password=<password>,file_mode=0777,dir_mode=0777"
         device: "<IP Address>”

   ```
2. Save changes.
3. Restart the `ws-default` container for the changes to take effect.

Perform the following steps to identify your data source within Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Local File System** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="144">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Path</strong></td><td>Directory where this data source is included.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.
7. Click **Scan Files**. \
   The **Scan Files** dialog box appears. Here you can refine metadata ingestion using the following options.&#x20;

   1. **Delete Empty Folders**: When selected, it deletes folders without any child entities from the Data Catalog metadata store. This option is intended only for full metadata scans.
   2. **Incremental Ingest**: Ingests data for filesystems or object stores where files or objects **created** or **modified** **time stamps** match the time period selected. This doesn't remove any existing data from previous ingests and can be used when you only want to ingest data from a particular timeframe. Available time periods are (Last) **12 Hours**, **24 Hours**, **1 Week**, **1 Month,** and **3 Months**.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>You cannot select <strong>Delete Empty Folders</strong> and <strong>Incremental Ingest</strong> at the same time. The <strong>Delete Empty Folders</strong> option applies only to full metadata scans and is not supported for incremental ingest operations.</p></div>
   3. **Include and Exclude Patterns:** This feature enables you to specify which folders or files should be scanned or excluded. By applying these filters, you can shorten scan duration and control the scope of metadata ingestion. For more information, see the feature walkthrough [Include or exclude patterns](https://hitachi-vantara.navattic.com/9ai0dle?g=cmfw350z4000004kzb74neovt\&s=0).

   This process loads files and folders into the system. You can monitor the status of the file scan on the **Workers** page.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a message will appear in the upper corner of the screen.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="204.4444580078125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the local file system as a data source.

## MariaDB data source

MariaDB is an open-source relational database management system (RDBMS) that is a fork of MySQL. Perform the following steps to configure the MariaDB data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the connection information, select **MariaDB** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="230.6666259765625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>The default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td>By default it is <strong>Credentials</strong>.</td></tr><tr><td><strong>Driver</strong></td><td>If you are selecting configuration method as Credentials or URI, then you must use the driver. Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The Java class name associated with the selected MariaDB driver. </td></tr><tr><td><strong>User Name</strong></td><td>The username that provides access to the MariaDB database. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password associated with the MariaDB user account. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains the MariaDB credentials (username and password). When provided, Data Catalog securely retrieves the credentials from Secret Manager instead of requiring manual entry.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secrets from Secret Manager. The role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the MariaDB secret is stored in Secret Manager. Data Catalog uses this region to access the correct Secret Manager endpoint.</td></tr><tr><td><strong>Host</strong></td><td>The address of the machine where the MariaDB database server is running. It can be an IP address or a domain name.</td></tr><tr><td><strong>Port</strong></td><td>The port number on which the MariaDB server is listening for incoming connections.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using the 'starts with' or regular expressions. Once you have located the relevant schemas, select the schemas and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting specific system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To utilize storage optimization options, a Pentaho Data Optimizer license is required.</p></div>

   <table><thead><tr><th width="220">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created the connection to the MariaDB data source.

## Microsoft Access data source

Perform the following steps to add Microsoft Access as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Microsoft Access** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="295.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td>Select <strong>Credentials</strong> or <strong>URI</strong> as the configuration method.</td></tr><tr><td><strong>Driver</strong></td><td>Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.To upload a new driver, click <strong>Manage Drivers</strong>, and click <strong>Add New</strong>, upload the driver, and then click <strong>Add Driver</strong>.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The Java class name associated with the selected Microsoft Access driver.</td></tr><tr><td><strong>User Name</strong></td><td>The username used to authenticate to the Microsoft Access database. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password used to authenticate to the Microsoft Access database. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains the Microsoft Access credentials (username and password). When provided, Data Catalog retrieves the credentials securely from Secret Manager instead of requiring manual entry.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secrets from Secret Manager. The role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the Microsoft Access credentials are stored in Secret Manager. Data Catalog uses this region to connect to the correct Secret Manager endpoint.</td></tr><tr><td><strong>Database File</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The Microsoft Access database file (<code>.mdb</code> or <code>.accdb</code>) to connect to.</td></tr><tr><td><strong>URI</strong><br>(Only for the <strong>URI</strong> method)</td><td>The JDBC URI string used to connect to the Access database.<br>For example, URL would look like <code>jdbc: postgresql://localhost:&#x3C;port_no>/</code>.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before you finalize and save your new data source configuration, you need to perform a process called <strong>Scan files</strong>. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas, and then click **Ingest** to load the database schema and related metadata.\
   **Note:** Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   **Note:** To use storage optimization options, you need a Pentaho Data Optimizer license.

   <table><thead><tr><th width="217.7777099609375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the Microsoft Access data source.

## Microsoft SQL Server data source

Perform the following steps to add Microsoft SQL Server as a data source Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Microsoft SQL Server** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="245.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration method</strong></td><td>Select <strong>Credentials</strong> or <strong>URI</strong> as a configuration method.</td></tr><tr><td><strong>Driver</strong></td><td>Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.<br>To upload a new driver, click <strong>Manage Drivers</strong>, click <strong>Add New</strong>, upload the driver, and click <strong>Add Driver</strong>.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The fully qualified Java class name of the JDBC driver.</td></tr><tr><td><strong>User Name</strong></td><td>The username used to authenticate to the Microsoft SQL Server database. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password associated with the specified SQL Server username. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains SQL Server credentials (username and password). When provided, Data Catalog retrieves credentials securely from Secret Manager, eliminating the need for manual credential entry.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secret versions from Secret Manager. The role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the SQL Server credentials are stored in Secret Manager. Data Catalog uses this region to access the appropriate Secret Manager endpoint.</td></tr><tr><td><strong>Host</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The address of the machine where the Microsoft SQL database server is running. It can be an IP address or a domain name.</td></tr><tr><td><strong>Port</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The port number on which the Microsoft SQL server is listening for incoming connections. The default port is 5432.</td></tr><tr><td><strong>URI</strong><br>(Only for the <strong>URI</strong> method)</td><td>The connection string used to connect to the SQL Server database. The URI must include the server address, database name, and any required parameters.<br>For example, URL would look like: <code>Server=myServerAddress;Database=myDatabase;User Id=myUsername;Password=myPassword;Port=1433;Integrated Security=False;Connection Timeout=30;</code>.</td></tr><tr><td><strong>Database Name</strong></td><td>The name of the database within the Microsoft SQL server that you want to connect with.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before you finalize and save your new data source configuration, you need to perform a process called <strong>Scan files</strong>. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="252.2222900390625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the Microsoft SQL Server data source.

## MySQL data source

Perform the following steps to add MySQL as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **MySQL** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="221.7777099609375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This setting specifies which agents should be associated with the data source in a multi-agent deployment. The only option is Default.</td></tr><tr><td><strong>Configuration method</strong></td><td>The method used to configure the connection. Select <strong>Credentials</strong> or <strong>URI</strong>.</td></tr><tr><td><strong>Driver</strong></td><td><p>The standard used to establish communication between the application and the database.</p><p>Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.</p><p>To upload a new driver, click <strong>Manage Drivers</strong>, and click <strong>Add New</strong>, upload the driver, and then click <strong>Add Driver</strong>.</p></td></tr><tr><td><strong>Driver Class Name</strong></td><td>The fully qualified Java class name of the JDBC driver.</td></tr><tr><td><strong>User Name</strong></td><td>The username that provides access to the specified MySQL database. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password associated with the specified MySQL username. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains MySQL credentials (username and password). When provided, Data Catalog retrieves these credentials securely from Secret Manager, overriding the Username and Password fields.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secrets from Secret Manager. The role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the MySQL secret is stored in Secret Manager. Data Catalog uses this region to access the correct Secret Manager endpoint.</td></tr><tr><td><strong>Host</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The address of the machine where the MySQL database server is running. It can be an IP address or a domain name.</td></tr><tr><td><strong>Port</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The port number on which the MySQL server is listening for incoming connections.</td></tr><tr><td><strong>URI</strong><br>(Only for the <strong>URI</strong> method) </td><td>The JDBC connection string to access the MySQL database. The URI must include the server address, port, database name, and any required parameters.<br>Example:<br><code>jdbc:mysql://myserver.example.com:3306/mydatabase?useSSL=false&#x26;connectTimeout=30000</code></td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before you finalize and save your new data source configuration, you need to perform a process called <strong>Scan files</strong>. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas, and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="252.2222900390625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the MySQL data source.

## NFS data source

Network File System (NFS) is a distributed file system protocol that enables remote file access over Unix and Linux networks. You can create a data source using the NFS with the local file system path by mounting data as a local file system to either the remote or local agent. Furthermore, you can easily add data to Data Catalog from Hitachi Network Attached Storage (HNAS) and NetApp data storage.

This protocol uses a client-server model where the server provides the shared file system and the client mounts the file system to access the shared files as if they were on a local disk. You can add data to the Data Catalog from any file-sharing network system if it is transferable using NFS.

Perform the following steps to add NFS as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **NFS** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="209.5555419921875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration method</strong></td><td>By default, it is a <strong>URI</strong>.</td></tr><tr><td><strong>URI</strong></td><td>URIs are used to identify and locate resources on the internet or within a network. For example, the URI would look like <code>nfs://server.example.com</code></td></tr><tr><td><strong>Path</strong></td><td>NFS path to access the data source. For example the path would look like <code>nfs:/share/data</code></td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.
7. Click **Scan Files**. \
   The **Scan Files** dialog box appears. Here you can refine metadata ingestion using the following options.&#x20;

   1. **Delete Empty Folders**: When selected, it deletes folders without any child entities from the Data Catalog metadata store. This option is intended only for full metadata scans.
   2. **Incremental Ingest**: Ingests data for filesystems or object stores where files or objects **created** or **modified** **time stamps** match the time period selected. This doesn't remove any existing data from previous ingests and can be used when you only want to ingest data from a particular timeframe. Available time periods are (Last) **12 Hours**, **24 Hours**, **1 Week**, **1 Month,** and **3 Months**.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>You cannot select <strong>Delete Empty Folders</strong> and <strong>Incremental Ingest</strong> at the same time. The <strong>Delete Empty Folders</strong> option applies only to full metadata scans and is not supported for incremental ingest operations.</p></div>
   3. **Include and Exclude Patterns:** This feature enables you to specify which folders or files should be scanned or excluded. By applying these filters, you can shorten scan duration and control the scope of metadata ingestion. For more information, see the feature walkthrough [Include or exclude patterns](https://hitachi-vantara.navattic.com/9ai0dle?g=cmfw350z4000004kzb74neovt\&s=0).

   This process loads files and folders into the system. You can monitor the status of the file scan on the **Workers** page.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a message will appear in the upper corner of the screen.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   **Note:** To use storage optimization options, you need a Pentaho Data Optimizer license.

   <table><thead><tr><th width="245.5556640625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the NFS data source.

## Okta as a data source

Okta is an identity and access management (IAM) service that helps organizations get a clear view of which users have access to which applications. By adding Okta as a data source in Data Catalog, you can automatically import a list of applications and see who is allowed to use them. This makes it easier to manage access, track ownership, and identify users who no longer need access. It also helps ensure that only authorized personnel can view and use sensitive data, supporting compliance and security goals across the organization.

### Generate Okta credentials for Data Catalog

Perform the following steps to generate the Okta credentials needed to add Okta as a data source in Data Catalog.

1. Log in to your Okta organization as a user with administrative privileges.
2. In the Admin Console, go to **Applications** > **Applications**, and then click **Create App Integration**.

   The Create a new app integration page appears.
3. Select **API Services** as the **Sign-in method**, and then click **Next**.
4. Enter a name for the PDC app integration and click **Save**.

   The app's main page appears.
5. From the service app page, select the **Okta API Scopes** tab and grant the necessary scopes:
   * `okta.apps.read`
   * `okta.groups.read`
   * `okta.users.read`
6. In the **Admin Roles** tab, assign the role **Read Only Administrator**, then click **Save Changes**.
7. In the **General** tab, edit the **Client Credentials**, set the **Client authentication** type to **Public key / Private key**, and add or generate a public/private key pair.
8. Download or copy the private key file (.pem) and note the Client ID from the saved Client Credentials section. You’ll need both when creating the data source in Data Catalog.

You have successfully generated the Okta credentials for Data Catalog.

Proceed to [add Okta as a data source](#add-okta-as-a-data-source) in Data Catalog.

### Add Okta as a data source

Perform the following steps to add Okta as a data source in Data Catalog:

**Prerequisites**

* Refer to the [**Component Reference**](https://docs.pentaho.com/pdc-admin/ldc-manage-data-sources-cp/broken-reference) section in the [**Get started with Pentaho Data Catalog**](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/uhk9gkhnIr3lLhiJ0Ubq/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.
* Make sure you have the necessary Okta details. For more information, see [Generate Okta credentials for Data Catalog](#generate-okta-credentials-for-data-catalog).

**Procedure**

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Okta** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="170.6666259765625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Domain</strong></td><td>The organization’s Okta domain (for example, https://yourcompany.okta.com).</td></tr><tr><td><strong>Client ID</strong></td><td>The Client ID, that is generated from your Okta app integration.</td></tr><tr><td><strong>Private Key Path</strong></td><td><p>The private key used for authentication with Okta.</p><p>Click <strong>Manage Key Paths</strong> to upload or manage keys.</p><p>Ensure the key is correctly configured in Okta and the app integration has the necessary scope and roles set in the okta admin console.</p></td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.
7. Click **Create Data Source** to establish your data source connection.
8. Click **Import Applications**.

   This process loads all the groups and applications associated with the Okta service in the Application section. For more information, see **Applications** in the **Use Pentaho Data Catalog** document.

   You can also monitor the status of the job on the Workers page.

You have successfully created a connection to Okta as a data source in Data Catalog.

After the Import Applications job completes, click **Applications** in the left navigation menu to view the imported hierarchy.

{% hint style="info" %}
The imported details are read-only. To sync the latest data from the Okta service, you must rerun the Import Applications job for the Okta data source. Any edits made by Data Catalog users to the imported assets will be overwritten during the next import.
{% endhint %}

The root level displays the name of the Okta data source, and the next level shows the groups retrieved from the Okta service. When you expand a group, all applications associated with that group appear below it. If an application is not part of any group in Okta, Data Catalog creates a group named **Default** and places such applications in it. If the same application belongs to multiple groups, it appears under each group. Each appearance is treated as a unique combination in the hierarchy view. For more information, see the [Applications ](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-applications-ug)section in the [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/) document.

## OneDrive or SharePoint data source

SharePoint and OneDrive in Microsoft 365 are cloud-based services that help organizations share and manage content, knowledge, and applications with seamless collaboration.

Perform the following steps to configure your OneDrive or SharePoint site as a data source within Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Microsoft OneDrive or SharePoint** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information to access Microsoft OneDrive or SharePoint.

   <table><thead><tr><th width="203.99993896484375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>The <strong>Default</strong> setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td><strong>Shared Key</strong> (default)</td></tr><tr><td><strong>Application (client) ID</strong></td><td>A unique identifier assigned to an application that has been registered in Azure Active Directory (Azure AD).</td></tr><tr><td><strong>Client Secret</strong></td><td>Password credentials to access data on the OneDrive or SharePoint site.</td></tr><tr><td><strong>Tenant ID</strong></td><td>A unique identifier of the OneDrive or SharePoint site.</td></tr><tr><td><strong>Path</strong></td><td><p>Folder where this data source is included.- Use '<code>/</code>' to scan all user’s OneDrive and SharePoint sites from for the root level, and use <code>/&#x3C;folder path>/</code> for a specific directory.</p><ul><li>Use <code>/users/&#x3C;username>/</code> for user-specific OneDrive.</li><li>Use <code>/sites/</code> for the root of the SharePoint sites and <code>/sites/&#x3C;SharePoint site path>/</code> for a specific SharePoint site.</li></ul></td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before finalizing and saving your new data source configuration, you must perform a process called 'Scan files'. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Scan Files**. \
   The **Scan Files** dialog box appears. Here you can refine metadata ingestion using the following options.&#x20;

   1. **Delete Empty Folders**: When selected, it deletes folders without any child entities from the Data Catalog metadata store. This option is intended only for full metadata scans.
   2. **Incremental Ingest**: Ingests data for filesystems or object stores where files or objects **created** or **modified** **time stamps** match the time period selected. This doesn't remove any existing data from previous ingests and can be used when you only want to ingest data from a particular timeframe. Available time periods are (Last) **12 Hours**, **24 Hours**, **1 Week**, **1 Month,** and **3 Months**.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>You cannot select <strong>Delete Empty Folders</strong> and <strong>Incremental Ingest</strong> at the same time. The <strong>Delete Empty Folders</strong> option applies only to full metadata scans and is not supported for incremental ingest operations.</p></div>
   3. **Include and Exclude Patterns:** This feature enables you to specify which folders or files should be scanned or excluded. By applying these filters, you can shorten scan duration and control the scope of metadata ingestion. For more information, see the feature walkthrough [Include or exclude patterns](https://hitachi-vantara.navattic.com/9ai0dle?g=cmfw350z4000004kzb74neovt\&s=0).

   This process loads files and folders into the system. You can monitor the status of the file scan on the **Workers** page.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a message will appear in the upper corner of the screen.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="223.3333740234375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to OneDrive or SharePoint as a data source.

## Oracle data source

Perform the following steps to add Oracle as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Oracle** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table data-header-hidden><thead><tr><th width="235.1112060546875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong>: Select <strong>Credentials</strong> or <strong>URI</strong> as a configuration method.</td><td></td></tr><tr><td>Configuration Method: <strong>Credentials</strong></td><td><ul><li><strong>Username/Password:</strong> Credentials that provide access to the specified database.</li><li><strong>Host:</strong> The address of the machine where the Oracle database server is running. It can be an IP address or a domain name.</li><li><strong>Port:</strong> The port number on which the Oracle server is listening for incoming connections.</li><li><strong>Database Name</strong>: The name of the database within the Oracle server that you want to connect with.</li></ul></td></tr><tr><td>Configuration method: <strong>URI</strong></td><td><ul><li><strong>Username/Password:</strong> Credentials that provide access to the specified database.</li><li><strong>URI:</strong> A service URL that looks like <code>jdbc:oracle:thin:@oracle.example.com:1521/mydb</code>.</li></ul></td></tr><tr><td><strong>Driver</strong></td><td>If you are selecting configuration method as Credentials or URI, then you must use the driver. Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before you finalize and save your new data source configuration, you need to perform a process called <strong>Scan files</strong>. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas, and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="255.5555419921875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the Oracle database as a data source.

## PostgreSQL data source

Perform the following steps to add PostgreSQL as a data source Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **PostgreSQL** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information to access the PostgreSQL data source.

   <table><thead><tr><th width="239.5555419921875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td>Select <strong>Credentials</strong> or <strong>URI</strong> as a configuration method.</td></tr><tr><td><strong>Driver</strong></td><td>Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The fully qualified Java class name of the JDBC driver.</td></tr><tr><td><strong>User Name</strong></td><td>The username used to authenticate to the PostgreSQL database. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password associated with the PostgreSQL user account. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains the PostgreSQL credentials (username and password). When provided, Data Catalog retrieves the credentials securely from Secret Manager instead of requiring manual entry.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secret versions from Secret Manager. This role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the PostgreSQL secret is stored in Secret Manager. Data Catalog uses this region to access the correct Secret Manager endpoint.</td></tr><tr><td><strong>Host</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The address of the machine where the PostgreSQL server is running. It can be an IP address or a domain name.</td></tr><tr><td><strong>Port</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The port on which the PostgreSQL server listens for incoming connections. The default PostgreSQL port is 5432.</td></tr><tr><td><strong>Database Name</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The name of the database or schema within the PostgreSQL server that you want to connect with.</td></tr><tr><td><strong>URI</strong><br>(Only for the <strong>URI</strong> method)</td><td>A unique identifier to locate the data source. It should have the name of the databases in the connection string itself. For example, URL would look like <code>jdbc: postgresql://localhost:&#x3C;port_no>/</code>.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before you finalize and save your new data source configuration, you need to perform a process called <strong>Scan files</strong>. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="217.7777099609375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the PostgreSQL data source.

## SAP HANA data source

Perform the following steps to add SAP HANA as a data source Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **SAP HANA** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table data-header-hidden><thead><tr><th width="236.2222900390625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td>Select <strong>Credentials</strong> or <strong>URI</strong> as a configuration method.</td></tr><tr><td><strong>Driver</strong></td><td>Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The fully qualified Java class name of the JDBC driver.</td></tr><tr><td><strong>User Name</strong></td><td>The username required to authenticate to SAP HANA when using URI mode. Optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password associated with the SAP HANA user account. Optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains SAP HANA credentials (username and password). When provided, Data Catalog retrieves the credentials securely from Secret Manager, overriding manual entry.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secrets from Secret Manager. This role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the SAP HANA secret is stored in Secret Manager. Data Catalog uses this region to access the correct Secret Manager endpoint.</td></tr><tr><td><strong>Host</strong><br>(Only for the <strong>Credentials</strong> method)<br></td><td>A physical or virtual machine (server) where an instance of SAP HANA is installed and running. It can be an IP address or a domain name.</td></tr><tr><td><strong>Port</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The port number on which the SAP HANA database server is listening for incoming connections.</td></tr><tr><td><strong>URI</strong><br>(Only for the <strong>URI</strong> method)</td><td>The JDBC connection string used to connect to SAP HANA. It must specify the host, port, database name, and optional credentials.<br>For example, URL would look like <code>jdbc: sap://localhost:&#x3C;port_no>/&#x3C;database_name>?user=&#x3C;user>&#x26;password=&#x3C;password></code>.</td></tr><tr><td><strong>Database Name</strong></td><td>The name of the database within the SAP HANA server that you want to connect with.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before you finalize and save your new data source configuration, you need to perform a process called <strong>Scan files</strong>. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas, and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="253.3333740234375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the SAP HANA data source.

## Salesforce data source

Salesforce is a cloud-based customer relationship management (CRM) platform that provides organizations with a unified platform to manage customer data, sales processes, marketing campaigns, support interactions, and other key business functions. By integrating Salesforce as a data source within Data Catalog, you can access and manage metadata from Salesforce. It enables data discovery to search, explore, and understand Salesforce data. Additionally, it enhances data lineage and compliance by providing detailed tracking of data movements.

Perform the following steps to add Salesforce as a data source in Data Catalog:

**Before you begin**

* Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.
* Configure trusted IP ranges in Salesforce to trust login requests coming from PDC IP addresses, eliminating the need for a security token.
  1. Sign in to your Salesforce organization (Production or Sandbox).
  2. In **Setup**, search for **Network Access**, or navigate to **Security Controls > Network Access**.
  3. Obtain the IP address of your Pentaho Data Catalog server.
  4. Add this IP address as a new **Trusted IP Range**.

     If your deployment uses a single server, enter the same IP address in both the **Start IP Address** and **End IP Address** fields.
* Ensure that the Salesforce user account used for Data Catalog integration has sufficient privileges to access the required objects and metadata. If not, grant the **View All Data** permission:
  1. In Salesforce, go to **Setup**.
  2. Navigate to **Users > Users**.
  3. Locate and select the user account used for the PDC integration.
  4. On the **User Details** page, click the Profile link and then click **Edit**.
  5. In the **Administrative Permissions** section, select the **View All Data** checkbox and click **Save**.

**Procedure**

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Salesforce** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="212.8887939453125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration method</strong></td><td>The method is used to configure the connection. The only option is <strong>Credentials</strong>.</td></tr><tr><td><strong>Driver</strong></td><td><p>The standard used to establish communication between the application and the database. Select <strong>Default</strong>, which is an existing driver, to ensure that communication between the application and the database is efficient, secure, and compliant with the required standards.</p><p><strong>CAUTION:</strong> Don’t change the driver for the Salesforce data source type. Changing it might disrupt the connection and cause unexpected behavior.</p></td></tr><tr><td><strong>Driver Class Name</strong></td><td>The fully qualified Java class name of the JDBC driver.</td></tr><tr><td><strong>Username</strong></td><td>The Salesforce login username, associated with the Salesforce account. When <strong>Secret Manager Key</strong> is configured, the <strong>User Name</strong> is optional.</td></tr><tr><td><strong>Password</strong></td><td>The password of the Salesforce account to authenticate the connection. When <strong>Secret Manager Key</strong> is configured, the <strong>Password</strong> is  optional.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains the Salesforce connection credentials (username and password). When provided, Data Catalog retrieves the credentials securely from Secret Manager, overriding manual entry.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secrets from Secret Manager. The role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the Salesforce credentials are stored in Secret Manager. Data Catalog uses this region to access the correct Secret Manager endpoint.</td></tr><tr><td><strong>Host</strong></td><td>The domain or endpoint of the Salesforce instance you are connecting to.</td></tr><tr><td><strong>Port</strong></td><td>The port number to connect to the Salesforce instance.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before you finalize and save your new data source configuration, you need to perform a process called <strong>Scan files</strong>. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="214.4444580078125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to Salesforce as a data source.

## SMB/CIFS data source

Server Message Block (SMB) and Common Internet File System (CIFS) are Windows file sharing protocols used in storage systems. You can add data to Data Catalog from a file sharing protocol, such as CIFS or SMB, to either the remote agent or local agent, thereby enabling the creation of a data source as CIFS or SMB with a local file system path.

This protocol uses a client-server model where the server provides a shared file system and the client mounts the file system to access the shared files as if they were on a local disk. You can add data to the Data Catalog from any file-sharing network system that supports transfer via the Server Message Block (SMB) and Common Internet File System (CIFS) protocols.

Perform the following steps to add SMB or CIFS as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **SMB or CIFS** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="199.55560302734375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration method</strong></td><td>By default, it is a <strong>URI</strong>.</td></tr><tr><td><strong>URI</strong></td><td>URIs are used to identify and locate resources on the internet or within a network. For example, the URI would look like <code>smb/cifs://server.example.com</code></td></tr><tr><td><strong>Domain</strong></td><td>The domain name, if the SMB or CIFS server is part of a Windows domain.</td></tr><tr><td><strong>Path</strong></td><td>NFS path to access the data source. For example, the path would look like <code>smb/cifs://server:/path/to/resource</code></td></tr><tr><td><strong>Username/Password</strong></td><td>Credentials that provide access to the SMB or CIFS resource.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.
7. Click **Scan Files**. \
   The **Scan Files** dialog box appears. Here you can refine metadata ingestion using the following options.&#x20;

   1. **Delete Empty Folders**: When selected, it deletes folders without any child entities from the Data Catalog metadata store. This option is intended only for full metadata scans.
   2. **Incremental Ingest**: Ingests data for filesystems or object stores where files or objects **created** or **modified** **time stamps** match the time period selected. This doesn't remove any existing data from previous ingests and can be used when you only want to ingest data from a particular timeframe. Available time periods are (Last) **12 Hours**, **24 Hours**, **1 Week**, **1 Month,** and **3 Months**.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>You cannot select <strong>Delete Empty Folders</strong> and <strong>Incremental Ingest</strong> at the same time. The <strong>Delete Empty Folders</strong> option applies only to full metadata scans and is not supported for incremental ingest operations.</p></div>
   3. **Include and Exclude Patterns:** This feature enables you to specify which folders or files should be scanned or excluded. By applying these filters, you can shorten scan duration and control the scope of metadata ingestion. For more information, see the feature walkthrough [Include or exclude patterns](https://hitachi-vantara.navattic.com/9ai0dle?g=cmfw350z4000004kzb74neovt\&s=0).

   This process loads files and folders into the system. You can monitor the status of the file scan on the **Workers** page.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a message will appear in the upper corner of the screen.</p></div>
8. (Optional) Configure the following options for the data source.

   <table><thead><tr><th width="251.1112060546875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr><tr><td><strong>Cost per Terabyte</strong></td><td>Menu to select currency and text field to enter the price per terabyte.</td></tr><tr><td><strong>Total Capacity</strong></td><td>Field to enter the total capacity of the data source in terabytes.</td></tr></tbody></table>
9. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
10. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the SMB or CISF resource as a data source.

## Snowflake data source

Perform the following steps to add Snowflake as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Snowflake** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="192.88885498046875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration method</strong></td><td>The method used to configure the connection. The only option is <strong>Credentials</strong>.</td></tr><tr><td><strong>Driver</strong></td><td><p>The standard used to establish communication between the application and the database.Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.</p><p>To upload a new driver, click <strong>Manage Drivers</strong>, and click <strong>Add New</strong>, upload the driver, and then click <strong>Add Driver</strong>.</p></td></tr><tr><td><strong>Driver Class Name</strong></td><td>The fully qualified Java class name of the JDBC driver.</td></tr><tr><td><strong>Username</strong></td><td>The Snowflake login username associated with the Snowflake account. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password for the Snowflake user account. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains Snowflake credentials (username and password). When provided, Data Catalog retrieves credentials securely from Secret Manager instead of requiring manual entry.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secrets from Secret Manager. This role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the Snowflake credentials are stored in Secret Manager. Data Catalog uses this region to access the correct Secret Manager endpoint.</td></tr><tr><td><strong>Host</strong></td><td>The address of the machine where the Snowflake database server is running. It can be an IP address or a domain name.</td></tr><tr><td><strong>Port</strong></td><td>The port number to connect to the Snowflake data source.</td></tr><tr><td><strong>Database Name</strong></td><td>The name of the database within the Snowflake that you want to connect with.</td></tr><tr><td><strong>Warehouse</strong></td><td>The name of the Snowflake virtual warehouse to use for executing queries, loading data, and performing compute operations.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before finalizing and saving your new data source configuration, you must perform a process called <strong>Scan files</strong>. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the data scanning limit specified in your license agreement, a Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To utilize storage optimization options, a Pentaho Data Optimizer license is required.</p></div>

   <table><thead><tr><th width="248.888916015625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the Snowflake data source.

## Sybase data source

Sybase is a relational database management system (RDBMS) used for data warehousing, business intelligence, and enterprise applications. Integrating Sybase as a data source within Data Catalog, you can access and manage metadata from the Sybase database. It enables data discovery to search, explore, and understand Sybase data. Additionally, it enhances data lineage and compliance by providing detailed tracking of data movements.

Perform the following steps to add Sybase as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Sybase** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="208.4444580078125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration method</strong></td><td>The method, used to configure the connection. The only option is <strong>URI</strong>.</td></tr><tr><td><strong>Driver</strong></td><td>Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.<br>To upload a new driver, click <strong>Manage Drivers</strong>, click <strong>Add New</strong>, upload the driver, and then click <strong>Add Driver</strong>.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The fully qualified Java class name of the JDBC driver.</td></tr><tr><td><strong>URI</strong></td><td>URIs are used to access and manage various objects and services within the Sybase environment. For example, the URI would look like <code>jdbc:sybase:tds:&#x3C;hostname>:&#x3C;port>?ServiceName=&#x3C;dbname></code></td></tr><tr><td><strong>Username</strong></td><td>The username required to authenticate to the Sybase database. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Password</strong></td><td>The password associated with the Sybase user account. This field is optional when using <strong>Secret Manager Key</strong>.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The name or identifier of the secret stored in Secret Manager that contains the Sybase credentials (username and password). When provided, Data Catalog retrieves the credentials securely from Secret Manager, overriding manual entry.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role that grants Data Catalog permission to read secrets from Secret Manager. This role must include permissions such as <code>secretmanager.versions.access</code>.</td></tr><tr><td><strong>Region</strong></td><td>The region where the Sybase credentials are stored in Secret Manager. Data Catalog uses this region to access the correct Secret Manager endpoint.</td></tr><tr><td><strong>Database Name</strong></td><td>The name of the data sources within the Sybase environment that contain the data you want to access.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before finalizing and saving your new data source configuration, you must perform a process called <strong>Scan files.</strong> If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="261.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the Sybase data source.

## Vertica data source

Perform the following steps to add Vertica as a data source in Data Catalog:

Refer to the [Component Reference](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/components-reference) section in the [Install Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/Njj4joO63OgOTabje2xP/) document to confirm that you have met all the necessary requirements listed for the data source you want to connect.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. In the **Resources** card, click **Add Data Source**.

   The Create Data Source page opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you are nearing or have exceeded the limit of data sources allowed by your license agreement, a message appears when you try to add a new data source.</p></div>
3. Specify the following information for the connection to your data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Data Catalog encrypts your data source connection details, such as user name and password, before storing them.</p></div>

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source Name</strong></td><td>Specify the name of your data source. This name is used in the Data Catalog interface. It should be something your Data Catalog users recognize.<br><strong>Note:</strong> Names must start with a letter, and must contain only letters, digits, and underscores. Spaces in names are not supported.</td></tr><tr><td><strong>Data Source ID</strong> (Optional)</td><td>Specify a permanent identifier for your data source.<br><strong>CAUTION:</strong> If this field is left blank, Data Catalog generates a permanent identifier, which cannot be modified.</td></tr><tr><td><strong>Description</strong> (Optional)</td><td>Specify a description of your data source.</td></tr></tbody></table>
4. After you have specified the basic connection information, select **Vertica** in the **Data Source Type** field.\
   Data Catalog then prompts you to specify additional connection information based on the file system or database type you are trying to access.
5. Specify the following additional connection information.

   <table><thead><tr><th width="239.5555419921875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Affinity</strong></td><td>This default setting specifies which agents should be associated with the data source in a multi-agent deployment.</td></tr><tr><td><strong>Configuration Method</strong></td><td>Select <strong>Credentials</strong> or <strong>URI</strong> as a configuration method.</td></tr><tr><td><strong>Driver</strong></td><td>Select an existing driver or upload a new driver to ensure that the communication between the application and the database is efficient, secure, and follows the required standards.<br>To upload a driver, click <strong>Manage Drivers</strong>, select <strong>Add New</strong>, upload the driver, and click <strong>Add Driver</strong>.</td></tr><tr><td><strong>Driver Class Name</strong></td><td>The fully qualified Java class name of the JDBC driver used to connect to Vertica.</td></tr><tr><td><strong>User Name</strong></td><td>The username that provides access to the Vertica database. If using <strong>Secret Manager Key</strong>, this field becomes optional.</td></tr><tr><td><strong>Password</strong></td><td>The password that provides access to the Vertica database. If using <strong>Secret Manager Key</strong>, this field becomes optional.</td></tr><tr><td><strong>Secret Manager Key</strong></td><td>The identifier of the secret stored in the Secret Manager (AWS Secrets Manager or GCP Secret Manager). When provided, the system retrieves database credentials securely from the secret instead of using manually entered Username and Password.</td></tr><tr><td><strong>Role</strong></td><td>The IAM role used to access the secret in the Secret Manager. Required when using role-based access to retrieve credentials.</td></tr><tr><td><strong>Region</strong></td><td>The cloud region where the Secret Manager key is stored.</td></tr><tr><td><strong>Host</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>A physical or virtual machine (server) where an instance of the Vertica database software is installed and running. It can be an IP address or a domain name.</td></tr><tr><td><strong>Port</strong><br>(Only for the <strong>Credentials</strong> method)</td><td>The port number on which the Vertica server is listening for incoming connections.</td></tr><tr><td><strong>URI</strong><br>(Only for the <strong>URI</strong> method)</td><td>The JDBC connection string used to establish a connection with Vertica.<br>For example, the URL would look like <code>jdbc:vertica://&#x3C;hostname>:&#x3C;port>/&#x3C;database>?user=&#x3C;username>&#x26;password=&#x3C;password></code>.</td></tr><tr><td><strong>Database Name</strong></td><td>The name of the database within the Vertica server that you want to connect with.</td></tr></tbody></table>
6. Click **Test Connection** to test your connection to the specified data source.\
   A Test Connection confirmation message window opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Before you finalize and save your new data source configuration, you need to perform a process called <strong>Scan files</strong>. If you are nearing or have exceeded the data scanning limit set by your license agreement, a message appears in the upper corner of the screen. Databases do not have a data scan quota.</p></div>
7. Click **Ingest Schema.** The **Select schemas for ingestion** dialog opens. You can search for schemas using the search bar at the top, using starts with or regular expressions. Once you have located the relevant schemas, select the schemas and then click **Ingest** to load the database schema and related metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Although you can select all schemas, it is a best practice to avoid selecting certain system-related schemas that are unnecessary for your needs.</p></div>
8. (Optional) In the **Physical Location** field, specify the physical location details of the data source.
9. (Optional) Configure the following storage optimization options for the data source.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To use storage optimization options, you need a Pentaho Data Optimizer license.</p></div>

   <table><thead><tr><th width="252.22216796875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Available for Migration</strong></td><td>Enables or disables the data source for storage optimization. When enabled, it includes the data source for data optimizer activities.</td></tr><tr><td><strong>Available for Writing</strong></td><td>Enables or disables writing capabilities for the data source and enables migration when turned on.</td></tr><tr><td><strong>Available for Data Mastering</strong></td><td>Enables or disables the data source for data mastering purposes.</td></tr></tbody></table>
10. (Optional) In the **Cost per Terabyte** field, specify the data source pricing details like currency, price per terabyte, and billing frequency.
11. (Optional) In the **Total Capacity** field, specify the total capacity of the data source in terabytes.
12. (Optional) Enter a **Note** for any additional information to share with others who might access this data source.
13. Click **Create Data Source** to establish your data source connection.

You have successfully created a connection to the Vertica data source.
