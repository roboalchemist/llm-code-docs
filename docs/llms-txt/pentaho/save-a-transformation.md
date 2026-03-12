# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/save-a-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/save-a-transformation.md

# Save a transformation

The method you use to save a transformation depends on if you are using PDI locally on your machine or if you are connected to a repository. If you are connected to a repository, you are remotely saving your file on the Pentaho Server. Optionally, you can save a transformation on a Virtual File System (VFS) if you are not connected to the Pentaho Repository.

## On your local machine

Follow these instructions to save a transformation on your local machine.

1. In the PDI client, perform one of the following actions:
   * Select **File** > **Save** or **File** > **Save as**.
   * Click the **Save current file** icon in the toolbar.
   * Hold down the CTRL S keys.\
     The Save As window opens.
2. Specify the transformation's name in the window and select the location.

   By default, the folder from where the last file was accessed is opened.

   **Note:** The file types allowed are .ktr or.kjb.
3. Click **Save**.

   The transformation is saved.

The window closes when your transformation is saved.

## In the Pentaho Repository

Follow these instructions to save a transformation to the Pentaho Repository.

1. Verify that you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi), which establishes remote access to the Pentaho Server.
2. In the PDI client, perform one of the following actions:

   * Select **File** > **Save** or **File** > **Save as**.
   * Click the **Save current file** icon in the toolbar.
   * Hold down the CTRLS keys.\
     The Save As window opens. By default, the folder from where the last file was accessed is opened.

   **Note:** The file types allowed are .ktr or.kjb.
3. Navigate to the repository folder where you want to save your transformation.
4. Specify the transformation's name in the **File name** field.
5. Click **Save**.

The window closes when your transformation is saved. If the transformation already exists, an overwrite warning message appears. Click **OK** to overwrite the existing transformation.

## On Virtual File Systems

From the menu bar in the PDI client, select **File** > **Open** to save a PDI transformation on a Virtual File System (VFS). See [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser) for details.
