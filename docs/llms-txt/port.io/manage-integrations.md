# Source: https://docs.port.io/guides/all/manage-integrations.md

# Monitor integrations

This guide will help you set up monitoring and management capabilities for your Port Ocean integrations.

By implementing this monitoring setup, you'll be able to track:

* Overall integration sync status and timing
* Detailed metrics per integration kind
* Object counts at various stages (raw, transformed, ingested)
* Sync duration and performance metrics

![](/img/guides/integrationsTableStats.png) ![](/img/guides/IntegrationsTableSyncKindStats.png)

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Before you begin, make sure you have:

* Self-hosted Ocean integrations installed.
* Port Ocean version v0.22.0 or later.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Monitor the health and performance of your integrations
* Track sync status and timing across different integration kinds
* Identify potential issues in the extract-transform-load (ETL) pipeline
* Measure the efficiency of your data ingestion process

## Data model setup[â](#data-model-setup "Direct link to Data model setup")

Use the following two blueprints to structure your integration data in Port:

The `Integration` blueprint tracks overall resync status, duration, and timing.

Integration Blueprint

Create in Port

```
{
  "identifier": "integration",
  "title": "Integration",
  "icon": "Ocean",
  "schema": {
    "properties": {
      "last_resync_completion_status": {
        "type": "string",
        "title": "Last Resync Completion Status",
        "icon": "Reset",
        "enum": [
          "SUCCESS",
          "FAILED"
        ],
        "enumColors": {
          "SUCCESS": "green",
          "FAILED": "red"
        }
      },
      "last_resync_duration": {
        "type": "number",
        "title": "Last Resync Duration Seconds",
        "icon": "Clock"
      },
      "last_resync_at": {
        "icon": "Updates",
        "type": "string",
        "title": "Last Resync At",
        "format": "date-time"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {}
}
```

The `Integration Kind Metrics` blueprint tracks detailed metrics for specific integration kinds, including raw, transformed, and ingested objects.

Integration Kind Metrics Blueprint

Create in Port

```
{
  "identifier": "integration_kind_metrics",
  "description": "Metrics on integration sync kind",
  "title": "Integration Kind Metrics",
  "icon": "Ocean",
  "schema": {
    "properties": {
      "kind": {
        "icon": "Sync",
        "type": "string",
        "title": "Kind"
      },
      "raw_objects": {
        "icon": "JsonEditor",
        "type": "number",
        "title": "Raw Objects"
      },
      "transformed_objects": {
        "icon": "Travel",
        "type": "number",
        "title": "Transformed Objects"
      },
      "entities_ingested": {
        "icon": "Port",
        "type": "number",
        "title": "Entities Ingested"
      },
      "duration": {
        "icon": "Clock",
        "type": "number",
        "title": "Duration"
      },
      "last_completion_status": {
        "type": "string",
        "title": "Last Completion Status",
        "icon": "Reset",
        "enum": [
          "SUCCESS",
          "FAILED"
        ],
        "enumColors": {
          "SUCCESS": "green",
          "FAILED": "red"
        }
      },
      "last_sync_at": {
        "type": "string",
        "title": "Last Sync At",
        "icon": "Clock",
        "format": "date-time"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "integration": {
      "title": "Integration",
      "target": "integration",
      "required": false,
      "many": false
    }
  }
}
```

## Webhook setup[â](#webhook-setup "Direct link to Webhook setup")

1. Go to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.
2. Click on **+ Data source**, and choose the **Webhook** type.
3. Click on **Custom integration** and create a new webhook.
4. Copy and store the generated webhook URL (should be in a format like `https://ingest.getport.io/abc123`).
5. Add the mappings below in the relevant section on the webhook configuration (see screenshot below).

![](/img/guides/portDataSourcesWebhookMapping.png)

**For Integration Kind Metrics**:

Integration Kind Metrics Webhook Mapping

```
{
  "blueprint": "integration_kind_metrics",
  "operation": "create",
  "filter": ".body.kindIdentifier != '__runtime__'",
  "entity": {
    "identifier": ".body.kindIdentifier",
    "title": ".body.kindIdentifier",
    "properties": {
      "kind": ".body.kind",
      "duration": ".body.metrics.phase.resync.durationSeconds|round",
      "raw_objects": ".body.metrics.phase.extract.objectCountType.rawExtracted.objectCount",
      "transformed_objects": ".body.metrics.phase.transform.objectCountType.transformed.objectCount",
      "entities_ingested": ".body.metrics.phase.load.objectCountType.loaded.objectCount",
      "last_completion_status": "if .body.metrics.phase.resync.success == 1 then \"SUCCESS\" else \"FAILED\" end",
      "last_sync_at": "now | todateiso8601"
    },
    "relations": {
      "integration": ".body.integrationType + \"-\" + .body.integrationIdentifier"
    }
  }
}
```

**For Integration Runtime Status**:

Integration Runtime Status Webhook Mapping

```
{
  "blueprint": "integration",
  "operation": "create",
  "filter": ".body.kindIdentifier == '__runtime__'",
  "entity": {
    "identifier": ".body.integrationType + \"-\" + .body.integrationIdentifier",
    "title": ".body.integrationIdentifier",
    "properties": {
      "last_resync_duration": ".body.metrics.phase.resync.durationSeconds|round",
      "last_resync_completion_status": "if .body.metrics.phase.resync.success == 1 then \"SUCCESS\" else \"FAILED\" end",
      "last_resync_at": "now | todateiso8601"
    }
  }
}
```

Ensure the mappings are correctly added to handle both cases distinctly.

## Configure metrics collection[â](#configure-metrics-collection "Direct link to Configure metrics collection")

Ocean Version requirement

Make sure you've updated the port-ocean version to use v0.22.0 or later.

To activate metrics collection, pass the following parameters when configuring your integration:

```
OCEAN__METRICS__ENABLED=true
OCEAN__METRICS__WEBHOOK_URL=<THE GENERATED WEBHOOK URL>
```

Replace `<THE GENERATED WEBHOOK URL>` with the URL you generated in Step 2.

tip

Remember to repeat this step for each integration you want to monitor.

## Create a monitoring dashboard[â](#create-a-monitoring-dashboard "Direct link to Create a monitoring dashboard")

Now you can set up a dashboard to visualize your integration metrics:

1. Navigate to your [software catalog](https://app.getport.io/organization/catalog).
2. Click **+ New**, select **New dashboard**, and create a new dashboard.
3. Add a **Table** widget, and select the `integration` blueprint.
4. Add a **Line chart** widget, select the `integration` blueprint, the integration you want to monitor, and the `last resync duration` property.
5. Add **Number chart** to show the `raw`, `transformed`, and `ingested` counts as either aggregated values or for a specific integration.

## Test your monitoring[â](#test-your-monitoring "Direct link to Test your monitoring")

After completing these steps:

1. Trigger your integration sync
2. Check Port to verify the status updates and metrics
3. Review your dashboard to ensure all widgets are populated with data

Health check endpoint

All Ocean integrations expose a health check endpoint at `/docs`.

For example, if your integration is accessible at `https://your-integration-host:8000`, you can access the health check at `https://your-integration-host:8000/docs`.
