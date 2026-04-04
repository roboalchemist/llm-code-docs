# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/discover-metadata-from-a-text-file/options-discover-metadata-from-a-text-file-step/enclosure-candidates-tab.md

# Enclosure candidates tab

![Discover metadata from a text file Enclosure candidates tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a98d74f09bf4eef08d3773b505c616f3bf25edbf%2FPDI_Discover%20metadata%20from%20a%20text%20file%20Enclosure%20candidates%20tab.png?alt=media)

You can enter characters you want to use for enclosures on the **Enclosure candidates** tab. The available options are listed in the following table:

| Option                           | Description                                                                                                                                                                            |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enclosure character required** | Select to require that all fields must be enclosed with enclosure characters. When this field is not selected, enclosure characters are optional.                                      |
| **Ignore enclosure errors**      | Select to ignore enclosure errors when a row is parsed that contains a different number of fields. Clear the option to generate enclosure errors which stops the step from continuing. |
| **Enclosure candidates**         | Enter the enclosure characters you want to use for the file scanning. Enclosure candidates can be one or more characters.                                                              |
