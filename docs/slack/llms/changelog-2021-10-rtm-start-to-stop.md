Source: https://docs.slack.dev/changelog/2021-10-rtm-start-to-stop

# rtm.start to stop

October 5, 2021

The original way to connect to one of our oldest APIs is finally retiring. For existing apps, [`rtm.start`](/reference/methods/rtm.start) will start behaving exactly like [`rtm.connect`](/reference/methods/rtm.connect) on **September 27, 2022**. Beginning November 30, 2021, newly created apps and integrations will only be able to use `rtm.connect`.

The RTM API remains available to developers using `rtm.connect`.

Retirement and deprecation complete

All changes described in this changelog have now taken place. Those still using `rtm.start` will now receive the response given by `rtm.connect` instead.

Before continuing, we wanted to point out that this announcement is _not_ deprecating the [Real Time Messaging (RTM) API](/legacy/legacy-rtm-api). If that time ever comes, we'll fully communicate that as a separate deprecation and retirement plan.

Read on to learn how to adapt your apps and integrations to upcoming changes to `rtm.start`.

## What's changing {#what}

Beginning November 30, 2021, newly created Slack apps will no longer be able to make API calls to `rtm.start`.

Beginning September 27, 2022, `rtm.start`'s current response will completely retire. To help most apps transition seamlessly, we will replace the response of [`rtm.start`](/reference/methods/rtm.start) with that of its replacement, [`rtm.connect`](/reference/methods/rtm.connect).

We're also introducing two new API methods: [`team.preferences.list`](/reference/methods/team.preferences.list) and [`team.billing.info`](/reference/methods/team.billing.info). These APIs provide information previously available only in the disorganized jumble of data returned, along with websocket URIs, in `rtm.start`.

Beginning today, you'll see `method_deprecated` warnings returned by `rtm.start`. After November 30, 2021, newly created apps will see the warning migrate to a `method_deprecated` _error_.

## What isn't changing {#what-isnt-changing}

Existing apps and integrations may continue using the RTM API. With few ways remaining to connect to the [RTM API](/legacy/legacy-rtm-api), we **strongly recommend** you consider alternatives ([like Socket Mode](#events-sockets)) even if you already use `rtm.connect`.

For apps created before November 30, 2021, making API calls to `https://slack.com/api/rtm.start` will still technically succeed and return successful, but highly truncated responses even after September 27, 2022.

## How do I prepare? {#how}

You have at least two options when migrating off of `rtm.start`.

1. Migrate to Slack apps: [Use the Events API via websockets over Socket Mode for Apps instead of the RTM API](#events-sockets)
2. Keep using legacy APIs: [Use `rtm.connect` instead of `rtm.start` and other Web API methods as needed](#rtm-connect)

### Using Events API with Socket Mode {#events-sockets}

If you're still using the RTM API, it means you haven't migrated to Slack apps yet, which don't support the RTM API. However, Slack apps do support websocket-based connections that operate _behind the firewall_, the most common reason developers chose RTM in the past.

[Learn how "Socket Mode" and Bolt make building event-driven apps easier](/apis/events-api/using-socket-mode).

Building Slack apps allow you to build more interactive, event-driven applications with friendlier user interfaces than the types of bots and integrations enabled by the RTM API.

### Using rtm.connect {#rtm-connect}

Following this path will help assure you that your app, integration, or bot will continue functioning after September 27, 2022 while requiring the fewest code changes. However, you'll still be using legacy APIs.

Migrate your API requests from `rtm.start` to [`rtm.connect`](/reference/methods/rtm.connect). In most cases, calls to `rtm.start` are looking for only a few basic pieces of information about a workspace and the websocket URI to connect to, which is exactly what `rtm.connect` provides.

Here's an example of `rtm.connect`'s response:

```json
{    "ok": true,    "url": "wss://some-fancy-url.slack-msgs.com/websocket/secretCodesOnlyMonstersUnderstand==/2",    "team": {        "id": "T061EG9R6",        "name": "Subarachnoid Workspace",        "domain": "subarachnoid"    },    "self": {        "id": "U061F7AUR",        "name": "episod"    }}
```text

You'll see there's only a few pieces of info there -- most importantly that websocket `url` field that allows you to connect to the [RTM API](/legacy/legacy-rtm-api).

### Looking for conversations, users, preferences, and plans? {#looking-for-conversations-users-preferences-and-plans}

The monstrously verbose information in `rtm.start` was originally returned so Slack clients built by Slack would have a quick dump of data to store in memory to initialize state from. Back then, a workspace had no more than a few hundred users or channels.

When we shared the platform with other developers, we left all that extraneous info in there. We stopped using it years ago. If there's info you rely on in `rtm.start` beyond the `url`, here's where to find _most_ of what you're looking for:

* Channels, conversations and all that - use [`conversations.list`](/reference/methods/conversations.list) but often [`users.conversations`](/reference/methods/users.conversations) will give you want you want to know.
* Users - list them with [`users.list`](/reference/methods/users.list) and get even more info about them with [`users.info`](/reference/methods/users.info).
* Workspace/team preferences - find them with our new method, [`team.preferences.list`](/reference/methods/team.preferences.list).
* Workspace/team billing plans - learn which billing plan a workspace is on with [`team.billing.info`](/reference/methods/team.billing.info).

## What if I do nothing? {#nothing}

Beginning **November 30, 2021**, you won't be able to make API calls to `rtm.start` with newly created classic apps or custom bot tokens. Apps and integrations created prior to November 30, 2021 may continue calling `rtm.start`, but ideally you'll adjust your calls to `rtm.connect` instead.

If you choose to do absolutely nothing before **September 27, 2022** your app or integration will quite possibly break.

Whether your app or integration breaks or not depends on how dependent your code is on the plethora of fields yielded by `rtm.start` but not returned by `rtm.connect`. If your current code primarily relies on looking for `url` and `team` and `self` and none of the other fields found in `rtm.start`, your app may continue functioning just fine. To verify whether that's true, you could adjust your API calls to `rtm.connect` instead. If it works, you've just migrated your app -- thank you!

## When does this happen? {#when}

There are three key dates for the retirement of the method called `rtm.start`.

Date

Happenstance

## November 30, 2021

Apps created on or after November 30, 2021 will no longer be able to use `rtm.start`.

## September 13, 2022

At 👉 18:30-23:30 UTC (which is 11:30am-4:30pm Pacific and 3:30am-8:30am Japan Standard Time) 👈   we will preview the future behavior of `rtm.start`. This is so you can understand exactly how the method's response may impact your existing apps and integrations, even if you haven't read this document yet or had time to make adjustments. It's possible we'll cut the preview duration short. If you experience issues during the preview, please contact support.

## September 27, 2022

All apps still using `rtm.start` will receive the briefer response found in `rtm.connect` instead beginning **September 27, 2022**.

## Tags:

* [Deprecation](/changelog/tags/deprecation)
* [Breaking change](/changelog/tags/breaking-change)
