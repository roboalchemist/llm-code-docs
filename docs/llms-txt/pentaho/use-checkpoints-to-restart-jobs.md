# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-checkpoints-to-restart-jobs.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-checkpoints-to-restart-jobs.md

# Use checkpoints to restart jobs

Checkpoints let you restart [PDI jobs](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/basic-concepts-of-pdi#jobs) that fail without you having to rerun the entire job from the beginning. You add checkpoints at hops that connect one job entry to another. Then, when you run the job and a checkpoint is encountered, the software saves the state of the job entry, including the parameters, internal result rows, and result files. If an error occurs that causes the job to fail, like the database is not functioning properly so you can't connect to it, the job ends. But, when the error is resolved and you restart the job, instead of the job starting at the beginning, it starts at the last checkpoint before the error occurred. Because the state of the job entry performed up to the checkpoint was saved, the job resumes as if the failure had not occurred. In addition to setting up checkpoints, you need to set up a checkpoint log. The checkpoint log tracks each time a job runs and where failures occur. This can be helpful for troubleshooting.

## Add a checkpoint

To add a checkpoint, complete these steps.

1. In Spoon, open a job.
2. Right-click a step or transformation in the job, then select **Restartable Checkpoint** from the menu that appears.

The checkpoint is added to the job.

## Delete a checkpoint

To delete a checkpoint, complete these steps.

1. In Spoon, open a job.
2. Right-click a step or transformation in the job, then select **Clear Checkpoint Marker** from the menu that appears.

The checkpoint is cleared from the job.

## Set up a checkpoint log

To set up a checkpoint log, complete these steps.

1. In Spoon, open a job.
2. Right-click in an empty space in the job’s tab that appears in the Spoon window. In the Properties window, click the **Log** tab.
3. Select **Checkpoints log table**.

   ![Job Properties Dialog Box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b1c2d6aed0ad3a865bd09aa3cf5fc6a1f399a22f%2Fcheckpointlogtable1.png?alt=media)
4. Add the log connection and the name of the log table, as well as other information as needed.
5. Choose the log table fields you want enabled.
6. When complete, click **OK**.
