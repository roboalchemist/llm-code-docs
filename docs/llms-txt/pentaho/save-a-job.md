# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/save-a-job.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/save-a-job.md

# Save a job

The method you use to save a job depends on if you are using PDI locally on your machine or if you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi). If you are connected to a repository, you are remotely saving your file on the Pentaho Server. Optionally, you can save a job on a Virtual File System (VFS).

## On your local machine

Follow these instructions to save a job on your local machine.

1. In the PDI client, perform one of the following actions:
   * Select **File** > **Save** or **File** > **Save as**.
   * Click the **Save current file** icon in the toolbar.
   * Hold down the CTRL S keys.\
     The Save As window appears.
2. Specify the job's name in the window and select the location.

   By default, the folder from where the last file is accessed is opened.

   **Note:** The file types allowed are .ktr or.kjb.
3. Click **Save**.

The window closes when your job is saved.

## In the Pentaho Repository

Follow these instructions to save a job to the Pentaho Repository.

1. Verify that you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi), which establishes remote access to the Pentaho Server.
2. In the PDI client, perform one of the following actions:
   * Select **File** > **Save** or **File** > **Save as**.
   * Click the **Save current file** icon in the toolbar.
   * Hold down the CTRL S keys.\
     The Save As window opens.
3. Navigate to the repository folder where you want to save your job.

   By default, the folder from where the last file was accessed is opened.
4. Specify the job's name in the **File name** field.

   **Note:** The file types allowed are .ktr or.kjb.
5. Click **Save**.

The window closes when your job is saved.

## On Virtual File Systems

From the menu bar in the PDI client, select **File** > **Open** to save a PDI job on a Virtual File System (VFS). See [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser) for details.
