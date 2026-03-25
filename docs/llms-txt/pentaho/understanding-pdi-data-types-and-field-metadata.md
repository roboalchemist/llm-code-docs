# Source: https://docs.pentaho.com/pdia-data-integration/understanding-pdi-data-types-and-field-metadata.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata.md

# Understanding PDI data types and field metadata

This section is for users who want to maximize the efficiency of their transformation and job results.

As a best practice for producing consistent, predictable outcomes when working with your data in PDI, you must consider how the Pentaho engine processes different data types and field metadata in transformations and jobs. For example, steps like [Avro Input](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Avro%20Input=GUID-88F915B8-9584-4C38-9974-36D62478D0E4=3=en=.md) and [Text File Input](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp), require additional considerations to best meet your working requirements for specific data types, mathematical operations, number conversions, and formatting.

**Note:** As a rule, data is never modified by metadata inside of PDI. Data is only modified when PDI writes to files or similar objects, but not to databases. Refer to the sections below that apply to your use case.
