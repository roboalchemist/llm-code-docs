# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/working-with-analyzer-measures/view-or-update-base-measures.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/working-with-analyzer-measures/view-or-update-base-measures.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-measures/view-or-update-base-measures.md

# View or update base measures

These instructions are for both measures and calculated measures created in PDI and published in Analyzer. Be aware that there are some slight differences in the Properties dialog box based on whether you have selected a measure or a calculated measure.

1. In the **Available fields** list on the left, click the name of the measure you want to view or edit, and then click the Down Arrow to the right of the measure name.

   A shortcut menu appears.
2. Click **Properties**.

   The Properties dialog box for that measure displays.

   **Note:** Note that if you are assigned the **Manage Data Sources** operation permission, you can edit several of these fields. Otherwise, these fields are read-only.

   ![Measure properties](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-958be00ecf7738cf86e3901c997c8a62f895dd36%2FAnalyzer_MeasurePropertiesDB.png?alt=media)
3. You can view and/or edit the following fields.

| Field            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Display Name** | The name of the measure as it displays in the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Aggregation**  | <p>The aggregation type is how the measure combines the data. Use the drop-down list to select an aggregation type from a system-defined list. Options include:- <strong>SUM</strong></p><ul><li><strong>AVERAGE</strong></li><li><strong>COUNT</strong></li><li><strong>COUNT\_DISTINCT</strong></li><li><strong>MINIMUM</strong></li><li><strong>MAXIMUM</strong><br>Note that <strong>COUNT</strong> and <strong>COUNT-DISTINCT</strong> are only applicable for non-numeric fields.</li></ul><p>This field only displays for measures, not for calculated measures.</p> |
| **Format**       | <p>Choose how this measure should be formatted, such as currency, general number, or percentage. Use the drop-down arrow to select a format from a system-defined list, or select the <strong>Text</strong> icon next to the field to enter a custom format.</p><p>See <a href="../working-with-analyzer-fields/format-field-options">Format Field Options</a> for more information on selecting the appropriate format for your report.</p>                                                                                                                                |
| **Description**  | The description of the measure, if any. This field is always read-only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Type**         | The type of field, such as measure. This field is always read-only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **MDX**          | The formula for the measure as an MDX statement. This field is always read-only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

4\. When finished editing, click \*\*OK\*\* to save and apply your changes, or \*\*Cancel\*\* to close the dialog box without saving your changes to the measure.
