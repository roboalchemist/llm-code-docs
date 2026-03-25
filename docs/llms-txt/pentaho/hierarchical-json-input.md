# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/hierarchical-json-input.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hierarchical-json-input.md

# Hierarchical JSON Input

You can use the Hierarchical JSON input step to load JSON data into PDI from a file. You can use filters to load only the desired data. The data can be split on a hierarchical data path using wildcards. You can specify the input file directly in this step or use a list of files from an input field. See [Hierarchical data](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/hierarchical-data) for an overview of hierarchical data in Pentaho.

You can use filters on the input even if you do not use the **Split rows across path** field, but the filters must be set to the root level of the HDT you want to load. When you use the **Split rows across path** field you must specify all filter paths rooted at the split path. If you do not use the **Split rows across path** field a normal HDT extraction path is used. See the [Hierarchical data path specifications](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/hierarchical-data/hdt-path-specification).
