# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job.md

# Run your job

After [creating a job](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/create-a-job) to orchestrate your ETL activities (such as your transformations), you should run it in the PDI client to test how it performs in various scenarios. With the Run Options window, you can apply and adjust different run configurations, options, parameters, and variables. By defining multiple run configurations, you have a choice of running your job locally or on a server using the Pentaho engine.

When you are ready to run your job, you can perform any of the following actions to access the Run Options window:

* Click the **Run** icon on the toolbar.
* Select **Run** from the **Action** menu.
* Press F9.

The Run Options window appears.

![Run Configuration Window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-2312d7c5b5427d7e4052fa195dd5b6da72d9bdfc%2FPDI_Run-Options_for_Jobs_Window.png?alt=media)

In the Run Options window, you can specify a **Run configuration** to define whether the job runs locally, on the Pentaho Server, or on a slave (remote) server. To set up run configurations, see [Run Configurations](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/run-configurations-work-with-jobs).

**Note:** The default Pentaho local configuration runs the job using the Pentaho engine on your local machine. You cannot edit this default configuration.

The Run Options window also lets you specify logging and other options, or experiment by passing temporary values for defined parameters and variables during each iterative run.

**Always show dialog on run** is set by default. You can deselect this option if you want to use the same run options every time you execute your job. After you have selected to not **Always show dialog on run**, you can access it again through the dropdown menu next to the **Run** icon in the toolbar, through the **Action** main menu, or by pressing F8.
