# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/pdi-hadoop-job-workflow.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/pdi-hadoop-job-workflow.md

# PDI Hadoop job workflow

PDI enables you to execute a Java class from within a PDI client job to perform operations on Hadoop data. The way you approach doing this is similar to the way would for any other PDI job. The specifically-designed job entry that handles the Java class is Hadoop Job Executor. In this illustration it is used in the WordCount - Advanced entry.

![Hadoop Job Executor Workflow](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-7a928837cdb2a48c03d9eece0bf68e5e4b7fed96%2FHadoopJobExecutorWordCount.png?alt=media)

TheHadoop Job Executor dialog box enables you to configure the entry with a `.jar` file that contains the Java class.

![Hadoop Job Executor dialog](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-95caa0f6f603edbbabe96a361fd5b3e67a4956e8%2Fhadoopjobexecutor_wordcount.png?alt=media)

If you are using the Amazon Elastic MapReduce (EMR) service, you can use the Amazon EMR Job Executor job entry to execute the Java class. This differs from the standard Hadoop Job Executor in that it contains connection information for Amazon S3 and configuration options for EMR.

![Amazon EMR Job Executor job entry](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-c1ff285f722d4e13bc46deecff07319e36933450%2FAmazonEMREntry.png?alt=media)
