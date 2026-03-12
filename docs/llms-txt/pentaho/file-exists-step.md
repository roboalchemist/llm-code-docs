# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/file-exists-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/file-exists-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/file-exists-step.md

# File exists (Step)

The File exists step verifies the existence of a file by checking filenames coming from previous steps, and adds a Boolean flag field to the input fields of the output.

![File exists dialog](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a949e9aaae53078b0b3947a5648dd76d385f3d29%2FPDI_TransStep_File_exists%20.png?alt=media)

The following fields are available to this transformation step:

| Field                 | Description                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Step name**         | Specify the unique name of the File exists transformation step on the canvas. You can customize the name or leave it as the default. |
| **Filename field**    | Specify the input field that will contain the filename at runtime.                                                                   |
| **Result fieldname**  | Specify the name of the field that will contain the Boolean (Y/N) flag.                                                              |
| **Add filename to**   | Select to add the filename to the list of filenames that can be used in the next job entry.                                          |
| **Include file type** | Select to include the file type in the field.                                                                                        |
| **File type field**   | Specify the name of the field that contains the file type as a String (for example, `file`, `folder`, or `imaginary`).               |

**Note:** To view a sample transformation in the PDI client, open the `/design-tools/data-integration/samples/transformations/File exists – VFS example.ktr` sample file.
