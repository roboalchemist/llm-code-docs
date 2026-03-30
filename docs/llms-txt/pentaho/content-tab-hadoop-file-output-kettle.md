# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-output-cp-main-page/select-an-engine-hadoop-file-ouput/using-the-hadoop-file-output-step-on-the-pentaho-engine-cp/options-hadoop-file-output-reuse/content-tab-hadoop-file-output-kettle.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-output-cp-main-page/options-hadoop-file-output-reuse/content-tab-hadoop-file-output-kettle.md

# Content tab

![Content tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a9555856834c8bcd08a66f6c301c3758f4530bb8%2FPDITransStep_HadoopFileOutput_ContentTab.png?alt=media)

The **Content** tab contains the following options for describing the content written to the output text file:

| Option                                 | Description                                                                                                                                                                                                     |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Append**                             | Append lines to the end of the specified file.                                                                                                                                                                  |
| **Separator**                          | Specify the character that separates the fields in a single line of text. Typically, it is a semicolon (;) or a tab. Click **Insert TAB** to place a tab in the **Separator** field.                            |
| **Enclosure**                          | Enclose fields with a pair of specified strings. It allows for separator characters in fields. This setting is optional and can be left blank.                                                                  |
| **Force the enclosure around fields?** | Force all field names to be enclosed with the character specified in the **Enclosure** property.                                                                                                                |
| **Header**                             | Indicate if the output text file has a header row (first line in the file).                                                                                                                                     |
| **Footer**                             | Indicate if the output text file has a footer row (last line in the file).                                                                                                                                      |
| **Format**                             | Specify the type of formatting to use. It can be either DOS or UNIX. UNIX files have lines separated by line feeds, while DOS files have lines separated by carriage returns and line feeds.                    |
| **Compression**                        | Specify the type of compression (ZIP or GZIP) to use when compressing the output. Only one file is placed in a single archive.                                                                                  |
| **Encoding**                           | Specify the text file encoding to use. Leave blank to use the default encoding on your system. To use Unicode, specify **UTF-8** or **UTF-16**. On first use, PDI searches your system for available encodings. |
| **Right pad fields**                   | Add spaces to the end of the fields (or removes characters at the end) until the length specified in the table under the **Fields** tab is reached.                                                             |
| **Fast data dump (no formatting)**     | Improve the performance when dumping large amounts of data to a text file by not including any formatting information.                                                                                          |
| **Split every ... rows**               | If the number `N` is larger than zero, split the output text file into multiple parts of `N` rows.                                                                                                              |
| **Add Ending line of file**            | Specify an alternate ending row to the output file.                                                                                                                                                             |
