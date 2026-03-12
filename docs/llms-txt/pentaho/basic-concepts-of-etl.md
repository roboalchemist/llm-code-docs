# Source: https://docs.pentaho.com/pba/pipeline-designer/basic-concepts-of-etl.md

# Basic concepts of ETL

The Pentaho Data Integration (PDI) platform, which includes the PDI client and Pipeline Designer, uses a workflow metaphor as building blocks for transforming your data and other tasks. Workflows are built using steps as you create transformations and jobs. Each step is joined by a hop which passes the flow of data from one item to the next.

## Transformations

A transformation is a network of logical tasks called steps. Transformations are essentially data flows. The transformation is, in essence, a directed graph of a logical set of data transformation configurations. Transformation file names have a `.ktr` extension.

The two main components associated with transformations are steps and hops:

* Steps are the building blocks of a transformation, for example a text file input or a table output. There are many steps available in the Pipeline Designer and they are grouped according to their function; for example, input, output, transform, and so on. Each step in a transformation is designed to perform a specific task, such as reading data from a flat file, filtering rows, or logging to a database. You can add a step by dragging it from the **Design** pane onto the canvas. Steps can be configured to perform the tasks you require. See [Transformation steps in Pipeline Designer](https://docs.pentaho.com/pba/pipeline-designer/working-with-transformations/transformation-steps-in-pipeline-designer) for details about the features and ETL functions of the various transformation steps available in Pipeline Designer.
* Hops are data pathways that connect steps together and allow schema metadata to pass from one step to another.  Hops determine the flow of data through the steps not necessarily the sequence in which they run. When you run a transformation, each step starts up in its own thread and pushes and passes data.

**Note:** All steps in a transformation are started and run in parallel, so the initialization sequence is not predictable. That is why you cannot, for example, set a variable in a first step and attempt to use that variable in a subsequent step.

You can connect steps together with hops. For details, see [Hops](#hops). A step can have many connections. Some steps join other steps together, while some serve as an input or output for another step. The data stream flows through steps to the various steps in a transformation. Hops are represented in Pipeline Designer as arrows. Hops allow data to be passed from step to step and also determine the direction and flow of data through the steps. If a step sends outputs to more than one step, the data can either be copied to each step or distributed among them.

## Jobs

Jobs are workflow-like models for coordinating resources, execution, and dependencies of ETL activities.

Jobs aggregate individual pieces of functionality to implement an entire process. Examples of common tasks performed in a job include getting FTP files, checking conditions such as existence of a necessary target database table, running a transformation that populates that table, and e-mailing an error log if a transformation fails. The final job outcome might be a nightly warehouse update, for example.

Job entries are the individual configured pieces; they are the primary building blocks of a job. In data transformations these individual pieces are called steps. Job entries can provide you with a wide range of functionality ranging from executing transformations to getting files from a Web server. A single job entry can be placed multiple times on the canvas; for example, you can take a single job entry such as a transformation run and place it on the canvas multiple times using different configurations. Job settings are the options that control the behavior of a job and the method of logging a job’s actions. Job file names have a `.kjb` extension. See [Job steps in Pipeline Designer](https://docs.pentaho.com/pba/pipeline-designer/working-with-jobs/job-steps-in-pipeline-designer) for details about the features and ETL functions of the various job entries available in Pipeline Designer.

Job hops control the execution order and the condition on which the next job entry will be executed. A job hop is just a flow of control. Hops link to job entries and, based on the results of the previous job entry, determine what happens next.

**Note:** Hops behave differently when used in a job than when used in a transformation.

Job hop conditions are described in the following table:

| Condition                       | Description                                                                                                                                                                               |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Unconditional**               | The next job entry is executed regardless of the result of the originating job entry                                                                                                      |
| **Follow when result is true**  | The next job entry is executed only when the result of the originating job entry is true; this means a successful execution such as, file found, table found, without error, and so on    |
| **Follow when result is false** | The next job entry is executed only when the result of the originating job entry was false, meaning unsuccessful execution, file not found, table not found, error(s) occurred, and so on |

## Hops

A hop connects one transformation step or job entry with another. The direction of the data flow is indicated by an arrow. To create the hop, click the handle of one step and drag the connection to the handle of another step.

Loops are not allowed in transformations because Pipeline Designer depends heavily on the previous steps to determine the field values that are passed from one step to another. Allowing loops in transformations may result in endless loops and other problems. Loops are allowed in jobs because Pipeline Designer executes job entries sequentially; however, make sure you do not create endless loops.

Mixing rows that have a different layout is not allowed in a transformation; for example, if you have two table input steps that use a varying number of fields. Mixing row layouts causes steps to fail because fields cannot be found where expected or the data type changes unexpectedly. The trap detector displays warnings at design time if a step is receiving mixed layouts.

In transformations, you can specify if data can either be **copied**, **distributed**, or **load balanced** between multiple hops leaving a step. Select the step, right-click and choose **Data Movement**.

A hop can be enabled or disabled (for testing purposes for example). Click the hop to enable or disable it.
