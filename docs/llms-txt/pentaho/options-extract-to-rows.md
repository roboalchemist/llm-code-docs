# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/extract-to-rows/options-extract-to-rows.md

# Options

The Extract to rows step has the following options:

![Extract to rows step dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-9445f148e30e322aece7525c43b33271281bdd52%2FPDI%20Extract%20to%20rows%20step.png?alt=media)

| Option                    | Description                                                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Step name                 | Specifies the unique name of the Extract to rows step on the canvas. You can customize the name or leave it as the default. |
| Source hierarchical field | Specifies the hierarchical input field name from the previous step, which will be used to extract the data.                 |
| Pass through fields       | Select to add the input fields to the output fields.                                                                        |

\## Fields

| Field                  | Description                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| Hierarchical data path | Complete path of the field name in the hierarchical field source.                        |
| Output field name      | Name of the field that maps to the corresponding field in the hierarchical input source. |
| Type                   | Data type of the generated output field.                                                 |
| Path field name        | (Optional) Adds the hierarchical path as a new output field with the specified name.     |
