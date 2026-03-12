# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step.md

# Copybook Input

The Copybook Input step reads binary data files that are mapped by a fixed-length COBOL copybook definition file. COBOL definition and binary files are used in IT scenarios that include data stored on mainframes. You can extract the binary data files and the definition files from the mainframe for data transformation and analysis, and avoid using mainframe cycles for complex data analysis tasks.

**Note:** The Copybook Input step performs self-contained static extraction of the data in the binary format. If you only need to perform ETL metadata injection, use the [Read Metadata from Copybook](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Read%20metadata%20from%20Copybook=GUID-6DF7C90E-B8E6-4E70-9E49-EC9CACB1808F=3=en=.md) step. You are not required to use both copybook steps in the same transformation. For more information see [Copybooks in PDI](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/copybook-steps-in-pdi-cp).
