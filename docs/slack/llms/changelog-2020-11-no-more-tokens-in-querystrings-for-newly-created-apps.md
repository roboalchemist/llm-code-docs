Source: https://docs.slack.dev/changelog/2020-11-no-more-tokens-in-querystrings-for-newly-created-apps

# No more tokens in querystrings for newly created apps

November 1, 2020

Tokens may no longer be passed in the query string for apps created after Feb 24, 2021

On **February 24, 2021**, we will stop allowing _newly created_ Slack apps to send requests to [Web API methods](/reference/methods) with access tokens presented in a URL query string. Instead, apps must send tokens in the `Authorization` HTTP header or alternatively as a URL-encoded POST body parameter.

Existing apps will be allowed to continue sending their tokens in the `token` query string parameter, though we recommend all apps to use authorization headers whenever possible.

## What's changing? {#what}

Until now, it's been possible to send a token as a query string parameter to issue requests to the Slack Web API. For example, one might request `GET https://slack.com/api/conversations.list?limit=50&token=xoxb-abc-123456` to [retrieve a list of conversations](/reference/methods/conversations.list) in a workspace.

Apps created after February 24, 2021 **may no longer send tokens as query parameters** and _must_ instead use an HTTP authorization header or send the token in an HTTP POST body.

For example, the same request above can be sent with header-based auth as:

```text
GET https://slack.com/api/conversations.list?limit=50Authorization: Bearer xoxb-abc-123456
```text

Or, as a POST request:

```text
POST https://slack.com/api/conversations.listContent-type: application/x-www-form-urlencodedlimit=50&token=xoxb-abc-123456
```text

## How to prepare {#how}

For Slack apps created after February 24, 2021, or if you maintain a library or other piece of software that relies on newly created Slack apps, you must send Web API requests with an access token included either in the HTTP Authorization header or as a POST parameter.

If you frequently use the API on the command line or in web browsers, you won't be able to attach the `token` query parameter to API method URLs. This means you will effectively be unable to use the API in web browsers without the assistance of a third-party tool such as Postman. Our API method tester works for ad hoc requests too, such as [listing channels in a workspace](/reference/methods/conversations.list).

If you issue requests using cURL with a command like:

```bash
curl "https://slack.com/api/conversations.list?token=xoxb-abc-123456"
```text

You'll want to adjust that command to something like:

```bash
curl -X POST -d "token-xoxb-abc-123456" "https://slack.com/api/conversations.list"
```text

All of the [SDK and libraries provided by Slack](/tools), such as Bolt, are ready to go.

## What if I do nothing? {#nothing}

Apps created before February 24, 2021 will continue functioning no matter which way you pass your token. We'd prefer you use Authorization headers regardless.

If you create a Slack app and use a library or tool that sends `token` as a query string parameter, the API will respond with an error and will not service the request.

If you use one of the [SDK or libraries](/tools) built by Slack, everything should continue functioning normally. You may want to verify you're using the latest versions just the same.

## When does this happen? {#when}

On February 24, 2021 we will stop allowing newly created apps to send `token` query string parameters.

Need any help? [Let us know!](https://my.slack.com/help/requests/new)

## Tags:

* [Announcement](/changelog/tags/announcement)
