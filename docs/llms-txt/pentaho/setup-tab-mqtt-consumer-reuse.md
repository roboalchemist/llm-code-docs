# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer/select-an-engine-mqtt-consumer/using-the-mqtt-consumer-step-on-the-pentaho-engine-cp/options-mqtt-consumer-reuse/setup-tab-mqtt-consumer-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer/options-mqtt-consumer-reuse/setup-tab-mqtt-consumer-reuse.md

# Setup tab

![Setup tab in MQTT Consumer](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-22d697a4745e18a2587a717ba9b159b4e4dd17ab%2FPDI_MQTT_consumer_step_setup_tab_new_client-ID_option.png?alt=media)

In the **Setup** tab, define the connections used for receiving messages, topics to which you want to subscribe, and the consumer group for the topics.

| Option                       | Description                                                                                                                                                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Connection**               | Specify the address of the MQTT server to which this step will connect for sending or retrieving messages.                                                                                                                                                            |
| **Client ID**                | Specify a unique ID for the MQTT client. The MQTT server uses this Client ID to recognize each distinct client and that client's current state.                                                                                                                       |
| **Topics**                   | Specify the MQTT topic(s) to be subscribed to.                                                                                                                                                                                                                        |
| **Quality of Service (QoS)** | <p>Quality of Service (QoS) is a level of guarantee for message delivery. Select one of the following options.</p><ul><li>At most once (0), which is the default value</li><li>At least once (<strong>1</strong>)</li><li>Exactly once (<strong>2</strong>)</li></ul> |
