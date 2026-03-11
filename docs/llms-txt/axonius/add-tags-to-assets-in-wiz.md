# Source: https://docs.axonius.com/docs/add-tags-to-assets-in-wiz.md

# Wiz - Add Tags to Assets

**Wiz - Add Tags to Assets** extracts tags from correlated assets within Axonius and adds them to the corresponding asset in Wiz, if it exists. The Axonius assets are assets that match the parameters of the selected query or that are selected on the relevant asset page.

For example, if a Wiz device correlates with a Tenable device, the tags on the Tenable device will be added to that device in Wiz.

The mechanism of this action is creating and sending a DAST/ASM security scan file to Wiz. Note that the processing of the file can take up to 12 hours on the Wiz end. Refer to Wiz's tutorial about External Enrichment for more information.

This enforcement action supports assets with a self-hosted cloud provider.

See an [example](#example-of-custom-tag-data) of the custom tags data and the [JSON schema](#custom-tag-json-schema) below.

### General Guidelines for Adding Tags

* It is recommended to keep a minimum of 24-hour gap between each run, as this aligns with Wiz's typical 24-hour environment scan cycle.
* Custom tags take up to 24 hours to appear on the asset.
* Tags are expired after 7 days. To ensure your tags are always up to date, run this action at least once a week.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

<Callout icon="📘" theme="info">
  Notes

  * This Enforcement Action works for all asset types except for Users.
  * To use this Enforcement Action, you must successfully configure the [Wiz](/docs/wiz) adapter.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Wiz adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the Select Adapter Connection drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Wiz](/docs/wiz) adapter connection.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  * If you are using the Wiz Axonius Integration service account for your adapter connection, enable **Use stored credentials from the Wiz adapter**, as the all the necessary permissions for adapter connection and actions are already set.

  * If you are using a custom Wiz service account for your adapter connection, migrate to using the [Wiz Axonius Integration service account](/docs/wiz#configuring-the-wiz-axonius-integration).
</Callout>

* **Fields to send as tags** - Use this option to select specific fields from the asset data and convert them into tags that will be sent to Wiz. This is useful when you want to send information that is not a standard adapter tag, such as hostname, OS type, IP, cloud account ID, etc.
  Click **+ Add adapter to choose from** to open the selection module.\
  Each selected field is converted into a tag in the following format:
  * `key`: the field name
  * `value`: the field value (as a string)

    For example, if you select the `Hostname` field, it will be converted into the following tag:

    * `key = "hostname"`
    * `value = "ip-...internal"` (the value of the asset field)
* **Tags to include** - Use this option to filter which adapter tags will be sent to Wiz. Enter a list of comma-separated tags to send. Only tags whose `tag_key` or `tag value` format is in that list will be sent.
  If the field is empty, all adapter tags from other adapter connections that are related to the asset (non-Wiz) will be sent.
  * For example: If the asset has the following adapter tags: `Name=selenium-staging`, `Environment=prod`, `Owner=devops`
  * ...and you populate **Tags to include** with: `Name`, `Environment` ; then only these tags are sent: `Name=selenium-staging`, `Environment=prod`

<Callout icon="📘" theme="info">
  **Note**

  * The recommended tag update frequency is 24 hours.
  * It might take up to 24 hours for custom tags to appear after upload.
  * Tags must be refreshed every 7 days to remain in Wiz.
  * Wiz automatically adds a `custom/ prefix`. Example: `Key: "Foo", Value: "Boo"` → `custom/Foo:Boo`
</Callout>

## Required Permissions

* Use the [Wiz Axonius Integration](/docs/wiz#configuring-the-wiz-axonius-integration) which has the necessary permissions.

## Required Ports

* **TCP port 443**

## APIs

Axonius uses the [wiz.io API](https://app.wiz.io/login?redirect=%2Fwiz-docs).

## Example of Custom Tag Data

Below is a sample of the custom tags data:

```json
{
  "integrationId": "000c0c7b-5f59-46ea-a305-934a15b94930",
  "dataSources": [
    {
      "id": "29A4E640-4BFD-4779-856756756",
      "analysisDate": "2023-08-02T16:50:00Z",
      "assets": [
        {
          "assetIdentifier": {
            "cloudPlatform": "AWS",
            "providerId": "arn:aws:ec2:eu-central-1:9123455:instance/i-04ea5a462c85555"
          },
          "customTags": [
            {
              "key": "App",
              "value": "Spotify"
            },
            {
              "key": "Owner",
              "value": "Beyoncé"
            }
          ]
        }
      ]
    }
  ]
}
```

## Custom Tag JSON Schema

Below is the JSON schema of the custom tags data:

```json
{
  "$id": "https://wiz.io/ingestionmodel.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Wiz Ingestion Model",
  "type": "object",
  "properties": {
    "integrationId": {
      "type": "string"
    },
    "dataSources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/dataSource"
      }
    }
  },
  "required": [
    "integrationId",
    "dataSources"
  ],
  "additionalProperties": false,
  "$defs": {
    "cloudPlatform": {
      "enum": "{{.CloudPlatformEnum}}"
    },
    "status": {
      "enum": "{{.StatusEnum}"
    }
  },
  "severity": {
    "enum": "{{.SeverityEnum}}"
  },
  "eventSeverity": {
    "enum": "{{.EventSeverityEnum}}"
  },
  "detectionMethod": {
    "enum": "{{.DetectionMethodEnum}}"
  },
  "dataCategory": {
    "enum": "{{.DataCategoryEnum}}"
  },
  "dataClassifier": {
    "enum": "{{.DataClassifierEnum}}"
  },
  "mitreTacticId": {
    "enum": "{{.MitreTacticIdEnum}}"
  },
  "mitreTacticName": {
    "enum": "{{.MitreTacticNameEnum}}"
  },
  "mitreTechniqueId": {
    "enum": "{{.MitreTechniqueIdEnum}}"
  },
  "mitreTechniqueName": {
    "enum": "{{.MitreTechniqueNameEnum}}"
  },
  "dataSource": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "analysisDate": {
        "type": "string",
        "format": "date-time"
      },
      "assets": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/asset"
        }
      }
    },
    "required": [
      "id",
      "assets"
    ],
    "additionalProperties": false
  },
  "asset": {
    "type": "object",
    "properties": {
      "assetIdentifier": {
        "$ref": "#/$defs/assetIdentifier"
      },
      "cloudConfigurationFindings": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/cloudConfigFinding"
        }
      },
      "hostConfigurationFindings": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/hostConfigFinding"
        }
      },
      "vulnerabilityFindings": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/vulnerabilityFinding"
        }
      },
      "webAppVulnerabilityFindings": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/webAppVulnerabilityFinding"
        }
      },
      "dataFindings": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/dataFinding"
        }
      },
      "events": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/event"
        }
      },
      "customTags": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/keyValue"
        }
      }
    },
    "required": [
      "assetIdentifier"
    ],
    "additionalProperties": false
  },
  "assetIdentifier": {
    "type": "object",
    "properties": {
      "cloudPlatform": {
        "$ref": "#/$defs/cloudPlatform"
      },
      "providerId": {
        "type": "string"
      },
      "networkAddress": {
        "type": "string"
      },
      "endpointUrl": {
        "type": "string"
      }
    },
    "oneOf": [
      {
        "required": [
          "providerId"
        ]
      },
      {
        "required": [
          "networkAddress"
        ]
      },
      {
        "required": [
          "endpointUrl"
        ]
      }
    ],
    "required": [
      "cloudPlatform"
    ],
    "additionalProperties": false
  },
  "cloudConfigFinding": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "status": {
        "$ref": "#/$defs/status"
      },
      "severity": {
        "$ref": "#/$defs/severity"
      },
      "externalDetectionSource": {
        "$ref": "#/$defs/detectionMethod"
      },
      "detailedName": {
        "type": "string"
      },
      "version": {
        "type": "string"
      },
      "externalFindingLink": {
        "type": "string"
      },
      "source": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "remediation": {
        "type": "string"
      }
    },
    "required": [
      "name",
      "status"
    ],
    "additionalProperties": false
  },
  "hostConfigFinding": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "status": {
        "$ref": "#/$defs/status"
      },
      "severity": {
        "$ref": "#/$defs/severity"
      },
      "externalFindingLink": {
        "type": "string"
      },
      "source": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "remediation": {
        "type": "string"
      }
    },
    "required": [
      "name",
      "status"
    ],
    "additionalProperties": false
  },
  "vulnerabilityFinding": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "severity": {
        "$ref": "#/$defs/severity"
      },
      "externalDetectionSource": {
        "$ref": "#/$defs/detectionMethod"
      },
      "detailedName": {
        "type": "string"
      },
      "version": {
        "type": "string"
      },
      "fixedVersion": {
        "type": "string"
      },
      "externalFindingLink": {
        "type": "string"
      },
      "source": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "remediation": {
        "type": "string"
      },
      "validatedAtRuntime": {
        "type": "boolean"
      }
    },
    "required": [
      "name",
      "severity"
    ],
    "additionalProperties": false
  },
  "webAppVulnerabilityFinding": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "severity": {
        "$ref": "#/$defs/severity"
      },
      "detailedName": {
        "type": "string"
      },
      "externalFindingLink": {
        "type": "string"
      },
      "source": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "remediation": {
        "type": "string"
      }
    },
    "required": [
      "name",
      "severity"
    ],
    "additionalProperties": false
  },
  "dataFinding": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "source": {
        "type": "string"
      },
      "externalFindingLink": {
        "type": "string"
      },
      "dataCategory": {
        "$ref": "#/$defs/dataCategory"
      },
      "severity": {
        "$ref": "#/$defs/severity"
      },
      "dataClassifierId": {
        "$ref": "#/$defs/dataClassifier"
      }
    },
    "required": [
      "name",
      "dataCategory",
      "dataClassifierId"
    ],
    "additionalProperties": false
  },
  "event": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "timestamp": {
        "type": "string",
        "format": "date-time"
      },
      "name": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "externalFindingLink": {
        "type": "string"
      },
      "severity": {
        "$ref": "#/$defs/eventSeverity"
      },
      "mitreTacticIds": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/mitreTacticId"
        }
      },
      "mitreTacticNames": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/mitreTacticName"
        }
      },
      "mitreTechniqueIds": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/mitreTechniqueId"
        }
      },
      "mitreTechniqueNames": {
        "type": "array",
        "items": {
          "$ref": "#/$defs/mitreTechniqueName"
        }
      },
      "principal": {
        "type": "string"
      },
      "ipAddress": {
        "type": "string"
      },
      "commandLine": {
        "type": "string"
      },
      "path": {
        "type": "string"
      },
      "hash": {
        "type": "string"
      }
    },
    "required": [
      "id",
      "timestamp",
      "name",
      "externalFindingLink",
      "severity",
      "mitreTacticIds",
      "mitreTechniqueIds"
    ],
    "additionalProperties": false
  },
  "keyValue": {
    "type": "object",
    "properties": {
      "key": {
        "type": "string"
      },
      "value": {
        "type": "string"
      }
    },
    "required": [
      "key",
      "value"
    ],
    "additionalProperties": false
  }
}

```

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).