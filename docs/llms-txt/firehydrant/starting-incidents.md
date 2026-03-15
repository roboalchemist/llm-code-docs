# Source: https://docs.firehydrant.com/docs/starting-incidents.md

# Starting Incidents

There are several methods for declaring incidents in FireHydrant:

1. Manually from Slack using our Slackbot
2. Manually via the Web UI
3. Using [Alert Routing](https://docs.firehydrant.com/docs/alert-routing)
4. Via integrations like [Zendesk](https://docs.firehydrant.com/docs/zendesk-integration) or Backstage
5. Programmatically [using the API](https://developers.firehydrant.com/#/operations/postV1Incidents)

***

## Creating incidents

### Via Slack

As you may have seen from the [Slack Responder Guide](https://docs.firehydrant.com/docs/slack-responder-guide), FireHydrant provides a Slackbot so you can conduct incidents end-to-end directly from your chat tool. There are multiple ways you can start an incident from within Slack:

#### Slack commands

FireHydrant's Slackbot can be interacted with using any one of three command aliases: `/fh`, `/firehydrant`, or `/incident`.

You can open the same new incident modal as above by running `/fh new`, and you can also get visual buttons to click by running either `/fh` by itself or `/fh help`.

> 📘 Note:
>
> At FireHydrant, we have a saying which is "Anyone can call the fire department." All of your users in Slack can declare incidents regardless of whether they have FireHydrant licenses.

#### From existing threads and messages

1. From any channel or thread, click the ellipses in Slack next to a message. There will be an option to open a new incident as well as add the message to an existing incident.

<Image alt="Declaring an incident from a message/thread" align="center" width="650px" src="https://files.readme.io/9c0738b-image.png">
  Declaring an incident from a message/thread
</Image>

2. Click **Open a new Incident**. This pops open the same declaration modal as you've configured, but this time, FireHydrant automatically inserts a link to the message in the description of the incident. Fill in information as needed and declare the incident.

<Image alt="Incident type emoji settings" align="center" width="650px" src="https://files.readme.io/ca85121fbfe8ffba917dd747a2bda7eeb2fa07e0b9eb07b504c421b5c2616afb-CleanShot_2025-01-07_at_18.01.57.png">
  Incident type emoji settings
</Image>

In addition to the message shortcut above, you can now configure emojis that map to specific [Incident Types](https://docs.firehydrant.com/docs/incident-types) in your Slack settings. When responding to any message with that emoji, FireHydrant will respond with a message and you can press the button to open a modal with pre-filled values.

<Image alt="Starting the incident creation process from an emoji" align="center" width="650px" src="https://files.readme.io/2f7038c833bea97baad7f647ceb075b156c7711bcceebb023ebf660aabd11efc-1.png">
  Starting the incident creation process from an emoji
</Image>

#### Slack app home

<Image alt="Opening a new incident from the FireHydrant Slack app home tab" align="center" src="https://files.readme.io/3c4378f-Untitled-2023-08-09-1614.png">
  Opening a new incident from the FireHydrant Slack app home tab
</Image>

1. In Slack, navigate to **Apps** and look for **FireHydrant**.
2. Click on the **Home** tab if you're not already there, and you should see the "Open a new incident" button.

### Via Web UI

Unlike Slack, in order to declare an incident from the web UI, you must have a FireHydrant account and be logged in. To open a new incident from the FireHydrant Web UI:

1. From anywhere within the app, you should see the **Declare Incident** button on the top right. Click on it.
2. You'll be taken to the declaration form. From here, you can either choose a pre-defined [Incident Type](https://docs.firehydrant.com/docs/incident-types) or you can pick and choose fields to fill ad-hoc.
3. Provide the **Incident Name** to declare an incident. A name for the incident is required always, but you can [customize the rest of the fields](https://docs.firehydrant.com/docs/incident-fields).
   1. Short descriptions for each of these fields appear on the web UI; read these descriptions, or click the  :information\_source:  icon for helper text describing each field.

<Image alt="Declare incident from in the Web UI" align="center" width="80% " src="https://files.readme.io/b615458-Screenshot_2023-10-13_at_6.27.50_PM.png">
  Declare incident from in the Web UI
</Image>

After you add and fill out any relevant fields, click **Declare incident** to create the incident.

> 📘 Pro-Tip:
>
> Assuming you're logged in, you can quickly access the web declaration form by visiting [https://fh.new](https://fh.new). This will automatically take you to the declaration form in the Web UI, using whichever account you're logged into and whichever organization is your default org. Pretty convenient, huh? :smiley:

### Via Signals

FireHydrant offers [Signals](https://docs.firehydrant.com/docs/signals-introduction), and built-in alerting and on-call management platform within FireHydrant. Any inbound webhooks from external sources can be matched on [Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules) configured by teams to become alerts.

When responders are paged/alerted, they can respond to the alert by escalating/promoting it into an incident.

[Read more about this capability](https://docs.firehydrant.com/docs/signals-promoting-alerts-into-incidents).

### Via Alert Routing

For any 3rd-party alerting providers, Alert Routing on FireHydrant lets you receive webhooks or alerts from various sources (native integration or custom) to make decisions on FireHydrant.

You can configure four reactions to each inbound alert on FireHydrant:

1. Automatically start an incident
2. Notify specific Slack channels and await manual confirmation before starting
3. Log the alert, but neither notify nor start an incident
4. Ignore the alert and do nothing

<Image align="center" width="50% " src="https://files.readme.io/68a241b-alert-routing-diagram.png" />

When configuring these decisions, you can make decisions based on numerous parameters within the incoming request body, depending on the integration. For more information, visit [Alert Routing docs](https://docs.firehydrant.com/docs/alert-routing).

If you have inbound alerts configured, then you will see them appear in your default alerting channel configured in Slack like so:

<Image alt="Example failed check from Checkly alerting the Slack channel" align="center" src="https://files.readme.io/2298790-image.png">
  Example failed check from Checkly alerting the Slack channel
</Image>

### Via Integrations

Specific integrations like [Zendesk](https://docs.firehydrant.com/docs/zendesk-integration) and Backstage have modules or plugins within their tools that FireHydrant has worked to build.

For example, you can declare incidents directly from your Zendesk portal via the FireHydrant App:

<Image alt="FireHydrant App in Zendesk" align="center" src="https://files.readme.io/87d9544-Untitled-2023-08-09-1614.png">
  FireHydrant App in Zendesk
</Image>

The same is available via the Backstage integration as well, and we have plenty of other integrations on the future roadmap.

### Via API

Almost everything you do on FireHydrant is programmatically accessible by our [robust API](https://developers.firehydrant.com/#/). To declare an incident via API, use [POST /incidents](https://developers.firehydrant.com/#/operations/postV1Incidents) remembering your authorization headers and request body. Here's an example:

```curl
curl --request POST \
  --url https://api.firehydrant.io/v1/incidents \
  --header 'Authorization: fhb-56e00f351d5bc767b32a02e9c16a6809' \
  --header 'Content-Type: application/json' \
  --data '{
  "name": "My API-induced incident",
  "description": "This is an example API call to create an incident",
  "severity": "TRIAGE",
  "impacts": [
    {
      "type": "service",
      "id": "12345-my-service-id",
      "condition_id": "12345-my-condition-id"
    }
  ]
}'
```

## Configuring declaration

For both the Web UI as well as the Slack form, FireHydrant offers the ability to customize what you see and which fields are required when declaring an incident.

To read more about this, visit [Incident Fields](https://docs.firehydrant.com/docs/incident-fields) documentation.

## Next Steps

* [Adding Responders](https://docs.firehydrant.com/docs/adding-responders)
* Learn more about [Alert Routing](https://docs.firehydrant.com/docs/alert-routing)
* [Managing Tasks](https://docs.firehydrant.com/docs/managing-tasks)