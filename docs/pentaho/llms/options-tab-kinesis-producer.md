# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kinesis-producer/options-kinesis-producer/options-tab-kinesis-producer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kinesis-producer/options-kinesis-producer/options-tab-kinesis-producer.md

# Options tab

In the **Options** tab, define the **Value** for the following write and connection timeout settings:

![Kinesis Producer options tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-c945483b77d1d822f0bce905e3c09f6187bbd524%2FPDI_TransStep_Tab_Options_Kinesis_Producer_width_608.png?alt=media)

| **Name**                                   | **Value**                                                                                                                                                         |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Write Timeout Seconds**                  | Specify a timeout value, in seconds, for the Kinesis Producer step to wait for the next time to write to the KDS stream. The default value is 30.                 |
| **Connection Timeout Seconds**             | Specify a timeout value, in seconds, for the Kinesis Producer step to wait while trying to connect to the server. The default value is 2.                         |
| **Connection Acquisition Timeout Seconds** | Specify a timeout value, in seconds, for the Kinesis Producer step to wait while trying to connect after the initial connection is made. The default value is 10. |
