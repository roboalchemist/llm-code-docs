# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-data-operations.md

# Manage data operations

In Pentaho Data Catalog, data operations refer to the various processes and strategies employed to optimize the storage and management of data across different environments. Data operations are designed to improve performance, reduce costs, and ensure efficient utilization of storage resources. You can monitor, verify, and examine details about your past, current, and pending data operations on the Data Operations page.

## Tour the Data Operations page

In Data Catalog, the Data Operations page gives a user-friendly interface to view the data operations. To access the page, see [View data operations](#view-data-operations). On the page, you can filter operations using the **Completed**, and **Failed** tabs. In addition, you can enter the keywords in **Search** to search in the Data Operations names and shows the results of the operations items.

![Data Operations Landing Page](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-7e54eb6238bbd7e1f01fb87a8132f5bdd5b60633%2FData%20Opeartions%20-%20Landing%20page.jpg?alt=media)

On the Data Operations page, you can view the list of data operations according to their status and you can filter the results using the **Completed** and **Failed** tabs. In addition, you can enter the keywords in **Search** to find names and view the results of specific operations. The following table describes the features and information available on the page.

<table><thead><tr><th width="152.88885498046875" align="center">Column</th><th>Description</th></tr></thead><tbody><tr><td align="center"><p><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-df92ee60a4db655bf59fd4e197fbbcd4fdbde731%2FPDSO%20More%20options.png?alt=media" alt=""></p></td><td><strong>More options</strong> icon. Click <strong>More options</strong> and choose <strong>Rehydration</strong> to rehydrate a file. For more information, see <a href="#rehydrate">Rehydrate</a>.</td></tr><tr><td align="center"><strong>Name</strong></td><td>Name of the file.</td></tr><tr><td align="center"><strong>Path</strong></td><td>Path of the file.</td></tr><tr><td align="center"><strong>Source</strong></td><td>The source of the file.</td></tr><tr><td align="center"><strong>Type</strong></td><td>The action performed or scheduled.</td></tr><tr><td align="center">Icon</td><td>Definition</td></tr><tr><td align="center"><p><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-586236bc4361113cf5c3c70cb04dc13a6194abc7%2FMigrated.png?alt=media" alt=""></p></td><td>File tiered.</td></tr><tr><td align="center"><p><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-53baf447b978bd469b3eb0bba01c6db3671aac58%2FDeleted.png?alt=media" alt=""></p></td><td>File purged.</td></tr><tr><td align="center"><p><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-01ba9c97f0da5d6b58b99a609183a6f49383a78d%2FRehydrate.png?alt=media" alt=""></p></td><td>File rehydrated.</td></tr><tr><td align="center"><strong>Destination</strong></td><td>The destination of the file.</td></tr><tr><td align="center"><strong>Source Type</strong></td><td>The source type of the file.</td></tr><tr><td align="center"><strong>Destination Type</strong></td><td>The data target type for the tiered or rehydrated file.</td></tr><tr><td align="center"><strong>Status</strong></td><td><p>The status of the data operation: - SUCCESS</p><ul><li>INIT (Initializing)</li><li>FAILED</li></ul></td></tr><tr><td align="center"><strong>Tag</strong></td><td>The tag applied to the file.</td></tr><tr><td align="center"><strong>Action</strong></td><td><p>The method used to begin the operation:- UI</p><ul><li>RULE</li></ul></td></tr><tr><td align="center"><strong>File Format</strong></td><td>The file format of data.</td></tr><tr><td align="center"><strong>Size</strong></td><td>The size of the file.</td></tr><tr><td align="center"><strong>Message</strong></td><td>The message returned about the data operation by Data Optimizer.</td></tr><tr><td align="center"><strong>Started</strong></td><td>Time the operation began.</td></tr><tr><td align="center"><strong>Ended</strong></td><td>Time the operation ended.</td></tr><tr><td align="center"><strong>Time taken</strong></td><td>Total time taken for the operation.</td></tr></tbody></table>

## View data operations

You can use the Data Operations page to understand the results of the data operations. It provides a detailed view of all completed, failed, or terminated operations helping you ensure data integrity and traceability.

Perform the following steps to view data operations:

1. On the left navigation menu, click **Data Operations**.

   The Manage Data Operations page appears.
2. On the **Data Operations** card, click any one, **Submitted**, **Completed**, **Failed**, or **Terminated**.

   The Data Operations page appears displaying data operation records based on the selected status. You can see detailed metadata about each data operation. For more information, see [Tour the Data Operations page](#tour-the-data-operations-page).

## Rehydrate

You can restore tiered files using rehydration. Rehydration uses the stub file created from tiering to restore the contents of the file. The stub file contains recall information that Data Catalog uses to rehydrate the file from the target to its original data source. You can selectively recall any file from its storage location and perform rehydration if a stub file exists in the file system.

**Note:**

* When a file is tiered, the last access time of the file does not change.
* You cannot rehydrate a purged or deleted file.

### Rehydrate a migrated file

Perform the following steps to rehydrate a file, except for HDFS:

1. On the **Menu**, click **Management**.

   The Manage Your Environment page opens.
2. On the **Data Operations** card, click **Submitted**, **Completed**, or **Failed**.

   The Data Operations page appears.
3. On the Data Operations page, locate the data operation or file that you want to restore, click the more icon, and then select **Rehydrate**.

   **Note:** You can also use **Search** to locate the file by name.

   Rehydration begins. You can monitor the status of the file’s rehydration on the Data Operations page.
