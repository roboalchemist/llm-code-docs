# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/analyze-your-transformation-results.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/analyze-your-transformation-results.md

# Analyze your transformation results

You can see how your transformation performed, if errors occurred, and explore the data by viewing the execution results.

After you [Run your transformation](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation), the **Execution Results** panel appears. It contains several different tabs that help you to see how the transformation ran, pinpoint errors, and monitor performance.

## Step metrics

The **Step Metrics** tab shows statistics for each step in your transformation including how many records were read, written, caused an error, processing speed (rows per second) and more. This tab also indicates whether an error occurred in your transformation step. If a mistake had occurred, steps that caused the transformation to fail will be highlighted in red. In the example below, the Lookup Missing Zips step caused an error.

![Step Metrics](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-bb3c944d0428ae51d067cd69ce5c661d8d641322%2FssPDIExecutingTransformation.png?alt=media)

## Logging

The **Logging** tab displays the logging details for the most recent execution of the transformation. You can also drill in deeper to determine where errors occur. Error lines are highlighted in red. In the example below, the Lookup Missing Zips step caused an error because it attempted to lookup values on a field called **POSTALCODE2**, which did not exist in the lookup stream.

![Logging Details](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-97a0ba0a3953598b2e5b734a845aeeb5a791cf16%2FssPDIExecuteTransformationLogging.png?alt=media)

## Execution history

The **Execution History** tab enables access to the Step Metrics and Logging information from previous executions of your transformation. This history only works if you have configured your transformation to log to a database through the **Logging** tab of the Transformation Settings dialog box. For more information on configuring logging, see [Logging and performance monitoring](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring).

## Performance graph

The **Performance Graph** enables you to analyze the performance of steps based on a variety of metrics including how many records were read, written, caused an error, processing speed (rows per second) and more. Like the **Execution History**, this graph requires you to configure your transformation to log to a database through the **Logging** tab of the Transformation Settings dialog box.

## Metrics

The **Metrics** tab shows a Gantt chart after your transformation executes. It contains information such as how long it takes to connect to a database, how much time is spent executing a SQL query, or how long it takes to load a transformation.

![Transformation Metrics](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-66290290e74564ce6613c65f0cf78eb8d884ab19%2FssPDIExecuteTransformationMetrics.png?alt=media)

## Preview data

Use the **Preview Data** tab to display a preview of the data per each step of your PDI transformation.

Click on a step to show the data values for that step, as shown in the following example:

![Preview Data](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-88c92683462fed541ce49b1002047b17403bcf15%2FssPDI_ExecutionPanel_InspectingData.png?alt=media)
