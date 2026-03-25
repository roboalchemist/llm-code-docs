# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/use-the-vfs-browser-in-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/use-the-vfs-browser-in-the-pdi-client.md

# Access files with the VFS browser

Perform the following steps to access your files with the VFS browser.

1. Select **File** > **Open** in the PDI client to open the VFS browser.

   The Open dialog box appears.

   ![Open dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e0db2371f2c71a4ffa02b6e8278820440e1b56b1%2FPDI%20Open%20file%20dialog%20box.png?alt=media)
2. In the left pane, select the type of file system. The following file systems are supported:
   * **Local**: Opens files on your local machine. Use the folders in the **Name** panel of the Open dialog box to select a resource.
   * **Hadoop Cluster**: Opens files on any Hadoop cluster except S3. Click the **Hadoop Cluster** drop-down box to select your cluster, then the resource you want to access.
   * **HDFS**: Opens files on Hadoop distributed file systems. Select the cluster you want for the **Hadoop Cluster** option, then select the resource you want to access.
   * **Google Drive**: Opens files on the Google file system. You must configure PDI to access the Google file system. See [Access to a Google Drive](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/access-to-a-google-drive) for more information.
   * **VFS Connections**: Opens files using a stored set of VFS properties to connect to a specific file system.
     * **Amazon S3/Minio/HCP**
     * **Azure Data Lake Gen 1**
     * **Azure Data Lake Gen 2 / Blob**
     * **Google Cloud Storage**
     * **HCP REST**
     * **Local**
     * **SMB/UNC Provider**
     * **Snowflake Staging**
3. Alternatively, in the **Address** bar, enter the VFS URI.

   The following examples are VFS URI addresses:

   * **Local**: `ftp://userID:password@ftp.myhost.com/path_to/file.txt`
   * **HDFS**: `hdfs://myusername:mypassword@mynamenode:port/path`
   * **SMB/UNC Provider**: `smb://<domain>;<username>:<password>@<server>:<port>/<path>`**Note:** The SMB “domain” is the Windows host name, for example, and “domain” and “server” can be the same in the case of an IP address.
4. (Optional) Select another value in the **File type** menu to filter on file types other than transformations and jobs, which is the default value.
5. (Optional) Select a file or folder and click the **X** icon in the upper-right corner of the browser to delete it.
6. (Optional) click the **+** icon to create a new folder.

**Note:** VFS dialog boxes are configured through specific transformation parameters. See [Configure VFS options](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/configure-vfs-options) for more information.
