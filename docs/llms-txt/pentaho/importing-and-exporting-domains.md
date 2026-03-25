# Source: https://docs.pentaho.com/pba-metadata-editor/readme/importing-and-exporting-domains.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/get-started-with-pentaho-metadata-editor-cp/importing-and-exporting-domains.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/get-started-with-pentaho-metadata-editor-cp/importing-and-exporting-domains.md

# Importing and exporting domains

When you save a domain, it is stored in a metadata repository. The Pentaho Server does not use the metadata repository. Instead, it accesses an XML file exported from the Pentaho Metadata Editor. Exporting your domain is a good way to ensure safe backups of your domains. When you import a new domain, it becomes the active domain in the Pentaho Metadata Editor.

## Import a domain

Perform the following steps to import a domain:

1. In the Pentaho Metadata Editor, go to **File** > **Import From XMI File**.

   **Note:** You may be prompted to save the currently active model if you have any unsaved changes pending.
2. In the file browser, select your domain file and click **OK**.
3. In the Save Model dialog box, type a name for the domain.

   If you enter the name of an existing domain, that domain is overwritten by the import.

## Export a domain

Perform the following steps to export a domain:

1. In the Pentaho Metadata Editor, go to **File** > **Export to XMI File**.

   **Note:** You may be prompted to save the currently active model if you have any unsaved changes pending.
2. Type a file name and select a location to save your file.

   The default extension for a metadata domain XML file is `.xmi`.
3. Click **Save**.

Once you have entered a name for your export file, the domain is exported to that file. You can inspect the export file using a text editor to view the underlying XML code.

## Domain backup and recovery

Each domain can be saved to the Common Warehouse Metadata (CWM) repository with any name you like. The **Save** and **Save As** options are available from both the Pentaho Metadata Editor file menu and the toolbar. Each time a domain is saved to the repository, a recovery export file of the domain is saved to the file system, under the `.pentaho-meta` directory. This directory is typically located in the your `home` directory. The recovery file contains the last successfully saved state of the domain. The files are named `recovery_[*studio:domainname*].xmi.`

Domain restoration may be necessary if you need to revert to the last known good state of your domain in the event of repository errors or corruption. You can restore a domain to the last saved state by importing a recovery file.
