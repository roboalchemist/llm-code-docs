# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/what-is-new-in-pdo-for-10.2.1.md

# What's new in Pentaho Data Optimizer

Data Optimizer 10.1 delivers a variety of features and enhancements to help you advance your data operations. Improvements in Data Optimizer 10.1 include:

The ability to tier using rules-based and manual processes between the following data sources: 

* SharePoint/OneDrive to NFS, SMB, S3 and HCP
* NFS to SharePoint/OneDrive, SMB, S3 and HCP
* SMB to SharePoint/OneDrive, NFS, S3 and HCP
* S3 to SharePoint/OneDrive, NFS, SMB and HCP
* HCP to SharePoint/OneDrive, NFS, SMB and S3
* Azure Blob (via NFS) to and from HCP, SharePoint/OneDrive, NFS, SMB and S3

Rules-based tiering and rehydration of HDFS data to S3 and HCP data sources by integration with Hadoop.

The ability to perform data operations where the data source and data destination are the same.

Enhanced rules engine support for better data lifecycle management with new ranges options for relative dates:

* Older than
* In between

Support for optimizations based on file attributes other than business terms to improve flexibility of policy-driven decisions.

Support for additional rules-based file, folder, column, and table attributes for fine-grained control of rules-based operations.

Support for rules-based operations to initiate data profiling and metadata scanning.

Support for file rehydration using the Data Operations page.

Enhanced rules-management now features a history of operations and statistical information.

New dashboards provide integration details about the data sources and data temperatures of files across your environment.
