# Source: https://html.spec.whatwg.org/multipage/comms.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/comms.html

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 8.10 Images](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [9.2 Server-sent events →](https://html.spec.whatwg.org/multipage/server-sent-events.html)
1.   [9 Communication](https://html.spec.whatwg.org/multipage/comms.html#comms)
    1.   [9.1 The `MessageEvent` interface](https://html.spec.whatwg.org/multipage/comms.html#the-messageevent-interface)

9 Communication[](https://html.spec.whatwg.org/multipage/comms.html#comms)
--------------------------------------------------------------------------

[](https://html.spec.whatwg.org/multipage/comms.html#network)The `WebSocket` interface used to be defined here. It is now defined in WebSockets. [[WEBSOCKETS]](https://html.spec.whatwg.org/multipage/references.html#refsWEBSOCKETS)

### 9.1 The `MessageEvent` interface[](https://html.spec.whatwg.org/multipage/comms.html#the-messageevent-interface)

[MessageEvent](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent "The MessageEvent interface represents a message received by a target object.")

Support in all current engines.

Firefox 3+Safari 4+Chrome 2+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

Messages in [server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events), [cross-document messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#web-messaging), [channel messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-messaging), [broadcast channels](https://html.spec.whatwg.org/multipage/web-messaging.html#broadcasting-to-other-browsing-contexts), and WebSockets use the `MessageEvent` interface for their `message` events: [[WEBSOCKETS]](https://html.spec.whatwg.org/multipage/references.html#refsWEBSOCKETS)

```
[Exposed=(Window,Worker,AudioWorklet)]
interface MessageEvent : Event {
  constructor(DOMString type, optional MessageEventInit eventInitDict = {});

  readonly attribute any data;
  readonly attribute USVString origin;
  readonly attribute DOMString lastEventId;
  readonly attribute MessageEventSource? source;
  readonly attribute FrozenArray<MessagePort> ports;

  undefined initMessageEvent(DOMString type, optional boolean bubbles = false, optional boolean cancelable = false, optional any data = null, optional USVString origin = "", optional DOMString lastEventId = "", optional MessageEventSource? source = null, optional sequence<MessagePort> ports = []);
};

dictionary MessageEventInit : EventInit {
  any data = null;
  USVString origin = "";
  DOMString lastEventId = "";
  MessageEventSource? source = null;
  sequence<MessagePort> ports = [];
};

typedef (WindowProxy or MessagePort or ServiceWorker) MessageEventSource;
```

Each `MessageEvent` has an origin (an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin), a string, or null), initially null.

`event.data`

[MessageEvent/data](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent/data "The data read-only property of the MessageEvent interface represents the data sent by the message emitter.")

Support in all current engines.

Firefox 3+Safari 4+Chrome 2+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

Returns the data of the message.

`event.origin`

[MessageEvent/origin](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent/origin "The origin read-only property of the MessageEvent interface is a string representing the origin of the message emitter.")

Support in all current engines.

Firefox 3+Safari 4+Chrome 2+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

Returns the origin of the message, for [server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) and [cross-document messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#web-messaging).

`event.lastEventId`

[MessageEvent/lastEventId](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent/lastEventId "The lastEventId read-only property of the MessageEvent interface is a string representing a unique ID for the event.")

Support in all current engines.

Firefox 3+Safari 4+Chrome 2+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)17+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

Returns the [last event ID string](https://html.spec.whatwg.org/multipage/server-sent-events.html#concept-event-stream-last-event-id), for [server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events).

`event.source`

[MessageEvent/source](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent/source "The source read-only property of the MessageEvent interface is a MessageEventSource (which can be a WindowProxy, MessagePort, or ServiceWorker object) representing the message emitter.")

Support in all current engines.

Firefox 3+Safari 4+Chrome 2+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

Returns the `WindowProxy` of the source window, for [cross-document messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#web-messaging), and the `MessagePort` being attached, in the `connect` event fired at `SharedWorkerGlobalScope` objects.

`event.ports`

[MessageEvent/ports](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent/ports "The ports read-only property of the MessageEvent interface is an array of MessagePort objects representing the ports associated with the channel the message is being sent through (where appropriate, e.g. in channel messaging or when sending a message to a shared worker).")

Support in all current engines.

Firefox 3+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

Returns the `MessagePort` array sent with the message, for [cross-document messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#web-messaging) and [channel messaging](https://html.spec.whatwg.org/multipage/web-messaging.html#channel-messaging).

The `data` attribute must return the value it was initialized to. It represents the message being sent.

Objects implementing the `MessageEvent` interface's [extract an origin](https://html.spec.whatwg.org/multipage/browsers.html#extract-an-origin) steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [origin](https://html.spec.whatwg.org/multipage/comms.html#concept-messageevent-origin) if it is an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin); otherwise null.

The `lastEventId` attribute must return the value it was initialized to. It represents, in [server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events), the [last event ID string](https://html.spec.whatwg.org/multipage/server-sent-events.html#concept-event-stream-last-event-id) of the event source.

The 
```
initMessageEvent(type, bubbles,
  cancelable, data, origin, lastEventId,
  source, ports)
```
 method must initialize the event in a manner analogous to the similarly-named `initEvent()` method. [[DOM]](https://html.spec.whatwg.org/multipage/references.html#refsDOM)

Various APIs (e.g., `WebSocket`, `EventSource`) use the `MessageEvent` interface for their `message` event without using the `MessagePort` API.

[← 8.10 Images](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [9.2 Server-sent events →](https://html.spec.whatwg.org/multipage/server-sent-events.html)
