# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/charts-reports-and-dashboards-using-pdi-operations-mart-data.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/charts-reports-and-dashboards-using-pdi-operations-mart-data.md

# Charts, reports, and dashboards using the DI Operations Mart data

Once you have created and populated your Data Integration Operations Mart with log data, you can use the features of the Pentaho User Console to examine this data and create reports, charts, and dashboards. We provide many pre-built reports, charts, and dashboards that you can modify.

To help understand the contents of the log, see [Data Integration Operations Mart](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart).

## Logging tables status

The following tables are contained in the PDI Operations Mart:

### Transformation log tables

The status values and their descriptions are in the following table:

| Status Display | Description                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| start          | Indicates the transformation was started and retains this status until the transformation ends when no logging interval is set. |
| end            | Transformation ended successfully.                                                                                              |
| stop           | Indicates the user stopped the transformation.                                                                                  |
| error          | Indicates an error occurred when attempting to run the transformation.                                                          |
| running        | A transformation is only in this status directly after starting and does not appear without a logging interval.                 |
| paused         | Indicates the user paused the transformation and does not appear without a logging interval.                                    |

### Jobs logs tables

The status values and their descriptions are in the following table:

| Status Display | Description                                                                                                    |
| -------------- | -------------------------------------------------------------------------------------------------------------- |
| start          | Indicates the job was started and retains this status until the job ends, and when no logging interval is set. |
| end            | Job ended successfully.                                                                                        |
| stop           | Indicates the user stopped the job.                                                                            |
| error          | Indicates an error occurred when attempting to run the job.                                                    |
| running        | A job is only in this status directly after starting and does not appear without a logging interval.           |
| paused         | Indicates the user paused the job and it does not appear without a logging interval.                           |

## Logging dimensions and metrics

These tables identify the various dimensions and metrics that can be used to create new ETL log charts and reports:

### Fact table

(fact\_execution)

| Field Name           | Description                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| execution\_date\_tk  | A technical key (TK) linking the fact to the date when the transformation/job was executed.                                     |
| execution\_time\_tk  | A technical key (TK) linking the fact to the time-of-day when the transformation/job was executed.                              |
| batch\_tk            | A technical key (TK) linking the fact to batch information for the transformation/job.                                          |
| execution\_tk        | A technical key (TK) linking the fact to execution information about the transformation/job.                                    |
| executor\_tk         | A technical key (TK) linking the fact to information about the executor (transformation or job).                                |
| parent\_executor\_tk | A technical key (TK) linking the fact to information about the parent transformation/job).                                      |
| root\_executor\_tk   | A technical key (TK) linking the fact to information about the root transformation/job.                                         |
| execution\_timestamp | The date and time when the transformation/job was executed.                                                                     |
| duration             | The length of time (in seconds) between when the transformation was logged (LOGDATE) and the maximum dependency date (DEPDATE). |
| rows\_input          | The number of lines read from disk or the network by the specified step. Can be input from files, databases, etc.               |
| rows\_output         | The number of rows output during the execution of the transformation/job.                                                       |
| rows\_read           | The number of rows read in from the input stream of the specified step.                                                         |
| rows\_written        | The number of rows written during the execution of the transformation/job.                                                      |
| rows\_rejected       | The number of rows rejected during the execution of the transformation/job.                                                     |
| errors               | The number of errors that occurred during the execution of the transformation/job.                                              |

### Batch dimension

(dim\_batch)

| Field Name             | Description                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------- |
| batch\_tk              | A technical key (TK) for linking facts to batch information.                           |
| batch\_id              | The ID number for the batch.                                                           |
| logchannel\_id         | A string representing the identifier for the logging channel used by the batch.        |
| parent\_logchannel\_id | A string representing the identifier for the parent logging channel used by the batch. |

### Date dimension

(dim\_date)

| Field Name          | Description                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| date\_tk            | A technical key (TK) for linking facts to date information.                                             |
| date\_field         | A Date object representing a particular day (year, month, day).                                         |
| ymd                 | A string representing the date value in year-month-day format.                                          |
| ym                  | A string representing the date value in year-month format.                                              |
| year                | An integer representing the year value.                                                                 |
| quarter             | An integer representing the number of the quarter (1-4) to which this date belongs.                     |
| quarter\_code       | A 2-character string representing the quarter (Q1-Q4) to which this date belongs.                       |
| month               | An integer representing the number of the month (1-12) to which this date belongs.                      |
| month\_desc         | A string representing the month (e.g., `January` or `December`) to which this date belongs.             |
| month\_code         | A string representing the shortened month code (e.g., `JAN` or `DEC`) to which this date belongs.       |
| day                 | An integer representing the day of the month (1-31) to which this date belongs.                         |
| day\_of\_year       | An integer representing the day of the year (1-366) to which this date belongs.                         |
| day\_of\_week       | An integer representing the day of the week (1-7) to which this date belongs.                           |
| day\_of\_week\_desc | A string representing the day of the week (e.g., `Sunday` or `Saturday`) to which this date belongs.    |
| day\_of\_week\_code | A string representing the shortened day-of-week code (e.g., `SUN` or `SAT`) to which this date belongs. |
| week                | An integer representing the week of the year (1-53) to which this date belongs.                         |

### Execution dimension

(dim\_execution)

| Field Name        | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| execution\_tk     | A technical key (TK) for linking facts to execution information. |
| execution\_id     | A unique string identifier for the execution.                    |
| server\_name      | The name of the server associated with the execution.            |
| server\_host      | The name of the server associated with the execution.            |
| executing\_user   | The name of the user who initiated the execution.                |
| execution\_status | The status of the execution (start, stop, end, error).           |

### Executor dimension

The following table contains information about an executor that is a job or transformation (dim\_executor):

| Field Name                       | Description                                                                                                          |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| executor\_tk                     | A technical key (TK) for linking facts to executor information.                                                      |
| version                          | An integer corresponding to the version of the executor.                                                             |
| date\_from                       | A date representing the minimum date for which the executor is valid.                                                |
| date\_to                         | A date representing the maximum date for which the executor is valid.                                                |
| executor\_id                     | A string identifier for the executor.                                                                                |
| executor\_source                 | The source location (either file- or repository-relative) for the executor.                                          |
| executor\_environment \*         | File server, repository name, related to the executor\_source.                                                       |
| executor\_type                   | The executor type (e.g., `job` or `transformation`).                                                                 |
| executor\_name                   | The name of the executor (e.g., transformation name).                                                                |
| executor\_desc                   | A string description of the executor (e.g., job description).                                                        |
| executor\_revision               | A string representing the revision of the executor (e.g., `1.3`).                                                    |
| executor\_version\_label         | A string representing a description of the revision (i.e., change comments).                                         |
| exec\_enabled\_table\_logging    | Whether table logging is enabled for this executor. Values are `Y` if enabled; `N` otherwise.                        |
| exec\_enabled\_detailed\_logging | Whether detailed (step or job entry) logging is enabled for this executor. Values are `Y` if enabled; `N` otherwise. |
| exec\_enabled\_perf\_logging     | Whether performance logging is enabled for this executor. Values are `Y` if enabled; `N` otherwise.                  |
| exec\_enabled\_history\_logging  | Whether historical logging is enabled for this executor. Values are `Y` if enabled; `N` otherwise.                   |
| last\_updated\_date              | The date the executor was last updated.                                                                              |
| last\_updated\_user              | The name of the user who last updated the executor.                                                                  |
| \* Reserved for future use.      |                                                                                                                      |

### Log table

The log table (dim\_log\_table) contains data used by the Pentaho Operations Mart.

**CAUTION:** Do not modify the Log table. The following table is for reference only:

| Field Name                     | Description                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| log\_table\_tk                 | A technical key (TK) for linking.                                                                          |
| object\_type                   | The type of PDI object being logged (e.g., `job` or `transformation` or `step`).                           |
| table\_connection\_name        | The name of the database connection corresponding to the location of the transformation/job logging table. |
| table\_name                    | The name of the table containing the transformation/job logging information.                               |
| schema\_name                   | The name of the database schema corresponding to the location of the transformation/job logging table.     |
| step\_entry\_table\_conn\_name | The name of the database connection corresponding to the location of the step/entry logging table.         |
| step\_entry\_table\_name       | The name of the table containing the step/entry logging information.                                       |
| step\_entry\_schema\_name      | The name of the database schema corresponding to the location of the step/entry logging table.             |
| perf\_table\_conn\_name        | The name of the database connection corresponding to the location of the performance logging table.        |
| perf\_table\_name              | The name of the table containing the performance logging information.                                      |
| perf\_schema\_name             | The name of the database schema corresponding to the location of the performance logging table.            |

### Time-of-day dimension

This dimension contains entries for every second of a day from midnight to midnight (dim\_time).

| Field Name | Description                                                                           |
| ---------- | ------------------------------------------------------------------------------------- |
| time\_tk   | A technical key (TK) for linking facts to time-of-day information.                    |
| hms        | A string representing the time of day as hours-minutes-seconds (e.g., `00:01:35`).    |
| hm         | A string representing the time of day as hours-minutes (e.g., `23:59`).               |
| ampm       | A string representing whether the time-of-day is AM or PM. Values are: `am` or `pm`   |
| hour       | The integer number corresponding to the hour of the day (0-23).                       |
| hour12     | The integer number corresponding to the hour of the day with respect to AM/PM (1-12). |
| minute     | The integer number corresponding to the minute of the hour (0-59).                    |
| second     | The integer number corresponding to the second of the minute (0-59).                  |

### Step fact table

This fact table contains facts about individual step executions (fact\_step\_execution).

| Field Name           | Description                                                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| execution\_date\_tk  | A technical key (TK) linking the fact to the date when the step was executed.                                                       |
| execution\_time\_tk  | A technical key (TK) linking the fact to the time-of-day when the step was executed.                                                |
| batch\_tk            | A technical key (TK) linking the fact to batch information for the step.                                                            |
| executor\_tk         | A technical key (TK) linking the fact to information about the executor (transformation).                                           |
| parent\_executor\_tk | A technical key (TK) linking the fact to information about the parent transformation.                                               |
| root\_executor\_tk   | A technical key (TK) linking the fact to information about the root transformation/job.                                             |
| execution\_timestamp | The date and time when the step was executed.                                                                                       |
| step\_tk             | A technical key (TK) linking the fact to information about the step.                                                                |
| step\_copy           | The step copy number. This is zero if there is only one copy of the step, or (`0` to `N-1`) if `N` copies of the step are executed. |
| rows\_input          | The number of lines read from disk or the network by the step. Can be input from files, databases, etc.                             |
| rows\_output         | The number of lines written to disk or the network by the step. Can be output to files, databases, etc.                             |
| rows\_read           | The number of rows read in from the input stream of the step.                                                                       |
| rows\_written        | The number of rows written to the output stream of the step.                                                                        |
| rows\_rejected       | The number of rows rejected during the execution of the step.                                                                       |
| errors               | The number of errors that occurred during the execution of the step.                                                                |

### Step dimension

This dimension contains information about individual steps and job entries (dim\_step) .

| Field Name                  | Description                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------- |
| step\_tk                    | A technical key (TK) for linking facts to step/entry information                          |
| step\_id                    | The string name of the step/entry                                                         |
| original\_step\_name \*     | The name of the step/entry template used to create this step/entry (e.g., `Table Input`). |
| \* Reserved for future use. |                                                                                           |

### Job entry fact table

This fact table contains facts about individual job entry executions (fact\_jobentry\_execution).

| Field Name           | Description                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------ |
| execution\_date\_tk  | A technical key (TK) linking the fact to the date when the job entry was executed.                           |
| execution\_time\_tk  | A technical key (TK) linking the fact to the time-of-day when the job entry was executed.                    |
| batch\_tk            | A technical key (TK) linking the fact to batch information for the job entry.                                |
| executor\_tk         | A technical key (TK) linking the fact to information about the executor (transformation or job).             |
| parent\_executor\_tk | A technical key (TK) linking the fact to information about the parent transformation/job.                    |
| root\_executor\_tk   | A technical key (TK) linking the fact to information about the root transformation/job.                      |
| step\_tk             | A technical key (TK) linking the fact to information about the job entry.                                    |
| execution\_timestamp | The date and time when the job entry was executed.                                                           |
| rows\_input          | The number of lines read from disk or the network by the job entry. Can be input from files, databases, etc. |
| rows\_output         | The number of lines written to disk or the network by the job entry. Can be output to files, databases, etc. |
| rows\_read           | The number of rows read in from the input stream of the job entry.                                           |
| rows\_written        | The number of rows written to the output stream of the job entry.                                            |
| rows\_rejected       | The number of rows rejected during the execution of the job entry.                                           |
| errors               | The number of errors that occurred during the execution of the job entry.                                    |
| result               | Whether the job entry finished successfully or not. Values are `Y` (successful) or `N` (otherwise).          |
| nr\_result\_rows     | The number of result rows after execution.                                                                   |
| nr\_result\_files    | The number of result files after execution.                                                                  |

### Execution performance fact table

This fact table contains facts about the performance of steps in transformation executions (fact\_perf\_execution).

| Field Name           | Description                                                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| execution\_date\_tk  | A technical key (TK) linking the fact to the date when the transformation was executed.                                             |
| execution\_time\_tk  | A technical key (TK) linking the fact to the time-of-day when the transformation was executed.                                      |
| batch\_tk            | A technical key (TK) linking the fact to batch information for the transformation.                                                  |
| executor\_tk         | A technical key (TK) linking the fact to information about the executor (transformation).                                           |
| parent\_executor\_tk | A technical key (TK) linking the fact to information about the parent transformation/job.                                           |
| root\_executor\_tk   | A technical key (TK) linking the fact to information about the root transformation/job.                                             |
| step\_tk             | A technical key (TK) linking the fact to information about the transformation/job.                                                  |
| seq\_nr              | The sequence number. This is an identifier differentiating performance snapshots for a single execution.                            |
| step\_copy           | The step copy number. This is zero if there is only one copy of the step, or (`0` to `N-1`) if `N` copies of the step are executed. |
| execution\_timestamp | The date and time when the transformation was executed.                                                                             |
| rows\_input          | The number of rows read from the input file, database, or network during the interval.                                              |
| rows\_output         | The number of rows written to output file, database, or network during the interval.                                                |
| rows\_read           | The number of rows read from previous steps during the interval.                                                                    |
| rows\_written        | The number of rows written to following steps during the interval.                                                                  |
| rows\_rejected       | The number of rows rejected by the steps error handling during the interval.                                                        |
| errors               | The number of errors that occurred during the execution of the transformation/job.                                                  |
| input\_buffer\_rows  | The size of the step’s input buffer in rows at the time of the snapshot.                                                            |
| output\_buffer\_rows | The size of the output buffer in rows at the time of the snapshot.                                                                  |
