# Source: https://docs.pentaho.com/pba/pipeline-designer/working-with-transformations/analyze-transformation-results.md

# Analyze transformation results

Analyze transformation results to identify errors, explore data previews, and assess performance using logs and step metrics. After you [Run a transformation](https://docs.pentaho.com/pba/pipeline-designer/working-with-transformations/run-a-transformation), the Execution Results open at the bottom of the canvas with tabs that help you to see how the transformation ran and pinpoint errors.

You can take the following actions in the Execution Results pane:&#x20;

* To open a larger view of the execution results, click the **Expand Preview** icon. The Execution Results window opens.
* To delete logs, click the **Delete all logs** icon.&#x20;
* To close the Execution Results pane, click the Close icon.

If the Execution Results pane is closed, you can open it from the **Canvas Action** toolbar by clicking the **Logs** icon.

### Logging <a href="#logging" id="logging"></a>

The **Logging** tab displays the logging details for the most recent execution of the transformation. You can also drill in deeper to determine where errors occur. Error lines are highlighted in red.

### Preview data <a href="#preview-data" id="preview-data"></a>

Use the **Preview Data** tab to display a preview of the data per each step of a transformation. Click on a step to show the data values for that step.

### Step Metrics <a href="#metrics" id="metrics"></a>

The **Step Metrics** tab shows statistics for each step in your transformation including how many records were read, written, caused an error, processing speed (rows per second) and more. This tab also indicates whether an error occurred in your transformation step. If a mistake occurs, steps that caused the transformation to fail are highlighted in red.
