Source: https://docs.slack.dev/changelog/2018-truncating-really-long-messages

# Truncating really long messages

April 1, 2018

We're tidying up the character limits on the `text` field of posted messages.

Beginning April 25th, 2018, we truncated messages sent to Slack that are longer than 500,000 characters. As of July 12, 2018, we truncate at 100,000 characters.

Over the [next several weeks](#when), we slowly lowered the allowed character count.

On **August 12, 2018** we started truncating messages containing more than **40,000 characters**.

## What's changing {#now}

The `text` field of messages is now limited to 100,000 characters, with the limit becoming 40,000 characters in August 2018.

Previously, we asked you only to keep messages under 4,000 _bytes_ but left the consequences ambiguous.

Know now that messages with tremendously long `text` bodies will be _truncated_ to (eventually) up to 40,000 characters.

When we truncate, we provide you a [warning](#warnings) about it. As with previous behavior, in addition to truncation you may find long messages automatically broken into multiple messages.

This behavior applies to all methods of posting messages to Slack: [`chat.postMessage`](/reference/methods/chat.postMessage), [`chat.postEphemeral`](/reference/methods/chat.postEphemeral), [interactive message](/legacy/legacy-messaging/legacy-making-messages-interactive) and [slash command](/interactivity/implementing-slash-commands) response URLs, [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks), and other ways to post .

On August 14, 2018 we'll reduce the maximum limit to 40,000 after a gradually lowering limits over several weeks.

## How to respond or prepare {#prepare}

To prepare for these changes:

* Measure how long your messages can be. It's a good thing to know.
* Send shorter messages. 40,000 characters is a lot for busy humans to read.
* Split intentionally long messages into multiple postings of no more than 40,000 characters each, preferably less.
* Or, you could do _nothing_ and just allow your really long messages to truncate.

Watch for the [warnings](#warnings) we send you when messages are truncated.

## The message_truncated warning {#warnings}

Here's an abbreviated example of the response you'd receive from `chat.postMessage` when attempting to send more than 40,000 characters of text:

```json
{    "text": "If one examines realism, one is faced with a choice: either reject structural discourse or conclude that language serves to marginalize the Other. The primary theme of Abian's[1] essay on realism is the genre, and subsequent failure, of predeconstructivist reality.... and so on for 40,000 characte",    "response_metadata": {        "messages": [            "[WARN] Your message was truncated but still posted. The `text` field accepts up to 40,000 characters."        ],        "warnings": [            "message_truncated"        ]    }}
```text

Track `message_truncated` warnings to understand how often your messages truncate and adjust your approach as necessary.

## What happens if I do nothing? {#nothing}

Your messages will still post. They'll truncate at 40,000 characters and potentially split into multiple messages.

You'll receive the [warnings](#warnings) above.

It's probably best to adjust your message content instead.

## When is this happening? {#when}

We're rolling message truncation out gradually.

On April 25, 2018, we began truncating messages greater than 500,000 characters.

On May 9, 2018, we ratcheted truncation down to 200,000 crafty characters.

On July 12, 2018, messages began truncating at 100,000 characters.

Finally, on August 14, 2018, we began truncating messages greater than 40,000.

Have a use case for messages over 40,000 characters we should hear about or other questions and concerns? Let us know.

## Tags:

* [Announcement](/changelog/tags/announcement)
