# Source: https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/job-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/job-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/job-job-entry.md

# Job (job entry)

The Job job entry executes a previously defined job, which allows you to perform functional decomposition: a break out of jobs into more manageable units.

For example, instead of writing a data warehouse load using one job which contains 500 entries, you could create smaller jobs and aggregate them.

**CAUTION:**

Although it is possible to create a recursive, never-ending job that points to itself, you should be aware that such a job will eventually fail with an out of memory or stack error.
