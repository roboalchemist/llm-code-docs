# Source: https://docs.verba.ink/guides/discord.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Discord deployment

> Connect a verb to Discord and configure how, where, and when it responds.

## Questions this guide answers

* Why does my bot show "connection failed"?
* Why does the bot ignore messages in some channels?
* How do mention mode and AI-channel mode differ?
* Why does `/reset` work in DMs but fail in servers?
* Why does the bot say "application did not respond"?

## Before you connect

You need:

* A Discord application + bot user
* A valid bot token
* Privileged intents enabled in Discord Developer Portal

<Warning>
  Missing privileged intents is the most common cause of a bot that connects in
  dashboard UI but does not respond in Discord.
</Warning>

## Connect flow

<Steps>
  <Step title="Create bot in Discord">
    Use the Discord Developer Portal and create an app/bot.
  </Step>

  <Step title="Enable required intents">
    Enable Message Content and other required privileged intents in the bot settings.
  </Step>

  <Step title="Paste token in Verba">
    Open your verb's Discord module and connect with your token.
  </Step>

  <Step title="Invite the bot">
    Use the generated OAuth link to add it to your server.
  </Step>
</Steps>

## How response routing works

In server channels, a connected verb responds when at least one condition is true:

* The verb is directly mentioned
* The channel is marked as an AI channel
* A training keyword match is detected

It does not respond when:

* Another bot is speaking (bot messages are ignored)
* Message includes `@everyone`/`@here`
* Message role-pings the bot's role directly
* User is on ignore/ban controls

## Mention mode vs AI-channel mode

### Mention mode

* Best for shared channels where bot noise should stay low
* Users ping the bot to trigger responses

### AI-channel mode (`/activate-channel`)

* Bot can respond without mentions in that channel
* Best for support/help channels or dedicated AI rooms

Use `/remove-channel` to disable AI-channel behavior.

## Slash commands available

Default command set:

* `/activate-channel`
* `/remove-channel`
* `/reset`
* `/generate`
* `/dashboard`
* `/vc-join`
* `/vc-leave`
* `/ping`

You can enable/disable each command in Discord module settings.

## Permissions behavior

* `/activate-channel` and `/remove-channel` require Administrator permission.
* `/reset` in server requires Administrator, server owner, or bot owner.
* `/reset` in DM is user-scoped and available without server permissions.
* Voice commands require Voice Engine enabled for the verb.

## Profile and presence settings

You can configure:

* Activity type (playing/listening/watching/custom)
* Activity text
* Presence (`online`, `idle`, `dnd`, `offline`)
* Slash command toggles

<Note>
  Activity text over dashboard limits is rejected or clamped. Keep status text short.
</Note>

## Server management tools

In the Discord module you can:

* View current server count
* Refresh profile/server data
* Leave specific servers
* Copy invite link quickly

## Typical failure patterns

<AccordionGroup>
  <Accordion title="Connection failed during token setup">
    Usually invalid token format, token already linked to another verb, or Discord rate limiting. Retry with a fresh token and verify it is not already attached elsewhere.
  </Accordion>

  <Accordion title="The application did not respond">
    Most often command timeout or missing Discord permissions in that channel. Check command toggle, channel permissions, and voice/image settings for the invoked command.
  </Accordion>

  <Accordion title="Bot is online but does not answer messages">
    Check whether the message was a mention, in an AI channel, or matched training keywords. Also verify intents and that the sender is not ignored/banned.
  </Accordion>

  <Accordion title="/reset fails in server">
    Server reset requires elevated permissions (admin/server owner/bot owner). DM reset does not.
  </Accordion>
</AccordionGroup>

<CardGroup cols={2}>
  <Card title="Discord Command Reference" icon="terminal" href="/guides/discord-command-reference">
    Exact behavior and permission rules for each slash command.
  </Card>

  <Card title="Troubleshooting" icon="life-ring" href="/guides/troubleshooting">
    Fast fix checklist for connection failures, timeouts, and no-response bugs.
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
