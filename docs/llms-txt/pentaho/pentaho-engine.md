# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/run-configurations-work-with-jobs/pentaho-engine.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/run-configurations-work-with-jobs/pentaho-engine.md

# Pentaho engine

The Pentaho engine does not execute sub-transformations or sub-jobs when you select the **Pentaho server** or **Slave server** option. If you want to run a sub-transformation on the same server where your parent job runs, select **Local** for the **Run Configuration** type.

![Run Configuration Dialog Box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a8331438d2d8d77571fd63ddffbbd9ec7b2b59ab%2FPDI_Job_Run-Configuration_for_Pentaho_Engine_Dialog.png?alt=media)

The Settings section of the Run configuration dialog box contains the following options when **Pentaho** is selected as the **Engine** for running a job:

| Option                           | Description                                                                                                                                                                                                                                                                               |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Local**                        | Select this option to use the Pentaho engine to run a job on your local machine.                                                                                                                                                                                                          |
| **Pentaho Server**               | Select this option to run your job on the Pentaho Server. This option only appears if you are connected to a [Pentaho Repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi).                                                  |
| **Slave server**                 | Select this option to send your job to a slave or remote server.                                                                                                                                                                                                                          |
| **Location**                     | If you select **Slave server**, specify the location of your remote server.                                                                                                                                                                                                               |
| **Send resources to the server** | If you specified a **Location** for a server, select to send your job to the specified server before running it. Select this option to run the job locally on the server. Any related resources, such as other referenced files, are also included in the information sent to the server. |
