# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer/select-an-engine-mqtt-consumer/using-the-mqtt-consumer-step-on-the-pentaho-engine-cp/options-mqtt-consumer-reuse/result-fields-tab-mqtt-consumer-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer/options-mqtt-consumer-reuse/result-fields-tab-mqtt-consumer-reuse.md

# Result fields tab

![Result fields tab in MQTT Consumer](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-06e5d791cec4dde19e7d08845416e32900123b63%2FPDITransStep_MQTTConsumer_ResultFieldsTab.png?alt=media)

Use this tab to select the step from the child transformation that will stream records back to the parent transformation. This capability allows records processed by an MQTT Consumer step in the parent transformation to be passed downstream to any other steps included within the same parent transformation.

| Option                  | Description                                                                                                                                                                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Return fields from:** | Select the name of the step (from the child transformation) that will stream fields back to the parent transformation. The data values in these returned fields will be available to any subsequent downstream steps in the parent transformation. |
