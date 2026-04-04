Source: https://docs.slack.dev/tools/bolt-js/concepts/message-listening

# Listening to messages

To listen to messages that [your app has access to receive](/messaging/retrieving-messages/#permissions), you can use the `message()` method which filters out events that aren’t of type `message`. A `message()` listener is equivalent to `event('message')`.

The `message()` listener accepts an optional `pattern` parameter of type `string` or `RegExp` object which filters out any messages that don’t match the pattern.

```text
// This will match any message that contains 👋app.message(':wave:', async ({ message, say }) => {  // Handle only newly posted messages here  if (message.subtype === undefined    || message.subtype === 'bot_message'    || message.subtype === 'file_share'    || message.subtype === 'thread_broadcast') {    await say(`Hello, <@${message.user}>`);  }});
```text

## Using a RegExp pattern {#using-regexp}

A RegExp pattern can be used instead of a string for more granular matching.

All of the results of the RegExp match will be in `context.matches`.

```text
app.message(/^(hi|hello|hey).*/, async ({ context, say }) => {  // RegExp matches are inside of context.matches  const greeting = context.matches[0];  await say(`${greeting}, how are you?`);});
```text

## Filtering on event subtypes {#filtering-event-subtypes}

You can filter on subtypes of events by using the built-in `subtype()` middleware. Common message subtypes like `message_changed` and `message_replied` can be found [on the message event page](/reference/events/message#subtypes).

```text
// Import subtype from the packageconst { App, subtype } = require('@slack/bolt');// Matches all message changes from usersapp.message(subtype('message_changed'), ({ event, logger }) => {  // This if statement is required in TypeScript code  if (event.subtype === 'message_changed'    && !event.message.subtype    && !event.previous_message.subtype) {    logger.info(`The user ${event.message.user} changed their message from ${event.previous_message.text} to ${event.message.text}`);  }});
```text
