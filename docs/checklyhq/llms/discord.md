# Source: https://checklyhq.com/docs/integrations/alerts/discord.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Alerts to Discord

> Configure Discord integration to receive real-time alerts from Checkly monitors

Checkly integrates with [Discord](https://discord.com/) and can
deliver failure, degradation, and recovery messages to any project in your Discord server / channel.

1. First, create a **Webhook**. Log in to Discord and go to "Server Settings" > "Integrations" and click "Create Webhook".

   <img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/discord/discord_step1.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=1cefece198bd1c7f2f34cebe0a0d752a" alt="setup checkly discord step 1" width="1019" height="736" data-path="images/docs/images/integrations/discord/discord_step1.png" />

2. **Choose a name** for your integration like "Checkly" and [add this Checkly icon](https://cdn.checklyhq.com/logos/fat_racoon_square.png).
   Click the "Copy the Webhook URL" to...well...copy the Webhook URL

   <img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/discord/discord_step2.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=1f5747efa155a37f3ade35c8517ec79a" alt="setup checkly discord integration step 2" width="1019" height="736" data-path="images/docs/images/integrations/discord/discord_step2.png" />

3. Log in to Checkly and navigate to [Alert Settings](https://app.checklyhq.com/alert-settings/).
   Click the "Add more channels" button, find Discord on the list, and click "Add channel".

   <img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/discord/discord_step3.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=b5826813db30a8a7bf712323765dc267" alt="setup checkly discord integration step 3" width="1085" height="728" data-path="images/docs/images/integrations/discord/discord_step3.png" />

4. Give the alert channel a name and **paste the Webhook URL** in their respective input fields. You can now also tweak
   which alerts you want to be notified of and which checks or check groups should be subscribed to this channel.

   <img src="https://mintcdn.com/checkly-422f444a/0b4gCdAyz7Dv4O-Z/images/docs/images/integrations/discord/discord_step4.png?fit=max&auto=format&n=0b4gCdAyz7Dv4O-Z&q=85&s=c3cdce01b918b40e7786a6d3cb1f47c9" alt="setup checkly discord integration step 4" width="1035" height="700" data-path="images/docs/images/integrations/discord/discord_step4.png" />

   <Callout type="note">
     Note that we provide a preconfigured message payload but you are free to edit the payload and add more or different
     variables. Just click the "Edit payload" button and reference the "Help & variables tab".
   </Callout>

Congratulations! You have successfully integrated Checkly with Discord!

## Advanced Discord Configuration

### Custom Discord Alerts

For more control over Discord alert formatting, you can create custom webhook payloads using Discord's embed format:

```json  theme={null}
{
  "embeds": [
    {
      "title": "{{ALERT_TITLE}}",
      "description": "**Check**: {{CHECK_NAME}}\n**Location**: {{RUN_LOCATION}}\n**Response Time**: {{RESPONSE_TIME}}ms",
      "color": "{{#eq ALERT_TYPE 'ALERT_FAILURE'}}15158332{{else}}{{#eq ALERT_TYPE 'ALERT_DEGRADED'}}16776960{{else}}3066993{{/eq}}{{/eq}}",
      "fields": [
        {
          "name": "Error",
          "value": "{{CHECK_ERROR_MESSAGE}}",
          "inline": false
        },
        {
          "name": "Started At",
          "value": "{{STARTED_AT}}",
          "inline": true
        },
        {
          "name": "Location",
          "value": "{{RUN_LOCATION}}",
          "inline": true
        }
      ],
      "footer": {
        "text": "Checkly Monitoring"
      },
      "timestamp": "{{STARTED_AT}}",
      "url": "{{RESULT_LINK}}"
    }
  ]
}
```

### Discord Alert Colors

Use different colors to distinguish alert types:

* **Red (15158332)**: Failures and critical alerts
* **Orange (16776960)**: Degraded performance alerts
* **Green (3066993)**: Recovery notifications

### Discord Best Practices

* Use separate channels for different environments (production, staging, development)
* Configure appropriate notification settings to avoid alert fatigue
* Use Discord's thread feature for grouping related alerts
* Set up role mentions (@role) for critical alerts that require immediate attention


Built with [Mintlify](https://mintlify.com).