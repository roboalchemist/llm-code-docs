# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/avro-output.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/avro-output.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/avro-output.md

# Avro Output

The Avro output step serializes data into an Avro binary or JSON format from the PDI data stream, then writes it to file. [Apache Avro](http://avro.apache.org/docs/current/index.html) is a data serialization system. Avro relies on schema for decoding binary and extracting data.

This output step creates the following files:

* A file containing output data in the Avro format
* An Avro schema file defined by the fields in this step

Fields can be defined manually or extracted from incoming steps.
