# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/kafka-offset/options-kafka-ofset/offset-settings-tab-kafka-offset.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/kafka-offset/options-kafka-ofset/offset-settings-tab-kafka-offset.md

# Offset Settings tab

To reset the offset value, set the start date in the **Offset timestamp** field and select the format in the **Timestamp format** field.

![Offset settings tab for Kafka Offset job](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-25254fb899ff68c6ee17b1c88be485f5e7cc21c1%2FPDI%20Kafka%20Offset%20Offset%20.Settings%20tab.png?alt=media)

| Option               | Description                                                                                                                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Offset timestamp** | Specifies the start date timestamp to use as the offset. The timestamp can be a past or future time. When this job is run, the offset value in each partition will be reset to timestamp given. |
| **Timestamp format** | <p>Specifies the timestamps format for the offset.</p><p>When epoch value is given, the timestamp format is not needed.</p>                                                                     |
