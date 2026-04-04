# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hierarchical-json-output/fields-hierarchical-json-output.md

# Fields

![Hierarchical JSON Output step dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a8f57b4ebc1af678856fe68b91352b92f708e85a%2FPDI%20Hierarchical%20JSON%20Output%20step.png?alt=media)

| Field                        | Description                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Input hierarchical field** | Specifies the hierarchical input field name from a previous step which is formatted to the JSON format. |
| **Output field**             | Specifies the step output field to contain the generated JSON output.                                   |

\## Options

| Option                     | Description                                                                                                                                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pass output to servlet** | Select to return the data using a web service instead of passing it to output rows. See [PDI data over web service](https://pentaho-public.atlassian.net/wiki/spaces/EAI/pages/384958757/PDI+data+over+web+services) |
| **Pretty print?**          | Select to format the output JSON data.                                                                                                                                                                               |
