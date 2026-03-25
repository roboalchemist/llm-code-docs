# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/create-a-vfs-metastore.md

# Create a VFS metastore

A PDI metastore is a location for storing resources shared by multiple tranformations. This enables Pentaho hyperscaler deployments to access the metastore in the cloud environment and also let the PDI client and the Pentaho Server reference the same VFS metastore. The VFS connection information is stored in an XML file The metastore can be located in three locations:

* The metastore can be stored on the machine where you're running PDI in either in your user directory or in a repository.
* If your PDI client is connected to the Pentaho Server, you will use a remote metastore located in your Pentaho Server repository.
* The metastore can be located in a cloud location accessible by a VFS connection.

Multiple users can access the metastore when it is stored in a remote location. The remote metastore has priority over a local metastore. For example, if you set up the PDI client with a valid metastore-config file and then connect to a Pentaho Server repository, your transformations will still use resources from the remote metastore, not the repository metastore.

## Enable a VFS metastore

Before you can use a remote metastore, you must enable the VFS connection in the PDI client. To do this you will create a metastore configuration XML file, then edit the VFS connection information in that file.

Perform the following steps to enable a VFS metastore:

1. Open the PDI client and create a VFS connection to the storage location that you want to use as your metastore.

   The VFS connection information will be saved to a file. See [Create a VFS connection](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/create-a-vfs-connection-in-pdi)
2. Close the PDI client.
3. Navigate to the `\Users\<yourusername>\.pentaho\metastore\pentaho\Amazon S3 Connection\` directory and copy the VFS connection file you just created to the `Users\<yourusername>\.kettle` directory.
4. Rename the file to `metastore-config`.
5. Open the `metastore-config` file with any text editor and add `scheme` and `rootPath` elements, along with their values.

   See the appropriate section in [Metastore configuration](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/broken-reference).
6. Save and close the `metastore-config` file.
7. Restart the PDI client.

The remote VFS metastore is now enabled. Note that the previous connections in the PDI client still exist in your local metastore directory, but no longer display in the PDI client. When you create a new VFS connection, the new connection will be in the location specified in your metastore-config file.

## Metastore configuration

The elements listed in the following table are required for all remote environments. When you create a VFS connection using the PDI client, you will not need to manually edit anything in the `<configuration>` section.

### Common elements

These elements are required for all VFS connections:

<table data-header-hidden><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td>Element</td><td>Value</td><td>Description</td></tr><tr><td><code>scheme</code></td><td>&#x3C;string></td><td><p>The type of connection. The values are:</p><p><strong>s3</strong> - Amazon, MinIO, and HCP</p><p><strong>gs</strong> - Google cloud storage</p><p><strong>abfss</strong> - Azure Data Lake Storage Gen2</p></td></tr><tr><td><code>rootPath</code></td><td>&#x3C;bucket-name>[/&#x3C;path>]</td><td><p>The bucket name and optional folder path where you want to create the VFS metastore. The <code>rootPath</code> element must point to the location where you will store the metastore file on the cloud location.</p><p>This is analogous to the <code>.pentaho</code> folder in a local metastore.</p><p>Examples:</p><ul><li><code>miniobucket/dir1</code></li><li><code>gcpbucket/dir1</code></li></ul></td></tr><tr><td><code>children</code></td><td></td><td><p>A container for type-specific configurations. For example:</p><pre><code>&#x3C;children>
    &#x3C;child>
&#x3C;id>description&#x3C;/id>
         &#x3C;value>&#x3C;/value>
    &#x3C;type>String&#x3C;/type>
&#x3C;/child>
…
&#x3C;/children>

</code></pre></td></tr></tbody></table>

### S3 elements

The elements listed in the table below apply to S3 environments. Some elements are conditional, based on your choices for other settings:

| Element               | Value                            | Description                                                                                                                                                                           |
| --------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `accessKey`           | `<s3-access-key>`                | The S3 user’s access key.                                                                                                                                                             |
| `secretKey`           | `<s3-secret-key>`                | The S3 user’s secret key.                                                                                                                                                             |
| `endPoint`            | `<s3-endpoint>`                  | <p>The URL to access the S3 location. Examples:</p><p><code>http\://\<host ip>:port</code></p><p><code><https://my-hcp-namespace.my-hcp-tenant.hcpdemo.hitachivantara.com></code></p> |
| `region`              | `<s3-region>`                    | The user-designated region. For example, `us-east-1`.                                                                                                                                 |
| `connectionType`      | 0 or 1                           | <p>The connection type value. The values are:</p><p><strong>0</strong> - to connect to AWS</p><p><strong>1</strong> - to connect to MinIO or HCP</p>                                  |
| `credentialFile`      |                                  | An encrypted string that is not user editable                                                                                                                                         |
| `profileName`         | `<string>`                       | The AWS user profile connection when the Type is 0 (AWS) and the `authType` is 1 (credentials file)                                                                                   |
| `defaultS3Config`     | true or false                    | The setting that controls whether the default S3 configuration is used. Set to `true` to use the default S3 configuration                                                             |
| `credentialsFilePath` | `<path to AWS credentials file>` | The path to the AWS credentials file when the connectionType is 0 (AWS) and the authType is 1 (credentials file),                                                                     |
| `pathStyleAccess`     | true or false                    | The setting that controls which access style is used. Specify `true` to use a path-style access; `false` to use S3 bucket-style access                                                |
| `signatureVersion`    | `AWSS3V4SignerType`              | The version of signature used for communicating with the AWS S3 location of your metastore.                                                                                           |
| `name`                | `vfsMetastore`                   | The name for the connection.                                                                                                                                                          |
| `description`         | `<string>`                       | A description of the connection.                                                                                                                                                      |
| `sessionToken`        | `<session token string>`         | Optional. A temporary credential that is used if the AWS S3 bucket is configured to require a session token for access                                                                |
| `authType`            | 0 or 1                           | <p>The authentication type to use when the connection type is 0 (AWS):</p><p>0 – Access key/Secret key</p><p>1 – Credentials file</p>                                                 |

### GCP elements

The elements listed in the table below apply to GCP environments:

| Element             | Value      | Description                                                                |
| ------------------- | ---------- | -------------------------------------------------------------------------- |
| `serviceAccountKey` | `<string>` | A key that is generated based on the contents of the service account JSON. |
| `keyPath`           | `<path>`   | The path to the file containing the GCP service account JSON.              |
| `name`              | `<string>` | The name of the connection.                                                |
| `description`       | `<string>` | A description of the connection.                                           |

### Azure Data Lake Storage Gen2 elements

The elements listed in the table below apply to Azure Data Lake Storage Gen2 environments. See [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/) documentation for more information.

| Element               | Value                | Description                                                                                                                                    |
| --------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `sharedKey`           | `<encrypted string>` | The shared key for accessing the service.                                                                                                      |
| `accountName`         | `<encrypted string>` | The name of the account.                                                                                                                       |
| `accessTier`          | `<string>`           | The access tier value. The default is `Hot.`                                                                                                   |
| `blockSize`           | `<Integer>`          | The default is 50.                                                                                                                             |
| `maxSingleUploadSize` | `<Integer>`          | The default is 100.                                                                                                                            |
| `bufferCount`         | `<Integer>`          | The default is 5.\[MB1]                                                                                                                        |
| `name`                | `<string>`           | The name of the connection.                                                                                                                    |
| `authType`            | `0`, `1`, or `2`     | <p>The authorization type. The values are:</p><p>0 - Account Shared Key</p><p>1 - Azure Active Directory</p><p>2 - Shared Access Signature</p> |
