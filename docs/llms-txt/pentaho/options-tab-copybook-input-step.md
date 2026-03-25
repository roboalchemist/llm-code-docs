# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step/options-copybook-input-step/options-tab-copybook-input-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step/options-copybook-input-step/options-tab-copybook-input-step.md

# Options tab

![Options tab, Copybook Input step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e147d4d8d24ecfa0ac5551551640e52e6641499a%2FPDI_CopybookInput_OptionsTab.png?alt=media)

Use this tab to define PDI output stream options.

## **Output record information**

Use this section to specify details about the records for output.

| Option                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Store record as a binary field**    | Specify an additional output field to contain the binary bytes that make up the record currently being processed. You can use the stored binary field as the input for the data fields downstream from the Copybook Input step.                                                                                                                                                                                                                                                                                                                                                                                            |
| **Create field with record number**   | Specify an additional output field to contain the record number within the file. For fixed-length record definitions, multiplying this number by the fixed record size yields the offset of the record within the input file. This field will reset to zero when a new data file is read. Also, the counter is specific to a copy of the step, so changes to the [**Change Number of Copies to Start**](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/use-the-transformation-menu) option may cause unexpected results. |
| **Create field with record checksum** | Specify an additional output field to contain a hex string representation of the `sha1` checksum of the source record byte data.**Note:** This option is useful for debugging conversion errors, but it could be resource intensive.                                                                                                                                                                                                                                                                                                                                                                                       |

\## \*\*Conversion errors\*\*

Use this section to specify how to handle errors during conversion.

* **Ignore conversion errors**

  Select this check box to log multiple conversion error messages such as malformed records, bad enclosure strings, wrong number of fields, and premature line ends. The errors are logged in JSON object format in a single PDI row. See [Use Error Handling](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step/use-error-handling-copybook-input-step) for details about the format.

  Clear this check box if you want conversion errors in the source binary files to stop the transformation.
