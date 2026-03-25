# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/sort-rows-transformation-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/sort-rows-transformation-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/sort-rows-transformation-step.md

# Sort rows

This step sorts rows based on the fields you specify and on whether they should be sorted in ascending or descending order.

When you use multiple copies of this step in a transformation in parallel, merge together each of the sorted blocks to ensure the proper sort sequence. You can further ensure the proper sequence by adding a [Sorted Merge](https://wiki.pentaho.com/display/EAI/Sorted+Merge) step immediately following the last Sort rows step.

You can create this type of transformation on the local Java Virtual Machine (JVM) with the **Change number of copies to start** option or in a clustered environment using Carte. The **Change Number of copies to Start** option is available through the **Transformation menu**. Right-click any step in the transformation canvas to open the **Transformation menu**.
