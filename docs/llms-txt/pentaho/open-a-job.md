# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/open-a-job.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/open-a-job.md

# Open a job

The method you use to open an existing job depends on if you are using PDI locally on your machine or if you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi). If you are connected to a repository, you are remotely accessing your file on the Pentaho Server. Optionally, you can open a job on a Virtual File System (VFS).

**Note:** If you get a message indicating that a plugin is missing, see [Troubleshooting Transformation Steps and Job Entries](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/troubleshooting-transformation-steps-and-job-entries) for more details.

If you recently had a file open, you can also use **File** > **Open Recent**.

## On your local machine

Follow these instructions to open a job on your local machine.

1. In the PDI client, perform one of the following actions:
   * Select **File** > **Open**.
   * Click the **Open file** icon in the toolbar.
   * Click the **OPEN Files** tile from the Welcome screen.
   * Hold down the CTRL O keys.
2. Select the file from the Open window, then click **Open**.

   **Note:** By default, the folder from where the last file was accessed is opened.

The Open window closes when your job appears in the canvas.

## In the Pentaho Repository

Follow these instructions to access a job in the Pentaho Repository.

1. Verify that you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi), which establishes remote access to the Pentaho Server.
2. In the PDI client, perform one of the following actions to access the Open repository browser window:
   * Select **File** > **Open**
   * Click the **Open file** icon in the toolbar.
   * Hold down the CTRLO keys.

     **Note:** By default, the folder from where the last file was accessed is opened.
3. To use a recently opened files, use the **Recents** option to navigate to your job.
4. Use either the search box to find your job, or use the left panel to navigate to a repository folder containing your job.

   **Note:** If the PDI is already connected to the Pentaho Repository, then only the **Recents** and **Pentaho Repository** options appear in the left pane. If the PDI is not connected to a Pentaho Repository, then the following options appear in the left pane:

   * Recents
   * Local
   * VFS Connections
   * Hadoop Clusters
5. If you are not connected to Pentaho Repository, then perform one of the following actions to access the job:
   * Double-click on your job.
   * Select it and press the **Enter** key.
   * Select it and click **Open**.
6. If you are connected to the Pentaho Repository, click **Open** to access the job.

The Open window closes when your job appears in the canvas.

## On Virtual File Systems

From the menu bar in the PDI client, select **File** > **Open** to open a PDI job on a Virtual File System (VFS). See [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser) for details.

<br>
