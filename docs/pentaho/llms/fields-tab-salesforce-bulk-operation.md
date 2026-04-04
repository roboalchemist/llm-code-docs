# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-bulk-operation/options-salesforce-bulk-operation/fields-tab-salesforce-bulk-operation.md

# Fields tab

Use this tab to specify the target changes to make in the Salesforce object fields for Insert, Update, and Upsert operations. This tab is not available for bulk delete operations. You cannot include the external id for upsert operations. All data except for dates is converted to strings using pre-existing format masks on the **Stream field**.

![PDI Salesforce bulk operation step Fields tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-46544d357e41a1002d4bf4e441b3f3ff809ab976%2FPDI%20Salesforce%20bulk%20operation%20step%20Fields%20tab.png?alt=media)

| Field            | Description                                                                                                                                                                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Stream field** | Specify the name of the PDI stream field containing the data for the Salesforce object.                                                                                                                                                    |
| **Object field** | Specify the destination Salesforce object field.                                                                                                                                                                                           |
| **Clear nulls?** | A Boolean value that specifies whether null values encountered on the input stream should be cleared from the target Salesforce object. Select **Yes** to remove the value in Salesforce, or **No** (Default) to leave the original value. |
