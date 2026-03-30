# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/select-an-engine-hadoop-file-input/using-the-hadoop-file-input-step-on-the-pentaho-engine-cp/options-hadoop-file-input-reuse/file-tab-hadoop-file-input-kettle/accepting-file-names-from-a-previous-step-kettle.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/options-hadoop-file-input-reuse/file-tab-hadoop-file-input-kettle/accepting-file-names-from-a-previous-step-kettle.md

# Accepting file names from a previous step

![Accept filenames from previous steps](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-36096b22b29373d09447e5ff47fdea86c80b2314%2FPDITransStep_HadoopFileInput_FileTab_AcceptFilenamesSection.png?alt=media)

The **Accept filenames from previous steps** section in the **File** tab provides flexibility in combination with other steps, such as Get File Names. You can specify your file name and pass it to this step. Using this method, the file name can come from any source, such as a text file or database table.

| Option                                     | Description                                                              |
| ------------------------------------------ | ------------------------------------------------------------------------ |
| **Accept file names from previous steps**  | Select the check box to get file names from previous steps.              |
| **Pass through fields from previous step** | Select the check box to get field information from previous steps.       |
| **Step to read file names from**           | Enter the name of the step from which to read the file names.            |
| **Field in the input to use as file name** | Text File Input looks in this step to determine which file names to use. |
