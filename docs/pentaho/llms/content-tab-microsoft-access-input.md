# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/microsoft-access-input/options-microsoft-access-input/content-tab-microsoft-access-input.md

# Content tab

Use the **Content** tab to control the output filename.

![Microsoft Access input step Content tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e0a41b96ef5f3b428e013fadbd10469d4af407d2%2FPDI%20Microsoft%20Access%20input%20step%20Content%20tab.png?alt=media)

| Option                            | Description                                                                                                                                                                                                        |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Table**                         | Specify the name of the Access table from which you want to read data. Click **Get tables** to query the database for the list of table names.                                                                     |
| **Include filename in output?**   | Select the checkbox and specify a field name to include the file name (string) in the output of the Microsoft Access input step.                                                                                   |
| **Include table name in output?** | Select the checkbox and specify a field name to include the table name (string) in the output of the Microsoft Access input step.                                                                                  |
| **Include rownum in output?**     | Select the checkbox and specify a field name to include the row number (Integer) in the output of the Microsoft Access input step.                                                                                 |
| **Reset rownum per file?**        | Select the checkbox to set the row number to 1 in each file that is being read.                                                                                                                                    |
| **Limit**                         | Specify an integer larger than zero to limit the number of rows read by the Microsoft Access input step.                                                                                                           |
| **Add filename to result?**       | Select the checkbox to add the Access filenames read to the result of this transformation. A unique list is kept in memory that can be used in the next job entry in a job, for example in another transformation. |
