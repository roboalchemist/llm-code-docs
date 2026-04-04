# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/orc-output.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/orc-output.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/orc-output.md

# ORC Output

The ORC Output step serializes data from the PDI data stream into an ORC file format, and then writes it to a file. [ORC](https://orc.apache.org/) is a data format for fast columnar storage. This step creates a file containing output data in the ORC format.

Fields written to the ORC output file are defined by the input fields. Fields not written to the output file are either deleted, or are written to the output file with alternate field names or default values.
