# Source: https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/file-exists-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/file-exists-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/file-exists-job-entry.md

# File Exists (Job Entry)

The File Exists job entry verifies the existence of a file on the selected file system by checking filenames, and returns a `True` or `False` value, accordingly.

![File Exists](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-22f69f5dd74ee56492dbab2a1c1c9f8a45665c47%2FPDI_FileExists_Job_Dialog.png?alt=media)

The following fields are available to this job entry:

| Field              | Description                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Job entry name** | Specify the unique name of the File exists job entry on the canvas. You can customize the name or leave it as the default. A job entry can be placed on the canvas several times; however, it will be the same job entry.                                                                                                                                                        |
| **File name**      | Specify the filename and path of the file to verify. Click **Browse** to navigate to the source file or folder through the VFS browser. See [VFS browser](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems) for more information.. |
