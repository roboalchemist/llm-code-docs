# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/run-configurations-work-with-transformations.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/run-configurations-work-with-transformations.md

# Run configurations

Some ETL activities are lightweight, such as loading in a small text file to write out to a database or filtering a few rows to trim down your results. For these activities, you can run your transformation locally using the default Pentaho engine. Some ETL activities are more demanding, containing many steps calling other steps or a network of transformation modules. For these activities, you can set up a separate Pentaho Server dedicated for running transformations using the Pentaho engine. Other ETL activities involve large amounts of data on network clusters requiring greater scalability and reduced execution times. For these activities, you can run your transformation using the **Spark Submit** job entry.

You can create or edit run configurations through the **Run configurations** folder in the **View** tab as shown below:

![Run Configurations Folder](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-8a2167ce5dee539dc1aeef3cab3202a8c028ffa6%2FPDI_Transformation%20View%20Tab%20in%20Run-Options_Panel.png?alt=media)

To create a new run configuration, right-click on the **Run configurations** folder and select **New**. To edit or delete a run configuration, right-click on an existing configuration.

**Note:** **Pentaho local** is the default run configuration. It runs transformations with the Pentaho engine on your local machine. You cannot edit this default configuration.

Selecting **New** or **Edit** opens the Run configuration dialog box that contains the following fields:

| Field           | Description                                        |
| --------------- | -------------------------------------------------- |
| **Name**        | Specify the name of the run configuration.         |
| **Description** | Optionally, specify details of your configuration. |
