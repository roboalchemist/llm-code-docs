# Source: https://configcat.com/docs/integrations/datadog.md

# Datadog - Monitor your feature flags events

## Overview[​](#overview "Direct link to Overview")

Monitor feature flag events in real-time. Feature flag changes will appear as events in Datadog, tagged with relevant product, config, and environment details.

![Feature flag events logged to Datadog](/docs/assets/datadog-event_192dpi.png)

## Installation[​](#installation "Direct link to Installation")

1. Have a [Datadog subscription.](https://www.datadoghq.com/)
2. Get a [Datadog API Key.](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys)

![Datadog API Key](/docs/assets/datadog-apikey_192dpi.png)

3. Open the [integrations tab](https://app.configcat.com/product/integrations) on ConfigCat Dashboard.
4. Click on Datadog's **Connect** button and set your Datadog API key.
5. OPTIONAL - Set the proper site of your Datadog account. [More about Datadog site](https://docs.datadoghq.com/getting_started/site/).
6. You're all set. Go ahead and make some changes on your feature flags, then check your Events in Datadog.

## Un-installation[​](#un-installation "Direct link to Un-installation")

1. Open the [integrations tab](https://app.configcat.com/product/integrations) on ConfigCat Dashboard.
2. Click on Datadog's **Connected** button.
3. Select the connection from the **Connected** dropdown.
4. Click the **Disconnect** button in the edit dialog.
5. Click **Yes** in the confirmation dialog.

## Event details[​](#event-details "Direct link to Event details")

Every event sent to Datadog by ConfigCat has a *source* property of `configcat` and *tagged* with the `product_name`, `config_name` and `environment_name` where the change has happened.

### Searching for Events[​](#searching-for-events "Direct link to Searching for Events")

For example here is how to search for events that happened in the production environment: `sources:configcat production`

![Filtering feature flag change events](/docs/assets/datadog-filtering_192dpi.png)

## Useful Resources[​](#useful-resources "Direct link to Useful Resources")

* [How to send feature flag change notifications to DataDog - Blog Post](https://configcat.com/blog/2021/03/17/connect-configcat-and-datadog/)
* [ConfigCat Integrations API](https://configcat.com/docs/api/reference/integrations/)
