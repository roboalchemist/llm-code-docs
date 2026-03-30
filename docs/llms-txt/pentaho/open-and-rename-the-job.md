# Source: https://docs.pentaho.com/install/9.3-install/using-spark-submit-cp/modify-the-sample-spark-submit-job/open-and-rename-the-job.md

# Open and rename the job

To copy files in these instructions, use either the Hadoop Copy Files job entry or Hadoop command line tools.

Perform the following steps to modify the sample Spark job and understand how a Spark Submit entry works in PDI:

1. Copy a text file that contains words that you would like to count to the HDFS on your cluster.
2. Start the PDI client.
3. Open the `Spark Submit.kjb` job, which can be found in the `design-tools/data-integration/samples/jobs/Spark Submit` folder.
4. Select **File** > **Save As**, and then rename and save the file as `Spark Submit Sample.kjb`.

The `Spark Submit Sample.kjb` file is saved to the `jobs` folder.

![Spark Submit Sample Job](https://3280820413-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fy1poGLvhSUVhf3TOysqu%2Fuploads%2Fgit-blob-dea5a80561fe3bdfd9a2acbdcf69eb7b009c8528%2Fspoonide.png?alt=media)
