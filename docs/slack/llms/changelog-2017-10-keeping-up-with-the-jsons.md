Source: https://docs.slack.dev/changelog/2017-10-keeping-up-with-the-jsons

# Keeping up with the JSONs

October 1, 2017

Incoming webhooks can do it. [Slash commands](/interactivity/implementing-slash-commands) and [interactive messages](/legacy/legacy-messaging/legacy-making-messages-interactive) speak it fluently. The message builder knows no other format. But, until now, [`chat.postMessage`](/reference/methods/chat.postMessage) stubbornly refused to understand your messages composed in impeccable JSON.

Finally, Slack allows you to send JSON to [a wide selection](#methods) of write-based [Web API](/apis/web-api/) methods. Additionally, now you can better separate concerns when presenting your credentials to Slack.

## What's changing? {#what}

A large selection of Web API write methods now support properly formatted JSON POST bodies. This is most useful for methods supporting complex JSON parameters like [`chat.postMessage`](/reference/methods/chat.postMessage), [`chat.postEphemeral`](/reference/methods/chat.postEphemeral), [`chat.update`](/reference/methods/chat.update), [`chat.unfurl`](/reference/methods/chat.unfurl), and [`dialog.open`](/reference/methods/dialog.open).

Mostly things should "just work." If you run into a situation where a method doesn't understand what seems like valid JSON — especially methods that take arrays or objects — please let us know!

Additionally, we now support and _prefer_ passing tokens in HTTP `Authorization` headers.

## How do I use it? {#how}

First we'll review how to use an `Authorization` header to transmit your OAuth credentials. You may already be familiar with this process if you've used other APIs or even our Files API.

Then we'll cover submitting JSON in the Web API, which depends on this authorization knowledge.

### Using Authorization headers to signal your tokens {#auth}

We now **strongly encourage** using the `Authorization` HTTP header to convey your app or integration's [tokens](/authentication/tokens).

To make use of sending JSON on write operations, you **_must_** provide your token value using an `Authorization` HTTP header.

Tokens used in the Slack API are _bearer tokens_. To specify this type of token to Slack, you must pre-pend `Bearer` to your HTTP `Authorization` header's value.

If your authorization token was a bot user token like `xoxb-1234-56789abcdefghjijklmnop`, then your `Authorization` header value would be `Bearer xoxb-1234-56789abcdefghjijklmnop`.

## Best practice:

```text
GET /api/users.info?user=W123456Authorization: Bearer xoxb-1234-56789abcdefghijklmnop
```text

## Still accepted, but _discouraged_:

```text
GET /api/users.info?user=W123456&token=xoxb-1234-56789abcdefghijklmnop
```text

You can send your token via `Authorization` header using all Web API methods. Just don't send it multiple ways at once!

Here's an example using the popular command line tool, [cURL](https://curl.haxx.se/):

```bash
curl -X GET -H 'Authorization: Bearer xoxb-1234-56789abcdefghijklmnop' \https://slack.com/api/users.info?user=W123456</code></pre>
```text

### Sending JSON when POSTing to Web API write methods {#our_friend_json}

To send JSON to the Web API, use the authorization procedure above: present your bearer tokens, whatever their [token type](/authentication/tokens), in a HTTP `Authorization` header.

Additionally specify the `Content-type` header as `application/json`. Your POST body should contain nothing but your JSON body.

Methods supporting comma-separated value arguments _should_ support presentation of arguments as a JSON array _or_ as a string with comma-separated values.

Methods accepting JSON objects or arrays, like `chat.postMessage` and `chat.unfurl`, _should_ support presenting those arguments natively in JSON.

The most common use case for sending JSON is preserving your message structure when using multiple platform tools together: incoming webhooks, slash commands, interactive messages, `chat.postMessage`, etc.

Don't send a mixture of query parameters, POST parameters, or JSON attributes. Choose one model per request.

#### Example JSON requests {#example-json-requests}

Creating a public channel with [`conversations.create`](/reference/methods/conversations.create):

```text
POST /api/conversations.createContent-type: application/jsonAuthorization: Bearer xoxa-xxxxxxxxx-xxxx{"name":"something-urgent"}
```text

Posting a message with [menus](/legacy/legacy-messaging/legacy-adding-menus-to-messages) using [`chat.postMessage`](/reference/methods/chat.postMessage):

```text
POST /api/chat.postMessageContent-type: application/jsonAuthorization: Bearer xoxa-xxxxxxxxx-xxxx{"channel":"C061EG9SL","text":"I hope the tour went well, Mr. Wonka.","attachments":[{"text":"Who wins the lifetime supply of chocolate?","fallback":"You could be telling the computer exactly what it can do with a lifetime supply of chocolate.","color":"#3AA3E3","attachment_type":"default","callback_id":"select_simple_1234","actions":[{"name":"winners_list","text":"Who should win?","type":"select","data_source":"users"}]}]}
```text

Note how the `attachments` argument is sent as a straight-forward JSON array.

Here's how to do that with cURL:

```bash
curl -X POST -H 'Authorization: Bearer xoxb-1234-56789abcdefghijklmnop' \-H 'Content-type: application/json' \--data '{"channel":"C061EG9SL","text":"I hope the tour went well, Mr. Wonka.","attachments": [{"text":"Who wins the lifetime supply of chocolate?","fallback":"You could be telling the computer exactly what it can do with a lifetime supply of chocolate.","color":"#3AA3E3","attachment_type":"default","callback_id":"select_simple_1234","actions":[{"name":"winners_list","text":"Who should win?","type":"select","data_source":"users"}]}]}' \https://slack.com/api/chat.postMessage
```text

## What isn't changing? {#what_not}

You can still send `application/x-www-form-urlencoded` data the way you're used to on a method URL's query string or POST body.

You can still use HTTP POST on read methods, though those methods do not understand attributes presented as JSON.

You don't have to send your access tokens via the `Authorization` HTTP header, but we'd prefer that you did.

Nothing changes with parts of the platform that _aren't_ the [Web API](/apis/web-api/).

## What happens if I do nothing? {#nothing}

We anticipate no issues. This is a backwards compatible, opt-in change that we're confident will make development against Slack easier for many.

There is a slim chance that if you've been sending `application/x-www-form-urlencoded` data to us but claiming its `application/json` or vice-versa, or if you have a habit of gratuitously including the same `token` field in a variety of different ways, you'll find us at a loss for how to consider your request.

## When did this happen? {#when}

As of October 30, 2017 you can send `application/json` POSTs to the [methods](#methods) detailed above. Additionally, you may now use `Authorization` HTTP headers to transmit tokens throughout the Web API.

* * *

## Methods supporting JSON POSTs {#methods}

These write methods currently support sending a HTTP POST with `application/json`.

SUPPORTS\_JSON\_METHOD\_LIST

Is your favorite method missing? Let us know.

## Tips when preparing your JSON {#tips}

Having trouble properly formatting your JSON? Here are some quick tips:

* JSON should never contain trailing commas; a stray comma will invalidate your JSON.
* JSON may not include comments, either of the `//` or `#` variety.
* For better readability, JSON may include additional whitespace and tabbing between keys and values. However, minify unmeaningful whitespace for best performance.
* Verify that your keys and other strings are enclosed in double quote characters: `"`
* Set your `Content-type` HTTP header to `application/json`
* Send your application's token as an `Authorization` HTTP header beginning with `"Bearer "`: `Authorization: Bearer xoxb-12345-abcdefghjk`

## Tags:

* [New feature](/changelog/tags/new-feature)
