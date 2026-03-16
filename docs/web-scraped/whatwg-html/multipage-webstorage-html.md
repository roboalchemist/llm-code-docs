# Source: https://html.spec.whatwg.org/multipage/webstorage.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/webstorage.html

Published Time: Mon, 16 Mar 2026 07:32:48 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 11 Worklets](https://html.spec.whatwg.org/multipage/worklets.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [13 The HTML syntax →](https://html.spec.whatwg.org/multipage/syntax.html)
1.   [12 Web storage](https://html.spec.whatwg.org/multipage/webstorage.html#webstorage)
    1.   [12.1 Introduction](https://html.spec.whatwg.org/multipage/webstorage.html#introduction-15)
    2.   [12.2 The API](https://html.spec.whatwg.org/multipage/webstorage.html#storage)
        1.   [12.2.1 The `Storage` interface](https://html.spec.whatwg.org/multipage/webstorage.html#the-storage-interface)
        2.   [12.2.2 The `sessionStorage` getter](https://html.spec.whatwg.org/multipage/webstorage.html#the-sessionstorage-attribute)
        3.   [12.2.3 The `localStorage` getter](https://html.spec.whatwg.org/multipage/webstorage.html#the-localstorage-attribute)
        4.   [12.2.4 The `StorageEvent` interface](https://html.spec.whatwg.org/multipage/webstorage.html#the-storageevent-interface)

    3.   [12.3 Privacy](https://html.spec.whatwg.org/multipage/webstorage.html#privacy)
        1.   [12.3.1 User tracking](https://html.spec.whatwg.org/multipage/webstorage.html#user-tracking)
        2.   [12.3.2 Sensitivity of data](https://html.spec.whatwg.org/multipage/webstorage.html#sensitivity-of-data)

    4.   [12.4 Security](https://html.spec.whatwg.org/multipage/webstorage.html#security-storage)
        1.   [12.4.1 DNS spoofing attacks](https://html.spec.whatwg.org/multipage/webstorage.html#dns-spoofing-attacks)
        2.   [12.4.2 Cross-directory attacks](https://html.spec.whatwg.org/multipage/webstorage.html#cross-directory-attacks)
        3.   [12.4.3 Implementation risks](https://html.spec.whatwg.org/multipage/webstorage.html#implementation-risks)

12 Web storage[](https://html.spec.whatwg.org/multipage/webstorage.html#webstorage)
-----------------------------------------------------------------------------------

[Web_Storage_API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API "The Web Storage API provides mechanisms by which browsers can store key/value pairs, in a much more intuitive fashion than using cookies.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android 6+Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

### 12.1 Introduction[](https://html.spec.whatwg.org/multipage/webstorage.html#introduction-15)

_This section is non-normative._

This specification introduces two related mechanisms, similar to HTTP session cookies, for storing name-value pairs on the client side. [[COOKIES]](https://html.spec.whatwg.org/multipage/references.html#refsCOOKIES)

The first is designed for scenarios where the user is carrying out a single transaction, but could be carrying out multiple transactions in different windows at the same time.

Cookies don't really handle this case well. For example, a user could be buying plane tickets in two different windows, using the same site. If the site used cookies to keep track of which ticket the user was buying, then as the user clicked from page to page in both windows, the ticket currently being purchased would "leak" from one window to the other, potentially causing the user to buy two tickets for the same flight without noticing.

To address this, this specification introduces the `sessionStorage` getter. Sites can add data to the session storage, and it will be accessible to any page from the same site opened in that window.

For example, a page could have a checkbox that the user ticks to indicate that they want insurance:

```
<label>
 <input type="checkbox" onchange="sessionStorage.insurance = checked ? 'true' : ''">
  I want insurance on this trip.
</label>
```

A later page could then check, from script, whether the user had checked the checkbox or not:

`if (sessionStorage.insurance) { ... }`
If the user had multiple windows opened on the site, each one would have its own individual copy of the session storage object.

The second storage mechanism is designed for storage that spans multiple windows, and lasts beyond the current session. In particular, web applications might wish to store megabytes of user data, such as entire user-authored documents or a user's mailbox, on the client side for performance reasons.

Again, cookies do not handle this case well, because they are transmitted with every request.

The `localStorage` getter is used to access a page's local storage area.

The site at example.com can display a count of how many times the user has loaded its page by putting the following at the bottom of its page:

```
<p>
  You have viewed this page
  <span id="count">an untold number of</span>
  time(s).
</p>
<script>
  if (!localStorage.pageLoadCount)
    localStorage.pageLoadCount = 0;
  localStorage.pageLoadCount = parseInt(localStorage.pageLoadCount) + 1;
  document.getElementById('count').textContent = localStorage.pageLoadCount;
</script>
```

Each site has its own separate storage area.

The `localStorage` getter provides access to shared state. This specification does not define the interaction with other agent clusters in a multiprocess user agent, and authors are encouraged to assume that there is no locking mechanism. A site could, for instance, try to read the value of a key, increment its value, then write it back out, using the new value as a unique identifier for the session; if the site does this twice in two different browser windows at the same time, it might end up using the same "unique" identifier for both sessions, with potentially disastrous effects.

### 12.2 The API[](https://html.spec.whatwg.org/multipage/webstorage.html#storage)

[Storage](https://developer.mozilla.org/en-US/docs/Web/API/Storage "The Storage interface of the Web Storage API provides access to a particular domain's session or local storage. It allows, for example, the addition, modification, or deletion of stored data items.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android 6+Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

#### 12.2.1 The `Storage` interface[](https://html.spec.whatwg.org/multipage/webstorage.html#the-storage-interface)

```
[Exposed=Window]
interface Storage {
  readonly attribute unsigned long length;
  DOMString? key(unsigned long index);
  getter DOMString? getItem(DOMString key);
  setter undefined setItem(DOMString key, DOMString value);
  deleter undefined removeItem(DOMString key);
  undefined clear();
};
```
`storage.length`

[Storage/length](https://developer.mozilla.org/en-US/docs/Web/API/Storage/length "The length read-only property of the Storage interface returns the number of data items stored in a given Storage object.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android 6+Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

Returns the number of key/value pairs.

`storage.key (n)`

[Storage/key](https://developer.mozilla.org/en-US/docs/Web/API/Storage/key "The key() method of the Storage interface, when passed a number n, returns the name of the nth key in a given Storage object. The order of keys is user-agent defined, so you should not rely on it.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android 6+Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

Returns the name of the n th key, or null if n is greater than or equal to the number of key/value pairs.

`value = storage.getItem (key)`

[Storage/getItem](https://developer.mozilla.org/en-US/docs/Web/API/Storage/getItem "The getItem() method of the Storage interface, when passed a key name, will return that key's value, or null if the key does not exist, in the given Storage object.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android 6+Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

`value = storage[key]`
Returns the current value associated with the given key, or null if the given key does not exist.

`storage.setItem (key, value)`

[Storage/setItem](https://developer.mozilla.org/en-US/docs/Web/API/Storage/setItem "The setItem() method of the Storage interface, when passed a key name and value, will add that key to the given Storage object, or update that key's value if it already exists.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android 6+Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

`storage[key] = value`
Sets the value of the pair identified by key to value, creating a new key/value pair if none existed for key previously.

Throws a `QuotaExceededError` if the new value couldn't be set. (Setting could fail if, e.g., the user has disabled storage for the site, or if the quota has been exceeded.)

Dispatches a `storage` event on `Window` objects holding an equivalent `Storage` object.

`storage.removeItem (key)`

[Storage/removeItem](https://developer.mozilla.org/en-US/docs/Web/API/Storage/removeItem "The removeItem() method of the Storage interface, when passed a key name, will remove that key from the given Storage object if it exists. The Storage interface of the Web Storage API provides access to a particular domain's session or local storage.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android 6+Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

`delete`storage[key]
Removes the key/value pair with the given key, if a key/value pair with the given key exists.

Dispatches a `storage` event on `Window` objects holding an equivalent `Storage` object.

`storage.clear()`

[Storage/clear](https://developer.mozilla.org/en-US/docs/Web/API/Storage/clear "The clear() method of the Storage interface clears all keys stored in a given Storage object.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android 6+Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

Removes all key/value pairs, if there are any.

Dispatches a `storage` event on `Window` objects holding an equivalent `Storage` object.

A `Storage` object has an associated:

map A [storage proxy map](https://storage.spec.whatwg.org/#storage-proxy-map).type"`local`" or "`session`". 
Unfortunate as it is, iteration order is not defined and can change upon most mutations.

To broadcast a `Storage` object storage, given a key, oldValue, and newValue, run these steps:

1.   Let thisDocument be storage's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window).

2.   Let url be the [serialization](https://url.spec.whatwg.org/#concept-url-serializer) of thisDocument's [URL](https://dom.spec.whatwg.org/#concept-document-url).

3.   Let remoteStorages be all `Storage` objects excluding storage whose:

    *   [type](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-type) is storage's [type](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-type)
    *   [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) is [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with storage's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)

and, if [type](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-type) is "`session`", whose [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window)'s [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable) is thisDocument's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable).

4.   [For each](https://infra.spec.whatwg.org/#list-iterate)remoteStorage of remoteStorages: [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given remoteStorage's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `storage` at remoteStorage's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), using `StorageEvent`, with `key` initialized to key, `oldValue` initialized to oldValue, `newValue` initialized to newValue, `url` initialized to url, and `storageArea` initialized to remoteStorage.

The `Document` object associated with the resulting [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) is not necessarily [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), but events fired on such objects are ignored by the [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop) until the `Document` becomes [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active) again.

* * *

The `length` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map)'s [size](https://infra.spec.whatwg.org/#map-size).

The `key(index)` method steps are:

1.   If index is greater than or equal to [this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map)'s [size](https://infra.spec.whatwg.org/#map-size), then return null.

2.   Let keys be the result of running [get the keys](https://infra.spec.whatwg.org/#map-getting-the-keys) on [this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map).

3.   Return keys[index].

The `getItem(key)` method steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map)[key] does not [exist](https://infra.spec.whatwg.org/#map-exists), then return null.

2.   Return [this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map)[key].

The 
```
setItem(key,
  value)
```
 method steps are:

1.   Let oldValue be null.

2.   Let reorder be true.

3.   If [this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map)[key] [exists](https://infra.spec.whatwg.org/#map-exists):

    1.   Set oldValue to [this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map)[key].

    2.   If oldValue[is](https://infra.spec.whatwg.org/#string-is)value, then return.

    3.   Set reorder to false.

4.   If value cannot be stored, then throw a `QuotaExceededError`.

5.   [Set](https://infra.spec.whatwg.org/#map-set)[this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map)[key] to value.

6.   If reorder is true, then [reorder](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-reorder)[this](https://webidl.spec.whatwg.org/#this).

7.   [Broadcast](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-broadcast)[this](https://webidl.spec.whatwg.org/#this) with key, oldValue, and value.

The `removeItem(key)` method steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map)[key] does not [exist](https://infra.spec.whatwg.org/#map-exists), then return.

2.   Set oldValue to [this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map)[key].

3.   [Remove](https://infra.spec.whatwg.org/#map-remove)[this](https://webidl.spec.whatwg.org/#this)'s [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map)[key].

4.   [Reorder](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-reorder)[this](https://webidl.spec.whatwg.org/#this).

5.   [Broadcast](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-broadcast)[this](https://webidl.spec.whatwg.org/#this) with key, oldValue, and null.

#### 12.2.2 The `sessionStorage` getter[](https://html.spec.whatwg.org/multipage/webstorage.html#the-sessionstorage-attribute)

```
interface mixin WindowSessionStorage {
  readonly attribute Storage sessionStorage;
};
Window includes WindowSessionStorage;
```
`window.sessionStorage`

[Window/sessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage "The read-only sessionStorage property accesses a session Storage object for the current origin. sessionStorage is similar to localStorage; the difference is that while data in localStorage doesn't expire, data in sessionStorage is cleared when the page session ends.")

Support in all current engines.

Firefox 2+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

Returns the `Storage` object associated with that window's origin's session storage area.

Throws a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException` if the `Document`'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque) or if the request violates a policy decision (e.g., if the user agent is configured to not allow the page to persist data).

A `Document` object has an associated session storage holder, which is null or a `Storage` object. It is initially null.

[![Image 2: (This is a tracking vector.)](https://resources.whatwg.org/tracking-vector.svg)](https://infra.spec.whatwg.org/#tracking-vector "There is a tracking vector here.") The `sessionStorage` getter steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window)'s [session storage holder](https://html.spec.whatwg.org/multipage/webstorage.html#session-storage-holder) is non-null, then return [this](https://webidl.spec.whatwg.org/#this)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window)'s [session storage holder](https://html.spec.whatwg.org/multipage/webstorage.html#session-storage-holder).

2.   Let map be the result of running [obtain a session storage bottle map](https://storage.spec.whatwg.org/#obtain-a-session-storage-bottle-map) with [this](https://webidl.spec.whatwg.org/#this)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object) and "`sessionStorage`".

3.   If map is failure, then throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException`.

4.   Let storage be a new `Storage` object whose [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map) is map.

5.   Set [this](https://webidl.spec.whatwg.org/#this)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window)'s [session storage holder](https://html.spec.whatwg.org/multipage/webstorage.html#session-storage-holder) to storage.

6.   Return storage.

After [creating a new auxiliary browsing context and document](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-auxiliary-browsing-context), the session storage [is copied](https://html.spec.whatwg.org/multipage/document-sequences.html#copy-session-storage) over.

#### 12.2.3 The `localStorage` getter[](https://html.spec.whatwg.org/multipage/webstorage.html#the-localstorage-attribute)

```
interface mixin WindowLocalStorage {
  readonly attribute Storage localStorage;
};
Window includes WindowLocalStorage;
```
`window.localStorage`

[Window/localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage "The localStorage read-only property of the window interface allows you to access a Storage object for the Document's origin; the stored data is saved across browser sessions.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 11+

Returns the `Storage` object associated with window's origin's local storage area.

Throws a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException` if the `Document`'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque) or if the request violates a policy decision (e.g., if the user agent is configured to not allow the page to persist data).

A `Document` object has an associated local storage holder, which is null or a `Storage` object. It is initially null.

[![Image 3: (This is a tracking vector.)](https://resources.whatwg.org/tracking-vector.svg)](https://infra.spec.whatwg.org/#tracking-vector "There is a tracking vector here.") The `localStorage` getter steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window)'s [local storage holder](https://html.spec.whatwg.org/multipage/webstorage.html#local-storage-holder) is non-null, then return [this](https://webidl.spec.whatwg.org/#this)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window)'s [local storage holder](https://html.spec.whatwg.org/multipage/webstorage.html#local-storage-holder).

2.   Let map be the result of running [obtain a local storage bottle map](https://storage.spec.whatwg.org/#obtain-a-local-storage-bottle-map) with [this](https://webidl.spec.whatwg.org/#this)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object) and "`localStorage`".

3.   If map is failure, then throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException`.

4.   Let storage be a new `Storage` object whose [map](https://html.spec.whatwg.org/multipage/webstorage.html#concept-storage-map) is map.

5.   Set [this](https://webidl.spec.whatwg.org/#this)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window)'s [local storage holder](https://html.spec.whatwg.org/multipage/webstorage.html#local-storage-holder) to storage.

6.   Return storage.

#### 12.2.4 The `StorageEvent` interface[](https://html.spec.whatwg.org/multipage/webstorage.html#the-storageevent-interface)

[StorageEvent](https://developer.mozilla.org/en-US/docs/Web/API/StorageEvent "The StorageEvent interface is implemented by the storage event, which is sent to a window when a storage area the window has access to is changed within the context of another document.")

Support in all current engines.

Firefox 13+Safari 4+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS 3+Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

```
[Exposed=Window]
interface StorageEvent : Event {
  constructor(DOMString type, optional StorageEventInit eventInitDict = {});

  readonly attribute DOMString? key;
  readonly attribute DOMString? oldValue;
  readonly attribute DOMString? newValue;
  readonly attribute USVString url;
  readonly attribute Storage? storageArea;

  undefined initStorageEvent(DOMString type, optional boolean bubbles = false, optional boolean cancelable = false, optional DOMString? key = null, optional DOMString? oldValue = null, optional DOMString? newValue = null, optional USVString url = "", optional Storage? storageArea = null);
};

dictionary StorageEventInit : EventInit {
  DOMString? key = null;
  DOMString? oldValue = null;
  DOMString? newValue = null;
  USVString url = "";
  Storage? storageArea = null;
};
```
`event.key`
Returns the key of the storage item being changed.

`event.oldValue`
Returns the old value of the key of the storage item whose value is being changed.

`event.newValue`
Returns the new value of the key of the storage item whose value is being changed.

`event.url`
Returns the [URL](https://dom.spec.whatwg.org/#concept-document-url) of the document whose storage item changed.

`event.storageArea`
Returns the `Storage` object that was affected.

The `key`, `oldValue`, `newValue`, `url`, and `storageArea` attributes must return the values they were initialized to.

The 
```
initStorageEvent(type, bubbles,
  cancelable, key, oldValue, newValue, url,
  storageArea)
```
 method must initialize the event in a manner analogous to the similarly-named `initEvent()` method. [[DOM]](https://html.spec.whatwg.org/multipage/references.html#refsDOM)

### 12.3 Privacy[](https://html.spec.whatwg.org/multipage/webstorage.html#privacy)

#### 12.3.1 User tracking[](https://html.spec.whatwg.org/multipage/webstorage.html#user-tracking)

A third-party advertiser (or any entity capable of getting content distributed to multiple sites) could use a unique identifier stored in its local storage area to track a user across multiple sessions, building a profile of the user's interests to allow for highly targeted advertising. In conjunction with a site that is aware of the user's real identity (for example an e-commerce site that requires authenticated credentials), this could allow oppressive groups to target individuals with greater accuracy than in a world with purely anonymous web usage.

There are a number of techniques that can be used to mitigate the risk of user tracking:

Blocking third-party storage
User agents may restrict access to the `localStorage` objects to scripts originating at the domain of the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of the [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable), for instance denying access to the API for pages from other domains running in `iframe`s.

Expiring stored data
User agents may, possibly in a manner configured by the user, automatically delete stored data after a period of time.

For example, a user agent could be configured to treat third-party local storage areas as session-only storage, deleting the data once the user had closed all the [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) that could access it.

This can restrict the ability of a site to track a user, as the site would then only be able to track the user across multiple sessions when they authenticate with the site itself (e.g. by making a purchase or logging in to a service).

However, this also reduces the usefulness of the API as a long-term storage mechanism. It can also put the user's data at risk, if the user does not fully understand the implications of data expiration.

Treating persistent storage as cookies
If users attempt to protect their privacy by clearing cookies without also clearing data stored in the local storage area, sites can defeat those attempts by using the two features as redundant backup for each other. User agents should present the interfaces for clearing these in a way that helps users to understand this possibility and enables them to delete data in all persistent storage features simultaneously. [[COOKIES]](https://html.spec.whatwg.org/multipage/references.html#refsCOOKIES)

Site-specific safelisting of access to local storage areas
User agents may allow sites to access session storage areas in an unrestricted manner, but require the user to authorize access to local storage areas.

Origin-tracking of stored data
User agents may record the [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) of sites that contained content from third-party origins that caused data to be stored.

If this information is then used to present the view of data currently in persistent storage, it would allow the user to make informed decisions about which parts of the persistent storage to prune. Combined with a blocklist ("delete this data and prevent this domain from ever storing data again"), the user can restrict the use of persistent storage to sites that they trust.

Shared blocklists
User agents may allow users to share their persistent storage domain blocklists.

This would allow communities to act together to protect their privacy.

While these suggestions prevent trivial use of this API for user tracking, they do not block it altogether. Within a single domain, a site can continue to track the user during a session, and can then pass all this information to the third party along with any identifying information (names, credit card numbers, addresses) obtained by the site. If a third party cooperates with multiple sites to obtain such information, a profile can still be created.

However, user tracking is to some extent possible even with no cooperation from the user agent whatsoever, for instance by using session identifiers in URLs, a technique already commonly used for innocuous purposes but easily repurposed for user tracking (even retroactively). This information can then be shared with other sites, using visitors' IP addresses and other user-specific data (e.g. user-agent headers and configuration settings) to combine separate sessions into coherent user profiles.

#### 12.3.2 Sensitivity of data[](https://html.spec.whatwg.org/multipage/webstorage.html#sensitivity-of-data)

User agents should treat persistently stored data as potentially sensitive; it's quite possible for emails, calendar appointments, health records, or other confidential documents to be stored in this mechanism.

To this end, user agents should ensure that when deleting data, it is promptly deleted from the underlying storage.

### 12.4 Security[](https://html.spec.whatwg.org/multipage/webstorage.html#security-storage)

#### 12.4.1 DNS spoofing attacks[](https://html.spec.whatwg.org/multipage/webstorage.html#dns-spoofing-attacks)

Because of the potential for DNS spoofing attacks, one cannot guarantee that a host claiming to be in a certain domain really is from that domain. To mitigate this, pages can use TLS. Pages using TLS can be sure that only the user, software working on behalf of the user, and other pages using TLS that have certificates identifying them as being from the same domain, can access their storage areas.

#### 12.4.2 Cross-directory attacks[](https://html.spec.whatwg.org/multipage/webstorage.html#cross-directory-attacks)

Different authors sharing one host name, for example users hosting content on the now defunct `geocities.com`, all share one local storage object. There is no feature to restrict the access by pathname. Authors on shared hosts are therefore urged to avoid using these features, as it would be trivial for other authors to read the data and overwrite it.

Even if a path-restriction feature was made available, the usual DOM scripting security model would make it trivial to bypass this protection and access the data from any path.

#### 12.4.3 Implementation risks[](https://html.spec.whatwg.org/multipage/webstorage.html#implementation-risks)

The two primary risks when implementing these persistent storage features are letting hostile sites read information from other domains, and letting hostile sites write information that is then read from other domains.

Letting third-party sites read data that is not supposed to be read from their domain causes _information leakage_. For example, a user's shopping wishlist on one domain could be used by another domain for targeted advertising; or a user's work-in-progress confidential documents stored by a word-processing site could be examined by the site of a competing company.

Letting third-party sites write data to the persistent storage of other domains can result in _information spoofing_, which is equally dangerous. For example, a hostile site could add items to a user's wishlist; or a hostile site could set a user's session identifier to a known ID that the hostile site can then use to track the user's actions on the victim site.

Thus, strictly following the [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) model described in this specification is important for user security.

[← 11 Worklets](https://html.spec.whatwg.org/multipage/worklets.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [13 The HTML syntax →](https://html.spec.whatwg.org/multipage/syntax.html)
