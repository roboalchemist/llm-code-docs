# Source: https://docs.apify.com/sdk/python/docs/concepts/webhooks.md

# Source: https://docs.apify.com/platform/integrations/webhooks.md

# Source: https://docs.apify.com/sdk/python/docs/concepts/webhooks.md

# Source: https://docs.apify.com/platform/integrations/webhooks.md

# Source: https://docs.apify.com/sdk/python/docs/concepts/webhooks.md

# Source: https://docs.apify.com/platform/integrations/webhooks.md

# Source: https://docs.apify.com/sdk/python/docs/concepts/webhooks.md

# Source: https://docs.apify.com/platform/integrations/webhooks.md

# Webhook integration

**Learn how to integrate multiple Apify Actors or external systems with your Actor or task run. Send alerts when your Actor run succeeds or fails.**

***

Webhooks allow you to configure the Apify platform to perform an action when a certain system event occurs. For example, you can use them to start another Actor when the current run finishes or fails.

You can find webhooks under the **Integrations** tab on an Actor's page in https://console.apify.com/actors.

![Integrations tab in Apify Console](/assets/images/integrations-tab-ccd1902979bfea9812a6de7046ec6f04.png)

To define a webhook, select a system **event** that triggers the webhook. Then, provide the **action** to execute after the event. When the event occurs, the system executes the action.

Current webhook limitations

Currently, the only available action is to send a POST HTTP request to a URL specified in the webhook.

* https://docs.apify.com/platform/integrations/webhooks/events.md
* https://docs.apify.com/platform/integrations/webhooks/actions.md
* https://docs.apify.com/platform/integrations/webhooks/ad-hoc-webhooks.md
