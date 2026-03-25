# Source: https://docs.firehydrant.com/docs/slack-emoji-actions-aka-quick-declare.md

# Emoji Actions (AKA: Quick Declare)

React to a message in Slack to quickly get started on a new incident in FireHydrant

FireHydrant's Slack integration lets you quickly declare incidents when an emoji you assign is used in a message reaction. For example, if you'd like the :firecracker: emoji to quickly declare an incident for a customer-facing outage, you can configure this in your Slack settings in FireHydrant.

> 📘 Note:
>
> Only owners can modify Emoji Actions on a Slack configuration

1. Navigate to your Slack integration settings by going to [Organization Settings > Integrations](https://app.firehydrant.io/settings/integrations). Search for Slack and click the pencil icon to edit it.
2. Next, click "Emoji Preferences" tab.

<Image alt="Configuring emoji preferences for different incident types" align="center" src="https://files.readme.io/1ec5b90b6d7018f48c5e94aafbc19bb11572efbfd803acab6b3ff96a962c85d2-image.png">
  Configuring emoji preferences for different incident types
</Image>

3. Here, you can add a row (or several!) with the emojis you'd like to trigger a quick incident declaration. If you like, you can optionally assign an incident type that will be used when declaring the incident from Slack.

![](https://files.readme.io/614d194383448c28f53a28077d791354714835dbedf54e81645c72f721af3524-image.png)

When a user reacts to a message with the assigned emoji (IE: :firecracker:) – FireHydrant will quickly reply to the message with a button allowing the user to open a new incident quickly!