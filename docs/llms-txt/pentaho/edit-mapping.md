# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/select-values/options-select-values/edit-mapping.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/select-values/options-select-values/edit-mapping.md

# Edit Mapping

Use the Edit Mapping dialog box to easily define multiple mappings between source and target fields.

**Note:** Edit Mapping must have only one target output step.

![Edit Mapping](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-c5510d65fb5ed6b5d2dea2ab1721fde8b92c880d%2FPDI_TableOutput_EnterMapping_Window.png?alt=media)

The Edit Mapping dialog box contains the following options:

| Option                           | Description                                                                                                                         |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Source fields**                | Select to highlight the fields from the incoming stream you want to map.                                                            |
| **Target fields**                | Select to highlight the fields in the output table you want to map.                                                                 |
| **Add** (Button)                 | Click **Add** to move a selected combination of a field name and a column name to the **Mappings** pane.                            |
| **Delete** (Button)              | Click **Delete** to move a mapped combination from the **Mappings** pane back to the **Source fields** and **Target fields** panes. |
| **Mappings**                     | The field to column mapping designating the incoming field and the table column where the field will be assigned.                   |
| **Auto target selection?**       | Select to have the step perform mapping to a target.                                                                                |
| **Hide assigned source fields?** | Select to remove a field from the **Source fields** pane when it has been matched and moved to the **Mappings** pane.               |
| **Auto source selection**        | Select to automatically select a field from the **Source fields** pane when a column name is selected.                              |
| **Hide assigned target fields?** | Select to remove a field from the **Target fields** pane when it has been matched and moved to the **Mappings** pane.               |
| **Guess** (Button)               | Click **Guess** to perform automatic matching of all fields and population of the **Mappings** pane.                                |

Your mapping results display in the **Mappings** panel.
