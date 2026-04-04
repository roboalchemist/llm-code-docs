# Source: https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/bulk-load-into-amazon-redshift.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-amazon-redshift.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-amazon-redshift.md

# Bulk load into Amazon Redshift

The Bulk load into Amazon Redshift entry leverages Amazon Redshift's [COPY](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html) command for greater automation while populating your Amazon Redshift cluster with your PDI data, eliminating the need for repetitive SQL scripting. By using the Redshift `COPY` command, this entry can take advantage of parallel loading and cloud storage for high performance processing.
