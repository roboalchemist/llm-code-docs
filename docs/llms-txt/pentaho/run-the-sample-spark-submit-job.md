# Source: https://docs.pentaho.com/install/9.3-install/using-spark-submit-cp/modify-the-sample-spark-submit-job/run-the-sample-spark-submit-job.md

# Run the sample Spark Submit job

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
