# Source: https://docs.datadoghq.com/continuous_integration/pipelines.md

# Source: https://docs.datadoghq.com/cloudprem/configure/pipelines.md

---
title: Processing Configuration
description: Learn how to configure your processing pipelines in CloudPrem
breadcrumbs: Docs > CloudPrem > Configure CloudPrem > Processing Configuration
---

# Processing Configuration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### CloudPrem is in Preview

Join the CloudPrem Preview to access new self-hosted log management features.

[Request Access](https://www.datadoghq.com/product-preview/cloudprem/)
{% /callout %}

## Overview{% #overview %}

CloudPrem includes a processing feature that allows you to parse and enrich logs. It automatically parses logs formatted in JSON. You can define pipelines and processors to extract meaningful information or attributes from semi-structured text, which can then be used for aggregations.

{% alert level="info" %}
CloudPrem log pipelines and processors are designed to be match the capabilities of Datadog's [cloud-based log pipelines and processors](https://docs.datadoghq.com/logs/log_configuration/pipelines/?tab=source).
{% /alert %}

For a list of supported and unsupported processors, see Compatibility with cloud-based pipelines.

You can configure log processing pipelines using a JSON file that adheres to the same format as Datadog pipeline configurations.

## Setting up processing{% #setting-up-processing %}

1. (Optional) If you have existing cloud-based pipelines in Datadog, you can fetch the configuration using the [Logs Pipelines API](https://docs.datadoghq.com/api/latest/logs-pipelines/#get-all-pipelines):

   ```bash
   curl -X GET "https://api.datadoghq.com/api/v1/logs/config/pipelines" \
    -H "Accept: application/json" \
    -H "DD-API-KEY: ${DD_API_KEY}" \
    -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" > pipelines-config.json
   ```

This JSON file can be used directly with CloudPrem.

To set the configuration in the Helm Chart, provide the path to your JSON configuration file using the `pipelinesConfig` parameter in the CloudPrem Helm chart:

```bash
helm repo update
helm upgrade <RELEASE_NAME> -n <NAMESPACE_NAME> --set-file pipelinesConfig=./pipelines-config.json -f datadog-values.yaml
```

CloudPrem logs an informational message (`Successfully read pipeline config file`) when it successfully reads the configuration file. Any processors defined in the file that are not supported by CloudPrem are ignored during startup. **Note**: Helm imposes a 1 MB size limit on the configuration file due to its underlying etcd storage.

## Configuration file format{% #configuration-file-format %}

The configuration is a JSON array, where each element represents a processor or a nested pipeline.

The order of elements in the array defines the sequential execution order of the processors. The structure mirrors the output of the Datadog API endpoint `api/v1/logs/config/pipelines`.

```json
[
  {
    // processor1 details
  },
  {
    // processor2 details
  }
]
```

```json
[
  {
    "type": "pipeline",
    "id": "U73LOMZ9QG2iM-04OcXypA",
    "name": "cluster agent logs parsing",
    "enabled": true,
    "filter": {
      "query": "service:cluster-agent"
    },
    "processors": [
      {
        "type": "grok-parser",
        "id": "xn2WAzysQ1asaasdfakjf",
        "enabled": true,
        "grok": {
          "supportRules": "",
          "matchRules": "agent_rule %{date(\"yyyy-MM-dd HH:mm:ss z\"):timestamp} \\| %{notSpace:agent} \\| %{word:level} \\| \\(%{notSpace:filename}:%{number:lineno} in %{word:process}\\) \\|( %{data::keyvalue(\":\")} \\|)?( - \\|)?( \\(%{notSpace:pyFilename}:%{number:pyLineno}\\) \\|)?%{data}\nagent_rule_pre_611 %{date(\"yyyy-MM-dd HH:mm:ss z\"):timestamp} \\| %{word:level} \\| \\(%{notSpace:filename}:%{number:lineno} in %{word:process}\\)%{data}\njmxfetch_rule     %{date(\"yyyy-MM-dd HH:mm:ss z\"):timestamp} \\| %{notSpace:agent} \\| %{word:level}\\s+\\| %{word:class} \\| %{data}"
        }
      },
      {
        "id": "xnsd5oanXq2893utcsQ",
        "type": "status-remapper",
        "enabled": true,
        "sources": ["level"]
      },
      {
        "type": "date-remapper",
        "id": "xn2WAzysQ1asdjJsb9dfb",
        "enabled": true,
        "sources": ["timestamp"]
      }
    ]
  }
]
```

## Compatibility with cloud-based pipelines{% #compatibility-with-cloud-based-pipelines %}

CloudPrem processing is designed to align closely with cloud-based [Datadog Log Management](https://docs.datadoghq.com/logs/log_configuration/processors/), allowing direct use of existing log pipeline configurations. It achieves this by ignoring unknown or unsupported processors. However, some differences exist:

- Some filter queries can't be parsed, such as filters with combined wildcards (for example, `@data.message:+*`).
- Filter on `message` has a different matching behavior (it also affects the category processor).
- CloudPrem uses a regex to grep the word, but it should tokenize the text and try to match the tokens. Phrases are also ignored.
- Groks use regular expressions internally. The regex engines may have slightly different matching behavior.
- Some grok patterns can't be parsed (for example, `%{?>notSpace:db.severity}`).

Ignored processors appear as a warning in the indexer logs.

### Supported Processors:{% #supported-processors %}

- attribute-remapper
- category-processor
- date-remapper
- grok-parser (limited compatibility)
- message-remapper
- pipeline
- service-remapper
- status-remapper
- string-builder-processor
- trace-id-remapper

### Unsupported Processors:{% #unsupported-processors %}

- arithmetic-processor
- geo-ip-parser
- lookup-processor
- url-parser
- user-agent-parser

## Further reading{% #further-reading %}

- [Learn more about CloudPrem Architecture](https://docs.datadoghq.com/cloudprem/architecture/)
- [Troubleshooting](https://docs.datadoghq.com/cloudprem/troubleshooting/)
