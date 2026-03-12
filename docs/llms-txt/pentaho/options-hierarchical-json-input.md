# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hierarchical-json-input/options-hierarchical-json-input.md

# Options

The Hierarchical JSON input step features several tabs with fields. Each tab is described below.

## Source tab

![Hierarchical JSON Input step dialog box showing source tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-79d31ff8747dcd5f1fd400c75909c0a4e7317c5c%2FPDI%20Heirachical%20JSON%20Input%20step%20dialog%20box.png?alt=media)

| Option/Field             | Description                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------ |
| **From file**            | Select to specify the file path and name of the JSON file you want to load into PDI. |
| **File name**            | File path and name of the JSON file to load.                                         |
| **From field**           | Select to use an incoming field as the JSON file path.                               |
| **Field with file name** | The incoming field containing the JSON file path.                                    |

\## Output tab

![Hierarchical JSON Input step Output tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e3c0356dad24612a1e7989c2427d55a768cd9b9b%2FPDI%20Hierarchical%20JSON%20Input%20output%20tab.png?alt=media)

| Field                      | Description                                                                                                                                                                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Output field**           | Specify the field name for output column.                                                                                                                                                                                                        |
| **Split rows across path** | Specify the JSON path to be parsed. See [Hierarchical data path specifications](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/hierarchical-data/hdt-path-specification) |

\*\*Note:\*\* The \*\*Split rows across path\*\* option is especially useful when loading JSON array objects within large JSON files.

## Filters tab

![Hierarchical JSON Input step filters tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b5a58aaf21362848dd2eef18cd04071580895aa9%2FPDI%20Hierarchical%20JSON%20Input%20filters%20tab.png?alt=media)

Use the **Path field**(Optional) to specify the filters to apply while using the **Split rows across path** option to fetch the subset of a JSON file. See [Hierarchical data path specifications](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/hierarchical-data/hdt-path-specification)
