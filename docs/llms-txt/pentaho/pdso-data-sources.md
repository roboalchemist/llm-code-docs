# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-data-sources.md

# Data Sources

With Data Optimizer, you can tier and purge data from Hadoop Distributed File Systems (HDFS), file shares, and object stores. To process data from these sources, Data Optimizer uses Data Catalog’s data source definitions, which maintain the connection information to your sources. The following data sources are supported in Data Optimizer:

<table data-header-hidden><thead><tr><th width="165"></th><th></th></tr></thead><tbody><tr><td>Type</td><td>Data source</td></tr><tr><td>File share</td><td><ul><li>Network File System (NFS), including local file and file-sharing network systems: Vendor agnostic NFS Protocol support including Hitachi Network Attached Storage (HNAS), NetApp Dell/EMC and any vendor utilizing NFS Protocol.</li><li>Server Message Block/Common Internet File System (SMB/CIFS), including local file and file-sharing network systems: Vendor agnostic SMB Protocol support including Hitachi Network Attached Storage (HNAS), NetApp Dell/EMC and any vendor utilizing SMB/CIFS protocol.</li><li>Cloud, including OneDrive and SharePoint.</li><li>Cloud Network Attached Storage (NAS) Azure Blob via NFS.</li></ul></td></tr><tr><td>Object store</td><td><ul><li>Amazon Web Service (AWS) S3.</li><li>Any S3 compatible platform.</li><li>Hitachi Content Platform (HCP).</li></ul></td></tr><tr><td>Block storage</td><td>Hadoop Distributed File System (HDFS) Cloudera and Hortonworks data platform distributions.</td></tr></tbody></table>

Click **Imported** on the **Data Sources** card to open the **Data Sources** page.

![Data Sources page](https://2613472723-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTt1SdXx3alZu8NJiPBj6%2Fuploads%2Fgit-blob-05ddd28465c96bafa6b59fdd8d88af29d5aab7cf%2FPDSO%20Data%20sources%20page.png?alt=media)

You can use the Data Sources page to view existing data source names, status, types, and usages, and to import data sources into Data Optimizer. See the following topics when working with data sources:

* [Viewing a data source](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-data-sources/pdso-view-a-data-source).
* [Importing a data source](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-data-sources/pdso-import-a-data-source).
* [Disabling a data source](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-data-sources/pdso-remove-a-data-source).
