# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp/select-an-engine-text-file-input/using-text-file-input-on-pentaho-engine-cp/options-text-file-input-reuse/file-tab-text-file-input-pentaho-engine/accept-file-names-text-file-input-kettle.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp/options-text-file-input-reuse/file-tab-text-file-input-pentaho-engine/accept-file-names-text-file-input-kettle.md

# Accept file names

![Accept filenames from previous steps](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-767ef055768d17a4b212fb2240d921dbb6b4bc32%2FPDI_TextFileInput_Dialog_AcceptFilenamesFromPreviousStep.png?alt=media)

You can specify your file name and pass it to the input step, which allows the file name to come from any source, such as a text file or database table.

| Option                                     | Description                                                                        |
| ------------------------------------------ | ---------------------------------------------------------------------------------- |
| **Accept filenames from previous step**    | Select to get file names from previous steps.                                      |
| **Pass through fields from previous step** | Select to get field information from previous steps.                               |
| **Step to read file names from**           | Enter the name of the step from which to read the file names.                      |
| **Field in the input to use as filename**  | Enter the name of the field in the input step to determine which file name to use. |
