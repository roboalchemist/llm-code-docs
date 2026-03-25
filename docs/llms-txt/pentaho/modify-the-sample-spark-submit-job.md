# Source: https://docs.pentaho.com/install/9.3-install/using-spark-submit-cp/modify-the-sample-spark-submit-job.md

# Source: https://docs.pentaho.com/install/10.2-install/using-spark-submit-cp/modify-the-sample-spark-submit-job.md

# Modify the sample Spark Submit job

The following example demonstrates how to use PDI to submit a Spark job.

### Open and rename the job

To copy files in these instructions, use either the Hadoop Copy Files job entry or Hadoop command line tools.

Perform the following steps to modify the sample Spark job and understand how a Spark Submit entry works in PDI:

1. Copy a text file that contains words that you would like to count to the HDFS on your cluster.
2. Start the PDI client.
3. Open the `Spark Submit.kjb` job, which can be found in the `design-tools/data-integration/samples/jobs/Spark Submit` folder.
4. Select **File** > **Save As**, and then rename and save the file as `Spark Submit Sample.kjb`.

The `Spark Submit Sample.kjb` file is saved to the `jobs` folder.

<figure><img src="https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2FWsnMWPxaZ9bJjpN5ta9G%2Fimage.png?alt=media&#x26;token=0f2f3ca8-6ad9-46b6-8a48-18cfa3b876ad" alt=""><figcaption></figcaption></figure>

### Run the sample Spark Submit job

Complete the following steps to run the sample Spark Submit job:

1. Open the Spark PI job entry.

   Spark PI is the name given to the Spark Submit job entry in the sample.
2. Indicate the path to the spark-submit utility in the **Spark Submit Utility** field.

   It is located where you installed the Spark client.
3. Indicate the path to your Spark examples JAR file (either the local version or the one on the cluster in the HDFS) in the **Application Jar** field.

   The Word Count example is in this JAR.
4. In the **Class Name** field, add the following: `org.apache.spark.examples.JavaWordCount`.
5. We recommend that you set the **Master URL** to `yarn-client`.

   To read more about other execution modes, see the [Submitting Applications article in the Spark documentation](https://spark.apache.org/docs/2.3.2/submitting-applications.html).
6. In the **Arguments** field, indicate the path to the file you want to run Word Count on.
7. Click **OK**.
8. Save the job.
9. Run the job.

As the Spark Submit job entry runs, you will see the results of the word count program in the Execution pane.
