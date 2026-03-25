# Source: https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/transformation-job-entry-cp.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/transformation-job-entry-cp.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/transformation-job-entry-cp.md

# Transformation (job entry)

The Transformation entry runs a previously-defined transformation within a job. This entry is the access point from your job to your ETL activity (transformation).

An example of a common job includes getting FTP files, checking the existence of a necessary target database table, running a transformation that populates that table, and emailing an error log if a transformation fails. For this example, the Transformation entry defines which transformation to run to populate the table.
