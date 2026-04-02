Source: https://docs.slack.dev/changelog/2017/05/01/rethinking-channel-entrance-and-exit-events-and-messages

# Rethinking channel entrance and exit events and messages

May 1, 2017

We've long delivered a [message subtype event](/reference/events/message) to everyone in a channel as members come and go.

As a _message_, its main purpose is to communicate facts to _users_ but it was never a very good vehicle for communicating these facts to bots and applications.

We're introducing new, more frugal logic behind when Slack dispatches [`message.channel_join`](/reference/events/message/channel_join) and [`message.channel_leave`](/reference/events/message/channel_leave) [message subtype](/reference/events/message) events in the [RTM API](/legacy/legacy-rtm-api) and [Events API](/apis/events-api/).

If you've relied on these events for programmatic notice when members leave or join a channel, we've got new, strongly structured signals for you to subscribe to and consume instead, [`member_joined_channel`](/reference/events/member_joined_channel) and [`member_left_channel`](/reference/events/member_left_channel).

## What's changing? {#whats-changing}

We're adding some new events ([additive](#additive)) and altering the frequency of others ([mutative](#mutative)).

### Additive {#additive}

Who doesn't like distinguished events describing specific activity in the [Events API](/apis/events-api/) and [RTM API](/legacy/legacy-rtm-api)? Introducing two star-crossed events:

* [`member_joined_channel`](/reference/events/member_joined_channel)
* [`member_left_channel`](/reference/events/member_left_channel)

Here's an example delivery sent through the Events API for the new `member_joined_channel` event. You'll find the `member_left_channel` event has entirely the same shape, form, and data. It just has its own event `type`, telling a different part of the same old story.

```json
{    "token": "your_lovely_verification_token",    "team_id": "T123ABC456",    "api_app_id": "A123ABC456",    "event": {        "type": "member_joined_channel",        "user": "U123ABC456",        "channel": "C123ABC456",        "channel_type": "C",        "event_ts": "1493335475.238488"    },    "type": "event_callback",    "authed_users": [        "U2222222222"    ],    "event_id": "Ev123ABC456",    "event_time": 1493335475}
```text

Let's look at the most pertinent fields in more detail. These events tell you 4 of the 5 Ws.

* _Who_: The `user` value is a user ID belonging to the user that joined (or left) the channel.
* _What_: The event `type` tells you what happened, either a channel join or leave.
* _Where_: The `channel` value is the ID for a public channel or private channel (AKA `group`). The `channel` is where this event is happening.
* _When_: Just now!
* _Why_: Your app may never know.

Finally, there's a `channel_type` value yielding a single letter indicating the type of channel represented by `channel`:

* `C` - typically a public [channel](/reference/objects/channel-object)
* `G` - private channels (or [`groups`](/reference/objects/group-object)) return this `channel_type`

You can subscribe to these new events now and should see them begin to stream in the RTM API in the coming days.

### Mutative {#mutative}

In addition to these two new events, we're changing the frequency of user-facing messages concerning joining and leaving channels and conversations.

Though the [`message.channel_join`](/reference/events/message/channel_join) and [`message.channel_leave`](/reference/events/message/channel_leave) events still _exist_, they won't fire _every_ time a user joins and leaves a channel or conversation.

Slack will use a few factors like the size and activity of teams and channels to determine how few or many arrival and departure messages to broadcast to channels. Ultimately, we want channels to feel cozy for all kinds of conversation.

If atomic predictability is important to your app, we recommend relying on the new `member_joined_channel` and `members_left_channel` events instead.

## What isn't changing? {#what-isnt-changing}

These vintage [`message.channel_join`](/reference/events/message/channel_join) and [`message.channel_leave`](/reference/events/message/channel_leave) events will continue lingering around. You'll probably encounter more of them on smaller teams than you do on larger teams.

## How do I prepare? {#how-do-i-prepare}

Anything you're accomplishing with channel join and leave messages today should be improved by interpreting the new `member_joined_channel` and `member_left_channel` events instead.

If you're using the Events API, subscribe to these new events as either a bot subscription _or_ a team subscription. Team subscriptions require the corresponding `:read` scope — you'll need `channels:read` to receive events from public channels and `groups:read` from private channels.

If you're using the RTM API, you'll begin receiving both of these events as part of your typical stream of events.

## When is this happening? {#when-is-this-happening}

The new events are available in the RTM API and Events API now.

Changes to the frequency and delivery strategies of older `message.channel_join` and `message.channel_leave` events will vary team-to-team.

## Tags:

* [Announcement](/changelog/tags/announcement)
