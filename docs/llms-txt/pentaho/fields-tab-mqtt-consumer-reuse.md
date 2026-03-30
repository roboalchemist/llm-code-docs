# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer/select-an-engine-mqtt-consumer/using-the-mqtt-consumer-step-on-the-pentaho-engine-cp/options-mqtt-consumer-reuse/fields-tab-mqtt-consumer-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer/options-mqtt-consumer-reuse/fields-tab-mqtt-consumer-reuse.md

# Fields tab

![Fields tab in MQTT Consumer](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-ba5d612c88fdfc3f99a8977022b1d0f0a58459b3%2FPDITransStep_MQTTConsumer_FieldsTab.png?alt=media)

Use this tab to define the fields in the record format.

| Option          | Description                                                                                                                                                                                                                                                                              |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Input Name**  | <p>The input name is received from the MQTT streams. The following are received by default:</p><ul><li><strong>message</strong></li></ul><p>The individual message contained in a record.</p><ul><li><strong>topic</strong></li></ul><p>The category to which records are published.</p> |
| **Output Name** | The **Output Name** can be mapped to subscriber and member requirements.                                                                                                                                                                                                                 |
| **Type**        | This will always be a String. This field applies to the **Message** and **Topic** input names.                                                                                                                                                                                           |
