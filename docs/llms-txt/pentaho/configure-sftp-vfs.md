# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/parameters/vfs-properties/configure-sftp-vfs.md

# Configure SFTP VFS

To configure the connection settings for SFTP dialog boxes in PDI, you must create either variables or parameters for each relevant value. Possible values are determined by the VFS driver you are using.

You can also use parameters to substitute VFS connection details, then use them in the VFS dialog box where appropriate. For instance, these would be relevant credentials, assuming the parameters have been set:

`sftp://${username}@${host}/${path}`

This technique enables you to hide sensitive connection details, such as usernames and passwords.

You can see examples of these techniques in the VFS Configuration Sample transformation in the `/data-integration/samples/transformations/` directory.
