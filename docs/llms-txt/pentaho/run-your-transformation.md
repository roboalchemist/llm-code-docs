# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation.md

# Run your transformation

After creating a transformation as a network of steps (a data workflow) that performs your ETL tasks, you should run it in the PDI client to test how it performs in various scenarios. With the Run Options window, you can apply and adjust different run configurations, options, parameters, and variables.

When you are ready to run your transformation, you can perform any of the following actions to access the Run Options window:

* Click the **Run** icon on the toolbar.
* Select **Run** from the **Action** menu.
* Press F9.

The Run Options window appears.

![Run Options Window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-14b808664c8a48a54b73edb431a93ed452e3e8de%2FssPDIRunOptions.png?alt=media)

In the Run Options window, you can specify a **Run configuration**. To set up run configurations, see [Run configurations](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/run-configurations-work-with-jobs).

**Note:** The default Pentaho local configuration runs the transformation using the Pentaho engine on your local machine. You cannot edit this default configuration.

The Run Options window also lets you specify logging and other options, or experiment by passing temporary values for defined parameters and variables during each iterative run.

**Always show dialog on run** is set by default. You can deselect this option if you want to use the same run options every time you execute your transformation. After you have selected to not **Always show dialog on run**, you can access it again through the dropdown menu next to the **Run** icon in the toolbar, through the **Action** main menu, or by pressing F8.

After running your transformation, you can use the [Execution panel](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/analyze-your-transformation-results) to analyze the results.
