# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-bulk-operation/options-salesforce-bulk-operation/advanced-tab-salesforce-bulk-operation.md

# Advanced tab

Use this tab to specify buffer file options and the API version.

![PDI Salesforce bulk operation step Advanced tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-df095ac1e8047d1084ae6ddc2c71f66db9516723%2FPDI%20Salesforce%20bulk%20operation%20step%20Advanced%20tab.png?alt=media)

| Field                                                  | Description                                                                                                                                                                                                |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Path to buffer the bulk job payloads**               | Specify the directory to store the temporary files. This location is also used to retrieve output records. The temporary files are automatically deleted when the step finishes.                           |
| **Maximum size of a buffered payload file (in bytes)** | Specify the maximum number of bytes to buffer and transmit in a bulk operation job. The maximum is the default 100 MB (104,857,600 bytes). If needed, you can lower this number to prevent locking errors. |
| **Buffer payload only (do not upload in job)**         | Add files to the directory specified in the **Path to buffer the bulk job payloads** field, but do not upload them to Salesforce.                                                                          |
| **Cleanup bulk jobs once processed**                   | Select to delete the buffer files when the step finishes.                                                                                                                                                  |
| **Salesforce API version**                             | Specify the Salesforce Bulk API version for your connection.                                                                                                                                               |

**Note:** :To view sample transformations in the PDI client, navigate to the `/design-tools/data-integration/plugins/pdi-salesforce-bulk-plugin/samples` directory and open any of the following files:

* `Input SFBL.ktr`
* `Delete SFBL.ktr`
* `Update SFBL.ktr`
* `Upsert SFBL.ktr`
