# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/apm-alerting/prometheus.md

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/webhook/examples/prometheus.md

# Prometheus

In this example you are going to create a webhook integration between [Prometheus Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) and Port, which will ingest alert entities.

## Port configuration[â](#port-configuration "Direct link to Port configuration")

Create the following blueprint definition:

Alert blueprint

Create in Port

```
{
  "identifier": "prometheusAlerts",
  "description": "Prometheus alerts in your software catalog",
  "title": "Prometheus Alerts",
  "icon": "Prometheus",
  "schema": {
    "properties": {
      "status": {
        "title": "Status",
        "description": "Current status of the alert, firing or resolved",
        "type": "string",
        "enum": ["firing", "resolved"],
        "enumColors": {
          "firing": "red",
          "resolved": "green"
        }
      },
      "labels": {
        "title": "Labels",
        "type": "object",
        "description": "Labels that are part of this alert, map of string keys to string values"
      },
      "createdAt": {
        "title": "Created at",
        "description": "Start time of the alert",
        "type": "string",
        "format": "date-time"
      },
      "resolvedAt": {
        "title": "Resolved At",
        "type": "string",
        "description": "End time of the alert",
        "format": "date-time"
      },
      "generatorURL": {
        "title": "Generator URL",
        "type": "string",
        "description": "URL of the alert rule in the Prometheus UI",
        "format": "url"
      },
      "fingerprint": {
        "title": "Fingerprint",
        "description": "The labels fingerprint, alarms with the same labels will have the same fingerprint",
        "type": "string"
      },
      "summary": {
        "title": "Summary",
        "type": "string"
      },
      "severity": {
        "title": "Severity",
        "type": "string",
        "enum": [
          "indeterminate",
          "information",
          "warning",
          "minor",
          "major",
          "critical",
          "fatal"
        ],
        "enumColors": {
          "indeterminate": "purple",
          "information": "blue",
          "warning": "yellow",
          "minor": "lightGray",
          "major": "pink",
          "critical": "red",
          "fatal": "red"
        }
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

Create the following webhook configuration [using Port's UI](/build-your-software-catalog/custom-integration/webhook/.md?operation=ui#configuring-webhook-endpoints)

Alert webhook configuration

1. **Basic details** tab - fill the following details:

   1. Title : `Prometheus Alert Mapper`;
   2. Identifier : `prometheus_alert_mapper`;
   3. Description : `A webhook configuration to map Prometheus alerts to Port`;
   4. Icon : `Prometheus`;

2. **Integration configuration** tab - fill the following JQ mapping:

   ```
   [
     {
       "blueprint": "prometheusAlerts",
       "filter": "true",
       "itemsToParse": ".body.alerts",
       "entity": {
         "identifier": ".item.labels.alertname + \"-\" + .item.fingerprint | gsub(\"[^a-zA-Z0-9@_.:/=-]\"; \"-\") | tostring",
         "title": ".item.labels.alertname",
         "properties": {
           "status": ".item.status",
           "severity": ".item.labels.severity",
           "labels": ".item.labels",
           "summary": ".item.annotations.summary",
           "createdAt": ".item.startsAt",
           "resolvedAt": ".item.endsAt",
           "generatorURL": "if .item.generatorURL != \"\" then .item.generatorURL else null end",
           "fingerprint": ".item.fingerprint"
         }
       }
     }
   ]
   ```

3. Click **Save** at the bottom of the page.

## Configure Alertmanager to send webhook[â](#configure-alertmanager-to-send-webhook "Direct link to Configure Alertmanager to send webhook")

1. Ensure you have the Prometheus Alertmanager installed as described in [prometheus/alertmanager](https://github.com/prometheus/alertmanager#installation);

2. Configure the Alertmanager to send alert information from your server to Port. Edit your Alertmanager configuration file (`alertmanager.yaml`) to add the generated webhook from Port as a **receivers**;

   1. Create a new **receivers** object called `port_webhook`. Paste the webhook `URL` into the `url` field and set the `send_resolved` value to `true`.
   2. Add the `port_webhook` **receivers** to the **route** object;

   Example configuration file.

   ```
   global:
     resolve_timeout: 20s

   route:
     group_wait: 30s
     group_interval: 5m
     repeat_interval: 3h
     receiver: port_webhook

   receivers:
    - name: port_webhook
    webhook_configs:
    - url: https://port-webhook-url
       send_resolved: true
   ```

3. Save the `alertmanager.yaml` file and restart the alertmanager to apply the changes.

Done! Any change that happens to your alerts in your server will trigger a webhook event to the webhook URL provided by Port. Port will parse the events according to the mapping and update the catalog entities accordingly.

# Let's Test It

This section includes a sample response data from Prometheus. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Prometheus:

**Webhook response data (Click to expand)**

```
{
      "status": "firing",
      "labels": {
        "severity": "critical",
        "instance": "server-01",
        "alertname": "High CPU Usage",
      },
      "annotations": {
        "summary": "High CPU Usage Alert"
      },
      "startsAt": "2024-02-12T08:00:00Z",
      "endsAt": "",
      "generatorURL": "https://monitoring.example.com",
      "fingerprint": "123abc456def"
    }
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

**Alert entity in Port (Click to expand)**

```
{
  "identifier": "High CPU Usage - 123abc456def",
  "title": "High CPU Usage",
  "blueprint": "prometheusAlerts",
  "team": [],
  "icon": "Prometheus",
  "properties": {
      "status": "firing",
      "severity": "critical",
      "labels": {
         "severity": "critical",
         "instance": "server-01",
         "alertname": "High CPU Usage",
      },
      "summary": "High CPU Usage Alert",
      "createdAt": "2024-02-12T08:00:00+00:00",
      "resolvedAt": "",
      "generatorURL": "https://monitoring.example.com",
      "fingerprint": "123abc456"
  },
  "relations": {},
  "createdAt": "2024-2-6T09:30:57.924Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2024-2-6T11:49:20.881Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
}
```
