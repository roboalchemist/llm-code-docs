# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/optimizing-spark-tuning/step-2-adjust-the-spark-parameters-in-the-transformation.md

# Step 2: Adjust the Spark parameters in the transformation

If possible, ensure that no other jobs are running on the cluster.

Spark parameters specified by a transformation parameter apply to a specific user and temporarily override the baseline for additional KTR considerations. For example, if you want to change the **spark.driver.memory**, you can embed the appropriate Spark parameter setting in the KTR so that it executes only when the transformation is run.

**Note:** If an identical property is also set on the cluster or Pentaho Server, the user's KTR takes precedence.

Use the following steps to optimize Spark tuning locally.

1. Set the Spark parameters as described in [Set the Spark parameters locally in PDI](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/spark-tuning-process/application-tuning-parameters-for-transformations/set-the-spark-parameters-locally-in-pdi).
2. Run the transformation on the cluster and evaluate the results as recorded in the **Logging** tab in the Execution Results panel of PDI.

   The local tuning for the Spark application is recorded in the **Logging** tab in the Execution Results panel of PDI.

   ![PDI logging of the Spark transformation parameters](https://3280820413-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fy1poGLvhSUVhf3TOysqu%2Fuploads%2Fgit-blob-dbc049eb8bfcc26bfeb52fb4a114e77c94181b72%2FPDI_Logging_SparkTransformProperties.png?alt=media)
3. Modify the values of the Spark parameters then rerun the transformation.
4. Repeat step 3 as needed to collect data on the performance results of the different values.
5. Examine the results of your iterations in the log.
6. Set the Spark parameters in the transformation according to the values that produced the fastest runtime.

You have locally tuned Spark for your transformation. If needed, proceed to [Step 3: Set the Spark tuning options on a PDI step in the transformation](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/optimizing-spark-tuning/step-3-set-the-spark-tuning-options-on-a-pdi-step-in-the-transformation) to apply step-level tuning. For example, additional tuning may be required to run the step if it runs slowly or if it inefficiently consumes available memory.
