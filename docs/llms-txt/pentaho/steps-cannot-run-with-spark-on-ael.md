# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/steps-cannot-run-with-spark-on-ael.md

# Steps cannot run with Spark on AEL

The following **Flow** category transformation steps do not run with Spark on AEL. When you include one of these steps in a transformation or job with Spark on AEL, the KTR or KJB may fail to execute without logging an error.

* Annotate stream
* Append streams
* Java filter
* Job executor
* Prioritize streams
* Shared dimension
* Single threader

To avoid this issue, do not use these orchestration steps with Spark on AEL. If you need to organize the flow of your PDI transformations with Spark, the best practice is to use the Pentaho Server to orchestrate the KTRs using a Pentaho engine job.

See the **Pentaho Data Integration** document for details on PDI transformations, jobs, steps, and entries.
