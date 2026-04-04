# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/spark-tuning-process/application-tuning-parameters-for-transformations/set-the-spark-parameters-locally-in-pdi.md

# Set the Spark parameters locally in PDI

In PDI, you can customize Spark properties in your transformation to further tune how the Spark cluster process your transformation. By adjusting the applicable tuning parameters in your transformation for the run instance, you are overriding the global settings for the cluster. You can set these properties as run modification parameters or as environment variables.

**Note:** When defining the parameter, you can assign it a default value to use if one is not fetched for it. If you prefer to set the Spark properties using environment variables, see the **Pentaho Data Integration** document for further information on environment variables.

Perform the following steps to set the Spark parameters in PDI:

1. In the PDI, double-click the transformation canvas, or press Ctrl T.

   The **transformation properties** dialog box opens.
2. Click the **Parameters** tab.

   The **Parameters** table opens.
3. Enter the Spark parameter in the **Parameters** column and the value for that property in the **Default Value** column of the table. Optionally, enter a description.

   **Note:** If the parameter and the variable share the same name, the parameter takes precedence.

   ![Parameters tab, Transformation properties dialog box](https://3280820413-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fy1poGLvhSUVhf3TOysqu%2Fuploads%2Fgit-blob-a5437d35d3254236987b5195ae572658e100ca06%2FPDI_TranformationProperties_ParametersTab.png?alt=media)
4. Click **OK**.

The performance results of your executed transformations are available in the **Logging** in the Execution Results panel of PDI and on the YARN ResourceManager and Spark History Server. Consult your cluster administrator to view these logs. You can refine the tuning of the cluster at the step level as described in [Optimizing Spark tuning](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark/optimizing-spark-tuning).
