# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/importing-issues-from-sarif-reports.md

# SARIF reports

You can import [Static Analysis Results Interchange Format (SARIF)](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html) reports into SonarQube Cloud. The issues will be taken into account by SonarQube Cloud in the analysis report, but the rules corresponding to these issues will not be visible on the Rules page nor reflected in quality profiles. This means that the rules that raise external issues must be managed in your third-party tool.

### Import process <a href="#import-process" id="import-process"></a>

SonarQube Cloud manages the import of a SARIF issue as follows:

* It assigns the `CONVENTIONAL` coding attribute and the `SECURITY` software quality to the issue.
* It maps the issue's severity level on the SECURITY software quality using the following fields:
  * `runs[].tool.extensions.rules[].defaultConfiguration.level` is overridden by
  * `runs[].tool.driver.rules[].defaultConfiguration.level`

| **Severity field in SARIF 2.1.0** | **Impact level in SonarQube Cloud** |
| --------------------------------- | ----------------------------------- |
| error                             | HIGH                                |
| warning                           | MEDIUM                              |
| note                              | LOW                                 |
| none                              | LOW                                 |

* Otherwise, the default MEDIUM impact level is applied.

See [software-qualities](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/software-qualities "mention") for more information.

### Setting up the import <a href="#setting-up" id="setting-up"></a>

To set up the import of SARIF reports into SonarQube Cloud:

1. Prepare your SARIF report files according to the import file specifications below.
2. Use on the scanner side the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") `sonar.sarifReportPaths` to define the list of SARIF report files to be imported during your project analysis. This parameter accepts a comma-delimited list of paths.

### Import file specifications <a href="#import-file-specifications" id="import-file-specifications"></a>

The SARIF files must:

* Be UTF-8 file encoded.
* Comply with the [official SARIF format, version 2.1.0](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html).

#### Mandatory fields <a href="#mandatory-fields" id="mandatory-fields"></a>

| Field                           | Description                                                               |
| ------------------------------- | ------------------------------------------------------------------------- |
| `version`                       | Must be set to "2.1.0".                                                   |
| `runs[].tool.driver.name`       | Name of the tool that created the report.                                 |
| `runs[].results[].message.text` | Message of the external issue.                                            |
| `runs[].results[].ruleId`       | Identifier of the corresponding rule in the tool that created the report. |

{% hint style="info" %}
If a mandatory field is missing, the report is ignored (see the corresponding line in the logs).
{% endhint %}

#### Optional fields <a href="#optional-fields" id="optional-fields"></a>

| Field                            | Sub-field                               | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `runs[].tool.driver`             | <p><br></p>                             | The tool that generated the report.                                                                                                                                                                                                                                                                                                                                                                                      |
| `runs[].tool.driver.rules[]`     | `id`                                    | Identifier of the rule of the tool that created the report.                                                                                                                                                                                                                                                                                                                                                              |
| <p><br></p>                      | `shortDescription.text`                 | Short description is mapped as the name of the rule in SonarQube. If the field is empty, SonarQube constructs the name based on the driver `name` and `id` fields.                                                                                                                                                                                                                                                       |
| <p><br></p>                      | `fullDescription.text`                  | Full description of the rule.                                                                                                                                                                                                                                                                                                                                                                                            |
| <p><br></p>                      | `defaultConfiguration.level`            | SonarQube uses this field to determine the issue's impact level on security software quality.                                                                                                                                                                                                                                                                                                                            |
| `runs[].tool.extensions.rules[]` | `defaultConfiguration.level`            | SonarQube uses this field to determine the issue's impact level on security software quality, if the driver field `runs[].tool.driver.rules[].defaultConfiguration.level` above is not used.                                                                                                                                                                                                                             |
| `runs[].results[]`               | `level`                                 | Ignored by SonarQube Cloud.                                                                                                                                                                                                                                                                                                                                                                                              |
| <p><br></p>                      | `stacks[]`                              | The stacks are mapped to the issue flows.                                                                                                                                                                                                                                                                                                                                                                                |
| <p><br></p>                      | `stacks[].frames[]`                     | Each frame of a stack represents one path of the whole issue flow.                                                                                                                                                                                                                                                                                                                                                       |
| <p><br></p>                      | `stack.frames.location`                 | Follows the same pattern as in locations indicated below.                                                                                                                                                                                                                                                                                                                                                                |
| `runs[].results[].locations[]`   | <p><br></p>                             | SonarQube only uses the first item in the array. It must be a physical location.                                                                                                                                                                                                                                                                                                                                         |
| <p><br></p>                      | `physicalLocation.artifactLocation.uri` | <p>Path of the file concerned by the issue.</p><p>If no location is defined, the issue is raised at the project level.</p>                                                                                                                                                                                                                                                                                               |
| <p><br></p>                      | `physicalLocation.region`               | <p>Text range concerned by the issue. Is defined by the following fields:</p><ul><li><code>startLine</code></li><li><code>startColumn</code>(optional)</li><li><code>endLine</code> (optional)</li><li><code>endColumn</code> (optional)</li></ul><p>If <code>startColumn</code>, <code>endLine</code>, <code>endColumn</code> are not specified,SonarQube automatically retrieves the full coordinates of the line.</p> |
| <p><br></p>                      | `relatedLocations`                      | Contains the same fields as `physicalLocation`.                                                                                                                                                                                                                                                                                                                                                                          |

{% hint style="warning" %}
The `runs[].results[].level`field which defines the issue's severity will be ignored by SonarQube Cloud.
{% endhint %}

#### Import file example <a href="#import-file-example" id="import-file-example"></a>

```json
{
  "version": "2.1.0",
  "$schema": "http://json.schemastore.org/sarif-2.1.0-rtm.5",
  "runs": [
    {
      "tool": {
        "driver": {
          "name": "a test linter",
          "rules": [
            {
              "id": "rule1",
              "shortDescription": {
                "text": "XooLint rule 1"
              },
              "fullDescription": {
                "text": "XooLint rule 1 full description"
              }
            },
            {
              "id": "rule2",
              "shortDescription": {
                "text": "XooLint rule 2"
              }
            }
          ]
        }
      },
      "results": [
        {
          "level": "error",
          "message": {
            "text": "'toto' is assigned a value but never used."
          },
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": {
                  "uri": "src/File0.xoo"
                },
                "region": {
                  "startLine": 1,
                  "startColumn": 5,
                  "endLine": 1,
                  "endColumn": 9
                }
              }
            }
          ],
          "relatedLocations": [
            {
              "message": {
                "text": "Secondary location message."
              },
              "physicalLocation": {
                "artifactLocation": {
                  "uri": "src/File0.xoo"
                },
                "region": {
                  "startLine": 2,
                  "startColumn": 1
                }
              }
            }
          ],
          "ruleId": "rule1"
        },
        {
          "level": "error",
          "message": {
            "text": "Issue with flow"
          },
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": {
                  "uri": "src/File1.xoo"
                },
                "region": {
                  "startLine": 1,
                  "startColumn": 5,
                  "endLine": 1,
                  "endColumn": 9
                }
              }
            }
          ],
          "stacks": [
            {
              "frames": [
                {
                  "location": {
                    "message": {
                      "text": "Stack frame message."
                    },
                    "physicalLocation": {
                      "artifactLocation": {
                        "uri": "src/File1.xoo"
                      },
                      "region": {
                        "startLine": 3,
                        "startColumn": 1
                      }
                    }
                  }
                },
                {
                  "location": {
                    "message": {
                      "text": "Stack frame message 2."
                    },
                    "physicalLocation": {
                      "artifactLocation": {
                        "uri": "src/File1.xoo"
                      },
                      "region": {
                        "startLine": 4,
                        "startColumn": 1
                      }
                    }
                  }
                }
              ]
            }
          ],
          "ruleId": "rule2"
        }
      ]
    }
  ]
}
```
