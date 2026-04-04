# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/schedules/setup-a-vfs-location-for-schedule-output.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/setup-a-vfs-location-for-schedule-output.md

# Set up a VFS location for schedule outputs

With the VFS connection in the Pentaho User Console you can use cloud storage locations to store the report-generated output files. You must be an administrator to create, edit, or delete the VFS connection, to designate roles access connections, and specify the folder. Supported VFS locations are:

* Amazon S3/Minio/HCP
* Azure Data Lake Gen 1
* Azure Data Lake Gen 2 / Blob
* Google Cloud Storage
* HCP REST
* Local
* SMB/UNC Provider

**Note:** If you want to use the local physical file system of your machine as a VFS location to store outputs, see [Set up a Local VFS location for schedule outputs](https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/set-up-a-local-vfs-location-for-schedule-outputs).

Perform the following steps to create a VFS connection from the Pentaho User Console:

1. Click **Home** and then click **Administration**.

   The Administration perspective opens.
2. Click **VFS Connections** and then click the plus sign to add a connection.

   The New VFS Connection dialog box for general settings opens.

   ![New VFS Connection dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-a7c4582439bd36b1a14ef07d30a2e8b458f86a8f%2FPUC%20New%20VFS%20Connecion%20dialog%20box.png?alt=media)
3. Enter a **Connection Name**, and optionally a **Description**.
4. Click **Connection Type** and select the type of connection that you want to create from the list:
   * **Amazon S3/Minio/HCP**
   * **Azure Data Lake Gen 1**
   * **Azure Data Lake Gen 2 / Blob**
   * **Google Cloud Storage**
   * **HCP REST**
   * **Local**
   * **SMB/UNC Provider**
5. In **Access Roles**, click a role or use CtrlClick to select multiple roles from the list to assign permissions for access to the VFS connection and folder.

   The defaults are Administrator and Authenticated.
6. Click **Next**.

   The New VFS Connection dialog box for connection details opens.
7. Enter the connection type details and options. Choose from:

| Connection Type                  | Options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Amazon**                       | <p>Click <strong>Connection Type</strong> and select <strong>Amazon</strong>.</p><p>Simple Storage Service (S3) accesses the resources on Amazon Web Services. See <a href="https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html">Working with AWS Credentials</a> for Amazon S3 setup instructions.</p><ul><li>Select the <strong>Authentication Type</strong>:<br>- <strong>Access Key/Secret Key</strong><br>- <strong>Credentials File</strong></li><li>Select the <strong>Region</strong>.</li><li><p>When <strong>Authentication Type</strong> is:</p><ul><li><strong>Access Key/Secret Key</strong>, then enter the <strong>Access Key</strong> and <strong>Secret Key</strong>, and optionally enter the <strong>Session Token</strong>.</li><li><strong>Credentials File</strong>, then enter the <strong>Profile Name</strong> and the <strong>File Location</strong>.</li></ul></li><li>Select the <strong>Default S3 Connection</strong> checkbox to make <strong>Amazon</strong> the default S3 connection.</li></ul>                                                                                                                                                                                                                                                                                                                                                                          |
| **Minio/HCP**                    | <p>Click <strong>Connection Type</strong> and select <strong>Minio/HCP</strong>.</p><p>Minio accesses data objects on an Amazon compatible storage server. See the <a href="https://docs.min.io/docs/">Minio Quickstart Guide</a> for Minio setup instructions.</p><ul><li>Enter the <strong>Access Key</strong>.</li><li>Enter the <strong>Secret Key</strong>.</li><li>Enter the <strong>Endpoint</strong>.</li><li>Enter the <strong>Signature Version</strong>.</li><li>Select the <strong>PathStyle Access</strong> checkbox to use path-style requests. Otherwise, Amazon S3 bucket-style access is used.</li><li>Select the <strong>Default S3 Connection</strong> checkbox to make <strong>Minio/HCP</strong> the default S3 connection.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Azure Data Lake Gen 1**        | <p>Accesses data objects on Microsoft Azure Gen 1 storage services. You must create an Azure account and configure Azure Data Lake Storage Gen 1. See <a href="https://docs.hitachivantara.com/r/W5Oy5NghPggWbWs_8gNJXw/bVcEnW6Cj5aOLgChBPiz5w">Access to Microsoft Azure</a> for more information.</p><ul><li>The <strong>Authentication Type</strong> is <strong>Service-to-service authentication</strong>.</li><li>Enter the <strong>Account Fully Qualified Domain Name</strong>.</li><li>Enter the <strong>Application (client) ID</strong>.</li><li>Enter the <strong>Client Secret</strong>.</li><li>Enter the <strong>OAuth 2.0 token endpoint</strong>.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Azure Data Lake Gen 2 / Blob** | <p>Accesses data objects on Microsoft Azure Gen 2 and Blob storage services. You must create an Azure account and configure Azure Data Lake Storage Gen 2 and Blob Storage. See <a href="https://docs.hitachivantara.com/r/W5Oy5NghPggWbWs_8gNJXw/bVcEnW6Cj5aOLgChBPiz5w">Access to Microsoft Azure</a> for more information.</p><ul><li>Select the <strong>Authentication Type</strong>:<br>- <strong>Account Shared Key</strong><br>- <strong>Azure Active Directory</strong><br>- <strong>Shared Access Signature</strong></li><li>Enter the <strong>Service Account Name</strong>.</li><li>Enter the <strong>Block Size (Min 1 MB to Max 100 MB)</strong>.The default is 50.</li><li>Enter the <strong>Buffer Count (Min 2)</strong>. The default is 5.</li><li>Enter the <strong>Max Block Upload Size (Min 1 MB to 900 MB)</strong>. The default is 100.</li><li>Select the <strong>Access Tier</strong>. The default value is Hot.</li><li><p>When <strong>Authentication Type</strong> is:</p><ul><li><strong>Account Shared Key</strong>, then enter the <strong>Service Account Shared Key</strong>.</li><li><strong>Azure Active Directory</strong>, then enter the <strong>Application (client) ID</strong>, <strong>Client Secret</strong>, and <strong>Directory (tenant) ID</strong>.</li><li><strong>Shared Access Signature</strong>, then enter the <strong>Shared Access Signature</strong>.</li></ul></li></ul> |
| **Google Cloud Storage**         | <p>Accesses data objects on the Google Cloud Storage file system. See <a href="https://cloud.google.com/storage/docs">Google Cloud Storage</a> for information.</p><ul><li>Enter the <strong>Service Account Key Location</strong>.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **HCP REST**                     | <p>Accesses data objects on the Hitachi Content Platform. You must configure HCP and PDI before accessing the platform. You must also configure object versioning in HCP Namespaces. See <a href="https://docs.hitachivantara.com/r/W5Oy5NghPggWbWs_8gNJXw/U4R_swcuWATRSshT9TM1bw">Access to HCP</a> for more information.</p><ul><li>Enter the <strong>Host</strong> and <strong>Port</strong> number.</li><li>Enter the <strong>Tenant</strong>, <strong>Namespace</strong>, <strong>Username</strong>, and <strong>Password</strong>.</li><li>Click <strong>More options</strong> then enter the <strong>Proxy Host</strong> and <strong>Proxy Port</strong> number.</li><li>Select whether to use <strong>Accept self-signed certificate</strong>. The default is No.</li><li>Select whether the <strong>Proxy is secure</strong>. The default is No.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Local**                        | Accesses a file system on your local machine. See [Set up a Local VFS location for schedule outputs](https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/set-up-a-local-vfs-location-for-schedule-outputs) for details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **SMB/UNC Provider**             | <p>Accesses Server Message Block data using a Universal Naming Convention string to specify the file location.</p><ul><li>Enter the <strong>Domain</strong>. The domain name of the target machine hosting the resource. If the machine has no domain name (for example, a home computer), then use the name of the machine.</li><li>Enter the <strong>Port Number</strong>. The default is 445.</li><li>Enter the <strong>Server</strong>, <strong>User Name</strong>, and <strong>Password</strong>.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

8\. Click \*\*Test\*\* to test the connection.

```
The test results open.
```

9\. Click **Next**.

```
The New VFS Connection dialog box for root folder details opens.
```

10\. In the **Root Folder Path** field, enter the path for your VFS connection output folder. Enter the full path to set a local connection to a specific folder. Optionally, use an empty path to allow access to the root and all its folders.

```
The default is to the root and its folders in your local physical file system.
```

11\. Click **Test** to test the connection.

```
The test results open.
```

12\. Click **Next**.

```
The New VFS Connection summary panel opens with all the information you have entered for the connection including the **Root Folder Path**.
```

13\. If needed, click the **pencil** icon to edit the connection.

14. Click **Finish**.

    The setup completes and test results appear. A New VFS Connection dialog box opens with options to **Create new VFS connection** or **Edit this connection**. If needed, click the **Edit this connection** to make changes to the connection.
15. Click **Finish**.

Your new connection is created and listed in the VFS Connections panel.

To edit a VFS connection, select the connection and click the **Edit Connection** icon. To delete the VFS connection, click the **Delete Connection** icon.
