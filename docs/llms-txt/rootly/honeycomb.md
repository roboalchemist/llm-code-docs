# Source: https://docs.rootly.com/integrations/honeycomb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Honeycomb

> Receive alerts from Honeycomb's observability platform to trigger incidents, route to Slack, or page on-call teams.

Honeycomb can be configured to send events into Rootly as alerts. The alerts received on Rootly can then be routed to a Slack channel, used to initiate incidents, or used to page Rootly On-Call targets.

## Installation

### Establish Authentication

To set up Honeycomb, you will need to first log into Honeycomb as an **admin user.**

Once logged in, make sure you are on the **environment** that you're looking to integrate with Rootly and select the **settings icon** ⚙️.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-1.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=e9650e9ff1c135c799c0cb8ecfe0a03b" width="862" height="258" data-path="images/integrations/honeycomb/images-1.webp" />
</Frame>

Then, select the **API Keys** tab > **Configuration** > **Create Configuration API Key**.

<Warning>
  Honeycomb has two types of API keys: **Configuration** and **Management** API keys.

  The one Rootly requires is a **Configuration** (aka. **Environment-level**) API key.
</Warning>

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-2.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=c1142982e33d0b737c7081b0e759d0e1" width="869" height="434" data-path="images/integrations/honeycomb/images-2.webp" />
</Frame>

In the **Create API Key** modal, enter a description `Name` and check **any of the permissions**. Once complete, go ahead and save the API key.

<Warning>
  Integrating with an API key is purely to authenticate Rootly as a client to your Honeycomb environment, so we can generate a **webhook URL** + **secret** combination that is exclusive to your organization. Rootly will NOT be making any direct calls to Honeycomb to read or write. Rootly will only be ingesting incoming alerts from Honeycomb.

  The Honeycomb integration will be moved to [Rootly Alert Sources](https://rootly.com/account/alerts?tab=alert-sources "Rootly Alert Sources"), so this step will eventually be obsolete.
</Warning>

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-3.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=3fc3d5ed7c1044b0cfe6566303ebbaaa" width="873" height="723" data-path="images/integrations/honeycomb/images-3.webp" />
</Frame>

Now, copy your newly generated API key from Honeycomb and **paste it into the Honeycomb integration modal in Rootly** and select **Connect**.

<Note>
  To get to the Honeycomb integration modal, you'll need to be an **Admin** user in Rootly and navigate to **Integrations** > **Honeycomb** > **Setup**
</Note>

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-4.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=a07449aa330ca6af1f4d05fcf33cc1f8" width="865" height="304" data-path="images/integrations/honeycomb/images-4.webp" />
</Frame>

A successful integration will give you the **webhook URL** + **secret** combination needed to configure webhooks in your Honeycomb account.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-5.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=500c847c4446c757ac9a06bbd277eb90" width="871" height="583" data-path="images/integrations/honeycomb/images-5.webp" />
</Frame>

### Create a Webhook

Now that you have your organization specific **webhook URL** + **secret** combination, let's go to your Honeycomb account to create a webhook.

Once logged in, navigate to the **Team settings** page.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-6.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=5a83e8c6ad33b79845b13e754c1c0891" width="890" height="893" data-path="images/integrations/honeycomb/images-6.webp" />
</Frame>

Then select the **Integrations** tab and click on **Add Integration**.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-7.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=05884bce0f47acc7d5780fbe1c01465e" width="887" height="807" data-path="images/integrations/honeycomb/images-7.webp" />
</Frame>

In the Add Integration modal, set the `Provider` to `Webhook` and give it a description `Name` (e.g. Page Engineering On-Call, Page Infrastructure Team, Rootly Alerts, etc.).

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-8.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=a63711de1b7e418c02e7d2160f399e83" width="883" height="540" data-path="images/integrations/honeycomb/images-8.webp" />
</Frame>

The value you put in the `Webhook URL` field will depend on what type of alert you want this particular webhook to send to Rootly.

**For General Alert (aka. Non-Paging Alert)**

Non-paging alerts will arrive in Rootly's [Alerts page](https://rootly.com/account/alerts "Alerts page") but will not page anyone.

Honeycomb requires the *Webhook URL* and *secret* from Rootly to be included in the Webhook URL field in the following format:

```txt Webhook URL theme={null}
https://webhooks.rootly.com/webhooks/incoming/honeycomb_webhooks?secret=<enter_sercret_here>  
```

<Note>
  The *webhook URL* and *secret* can be obtained from your Honeycomb integration page in Rootly (**Integrations** > **Honeycomb** > **Configure**).
</Note>

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-9.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=93bdfdcba9450fa50444052ed83742f7" width="890" height="548" data-path="images/integrations/honeycomb/images-9.webp" />
</Frame>

<Warning>
  Yes, the *secret* need to exist both as part of the `Webhook URL` path AND in the `Shared Secret` field. Make sure that the secret in both places are exactly the same.
</Warning>

**To Page Rootly On-Call (aka. Paging Alert)**

Paging through Rootly On-Call also relies on webhook alerts. The main difference being the inclusion of a notification target in the query parameter.

The notification target consists of the following:

* `resource_type` - this defines the Rootly resource type that will be used for paging.
  * The following are the available values: `User` | `Group` (Team) | `EscalationPolicy` | `Service`
* `resource_id` - this specifies the exact resource that will be targeted for the page.
  * The id of the resource can be found when editing each resource.

Enter the *webhook URL,* *secret* and *notification target* in the following format in the `Webhook URL` field in Honeycomb:

```txt Webhook URL theme={null}
https://webhooks.rootly.com/webhooks/incoming/honeycomb_webhooks/notify/<resource_type>/<resource_id>?secret=<enter_sercret_here>  
```

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-10.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=7291ada0ecaa70cbdad1fedf0f363cc2" width="888" height="545" data-path="images/integrations/honeycomb/images-10.webp" />
</Frame>

<Warning>
  Yes, the *secret* need to exist both as part of the Webhook URL path AND in the Shared Secret field. Make sure that the secret in both places are exactly the same.
</Warning>

## Uninstall

You can **uninstall** this integration in the integrations panel by clicking **Configure > Delete.**

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/DEGWl8qg20zbzmSF/images/integrations/honeycomb/images-11.webp?fit=max&auto=format&n=DEGWl8qg20zbzmSF&q=85&s=f8d897727fb6d6a665d761654528eea3" width="890" height="602" data-path="images/integrations/honeycomb/images-11.webp" />
</Frame>

Ensure that you delete your webhooks in Honeycomb as well. Deleting the integration in Rootly will NOT stop Honeycomb from sending Rootly alert events.


Built with [Mintlify](https://mintlify.com).