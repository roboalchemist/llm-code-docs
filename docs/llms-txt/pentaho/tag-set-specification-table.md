# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/options-mongodb-input/input-options-tab/tag-set-specification-table.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/options-mongodb-input/input-options-tab/tag-set-specification-table.md

# Tag set specification table

Tags allow you to customize write concerns and read preferences for a replica set. The **Tag set specification** table allows you to specify criteria for selecting replica set members. See [Tag Sets](https://docs.mongodb.com/manual/tutorial/configure-replica-set-tag-sets/index.html) for more information.

Enter the following information in the **Tag Set** fields:

| Field            | Description                                                                                                                                                                                                                                                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **#**            | Indicates the number of the tag set.                                                                                                                                                                                                                                                                                       |
| **Tag set**      | Displays the tag set criteria. You can join, delete, copy, and paste tag sets, then click **Test tag set** to see which replica set members match your **Tag set** specification criteria.                                                                                                                                 |
| **Get Tags**     | Click **Get tags**to retrieve a list of tag sets in the source database. Set are listed in order of execution.                                                                                                                                                                                                             |
| **Join tags**    | Click **Join tags**to append selected tag sets so that nodes matching the criteria are queried or written to simultaneously. If you select individual tag sets, then click Join tags, the tag sets are combined to create one tag set. Note that this change only occurs in the MongoDB Input window, not on the database. |
| **Test tag set** | Click **Test tag set**to display set members that match the tags indicated in the tag set specification. The ID, host name, priority, and tags for each replica set member that matches the tag set specification criteria are displayed.                                                                                  |
