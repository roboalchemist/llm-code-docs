# Source: https://developers.make.com/custom-apps-documentation/app-components/webhooks/dedicated.md

# Dedicated

{% hint style="info" %}
Even when a service sends all data to only one URL registered for the user, it's a dedicated webhook. It's up to you to determine how the app will handle incoming data. Over 90% of services use dedicated webhooks so be cautious when using a shared webhook.
{% endhint %}

## Types of dedicated webhooks

### Attached

For an [attached dedicated webhook](https://developers.make.com/custom-apps-documentation/app-components/webhooks/dedicated/attached), the new URL address that is created is automatically registered to the service using an attach procedure and can be unregistered using detach procedure.

If there is an endpoint available in the API for registration of the webhook, the attach directive should be implemented.

### Not attached

For a [dedicated webhook that is not attached](https://developers.make.com/custom-apps-documentation/app-components/webhooks/dedicated/not-attached), the new URL address that is created has to be registered manually by the user. The user copies the URL address and pastes it to the webhook's settings of the web service.

If there is no attach directive available in the API but the web service allows setting up a webhook manually, implement the dedicated webhook without the attach directive.
