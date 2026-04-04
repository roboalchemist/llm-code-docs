# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step/creating-link-dimensions/create-a-dimension-key.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step/creating-link-dimensions/create-a-dimension-key.md

# Create a dimension key

Before your link dimension can be used by others, you must create a dimension key for the shared dimension to link to.

**Note:** You can create multiple annotations on the same field. For example, you might want to create an attribute and a dimension key on the same field, such as Year, in your time dimension.

1. If you haven't done so already, complete steps 1-7 in [Use the Annotate Stream step](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step).
2. From the list in the **Annotations** table, choose a field to use as the dimension key by double-clicking it.

   For example, you may want to use the field `Calendar Year` as the dimension key for the shared dimension `Year`. Optionally, you can select the field in the **Annotations** table and then click the **Edit** (Pencil icon) in the upper-right corner.

   The Annotate dialog box appears for the selected field.
3. Select **Create Dimension Key** from the **Actions** drop-down menu for the field.

   The **Name - Value** table auto-populates with the name and value of the dimension key. You can edit the value to use as the dimension key.
4. Click **OK** to save the annotation and close the dialog box.

   In the [Shared Dimension](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr) dialog box, the selected field will now appear with the summary that it is the key for the shared dimension. For example, the field `Calendar Year` may display `Calendar Year is key for dimension Year` in the **Summary** column.
