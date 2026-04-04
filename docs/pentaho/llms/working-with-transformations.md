# Source: https://docs.pentaho.com/pba/pipeline-designer/working-with-transformations.md

# Source: https://docs.pentaho.com/pdia-data-integration/pipeline-designer/working-with-transformations.md

# Working with transformations

Create, configure, and run transformations to perform ETL tasks in Pipeline Designer. After you run a transformation, review logs and step metrics to validate results and troubleshoot issues.

{% hint style="info" %}
To schedule transformations to run one time or on a recurring schedule, use the Pentaho Data Integration client (Spoon). See [Manage PDI transformations and job schedules](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/manage-pdi-transformations-and-job-schedules).
{% endhint %}

### Create a transformation

Create a transformation to arrange a network of ETL tasks (steps) into a data workflow.

1. Log in to the Pentaho User Console.
2. Open **Pipeline Designer**:
   * If you are using the **Modern Design**, select **Pipeline Designer** from the left menu.
   * If you are using the **Classic Design**, select **Switch to the Modern Design**, then select **Pipeline Designer**.
3. In the **Transformation** card, select **Create Transformation**.
4. Add steps:
   1. In the **Design** pane, search for or browse to the steps you need.
   2. Drag steps onto the canvas.
5. Configure steps by hovering over a step and selecting an action:
   * **Delete**: Remove the step from the canvas.
   * **Edit**: Configure step properties.
     * To learn more about a step while configuring it, select **Help** in the step dialog.
   * **Duplicate**: Add a copy of the step to the canvas.
   * **More Actions** > **Change Number of Copies**: Run multiple copies of a step in parallel.
   * **More Actions** > **Data Movement**: Control how rows flow to downstream step copies:
     * **Round-robin** (default): Distribute rows evenly across downstream step copies.
     * **Load balance**: Send rows to the downstream copy with the lightest load.
     * **Copy data to next steps**: Send each row to all downstream copies.
6. Add hops (connections) between steps:
   * Hover over a step handle until the plus sign (+) appears.
   * Drag from the plus sign to another step handle.
7. Optional: Add a note to the canvas.
   * Use the canvas toolbar, or see [Use notes on canvas](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/use-notes-on-canvas).
8. Save the transformation:
   1. Select **Save**.
   2. In **Select File or Directory**, pick the target folder.
   3. Optional: Create a folder by selecting **New Folder**.
   4. Select **Save**, then confirm in **Save Change**.

### Edit transformation properties

Transformation properties describe the transformation and control how it runs.

#### Dependencies tab

Use **Dependencies** to document and validate upstream tables your transformation depends on. This is useful when you need to detect source table changes by using a “last changed” field.

Select **Get dependencies** to detect dependencies automatically.

| Setting    | Description                                              |
| ---------- | -------------------------------------------------------- |
| Connection | Select a database connection used by the transformation. |
| Table      | Select a table from the selected connection.             |
| Field      | Select a field within the selected table.                |

#### Miscellaneous tab

Use **Miscellaneous** to tune buffers and logging feedback, and to configure transactional behavior.

| Setting                                        | Description                                                                                                                            |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Number of rows in rowset                       | Size of the buffers between connected steps. Change only if you are memory constrained.                                                |
| Show a feedback row in transformation steps?   | Adds periodic feedback entries to the log during execution. Default is enabled.                                                        |
| The feedback size                              | Number of rows between feedback log entries. Increase this for large runs to reduce log volume.                                        |
| Make the transformation database transactional | Uses a single transactional connection per database connection and rolls back on failure. Commit happens after the last step finishes. |
| Shared objects file                            | Location of the XML file for shared objects (connections, cluster schemas, and more).                                                  |
| Manage thread priorities?                      | Enables thread-priority tuning based on rowset buffer levels. Disable if the overhead outweighs benefits.                              |

#### Monitoring tab

Use **Monitoring** to enable step performance monitoring and control how often metrics are sampled.

| Setting                                    | Description                                                                                            |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| Enable step performance monitoring?        | Collects per-step throughput and I/O metrics for viewing in the execution results (performance graph). |
| Step performance measurement interval (ms) | Snapshot interval in milliseconds (example: `10`).                                                     |
| Maximum number of snapshots in memory      | Maximum number of metric snapshots retained during runtime.                                            |

### Run a transformation

Run a transformation to execute steps in the order defined by the hops on the canvas.

1. Log in to the Pentaho User Console.
2. Open **Pipeline Designer**:
   * If you are using the **Modern Design**, select **Pipeline Designer** from the left menu.
   * If you are using the **Classic Design**, select **Switch to the Modern Design**, then select **Pipeline Designer**.
3. In the bottom table, select **Recently opened** or **Favorites**.
4. Open the transformation:
   1. Browse to the transformation and select **Open**.
   2. Or select **Open files**, then browse to the transformation and select **Open**.
5. In the **Canvas Action** toolbar, select **Run**, then choose one:
   * **Run**: Start with defaults.
   * **Run options**: Configure options, then select **Run**.

The transformation runs and the **Preview** panel opens with **Logging** selected.

{% hint style="info" %}
To stop a running transformation, see [Stop transformations and jobs](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/stop-transformations-and-jobs).
{% endhint %}

#### Run options

| Option                     | What it does                                                                                                                                                                                                                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Select configuration       | Select the run configuration.                                                                                                                                                                                                                                       |
| Clear log before running   | Clears existing logs before execution.                                                                                                                                                                                                                              |
| Enable safe mode           | Validates that each row matches the first row’s layout.                                                                                                                                                                                                             |
| Gather performance metrics | Collects runtime metrics for step performance. See [Use performance graphs](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/logging-and-performance-monitoring/monitor-performance/use-performance-graphs). |
| Log level                  | Controls the amount of logging. Higher levels can expose sensitive data.                                                                                                                                                                                            |
| Parameters                 | Applies parameter values for this run. See [Parameters](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/pdi-run-modifiers/parameters).                                                                      |
| Variables                  | Applies temporary values for variables for this run. See [Variables](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/pdi-run-modifiers/variables).                                                          |
| Arguments                  | Supplies runtime arguments (max 10). See [Arguments](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/pdi-run-modifiers/arguments).                                                                          |

### Analyze transformation results

Analyze results to identify errors, preview data, and assess performance using logs and step metrics. After you run a transformation, **Execution Results** opens at the bottom of the canvas.

You can do the following:

* Expand results by selecting **Expand Preview**.
* Delete logs by selecting **Delete all logs**.
* Close the panel, then re-open it later from the **Canvas Action** toolbar by selecting **Logs**.

#### Logging

The **Logging** tab shows logging details for the most recent execution. Error lines are highlighted in red.

#### Preview data

The **Preview Data** tab shows a preview of data for each step. Select a step to view its output.

#### Step metrics

The **Step Metrics** tab shows per-step statistics, including rows read and written, errors, and processing speed (rows per second). Steps that caused a failure are highlighted in red.

### Transformation steps

Steps extend and expand transformation functionality. Add steps from the **Design** pane, then connect them with hops.

For the full reference list, see [PDI transformation steps](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview).
