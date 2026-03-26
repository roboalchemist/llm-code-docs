# Source: https://checklyhq.com/docs/integrations/incident-management/statuspage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating StatusPage

> Configure StatusPage integration to automatically open incidents when Checkly monitors fail

Checkly's webhooks can be used to automatically open incidents with [StatusPage](https://www.atlassian.com/software/statuspage). Assuming you already have your status page set up, the setup is as follows:

1. First of all, ensure you have an API key available for your status page. In case you don't, [create a new one](https://support.atlassian.com/statuspage/docs/create-and-manage-api-keys/). You will also need to make a note of your status page's id.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/statuspage/statuspage-api-page.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=98b3dfb17f125e05438212666d0d2891" alt="status page api details page" width="2310" height="1558" data-path="images/docs/images/integrations/statuspage/statuspage-api-page.png" />

2. Next up, navigate to the Alert Settings tab on Checkly and add a new channel.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/statuspage/statuspage_add_alert.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=029c67e99b75d5031d890194382b07c8" alt="checkly create alert" width="2100" height="886" data-path="images/docs/images/integrations/statuspage/statuspage_add_alert.png" />

3. Select `Webhook`.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/statuspage/statuspage_alert_channels.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=91cd0442f815d4cfa6e220796d5dca52" alt="checkly create webhook for statuspage" width="2170" height="960" data-path="images/docs/images/integrations/statuspage/statuspage_alert_channels.png" />

4. Configuring the webhook, enter `POST` as method and `https://api.statuspage.io/v1/pages/<YOUR_PAGE_ID>/incidents` as URL. The body needs to be configured as shown in StatusPage's [official documentation](https://developer.statuspage.io/#operation/postPagesPageIdIncidents).

An example could be:

```json  theme={null}
{
  "incident": {
    "name": "{{ALERT_TITLE}}",
    "status": "investigating",
    "impact_override": "critical",
    "metadata": {},
    "deliver_notifications": true,
    "auto_tweet_at_beginning": false,
    "auto_tweet_on_completion": false,
    "auto_tweet_on_creation": false,
    "auto_tweet_one_hour_before": false,
    "backfill_date": "string",
    "backfilled": false,
    "body": "Something broke :(",
    "components": {},
    "component_ids": [],
    "scheduled_auto_transition": false
  }
}
```

Where the `name` field will be set to the title of the Checkly alert. See all [available alert variables](/integrations/alerts/webhooks#using-variables).

<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/integrations/statuspage/statuspage_body_url.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=8b15df4607e399df96e1fbcb7047a4b5" alt="checkly statuspage webhook body and url" width="2210" height="1270" data-path="images/docs/images/integrations/statuspage/statuspage_body_url.png" />

5. You will also need to provide your StatusPage API key in the `Authorization` header in the Headers tab, as well as select on which status the webhook should fire ("when a check fails", in this case), and which checks/groups should subscribe to the webhook. Subscribed checks and groups will trigger the webhook and open an incident.

<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/integrations/statuspage/statuspage_header_auth.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=664a0e8e11bad7408e9abe916ff4d321" alt="checkly webhook authorization header for statuspage" width="2172" height="1334" data-path="images/docs/images/integrations/statuspage/statuspage_header_auth.png" />

You are done! When a subscribed check fails, an incident will be opened on StatusPage:

<img src="https://mintcdn.com/checkly-422f444a/pk96p0t2gChABUbF/images/docs/images/integrations/statuspage/statuspage_end_result.png?fit=max&auto=format&n=pk96p0t2gChABUbF&q=85&s=cb656eb6c990832a69ad522a29c8e22a" alt="checkly statuspage integration end result" width="1758" height="1430" data-path="images/docs/images/integrations/statuspage/statuspage_end_result.png" />

<Callout type="note">
  Note that currently, automatically resolving existing incidents on check recovery is not supported.
</Callout>

Congratulations! You have successfully integrated Checkly with StatusPage!


Built with [Mintlify](https://mintlify.com).