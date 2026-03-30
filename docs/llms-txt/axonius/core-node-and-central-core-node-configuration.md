# Source: https://docs.axonius.com/docs/core-node-and-central-core-node-configuration.md

# Core Node and Central Core Node Configuration

As part of the central core architecture, the following configuration must be set on each core node and on the central core node. For more details, see [Central Core Architecture](/docs/central-core-architecture).

## Core Node Configuration (for Upload)

<Callout icon="📘" theme="info">
  Note

  The exact settings, including the passphrase, must be configured on all core nodes and on the central core node.
</Callout>

**To configure the core node:**

1. From the top right corner of any page, click Settings ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **Data**, and select **Central Core Architecture**.
3. For each core node: In the **Data Synchronization Settings** section, select **Enable data synchronization (central core architecture)**, choose the desired storage type (each type has dedicated fields), and specify the required credentials. Those credentials will be used to upload an assets file of all its assets.

Axonius supports the following storage types for asset data from each Axonius core node. Each requires a different open port:

* [Amazon S3 Bucket](#amazon-s3-settings)
* [Azure Blob Storage](#azure-blob-storage-settings)
* [SMB Share](#smb-share-settings)
* [SSH](#ssh-settings)

## Central Core Node Configuration (for Download)

<Callout icon="📘" theme="info">
  Note

  Contact your Axonius account representative to configure the desired Axonius instance as the central core node.
</Callout>

Configure the same storage location credentials and the same passphrase as supplied in all the core nodes, as the central core node downloads and loads all the data from a single storage location.

## Amazon S3 Settings

For information about creating, configuring, and accessing Amazon S3 buckets, see [Configuring an S3 Bucket to use with Axonius](/docs/configuring-an-s3-bucket-to-use-with-axonius).

![DeployS3Buckets](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/CentralCore-S3.png)

1. **Operation Mode** *(optional)* - See [Operation Mode](#operation-mode).
2. **Gateway** *(optional)* - Select the gateway to use for backup. When a gateway is selected, all backup/restore operations are routed through it.
3. **Storage type** - Select AWS S3 Bucket.
4. **Data encryption passphrase (min. 16 characters)** *(required, default: empty)* - Specify a passphrase for the created file. The passphrase must consist of at least 16 characters.
5. **Amazon S3 endpoint URL** - When using an S3 endpoint URL, enter the URL here.
6. **Amazon S3 bucket name** - Name of Amazon S3 bucket. The bucket name is the string that follows the last colon in the full ARN. For example, if the ARN is `arn:aws:s3:::my-s3-backup-location`, the bucket name is `my-s3-backup-location`.
7. **Bucket Location** - Set the AWS infrastructure to which to connect. The default value for this setting is **AWS Standard**. To access a bucket which resides in the AWS GovCloud infrastructure, select **AWS GovCloud**.
8. **AWS Access Key ID** and **AWS Secret Access Key** *(optional, default: empty)* - Specify the AWS Access Key ID and the AWS Secret Access Key to access the Amazon S3 bucket.
   * If supplied, Axonius uses the account user credentials to send the asset file to the Amazon S3 bucket.
   * If not supplied, Axonius will use the EC2 instance (Axonius installed on) attached IAM role / instance profile to send the asset file to the Amazon S3 bucket.
9. **Enable backup to Amazon S3** *(required, default: False)* - On each core node, this checkbox must be enabled.
10. **Proxy** *(optional, default: empty)* - HTTP/HTTPS proxy to use when connecting to the AWS APIs.
    * If supplied, Axonius will utilize the proxy when connecting to the AWS APIs.
    * If not supplied, Axonius will connect directly to the AWS APIs.
11. **Filename format** *(optional, default: empty)* - Specify a fixed file name, format or use the default file format. The file name appears as Backup Source on the Devices page.
    * If supplied, the asset file name and its format will be as specified.
      * The following parameters are supported: year, month, day, hour, minute, second
      * For example: core*1*`{year}`*`{month}`*`{day}`\_`{hour}`:`{minute}`:`{second}`.extension
      * The supplied value can contain slashes "/" to specify a folder to place the data in.
    * If not supplied, the asset file format will be as follows:
      * axonius\_backup\_\_\_\_.tar.gz.gpg
      * For example: axonius\_backup\_Master\_axonius\_10.0.2.3\_2020-10-04\_03:54:11.718614.tar.gz.gpg
12. **Upload CVEs to Central Core** - Select this option to upload data from the Aggregated Security Findings module to the central core.
13. **Upload Software data to Central Core** - Select this option to upload data from the Software Management module to the central core.

### Required Ports

* Port TCP 443

### Required Permissions

The values supplied in **AWS Access Key ID** and **AWS Access Key Secret** or the EC2 instance (Axonius installed on) attached IAM role account must have the following permissions:

* s3:PutObject
* s3:GetObject
* s3:ListBucket
* s3:PutObjectTagging
* s3:DeleteObject

Those permissions must be added to a policy attached to relevant IAM user account. For details on creating an IAM user and attaching policies, see [Connecting the Amazon Web Services (AWS) Adapter](/docs/connecting-aws-adapter-using-iam-user).

## Azure Blob Storage Settings

![AzureBlobStorage](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/CentralCore-AzureBlob.png)

1. **Operation Mode** - See [Operation Mode](#operation-mode).
2. **Gateway** *(optional)* - Select the gateway to use for backup. When a gateway is selected, all backup/restore operations are routed through it.
3. **Data encryption passphrase (min. 16 characters)** *(required, default: empty)* - Specify a passphrase for the created file. The passphrase must consist of at least 16 characters.
4. **Storage container name** *(required, default: empty)* - The Azure Storage container name.
5. **Connection string** *(required, default: empty)* - The connection string that includes the authorization information required to access data in the Azure Storage account.
6. **Upload CVEs to Central Core** - Select this option to upload data from the Aggregated Security Findings module to the central core.
7. **Upload Software data to Central Core** - Select this option to upload data from the Software Management module to the central core.

### Required Ports

* Port TCP 443

### Prerequisite

Azure storage performance type may be **Standard** or **Premium** as long at it supports **Block blobs**.

### Required Permissions

The values supplied in **Storage container name** and **Connection string** must have read (for the central core node) / write (for the core node) privileges in the folder that contains the assets file.

To configure the **Storage container name** and **Connection string**:

1. Log in to your Azure account.
2. From the **Home** blade, search for and open **Storage Accounts**.
3. If you have a storage account already created, you can use that. Alternately, you can choose to create a new storage account.
   1. Click the **+ Add** button to add a new **Storage Account**.
   2. On the **Create storage** account blade, choose the appropriate **Subscription** and **Resource group**. Specify a name for the storage account, and a preferred location. If you have security or other requirements to further define the account, set those as appropriate.
   3. Click **Review** and **Create**.
4. Back in the **Storage accounts** blade, click on the **Storage account** that you would like to use.
5. In the menu on the left, choose **Access keys**.
6. Copy the connection string for either key1 or key2.

<Callout icon="📘" theme="info">
  Note

  Please note that when you rotate your storage account keys, you will need to update the **Connection string** in Axonius.
</Callout>

## SMB Share Settings

![SMB\_Share](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/CentralCore-SMBShare.png)

1. **Operation Mode** - See [Operation Mode](#operation-mode).
2. **Gateway** *(optional)* - Select the gateway to use for backup. When a gateway is selected, all backup/restore operations are routed through it.
3. **Data encryption passphrase (min. 16 characters)** *(required, default: empty)* - Specify a passphrase for the created file. The passphrase must consist of at least 16 characters.
4. **SMB port** *(optional, default: empty)* - The SMB port.
   * If supplied, the specified port will be used.
   * If not supplied, If **Use 'NetBIOS over TCP' (NBT)** is enabled, port TCP 139 will be used. Otherwise, port TCP 445 will be used.
5. **SMB share path** *(required)* - Specify the SMB share path, The SMB share path should be in the following format: `&lt;hostname/ip_address&gt;\path\to\directory`. For example `127.0.0.1\local_share\home\elizabeth`
6. **User name** and **Password** *(optional, default: empty)* - Specify the SMB share user name and password, if required.
7. **Use 'NetBIOS over TCP' (NBT)** *(required, default: False)* - Specify whether to verify the server's name via NetBios for this connection.
   * If enabled, Axonius will verify the server's name via NetBios for this connection.
   * If disabled, Axonius will not verify the server's name via NetBios for this connection.
8. **Upload CVEs to Central Core** - Select this option to upload data from the Aggregated Security Findings module to the central core.
9. **Upload Software data to Central Core** - Select this option to upload data from the Software Management module to the central core.

### Required Ports

* If **Use 'NetBIOS over TCP' (NBT)** is enabled - port TCP 139
* If **Use 'NetBIOS over TCP' (NBT)** is disabled - port TCP 445

### Required Permissions

SMB requires read (for the central core node) / write (for the core node) privileges in the folder that contains the assets file.

## SSH Settings

![SSH](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/CentralCore-SSH.png)

Use this option to back up and restore central core to servers that support the SSH protocol.

1. **Operation Mode** - See [Operation Mode](#operation-mode).
2. **Gateway** *(optional)* - Select the gateway to use for backup. When a gateway is selected, all backup/restore operations are routed through it.
3. **Data encryption passphrase (min. 16 characters)** *(required, default: empty)* - Specify a passphrase for the created file. The passphrase must consist of at least 16 characters.
4. **Host** - DNS Address or IP of the machine to connect to.
5. **Port** - The port to connect through. If you do not enter a port, port 22 is used by default.
6. **Username** - Username to connect to the server.
7. **Password** - Password to connect to the server.
8. **Private Key** - A private key certificate (PEM format) for the SSH user.
9. **Directory Absolute Path** - The path where the files will be uploaded to / downloaded from.
10. **Upload CVEs to Central Core** - Select this option to upload data from the Aggregated Security Findings module to the central core.
11. **Upload Software data to Central Core** - Select this option to upload data from the Software Management module to the central core.

### Required Permissions

The user defined in the connection will need to have read and write permissions for the target directory.

## Operation Mode

**Backup every cycle** - Select to take an entire snapshot of all assets, archive the snapshot and upload it to the storage, thereby allowing a central core instance to download it. This is the default value.

**Restore during cycle** - Reserved for use by Axonius.

**Disabled** - When you set this option, the storage credentials are stored, but backup files are not downloaded or uploaded.