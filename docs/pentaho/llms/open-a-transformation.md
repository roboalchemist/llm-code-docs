# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/open-a-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/open-a-transformation.md

# Open a transformation

The method you use to open an existing transformation depends on if you are using PDI locally on your machine or if you are connected to a repository. If you are connected to a repository, then you are remotely accessing your file on the Pentaho Server. Optionally, you can open a transformation on a Virtual File System (VFS).

**Note:** If you get a message indicating that a plugin is missing, see the [Troubleshooting transformation steps and job entries](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/troubleshooting-transformation-steps-and-job-entries) section for more details.

If you recently had a file open, you can also use **File** > **Open Recent**.

## On your local machine

Follow these instructions to open a transformation on your local machine.

1. In the PDI client, perform one of the following actions:
   * Select **File** > **Open**.
   * Click the **Open file** icon in the toolbar.
   * Click the **OPEN Files** tile from the **Welcome** screen.
   * Hold down the CTRLO keys.
2. Select the file from the Open window, then click **Open**.

   **Note:** By default, the folder from where the last file was accessed is opened.

The Open window closes when your transformation appears in the canvas.

## In the Pentaho Repository

Follow these instructions to access a transformation in the Pentaho Repository.

1. Verify that you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi), which establishes remote access to the Pentaho Server.
2. In the PDI client, perform one of the following actions to access the Open repository browser window:
   * Select **File** > **Open**.
   * Click the **Open file** icon in the toolbar.
   * Click the **OPEN Files** tile from the **Welcome** screen.
   * Hold down the CTRLO keys.**Note:** By default, the folder from where the last file was accessed is opened.
3. To use a recently opened file, use the **Recents** option to navigate to your transformation.
4. Use either the search box to find your transformation, or use the left panel to navigate to a repository folder containing your transformation.

   **Note:** If the PDI is already connected to the Pentaho Repository, then only the Recents and Pentaho Repository options appear in the left pane. If the PDI is not connected to a Pentaho Repository, then the following options appear in the left pane:

   * Recents
   * Local
   * VFS Connections
   * Hadoop Clusters
5. If you are not connected to Pentaho Repository, then perform one of the following actions to access the transformation:
   * Double-click on your transformation.
   * Select it and press the Enter key.
   * Select it and click **Open**.
6. If you are connected to the Pentaho Repository, click **Open** to access the transformation.

The Open window closes when your transformation appears in the canvas.

## On Virtual File Systems

From the menu bar in the PDI client, select **File** > **Open** to open a PDI transformation on a Virtual File System (VFS). See [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser) for details.
