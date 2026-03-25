# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/creating-annotation-groups.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/creating-annotation-groups.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/creating-annotation-groups.md

# Creating annotation groups

Annotation groups are useful when data sources, such as a weblog table, are reused in many transformations. Whenever this table is used, you can link to the shared annotation group to get model information on each table field. If the table were to ever change, then the annotations would only need to be updated in one place.

You can create multiple annotations based on the same annotation group by copying the group, and then saving it with a different name. You can do this as many times as you need to make a series of related annotation groups, such as annotations for time dimensions.

You must create a group to save your annotations. This group can be saved as just a local group or as a shared group. When the group is saved [locally](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step/creating-annotation-groups/create-an-annotation-group-locally), it is saved to the transformation on your machine. When you select **Shared**, it will also be stored in the metastore and available to other users.
