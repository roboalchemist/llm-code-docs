# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/pentaho-address-to-a-vfs-connection-open-a-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/pentaho-address-to-a-vfs-connection-open-a-transformation.md

# Pentaho address to a VFS connection

The Pentaho address is the Pentaho virtual file system (`pvfs`) location within your VFS connection. When you are locating a file under the VFS connection category in the file access dialog box, the directory path in your Virtual File System appears in the address text box.

![VFS navigation path in the Open dialog box in the PDI client](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-737c2cdaff12fc62694969d198861a1a1d3f6cdd%2FssPDI_OpenDialogBox_VFSAddressBar.png?alt=media)

When you click in the address bar, the Pentaho address to the file appears in the text box.

![PVFS file path in the Open dialog box in the PDI client](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f45eca9a3b4549e688d42d86915311abff88aa3d%2FssPDI_OpenDialogBox_VFSAddressBar_PVFSPath.png?alt=media)

You can copy and paste a Pentaho address into file path options of PDI steps and entries that support VFS connections.

**Note:** You must use the Pentaho virtual file system for anything related to Amazon S3. In addition, file paths and permissions in your existing transformations and jobs that use Amazon S3 are supported when **Amazon S3** is the **Default S3 Connection**.
