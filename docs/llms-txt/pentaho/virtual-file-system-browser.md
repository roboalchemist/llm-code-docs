# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/virtual-file-system-browser.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser.md

# Connecting to Virtual File Systems

You can connect to most Virtual File Systems (VFS) through VFS connections in PDI. A VFS connection is a stored set of VFS properties that you can use to connect to a specific file system. In PDI, you can add a VFS connection and then reference that connection whenever you want to [access files or folders on your Virtual File System](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/open-a-transformation-task). For example, you can use the VFS connection for Hitachi Content Platform (HCP) in any of the HCP transformation steps without the need to repeatedly enter your credentials for data access.

With a VFS connection, you can set your VFS properties with a single instance that can be used multiple times. The VFS connection supports the following file systems:

* **Amazon S3/Minio/HCP**
  * Simple Storage Service (S3) accesses the resources on Amazon Web Services. See [Working with AWS Credentials](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html) for Amazon S3 setup instructions.

    **Note:** If a connectivity issue occurs with AWS / S3, perform either of the following actions:

    * Set the Environment Variables for `AWS_REGION` or `AWS_DEFAULT_REGION` to the applicable Default Region.
    * Set the correct Default Region in the shared configuration file (`~/.aws/config`) or the credentials file (`~/.aws/credentials`). For example:

      ![AWS sample config file](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-10cb315a3e908644f3a4f14965a8e78ddc67c2b0%2FAWS_S3_sample_code.png?alt=media)

    See <https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/region-selection.html> and <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html> for more information.
  * Minio accesses data objects on an Amazon compatible storage server. See the [Minio Quickstart Guide](https://docs.min.io/docs/) for Minio setup instructions.
  * HCP uses the S3 protocol to access HCP. See [Access to HCP REST](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-hcp-rest) for more information.
* **Azure Data Lake Gen 1**

  Accesses data objects on Microsoft Azure Gen 1 storage services. You must create an Azure account and configure Azure Data Lake Storage Gen 1. See [Access to Microsoft Azure](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-microsoft-azure) for more information.

  **Note:** Support for Azure Data Lake Gen 1 is discontinued and limited to users with existing Gen 1 accounts. As a best practice, use Azure Data Lake Storage Gen 2. See [Azure](https://azure.microsoft.com/en-us/updates/action-required-switch-to-azure-data-lake-storage-gen2-by-29-february-2024/) for details.
* **Azure Data Lake Gen 2/Blob**

  Accesses data objects on Microsoft Azure Gen 2 or Blob storage services. . You must create an Azure account and configure Azure Data Lake Storage Gen 2 and Blob Storage. See [Access to Microsoft Azure](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-microsoft-azure) for more information.
* **Google Cloud Storage**

  Accesses data in the Google Cloud Storage file system. See [Google Cloud Storage](https://cloud.google.com/storage/docs) for more information on this protocol.
* **HCP REST**

  Accesses data in the Hitachi Content Platform. You must configure HCP and PDI before accessing the platform. See [Access to HCP REST](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-hcp-rest) for more information.
* **Local**

  Accesses data in your local physical file system.
* **SMB/UNC Provider**

  Accesses data in a Windows platform that uses the Server Message Block (SMB) protocol and Universal Naming Convention (UNC) string to specify the resource location path.
* **Snowflake Staging**

  Accesses a staging area used by Snowflake to load files. See [Snowflake staging area](https://docs.snowflake.net/) for more information on this protocol.

After you create a VFS connection, you can use it with PDI steps and entries that support the use of VFS connections. If you are connected to a repository, the VFS connection is saved in the repository. If you are not connected to a repository, the connection is saved locally on the machine where it was created.

If a VFS connection in PDI is not available for your Virtual File System, you may be able to access it with the VFS browser. See [VFS browser](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems) for further details.
