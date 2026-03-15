# Source: https://docs.firehydrant.com/docs/alertmanager-integration.md

# Alertmanager

Alertmanager from Prometheus handles alerts sent by applications like the Prometheus server. Use alerts from Alertmanager to power incidents and notifications in FireHydrant.

> 🚧 Alertmanager and Signals
>
> If you're looking to connect Alertmanager to FireHydrant to create alerts in Signals, checkout the Signals Integration guide for [Alertmanager](https://docs.firehydrant.com/docs/signals-alertmanager). This document describes Alert Routing, which does not send pages or alerts to responders.

## Configuration steps

1. First, you need to authorize the Alertmanager integration on [FireHydrant's\
   integrations page](https://app.firehydrant.io/organizations/integrations).
2. You'll see a webhook URL provided once you click **Authorize Application**.
3. Now configure Alertmanager to send alerts to the webhook above. This is done\
   by creating a new "receiver" in Alertmanager. You will need to add something\
   similar to the following snippet to your configuration:

```yaml
 "receivers":
 - name: firehydrant
   webhook_configs:
     - url: "<integration-webhook-url>"
 "route":
   "routes":
   - receiver: firehydrant
     continue: true
```

See [additional documentation for configuring Alertmanager webhooks](https://prometheus.io/docs/alerting/latest/configuration/#webhook_config).

## Using Alert Routes with Alertmanager

Once Alertmanager is configured, you can set up Alert Routes to take action on your alerts based on the data included in the alert. You can automatically open new incidents, send alerts to any Slack channel, log an alert in FireHydrant, or simply ignore it. To learn more, read about [Alert Routing](https://docs.firehydrant.com/docs/alert-routing).