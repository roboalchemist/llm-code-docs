# Source: https://docs.verba.ink/guides/discord-command-reference.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Discord command reference

> Exact slash command behavior, permissions, and expected responses.

## Command availability

Verba can register these slash commands:

* `/activate-channel`
* `/remove-channel`
* `/reset`
* `/generate`
* `/dashboard`
* `/vc-join`
* `/vc-leave`
* `/ping`

Each command can be toggled on/off in your Discord module settings.

## Permission matrix

| Command             | Where     | Permission requirement                      |
| ------------------- | --------- | ------------------------------------------- |
| `/activate-channel` | Server    | Administrator                               |
| `/remove-channel`   | Server    | Administrator                               |
| `/reset`            | DM        | None (user-scoped DM reset)                 |
| `/reset`            | Server    | Administrator, server owner, or bot owner   |
| `/generate`         | Server/DM | Command enabled + image generation enabled  |
| `/dashboard`        | Server/DM | Command enabled                             |
| `/vc-join`          | Server    | Voice engine enabled + voice channel access |
| `/vc-leave`         | Server    | Voice engine enabled                        |
| `/ping`             | Server/DM | Command enabled                             |

## Command behavior details

### `/activate-channel`

* Marks the current channel as AI-enabled.
* In AI-enabled channels, bot can reply without mentions.

### `/remove-channel`

* Removes the current channel from AI-enabled list.

### `/reset`

* In DM: clears DM conversation memory for that user context.
* In server: clears server conversation memory for that bot/server context.

### `/generate`

* Generates an image from prompt.
* Optional reference image is supported.
* If image generation is disabled on the bot, command returns a disabled message.

### `/dashboard`

* Returns the dashboard URL.

### `/vc-join`

* Joins the requester's voice channel (or selected voice channel parameter).
* Fails if bot lacks voice permissions or voice runtime dependencies.

### `/vc-leave`

* Leaves current voice channel if connected.

### `/ping`

* Health/status check command with latency output.

## Command toggle behavior

When a command is disabled in dashboard:

* Invocation returns a disabled-command response.
* Command registration may take a short delay to reflect in Discord command picker.

## Common command errors

<AccordionGroup>
  <Accordion title="This command is disabled for this bot">
    Re-enable the command in Discord module -> Slash Command Toggles.
  </Accordion>

  <Accordion title="You need Administrator permission">
    Server-only administrative commands require admin privileges in that guild.
  </Accordion>

  <Accordion title="This command can only be used in a server channel">
    Channel-management commands are server scoped and not available in DMs.
  </Accordion>

  <Accordion title="Image provider unavailable">
    Temporary upstream issue. Retry shortly or simplify prompt/reference image.
  </Accordion>

  <Accordion title="Voice runtime unavailable">
    Worker/runtime dependency issue. Restart worker and verify voice deps.
  </Accordion>
</AccordionGroup>

## Custom message templates

You can customize command/error text in the **Custom Messages** page.

Frequently used template variables:

* `{messagesPerMinute}`
* `{contextLabel}`
* `{channelMention}`
* `{verb}`
* `{user}`

<Card title="Discord Deployment" icon="message" href="/guides/discord">
  Setup guide for connection, intents, profiles, and server routing.
</Card>

Built with [Mintlify](https://mintlify.com).
