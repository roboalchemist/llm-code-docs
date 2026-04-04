# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/parameters/vfs-properties.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/parameters/vfs-properties.md

# VFS properties

You can specify VFS properties as parameters.

## Specifying VFS properties as parameters

VFS properties can be specified as [parameters](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/parameters). The format of the reference to a VFS property is **vfs.scheme.property.host**.

The following list describes the subparts of the format:

* The **vfs** subpart is required to identify this as a virtual file system configuration property.
* The **scheme** subpart represents the VFS driver's scheme (or VFS type), such as HTTP, SFTP, or ZIP.
* The **property** subpart is the name of a VFS driver's ConfigBuilder's setter (the specific VFS element that you want to set).
* The **host** optionally defines a specific IP address or hostname that this setting applies to.

You must consult each scheme's API reference to determine which properties you can create variables for. Apache provides VFS scheme documentation at <https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/>. The **org.apache.commons.vfs.provider** package lists each of the configurable VFS providers (FTP, HTTP, SFTP, etc.). Each provider has a **FileSystemConfigBuilder** class that in turn has **set\*(FileSystemOptions, Object)** methods. If a method's second parameter is a **String** or a **number** (Integer, Long, etc.) then you can create a PDI variable to set the value for VFS dialog boxes.

The table below explains VFS properties for the SFTP scheme. Each property must be declared as a PDI variable and preceded by the `vfs.sftp` prefix as defined above.

| SFTP VFS Property         | Purpose                                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **compression**           | Specifies whether ZLIB compression is used for the destination files. Possible values are `zlib` and `none`.                                                             |
| **identity**              | The private key file (fully qualified local or remote path and filename) to use for host authentication.                                                                 |
| **authkeypassphrase**     | The passphrase for the private key specified by the **identity** property.                                                                                               |
| **StrictHostKeyChecking** | If this is set to `no`, the certificate of any remote host will be accepted. If set to `yes`, the remote host must exist in the known hosts file (`~/.ssh/known_hosts`). |

**Note:** All of these properties are optional.

The following examples show how to specify parameters as VFS properties:

![Transformation Properties Example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-69f9f1449fd41326ed32bc0b584dd1b28eeff014%2FTransformationProperties_vfs.png?alt=media)

## Configure SFTP VFS

To configure the connection settings for SFTP dialog boxes in PDI, you must create either variables or parameters for each relevant value. Possible values are determined by the VFS driver you are using.

You can also use parameters to substitute VFS connection details, then use them in the VFS dialog box where appropriate. For instance, these would be relevant credentials, assuming the parameters have been set:

`sftp://${username}@${host}/${path}`

This technique enables you to hide sensitive connection details, such as usernames and passwords.

You can see examples of these techniques in the VFS Configuration Sample transformation in the `/data-integration/samples/transformations/` directory.
