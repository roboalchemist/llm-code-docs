# Source: https://docs.port.io/build-your-software-catalog/custom-integration/webhook/examples/grafana.md

# Grafana

In this example you are going to create a webhook integration between [Grafana](https://grafana.com/) and Port, which will ingest alert entities.

## Port configuration[â](#port-configuration "Direct link to Port configuration")

Create the following blueprint definition:

Alert blueprint

Create in Port

```
{
  "identifier": "grafanaAlert",
  "description": "This blueprint represents a Grafana alert in your software catalog",
  "title": "Grafana Alert",
  "icon": "Grafana",
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
      "description": {
        "title": "Description",
        "type": "string"
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
      "values": {
        "title": "Values",
        "type": "object",
        "description": "Values that triggered the current status"
      },
      "generatorURL": {
        "title": "Generator URL",
        "type": "string",
        "description": "URL of the alert rule in the Grafana UI",
        "format": "url"
      },
      "fingerprint": {
        "title": "Fingerprint",
        "description": "The labels fingerprint, alarms with the same labels will have the same fingerprint",
        "type": "string"
      },
      "silenceURL": {
        "title": "Silence URL",
        "description": "URL to silence the alert rule in the Grafana UI",
        "type": "string",
        "format": "url"
      },
      "summary": {
        "title": "Summary",
        "type": "string"
      },
      "runbookURL": {
        "title": "Runbook URL",
        "type": "string",
        "description": "URL of the runbook in the Grafana UI",
        "format": "url"
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

   1. Title : `Grafana Alert Mapper`;
   2. Identifier : `grafana_alert_mapper`;
   3. Description : `A webhook configuration to map Grafana alerts to Port`;
   4. Icon : `Grafana`;

2. **Integration configuration** tab - fill the following JQ mapping:

   ```
   [
     {
       "blueprint": "grafanaAlert",
       "filter": "true",
       "itemsToParse": ".body.alerts",
       "entity": {
         "identifier": ".item.labels.alertname + \"-\" + .item.fingerprint | gsub(\"[^a-zA-Z0-9@_.:/=-]\"; \"-\") | tostring",
         "title": ".item.labels.alertname",
         "properties": {
           "status": ".item.status",
           "labels": ".item.labels",
           "description": ".item.annotations.description",
           "summary": ".item.annotations.summary",
           "runbookURL": ".item.annotations.runbook_url",
           "createdAt": ".item.startsAt",
           "resolvedAt": ".item.endsAt",
           "values": ".item.values",
           "generatorURL": "if .item.generatorURL != \"\" then .item.generatorURL else null end",
           "fingerprint": ".item.fingerprint",
           "silenceURL": "if .item.silenceURL != \"\" then .item.silenceURL else null end"
         }
       }
     }
   ]
   ```

3. Click **Save** at the bottom of the page.

## Create a webhook in Grafana[â](#create-a-webhook-in-grafana "Direct link to Create a webhook in Grafana")

1. Go to **Alerting** in your Grafana account;

2. Under **Contact points** click **Add contact point**;

3. Input the following details:

   <!-- -->

   1. `Name` - use a meaningful name such as Port Webhook;
   2. `Integration` - select `Webhook` from the list;
   3. `URL` - enter the value of the `url` key you received after creating the webhook configuration;

4. Click **Save contact point** to save the contact;

5. Go to **Notification policies** and add the Port Webhook contact point to your **Default policy** and be notified of any alert in Grafana;

6. You can optionally add the contact point to an existing notification policy or create a new policy depending on your use case;

7. Click **Save policy**.

Done! any change that happens to your alerts in Grafana will trigger a webhook event to the webhook URL provided by Port. Port will parse the events according to the mapping and update the catalog entities accordingly.

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from Grafana. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Grafana:

**Webhook response data (Click to expand)**

```
{
  "status": "firing",
  "labels": {
    "alertname": "High memory usage",
    "team": "blue",
    "zone": "us-1"
  },
  "annotations": {
    "description": "The system has high memory usage",
    "runbook_url": "https://myrunbook.com/runbook/1234",
    "summary": "This alert was triggered for zone us-1"
  },
  "startsAt": "2021-10-12T09:51:03.157076+02:00",
  "endsAt": "0001-01-01T00:00:00Z",
  "generatorURL": "https://play.grafana.org/alerting/1afz29v7z/edit",
  "fingerprint": "c6eadffa33fcdf37",
  "silenceURL": "https://play.grafana.org/alerting/silence/new?alertmanager=grafana&matchers=alertname%3DT2%2Cteam%3Dblue%2Czone%3Dus-1",
  "dashboardURL": "",
  "panelURL": "",
  "values": {
    "B": 44.23943737541908,
    "C": 1
  }
}
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

**Alert entity in Port (Click to expand)**

```
{
  "identifier": "High memory usage - c6eadffa33fcdf37",
  "title": "High memory usage",
  "blueprint": "grafanaAlert",
  "team": [],
  "icon": "Grafana",
  "properties": {
    "status": "firing",
    "labels": {
      "alertname": "High memory usage",
      "team": "blue",
      "zone": "us-1"
    },
    "description": "The system has high memory usage",
    "summary": "This alert was triggered for zone us-1",
    "runbookURL": "https://myrunbook.com/runbook/1234",
    "createdAt": "2021-10-12T09:51:03.157076+02:00",
    "resolvedAt": "0001-01-01T00:00:00+00:00",
    "values": {
      "B": 44.23943737541908,
      "C": 1
    },
    "generatorURL": "https://play.grafana.org/alerting/1afz29v7z/edit",
    "fingerprint": "c6eadffa33fcdf37",
    "silenceURL": "https://play.grafana.org/alerting/silence/new?alertmanager=grafana&matchers=alertname%3DT2%2Cteam%3Dblue%2Czone%3Dus-1"
  },
  "relations": {},
  "createdAt": "2024-2-6T09:30:57.924Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2024-2-6T11:49:20.881Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
}
```
