# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables/set-kettle-or-java-environment-variables-in-the-pentaho-mapreduce-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables/set-kettle-or-java-environment-variables-in-the-pentaho-mapreduce-job-entry.md

# Set Kettle or Java environment variables in the Pentaho MapReduce job entry

Pentaho MapReduce jobs are typically run in distributed fashion, with the mapper, combiner, and reducer run on different nodes. If you need to set a Java or Kettle environment variable for the different nodes, such as the**KETTLE\_MAX\_JOB\_TRACKER\_SIZE**, set them in the Pentaho MapReduce job entry window.

**Note:** Values for Kettle environment variables set in the Pentaho MapReduce window override the Kettle environment variable values in the `kettle.properties` file.

To set kettle or java environment variables, complete these steps:

1. In the PDI client, double-click the Pentaho MapReduce job entry, then click the **User Defined** tab.
2. In the **Name** field, set the environment or Kettle variable you need:
   * For Kettle environment variables, type the name of the variable in the **Name** field, like this: `KETTLE_SAMPLE_VAR.`
   * For Java environment variables, preface the value with the `java.system.` prefix, like this: `java.system.SAMPLE_PATH_VAR.`
3. Enter the value of the variable in the **Value** field.
4. Click the **OK** button.
