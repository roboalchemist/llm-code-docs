# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/copybook-steps-in-pdi-cp.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/copybook-steps-in-pdi-cp.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/copybook-steps-in-pdi-cp.md

# Copybook steps in PDI

Pentaho Data Integration supports simplified integration with fixed-length records in binary mainframe data files, so more users can ingest, integrate, and blend mainframe data as part of their data integration pipelines. This capability is critical if your business relies on massive amounts of customer and transactional datasets generated in mainframes that you want to search and query to create reports.

Mainframe file records are typically defined by a COBOL copybook. A COBOL copybook is a selection of code that defines the data layout of items from a data source, including records, segments, fields, and keys. Copybooks allow developers to reuse data structures in multiple instances.

Copybook data is usually extracted from the mainframes in a block of records and then stored in binary files, along with a definition file, that can be read by PDI. Based on the definition file, the Copybook input step and the Read metadata from Copybook step read the binary content in the data files and convert it to PDI rows which makes the data easy to integrate into your transformations.

These steps navigate you through challenging conversion issues, such as packed decimal numbers and multibyte data type storage, which are typical of COBOL copybooks. The steps can also handle REDEFINES clauses, which change some of the fields in a record based on other values in the record.
