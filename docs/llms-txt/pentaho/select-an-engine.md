# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/run-configurations-work-with-transformations/select-an-engine.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/run-configurations-work-with-transformations/select-an-engine.md

# Select an Engine

You can select the **Pentaho Engine** to run transformations in the default Pentaho (Kettle) environment.

You can also use the **Spark Submit** job entry to run big data transformations on your Hadoop cluster to coordinate large amounts of data over multiple nodes. See [Spark Submit](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/spark-submit) for details.

## Pentaho Engine

The Pentaho engine does not execute sub-transformations or sub-jobs when you select the **Pentaho server** or **Slave server** option. If you want to run a sub-transformation on the same server where your parent job runs, select **Local** for the **Run Configuration** type.

![Run Configuration Dialog Box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a8331438d2d8d77571fd63ddffbbd9ec7b2b59ab%2FPDI_Transformation%20Run-Configuration%20for%20Pentaho%20Engine_Dialog.png?alt=media)

The **Settings** section of the Run configuration dialog box contains the following options when **Pentaho** is selected as the **Engine** for running a transformation:

| Option                           | Description                                                                                                                                                                                                                                                                                                                      |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Local**                        | Select this option to use the Pentaho engine to run a transformation on your local machine.                                                                                                                                                                                                                                      |
| **Pentaho server**               | Select this option to run your transformation on the Pentaho Server. This option only appears if you are connected to a [Pentaho Repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi).                                                                              |
| **Slave server**                 | Select this option to send your transformation to a slave (remote) server or Carte cluster.                                                                                                                                                                                                                                      |
| **Location**                     | <p>If you select <strong>Slave server</strong>, specify its location.</p><p>If you have set up a Carte cluster, you can specify <strong>Clustered</strong>. See <a href="../../../../advanced-topics-pentaho-data-integration-overview/use-carte-clusters">Use Carte Clusters</a> for more details.</p>                          |
| **Send resources to the server** | If you specified a remote server for your remote **Location**, select to send your transformation to the specified server before running it. Select this option to run the transformation locally on the server. Any related resources, such as other referenced files, are also included in the information sent to the server. |
| **Log remote execution locally** | If you specified **Clustered** for your remote **Location**, select to show the logs from the cluster nodes.                                                                                                                                                                                                                     |
| **Show transformations**         | If you specified **Clustered** for your remote **Location**, select to show the other transformations that are generated when you run on a cluster.                                                                                                                                                                              |
