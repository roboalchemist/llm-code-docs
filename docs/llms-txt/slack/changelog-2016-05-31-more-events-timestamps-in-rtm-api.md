Source: https://docs.slack.dev/changelog/2016/05/31/more-events-timestamps-in-rtm-api

# More event timestamps in the RTM API

May 31, 2016

Within the next few weeks, we'll add `event_ts` timestamp fields to additional [streamed events](/reference/events) you receive in the [real-time messaging API](/legacy/legacy-rtm-api).

## What are these fields for? {#what-are-these-fields-for}

The `event_ts` field differs from the `ts` timestamp fields you already receive with most events. The `ts` field is associated with the object or transition the event is describing while the `event_ts` attribute refers to the streamed event.

The `ts` field is like a date scrawled on a letter contained within an envelope — it's part of the message itself.

The `event_ts` is like a postmark stamped on the envelope as part of the postal process, an artifact of the workflow used to deliver the message to the intended recipient.

As with `ts`, `event_ts` is expressed in a kind of "[epoch time](https://en.wikipedia.org/wiki/Unix_time)", contained within a string and including fractions of seconds.

An example `event_ts` timestamp value of `"1361482916.000004"`, could be converted to UTC as `2013-02-21 21:41:56 UTC`.

`event_ts` is especially useful when noting your real time progress through a channel's history.

## What's changing: {#whats-changing}

We're adding `event_ts` timestamp fields to additional [RTM API](/legacy/legacy-rtm-api)[events](/reference/events), including but certainly not limited to event fan favorites like `group_archive`, `user_change`, and `star_added`.

## How to prepare: {#how-to-prepare}

We don't anticipate developers needing to prepare for this additive API alteration.

Streamed events will gain a `event_ts` field as part of their JSON structure.

This field is already present on a number of events including `im_history_changed`, `emoji_changed` and our medium of conversation: `message`.

If you can reliably maintain a connection with the RTM API today, it is unlikely you'll encounter any difficulties with this field addition.

## When it's happening: {#when-its-happening}

We'll begin adding these fields sometime in mid to late **June 2016**. Let us know about any anticipated issues by contacting us [here](https://slack.com/help/requests/new).

**Tags:**

* [New feature](/changelog/tags/new-feature)
