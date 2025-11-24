# Source: https://docs.chatling.ai/ai-agent/actions/cal-booking.md

# Cal.com Booking Widget

The Cal.com Booking Widget action embeds your Cal.com scheduler directly inside the chat, so users can view real-time availability and book without leaving the conversation.

<img src="https://chatling-assets.b-cdn.net/cal-com-action-ai-agent.jpg" width="350" alt="Cal.com Booking Widget action" />

## Configuration

### `Action Name`

A short, specific identifier that tells the Agent what this action does (e.g. best\_sellers\_buttons, support\_button).

### `When to Use`

A detailed description of what the action does and when it must be used.

When applicable, you can specify one or more of the following:

* **Positive cues/phrases**: Example utterances and keywords that signal this action (include a few variations).
* **Preconditions**: What must be true before running.
* **Do not use when**: Explicit exclusions to avoid false triggers.

<img src="https://chatling-assets.b-cdn.net/action-when-to-use-field.jpg" width="450" alt="When to use option" />

### `Frequency`

Specify how often the Agent can invoke this action to avoid overusing it, e.g `Once per chat` or `Whenever applicable`.

<img src="https://chatling-assets.b-cdn.net/action-frequency-field.jpg" width="450" alt="Frequency option" />

### `Widget`

Configure the widget's settings and appearance.

* **Event link**: The link to the Cal.com event page, such as `https://cal.com/rick/get-rick-rolled`.
* **Layout**: The layout of calendar, such as `Month`, `Week`, or `Column`.
* **Hide event type details**: Whether to hide the details of the event.
* **Pre-fill information**: The information to pre-fill in the booking form, such as `Name`, `Email`, and `Phone`.

### `Save Booking Information`

Save the data from the booking in variables to re-use later in the chat, if applicable.
