# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/transformation-job-entry-cp/options-transformation-job/logging-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/job-job-entry/options-job-job-entry/logging-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/transformation-job-entry-cp/options-transformation-job/logging-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/job-job-entry/options-job-job-entry/logging-tab.md

# Logging tab

By default, if you do not set logging, PDI will take the generated log entries and create a log record inside of the job. For example, suppose a job has three transformations to run and you have not set logging. The transformations will not log information to other files, locations, or special configurations. In this instance, the job executes and logs information into its master job log.

In most instances, it is acceptable for logging information to be available in the job log. For example, if you have load dimensions, you would want logs for your load dimension runs to display in the job logs. If there are errors in the transformations, they will display in the job logs. However, you want all your log information kept in one place, you must set up logging.

![Logging tab, Job (job entry)](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6c9e4d433ddac4aec61c64ae88a5c3d46d1ad8f9%2FPDI_JobJE_LoggingTab.png?alt=media)

This tab includes the following fields:

| Option                      | Description                                                                                                                                                                                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Specify logfile**         | Specifies a separate log file for running this job.                                                                                                                                                                                                            |
| **Name**                    | The directory and base name of the log file, for example, `C:\logs`.                                                                                                                                                                                           |
| **Extension**               | The file name extension, for example, `.log` or `.txt`.                                                                                                                                                                                                        |
| **Log level**               | Specifies the logging level for running the job. See [Logging levels](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/logging-levels) for more details. |
| **Append logfile?**         | Appends the log file instead of creating a new one.                                                                                                                                                                                                            |
| **Create parent folder**    | Creates the parent folder for the log file if it does not already exist.                                                                                                                                                                                       |
| **Include date in logfile** | Adds the system date to the file name with the format YYYYMMDD, for example`_20051231`.                                                                                                                                                                        |
| **Include time in logfile** | Adds the system time to the file name with the format HHMMSS, for example `_235959`.                                                                                                                                                                           |
