# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step/creating-link-dimensions/create-a-link-dimension.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step/creating-link-dimensions/create-a-link-dimension.md

# Create a link dimension

This step assumes you have created a shared dimension which you want to use.

These steps guide you through creating a link dimension using the Annotate Stream step.

1. If you haven't done so already, complete steps 1-7 in [Use the Annotate Stream step](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/use-the-annotate-stream-step).
2. Select **Link Dimension** from the **Actions** drop-down menu. The **Name - Value** table auto-populates with a list of annotation properties for the dimension.

   | Component        | Description                                                                                                                                                                                                                                                                                                                                                                              |
   | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Dimension Name   | Enter a name for the dimension. Note that you can overwrite the dimension name set in the [Shared Dimension](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr) step. |
   | Shared Dimension | Enter or select a previously created **Shared Dimension** to link to from the drop-down menu.                                                                                                                                                                                                                                                                                            |

   ![Create link dimension](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f9dee629fbd3161cd797c842f2422426ac071085%2FSDR_CreateLinkDimension.png?alt=media)
3. Use the **Previous** and **Next** buttons to navigate through the fields. When finished, click **OK** to save your annotations and close the dialog box, or **Cancel** to close the dialog box without saving your annotations.

Remember that before your link dimension can be used by others, you must create a dimension key for the shared dimension to link to. When creating annotations, you can use a single field more than once, so you will be able to use the same field for both the key and to create annotations.
