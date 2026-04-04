# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-copybook.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-copybook.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-copybook.md

# Read metadata from Copybook

The Read metadata from Copybook step reads a binary fixed-length copybook definition file and outputs the file and column descriptor information as fields to PDI rows. You can then use these rows with the [ETL Metadata Injection](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/ETL%20metadata%20injection=GUID-DFD39FB2-F48B-46E8-96F6-62F905AF7F3B=3=en=.md) step to populate the [Copybook Input](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Copybook%20Input%20\(pdi%20step\)=GUID-1A13E373-2BFD-4D14-963C-A810BE5D2A77=3=en=.md)step. Also, you can use this step to create a metadata template for multiple data files or to create a data model for a relational database. See [Copybook steps in PDI](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/copybook-steps-in-pdi-cp) for more information.

This step is required to use metadata injection with the Copybook Input step.
