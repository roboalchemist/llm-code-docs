# Source: https://docs.pentaho.com/pdia-data-integration/transforming-data-with-pdi.md

# Transforming data with PDI

Transform data and manage jobs in Pentaho Data Integration (PDI).

Use this page to build, run, monitor, and optimize transformations and jobs.

### In this article

* [Work with transformations](#work-with-transformations)
* [Work with jobs](#work-with-jobs)
* [PDI run modifiers](#pdi-run-modifiers)
* [Partitioning data](#partitioning-data)
* [Logging and performance monitoring](#logging-and-performance-monitoring)
* [Add notes to transformations and jobs](#add-notes-to-transformations-and-jobs)
* [Manage PDI transformations and job schedules](#manage-pdi-transformations-and-job-schedules)

### Work with transformations

In the [PDI client (Spoon)](https://docs.pentaho.com/pdia-data-integration/basic-concepts-of-pdi), you can develop transformations.

Transformations are data workflows representing your ETL activities.

Transformation steps define the individual ETL activities.

Transformations are stored in `.ktr` files.

#### Create a transformation

Follow these steps:

1. Do one of the following:
   * Select **File** > **New** > **Transformation**.
   * Select **New file** on the toolbar, then select **Transformation**.
   * Press `Ctrl+N`.
2. Select the **Design** tab.
3. Expand folders or search in **Steps**.
4. Drag a step onto the canvas.
5. Double-click the step to open its properties.
6. Add more steps as needed:
   * Drag a step, then press `Shift` and draw a hop to connect steps.
   * Double-click a step to add it with a hop from the previous step.

Save the transformation before you run it.

#### Open a transformation

How you open a transformation depends on where it lives.

You can open a local file, a repository object, or a file on a Virtual File System (VFS).

{% hint style="info" %}
If you get a missing plugin error, see [Troubleshooting transformation steps and job entries](https://docs.pentaho.com/pdia-data-integration/data-integration-issues/troubleshooting-transformation-steps-and-job-entries).
{% endhint %}

**Open a local transformation**

1. In the PDI client, do one of the following:
   * Select **File** > **Open**.
   * Select **Open file** on the toolbar.
   * Select **OPEN Files** on the Welcome screen.
   * Press `Ctrl+O`.
2. Select the `.ktr` file, then select **Open**.

**Open a transformation from the Pentaho Repository**

1. Verify you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/redirects/use-a-pentaho-repository-in-pdi).
2. Open the repository browser:
   * Select **File** > **Open**.
   * Select **Open file** on the toolbar.
   * Select **OPEN Files** on the Welcome screen.
   * Press `Ctrl+O`.
3. Use **Recents**, search, or browse folders to find your transformation.
4. Select the transformation, then select **Open**.

**Open a transformation on a Virtual File System**

Select **File** > **Open**.

For details, see [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/virtual-file-system-browser).

#### Rename a folder or file (local only)

You can rename folders and files from the **Open** window.

You can rename only when you are not connected to the Pentaho Repository.

1. In the **Open** window, select a folder or file.
2. Right-click the folder or file.
3. Select **Rename**.

#### Save a transformation

How you save a transformation depends on where it lives.

**Save a local transformation**

1. In the PDI client, do one of the following:
   * Select **File** > **Save** or **File** > **Save as**.
   * Select **Save current file** on the toolbar.
   * Press `Ctrl+S`.
2. Enter a name and choose a location.
3. Select **Save**.

**Save a transformation to the Pentaho Repository**

1. Verify you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/redirects/use-a-pentaho-repository-in-pdi).
2. In the PDI client, do one of the following:
   * Select **File** > **Save** or **File** > **Save as**.
   * Select **Save current file** on the toolbar.
   * Press `Ctrl+S`.
3. Browse to the repository folder.
4. Enter a name, then select **Save**.

**Save a transformation on a Virtual File System**

Select **File** > **Open** to save a transformation on a Virtual File System (VFS).

For details, see [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/virtual-file-system-browser).

#### Run a transformation

Run a transformation to test how it performs.

The **Run Options** window lets you set run configurations, logging, options, and temporary parameter values.

Open **Run Options** in one of these ways:

* Select **Run** on the toolbar.
* Select **Action** > **Run**.
* Press `F9`.

The **Run Options** window appears.

In **Run Options**, you choose a run configuration.

To set up run configurations, see [Run configurations (transformations)](#run-configurations-transformations).

After you run a transformation, use the [Execution Results](#analyze-transformation-results) section to review output.

**Run configurations (transformations)**

Some ETL activities are lightweight.

Others need dedicated servers or cluster execution.

You can create or edit run configurations in **View** > **Run configurations**.

**Pentaho local** is the default run configuration.

You cannot edit it.

**Create or edit a run configuration**

Right-click **Run configurations**, then select **New**.

Or, right-click a configuration and select **Edit**.

The dialog contains:

| Field           | Description                               |
| --------------- | ----------------------------------------- |
| **Name**        | Name of the run configuration.            |
| **Description** | Optional details about the configuration. |

**Select an engine**

You can select the **Pentaho engine** to run transformations in the default environment.

You can also use **Spark Submit** to run big data transformations on a Hadoop cluster.

See [Spark Submit](https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/spark-submit).

The Pentaho engine does not execute sub-transformations or sub-jobs when you select **Pentaho server** or **Slave server**.

If you need sub-transformations to run on the same host as the parent job, use **Local**.

**Run options**

Errors, warnings, and other information are stored in logs.

You set log verbosity and other behavior in the **Options** section.

For background, see [Logging and performance monitoring](#logging-and-performance-monitoring).

| Option                         | Description                                                                                                                                                                                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Clear log before running**   | Clears logs before each run.                                                                                                                                                                                                                                      |
| **Log level**                  | Controls how much information is logged.                                                                                                                                                                                                                          |
| **Enable safe mode**           | Checks every row to ensure layout consistency.                                                                                                                                                                                                                    |
| **Gather performance metrics** | Captures performance metrics during the run. See [Use performance graphs](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/logging-and-performance-monitoring/monitor-performance/use-performance-graphs). |

**Parameters and variables (run-time overrides)**

You can temporarily override parameters and variables for each run.

These overrides apply only to the current run.

* Use [parameters](#parameters) to set run-time parameter values.
* Use [variables](#variables) to set run-time variable values.
* Use [arguments](#arguments) for command-line style arguments.

#### Analyze transformation results

After you run a transformation, the **Execution Results** panel appears.

It helps you inspect step behavior, errors, and performance.

**Step metrics**

The **Step Metrics** tab shows per-step statistics.

It includes records read, written, errors, and row throughput.

Steps that failed are highlighted in red.

**Logging**

The **Logging** tab shows log details for the most recent run.

Error lines are highlighted in red.

**Execution history**

The **Execution History** tab shows metrics and logs from previous runs.

It requires database logging configured in transformation properties.

See [Set up transformation logging](#set-up-transformation-logging).

**Performance graph**

The **Performance Graph** tab shows step performance over time.

It requires database logging enabled.

**Metrics**

The **Metrics** tab shows a Gantt chart for run timings.

**Preview data**

Use **Preview Data** to inspect step output rows.

Select a step to view its data.

#### Stop your transformation

You can stop transformations in two ways.

* Use **Stop** to stop immediately.
* Use **Stop input processing** to stop input safely after in-flight records complete.

<details>

<summary>Transformation properties reference</summary>

Transformation properties describe the transformation and configure its behavior.

To open properties, press `Ctrl+T` or right-click the canvas and select **Properties**.

The settings are grouped into these tabs:

* Transformation
* Parameters
* Logging
* Dates
* Dependencies
* Miscellaneous
* Monitoring

After you adjust settings, select **SQL** to generate SQL for logging tables.

For SQL execution details, see [Use the SQL Editor](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/logging-and-performance-monitoring/use-the-sql-editor).

#### Transformation tab

Use the **Transformation** tab to specify general properties.

| Property                | Description                                     |
| ----------------------- | ----------------------------------------------- |
| Transformation name     | Required to save settings to a repository.      |
| Transformation filename | `.ktr` file name.                               |
| Description             | Short description shown in Repository Explorer. |
| Extended description    | Long description.                               |
| Status                  | Draft or production.                            |
| Version                 | Version description.                            |
| Directory               | Repository directory.                           |
| Created by              | Original creator.                               |
| Created at              | Create time.                                    |
| Last modified by        | Last editor.                                    |
| Last modified at        | Last update time.                               |

#### Parameters tab

Use the **Parameters** tab to add parameters.

| Property      | Description                                               |
| ------------- | --------------------------------------------------------- |
| Parameter     | Local variable shared across steps in the transformation. |
| Default Value | Used if a parameter value is not set elsewhere.           |
| Description   | Description of the parameter.                             |

#### Logging tab

Use the **Logging** tab to configure logging.

For a guided setup, see [Set up transformation logging](#set-up-transformation-logging).

#### Dates tab

Use the **Dates** tab to configure date ranges and limits.

#### Dependencies tab

Use the **Dependencies** tab to list transformation dependencies.

#### Miscellaneous tab

Use the **Miscellaneous** tab to configure buffer sizes and admin settings.

This tab includes the **Make the transformation database transactional** option.

For rollback patterns, see [Transactional databases and job rollback](#transactional-databases-and-job-rollback).

#### Monitoring tab

Use the **Monitoring** tab to enable step performance monitoring.

</details>

<details>

<summary>Transformation canvas context menu (Transformation menu)</summary>

Use the **Transformation** menu to access settings, options, and properties.

Right-click any step in the canvas.

Each item is described in this table.

| Menu Item                            | Description                                                                                                                                                                                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **New Hop**                          | Creates a new hop.                                                                                                                                                                                                                     |
| **Edit**                             | Shows the step configuration window.                                                                                                                                                                                                   |
| **Description**                      | Adds a description to the step.                                                                                                                                                                                                        |
| **Open Referenced Object**           | Maps a sub-transformation. See [Mapping](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/mapping).                                                                                          |
| **Data Movement**                    | Round robin, load balance, or copy rows across hops.                                                                                                                                                                                   |
| **Change Number of Copies to Start** | Starts step copies in parallel.                                                                                                                                                                                                        |
| **Copy**                             | Copies selected items to the clipboard.                                                                                                                                                                                                |
| **Duplicate**                        | Duplicates the selection on the canvas.                                                                                                                                                                                                |
| **Delete**                           | Deletes selected items.                                                                                                                                                                                                                |
| **Hide**                             | Hides the step. You must edit the XML to show it again.                                                                                                                                                                                |
| **Detach**                           | Detaches the step or entry.                                                                                                                                                                                                            |
| **Input Fields**                     | Shows incoming field metadata.                                                                                                                                                                                                         |
| **Output Fields**                    | Shows outgoing field metadata.                                                                                                                                                                                                         |
| **Sniff Test During Execution**      | Shows row data while executing. See [Sniff Test tool](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/logging-and-performance-monitoring/monitor-performance/sniff-test-tool). |
| **Check Selected Step(s)**           | Checks steps for configuration problems.                                                                                                                                                                                               |
| **Error Handling**                   | Configures step error handling.                                                                                                                                                                                                        |
| **Preview**                          | Launches the debug dialog.                                                                                                                                                                                                             |
| **Align/Distribute**                 | Aligns or distributes steps on the canvas.                                                                                                                                                                                             |
| **Data Services**                    | Creates or manages data services. See [Pentaho Data Services](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/loading-data-from-pdi-archive/pentaho-data-services).                                               |
| **Mapping**                          | Creates a Select/Rename Values step for field mappings.                                                                                                                                                                                |
| **Partitions**                       | Configures partitioning. See [Partitioning data](#partitioning-data).                                                                                                                                                                  |
| **Clusters**                         | Configures Carte clusters. See [Use Carte Clusters](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/loading-data-from-pdi-archive/use-carte-clusters).                                                            |

</details>

### Work with jobs

In the [PDI client (Spoon)](https://docs.pentaho.com/pdia-data-integration/basic-concepts-of-pdi), you can develop jobs to orchestrate ETL activities.

Job entries define the work a job performs.

Jobs are stored in `.kjb` files.

#### Create a job

Follow these steps:

1. Do one of the following:
   * Select **File** > **New** > **Job**.
   * Select **New file** on the toolbar, then select **Job**.
   * Press `Ctrl+Alt+N`.
2. Select the **Design** tab.
3. Expand folders or search in **Entries**.
4. Drag an entry onto the canvas.
5. Double-click the entry to open its properties.
6. Add more entries as needed:
   * Drag an entry, then press `Shift` and draw a hop.
   * Double-click an entry to add it with a hop from the previous entry.

Save the job when you are done.

#### Open a job

How you open a job depends on where it lives.

You can open a local file, a repository object, or a file on a Virtual File System (VFS).

{% hint style="info" %}
If you get a missing plugin error, see [Troubleshooting transformation steps and job entries](https://docs.pentaho.com/pdia-data-integration/data-integration-issues/troubleshooting-transformation-steps-and-job-entries).
{% endhint %}

**Open a local job**

1. In the PDI client, do one of the following:
   * Select **File** > **Open**.
   * Select **Open file** on the toolbar.
   * Select **OPEN Files** on the Welcome screen.
   * Press `Ctrl+O`.
2. Select the `.kjb` file, then select **Open**.

**Open a job from the Pentaho Repository**

1. Verify you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/redirects/use-a-pentaho-repository-in-pdi).
2. Open the repository browser:
   * Select **File** > **Open**.
   * Select **Open file** on the toolbar.
   * Press `Ctrl+O`.
3. Use **Recents**, search, or browse folders to find your job.
4. Select the job, then select **Open**.

**Open a job on a Virtual File System**

Select **File** > **Open**.

For details, see [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/virtual-file-system-browser).

#### Rename a folder or file (local only)

Use [Rename a folder or file (local only)](#rename-a-folder-or-file-local-only).

#### Save a job

How you save a job depends on where it lives.

**Save a local job**

1. In the PDI client, do one of the following:
   * Select **File** > **Save** or **File** > **Save as**.
   * Select **Save current file** on the toolbar.
   * Press `Ctrl+S`.
2. Enter a name and choose a location.
3. Select **Save**.

**Save a job to the Pentaho Repository**

1. Verify you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/redirects/use-a-pentaho-repository-in-pdi).
2. In the PDI client, do one of the following:
   * Select **File** > **Save** or **File** > **Save as**.
   * Select **Save current file** on the toolbar.
   * Press `Ctrl+S`.
3. Browse to the repository folder.
4. Enter a name, then select **Save**.

**Save a job on a Virtual File System**

Select **File** > **Open** to save a job on a Virtual File System (VFS).

For details, see [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/virtual-file-system-browser).

#### Run a job

Run a job to test how it performs.

The **Run Options** window lets you set run configurations, logging, options, and temporary values.

Open **Run Options** in one of these ways:

* Select **Run** on the toolbar.
* Select **Action** > **Run**.
* Press `F9`.

In **Run Options**, you choose a run configuration.

To set up run configurations, see [Run configurations (jobs)](#run-configurations-jobs).

**Run configurations (jobs)**

You can create or edit configurations in **View** > **Run configurations**.

**Pentaho local** is the default run configuration.

You cannot edit it.

**Pentaho engine**

The Pentaho engine does not execute sub-transformations or sub-jobs when you select **Pentaho server** or **Slave server**.

If you need sub-transformations to run on the same host as the parent job, use **Local**.

**Run options**

| Option                         | Description                                    |
| ------------------------------ | ---------------------------------------------- |
| **Clear log before running**   | Clears logs before each run.                   |
| **Log level**                  | Controls how much information is logged.       |
| **Enable safe mode**           | Checks every row to ensure layout consistency. |
| **Start job at**               | Starts the run at an alternative entry.        |
| **Gather performance metrics** | Captures performance metrics during the run.   |

**Parameters and variables (run-time overrides)**

You can temporarily override parameters and variables for each run.

These overrides apply only to the current run.

* Use [parameters](#parameters) to set run-time parameter values.
* Use [variables](#variables) to set run-time variable values.
* Use [arguments](#arguments) for command-line style arguments.

#### Stop your job

You can stop jobs in two ways.

* Use **Stop** to stop immediately.
* Use **Stop input processing** to stop input safely after in-flight records complete.

<details>

<summary>Job properties reference</summary>

Job properties control job behavior and logging.

To open properties, press `Ctrl+T` or right-click the canvas and select **Properties**.

The properties are grouped into these tabs:

* Job
* Parameters
* Settings
* Log
* Transactions

</details>

<details>

<summary>Job canvas context menu (Job menu)</summary>

Right-click any entry in the job canvas to view the **Job** menu.

| Menu Item                        | Description                                                                                                        |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **New Hop**                      | Creates a new hop.                                                                                                 |
| **Edit**                         | Shows the entry configuration window.                                                                              |
| **Description**                  | Adds a description to the entry.                                                                                   |
| **Open Referenced Object**       | Opens referenced transformations.                                                                                  |
| **Copy**                         | Copies selected items to the clipboard.                                                                            |
| **Duplicate**                    | Duplicates the selection on the canvas.                                                                            |
| **Delete**                       | Deletes selected items.                                                                                            |
| **Hide**                         | Hides the entry. You must edit the XML to show it again.                                                           |
| **Detach**                       | Detaches the entry from the job.                                                                                   |
| **Align/Distribute**             | Aligns or distributes entries on the canvas.                                                                       |
| **Restartable Checkpoint**       | Adds a checkpoint to restart failed jobs. See [Use checkpoints to restart jobs](#use-checkpoints-to-restart-jobs). |
| **Run Next Entries in Parallel** | Runs next entries in parallel.                                                                                     |

</details>

### PDI run modifiers

This section describes the types of run modifiers, their uses, and configuration.

You can use arguments, parameters, or variables to modify how you run transformations and jobs.

#### Arguments

A PDI argument is a named, user-supplied, single-value input.

Arguments are passed as command-line values after the Pan or Kitchen options.

Each transformation or job supports up to 10 arguments.

Example:

```sh
sh pan.sh -file:/example_transformations/example.ktr argOne argTwo argThree
```

In Spoon, you can test arguments in the **Run Options** window.

Use the **Arguments** button to enter values.

#### Parameters

Parameters are local variables that apply only to the transformation where you define them.

You can assign a default value.

If a parameter name collides with a variable, the parameter takes precedence.

Define parameters in transformation settings:

* Right-click the transformation canvas and select **Transformation settings**.
* Or press `Ctrl+T`.
* Select the **Parameters** tab.

**VFS properties**

You can specify VFS properties as parameters.

**Specifying VFS properties as parameters**

VFS properties can be specified as parameters.

The format of the reference to a VFS property is **vfs.scheme.property.host**.

The following list describes the subparts of the format:

* The **vfs** subpart is required to identify this as a virtual file system configuration property.
* The **scheme** subpart represents the VFS driver's scheme (or VFS type), such as HTTP, SFTP, or ZIP.
* The **property** subpart is the name of a VFS driver's ConfigBuilder's setter (the specific VFS element that you want to set).
* The **host** optionally defines a specific IP address or hostname that this setting applies to.

You must consult each scheme's API reference to determine which properties you can create variables for.

Apache provides VFS scheme documentation at <https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/>.

The **org.apache.commons.vfs.provider** package lists each of the configurable VFS providers (FTP, HTTP, SFTP, and others).

Each provider has a **FileSystemConfigBuilder** class that in turn has **set\*(FileSystemOptions, Object)** methods.

If a method's second parameter is a **String** or a number (Integer, Long, and others), then you can create a PDI variable to set the value for VFS dialog boxes.

The table below explains VFS properties for the SFTP scheme.

Each property must be declared as a PDI variable and preceded by the `vfs.sftp` prefix as defined above.

| SFTP VFS Property         | Purpose                                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **compression**           | Specifies whether ZLIB compression is used for the destination files. Possible values are `zlib` and `none`.                                                             |
| **identity**              | The private key file (fully qualified local or remote path and filename) to use for host authentication.                                                                 |
| **authkeypassphrase**     | The passphrase for the private key specified by the **identity** property.                                                                                               |
| **StrictHostKeyChecking** | If this is set to `no`, the certificate of any remote host will be accepted. If set to `yes`, the remote host must exist in the known hosts file (`~/.ssh/known_hosts`). |

**Note:** All of these properties are optional.

The following examples show how to specify parameters as VFS properties:

![Transformation Properties Example](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-69f9f1449fd41326ed32bc0b584dd1b28eeff014%2FTransformationProperties_vfs.png?alt=media)

**Configure SFTP VFS**

To configure the connection settings for SFTP dialog boxes in PDI, you must create either variables or parameters for each relevant value.

Possible values are determined by the VFS driver you are using.

You can use parameters to substitute VFS connection details, then use them in the VFS dialog box.

For example, assuming the parameters have been set:

`sftp://${username}@${host}/${path}`

This technique enables you to hide sensitive connection details, such as usernames and passwords.

You can see examples of these techniques in the VFS Configuration Sample transformation in the `/data-integration/samples/transformations/` directory.

#### Variables

A variable is user-supplied information used dynamically in different scopes.

Variables can be local to a step or available to the whole JVM.

You can define variables in these ways:

* Set Variable step or Set Session Variables step.
* `kettle.properties`.
* **Edit** > **Set Environment Variables**.

You can reference variables in fields using:

* `${VARIABLE}`
* `%%VARIABLE%%`

If a name collides with a parameter or argument, variables defer.

**Environment variables**

Environment variables are traditional variables in PDI.

You define them in **Edit** > **Set Environment Variables**.

Or you pass JVM system properties using the `-D` flag.

Environment variables are not safe for dynamic concurrent runs.

They are visible to all software running in the same JVM.

**Kettle variables**

Kettle variables are scoped to Kettle and can be limited to a job or transformation.

You can set Kettle variables in these ways:

* [Set Kettle variables in the PDI client](#set-kettle-variables-in-the-pdi-client)
* [Set Kettle variables manually](#set-kettle-variables-manually)
* [Set Kettle or Java environment variables in the Pentaho MapReduce job entry](#set-kettle-or-java-environment-variables-in-the-pentaho-mapreduce-job-entry)
* [Set the LAZY\_REPOSITORY variable in the PDI client](#set-the-lazy_repository-variable-in-the-pdi-client)

**Set Kettle variables in the PDI client**

1. Select **Edit** > **Edit the kettle.properties file**.
2. Update existing values.
3. To add a variable:
   1. Right-click a line number and select **Insert before this row** or **Insert after this row**.
   2. Enter the variable name and value.
   3. To reorder, right-click the line and select **Move Up** or **Move Down**.
4. Select **OK**.

**Set Kettle variables manually**

1. Open `kettle.properties` in a text editor.
2. Edit values.
3. Save the file.

**Set Kettle or Java environment variables in the Pentaho MapReduce job entry**

MapReduce jobs run distributed across nodes.

Set node-specific variables in the MapReduce job entry.

1. Double-click the **Pentaho MapReduce** job entry, then select **User Defined**.
2. In **Name**, set a variable name:
   * Kettle variable: `KETTLE_SAMPLE_VAR`
   * Java system property: prefix with `java.system.` (example `java.system.SAMPLE_PATH_VAR`)
3. In **Value**, enter the variable value.
4. Select **OK**.

**Set the LAZY\_REPOSITORY variable in the PDI client**

This variable restores repository directory-loading behavior from before Pentaho 6.1.

1. Select **Edit** > **Edit the kettle.properties file**.
2. Set `KETTLE_LAZY_REPOSITORY=true`.
3. Select **OK**, then restart the PDI client.

#### Internal variables

These variables are always defined:

| Variable Name                     | Sample Value          |
| --------------------------------- | --------------------- |
| **Internal.Kettle.Build.Date**    | `2010/05/22 18:01:39` |
| **Internal.Kettle.Build.Version** | `2045`                |
| **Internal.Kettle.Version**       | `4.3`                 |

These variables are defined in a transformation:

| Variable Name                                    | Sample Value                                        |
| ------------------------------------------------ | --------------------------------------------------- |
| **Internal.Transformation.Filename.Directory**   | `D:\\Kettle\\samples`                               |
| **Internal.Transformation.Filename.Name**        | `Denormaliser - 2 series of key-value pairs.ktr`    |
| **Internal.Transformation.Name**                 | `Denormaliser - 2 series of key-value pairs sample` |
| **Internal.Transformation.Repository.Directory** | `/`                                                 |

These variables are defined in a job:

| Variable Name                         | Sample Value             |
| ------------------------------------- | ------------------------ |
| **Internal.Job.Filename.Directory**   | `file:///home/matt/jobs` |
| **Internal.Job.Filename.Name**        | `Nested jobs.kjb`        |
| **Internal.Job.Name**                 | `Nested job test case`   |
| **Internal.Job.Repository.Directory** | `/`                      |

These variables are defined in transformations and jobs within a project:

| Variable Name                            | Sample Value                                       |
| ---------------------------------------- | -------------------------------------------------- |
| **Internal.Project.Data.Directory**      | `pvfs://Repository/home/admin/projects/myproject/` |
| **Internal.Project.Execution.Directory** | `/home/admin/projects/myproject`                   |
| **Internal.Project.Name**                | `My project`                                       |
| **Internal.Project.Description**         | `Description of my project`                        |

{% hint style="info" %}
Project directory variables are used in different situations.

* **Internal.Project.Data.Directory** is used by steps that are not repository-aware, like [Text File Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp).
* **Internal.Project.Execution.Directory** is used by repository-aware steps, like [Transformation Executor](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/transformation-executor).
  {% endhint %}

These variables are defined in a clustered transformation on a slave server:

| Variable Name                            | Sample Value          |
| ---------------------------------------- | --------------------- |
| **Internal.Slave.Transformation.Number** | `0..<cluster size-1>` |
| **Internal.Cluster.Size**                | `<cluster size>`      |

### Partitioning data

Partitioning distributes rows into subsets according to a rule.

Use partitioning to scale up (more CPU cores) and scale out (multiple servers).

#### Get started

By default, each step in a transformation runs in parallel in a separate thread.

#### Partitioning during data processing

You can scale up using **Change Number of Copies to Start**.

This creates multiple copies of a step at runtime.

Without partition rules, parallel aggregation can produce incorrect results.

#### Understand repartitioning logic

When a step needs to repartition data, it creates buffers from each source copy to each target copy.

Partitioning applies a rule-based distribution so like rows go to the same copy.

#### Partitioning data over tables

The Table Output step supports partitioning rows to different tables.

It can accept the table name from a **Partitioning field**.

You can also partition per month or per day.

#### Use partitioning

Partitioning methods can be based on any criteria.

You can also use a partitioning plugin.

1. Set up a partition schema.
2. Apply the schema to a step.
3. Select a partitioning method for row distribution.

#### Use data swimlanes

When a partitioned step passes data to another partitioned step with the same schema, data stays in swimlanes.

No repartitioning is needed.

#### Rules for partitioning

These rules drive distribution and buffer allocation:

* A partitioned step runs one copy per partition.
* Repartitioning creates buffers from each source copy to each target copy.
* Non-partitioned to partitioned causes repartitioning.
* Same schema between partitioned steps avoids repartitioning.
* Different schemas between partitioned steps causes repartitioning.

#### Partitioning clustered transformations

Partitioning can scale out on a cluster of slave servers.

Keep repartitioning to a minimum to avoid network overhead.

Try to keep data in swimlanes for as long as possible.

#### Learn more

* [Set up a Carte cluster](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/carte-clusters-archive/set-up-a-carte-cluster)

### Logging and performance monitoring

You can use logging and performance monitoring to troubleshoot, tune, and plan capacity.

You can also run an impact analysis from **Action** > **Impact**.

#### Set up transformation logging

Follow these steps to create a log table for a transformation:

1. Ask your system administrator to create a database or table space called `PdiLog`.
2. Open transformation properties (`Ctrl+T`).
3. Select the **Logging** tab.
4. Configure connection, schema, and table name.
5. Select fields to log.
6. Select **SQL**, then execute the generated SQL.

{% hint style="info" %}
For effective deletion of expired logs, keep **LOGDATE** and **TRANSNAME** enabled.
{% endhint %}

{% hint style="warning" %}
Monitoring **LOG\_FIELD** can negatively affect Pentaho Server performance.
{% endhint %}

#### Set up job logging

Follow these steps to create a log table for a job:

1. Ask your system administrator to create a database or table space called `PdiLog`.
2. Open job properties (`Ctrl+T`).
3. Select the **Log** tab.
4. Configure connection, schema, and table name.
5. Select fields to log.
6. Select **SQL**, then execute the generated SQL.

{% hint style="info" %}
For effective deletion of expired logs, keep **LOGDATE** and **JOBNAME** enabled.
{% endhint %}

#### Logging levels

| Log Level     | Description                                     |
| ------------- | ----------------------------------------------- |
| **Nothing**   | No logging.                                     |
| **Error**     | Only errors.                                    |
| **Minimal**   | Minimal logging.                                |
| **Basic**     | Default.                                        |
| **Detailed**  | Detailed logging output.                        |
| **Debug**     | Very detailed output for debugging.             |
| **Row Level** | Row-level logging. Generates a lot of log data. |

#### Monitor performance

Use these tools:

* [Sniff Test tool](#sniff-test-tool)
* [Monitoring tab](#monitoring-tab)
* [Use performance graphs](#use-performance-graphs)

**Sniff Test tool**

The Sniff Test displays row data as it travels from one step to another.

It is designed as a supplement to logs.

{% hint style="warning" %}
Sniff Test slows transformation run speed.
{% endhint %}

1. Right-click a step while the transformation runs.
2. Select **Sniff Test During Execution**.
3. Select an option:
   * **Sniff test input rows**
   * **Sniff test output rows**
   * **Sniff test error handling**

**Monitoring tab**

Enable step performance monitoring in transformation properties:

1. Open transformation properties (`Ctrl+T`).
2. Select **Enable step performance monitoring?**.

Step performance monitoring can increase memory consumption in long-running transformations.

**Use performance graphs**

If you configured performance monitoring with database logging, you can view performance graphs.

<details>

<summary>PDI performance tuning tips</summary>

The following tips can help diagnose performance issues.

| Step          | Tip                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JS            | Turn off compatibility mode                                                   | <p>Rewriting JavaScript to use a format that is not compatible with previous versions is, in most instances, easy to do and makes scripts easier to work with and to read. By default, old JavaScript programs run in compatibility mode. That means that the step will process like it did in a previous version. You may see a small performance drop because of the overload associated with forcing compatibility. If you want to make use of the new architecture, disable compatibility mode and change the code as shown below:</p><ul><li><code>intField.getInteger() > intField</code></li><li><code>numberField.getNumber() > numberField</code></li><li><code>dateField.getDate() > dateField</code></li><li><code>bigNumberField.getBigNumber() > bigNumberField</code></li><li>and so on...</li></ul><p>Instead of Java methods, use the built-in library. Notice that the resulting program code is more intuitive. For example:</p><ul><li>checking for null is now: <code>field.isNull() > field==null</code></li><li>Converting string to date: <code>field.Clone().str2dat() > str2date(field)</code></li><li>and so on...</li></ul><p>If you convert your code as shown above, you may get significant performance benefits.</p><p><strong>Note:</strong> It is no longer possible to modify data in-place using the value methods. This was a design decision to ensure that no data with the wrong type would end up in the output rows of the step. Instead of modifying fields in-place, create new fields using the table at the bottom of the Modified JavaScript transformation.</p> |
| JS            | Combine steps                                                                 | One large JavaScript step runs faster than three consecutive smaller steps. Combining processes in one larger step helps to reduce overhead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| JS            | Avoid the JavaScript step or write a custom plug in                           | Remember that while JavaScript is the fastest scripting language for Java, it is still a scripting language. If you do the same amount of work in a native step or plugin, you avoid the overhead of the JS scripting engine. This has been known to result in significant performance gains. It is also the primary reason why the Calculator step was created — to avoid the use of JavaScript for simple calculations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| JS            | Create a copy of a field                                                      | No JavaScript is required for this, a Select Values step does the trick. You can specify the same field twice. Once without a rename, once (or more) with a rename. Another trick is to use B=NVL(A,A) in a Calculator step where B is forced to be a copy of A.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| JS            | Data conversion                                                               | Consider performing conversions between data types (dates, numeric data, and so on) in a Select Values step. You can do this in the **Metadata** tab of the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| JS            | Variable creation                                                             | If you have variables that can be declared once at the beginning of the transformation, make sure you put them in a separate script and mark that script as a startup script (right click on the script name in the tab). JavaScript object creation is time consuming so if you can avoid creating a new object for every row you are transforming, this will translate to a performance boost for the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| N/A           | Launch several copies of a step                                               | <p>There are two important reasons why launching multiple copies of a step may result in better performance:1. The step uses a lot of CPU resources and you have multiple processor cores in your computer. Example: a JavaScript step.<br>2. Network latencies and launching multiple copies of a step can reduce average latency. If you have a low network latency of say 5ms and you need to do a round trip to the database, the maximum performance you get is 200 (x5) rows per second, even if the database is running smoothly. You can try to reduce the round trips with caching, but if not, you can try to run multiple copies. Example: a database lookup or table output.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| N/A           | Manage thread priorities                                                      | This feature that is found in the Transformation Settings dialog box under the (**Misc** tab) improves performance by reducing the locking overhead in certain situations. This feature is enabled by default for new transformations that are created in recent versions, but for older transformations this can be different.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Select Values | If possible, don't remove fields in Select Values                             | Don't remove fields in Select Value unless you must. It's a CPU-intensive task as the engine needs to reconstruct the complete row. It is almost always faster to add fields to a row rather than delete fields from a row.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Get Variables | Watch your use of Get Variables                                               | May cause bottlenecks if you use it in a high-volume stream (accepting input). To solve the problem, take the Get Variables step out of the transformation (right click, detach) then insert it in with a Join Rows step. Make sure to specify the main step from which to read in the Join Rows step. Set it to the step that originally provided the Get Variables step with data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| N/A           | Use new text file input                                                       | The CSV File Input or Fixed File Input steps provide optimal performance. If you have a fixed width (field/row) input file, you can even read data in parallel. (multiple copies) These new steps have been rewritten using Non-blocking I/O (NIO) features. Typically, the larger the NIO buffer you specify in the step, the better your read performance will be.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| N/A           | When appropriate, use lazy conversion                                         | In instances in which you are reading data from a text file and you write the data back to a text file, use Lazy conversion to speed up the process. The principle behind lazy conversion that it delays data conversion in hopes that it isn't necessary (reading from a file and writing it back comes to mind). Beyond helping with data conversion, lazy conversion also helps to keep the data in "binary" storage form. This, in turn, helps the internal Kettle engine to perform faster data serialization (sort, clustering, and so on). The **Lazy Conversion** option is available in the CSV File Input and Fixed File Input text file reading steps.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Join Rows     | Use Join Rows                                                                 | You need to specify the main step from which to read. This prevents the step from performing any unnecessary spooling to disk. If you are joining with a set of data that can fit into memory, make sure that the cache size (in rows of data) is large enough. This prevents (slow) spooling to disk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| N/A           | Review the big picture: database, commit size, row set size and other factors | Consider how the whole environment influences performance. There can be limiting factors in the transformation itself and limiting factors that result from other applications and PDI. Performance depends on your database, your tables, indexes, the JDBC driver, your hardware, speed of the LAN connection to the database, the row size of data and your transformation itself. Test performance using different commit sizes and changing the number of rows in row sets in your transformation settings. Change buffer sizes in your JDBC drivers or database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| N/A           | Step Performance Monitoring                                                   | Step Performance Monitoring is an important tool that allows you identify the slowest step in your transformation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

</details>

#### Logging best practices

You can improve logging with rotation and other best practices.

For more information, see the **Administer Pentaho Data Integration and Analytics** document.

#### Use checkpoints to restart jobs

Checkpoints let you restart jobs that fail without rerunning from the beginning.

**Add a checkpoint**

1. Open a job.
2. Right-click an entry, then select **Restartable Checkpoint**.

**Delete a checkpoint**

1. Open a job.
2. Right-click an entry, then select **Clear Checkpoint Marker**.

**Set up a checkpoint log**

1. Open a job.
2. Right-click the job canvas, then select **Properties**.
3. Select the **Log** tab, then select **Checkpoints log table**.
4. Configure the log connection and table name.
5. Select **OK**.

#### Use the SQL Editor

Use the SQL Editor to preview and execute DDL generated by the PDI client.

Keep these points in mind:

* Separate statements with semicolons.
* Spoon removes line breaks and semicolons before execution.
* PDI clears database cache for the connection you execute on.

#### Use the Database Explorer

Use Database Explorer to explore configured database connections.

You open it from the Database Connections dialog box.

#### Transactional databases and job rollback

By default, changes are committed as a job or transformation executes.

If you need rollback behavior, make the database transactional.

**Make a transformation database transactional**

1. Open a transformation.
2. Open transformation properties.
3. Select the **Miscellaneous** tab.
4. Select **Make the transformation database transactional**.
5. Select **OK**.

**Make a job database transactional**

1. Open a job.
2. Open job properties.
3. Select the **Transactions** tab.
4. Select **Make the job database transactional**.
5. Select **OK**.

### Add notes to transformations and jobs

Notes help document structure, design decisions, business rules, and dependencies.

#### Create a note

1. Right-click the canvas and select **New Note**.
2. Select **Font Style** to change font and color.
3. Select **Note**, then type your note.
4. Select **OK**.

#### Edit a note

1. Double-click the note.
2. Select **Font Style** to change font and color.
3. Select **Note**, then edit your note.
4. Select **OK**.

#### Reposition a note

1. Drag the note to a new position.
2. Optional: right-click the note:
   * Select **Raise Note** to move it above other items.
   * Select **Lower Note** to move it below other items.

#### Delete a note

1. Right-click the note.
2. Select **Delete Note**.

### Manage PDI transformations and job schedules

Schedule transformations and jobs to run at specific times or intervals.

#### Schedule a transformation or job

1. Connect to the Pentaho Repository.
2. Open a job or transformation, then select **Action** > **Schedule**.
3. Set start time:
   * **Now**, or
   * **Date** with date, time, and time zone.
4. Set repeat schedule.
5. Set end time or select **No end**.
6. Optional: enable **Safe mode**.
7. Select **Log Level**.
8. Update argument, parameter, or variable values if needed.
9. Select **OK**.

#### Edit a scheduled run

1. Select the **Scheduler** perspective.
2. Select the schedule, then select **Edit Scheduled Task**.

#### Stop a schedule

1. Select the **Scheduler** perspective.
2. Select the schedule, then select **Stop Scheduled Task**.

#### Enable or disable a schedule

1. Select the **Scheduler** perspective.
2. Select the schedule.
3. Select **Start Scheduler** to enable.
4. Select **Stop Scheduler** to disable.

#### Delete a scheduled run

1. Select the **Scheduler** perspective.
2. Select the schedule, then select **Remove**.

#### Refresh the schedule list

1. Select the **Scheduler** perspective.
2. Select **Refresh**.

### Archived source pages

These pages were merged into this single topic page and moved under [Transforming data with PDI (archive)](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive):

* [Work with transformations](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/work-with-transformations-cp)
* [Work with jobs](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/work-with-jobs)
* [PDI run modifiers](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/pdi-run-modifiers)
* [Partitioning data](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/partitioning-data)
* [Logging and performance monitoring](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/logging-and-performance-monitoring)
* [Add notes to transformations and jobs](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/add-notes-to-transformations-and-jobs)
* [Manage PDI transformations and job schedules](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/manage-pdi-transformations-and-job-schedules)
