# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr/create-a-dimension-key-in-shared-dimension-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr/create-a-dimension-key-in-shared-dimension-step.md

# Create a dimension key in Shared Dimension step

To use a shared dimension, you will need to designate one annotation in the Shared Dimension step as the dimension key. Since you can create multiple annotations on the same field, you can use a selected field as an annotation and as the dimension key. For example, you might want to create an attribute and a dimension key on the field Year in your time dimension.

1. If you have not done so already, complete steps 1-8 of [Create a shared dimension](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr/create-a-shared-dimension).
2. Select **Create Dimension Key** from the **Actions** menu.

   The **Name - Value** table auto-populates with the **Dimension** attribute.

   ![Create dimension key](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-89ede2e77c83caa95decc395941feeca1e59463b%2FSDR_CreateDimensionKey.png?alt=media)
3. Enter or select a dimension in the **Value** field for **Dimension**. The selected field will be used as the key for this dimension.
4. Click **OK** to finish or click **Cancel** to exit.

   In the Shared Dimension dialog box, the selected field will now appear with the summary that it is the key for the shared dimension. For example, the field `'Calendar Year'` may display `'Calendar Year is key for dimension Year'` in the **Summary** column.

   ![Shared Dimension with Calendar Year](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3408aca048ce6e8e6c07a57b36be77c556f7f66e%2FSDR_SharedDimension_db.png?alt=media)

You can use a single field more than once, so you will be able to use the field you selected here for both the key and to create annotations.
