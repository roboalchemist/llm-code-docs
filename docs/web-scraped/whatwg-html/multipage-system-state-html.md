# Source: https://html.spec.whatwg.org/multipage/system-state.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/system-state.html

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 8.6 Timers](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [8.10 Images →](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html)
1.       1.   [8.9 System state and capabilities](https://html.spec.whatwg.org/multipage/system-state.html#system-state-and-capabilities)
        1.   [8.9.1 The `Navigator` object](https://html.spec.whatwg.org/multipage/system-state.html#the-navigator-object)
            1.   [8.9.1.1 Client identification](https://html.spec.whatwg.org/multipage/system-state.html#client-identification)
            2.   [8.9.1.2 Language preferences](https://html.spec.whatwg.org/multipage/system-state.html#language-preferences)
            3.   [8.9.1.3 Browser state](https://html.spec.whatwg.org/multipage/system-state.html#navigator.online)
            4.   [8.9.1.4 Custom scheme handlers: the `registerProtocolHandler()` method](https://html.spec.whatwg.org/multipage/system-state.html#custom-handlers)
                1.   [8.9.1.4.1 Security and privacy](https://html.spec.whatwg.org/multipage/system-state.html#security-and-privacy)
                2.   [8.9.1.4.2 User agent automation](https://html.spec.whatwg.org/multipage/system-state.html#user-agent-automation)

            5.   [8.9.1.5 Cookies](https://html.spec.whatwg.org/multipage/system-state.html#cookies)
            6.   [8.9.1.6 PDF viewing support](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewing-support)

### 8.9 System state and capabilities[](https://html.spec.whatwg.org/multipage/system-state.html#system-state-and-capabilities)

#### 8.9.1 The `Navigator` object[](https://html.spec.whatwg.org/multipage/system-state.html#the-navigator-object)

[Navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator "The Navigator interface represents the state and the identity of the user agent. It allows scripts to query it and to register themselves to carry on some activities.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 3+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Instances of `Navigator` represent the identity and state of the user agent (the client). It has also been used as a generic global under which various APIs are located, but this is not precedent to build upon. Instead use the `WindowOrWorkerGlobalScope` mixin or equivalent.

```
[Exposed=Window]
interface Navigator {
  // objects implementing this interface also implement the interfaces given below
};
Navigator includes NavigatorID;
Navigator includes NavigatorLanguage;
Navigator includes NavigatorOnLine;
Navigator includes NavigatorContentUtils;
Navigator includes NavigatorCookies;
Navigator includes NavigatorPlugins;
Navigator includes NavigatorConcurrentHardware;
```

These interface mixins are defined separately so that `WorkerNavigator` can reuse parts of the `Navigator` interface.

Each `Window` has an associated `Navigator`, which is a `Navigator` object. Upon creation of the `Window` object, its [associated `Navigator`](https://html.spec.whatwg.org/multipage/system-state.html#associated-navigator) must be set to a [new](https://webidl.spec.whatwg.org/#new)`Navigator` object created in the `Window` object's [relevant realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-realm).

[Window/navigator](https://developer.mozilla.org/en-US/docs/Web/API/Window/navigator "The Window.navigator read-only property returns a reference to the Navigator object, which has methods and properties about the application running the script.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 3+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

The `navigator` and `clientInformation` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [associated `Navigator`](https://html.spec.whatwg.org/multipage/system-state.html#associated-navigator).

##### 8.9.1.1 Client identification[](https://html.spec.whatwg.org/multipage/system-state.html#client-identification)

```
interface mixin NavigatorID {
  readonly attribute DOMString appCodeName; // constant "Mozilla"
  readonly attribute DOMString appName; // constant "Netscape"
  readonly attribute DOMString appVersion;
  readonly attribute DOMString platform;
  readonly attribute DOMString product; // constant "Gecko"
  [Exposed=Window] readonly attribute DOMString productSub;
  readonly attribute DOMString userAgent;
  [Exposed=Window] readonly attribute DOMString vendor;
  [Exposed=Window] readonly attribute DOMString vendorSub; // constant ""
};
```

In certain cases, despite the best efforts of the entire industry, web browsers have bugs and limitations that web authors are forced to work around.

This section defines a collection of attributes that can be used to determine, from script, the kind of user agent in use, in order to work around these issues.

The user agent has a navigator compatibility mode, which is either _Chrome_, _Gecko_, or _WebKit_.

The [navigator compatibility mode](https://html.spec.whatwg.org/multipage/system-state.html#concept-navigator-compatibility-mode) constrains the `NavigatorID` mixin to the combinations of attribute values and presence of `taintEnabled()` and `oscpu` that are known to be compatible with existing web content.

Client detection should always be limited to detecting known current versions; future versions and unknown versions should always be assumed to be fully compliant.

`self.navigator.appCodeName`
Returns the string "`Mozilla`".

`self.navigator.appName`
Returns the string "`Netscape`".

`self.navigator.appVersion`
Returns the version of the browser.

`self.navigator.platform`
Returns the name of the platform.

`self.navigator.product`
Returns the string "`Gecko`".

`window.navigator.productSub`
Returns either the string "`20030107`", or the string "`20100101`".

`self.navigator.userAgent`

[Navigator/userAgent](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/userAgent "The Navigator.userAgent read-only property returns the user agent string for the current browser.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[WorkerNavigator/userAgent](https://developer.mozilla.org/en-US/docs/Web/API/WorkerNavigator/userAgent "The WorkerNavigator.userAgent read-only property returns the user agent string for the current browser.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 5+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Returns the complete ``User-Agent`` header.

`window.navigator.vendor`
Returns either the empty string, the string "`Apple Computer, Inc.`", or the string "`Google Inc.`".

`window.navigator.vendorSub`
Returns the empty string.

The `appCodeName` getter steps are to return "`Mozilla`".

The `appName` getter steps are to return "`Netscape`".

The `appVersion` getter steps are:

1.   Let userAgent be [this](https://webidl.spec.whatwg.org/#this)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [environment default ``User-Agent`` value](https://fetch.spec.whatwg.org/#environment-default-user-agent-value).

2.   If userAgent does not start with ``Mozilla/5.0 (``, then return the empty string.

3.   Let trail be the substring of userAgent, [isomorphic decoded](https://infra.spec.whatwg.org/#isomorphic-decode), that follows the "`Mozilla/`" prefix.

4.   If the [navigator compatibility mode](https://html.spec.whatwg.org/multipage/system-state.html#concept-navigator-compatibility-mode) is _Chrome_ or _WebKit_
Return trail.

If the [navigator compatibility mode](https://html.spec.whatwg.org/multipage/system-state.html#concept-navigator-compatibility-mode) is _Gecko_
If trail starts with "`5.0 (Windows`", then return "`5.0 (Windows)`".

Otherwise, return the prefix of trail up to but not including the first U+003B (;), concatenated with the character U+0029 RIGHT PARENTHESIS. For example, "`5.0 (Macintosh)`", "`5.0 (Android 10)`", or "`5.0 (X11)`".

The `platform` getter steps are to return a string representing the platform on which the browser is executing (e.g. "`MacIntel`", "`Win32`", "`Linux x86_64`", "`Linux armv81`") or, for privacy and compatibility, a string that is commonly returned on another platform.

The `product` getter steps are to return "`Gecko`".

The `productSub` getter steps are to return the appropriate string from the following list:

If the [navigator compatibility mode](https://html.spec.whatwg.org/multipage/system-state.html#concept-navigator-compatibility-mode) is _Chrome_ or _WebKit_
The string "`20030107`".

If the [navigator compatibility mode](https://html.spec.whatwg.org/multipage/system-state.html#concept-navigator-compatibility-mode) is _Gecko_
The string "`20100101`".

The `vendor` getter steps are to return the appropriate string from the following list:

If the [navigator compatibility mode](https://html.spec.whatwg.org/multipage/system-state.html#concept-navigator-compatibility-mode) is _Chrome_
The string "`Google Inc.`".

If the [navigator compatibility mode](https://html.spec.whatwg.org/multipage/system-state.html#concept-navigator-compatibility-mode) is _Gecko_
The empty string.

If the [navigator compatibility mode](https://html.spec.whatwg.org/multipage/system-state.html#concept-navigator-compatibility-mode) is _WebKit_
The string "`Apple Computer, Inc.`".

The `vendorSub` getter steps are to return the empty string.

If the [navigator compatibility mode](https://html.spec.whatwg.org/multipage/system-state.html#concept-navigator-compatibility-mode) is _Gecko_, then the user agent must also support the following partial interface:

```
partial interface mixin NavigatorID {
  [Exposed=Window] boolean taintEnabled(); // constant false
  [Exposed=Window] readonly attribute DOMString oscpu;
};
```

The `taintEnabled()` method must return false.

The `oscpu` attribute's getter must return either the empty string or a string representing the platform on which the browser is executing, e.g. "`Windows NT 10.0; Win64; x64`", "
```
Linux
  x86_64
```
".

[![Image 2: (This is a tracking vector.)](https://resources.whatwg.org/tracking-vector.svg)](https://infra.spec.whatwg.org/#tracking-vector "There is a tracking vector here.") Any information in this API that varies from user to user can be used to profile the user. In fact, if enough such information is available, a user can actually be uniquely identified. For this reason, user agent implementers are strongly urged to include as little information in this API as possible.

##### 8.9.1.2 Language preferences[](https://html.spec.whatwg.org/multipage/system-state.html#language-preferences)

```
interface mixin NavigatorLanguage {
  readonly attribute DOMString language;
  readonly attribute FrozenArray<DOMString> languages;
};
```
`self.navigator.language`

[Navigator/language](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language "The Navigator.language read-only property returns a string representing the preferred language of the user, usually the language of the browser UI.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 4+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 11

* * *

Firefox Android 4+Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

[WorkerNavigator/language](https://developer.mozilla.org/en-US/docs/Web/API/WorkerNavigator/language "The WorkerNavigator.language read-only property returns a string representing the preferred language of the user, usually the language of the browser UI.")

Support in all current engines.

Firefox 3.5+Safari 10+Chrome 4+

* * *

Opera 4+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 11

* * *

Firefox Android 4+Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Returns a language tag representing the user's preferred language.

`self.navigator.languages`

[Navigator/languages](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/languages "The Navigator.languages read-only property returns an array of strings representing the user's preferred languages. The language is described using language tags according to RFC 5646: Tags for Identifying Languages (also known as BCP 47). In the returned array they are ordered by preference with the most preferred language first.")

Support in all current engines.

Firefox 32+Safari 10.1+Chrome 37+

* * *

Opera 24+Edge 79+

* * *

Edge (Legacy)16+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet 3.0+Opera Android 24+

[WorkerNavigator/languages](https://developer.mozilla.org/en-US/docs/Web/API/WorkerNavigator/languages "The WorkerNavigator.languages read-only property returns an array of strings representing the user's preferred languages. The language is described using language tags according to RFC 5646: Tags for Identifying Languages (also known as BCP 47). In the returned array they are ordered by preference with the most preferred language first.")

Support in all current engines.

Firefox 32+Safari 10.1+Chrome 37+

* * *

Opera 24+Edge 79+

* * *

Edge (Legacy)16+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet 3.0+Opera Android 24+

Returns an array of language tags representing the user's preferred languages, with the most preferred language first.

The most preferred language is the one returned by `navigator.language`.

A `languagechange` event is fired at the `Window` or `WorkerGlobalScope` object when the user agent's understanding of what the user's preferred languages are changes.

The `languages` getter steps are:

1.   Let emulatedLanguage be the [WebDriver BiDi emulated language](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-emulated-language) for [this](https://webidl.spec.whatwg.org/#this)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).
2.   If emulatedLanguage is not null, return a [frozen array](https://webidl.spec.whatwg.org/#dfn-frozen-array-type) containing emulatedLanguage.
3.   Return a [frozen array](https://webidl.spec.whatwg.org/#dfn-frozen-array-type) of valid BCP 47 language tags representing either one or more [plausible languages](https://html.spec.whatwg.org/multipage/system-state.html#a-plausible-language), or the user's preferred languages, ordered by preference with the most preferred language first. [[BCP47]](https://html.spec.whatwg.org/multipage/references.html#refsBCP47)

The same object must be returned until the user agent needs to return different values, or values in a different order, or emulatedLanguage is updated.

To determine a plausible language, the user agent should bear in mind the following:

*   [![Image 3: (This is a tracking vector.)](https://resources.whatwg.org/tracking-vector.svg)](https://infra.spec.whatwg.org/#tracking-vector "There is a tracking vector here.") Any information in this API that varies from user to user can be used to profile or identify the user.
*   If the user is not using a service that obfuscates the user's point of origin (e.g. the Tor anonymity network), then the value that is least likely to distinguish the user from other users with similar origins (e.g. from the same IP address block) is the language used by the majority of such users. [[TOR]](https://html.spec.whatwg.org/multipage/references.html#refsTOR)
*   If the user is using an anonymizing service, then the value "`en-US`" is suggested; if all users of the service use that same value, that reduces the possibility of distinguishing the users from each other.

[![Image 4: (This is a tracking vector.)](https://resources.whatwg.org/tracking-vector.svg)](https://infra.spec.whatwg.org/#tracking-vector "There is a tracking vector here.") To avoid introducing any more fingerprinting vectors, user agents should use the same list for the APIs defined in this function as for the HTTP ``Accept-Language`` header.

##### 8.9.1.3 Browser state[](https://html.spec.whatwg.org/multipage/system-state.html#navigator.online)

```
interface mixin NavigatorOnLine {
  readonly attribute boolean onLine;
};
```
`self.navigator.onLine`

[Navigator/onLine](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/onLine "Returns the online status of the browser. The property returns a boolean value, with true meaning online and false meaning offline. The property sends updates whenever the browser's ability to connect to the network changes. The update occurs when the user follows links or when a script requests a remote page. For example, the property should return false when users click links soon after they lose internet connection.")

Support in all current engines.

Firefox 1.5+Safari 4+Chrome 2+

* * *

Opera 3+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android 4+Safari iOS?Chrome Android 18+WebView Android🔰 37+Samsung Internet?Opera Android 10.1+

[WorkerNavigator/onLine](https://developer.mozilla.org/en-US/docs/Web/API/WorkerNavigator/onLine "Returns the online status of the browser. The property returns a boolean value, with true meaning online and false meaning offline. The property sends updates whenever the browser's ability to connect to the network changes. The update occurs when the user follows links or when a script requests a remote page.")

Support in all current engines.

Firefox 3.5+Safari 4+Chrome 4+

* * *

Opera 10.6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android 4+Safari iOS 5+Chrome Android?WebView Android🔰 4.4+Samsung Internet?Opera Android 11+

Returns false if the user agent is definitely offline (disconnected from the network). Returns true if the user agent might be online.

The events `online` and `offline` are fired when the value of this attribute changes.

This attribute is inherently unreliable. A computer can be connected to a network without having Internet access.

In this example, an indicator is updated as the browser goes online and offline.

```
<!DOCTYPE HTML>
<html lang="en">
 <head>
  <title>Online status</title>
  <script>
   function updateIndicator() {
     document.getElementById('indicator').textContent = navigator.onLine ? 'online' : 'offline';
   }
  </script>
 </head>
 <body onload="updateIndicator()" ononline="updateIndicator()" onoffline="updateIndicator()">
  <p>The network is: <span id="indicator">(state unknown)</span>
 </body>
</html>
```

##### 8.9.1.4 Custom scheme handlers: the `registerProtocolHandler()` method[](https://html.spec.whatwg.org/multipage/system-state.html#custom-handlers)

[Navigator/registerProtocolHandler](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/registerProtocolHandler "The Navigator method registerProtocolHandler() lets websites register their ability to open or handle particular URL schemes (aka protocols).")

Firefox 2+Safari No Chrome 13+

* * *

Opera 11.6+Edge 79+

* * *

Edge (Legacy)No Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android No WebView Android?Samsung Internet?Opera Android?

```
interface mixin NavigatorContentUtils {
  [SecureContext] undefined registerProtocolHandler(DOMString scheme, USVString url);
  [SecureContext] undefined unregisterProtocolHandler(DOMString scheme, USVString url);
};
```
`window.navigator.registerProtocolHandler(scheme, url)`
Registers a handler for scheme at url. For example, an online telephone messaging service could register itself as a handler of the `sms:` scheme, so that if the user clicks on such a link, they are given the opportunity to use that web site. [[SMS]](https://html.spec.whatwg.org/multipage/references.html#refsSMS)

The string "`%s`" in url is used as a placeholder for where to put the URL of the content to be handled.

Throws a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException` if the user agent blocks the registration (this might happen if trying to register as a handler for "`http`", for instance).

Throws a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException` if the "`%s`" string is missing in url.

`window.navigator.unregisterProtocolHandler(scheme, url)`

[Navigator/unregisterProtocolHandler](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/unregisterProtocolHandler "The Navigator method unregisterProtocolHandler() removes a protocol handler for a given URL scheme.")

Support in one engine only.

Firefox No Safari No Chrome 38+

* * *

Opera 25+Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android No WebView Android?Samsung Internet?Opera Android?

Unregisters the handler given by the arguments.

Throws a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException` if the user agent blocks the deregistration (this might happen if with invalid schemes, for instance).

Throws a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException` if the "`%s`" string is missing in url.

The 
```
registerProtocolHandler(scheme,
  url)
```
 method steps are:

1.   Let (normalizedScheme, normalizedURLString) be the result of running [normalize protocol handler parameters](https://html.spec.whatwg.org/multipage/system-state.html#normalize-protocol-handler-parameters) with scheme, url, and [this](https://webidl.spec.whatwg.org/#this)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2.   [In parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel): register a protocol handler for normalizedScheme and normalizedURLString. User agents may, within the constraints described, do whatever they like. A user agent could, for instance, prompt the user and offer the user the opportunity to add the site to a shortlist of handlers, or make the handlers their default, or cancel the request. User agents could also silently collect the information, providing it only when relevant to the user.

User agents should keep track of which sites have registered handlers (even if the user has declined such registrations) so that the user is not repeatedly prompted with the same request.

If the [`registerProtocolHandler()` automation mode](https://html.spec.whatwg.org/multipage/system-state.html#registerprotocolhandler()-automation-mode) of [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window) is not "`none`", the user agent should first verify that it is in an automation context (see [WebDriver's security considerations](https://w3c.github.io/webdriver/#security)). The user agent should then bypass the above communication of information and gathering of user consent, and instead do the following based on the value of the [`registerProtocolHandler()` automation mode](https://html.spec.whatwg.org/multipage/system-state.html#registerprotocolhandler()-automation-mode):

"`autoAccept`"
Act as if the user has seen the registration details and accepted the request.

"`autoReject`"
Act as if the user has seen the registration details and rejected the request.

When the user agent uses this handler for a [URL](https://url.spec.whatwg.org/#concept-url)inputURL:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): inputURL's [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is normalizedScheme.

    2.   [Set the username](https://url.spec.whatwg.org/#set-the-username) given inputURL and the empty string.

    3.   [Set the password](https://url.spec.whatwg.org/#set-the-password) given inputURL and the empty string.

    4.   Let inputURLString be the [serialization](https://url.spec.whatwg.org/#concept-url-serializer) of inputURL.

    5.   Let encodedURL be the result of running [UTF-8 percent-encode](https://url.spec.whatwg.org/#string-utf-8-percent-encode) on inputURLString using the [component percent-encode set](https://url.spec.whatwg.org/#component-percent-encode-set).

    6.   Let handlerURLString be normalizedURLString.

    7.   Replace the first instance of "`%s`" in handlerURLString with encodedURL.

    8.   Let resultURL be the result of [parsing](https://url.spec.whatwg.org/#concept-url-parser)handlerURLString.

    9.   [Navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) an appropriate [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) to resultURL.

If the user had visited a site at `https://example.com/` that made the following call:

`navigator.registerProtocolHandler('web+soup', 'soup?url=%s')`
...and then, much later, while visiting `https://www.example.net/`, clicked on a link such as:

`<a href="web+soup:chicken-kïwi">Download our Chicken Kïwi soup!</a>`
...then the UA might navigate to the following URL:

https://example.com/soup?url=web+soup:chicken-k%C3%AFwi
This site could then do whatever it is that it does with soup (synthesize it and ship it to the user, or whatever).

This does not define when the handler is used. To some extent, the [processing model for navigating across documents](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) defines some cases where it is relevant, but in general user agents may use this information wherever they would otherwise consider handing schemes to native plugins or helper applications.

The 
```
unregisterProtocolHandler(scheme,
  url)
```
 method steps are:

1.   Let (normalizedScheme, normalizedURLString) be the result of running [normalize protocol handler parameters](https://html.spec.whatwg.org/multipage/system-state.html#normalize-protocol-handler-parameters) with scheme, url, and [this](https://webidl.spec.whatwg.org/#this)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

2.   [In parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel): unregister the handler described by normalizedScheme and normalizedURLString.

* * *

To normalize protocol handler parameters, given a string scheme, a string url, and an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)environment, run these steps:

1.   Set scheme to scheme, [converted to ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase).

2.   If scheme is neither a [safelisted scheme](https://html.spec.whatwg.org/multipage/system-state.html#safelisted-scheme) nor a string starting with "`web+`" followed by one or more [ASCII lower alphas](https://infra.spec.whatwg.org/#ascii-lower-alpha), then throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException`.

This means that including a colon in scheme (as in "`mailto:`") will throw.

The following schemes are the safelisted schemes:

    *   `bitcoin`
    *   `ftp`
    *   `ftps`
    *   `geo`
    *   `im`
    *   `irc`
    *   `ircs`
    *   `magnet`
    *   `mailto`
    *   `matrix`
    *   `mms`
    *   `news`
    *   `nntp`
    *   `openpgp4fpr`
    *   `sftp`
    *   `sip`
    *   `sms`
    *   `smsto`
    *   `ssh`
    *   `tel`
    *   `urn`
    *   `webcal`
    *   `wtai`
    *   `xmpp`

This list can be changed. If there are schemes that ought to be added, please send feedback.

3.   If url does not contain "`%s`", then throw a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException`.

4.   Let urlRecord be the result of [encoding-parsing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url) given url, relative to environment.

5.   If urlRecord is failure, then throw a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException`.

This is forcibly the case if the `%s` placeholder is in the host or port of the URL.

6.   If urlRecord's [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is not an [HTTP(S) scheme](https://fetch.spec.whatwg.org/#http-scheme) or urlRecord's [origin](https://url.spec.whatwg.org/#concept-url-origin) is not [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with environment's [origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-origin), then throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException`.

7.   [Assert](https://infra.spec.whatwg.org/#assert): the result of [Is url potentially trustworthy?](https://w3c.github.io/webappsec-secure-contexts/#potentially-trustworthy-url) given urlRecord is "`Potentially Trustworthy`".

Because [normalize protocol handler parameters](https://html.spec.whatwg.org/multipage/system-state.html#normalize-protocol-handler-parameters) is run within a [secure context](https://html.spec.whatwg.org/multipage/webappapis.html#secure-context), this is implied by the [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) condition.

8.   Return (scheme, urlRecord).

The [serialization](https://url.spec.whatwg.org/#concept-url-serializer) of urlRecord will by definition not be a [valid URL string](https://url.spec.whatwg.org/#valid-url-string) as it includes the string "`%s`" which is not a valid component in a URL.

###### 8.9.1.4.1 Security and privacy[](https://html.spec.whatwg.org/multipage/system-state.html#security-and-privacy)

Custom scheme handlers can introduce a number of concerns, in particular privacy concerns.

**Hijacking all web usage.** User agents should not allow schemes that are key to its normal operation, such as an [HTTP(S) scheme](https://fetch.spec.whatwg.org/#http-scheme), to be rerouted through third-party sites. This would allow a user's activities to be trivially tracked, and would allow user information, even in secure connections, to be collected.

**Hijacking defaults.** User agents are strongly urged to not automatically change any defaults, as this could lead the user to send data to remote hosts that the user is not expecting. New handlers registering themselves should never automatically cause those sites to be used.

**Registration spamming.** User agents should consider the possibility that a site will attempt to register a large number of handlers, possibly from multiple domains (e.g., by redirecting through a series of pages each on a different domain, and each registering a handler for `web+spam:` — analogous practices abusing other web browser features have been used by pornography web sites for many years). User agents should gracefully handle such hostile attempts, protecting the user.

**Hostile handler metadata.** User agents should protect against typical attacks against strings embedded in their interface, for example ensuring that markup or escape characters in such strings are not executed, that null bytes are properly handled, that over-long strings do not cause crashes or buffer overruns, and so forth.

**Leaking private data.** Web page authors may reference a custom scheme handler using URL data considered private. They might do so with the expectation that the user's choice of handler points to a page inside the organization, ensuring that sensitive data will not be exposed to third parties. However, a user may have registered a handler pointing to an external site, resulting in a data leak to that third party. Implementers might wish to consider allowing administrators to disable custom handlers on certain subdomains, content types, or schemes.

**Interface interference.** User agents should be prepared to handle intentionally long arguments to the methods. For example, if the user interface exposed consists of an "accept" button and a "deny" button, with the "accept" binding containing the name of the handler, it's important that a long name not cause the "deny" button to be pushed off the screen.

###### 8.9.1.4.2 User agent automation[](https://html.spec.whatwg.org/multipage/system-state.html#user-agent-automation)

Each `Document` has a `registerProtocolHandler()` automation mode. It defaults to "`none`", but it also can be either "`autoAccept`" or "`autoReject`".

For the purposes of user agent automation and website testing, this standard defines Set RPH Registration Mode WebDriver [extension command](https://w3c.github.io/webdriver/#dfn-extension-commands). It instructs the user agent to place a `Document` into a mode where it will automatically simulate a user either accepting or rejecting and registration confirmation prompt dialog.

| HTTP Method | URI Template |
| --- | --- |
| ``POST`` | `/session/{session id}/custom-handlers/set-mode` |

The [remote end steps](https://w3c.github.io/webdriver/#dfn-remote-end-steps) are:

1.   If parameters is not a JSON Object, return a [WebDriver error](https://w3c.github.io/webdriver/#dfn-errors) with [WebDriver error code](https://w3c.github.io/webdriver/#dfn-error-code)[invalid argument](https://w3c.github.io/webdriver/#dfn-invalid-argument).

2.   Let mode be the result of [getting a property](https://w3c.github.io/webdriver/#dfn-getting-properties) named "`mode`" from parameters.

3.   If mode is not "`autoAccept`", "`autoReject`", or "`none`", return a [WebDriver error](https://w3c.github.io/webdriver/#dfn-errors) with [WebDriver error code](https://w3c.github.io/webdriver/#dfn-error-code)[invalid argument](https://w3c.github.io/webdriver/#dfn-invalid-argument).

4.   Let document be the [current browsing context](https://w3c.github.io/webdriver/#dfn-current-browsing-context)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document).

5.   Set document's [`registerProtocolHandler()` automation mode](https://html.spec.whatwg.org/multipage/system-state.html#registerprotocolhandler()-automation-mode) to mode.

6.   Return [success](https://w3c.github.io/webdriver/#dfn-success) with data null.

##### 8.9.1.5 Cookies[](https://html.spec.whatwg.org/multipage/system-state.html#cookies)

```
interface mixin NavigatorCookies {
  readonly attribute boolean cookieEnabled;
};
```
`window.navigator.cookieEnabled`

[Navigator/cookieEnabled](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/cookieEnabled "navigator.cookieEnabled returns a Boolean value that indicates whether cookies are enabled or not.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Returns false if setting a cookie will be ignored, and true otherwise.

The `cookieEnabled` attribute must return true if the user agent attempts to handle cookies according to HTTP State Management Mechanism, and false if it ignores cookie change requests. [[COOKIES]](https://html.spec.whatwg.org/multipage/references.html#refsCOOKIES)

##### 8.9.1.6 PDF viewing support[](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewing-support)

`window.navigator.pdfViewerEnabled`
Returns true if the user agent supports inline viewing of PDF files when [navigating](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) to them, or false otherwise. In the latter case, PDF files will be handled by [external software](https://html.spec.whatwg.org/multipage/browsing-the-web.html#hand-off-to-external-software).

```
interface mixin NavigatorPlugins {
  [SameObject] readonly attribute PluginArray plugins;
  [SameObject] readonly attribute MimeTypeArray mimeTypes;
  boolean javaEnabled();
  readonly attribute boolean pdfViewerEnabled;
};

[Exposed=Window,
 LegacyUnenumerableNamedProperties]
interface PluginArray {
  undefined refresh();
  readonly attribute unsigned long length;
  getter Plugin? item(unsigned long index);
  getter Plugin? namedItem(DOMString name);
};

[Exposed=Window,
 LegacyUnenumerableNamedProperties]
interface MimeTypeArray {
  readonly attribute unsigned long length;
  getter MimeType? item(unsigned long index);
  getter MimeType? namedItem(DOMString name);
};

[Exposed=Window,
 LegacyUnenumerableNamedProperties]
interface Plugin {
  readonly attribute DOMString name;
  readonly attribute DOMString description;
  readonly attribute DOMString filename;
  readonly attribute unsigned long length;
  getter MimeType? item(unsigned long index);
  getter MimeType? namedItem(DOMString name);
};

[Exposed=Window]
interface MimeType {
  readonly attribute DOMString type;
  readonly attribute DOMString description;
  readonly attribute DOMString suffixes;
  readonly attribute Plugin enabledPlugin;
};
```

Although these days detecting PDF viewer support can be done via `navigator.pdfViewerEnabled`, for historical reasons, there are a number of complex and intertwined interfaces that provide the same capability, which legacy code relies on. This section specifies both the simple modern variant and the complicated historical one.

[![Image 5: (This is a tracking vector.)](https://resources.whatwg.org/tracking-vector.svg)](https://infra.spec.whatwg.org/#tracking-vector "There is a tracking vector here.") Each user agent has a PDF viewer supported boolean, whose value is [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) (and might vary according to user preferences).

This value also impacts the [navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) processing model.

* * *

Each `Window` object has a PDF viewer plugin objects list. If the user agent's [PDF viewer supported](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-supported) is false, then it is the empty list. Otherwise, it is a list containing five `Plugin` objects, whose [names](https://html.spec.whatwg.org/multipage/system-state.html#concept-plugin-name) are, respectively:

1.   "`PDF Viewer`"
2.   "`Chrome PDF Viewer`"
3.   "`Chromium PDF Viewer`"
4.   "`Microsoft Edge PDF Viewer`"
5.   "`WebKit built-in PDF`"

The values of the above list form the PDF viewer plugin names list.

These names were chosen based on evidence of what websites historically search for, and thus what is necessary for user agents to expose in order to maintain compatibility with existing content. They are ordered alphabetically. The "`PDF Viewer`" name was then inserted in the 0th position so that the `enabledPlugin` getter could point to a generic plugin name.

Each `Window` object has a PDF viewer mime type objects list. If the user agent's [PDF viewer supported](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-supported) is false, then it is the empty list. Otherwise, it is a list containing two `MimeType` objects, whose [types](https://html.spec.whatwg.org/multipage/system-state.html#concept-mimetype-type) are, respectively:

1.   "`application/pdf`"
2.   "`text/pdf`"

The values of the above list form the PDF viewer mime types list.

* * *

Each `NavigatorPlugins` object has a plugins array, which is a new `PluginArray`, and a mime types array, which is a new `MimeTypeArray`.

The `NavigatorPlugins` mixin's `plugins` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [plugins array](https://html.spec.whatwg.org/multipage/system-state.html#plugins-array).

The `NavigatorPlugins` mixin's `mimeTypes` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [mime types array](https://html.spec.whatwg.org/multipage/system-state.html#mime-types-array).

The `NavigatorPlugins` mixin's `javaEnabled()` method steps are to return false.

[Navigator/pdfViewerEnabled](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/pdfViewerEnabled "The pdfViewerEnabled property of the Navigator interface indicates whether the browser supports inline display of PDF files when navigating to them.")

Support in all current engines.

Firefox 99+Safari 16.4+Chrome 94+

* * *

Opera?Edge 94+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `NavigatorPlugins` mixin's `pdfViewerEnabled` getter steps are to return the user agent's [PDF viewer supported](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-supported).

* * *

The `PluginArray` interface [supports named properties](https://webidl.spec.whatwg.org/#dfn-support-named-properties). If the user agent's [PDF viewer supported](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-supported) is true, then they are the [PDF viewer plugin names](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-plugin-names). Otherwise, they are the empty list.

The `PluginArray` interface's `refresh()` method steps are to do nothing.

* * *

The `MimeTypeArray` interface [supports named properties](https://webidl.spec.whatwg.org/#dfn-support-named-properties). If the user agent's [PDF viewer supported](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-supported) is true, then they are the [PDF viewer mime types](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-mime-types). Otherwise, they are the empty list.

* * *

Each `Plugin` object has a name, which is set when the object is created.

The `Plugin` interface's `name` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [name](https://html.spec.whatwg.org/multipage/system-state.html#concept-plugin-name).

The `Plugin` interface's `description` getter steps are to return "`Portable Document Format`".

The `Plugin` interface's `filename` getter steps are to return "`internal-pdf-viewer`".

The `Plugin` interface [supports named properties](https://webidl.spec.whatwg.org/#dfn-support-named-properties). If the user agent's [PDF viewer supported](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-supported) is true, then they are the [PDF viewer mime types](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-mime-types). Otherwise, they are the empty list.

The `Plugin` interface's `item(index)` method steps are:

1.   Let mimeTypes be [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [PDF viewer mime type objects](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-mime-type-objects).

2.   If index<mimeTypes's [size](https://infra.spec.whatwg.org/#list-size), then return mimeTypes[index].

3.   Return null.

* * *

Each `MimeType` object has a type, which is set when the object is created.

The `MimeType` interface's `type` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [type](https://html.spec.whatwg.org/multipage/system-state.html#concept-mimetype-type).

The `MimeType` interface's `description` getter steps are to return "`Portable Document Format`".

The `MimeType` interface's `suffixes` getter steps are to return "`pdf`".

The `MimeType` interface's `enabledPlugin` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [PDF viewer plugin objects](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-plugin-objects)[0] (i.e., the generic "`PDF Viewer`" one).

[← 8.6 Timers](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [8.10 Images →](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html)
