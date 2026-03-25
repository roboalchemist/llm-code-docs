# Source: https://docs.firehydrant.com/docs/microsoft-azure-monitor-event-source.md

# Microsoft Azure Monitor Event Source

The Microsoft Azure Event Source allows users to configure Azure to send Events to FireHydrant for creating Alerts. [Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules) can be configured to scan the payloads and ensure the right teams are notified of events they care about.

## Configuration

Follow [Microsoft's documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview) for configuring monitoring alerts. FireHydrant supports [Metric-type alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-payload-samples#sample-alert-payload) - other alert types should be configured with [Custom Event Sources](https://docs.firehydrant.com/docs/signals-custom-event-sources).

In FireHydrant, copy the Microsoft Azure ingress URL on the [Event Sources](https://app.firehydrant.io/signals/sources/integrations)  page and use that as the destination webhook URL for your Azure monitor alerts.

## Field Mappings

FireHydrant's Azure transposer will map the following fields to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model).

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Azure Parameter
      </th>

      <th>
        FireHydrant Parameter
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `data.essentials.originAlertId`
      </td>

      <td>
        `idempotency_key`
      </td>
    </tr>

    <tr>
      <td>
        `data.essentials.severity`\
        `data.essentials.alertRule`
      </td>

      <td>
        `summary` - Will be in the format of `[Severity] Alert Rule`
      </td>
    </tr>

    <tr>
      <td>
        `data.essentials.description`\
        `data.essentials.alertTargetIDs[]`\
        `data.essentials.configurationItems[]`
      </td>

      <td>
        `body`
      </td>
    </tr>

    <tr>
      <td />

      <td>
        `level` - Always `ERROR`
      </td>
    </tr>

    <tr>
      <td>
        `data.essentials.monitorCondition`
      </td>

      <td>
        `status` - Open when `monitorCondition` is "Fired" otherwise closed
      </td>
    </tr>

    <tr>
      <td>
        `data.essentials.monitoringService`\
        `data.essentials.severity`\
        `data.essentials.signalType`
      </td>

      <td>
        `annotations['azure.monitoringService']`\
        `annotations['azure.severity']`\
        `annotations['azure.signalType']`
      </td>
    </tr>
  </tbody>
</Table>

These mappings mean that an inbound webhook from Azure with the following content:

```json Azure Payload
{
  "schemaId": "azureMonitorCommonAlertSchema",
  "data": {
    "essentials": {
      "alertId": "/subscriptions/testsubid/providers/Microsoft.AlertsManagement/alerts/b9569717-bc32-442f-add5-83a997729330",
      "alertRule": "WCUS-R2-Gen2",
      "severity": "Sev3",
      "signalType": "Metric",
      "monitorCondition": "Fired",
      "monitoringService": "Platform",
      "alertTargetIDs": [
        "/subscriptions/testsubid/resourcegroups/pipelinealertrg/providers/microsoft.compute/virtualmachines/wcus-r2-gen2"
      ],
      "configurationItems": [
        "wcus-r2-gen2"
      ],
      "originAlertId": "3f2d4487-b0fc-4125-8bd5-7ad17384221e_PipeLineAlertRG_microsoft.insights_metricAlerts_WCUS-R2-Gen2_-117781227",
      "firedDateTime": "2019-03-22T13:58:24.3713213Z",
      "description": "foobar",
      "essentialsVersion": "1.0",
      "alertContextVersion": "1.0"
    },
    "alertContext": {
      "properties": null,
      "conditionType": "SingleResourceMultipleMetricCriteria",
      "condition": {
        "windowSize": "PT5M",
        "allOf": [
          {
            "metricName": "Percentage CPU",
            "metricNamespace": "Microsoft.Compute/virtualMachines",
            "operator": "GreaterThan",
            "threshold": "25",
            "timeAggregation": "Average",
            "dimensions": [
              {
                "name": "ResourceId",
                "value": "3efad9dc-3d50-4eac-9c87-8b3fd6f97e4e"
              }
            ],
            "metricValue": 7.727
          }
        ]
      }
    },
    "customProperties": {
      "Key1": "Value1",
      "Key2": "Value2"
    }
  }
}
```

...will result in the following mapped Signal on FireHydrant:

````json Transposed Signal
{
  "summary": "[Sev3] WCUS-R2-Gen2",
  "body": "foobar\n\n**Alert Target IDs:**\n```\n- /subscriptions/testsubid/resourcegroups/pipelinealertrg/providers/microsoft.compute/virtualmachines/wcus-r2-gen2\n```\n\n**Configuration Items:**\n```\n- wcus-r2-gen2\n```\n",
  "idempotency_key": "3f2d4487-b0fc-4125-8bd5-7ad17384221e_PipeLineAlertRG_microsoft.insights_metricAlerts_WCUS-R2-Gen2_-117781227",
  "level": "ERROR",
  "annotations": {
    "azure.monitoringService": "Platform",
    "azure.severity": "Sev3",
    "azure.signalType": "Metric"
  }
}
````