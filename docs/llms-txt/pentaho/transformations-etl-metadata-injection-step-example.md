# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/example-etl-metadata-injection-step/transformations-etl-metadata-injection-step-example.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/example-etl-metadata-injection-step/transformations-etl-metadata-injection-step-example.md

# Transformations

Metadata injection involves a main repetitive process. For this example, the `03_process_supplier_file` transformation in the `metadata-injection-example/transformation` folder is the template transformation, which is applied to each supplier’s file. The `02_process_supplier` transformation, which contains the ETL Metadata Injection step, injects metadata into the repetitive template transformation (`03_process_supplier_file`). Since this example pertains to the insertion of data from multiple files, the `02_process_supplier` transformation is called from another transformation (`01_process_all_suppliers`) per each supplier file.

This example contains the following three transformations:

* **Transformation for all input sources (`01_process_all_suppliers`)**

  The transformation going through all the suppliers’ spreadsheets, calling the metadata injection transformation per each supplier, and logging the entire process (for possible troubleshooting, if needed). Each input source is specified through a variable in a Transformation Executor step, which calls the `02_process_supplier` transformation.
* **Metadata injection transformation (`02_process_supplier`)**

  The transformation defining the structure of the metadata and how it is injected into the main transformation. For this example, the metadata values are in separate spreadsheet files. This transformation extracts these values, prepares them for the injection, and then inserts them into the template transformation through the ETL Metadata Injection step.
* **Template transformation (`03_process_supplier_file`)**

  The main repetitive transformation for processing the data per each supplier’s spreadsheet. The settings for each step in this transformation pertain to metadata injection, instead of data values of a single specific source. For example, the **supplier** field is a variable that depends on which supplier’s data is being accessed at that time.
