# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step.md

# Use the Annotate Stream step

You can create annotations in different ways. The annotation type which you create determines which properties are shown in the dialog box to complete that annotation. This task assumes you are in the transformation canvas of the PDI client.

1. In the **Design** tab, click the **Flow** folder, and then double-click the Annotate Stream step.

   Alternatively, you can drag the step icon on to the transformation canvas.

   ![Annotate Stream step icon](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-99f8ea6655214d5d7e350d9da07fd04eb7cd92da%2FSDR_AnnotateStreamIcon.png?alt=media)
2. Double-click the **Annotate Stream** icon to open the Annotate Stream dialog box.
3. Enter a name for the step in the **Step name** field.
4. Select if you want to save the step locally or if you want to share it.
   * **Local**: The annotations will be saved locally into the transformation.
   * **Shared**: Allows you to select, create, or rename a shared group of annotations for use by PDI users.
5. (Optional) Enter a description for the annotations in the **Description** field.
6. Select available fields for annotation.
   1. Click **Select Fields** to open the Select Fields to Annotate dialog box.
   2. Double-click the fields in the **Available Fields** list to add them to the Selected Fields list. Optionally, you can use the arrows to move one or more fields to the **Selected Fields** list.
   3. When finished, click **OK** to close the dialog box.

      The selected fields now display in the **Annotations** table featuring the following columns:

      | Column           | Description                                                                                                   |
      | ---------------- | ------------------------------------------------------------------------------------------------------------- |
      | **Field**        | Lists the names of the fields selected for annotation.                                                        |
      | **Model Action** | Specifies which model action is being taken: **Create Measure**, **Create Attribute**, or **Link Dimension**. |
      | **Summary**      | Displays a summary of that specific annotation.                                                               |
7. Now you can annotate the selected fields.

   1. To annotate a field, double-click it in the **Annotations** section. Optionally, you can select the field in the **Annotations** table and then click the **Edit** (pencil) icon in the upper-right corner.

      The Annotate dialog box appears for the selected field.
   2. In the **Actions** field, click the drop-down arrow to select one of the following actions.

      For help on selecting values, select the topic link beside each action.

      * Create Measure. See [Creating measures on stream fields](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step/creating-measures-on-stream-fields).
      * Create Attribute. See [Creating attributes](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step/creating-attributes).
      * Link Dimension. See [Creating link dimensions](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step/creating-link-dimensions).
   3. You can use the **Previous** and **Next** buttons to navigate through the fields. When finished, click **OK** to continue or **Cancel** to close the dialog box without saving your annotations.

   **Note:** You can remove a field from the **Annotations** section by selecting it in the table and then clicking the **Delete** (X icon) in the upper-right corner.
8. (Optional) You can create a calculated measure to add to the model.
   1. Click the **Add Calculated Measure** button to open the Annotate dialog box.
   2. Fill in the following fields:

| Field                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Measure Name**                                          | Enter the name of the calculated measure you are creating.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Format**                                                | <p>Specify how you want your calculated measure to appear in a report, such as currency, general number, or percentage. Use the drop-down arrow to select a format from a system-defined list, or type in the field to enter a custom format. For example, to display the measure as a percentage, you might select <code>0.00 %</code>.</p><p>See the <strong>Pentaho Business Analytics</strong> document for more information on selecting the appropriate format string.</p> |
| **Formula**                                               | Enter the formula of your calculated measure. This is an MDX statement. For more information, see the **Pentaho Business Analytics** document.                                                                                                                                                                                                                                                                                                                                   |
| **When calculating subtotals use this formula** check box | (Optional) Select this check box if you want this calculated measure to be used in calculations of subtotals in your reports.                                                                                                                                                                                                                                                                                                                                                    |
| **Hide this calculated measure in the model**             | (Optional) Select this check box if you want to hide this calculated measure in the data model. When selected, the calculated measure will be a part of the model, but will not be visible to users when the data source is opened in Analyzer. This check box is useful for calculated measures needed to build a proper data model, but not needed for analytic purposes.                                                                                                      |

3\. Use the \*\*Previous\*\* and \*\*Next\*\* buttons to navigate through the fields. When finished, click \*\*OK\*\* to add the attribute to the annotations list or \*\*Cancel\*\* to close the dialog box without saving your annotations. The calculated measure displays in the \*\*Annotation\*\* table with the \*\*Model Action\*\* option \*\*Create Calculated Measure\*\* and a summary detailing the measure name and formula.

```
**Note:** The calculated measure is not validated until it is selected in Analyzer. Calculated measures will display as base measures in the **Available Fields** list in Analyzer.
```

9\. Click **Apply** to save your changes.

```
You can continue to create or edit annotations.
```

10\. When finished, click **OK** to save your changes and close the dialog box, or **Cancel** to discard your changes and close the dialog box.

![Annotate Stream step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-49be19fd843781b708c21166cb6b08aa56e4f9ca%2FSDR_AnnotateStreamStep.png?alt=media)
