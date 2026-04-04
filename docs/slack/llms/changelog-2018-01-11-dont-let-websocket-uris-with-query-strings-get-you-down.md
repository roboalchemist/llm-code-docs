Source: https://docs.slack.dev/changelog/2018/01/11/dont-let-websocket-uris-with-query-strings-get-you-down

# Don't let websocket URIs with query strings get you down

January 11, 2018

We now serve query string parameters on the `wss://` WebSocket URIs produced by [`rtm.connect`](/reference/methods/rtm.connect) and [`rtm.start`](/reference/methods/rtm.start).

While the specification for WebSockets explicitly allows query string parameters, some third party libraries not fully implementing the spec may handle these parameters incorrectly, stripping them off and invalidating your attempts to open a connection.

## Known issues {#known-issues}

Though we didn't anticipate issues sending query strings in websocket URIs, some libraries and frameworks may need tinkering with.

* Use [**Slack API in Go**](https://github.com/nlopes/slack) AKA `github.com/nlopes/slack`? Update to the latest version of this Golang project to resolve connection issues. A [recent commit](https://github.com/nlopes/slack/pull/217) merged with master fixes websocket URI handling.

## What's changing? {#whats-changing}

Previously, `rtm.connect` and `rtm.start` would only yield websocket URLs containing protocol, host, domain, and path elements, but _no_ query parameter components.

Now Slack will often return a WebSocket URI string with a query string parameter, such as `?dp=1`, included.

New URIs with query string parameters:

```text
wss://mpmulti-2323.lb.slack-msgs.com/websocket/iSaBellRinging--4Hclub-TKOmac-ozma-gr12-tAbsco_3gP551gB0=/3?dp=1
```text

Original URIs without parameters:

```text
wss://mpmulti-7272.lb.slack-msgs.com/websocket/iSaBellRinging--4Hclub-TKOmac-ozma-gr12-tAbsco_3gP551gB0=/2
```text

You must **_preserve_** these parameters when directing your WebSocket client to open the connection.

If your code or library doesn't preserve the query string, the connection will fail. If your library automatically attempts to retrieve a new websocket connection by requesting `rtm.connect` or `rtm.start` again, it will likely become stuck in an endless loop, resulting in rate limiting and preventing further connections.

## What isn't changing? {#what-isnt-changing}

Nothing else about the RTM API or WebSocket connections or other platform features are changing.

## How do I prepare? {#how-do-i-prepare}

If you're sure this problem is affecting you, upgrade any client libraries you depend on. If the issue is still unrectified, consider diving in to the code you rely on and examine how websocket URIs are treated after reception. If the URIs are truncated, rectify it by preserving the URI exactly as returned by the API.

## When is this happening? {#when-is-this-happening}

These changes to websocket URIs have been slowly trickling to production over the past several weeks, beginning in December 2017.

Still having trouble or want to help others resolve issues like this? [Let us know what you've found out](https://slack.com/help/requests/new).

## Tags:

* [New feature](/changelog/tags/new-feature)
