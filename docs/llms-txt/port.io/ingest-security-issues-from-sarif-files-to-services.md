# Source: https://docs.port.io/guides/all/ingest-security-issues-from-sarif-files-to-services.md

# Ingest security issues from `.sarif` files and relate them to services

This guide will demonstrate how to ingest security issues from `.sarif` files and relate them to the corresponding service entities in Port.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Ensure you have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* The `Service` blueprint should be created during the onboarding process.
* Ensure you have [GitHub](/build-your-software-catalog/sync-data-to-catalog/git/github/.md#setup) or [Gitlab](/build-your-software-catalog/sync-data-to-catalog/git/gitlab/installation.md) installed and configured in your environment.

<br />

## Data model setup[â](#data-model-setup "Direct link to Data model setup")

### Add blueprint[â](#add-blueprint "Direct link to Add blueprint")

Add the `Security Issue` blueprint:

1. **Go to the [Builder](https://app.getport.io/settings/data-model)** in your Port portal.
2. **Click on "+ Blueprint"**.
3. **Click on the `{...}` button** in the top right corner, and choose "Edit JSON".
4. **Add this JSON schema**:

**Security Issue Blueprint (Click to expand)**

Create in Port

```
{
  "identifier": "security_issue",
  "description": "A security issue parsed from SARIF format",
  "title": "Security Issue",
  "icon": "Alert",
  "schema": {
    "properties": {
      "rule_name": {
        "type": "string",
        "title": "Rule Name"
      },
      "rule_desc": {
        "type": "string",
        "title": "Rule Description"
      },
      "location": {
        "type": "string",
        "title": "Location"
      },
      "message": {
        "type": "string",
        "title": "Message"
      },
      "title": {
        "type": "string",
        "title": "Title"
      },
      "ai_summary": {
        "type": "string",
        "title": "ai_summary",
        "format": "markdown"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "issue_service": {
      "title": "issue service",
      "description": "The service this issue was found in",
      "target": "service",
      "required": false,
      "many": false
    }
  }
}
```

<br />

### Ingest Security Issues from `.sarif` files[â](#ingest-security-issues-from-sarif-files "Direct link to ingest-security-issues-from-sarif-files")

To ingest security issues listed in `.sarif` files, follow these steps:

1. **Go to the [data sources page](https://app.getport.io/settings/data-sources)** in your Port portal, and select your GitHub/Gitlab integration.
2. **Modify the mapping** to include the `file` kind with the configuration provided below:

**Port Configuration (Click to expand)**

```
- kind: file
    selector:
      query: 'true'
      files:
        - path: '**/*.sarif'
    port:
      itemsToParse: |
        .file.content.runs[0] as $content |
        $content.tool.driver.rules as $rules |
        [ $content.results[] ] |
        map(
          . as $result |
          {
          ruleId: .ruleId,
          error: .message.text,
          loc: .locations[0].physicalLocation.artifactLocation.uri,
          ruleName: ($rules[] | select(.id == $result.ruleId) | .name),
          ruleDesc: ($rules[] | select(.id == $result.ruleId) | .shortDescription.text)
          })
      entity:
        mappings:
          identifier: .repo.name + "_" + .item.ruleId
          title: .item.error
          blueprint: '"security_issue"'
          properties:
            rule_name: .item.ruleName
            rule_desc: .item.ruleDesc
            location: .item.loc
            message: .item.error
          relations:
            issue_service: .repo.name
```

### Configuration details[â](#configuration-details "Direct link to Configuration details")

* **`kind: file`** specifies that the source is a file, in this case, `.sarif` files.
* **`files:`** defines the path pattern to locate `.sarif` files within your repositories.
* **`itemsToParse:`** processes the `.sarif` file content to extract security issues.
* **`identifier:`** constructs a unique identifier for each security issue by combining the repository name and the rule ID.
* **`properties:`** captures essential details like rule name, description, location, and message.
* **`relations:`** establishes a relation between the security issue and the corresponding service.

<br />

## Example

Once you have configured the data source and mappings, the extracted security issues will appear in the Port UI with properties like rule name, description, location, and message. Hereâs an example SARIF file structure that you can copy and replicate for testing purposes:

![](/img/guides/exampleExtractedIssues.png)

**Example SARIF File (Click to expand)**

```
{
  "version": "2.1.0",
  "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json",
  "runs": [
    {
      "tool": {
        "driver": {
          "name": "CustomSecurityTool",
          "rules": [
            {
              "id": "CS0001",
              "name": "HardcodedPassword",
              "shortDescription": {
                "text": "Hardcoded password detected."
              }
            },
            {
              "id": "CS0002",
              "name": "SQLInjection",
              "shortDescription": {
                "text": "Possible SQL injection vulnerability."
              }
            }
          ]
        }
      },
      "results": [
        {
          "ruleId": "CS0001",
          "message": {
            "text": "A hardcoded password was found in the source code."
          },
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": {
                  "uri": "src/app/login.js"
                },
                "region": {
                  "startLine": 42,
                  "startColumn": 13
                }
              }
            }
          ]
        },
        {
          "ruleId": "CS0002",
          "message": {
            "text": "User input is directly concatenated into a SQL query."
          },
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": {
                  "uri": "src/app/database.js"
                },
                "region": {
                  "startLine": 88,
                  "startColumn": 22
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

![](/img/guides/exampleSingleExtractedIssues.png)

<br />

<br />

File format

The `.sarif` format is a standardized structure for reporting static analysis results. This guide relies on that standard format, but additional fields can be extracted or modified. For example:

* The `location` field is an array in SARIF and can be treated as relations to specific components if needed.
* The mapping configuration can be customized to accommodate new properties, making this approach flexible for various use cases.

By following these steps, you can effectively ingest security issues from `.sarif` files and relate them to the corresponding service entities in Port ð.
