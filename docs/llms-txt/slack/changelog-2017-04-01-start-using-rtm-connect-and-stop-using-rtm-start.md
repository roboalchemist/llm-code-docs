Source: https://docs.slack.dev/changelog/2017/04/01/start-using-rtm-connect-and-stop-using-rtm-start

# Start using RTM connect and stop using RTM start

April 1, 2017

**_Update 2017-07-12_**: As promised, the `latest` fields within `rtm.start`'s channel objects are no longer returned. Additionally, the `unread_count` and `unread_count_display` channel fields are also _missing_, though they can still be found in [`conversations.info`](/reference/methods/conversations.info).

* * *

[`rtm.start`](/reference/methods/rtm.start) began life as a broker and bootstrap to Websocket connections established by Slack's desktop and mobile clients. Whenever our clients needed more information to establish state, those fields would get stuffed into the cacophony that is `rtm.start`'s opening salvos.

As team sizes and feature complexity has grown, delivering this immense quantity of information about nearly every user, channel, and conversation on a team has become more difficult to compute, consume, or continue.

It is in this spirit we offer a friendlier alternative in [`rtm.connect`](/reference/methods/rtm.connect), a method born with the sole purpose of reserving a websocket connection and providing your application its URL.

[`rtm.start`](/reference/methods/rtm.start) must evolve to continue functioning well for all teams and apps. We strongly recommend using [`rtm.connect`](/reference/methods/rtm.connect) to establish your connections alongside [Web API methods](/reference/methods) to build your app's understanding of the users, channels, and conversations within a team.

One such change coming to `rtm.start` is the elimination of the `latest` attribute assigned to each `channel` in its response.

On **July 11, 2017** we'll no longer return these `latest` fields. If your app needs a channel's latest timestamp value, use [`conversations.info`](/reference/methods/conversations.info) to retrieve it instead.

You can test this future behavior in `rtm.start` today by providing the `no_latest=1` parameter.

## What's changing? {#whats-changing}

The short version:

* We introduced [`rtm.connect`](/reference/methods/rtm.connect), an improved light-weight way to connect to the RTM API.
* You can expect growing pains on [`rtm.start`](/reference/methods/rtm.start) from here on out.
* We recommend using `rtm.connect` in conjunction with the [Web API](/apis/web-api/) to avoid those pains.
* `channel` objects in `rtm.start`s will no longer include the `latest` attribute after July 11, 2017.
* Use the new `no_latest=1` parameter with `rtm.start` to preview this behavior today.

The new `rtm.connect` method yields a satisfyingly short yet useful response:

```json
{    "ok": true,    "url": "wss:\/\/ms9.slack-msgs.com\/websocket\/2I5yBpcvk",    "team": {        "id": "T654321",        "name": "Librarian Society of Soledad",        "domain": "libsocos",        "enterprise_id": "E234567",        "enterprise_name": "Intercontinental Librarian Society"    },    "self": {        "id": "W123456",        "name": "brautigan"    }}
```text

## What isn't changing? {#what-isnt-changing}

* We're not deprecating `rtm.start` at this time, but we strongly encourage you to move away from it and to expect continued changes to maintain its scalability.
* The websocket connection established for your app is the same regardless of which method is chosen.

## How do I prepare? {#how-do-i-prepare}

The tactics to follow vary on your situation:

#### Only using rtm.start to connect? {#only-using-rtmstart-to-connect}

We encourage you to review your code and libraries to understand how the initial fields returned by `rtm.start` are or are not used. If your app only uses the `url` field, you should be able to safely move to `rtm.connect` with no further modifications being necessary.

#### Using some of the data in rtm.start? {#using-some-of-the-data-in-rtmstart}

If using at least some of the additional data provided by `rtm.start`, we recommend moving on to determining if you use the `latest` timestamp field attached to `channel` objects. If you don't, start using the `no_latest=1` parameter to help speed up your connections and consider retrieving all the data you need from the [Web API](/apis/web-api/) instead and moving to `rtm.connect`.

#### Using the latest field from channel objects in rtm.start? {#using-the-latest-field-from-channel-objects-in-rtmstart}

If you're using the `latest` field, you'll definitely want to act. Start by collecting information about the channels your app is invested in from the Web API using a combination of [`conversations.list`](/reference/methods/conversations.list) and [`conversations.info`](/reference/methods/conversations.info).

Then start using the `no_latest=1` parameter when connecting with `rtm.start`, or move to `rtm.connect` entirely.

The [Events API](/apis/events-api/) is an attractive alternative to everything [RTM API](/legacy/legacy-rtm-api).

## When is this happening? {#when-is-this-happening}

[`rtm.connect`](/reference/methods/rtm.connect) is available today! [`rtm.start`](/reference/methods/rtm.start)'s `no_latest=1` parameter is also functional, so you can get started testing the future today.

On **July 11, 2017** we will remove the `latest` attribute from channel objects appearing in all `rtm.start` responses.

## Tags:

* [Breaking change](/changelog/tags/breaking-change)
