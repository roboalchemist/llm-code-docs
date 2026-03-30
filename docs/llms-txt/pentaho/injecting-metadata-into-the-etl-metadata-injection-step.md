# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/options-etl-metadata-injection/inject-metadata-tab/injecting-metadata-into-the-etl-metadata-injection-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/options-etl-metadata-injection/inject-metadata-tab/injecting-metadata-into-the-etl-metadata-injection-step.md

# Injecting metadata into the ETL Metadata Injection step

For injecting metadata into the ETL Metadata Injection step itself, the following exceptions apply:

* To inject a method for how to specify a field (such as by FILENAME, REPOSITORY\_BY\_NAME, or REPOSITORY\_BY\_REFERENCE), set a TRANS\_SPECIFICATION\_METHOD constant to the field of an input step. You can then map the field as a source to the TRANS\_SPECIFICATION\_METHOD constant in the ETL Metadata Injection step.
* The target field for the ETL Metadata Injection step inserting the metadata into the original injection is defined by **\[GROUP NAME].\[FIELD NAME]**. For example, if the **GROUP NAME** is 'OUTPUT\_FIELDS' and the **FIELD NAME** is 'OUTPUT\_FIELDNAME', you would set the target field to 'OUTPUT\_FIELDS.OUTPUT\_FIELDNAME'.
