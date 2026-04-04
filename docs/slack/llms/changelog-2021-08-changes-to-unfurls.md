Source: https://docs.slack.dev/changelog/2021-08-changes-to-unfurls

# Changes to unfurls

August 30, 2021

On September 1, 2021, the [`link_shared`](/reference/events/link_shared) event is changing. The change will happen for free teams on September 1, and will roll out to paid teams over the following weeks.

The [`chat.unfurl`](/reference/methods/chat.unfurl) method will also accept new arguments.

Changes to `link_shared` will help enable a smoother unfurl experience for apps that haven't yet been installed.

## What's changing {#changed}

The [`link_shared`](/reference/events/link_shared) event will now be sent **when a user types a link into the message composer**, in addition to when the message is **sent** to a channel.

As part of this change, two new fields will be included:

* `unfurl_id`, which identifies the link and can be used to supply the `chat.unfurl` method.
* `source`, an enumerated string that tells you whether the event happened in composer (`"source": "composer"`) or in a sent message (`"source": "conversations_history`).

A full payload for the `link_shared` event sent when a link is typed into the message **composer** is:

```json
{    "type": "link_shared",    "channel": "COMPOSER",    "is_bot_user_member": true,    "user": "Uxxxxxxx",    "message_ts": "Uxxxxxxx-909b5454-75f8-4ac4-b325-1b40e230bbd8-gryl3kb80b3wm49ihzoo35fyqoq08n2y",    "unfurl_id": "Uxxxxxxx-909b5454-75f8-4ac4-b325-1b40e230bbd8-gryl3kb80b3wm49ihzoo35fyqoq08n2y",    "source": "composer",    "links": [        {            "domain": "example.com",            "url": "https://example.com/12345"        },        {            "domain": "example.com",            "url": "https://example.com/67890"        },        {            "domain": "another-example.com",            "url": "https://yet.another-example.com/v/abcde"        }    ]}
```text

Note that `channel` in these messages represents the fact that this event comes from the message composer, not any particular channel for the message. If you make assumptions about the channel for `link_shared` events being a real channel, those assumptions won't work for the `COMPOSER` channel.

Similarly, the `message_ts` for these events will **not** be a valid timestamp for any method besides `chat.unfurl`.

As mentioned, `chat.unfurl` will continue to accept the combination of `channel` and `ts` you find in these `link_shared` events, even though they're not strictly channels or timestamps. But you can also use the `unfurl_id` and `source` parameters (if you use one, you must use both together) to call `chat.unfurl`.

## How to respond or prepare {#prepare}

If you don't want to make use of new unfurl experiences, you can filter out `link_shared` events from the `source` of `composer`.

If you do wish to use new unfurls, check the `source` and make sure your logic doesn't assume that `channel` and `message_ts` are valid channels and timestamps.

## What happens if I do nothing? {#happens}

Your app could receive invalid channel errors if it tries to use Slack APIs in response to receiving a `link_shared` event.

## When is this happening {#when}

This change happens on September 1, 2021 for free teams, with a gradual rollout to paid teams over the next month.

## Tags:

* [Announcement](/changelog/tags/announcement)
