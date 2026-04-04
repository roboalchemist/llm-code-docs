# Source: https://html.spec.whatwg.org/multipage/web-messaging.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/web-messaging.html

Published Time: Mon, 16 Mar 2026 07:32:48 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 9.2 Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [10 Web workers →](https://html.spec.whatwg.org/multipage/workers.html)
1.       1.   [9.3 Cross-document messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#web-messaging)
        1.   [9.3.1 Introduction](https://html.spec.whatwg.org/multipage/web-messaging.html#introduction-12)
        2.   [9.3.2 Security](https://html.spec.whatwg.org/multipage/web-messaging.html#security-postmsg)
            1.   [9.3.2.1 Authors](https://html.spec.whatwg.org/multipage/web-messaging.html#authors)
            2.   [9.3.2.2 User agents](https://html.spec.whatwg.org/multipage/web-messaging.html#user-agents)

        3.   [9.3.3 Posting messages](https://html.spec.whatwg.org/multipage/web-messaging.html#posting-messages)

    2.   [9.4 Channel messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-messaging)
        1.   [9.4.1 Introduction](https://html.spec.whatwg.org/multipage/web-messaging.html#introduction-13)
            1.   [9.4.1.1 Examples](https://html.spec.whatwg.org/multipage/web-messaging.html#examples-5)
            2.   [9.4.1.2 Ports as the basis of an object-capability model on the web](https://html.spec.whatwg.org/multipage/web-messaging.html#ports-as-the-basis-of-an-object-capability-model-on-the-web)
            3.   [9.4.1.3 Ports as the basis of abstracting out service implementations](https://html.spec.whatwg.org/multipage/web-messaging.html#ports-as-the-basis-of-abstracting-out-service-implementations)

        2.   [9.4.2 Message channels](https://html.spec.whatwg.org/multipage/web-messaging.html#message-channels)
        3.   [9.4.3 The `MessageEventTarget` mixin](https://html.spec.whatwg.org/multipage/web-messaging.html#the-messageeventtarget-mixin)
        4.   [9.4.4 Message ports](https://html.spec.whatwg.org/multipage/web-messaging.html#message-ports)
        5.   [9.4.5 Ports and garbage collection](https://html.spec.whatwg.org/multipage/web-messaging.html#ports-and-garbage-collection)

    3.   [9.5 Broadcasting to other browsing contexts](https://html.spec.whatwg.org/multipage/web-messaging.html#broadcasting-to-other-browsing-contexts)

### 9.3 Cross-document messaging[](https://html.spec.whatwg.org/multipage/web-messaging.html#web-messaging)

[Window/postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage "The window.postMessage() method safely enables cross-origin communication between Window objects; e.g., between a page and a pop-up that it spawned, or between a page and an iframe embedded within it.")

Support in all current engines.

Firefox 3+Safari 4+Chrome 2+

* * *

Opera 9.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android≤37+Samsung Internet?Opera Android 10.1+

Web browsers, for security and privacy reasons, prevent documents in different domains from affecting each other; that is, cross-site scripting is disallowed.

While this is an important security feature, it prevents pages from different domains from communicating even when those pages are not hostile. This section introduces a messaging system that allows documents to communicate with each other regardless of their source domain, in a way designed to not enable cross-site scripting attacks.

[](https://html.spec.whatwg.org/multipage/web-messaging.html#fingerprint-postMessage)[![Image 2: (This is a tracking vector.)](https://resources.whatwg.org/tracking-vector.svg)](https://infra.spec.whatwg.org/#tracking-vector "There is a tracking vector here.") The `postMessage()` API can be used as a [tracking vector](https://infra.spec.whatwg.org/#tracking-vector).

#### 9.3.1 Introduction[](https://html.spec.whatwg.org/multipage/web-messaging.html#introduction-12)

_This section is non-normative._

For example, if document A contains an `iframe` element that contains document B, and script in document A calls `postMessage()` on the `Window` object of document B, then a message event will be fired on that object, marked as originating from the `Window` of document A. The script in document A might look like:

```
var o = document.getElementsByTagName('iframe')[0];
o.contentWindow.postMessage('Hello world', 'https://b.example.org/');
```

To register an event handler for incoming events, the script would use `addEventListener()` (or similar mechanisms). For example, the script in document B might look like:

```
window.addEventListener('message', receiver, false);
function receiver(e) {
  if (e.origin == 'https://example.com') {
    if (e.data == 'Hello world') {
      e.source.postMessage('Hello', e.origin);
    } else {
      alert(e.data);
    }
  }
}
```

This script first checks the domain is the expected domain, and then looks at the message, which it either displays to the user, or responds to by sending a message back to the document which sent the message in the first place.

#### 9.3.2 Security[](https://html.spec.whatwg.org/multipage/web-messaging.html#security-postmsg)

Use of this API requires extra care to protect users from hostile entities abusing a site for their own purposes.

Authors should check the `origin` attribute to ensure that messages are only accepted from domains that they expect to receive messages from. Otherwise, bugs in the author's message handling code could be exploited by hostile sites.

Furthermore, even after checking the `origin` attribute, authors should also check that the data in question is of the expected format. Otherwise, if the source of the event has been attacked using a cross-site scripting flaw, further unchecked processing of information sent using the `postMessage()` method could result in the attack being propagated into the receiver.

Authors should not use the wildcard keyword (*) in the targetOrigin argument in messages that contain any confidential information, as otherwise there is no way to guarantee that the message is only delivered to the recipient to which it was intended.

* * *

Authors who accept messages from any origin are encouraged to consider the risks of a denial-of-service attack. An attacker could send a high volume of messages; if the receiving page performs expensive computation or causes network traffic to be sent for each such message, the attacker's message could be multiplied into a denial-of-service attack. Authors are encouraged to employ rate limiting (only accepting a certain number of messages per minute) to make such attacks impractical.

##### 9.3.2.2 User agents[](https://html.spec.whatwg.org/multipage/web-messaging.html#user-agents)

The integrity of this API is based on the inability for scripts of one [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) to post arbitrary events (using `dispatchEvent()` or otherwise) to objects in other origins (those that are not the [same](https://html.spec.whatwg.org/multipage/browsers.html#same-origin)).

Implementers are urged to take extra care in the implementation of this feature. It allows authors to transmit information from one domain to another domain, which is normally disallowed for security reasons. It also requires that UAs be careful to allow access to certain properties but not others.

* * *

User agents are also encouraged to consider rate-limiting message traffic between different [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin), to protect naïve sites from denial-of-service attacks.

#### 9.3.3 Posting messages[](https://html.spec.whatwg.org/multipage/web-messaging.html#posting-messages)

`window.postMessage(message [, options ])`

[Window/postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage "The window.postMessage() method safely enables cross-origin communication between Window objects; e.g., between a page and a pop-up that it spawned, or between a page and an iframe embedded within it.")

Support in all current engines.

Firefox 3+Safari 4+Chrome 2+

* * *

Opera 9.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 10.1+

Posts a message to the given window. Messages can be structured objects, e.g. nested objects and arrays, can contain JavaScript values (strings, numbers, `Date` objects, etc.), and can contain certain data objects such as `File``Blob`, `FileList`, and `ArrayBuffer` objects.

Objects listed in the `transfer` member of options are transferred, not just cloned, meaning that they are no longer usable on the sending side.

A target origin can be specified using the `targetOrigin` member of options. If not provided, it defaults to "`/`". This default restricts the message to same-origin targets only.

If the origin of the target window doesn't match the given target origin, the message is discarded, to avoid information leakage. To send the message to the target regardless of origin, set the target origin to "`*`".

Throws a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException` if transfer array contains duplicate objects or if message could not be cloned.

`window.postMessage(message, targetOrigin [, transfer ])`
This is an alternate version of `postMessage()` where the target origin is specified as a parameter. Calling `window.postMessage(message, target, transfer)` is equivalent to 
```
window.postMessage(message, {targetOrigin,
   transfer})
```
.

When posting a message to a `Window` of a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) that has just been navigated to a new `Document` is likely to result in the message not receiving its intended recipient: the scripts in the target [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) have to have had time to set up listeners for the messages. Thus, for instance, in situations where a message is to be sent to the `Window` of newly created child `iframe`, authors are advised to have the child `Document` post a message to their parent announcing their readiness to receive messages, and for the parent to wait for this message before beginning posting messages.

The window post message steps, given a targetWindow, message, and options, are as follows:

1.   Let targetRealm be targetWindow's [realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-global-object-realm).

2.   Let incumbentSettings be the [incumbent settings object](https://html.spec.whatwg.org/multipage/webappapis.html#incumbent-settings-object).

3.   Let targetOrigin be options["`targetOrigin`"].

4.   If targetOrigin is a single U+002F SOLIDUS character (/), then set targetOrigin to incumbentSettings's [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

5.   Otherwise, if targetOrigin is not a single U+002A ASTERISK character (*), then:

    1.   Let parsedURL be the result of running the [URL parser](https://url.spec.whatwg.org/#concept-url-parser) on targetOrigin.

    2.   If parsedURL is failure, then throw a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException`.

    3.   Set targetOrigin to parsedURL's [origin](https://url.spec.whatwg.org/#concept-url-origin).

6.   Let transfer be options["`transfer`"].

7.   Let serializeWithTransferResult be [StructuredSerializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer)(message, transfer). Rethrow any exceptions.

8.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the posted message task source given targetWindow to run the following steps:

    1.   If the targetOrigin argument is not a single literal U+002A ASTERISK character (*) and targetWindow's [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is not [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with targetOrigin, then return.

    2.   Let origin be incumbentSettings's [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

    3.   Let source be the `WindowProxy` object corresponding to incumbentSettings's [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-global) (a `Window` object).

    4.   Let deserializeRecord be [StructuredDeserializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserializewithtransfer)(serializeWithTransferResult, targetRealm).

If this throws an exception, catch it, [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `messageerror` at targetWindow, using `MessageEvent`, with its [origin](https://html.spec.whatwg.org/multipage/comms.html#concept-messageevent-origin) initialized to origin and the `source` attribute initialized to source, and then return.

    5.   Let messageClone be deserializeRecord.[[Deserialized]].

    6.   Let newPorts be a new [frozen array](https://webidl.spec.whatwg.org/#dfn-frozen-array-type) consisting of all `MessagePort` objects in deserializeRecord.[[TransferredValues]], if any, maintaining their relative order.

    7.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `message` at targetWindow, using `MessageEvent`, with its [origin](https://html.spec.whatwg.org/multipage/comms.html#concept-messageevent-origin) initialized to origin, the `source` attribute initialized to source, the `data` attribute initialized to messageClone, and the `ports` attribute initialized to newPorts.

The `Window` interface's 
```
postMessage(message,
  options)
```
 method steps are to run the [window post message steps](https://html.spec.whatwg.org/multipage/web-messaging.html#window-post-message-steps) given [this](https://webidl.spec.whatwg.org/#this), message, and options.

The `Window` interface's 
```
postMessage(message, targetOrigin,
  transfer)
```
 method steps are to run the [window post message steps](https://html.spec.whatwg.org/multipage/web-messaging.html#window-post-message-steps) given [this](https://webidl.spec.whatwg.org/#this), message, and «[ "`targetOrigin`" → targetOrigin, "`transfer`" → transfer ]».

### 9.4 Channel messaging[](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-messaging)

[Channel_Messaging_API](https://developer.mozilla.org/en-US/docs/Web/API/Channel_Messaging_API "The Channel Messaging API allows two separate scripts running in different browsing contexts attached to the same document (e.g., two IFrames, or the main document and an IFrame, two documents via a SharedWorker, or two workers) to communicate directly, passing messages between one another through two-way channels (or pipes) with a port at each end.")

Support in all current engines.

Firefox 41+Safari 5+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

[Channel_Messaging_API/Using_channel_messaging](https://developer.mozilla.org/en-US/docs/Web/API/Channel_Messaging_API/Using_channel_messaging "The Channel Messaging API allows two separate scripts running in different browsing contexts attached to the same document (e.g., two <iframe> elements, the main document and a single <iframe>, or two documents via a SharedWorker) to communicate directly, passing messages between each other through two-way channels (or pipes) with a port at each end.")

Support in all current engines.

Firefox 41+Safari 5+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

#### 9.4.1 Introduction[](https://html.spec.whatwg.org/multipage/web-messaging.html#introduction-13)

_This section is non-normative._

To enable independent pieces of code (e.g. running in different [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)) to communicate directly, authors can use [channel messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-messaging).

Communication channels in this mechanism are implemented as two-ways pipes, with a port at each end. Messages sent in one port are delivered at the other port, and vice-versa. Messages are delivered as DOM events, without interrupting or blocking running [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task).

To create a connection (two "entangled" ports), the `MessageChannel()` constructor is called:

`var channel = new MessageChannel();`
One of the ports is kept as the local port, and the other port is sent to the remote code, e.g. using `postMessage()`:

`otherWindow.postMessage('hello', 'https://example.com', [channel.port2]);`
To send messages, the `postMessage()` method on the port is used:

`channel.port1.postMessage('hello');`
To receive messages, one listens to `message` events:

```
channel.port1.onmessage = handleMessage;
function handleMessage(event) {
  // message is in event.data
  // ...
}
```

Data sent on a port can be structured data; for example here an array of strings is passed on a `MessagePort`:

`port1.postMessage(['hello', 'world']);`
##### 9.4.1.1 Examples[](https://html.spec.whatwg.org/multipage/web-messaging.html#examples-5)

_This section is non-normative._

In this example, two JavaScript libraries are connected to each other using `MessagePort`s. This allows the libraries to later be hosted in different frames, or in `Worker` objects, without any change to the APIs.

```
<script src="contacts.js"></script> <!-- exposes a contacts object -->
<script src="compose-mail.js"></script> <!-- exposes a composer object -->
<script>
 var channel = new MessageChannel();
 composer.addContactsProvider(channel.port1);
 contacts.registerConsumer(channel.port2);
</script>
```

Here's what the "addContactsProvider()" function's implementation could look like:

```
function addContactsProvider(port) {
  port.onmessage = function (event) {
    switch (event.data.messageType) {
      case 'search-result': handleSearchResult(event.data.results); break;
      case 'search-done': handleSearchDone(); break;
      case 'search-error': handleSearchError(event.data.message); break;
      // ...
    }
  };
};
```

Alternatively, it could be implemented as follows:

```
function addContactsProvider(port) {
  port.addEventListener('message', function (event) {
    if (event.data.messageType == 'search-result')
      handleSearchResult(event.data.results);
  });
  port.addEventListener('message', function (event) {
    if (event.data.messageType == 'search-done')
      handleSearchDone();
  });
  port.addEventListener('message', function (event) {
    if (event.data.messageType == 'search-error')
      handleSearchError(event.data.message);
  });
  // ...
  port.start();
};
```

The key difference is that when using `addEventListener()`, the `start()` method must also be invoked. When using `onmessage`, the call to `start()` is implied.

The `start()` method, whether called explicitly or implicitly (by setting `onmessage`), starts the flow of messages: messages posted on message ports are initially paused, so that they don't get dropped on the floor before the script has had a chance to set up its handlers.

##### 9.4.1.2 Ports as the basis of an object-capability model on the web[](https://html.spec.whatwg.org/multipage/web-messaging.html#ports-as-the-basis-of-an-object-capability-model-on-the-web)

_This section is non-normative._

Ports can be viewed as a way to expose limited capabilities (in the object-capability model sense) to other actors in the system. This can either be a weak capability system, where the ports are merely used as a convenient model within a particular origin, or as a strong capability model, where they are provided by one origin provider as the only mechanism by which another origin consumer can effect change in or obtain information from provider.

For example, consider a situation in which a social web site embeds in one `iframe` the user's email contacts provider (an address book site, from a second origin), and in a second `iframe` a game (from a third origin). The outer social site and the game in the second `iframe` cannot access anything inside the first `iframe`; together they can only:

*   [Navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) the `iframe` to a new [URL](https://url.spec.whatwg.org/#concept-url), such as the same [URL](https://url.spec.whatwg.org/#concept-url) but with a different [fragment](https://url.spec.whatwg.org/#concept-url-fragment), causing the `Window` in the `iframe` to receive a `hashchange` event.

*   Resize the `iframe`, causing the `Window` in the `iframe` to receive a `resize` event.

*   Send a `message` event to the `Window` in the `iframe` using the `window.postMessage()` API.

The contacts provider can use these methods, most particularly the third one, to provide an API that can be accessed by other origins to manipulate the user's address book. For example, it could respond to a message "
```
add-contact Guillaume Tell
  <tell@pomme.example.net>
```
" by adding the given person and email address to the user's address book.

To avoid any site on the web being able to manipulate the user's contacts, the contacts provider might only allow certain trusted sites, such as the social site, to do this.

Now suppose the game wanted to add a contact to the user's address book, and that the social site was willing to allow it to do so on its behalf, essentially "sharing" the trust that the contacts provider had with the social site. There are several ways it could do this; most simply, it could just proxy messages between the game site and the contacts site. However, this solution has a number of difficulties: it requires the social site to either completely trust the game site not to abuse the privilege, or it requires that the social site verify each request to make sure it's not a request that it doesn't want to allow (such as adding multiple contacts, reading the contacts, or deleting them); it also requires some additional complexity if there's ever the possibility of multiple games simultaneously trying to interact with the contacts provider.

Using message channels and `MessagePort` objects, however, all of these problems can go away. When the game tells the social site that it wants to add a contact, the social site can ask the contacts provider not for it to add a contact, but for the _capability_ to add a single contact. The contacts provider then creates a pair of `MessagePort` objects, and sends one of them back to the social site, who forwards it on to the game. The game and the contacts provider then have a direct connection, and the contacts provider knows to only honor a single "add contact" request, nothing else. In other words, the game has been granted the capability to add a single contact.

##### 9.4.1.3 Ports as the basis of abstracting out service implementations[](https://html.spec.whatwg.org/multipage/web-messaging.html#ports-as-the-basis-of-abstracting-out-service-implementations)

_This section is non-normative._

Continuing the example from the previous section, consider the contacts provider in particular. While an initial implementation might have simply used `XMLHttpRequest` objects in the service's `iframe`, an evolution of the service might instead want to use a [shared worker](https://html.spec.whatwg.org/multipage/workers.html#sharedworker) with a single `WebSocket` connection.

If the initial design used `MessagePort` objects to grant capabilities, or even just to allow multiple simultaneous independent sessions, the service implementation can switch from the `XMLHttpRequest`s-in-each-`iframe` model to the shared-`WebSocket` model without changing the API at all: the ports on the service provider side can all be forwarded to the shared worker without it affecting the users of the API in the slightest.

#### 9.4.2 Message channels[](https://html.spec.whatwg.org/multipage/web-messaging.html#message-channels)

[MessageChannel](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel "The MessageChannel interface of the Channel Messaging API allows us to create a new message channel and send data through it via its two MessagePort properties.")

Support in all current engines.

Firefox 41+Safari 5+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

```
[Exposed=(Window,Worker)]
interface MessageChannel {
  constructor();

  readonly attribute MessagePort port1;
  readonly attribute MessagePort port2;
};
```
`channel = new MessageChannel()`

[MessageChannel/MessageChannel](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel/MessageChannel "The MessageChannel() constructor of the MessageChannel interface returns a new MessageChannel object with two new MessagePort objects.")

Support in all current engines.

Firefox 41+Safari 5+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Returns a new `MessageChannel` object with two new `MessagePort` objects.

`channel.port1`

[MessageChannel/port1](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel/port1 "The port1 read-only property of the MessageChannel interface returns the first port of the message channel — the port attached to the context that originated the channel.")

Support in all current engines.

Firefox 41+Safari 5+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Returns the first `MessagePort` object.

`channel.port2`

[MessageChannel/port2](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel/port2 "The port2 read-only property of the MessageChannel interface returns the second port of the message channel — the port attached to the context at the other end of the channel, which the message is initially sent to.")

Support in all current engines.

Firefox 41+Safari 5+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Returns the second `MessagePort` object.

A `MessageChannel` object has an associated port 1 and an associated port 2, both `MessagePort` objects.

The `port1` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [port 1](https://html.spec.whatwg.org/multipage/web-messaging.html#port-1).

The `port2` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [port 2](https://html.spec.whatwg.org/multipage/web-messaging.html#port-2).

#### 9.4.3 The `MessageEventTarget` mixin[](https://html.spec.whatwg.org/multipage/web-messaging.html#the-messageeventtarget-mixin)

```
interface mixin MessageEventTarget {
  attribute EventHandler onmessage;
  attribute EventHandler onmessageerror;
};
```

The following are the [event handlers](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) (and their corresponding [event handler event types](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type)) that must be supported, as [event handler IDL attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes), by objects implementing the `MessageEventTarget` interface:

| [Event handler](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) | [Event handler event type](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type) |
| --- | --- |
| `onmessage` [MessagePort/message_event](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort/message_event "The message event is fired on a MessagePort object when a message arrives on that channel.") Support in all current engines. Firefox 41+Safari 5+Chrome 2+ * * * Opera 10.6+Edge 79+ * * * Edge (Legacy)12+Internet Explorer 10+ * * * Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11.5+ [DedicatedWorkerGlobalScope/message_event](https://developer.mozilla.org/en-US/docs/Web/API/DedicatedWorkerGlobalScope/message_event "The message event is fired on a DedicatedWorkerGlobalScope object when the worker receives a message from its parent (i.e. when the parent sends a message using Worker.postMessage()).") Support in all current engines. Firefox 3.5+Safari 4+Chrome 4+ * * * Opera 10.6+Edge 79+ * * * Edge (Legacy)12+Internet Explorer 10+ * * * Firefox Android?Safari iOS 5+Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11.5+ | `message` |
| `onmessageerror` [MessagePort/messageerror_event](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort/messageerror_event "The messageerror event is fired on a MessagePort object when it receives a message that can't be deserialized.") Support in all current engines. Firefox 57+Safari 16.4+Chrome 60+ * * * Opera?Edge 79+ * * * Edge (Legacy)18 Internet Explorer No * * * Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 47+ [DedicatedWorkerGlobalScope/messageerror_event](https://developer.mozilla.org/en-US/docs/Web/API/DedicatedWorkerGlobalScope/messageerror_event "The messageerror event is fired on a DedicatedWorkerGlobalScope object when it receives a message that can't be deserialized.") Support in all current engines. Firefox 57+Safari 16.4+Chrome 60+ * * * Opera?Edge 79+ * * * Edge (Legacy)18 Internet Explorer No * * * Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 47+ | `messageerror` |

#### 9.4.4 Message ports[](https://html.spec.whatwg.org/multipage/web-messaging.html#message-ports)

[MessagePort](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort "The MessagePort interface of the Channel Messaging API represents one of the two ports of a MessageChannel, allowing messages to be sent from one port and listening out for them arriving at the other.")

Support in all current engines.

Firefox 41+Safari 5+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Each channel has two message ports. Data sent through one port is received by the other port, and vice versa.

```
[Exposed=(Window,Worker,AudioWorklet), Transferable]
interface MessagePort : EventTarget {
  undefined postMessage(any message, sequence<object> transfer);
  undefined postMessage(any message, optional StructuredSerializeOptions options = {});
  undefined start();
  undefined close();

  // event handlers
  attribute EventHandler onclose;
};

MessagePort includes MessageEventTarget;

dictionary StructuredSerializeOptions {
  sequence<object> transfer = [];
};
```
`port.postMessage(message [, transfer])`

[MessagePort/postMessage](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort/postMessage "The postMessage() method of the MessagePort interface sends a message from the port, and optionally, transfers ownership of objects to other browsing contexts.")

Support in all current engines.

Firefox 41+Safari 5+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

`port.postMessage(message [, { transfer }])`
Posts a message through the channel. Objects listed in transfer are transferred, not just cloned, meaning that they are no longer usable on the sending side.

Throws a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException` if transfer contains duplicate objects or port, or if message could not be cloned.

`port.start()`

[MessagePort/start](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort/start "The start() method of the MessagePort interface starts the sending of messages queued on the port. This method is only needed when using EventTarget.addEventListener; it is implied when using onmessage.")

Support in all current engines.

Firefox 41+Safari 5+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Begins dispatching messages received on the port.

`port.close()`

[MessagePort/close](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort/close "The close() method of the MessagePort interface disconnects the port, so it is no longer active. This stops the flow of messages to that port.")

Support in all current engines.

Firefox 41+Safari 5+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

Disconnects the port, so that it is no longer active.

Each `MessagePort` object has a message event target (a `MessageEventTarget`), to which the `message` and `messageerror` events are dispatched. Unless otherwise specified, it defaults to the `MessagePort` object itself.

Each `MessagePort` object can be entangled with another (a symmetric relationship). Each `MessagePort` object also has a [task source](https://html.spec.whatwg.org/multipage/webappapis.html#task-source) called the port message queue, initially empty. A [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) can be enabled or disabled, and is initially disabled. Once enabled, a port can never be disabled again (though messages in the queue can get moved to another queue or removed altogether, which has much the same effect). A `MessagePort` also has a has been shipped flag, which must initially be false.

If the document is [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), but the event listeners were all created in the context of documents that are _not_[fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then the messages will not be received unless and until the documents become [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active) again.

Each [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop) has a [task source](https://html.spec.whatwg.org/multipage/webappapis.html#task-source) called the unshipped port message queue. This is a virtual [task source](https://html.spec.whatwg.org/multipage/webappapis.html#task-source): it must act as if it contained the [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) of each [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) of each `MessagePort` whose [has been shipped](https://html.spec.whatwg.org/multipage/web-messaging.html#has-been-shipped) flag is false, whose [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) is enabled, and whose [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop) is that [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop), in the order in which they were added to their respective [task source](https://html.spec.whatwg.org/multipage/webappapis.html#task-source). When a [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) would be removed from the [unshipped port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#unshipped-port-message-queue), it must instead be removed from its [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue).

When a `MessagePort`'s [has been shipped](https://html.spec.whatwg.org/multipage/web-messaging.html#has-been-shipped) flag is false, its [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) must be ignored for the purposes of the [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop). (The [unshipped port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#unshipped-port-message-queue) is used instead.)

The [has been shipped](https://html.spec.whatwg.org/multipage/web-messaging.html#has-been-shipped) flag is set to true when a port, its twin, or the object it was cloned from, is or has been transferred. When a `MessagePort`'s [has been shipped](https://html.spec.whatwg.org/multipage/web-messaging.html#has-been-shipped) flag is true, its [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) acts as a first-class [task source](https://html.spec.whatwg.org/multipage/webappapis.html#task-source), unaffected to any [unshipped port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#unshipped-port-message-queue).

When the user agent is to entangle two `MessagePort` objects, it must run the following steps:

1.   If one of the ports is already entangled, then disentangle it and the port that it was entangled with.

If those two previously entangled ports were the two ports of a `MessageChannel` object, then that `MessageChannel` object no longer represents an actual channel: the two ports in that object are no longer entangled.

2.   Associate the two ports to be entangled, so that they form the two parts of a new channel. (There is no `MessageChannel` object that represents this channel.)

Two ports A and B that have gone through this step are now said to be entangled; one is entangled to the other, and vice versa.

While this specification describes this process as instantaneous, implementations are more likely to implement it via message passing. As with all algorithms, the key is "merely" that the end result be indistinguishable, in a black-box sense, from the specification.

The disentangle steps, given a `MessagePort`initiatorPort which initiates disentangling, are as follows:

1.   Let otherPort be the `MessagePort` which initiatorPort was entangled with.

2.   [Assert](https://infra.spec.whatwg.org/#assert): otherPort exists.

3.   Disentangle initiatorPort and otherPort, so that they are no longer entangled or associated with each other.

4.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `close` at otherPort.

The `close` event will be fired even if the port is not explicitly closed. The cases where this event is dispatched are:

*   the `close()` method was called;
*   the `Document` was [destroyed](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document); or
*   the `MessagePort` was [garbage collected](https://html.spec.whatwg.org/multipage/web-messaging.html#ports-and-garbage-collection).

We only dispatch the event on otherPort because initiatorPort explicitly triggered the close, its `Document` no longer exists, or it was already garbage collected, as described above.

* * *

`MessagePort` objects are [transferable objects](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects). Their [transfer steps](https://html.spec.whatwg.org/multipage/structured-data.html#transfer-steps), given value and dataHolder, are:

1.   Set value's [has been shipped](https://html.spec.whatwg.org/multipage/web-messaging.html#has-been-shipped) flag to true.

2.   Set dataHolder.[[PortMessageQueue]] to value's [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue).

3.   If value is entangled with another port remotePort, then:

    1.   Set remotePort's [has been shipped](https://html.spec.whatwg.org/multipage/web-messaging.html#has-been-shipped) flag to true.

    2.   Set dataHolder.[[RemotePort]] to remotePort.

4.   Otherwise, set dataHolder.[[RemotePort]] to null.

* * *

The message port post message steps, given sourcePort, targetPort, message, and options are as follows:

1.   Let transfer be options["`transfer`"].

2.   If transfer[contains](https://infra.spec.whatwg.org/#list-contain)sourcePort, then throw a ["`DataCloneError`"](https://webidl.spec.whatwg.org/#datacloneerror)`DOMException`.

3.   Let doomed be false.

4.   If targetPort is not null and transfer[contains](https://infra.spec.whatwg.org/#list-contain)targetPort, then set doomed to true and optionally report to a developer console that the target port was posted to itself, causing the communication channel to be lost.

5.   Let serializeWithTransferResult be [StructuredSerializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer)(message, transfer). Rethrow any exceptions.

6.   If targetPort is null, or if doomed is true, then return.

7.   Add a [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that runs the following steps to the [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) of targetPort:

    1.   Let finalTargetPort be the `MessagePort` in whose [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) the task now finds itself.

This can be different from targetPort, if targetPort itself was transferred and thus all its tasks moved along with it.

    2.   Let messageEventTarget be finalTargetPort's [message event target](https://html.spec.whatwg.org/multipage/web-messaging.html#message-event-target).

    3.   Let targetRealm be finalTargetPort's [relevant realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-realm).

    4.   Let deserializeRecord be [StructuredDeserializeWithTransfer](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserializewithtransfer)(serializeWithTransferResult, targetRealm).

If this throws an exception, catch it, [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `messageerror` at messageEventTarget, using `MessageEvent`, and then return.

    5.   Let messageClone be deserializeRecord.[[Deserialized]].

    6.   Let newPorts be a new [frozen array](https://webidl.spec.whatwg.org/#dfn-frozen-array-type) consisting of all `MessagePort` objects in deserializeRecord.[[TransferredValues]], if any, maintaining their relative order.

    7.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `message` at messageEventTarget, using `MessageEvent`, with the `data` attribute initialized to messageClone and the `ports` attribute initialized to newPorts.

The 
```
postMessage(message,
  options)
```
 method steps are:

1.   Let targetPort be the port with which [this](https://webidl.spec.whatwg.org/#this) is entangled, if any; otherwise let it be null.

2.   Run the [message port post message steps](https://html.spec.whatwg.org/multipage/web-messaging.html#message-port-post-message-steps) providing [this](https://webidl.spec.whatwg.org/#this), targetPort, message and options.

The 
```
postMessage(message,
  transfer)
```
 method steps are:

1.   Let targetPort be the port with which [this](https://webidl.spec.whatwg.org/#this) is entangled, if any; otherwise let it be null.

2.   Let options be «[ "`transfer`" → transfer ]».

3.   Run the [message port post message steps](https://html.spec.whatwg.org/multipage/web-messaging.html#message-port-post-message-steps) providing [this](https://webidl.spec.whatwg.org/#this), targetPort, message and options.

* * *

The `start()` method steps are to enable [this](https://webidl.spec.whatwg.org/#this)'s [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue), if it is not already enabled.

* * *

The `close()` method steps are:

1.   Set [this](https://webidl.spec.whatwg.org/#this)'s [[[Detached]]](https://html.spec.whatwg.org/multipage/structured-data.html#detached) internal slot value to true.

2.   If [this](https://webidl.spec.whatwg.org/#this) is entangled, [disentangle](https://html.spec.whatwg.org/multipage/web-messaging.html#disentangle) it.

* * *

The following are the [event handlers](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) (and their corresponding [event handler event types](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type)) that must be supported, as [event handler IDL attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes), by all objects implementing the `MessagePort` interface:

| [Event handler](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) | [Event handler event type](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type) |
| --- | --- |
| `onclose` | `close` |

The first time a `MessagePort` object's `onmessage` IDL attribute is set, the port's [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) must be enabled, as if the `start()` method had been called.

#### 9.4.5 Ports and garbage collection[](https://html.spec.whatwg.org/multipage/web-messaging.html#ports-and-garbage-collection)

When a `MessagePort` object o is garbage collected, if o is entangled, then the user agent must [disentangle](https://html.spec.whatwg.org/multipage/web-messaging.html#disentangle)o.

When a `MessagePort` object o is entangled and `message` or `messageerror` event listener is registered, user agents must act as if o's entangled `MessagePort` object has a strong reference to o.

Furthermore, a `MessagePort` object must not be garbage collected while there exists an event referenced by a [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) in a [task queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue) that is to be dispatched on that `MessagePort` object, or while the `MessagePort` object's [port message queue](https://html.spec.whatwg.org/multipage/web-messaging.html#port-message-queue) is enabled and not empty.

Thus, a message port can be received, given an event listener, and then forgotten, and so long as that event listener could receive a message, the channel will be maintained.

Of course, if this was to occur on both sides of the channel, then both ports could be garbage collected, since they would not be reachable from live code, despite having a strong reference to each other. However, if a message port has a pending message, it is not garbage collected.

Authors are strongly encouraged to explicitly close `MessagePort` objects to disentangle them, so that their resources can be recollected. Creating many `MessagePort` objects and discarding them without closing them can lead to high transient memory usage since garbage collection is not necessarily performed promptly, especially for `MessagePort`s where garbage collection can involve cross-process coordination.

### 9.5 Broadcasting to other browsing contexts[](https://html.spec.whatwg.org/multipage/web-messaging.html#broadcasting-to-other-browsing-contexts)

[BroadcastChannel](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel "The BroadcastChannel interface represents a named channel that any browsing context of a given origin can subscribe to. It allows communication between different documents (in different windows, tabs, frames or iframes) of the same origin. Messages are broadcasted via a message event fired at all BroadcastChannel objects listening to the channel, except the object that sent the message.")

Support in all current engines.

Firefox 38+Safari 15.4+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[Broadcast_Channel_API](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API "The Broadcast Channel API allows basic communication between browsing contexts (that is, windows, tabs, frames, or iframes) and workers on the same origin.")

Support in all current engines.

Firefox 38+Safari 15.4+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Pages on a single [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) opened by the same user in the same user agent but in different unrelated [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) sometimes need to send notifications to each other, for example "hey, the user logged in over here, check your credentials again".

For elaborate cases, e.g. to manage locking of shared state, to manage synchronization of resources between a server and multiple local clients, to share a `WebSocket` connection with a remote host, and so forth, [shared workers](https://html.spec.whatwg.org/multipage/workers.html#sharedworker) are the most appropriate solution.

For simple cases, though, where a shared worker would be an unreasonable overhead, authors can use the simple channel-based broadcast mechanism described in this section.

```
[Exposed=(Window,Worker)]
interface BroadcastChannel : EventTarget {
  constructor(DOMString name);

  readonly attribute DOMString name;
  undefined postMessage(any message);
  undefined close();
  attribute EventHandler onmessage;
  attribute EventHandler onmessageerror;
};
```
`broadcastChannel = new BroadcastChannel(name)`

[BroadcastChannel/BroadcastChannel](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel/BroadcastChannel "The BroadcastChannel() constructor creates a new BroadcastChannel and connects it to the underlying channel.")

Support in all current engines.

Firefox 38+Safari 15.4+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns a new `BroadcastChannel` object via which messages for the given channel name can be sent and received.

`broadcastChannel.name`

[BroadcastChannel/name](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel/name "The read-only BroadcastChannel.name property returns a string, which uniquely identifies the given channel with its name. This name is passed to the BroadcastChannel() constructor at creation time and is therefore read-only.")

Support in all current engines.

Firefox 38+Safari 15.4+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns the channel name (as passed to the constructor).

`broadcastChannel.postMessage(message)`

[BroadcastChannel/postMessage](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel/postMessage "The BroadcastChannel.postMessage() sends a message, which can be of any kind of Object, to each listener in any browsing context with the same origin. The message is transmitted as a 'message' event targeted at each BroadcastChannel bound to the channel.")

Support in all current engines.

Firefox 38+Safari 15.4+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Sends the given message to other `BroadcastChannel` objects set up for this channel. Messages can be structured objects, e.g. nested objects and arrays.

`broadcastChannel.close()`

[BroadcastChannel/close](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel/close "The BroadcastChannel.close() terminates the connection to the underlying channel, allowing the object to be garbage collected. This is a necessary step to perform as there is no other way for a browser to know that this channel is not needed anymore.")

Support in all current engines.

Firefox 38+Safari 15.4+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Closes the `BroadcastChannel` object, opening it up to garbage collection.

A `BroadcastChannel` object has a channel name and a closed flag.

The `new BroadcastChannel(name)` constructor steps are:

1.   Set [this](https://webidl.spec.whatwg.org/#this)'s [channel name](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-name) to name.

2.   Set [this](https://webidl.spec.whatwg.org/#this)'s [closed flag](https://html.spec.whatwg.org/multipage/web-messaging.html#concept-broadcastchannel-closed) to false.

The `name` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [channel name](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-name).

The `postMessage(message)` method steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this) is not [eligible for messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#eligible-for-messaging), then return.

2.   If [this](https://webidl.spec.whatwg.org/#this)'s [closed flag](https://html.spec.whatwg.org/multipage/web-messaging.html#concept-broadcastchannel-closed) is true, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

3.   Let serialized be [StructuredSerialize](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserialize)(message). Rethrow any exceptions.

4.   Let sourceOrigin be [this](https://webidl.spec.whatwg.org/#this)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin).

5.   Let sourceStorageKey be the result of running [obtain a storage key for non-storage purposes](https://storage.spec.whatwg.org/#obtain-a-storage-key-for-non-storage-purposes) with [this](https://webidl.spec.whatwg.org/#this)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

6.   Let destinations be a list of `BroadcastChannel` objects that match the following criteria:

    *   They are [eligible for messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#eligible-for-messaging).

    *   The result of running [obtain a storage key for non-storage purposes](https://storage.spec.whatwg.org/#obtain-a-storage-key-for-non-storage-purposes) with their [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)[equals](https://storage.spec.whatwg.org/#storage-key-equal)sourceStorageKey.

    *   Their [channel name](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-name)[is](https://infra.spec.whatwg.org/#string-is)[this](https://webidl.spec.whatwg.org/#this)'s [channel name](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-name).

7.   Remove source from destinations.

8.   Sort destinations such that all `BroadcastChannel` objects whose [relevant agents](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent) are the same are sorted in creation order, oldest first. (This does not define a complete ordering. Within this constraint, user agents may sort the list in any [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) manner.)

9.   For each destination in destinations, [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given destination's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to perform the following steps:

    1.   If destination's [closed flag](https://html.spec.whatwg.org/multipage/web-messaging.html#concept-broadcastchannel-closed) is true, then abort these steps.

    2.   Let targetRealm be destination's [relevant realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-realm).

    3.   Let data be [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)(serialized, targetRealm).

If this throws an exception, catch it, [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `messageerror` at destination, using `MessageEvent`, with its [origin](https://html.spec.whatwg.org/multipage/comms.html#concept-messageevent-origin) initialized to sourceOrigin, and then abort these steps.

    4.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `message` at destination, using `MessageEvent`, with the `data` attribute initialized to data and its [origin](https://html.spec.whatwg.org/multipage/comms.html#concept-messageevent-origin) initialized to sourceOrigin.

While a `BroadcastChannel` object whose [closed flag](https://html.spec.whatwg.org/multipage/web-messaging.html#concept-broadcastchannel-closed) is false has an event listener registered for `message` or `messageerror` events, there must be a strong reference from the `BroadcastChannel` object's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to the `BroadcastChannel` object itself.

The `close()` method steps are to set [this](https://webidl.spec.whatwg.org/#this)'s [closed flag](https://html.spec.whatwg.org/multipage/web-messaging.html#concept-broadcastchannel-closed) to true.

Authors are strongly encouraged to explicitly close `BroadcastChannel` objects when they are no longer needed, so that they can be garbage collected. Creating many `BroadcastChannel` objects and discarding them while leaving them with an event listener and without closing them can lead to an apparent memory leak, since the objects will continue to live for as long as they have an event listener (or until their page or worker is closed).

* * *

The following are the [event handlers](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) (and their corresponding [event handler event types](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type)) that must be supported, as [event handler IDL attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes), by all objects implementing the `BroadcastChannel` interface:

| [Event handler](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) | [Event handler event type](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-event-type) |
| --- | --- |
| `onmessage` [BroadcastChannel/message_event](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel/message_event "The message event is fired on a BroadcastChannel object when a message arrives on that channel.") Support in all current engines. Firefox 38+Safari 15.4+Chrome 54+ * * * Opera?Edge 79+ * * * Edge (Legacy)?Internet Explorer No * * * Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android? | `message` |
| `onmessageerror` [BroadcastChannel/messageerror_event](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel/messageerror_event "The messageerror event is fired on a BroadcastChannel object when a message that can't be deserialized arrives on the channel.") Support in all current engines. Firefox 57+Safari 15.4+Chrome 60+ * * * Opera?Edge 79+ * * * Edge (Legacy)?Internet Explorer No * * * Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 47+ | `messageerror` |

Suppose a page wants to know when the user logs out, even when the user does so from another tab at the same site:

```
var authChannel = new BroadcastChannel('auth');
authChannel.onmessage = function (event) {
  if (event.data == 'logout')
    showLogout();
}

function logoutRequested() {
  // called when the user asks us to log them out
  doLogout();
  showLogout();
  authChannel.postMessage('logout');
}

function doLogout() {
  // actually log the user out (e.g. clearing cookies)
  // ...
}

function showLogout() {
  // update the UI to indicate we're logged out
  // ...
}
```

[← 9.2 Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [10 Web workers →](https://html.spec.whatwg.org/multipage/workers.html)
