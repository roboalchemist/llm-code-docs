# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/generic-issue-import-format.md

# Generic formatted reports

If your third-party analyzer is not supported by SonarQube Server then you can import the reports by using the SonarQube Server generic issue format. No plugin is required.

The external issues will be taken into account by SonarQube Server in the analysis report, but the rules corresponding to these issues will not be visible on the **Rules** page nor reflected in quality profiles. This means that the rules that raise external issues must be managed in your third-party tool.

### Setting up the import <a href="#setting-up-import" id="setting-up-import"></a>

1. Set up the generation of the third-party reports in the generic issue format according to the specifications below.
2. Set up the import of the report files by defining the [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters "mention") `sonar.externalIssuesReportPaths` on the CI/CD host with the list of import directories or files. to define the list of report files to be imported during your project analysis. This parameter accepts a comma-delimited list of paths (A file path definition is either relative to the `sonar.projectBaseDir` property, which is by default the directory from which the analysis was started, or absolute.).

### Generic issue format specifications <a href="#generic-format-spec" id="generic-format-spec"></a>

The issues report must contain, an array of rule objects (`rules`) and an array of issue objects (`issues`).

{% hint style="info" %}
The generic issue format has changed with SonarQube Server 10.3. The previous format is deprecated. If you use it, SonarQube Server will apply the following default values:

* For the `cleanCodeAttribute` field: CONVENTIONAL
* For the `softwareQuality` field: MAINTAINABILITY
* For the `severity` field: MEDIUM

If you use SonarQube Server 10.8 or. later, you must use the latest generic issue format as outlined below. Otherwise, all issues will appear with Maintainability set to Medium in MQR Mode.

If you are switching between Standard Experience and MQR Mode, see [changing-modes](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/changing-modes "mention") for more information about how it might affect your metrics and workflow.
{% endhint %}

#### List of objects and properties in the report <a href="#list-of-objects-and-properties-in-the-report" id="list-of-objects-and-properties-in-the-report"></a>

The following objects and properties comprise the generic issues report.

**Rules object**

`rules` (array of rule objects)

**Objects and properties included in rules:**

`id` (string, required): Rule identifier

`name` (string, required): Rule name

`description` (string, required): Rule description

`engineId` (string, required): Identifier of the third-party analyzer that provides the rule.

`cleanCodeAttribute` (string, required): Coding attribute associated with the rule, possible values for:

* Consistency: FORMATTED, CONVENTIONAL, IDENTIFIABLE
* Intentionality: CLEAR, LOGICAL, COMPLETE, EFFICIENT
* Adaptibility: FOCUSED, DISTINCT, MODULAR, TESTED
* Responsibility: LAWFUL, TRUSTWORTHY, RESPECTFUL

`type` (string, optional if `impacts` is provided): Rule type, possible values: BUG, VULNERABILITY, CODE\_SMELL. We recommend incluing `type` if your instance is set to [Standard Experience mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience).

`severity` (string, optional if `impacts` is provided): Rule severity, possible values: BLOCKER, CRITICAL, MAJOR, MINOR, INFO. We recommend including `severity` if your instance is set to Standard Experience mode.

`impacts` (array of impact objects, optional if `type` and `severity` are provided). We recommend including `impacts` if your instance is set to [MQR Mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode).

* `softwareQuality` (string)\
  Possible values: SECURITY, RELIABILITY, MAINTAINABILITY
* `severity` (string)\
  Possible values: BLOCKER, HIGH, MEDIUM, LOW, INFO

Example of a `rules` object containing one rule:

```json
"rules": [
    {
      "id": "rule1",
      "name": "Name of rule 1",
      "description": "Description of rule 1",
      "engineId": "third-party analyzer 1",
      "cleanCodeAttribute": "FORMATTED",
      "type": "CODE_SMELL",
      "severity": "CRITICAL",
      "impacts": [
        {
          "softwareQuality": "MAINTAINABILITY",
          "severity": "HIGH"
        },
        {
          "softwareQuality": "SECURITY",
          "severity": "LOW"
        }
      ]
    }
  ]
```

**Issues object**

`issues` (array of issue objects)

**Objects and properties included in issues:**

`ruleID` (string, required): Identifier of the rule that raised the issue.

`effortMinutes` (integer): Effort in minutes to solve the issue. The default value is 0.

`primaryLocation` (object, required): Primary location of the issue in code.

* `message` (string, required): Description of the issue.
* `filePath` (string, required): Path to the code file that raised the issue.
* `textRange` (object): Object used to locate the code that raised the issue.
  * `startLine` (integer, required): Start line of the code that raised the issue.
  * `endLine` (integer): End line of the code that raised the issue.
  * `startColumn` (integer): Start column of the code that raised the issue. **Do not specify** for empty lines.
  * `endColumn` (integer): End column of the code that raised the issue.

`secondaryLocations` (array of locations): Secondary locations of the issue if there are several places of concern in the code. See `primaryLocation` on how to structure the location object.

Example of an `issues` object containing one issue:

```json
"issues": [
    {
      "ruleId": "rule1",
      "effortMinutes": 40,
      "primaryLocation": {
        "message": "fix issue 1",
        "filePath": "file1.js",
        "textRange": {
          "startLine": 1,
          "startColumn": 2,
          "endLine": 3,
          "endColumn": 4
        }
      },
      "secondaryLocations": [
        {
          "message": "fix issue 2",
          "filePath": "file2.js",
          "textRange": {
            "startLine": 1
          }
        },
        {
          "message": "fix issue 3",
          "filePath": "file3.js",
          "textRange": {
            "startLine": 2
          }
        }
      ]
    }
  ]
```

#### Report file example <a href="#report-file-example" id="report-file-example"></a>

```json
{
  "rules": [
    {
      "id": "rule1",
      "name": "Name of rule 1",
      "description": "Description of rule 1",
      "engineId": "third-party analyzer 1",
      "cleanCodeAttribute": "FORMATTED",
      "type": "CODE_SMELL",
      "severity": "CRITICAL",
      "impacts": [
        {
          "softwareQuality": "MAINTAINABILITY",
          "severity": "HIGH"
        },
        {
          "softwareQuality": "SECURITY",
          "severity": "LOW"
        }
      ]
    },
    {
      "id": "rule2",
      "name": "Name of rule 2",
      "description": "Description of rule 2",
      "engineId": "third-party analyzer 2",
      "cleanCodeAttribute": "IDENTIFIABLE",
      "type": "BUG",
      "severity": "MINOR",
      "impacts": [
        {
          "softwareQuality": "RELIABILITY",
          "severity": "LOW"
        }
      ]
    }
  ],
  "issues": [
    {
      "ruleId": "rule1",
      "effortMinutes": 40,
      "primaryLocation": {
        "message": "fix issue 1",
        "filePath": "file1.js",
        "textRange": {
          "startLine": 1,
          "startColumn": 2,
          "endLine": 3,
          "endColumn": 4
        }
      },
      "secondaryLocations": [
        {
          "message": "fix issue 2",
          "filePath": "file2.js",
          "textRange": {
            "startLine": 1
          }
        },
        {
          "message": "fix issue 3",
          "filePath": "file3.js",
          "textRange": {
            "startLine": 2
          }
        }
      ]
    },
    {
      "ruleId": "rule2",
      "primaryLocation": {
        "message": "fix issue 4",
        "filePath": "file4.js",
        "textRange": {
          "startLine": 3
        }
      }
    }
  ]
}
```

### Related pages

[about-external-issues](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/about-external-issues "mention")

[external-analyzer-reports](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/external-analyzer-reports "mention")

[importing-issues-from-sarif-reports](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports "mention")
