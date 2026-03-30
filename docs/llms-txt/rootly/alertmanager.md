# Source: https://docs.rootly.com/integrations/alertmanager.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Prometheus Alertmanager

> Integrate Prometheus Alertmanager with Rootly to send webhook alerts that can create incidents, notify channels, or trigger on-call paging.

## Why

Prometheus [Alertmanager](https://github.com/prometheus/alertmanager "Alertmanager") will let you send a webhook to Rootly as an incoming alert. The incoming alert can then be used to either create an incident, notify channels, or page on-call targets.

## Installation

Locate **Alertmanager** on the [Integrations catalogue](https://rootly.com/account/integrations "Integrations catalogue") and select `Setup`. You will be presented with the following pop-up.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/prometheus/images-1.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=597010e4d7320df9393b7b48bca9f1d7" width="861" height="426" data-path="images/integrations/prometheus/images-1.webp" />
</Frame>

### Receiving General Alerts

In order to send general (non-paging) alerts to Rootly, you'll need to modify the `alert-manager.yml` configuration file as shown below:

```YAML  theme={null}
route:
  receiver: default
  group_by:
  - job
  routes:
  - receiver: rootly
    match:
      alertname: Rootly
    repeat_interval: 1m

receivers:
 - name: rootly
   webhook_configs:
   - url: 'https://webhooks.rootly.com/webhooks/incoming/alertmanager_webhooks'
     send_resolved: true
     http_config:
       authorization:
         type: Bearer
         credentials: a0b9fcad1aae0689cfa05c17df497b2bc5c56d26d3e253503438864dbd6697ee
```

Copy the *Webhook URL* field and *secret* from the pop-up above, and set it as the `url` and `credentials` parameters, respectively.

<Note>
  If you lose the pop-up above, you can find it again from your Prometheus integration page in Rootly (**Integrations** > **Prometheus** > **Configure**).
</Note>

### To Page Rootly On-Call

Prometheus (Alertmanager) can be configured in two different ways to page Rootly On-Call.

#### Via Receiver URL in Alertmanager

Similarly to the non-paging alert setup above, you'll need to modify the alertmanager.yml configuration file as shown below. The main difference here being the notification target must be specified as part of the *receivers* url.

```YAML  theme={null}
route:
  receiver: default
  group_by:
  - job
  routes:
  - receiver: rootly
    match:
      alertname: Rootly
    repeat_interval: 1m

receivers:
 - name: rootly
   webhook_configs:
   - url: 'https://webhooks.rootly.com/webhooks/incoming/alertmanager_webhooks/notify/User/27854'
     send_resolved: true
     http_config:
       authorization:
         type: Bearer
         credentials: a0b9fcad1aae0689cfa05c17df497b2bc5c56d26d3e253503438864dbd6697ee
```

Copy the *Webhook URL* field and *secret* from the Prometheus (Alertmanager) configuration modal in Rootly, and set it as the `url` and `credentials` parameters, respectively.

Then set the notification target by appending the following to the end of the `url`.

`notify/<resource_type>/<resource_id>`

The notification target consists of the following:

* `resource_type` - this defines the Rootly resource type that will be used for paging.
  * The following are the available values: `User` | `Group` (Team) | `EscalationPolicy` | `Service`
* `resource_id` - this specifies the exact resource that will be targeted for the page.
  * The id of the resource can be found when editing each resource.

#### Via Prometheus Rules Annotation

If you are using Prometheus's alerting rules, you can set the notification target through the annotations in your `prometheus.rules.yml` file.

```yaml  theme={null}
groups:
- name: ./rules.conf
  rules:

  # heartbeat alert
  - alert: Heartbeat
    expr: vector(1)
    labels:
      event: "Heartbeat"
      instance: "prometheus"
      monitor: "prometheus"
      severity: "major"
      timeout: "120"
    annotations:
      summary: "Heartbeat from prometheus"
      description: "Heartbeat from from prometheus"
      rootly: "{\"notification_target\":{\"type\":\"User\",\"id\":\"27854\"}}"
```

The notification target values can be set to the following under the rootly field:

* `Type` - this defines the Rootly resource type that will be used for paging.
  * The following are the available values: `User` | `Group` (Team) | `EscalationPolicy` | `Service`
* `id` - this specifies the exact resource that will be targeted for the page.
  * The id of the resource can be found when editing each resource.

# Support

Please visit [https://prometheus.io/docs/alerting/latest/configuration/](https://prometheus.io/docs/alerting/latest/configuration/ "https://prometheus.io/docs/alerting/latest/configuration/") for more information on Prometheus Alertmanager.

If you need help or more information about this integration, please contact [support@rootly.com](mailto:support@rootly.com) or start a chat by navigating to **Help > Chat with Us**.


Built with [Mintlify](https://mintlify.com).