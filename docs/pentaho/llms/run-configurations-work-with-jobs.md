# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/run-configurations-work-with-jobs.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/run-configurations-work-with-jobs.md

# Run configurations

Some ETL activities are lightweight, such as loading in a small text file to write out to a database or filtering a few rows to trim down your results. For these activities, you can run your job locally using the default Pentaho engine. Some ETL activities are more demanding, containing many entries and steps calling other entries and steps or a network of modules. For these activities, you can set up a separate Pentaho Server dedicated for running jobs and transformations using the Pentaho engine.

You can create or edit these configurations through **Run configurations** in the **View** tab as shown below:

![Run Configuration Selection](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b4173a84f56146108cd442d9078492ed2ccfcde2%2FPDI_View_Tab_in_Run-Options_Panel.png?alt=media)

To create a new run configuration, right-click on **Run configurations** and select **New**. To edit or delete a run configuration, right-click on an existing configuration.

**Note:** Pentaho local is the default run configuration. It runs jobs with the Pentaho engine on your local machine. You cannot edit this default configuration.

Selecting **New** or **Edit** opens the Run configuration dialog box that contains the following fields:

| Field           | Description                                        |
| --------------- | -------------------------------------------------- |
| **Name**        | Specify the name of the run configuration.         |
| **Description** | Optionally, specify details of your configuration. |
