---
id: AlertRules
title: Alert Rules
---
Alert rules let you create complex conditions for an integration, by matching fields like alert_type, summary, description of the alert, and payload sent by the alert.Alert Rules also lets you take custom actions like assign a custom EP or a user to an integrations. Custom actions include:

1. Change alert type
2. Change incident urgency
3. Add note to incident
4. Assign incident tag
5. Assign incident role
6. Change entity_id
7. Change incident title
8. Change incident summary
9. Assign incident to a user
10. Route incident to an escalation policy other than the default policy associate with the service
11. Suppress the incident

## The basics of Alerts and Incidents in Zenduty

```
Every alert coming from an integration source has an entity_id. An entity_id points to a resource or an entity in the source application. For example, the entity_id of an alert from Jira will be its ticket ID. An alert from Datadog will be its alert ID in Datadog. An alert from Grafana will be its Rule ID. Multiple alerts can have the same entity_id. entity_id is how Zenduty groups multiple alerts about the same problem into one single incident.

Each alert comes with an alert_type. There are six types of alert types: critical, acknowledged, resolved, info, warning, error. If the alert source is sending an entity_id, and the alert type is either critical, error or warning, then that alert(depending on your integration level settings) will trigger a single incident. Every alert after that with the same entity_id will be attached to the earlier created incident. An 'acknowledged' alert_type from the source will automatically acknowledge an incident and a 'resolved' alert_type will automatically resolve the incident.

For example:

Alert 1: entity_id:database-alpha, alert_type:critical, message:DB is down

The above alert will create a new incident(Let's call it 'I'). Incident 'I' is now in the triggered state


Alert 2: entity_id:database-alpha, alert_type:critical, message:DB is still down

The above alert will not create a new incident, but will be appended as an alert to incident 'I'. Incident 'I' is will continue to be in the triggered state


Alert 3: entity_id:database-alpha, alert_type:resolved, message:DB is up

The above alert will automatically resolve the incident 'I' and will also be appended as an alert to incident 'I'


Alert 4: entity_id:database-alpha, alert_type:critical, message:DB is down

The above alert will create another new incident(Let's call it 'I2'). Incident 'I2' is now in the triggered state. 


And so on...
```

## Adding an Alert Rule

1. Go to the service your integration is in. Click on "manage".

2. Go to the "integrations" tab and choose the integration for which you want to add Alert Rules. Click on "configure".

![](/img/alert_1.png)

1. Click on the "Alert Rules" tab. Click on the "Create Alert Rule" button.

![](/img/alert_2.png)

1. Give your alert a name and set conditions and actions. Save to apply.

![](/img/alert_3.png)

1. All saved Alert Rules associated with a particular integration will show up in the Alert Rules tab in the configuration settings of the integration.

![](/img/alert_4.png)

## JSON Path Search

You can assign payload with specific rules to your alerts. Follow the [JSON path syntax here](https://restfulapi.net/json-jsonpath/) while describing these rules. For example, if the payload sent by the alert is {"project":"zd-test", "release":{"version":"2.3.1"}}, then to compare the release version, your JSONPath will be $.release.version.

![](/img/alert_5.png)

![](/img/alert_6.png)

## Modifying incident title and summary, adding notes

You can modify the incident titles and summaries by using the alert data(message, summary, payload, entity_id) within placeholders like `The incident message is {{message}}`, or `The incident summary is {{summary}}` or `High priority incident in release {{payload.release.version}}`.

![](/img/alert_7.png)

![](/img/alert_8.png)

![](/img/alert_9.png)

## Editing an Alert Rule

Simply click the "view" button next to the rule you want to edit.

## Deleting an Alert Rule

Simply click the "delete" button corresponding to the rule you want to delete.

## FAQs:

1. For time window based operations that cross into the next day, for example 18:00:00 to 04:00:00, split the time in the conditions as 18:00 to 23:59:59 and 00:00:00 to 04:00:00
