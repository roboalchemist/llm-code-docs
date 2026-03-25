# Source: https://docs.envzero.com/changelogs/2024/05/webhook-notifications.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🪝 Webhook Notification Target

> Webhooks are now supported as a notification target in env zero, allowing for powerful and secure reactions to events on your account. Follow the documentation to set up a new webhook notification target under organization settings.

We are happy to announce that webhook is now supported as a notification target!

Webhooks provide a powerful and secure way to react to different events on your env zero account.

To set up a new webhook notification target, go to the Notifications menu under the organization settings. Next, create a new notification, and under Type choose Webhook:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/05/6d49247-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=54025888adfd9868abe10015817129b3" width="581" height="608" data-path="images/changelogs/2024/05/6d49247-image.png" />
</Frame>

Enter your webhook details. Please note that an HTTPS connection is required for the URL. If you're experimenting or need a temporary solution, services like [webhook.site](https://webhook.site) can be useful. See [our doc](/guides/integrations/notifications/webhooks) for more details.

Once created, you can send a test event to your webhook URL by clicking 'Test endpoint' to ensure everything is working smoothly.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/05/da1ca66-16e0452-screenshot_2024-05-15_at_16.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=6415a2ad84e273988393be2f88a6b12f" width="1722" height="948" data-path="images/changelogs/2024/05/da1ca66-16e0452-screenshot_2024-05-15_at_16.png" />
</Frame>

For further details, [check out our detailed documentation](/guides/integrations/notifications/webhooks).

We hope you find this new feature valuable and are sure that it will enhance your experience. If you have any questions or need further assistance, feel free to reach out!

Built with [Mintlify](https://mintlify.com).
