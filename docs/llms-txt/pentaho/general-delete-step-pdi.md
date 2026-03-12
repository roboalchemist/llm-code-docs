# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/delete-step-pdi/general-delete-step-pdi.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/delete-step-pdi/general-delete-step-pdi.md

# General

![Delete step dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f55328df41e218c29c4cc11d8e0356b30e05793b%2FPDI_DeleteStep_Dialog.png?alt=media)

The following table describes the general options for the **Delete** step.

| Option            | Description                                                                                                                                                                                                                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Step name**     | Specifies the unique name of the **Delete** step on the canvas. You can customize the name or leave it as the default.                                                                                                                                                                                                                                        |
| **Connection**    | <p>Select the name of a connected database from the drop-down list. Alternately, you can: - Click <strong>Edit</strong> to revise your current database connection.</p><ul><li>Click <strong>New</strong> to establish a new database connection.</li><li>Click <strong>Wizard</strong> to open a new database connection using the Wizard.</li></ul>         |
| **Target schema** | Specify the schema of the table to load from your database.                                                                                                                                                                                                                                                                                                   |
| **Target table**  | Specify the name of the table in your database where you want to delete the data.                                                                                                                                                                                                                                                                             |
| **Commit size**   | <p>Specify the size of the commit batch. The size is the number of <code>DELETE</code> statements to perform before sending a <code>COMMIT</code> command to the database. Depending on your connected database, commit sizes can affect step performance. If blank or set to <code>0</code>, the database determines the size.</p><p>The default is 100.</p> |
