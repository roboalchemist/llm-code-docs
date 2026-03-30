# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer/options-kinesis-consumer/result-fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/options-kafka-consumer/result-fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer/options-amqp-consumer/result-fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer/options-kinesis-consumer/result-fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer/options-kafka-consumer/result-fields-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer/options-amqp-consumer/result-fields-tab.md

# Result Fields tab

![Result Fields tab in AMQP Consumer](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b4796b14e8f6acf5df0cff6c7bcf4024dd9406de%2FPDITransStep_AMQPConsumer_ResultFieldsTab.png?alt=media)

Use this tab to select the step from the child transformation that will stream records back to the parent transformation. This capability allows records processed by an AMQP Consumer step in the parent transformation to be passed downstream to any other steps included within the same parent transformation.

| Option                  | Description                                                                                                                                                                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Return fields from:** | Select the name of the step (from the child transformation) that will stream fields back to the parent transformation. The data values in these returned fields will be available to any subsequent downstream steps in the parent transformation. |
