# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/optimizing-spark-tuning/step-3-set-the-spark-tuning-options-on-a-pdi-step-in-the-transformation.md

# Step 3: Set the Spark tuning options on a PDI step in the transformation

If possible, ensure that no other jobs are running on the cluster.

Spark parameters specified within a step apply to a specific user and temporarily add further step considerations. For example, if you find that you are only partially filling your executors when running the KTR, you may want to change the **repartition.numPartitions** and **coalesce** parameters for a specific step. You can include the parameters in the step so that they execute only when the transformation is run.

Use the following steps to fine-tune Spark for a specific step in the KTR.

1. Set the Spark parameters as described in [Setting PDI step Spark tuning options](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/opening-spark-tuning-options-cp/setting-spark-tuning-options).
2. Run the transformation on the cluster and evaluate the results as recorded in the **Logging** tab on the Execution Results panel of PDI.

   The step names and tuning options for the Spark application are recorded in the **Logging** tab in the Execution Results panel of PDI.

   ![PDI logging of Spark tuning options](https://3280820413-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fy1poGLvhSUVhf3TOysqu%2Fuploads%2Fgit-blob-72431554c9bfcaef8bc082ffe828a3be3aa02746%2FPDI_Logging_SparkStepTunings2.png?alt=media)
3. Modify the values of the Spark parameters then rerun the transformation.
4. Repeat step 3 as needed to collect performance results data for different values.
5. Examine the results of your iterations in the log.
6. Set the Spark parameters in the step according to the values that produced the fastest runtime.

You have tuned Spark for the step in the KTR, completing the Spark optimization process. You may need to reevaluate your tunings from time to time, such as if you add additional steps to your KTR.
