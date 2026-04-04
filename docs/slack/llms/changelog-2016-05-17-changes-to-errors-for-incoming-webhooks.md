Source: https://docs.slack.dev/changelog/2016-05-17-changes-to-errors-for-incoming-webhooks

# Changes to errors for incoming webhooks

May 17, 2016

Today, [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks) either work or they don't. Usually they do, but when they don't, you get a somewhat nasty umbrella HTTP 500 error, even when error conditions were due to something well-understood, like malformed requests or non-existent destination channels.

We will diversify our responses to include commonly-interpreted HTTP status codes. For most developers using incoming webhooks, this change will not require additional effort. Most HTTP clients readily consume and predictably react with these status codes.

## What's changing: {#whats-changing}

To clarify the nature of these failures and reserve HTTP 500 for only the most exceptional of circumstances, we'll begin returning HTTP 400, 403, and 404 as appropriate, better explaining the situation.

Here are the errors you may encounter, along with the strings we'll return to you in the response body.

### HTTP 400 Bad Request {#http-400-bad-request}

* `invalid_payload` - the data sent in your request cannot be understood as presented; verify your content body matches your content type and is structurally valid.
* `user_not_found` - the user used in your request does not actually exist.

### HTTP 403 Forbidden {#http-403-forbidden}

* `action_prohibited` - the team associated with your request has some kind of restriction on the webhook posting in this context.

### HTTP 404 Not Found {#http-404-not-found}

* `channel_not_found` - the channel associated with your request does not exist.

### HTTP 410 Gone {#http-410-gone}

* `channel_is_archived` - the channel has been archived and doesn't accept further messages, even from your incoming webhook.

### HTTP 500 Server Error {#http-500-server-error}

* `rollup_error` - something strange and unusual happened that was likely not your fault at all.

## When it's happening: {#when-its-happening}

We'd like to make this change on **June 14th, 2016**.

## How to prepare: {#how-to-prepare}

You're unlikely to run into trouble if you interpret a HTTP 200 response as success and any other response code as a failure of some kind. This is the most common behavior when working with incoming webhooks.

If you're specifically looking for HTTP 500 as the primary failure state, you'll want to tell your computers to better understand these 400-series errors as well.

Finally, interpreting these status codes and responses can be put to especially good use, by using them to provide users feedback when encountering error conditions, like incorrect channel selection. Logging these codes are also helpful when debugging and reporting issues with webhooks.

Let us know if you anticipate any issues with your apps and integrations. If the coast is clear, you'll see this ship sail on **June 14th, 2016**.

**Tags:**

* [Announcement](/changelog/tags/announcement)
