# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/add-sequence-step-article/database-generated-sequence-add-sequence-step.md

# Database generated sequence

![Add sequence step](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-f31544fdf672c241aa6a871039071a0b60983785%2FssPDIAddSequencePropertiesDialogBox.png?alt=media)

The following table contains options for generating a sequence from a database:

| Option                               | Description                                                                                                                                                                                                                                                                         |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Use DB to generate the sequence?** | <p>Select this check box if you want the sequence to be driven by a database sequence.</p><p><strong>Use counter to calculate sequence?</strong> is automatically selected if this check box is cleared. <strong>Use counter to calculate sequence?</strong> is set by default.</p> |
| **Connection**                       | Select the connection to where your database sequence resides. If you do not have an existing connection, click either **New** or **Wizard**. If you need to modify an existing connection, click **Edit**.                                                                         |
| **Schema name** (optional)           | Specify the schema name of any related table. Click **Schemas** to select a schema within the database you specified for **Connection**.                                                                                                                                            |
| **Sequence name**                    | Specify the name of the database sequence. Click **Sequences** to select a sequence within the database you specified for **Connection**.                                                                                                                                           |
