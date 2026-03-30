# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/spark-submit/options-spark-submit-job/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/job-job-entry/options-job-job-entry/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-snowflake/options-snowflake-bulk-loader/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-amazon-redshift/options-bulk-load-into-amazon-redshift/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/single-threader/options-single-threader/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/parquet-output/options-parquet-output/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mqtt-producer/options-mqtt-producer/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer/options-kinesis-consumer/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kafka-producer/options-kafka-producer/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/options-kafka-consumer/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/jms-producer/jms-connection-information/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/options-etl-metadata-injection/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/spark-submit/options-spark-submit-job/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/job-job-entry/options-job-job-entry/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-snowflake/options-snowflake-bulk-loader/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-amazon-redshift/options-bulk-load-into-amazon-redshift/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/single-threader/options-single-threader/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/parquet-output/options-parquet-output/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mqtt-producer/options-mqtt-producer/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer/options-kinesis-consumer/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-producer/options-kafka-producer/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/options-kafka-consumer/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/jms-producer/jms-connection-information/options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/options-etl-metadata-injection/options-tab.md

# Options tab

![ETL Metadata Injection Step Options Tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-c61b0194b346ac6ada4ef256de8479c887854ead%2FPDI_TransStep_ETL_Metadata_Injection_Inject_Options_Tab.png?alt=media)

Enter the following optional settings:

| Option                                         | Description                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Step to read from (optional)**               | (Optional) Select a step in your template transformation to pass data directly to a step following the ETL Metadata Injection step in your current transformation.                                                                                                                                |
| **Field name**                                 | If **Step to read from** is selected, enter the name of the field passed directly from the step in the template transformation.                                                                                                                                                                   |
| **Type**                                       | If **Step to read from** is selected, select the type of the field passed directly from the step in the template transformation.                                                                                                                                                                  |
| **Length**                                     | If **Step to read from** is selected, enter the length of the field passed directly from the step in the template transformation.                                                                                                                                                                 |
| **Precision**                                  | If **Step to read from** is selected, enter the precision of the field passed directly from the step in the template transformation.                                                                                                                                                              |
| **Optional target file (KTR after injection)** | For initial transformation development or debugging, specify an optional file for creating and saving a transformation of your template after metadata injection occurs. The resulting transformation will be your template transformation with the metadata already injected as constant values. |
| **Streaming source step**                      | Select a source step in your current transformation to directly pass data to the **Streaming target step** in the template transformation.                                                                                                                                                        |
| **Streaming target step**                      | Select the target step in your template transformation to receive data directly from the **Streaming source step**.                                                                                                                                                                               |
| **Run resulting transformation**               | Select to inject metadata and run the template transformation. If this option is not selected, metadata injection occurs, but the template transformation does not run.                                                                                                                           |
