# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/spark-submit/options-spark-submit-job/files-tab-spark-submit-pdi-entry/java-or-scala-spark-submit-pdi-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/spark-submit/options-spark-submit-job/files-tab-spark-submit-pdi-entry/java-or-scala-spark-submit-pdi-entry.md

# Java or Scala

![Files tab, Java or Scala, Spark Submit](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6b361db91004300e35b327c36815b244c56e9606%2FssPDISpark_Submit-FileTab-Java_and_Scala.png?alt=media)

If you select **Java or Scala** as the file **Type**, the **Files** tab will contain the following options:

| Option              | Description                                                                                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Class**           | Optionally, specify the entry point for your application.                                                                                                                                                                                                                            |
| **Application Jar** | Specify the main file of the Spark job you are submitting. It is a path to a bundled jar including your application and all dependencies. The URL must be globally visible inside of your cluster, for instance, an `hdfs://` path or a `file://` path that is present on all nodes. |
| **Dependencies**    | Specify the **Environment** and **Path** of other packages, bundles, or libraries used as a part of your Spark job. **Environment** defines whether these dependencies are **Local** to your machine or **Static** on the cluster or the web.                                        |
