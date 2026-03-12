# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/optimizing-spark-tuning/step-1-set-the-spark-parameters-on-the-cluster.md

# Step 1: Set the Spark parameters on the cluster

If possible, ensure that no other jobs are running on the cluster.

Use the following steps to optimize Spark tuning globally.

1. Set the Spark parameters as described in [Set the Spark parameters globally](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/spark-tuning-process/application-tuning-parameters-for-transformations/set-the-spark-parameters-globally).
2. Run a single step PDI transformation on the cluster using a small number of executors per node and record the number of minutes it takes for the run to complete.
3. Increment the number of executors per node by 1, and then rerun the PDI transformation and record the time it takes to complete.
4. Repeat step 3 for as many executors per node that you want to verify.

   The following table shows an example of the results using the **Sort** PDI transformation step.

   | PDI step | Run number | Executors per node | Job duration |
   | -------- | ---------- | ------------------ | ------------ |
   | **Sort** | 1          | `2`                | 37 minutes   |
   | **Sort** | 2          | `3`                | 42 minutes   |
   | **Sort** | 3          | `4`                | 38 minutes   |
   | **Sort** | 4          | `5`                | 40 minutes   |
5. Evaluate the results of the runs, then choose the fastest, most repeatable run.

   The performance results of your executed transformations are available on the YARN ResourceManager and Spark History Server.
6. Set the values for the Spark parameters in the `application.properties` file according to the findings in step 5.
7. Rerun the transformation with the selected value several times to verify the results.

   The global tuning for the Spark application is recorded in the **Logging** tab in the Execution Results panel of PDI.

   ![PDI logging of Spark application parameters](https://3280820413-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fy1poGLvhSUVhf3TOysqu%2Fuploads%2Fgit-blob-4259fee3f52acab818f21118b707da579b1bc1a1%2FPDI_Logging_SparkAELproperties.png?alt=media)

Spark parameters are set on the cluster or Pentaho Server as a baseline and apply to all users and all transformations. If needed, proceed to [Step 2: Adjust the Spark parameters in the transformation](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/optimizing-spark-tuning/step-2-adjust-the-spark-parameters-in-the-transformation) to tune Spark for your transformation. For example, additional tuning may be required to run the KTR if it runs slowly or consumes excessive resources.
