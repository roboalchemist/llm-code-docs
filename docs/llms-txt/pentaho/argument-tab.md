# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/job-job-entry/options-job-job-entry/argument-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/job-job-entry/options-job-job-entry/argument-tab.md

# Argument tab

![Argument tab, Job (job entry)](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-8bc0e6a8ca7734066cd02ad395f18e599d3a1745%2FPDI_JobJE_ArgumentsTab.png?alt=media)

Enter the following information to pass arguments to the job:

| Option                        | Description                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Copy results to arguments** | Copies the results from a previous transformation as arguments of the job using the [Copy rows to result](http://wiki.pentaho.com/display/EAI/Copy+rows+to+result)step. If **Execute for every input row** is selected, then each row is a set of command-line arguments to be passed to the job; otherwise, only the first row is used to generate the command-line arguments. |
| **Argument**                  | Specify which command-line arguments will be passed to the job.                                                                                                                                                                                                                                                                                                                 |
