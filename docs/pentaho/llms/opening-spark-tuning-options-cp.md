# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/opening-spark-tuning-options-cp.md

# Opening the PDI step Spark tuning options

You can access the Spark tuning options from a PDI step by right-clicking on the step in the canvas and selecting **Spark tuning parameters** from the menu.

![Spark Tuning Parameters menu](https://3280820413-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fy1poGLvhSUVhf3TOysqu%2Fuploads%2Fgit-blob-336d16f61a192cc0fde1cf3a3ed669ec7671bad9%2FPDI_TRANSSTEP_SPARKTUNING_MENU.png?alt=media)

**Note:** Spark tuning options are not available for some PDI steps, such as most Consumer steps and the Avro, Hbase, Orc, and Parquet input steps.

The **Spark tuning parameters** dialog box appears. Click in the column to view the Spark tuning options available for that step in the dialog box. These options vary from step to step, depending on the scope of the step.

![Spark tuning dialog box](https://3280820413-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fy1poGLvhSUVhf3TOysqu%2Fuploads%2Fgit-blob-9af45e3f8c939d545a6ebc840234f34b96f6cd40%2FPDI_Transstep_SparkTuning_DB.png?alt=media)

**Note:** Support for the step-level Spark tuning options are based on the Spark version installed on the cluster. While Pentaho 9.3 is coded for Spark 2.3, the actual implementation varies with the Spark version running on the cluster.
