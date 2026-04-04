# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-shared-dimension.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr/create-a-shared-dimension.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr/create-a-shared-dimension.md

# Create a shared dimension

This section describes how to create a shared dimension.

**Note:** Be sure to create one annotation to serve as the dimension key.

1. In the **Design** tab, click the **Flow** folder, and then double-click the **Shared Dimension** step icon. Alternatively, you can drag the step icon on to the transformation canvas.

   ![Shared Dimension step icon](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-76752a8078db36e65d6947af57833a49b8bda80d%2FSDR_SharedDimension_Icon.png?alt=media)
2. Double-click the **Shared Dimension** icon to open the Shared Dimension dialog box.
3. Enter a name for the step in the **Step name** field.
4. If you are basing your new dimension on an existing shared dimension, select it from the **Shared Dimension Name** drop-down list of available shared dimensions, or enter a new name for it.
5. Select a source to associate your dimension from the **Data Provider Step** drop-down list.

   The following steps are valid sources:

   * Combination Lookup
   * Database Lookup
   * Dimension Lookup
   * Insert/Update
   * Table Output
   * Vertica Bulk Loader
6. Enter a description of the shared dimension in the **Description** field.
7. Select available fields for annotation.
   1. Click the **Select Fields** button to open the Select Fields to Annotate dialog box.
   2. Double-click the fields in the **Available Fields** list to add them to the**Selected Fields** list.

      For example, you might select **Year** to annotate as your dimension key and **Year**, **Month**, and **Week** to annotate as attributes Optionally, you can use the arrows to move one or more fields to the **Selected Fields** list.
   3. When finished, click **OK** to close the dialog box. The selected fields now display in the **Annotations** table featuring the following columns:

| Column           | Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Field**        | Lists the names of the fields selected for annotation.                                                                                                                                                                                                                                                                                                                                                                               |
| **Model Action** | <p>Specifies which model action is being taken:- <a href="../using-the-annotate-stream-step/use-the-annotate-stream-step/creating-attributes">Creating attributes</a></p><ul><li><a href="../using-the-annotate-stream-step/use-the-annotate-stream-step/creating-link-dimensions/create-a-dimension-key">Create a dimension key</a>: the selected field will be designated as the dimension key for the shared dimension.</li></ul> |
| **Summary**      | Displays a summary of that specific annotation.                                                                                                                                                                                                                                                                                                                                                                                      |

8\. Now you can create \[annotations]\(../Using%20the%20Annotate%20Stream%20step.md) for the selected fields.

```
1.  To annotate a field, double-click it in the **Annotations** section. Optionally, you can select the select the field in the **Annotations** table and then select the **Edit** \(Pencil icon\) in the upper-right corner.

    The Annotate dialog box appears for the selected field.

2.  In the **Actions** field, click the drop-down arrow to select one of the following actions:

    -   **Create Attribute**. See [Creating attributes](../Using%20the%20Annotate%20Stream%20step/Use%20the%20Annotate%20Stream%20step/Creating%20attributes.md).
    -   **Create Dimension Key**. See [Create a dimension key](../Using%20the%20Annotate%20Stream%20step/Use%20the%20Annotate%20Stream%20step/Creating%20Link%20Dimensions%20for%20SDR/Create%20a%20dimension%20key.md).
3.  You can use the **Previous** and **Next** buttons to navigate through the fields. When finished, click **OK** to continue or **Cancel** to close the dialog box without saving your annotations.

    **Note:** You can remove a field from the **Annotations** section by selecting it in the table and then clicking the **Delete** \(X icon\) in the upper-right corner.
```

9\. Click **Apply** to save changes you made to an annotation. Click **OK** to continue or **Cancel** to close the dialog box.

This is an example of the Shared Dimensions dialog box.

![Shared Dimension step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3408aca048ce6e8e6c07a57b36be77c556f7f66e%2FSDR_SharedDimension_db.png?alt=media)
