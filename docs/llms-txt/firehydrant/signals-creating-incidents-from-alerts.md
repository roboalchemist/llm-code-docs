# Source: https://docs.firehydrant.com/docs/signals-creating-incidents-from-alerts.md

# Creating Incidents from Alerts

Alerts are the first step in the Incident Management process: they help you assemble the right person or team to determine if a Signal from your system might be an incident. Let’s take a look at how Alerts in FireHydrant connect to the Incident Management

## Fine-Tuning Alerts for Better Incidents

One of the best ways to improve your incident response is to ensure that your teams are alerted for things that are most likely to turn into incidents. FireHydrant provides a few ways for you to fine-tune your alerts.

🔀 **Run a Back-Test of Signals using CEL**\
On the Alert Rules page, you can quickly run a backtest of events by running a CEL query in the page's filter builder. Running a backtest can give you an idea of the volume of any query, and you can easily create new [Alert Rules](https://docs.firehydrant.com/docs/alert-rules) from a query.

📊 **Alerting Analytics**\
Use our new Alerting Analytics page to understand how incoming events are turning into Alerts, how many alerts are being acknowledged, and how many alerts are then turning into incidents. You can also see alerting metrics by multiple facets including teams, service catalog components, or rules matched.

## Opening Incidents from Alerts

Alerts are one of the best leading indicators of a potential incident, and in FireHydrant, you have a few ways that you can open an incident from an Alert

* When a responder receives an Alert, one of the ways that they can respond to that Alert is to Open an Incident. It’s as easy as sending a code via SMS, responding to a voice call, or clicking a button in a Slack DM, an Email, or in the mobile app.

  <Callout icon="⚡" theme="default">
    ### Open Flow

    When an incident is opened from [Mobile App](https://apps.apple.com/us/app/firehydrant/id6473452572), SMS, WhatsApp, or Voice alerts, FireHydrant skips the declare incident form and directly opens an incident. This subsequently also bypasses any required [Incident Fields](https://docs.firehydrant.com/docs/incident-fields) settings. You can later add details once the incident is opened.

    If the incident is opened from Web UI, Slack, or Email alerts, we will open the incident declaration webpage or Slack modal with pre-filled information from the alert.
  </Callout>

Regardless of the alert's state (e.g., Open, Acknowledged, Dismissed, Resolved, etc.), you can always declare an incident from the alert.

## Connecting alerts to an ongoing Incident

In cases where your team already has an ongoing incident for an Alert that comes into FireHydrant, responders can acknowledge the Alert and then connect it to the ongoing incident. In the web app, Slack, and the mobile app, they can take the Connect to Existing Incident action to select any incident in FireHydrant for that Alert.

You can link an alert with an existing incident regardless of the alert's current status, just like opening incidents.