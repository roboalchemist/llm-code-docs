# Source: https://docs.instabug.com/product-guides-and-integrations/integrations/pagerduty.md

# PagerDuty

### Setting up the integration

{% stepper %}
{% step %}

#### Create a Custom Event Transformer in PagerDuty

To set up your PagerDuty integration, create a Custom Event Transformer in PagerDuty, which will allow you to map Luciq events to a PagerDuty Incident.

Link: <https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTc5-custom-event-transformer>
{% endstep %}

{% step %}

#### Edit the transformer code

Once the Custom Event Transformer is created, edit the code portion to look something like this (feel free to change this to customize it for your needs):

{% code title="transformer.js" %}

```javascript
var body = PD.inputRequest.body

var normalized_event = {
  event_type: PD.Trigger,
  description: `Luciq | ${body.application} | ${body.trace} ${body.trigger_operator}`,
  details: PD.inputRequest,
  client: "Luciq",
  client_url: body.url
};

PD.emitGenericEvents([normalized_event]);
```

{% endcode %}
{% endstep %}

{% step %}

#### Add the PagerDuty webhook URL

Simply add the PagerDuty webhook URL to which Luciq should forward your alerts.

![](https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F1jX8ga8MxT904h3yMcQ0%2Fe79f17e9bf9c33fe52c0c8fe2cb8c4d3bb4778494a6368f9db7ab26860ef433e%20pagerduty%202.png?alt=media\&token=08a3387c-2d2b-47a5-bab0-7851a24f00f4)
{% endstep %}

{% step %}

#### Test the integration

At this point, test your integration so that you're sure everything is working smoothly.

![](https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FX6UqkWoYsuT56z6FpvAP%2F500f0adf262fb69b90d5378ef6207016741413d815e2aaa6860a08455504b7fa%20pagerduty%201.png?alt=media\&token=06de3078-16a5-4538-93ed-6ab7dd56fd10)
{% endstep %}

{% step %}

#### Finish and name your integration

All done! Your integration is now set up — give your integration a name and you're ready to go.

![](https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FYVEiemtyzlewNek7o9qm%2Fa8c28177eb8b5e84f65f5c18e1e31d984649ebfc39b6fd54dbadfa8c0159af9a%20pagerduty%203.png?alt=media\&token=4fc80223-0137-4018-896e-f93268a0417d)
{% endstep %}
{% endstepper %}

### JSON model

{% code title="JSON" %}

```json
{
  "application": "String", // Luciq App Name, 
  "platform": "String", // the App Platform (IOS, ...)
  "title": "String", // Rule title
  "app_version": "String", // The App Version, Example: 1.0.1,...
  "metric": "String", //the Metric that the incident is related to, Example: Screen Loading, App Launches, ..
  "trace": "String", //Crash Cause: exception name, Filename, and line, or Group name example Hot/cold App Launch
  "trigger": "String", // The Alert Trigger, Example: Crash-free sessions in the last 24 hours
  "trigger_operator": "String", // [Tigger] + [Tigger operator] + [Trigger value] + [Time frame]
  "conditions": [ //[Alert conditions] 
    {
      "key": "String",
      "operator": "String",
      "value": "String"
    }
  ],
  "conditions_operation": "String", // the conditions are ANDed or ORed
  "current_value": "String",// the Actual value of the metric at the time of the incident
  "url": "String" // in case the rule is a crashes rule, URL will be the Crash URL, other wise it will be the incident url
}
```

{% endcode %}
