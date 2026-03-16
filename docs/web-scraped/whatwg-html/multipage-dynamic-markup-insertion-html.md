# Source: https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 8 Web application APIs](https://html.spec.whatwg.org/multipage/webappapis.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [8.6 Timers →](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html)
1.       1.   [8.4 Dynamic markup insertion](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#dynamic-markup-insertion)
        1.   [8.4.1 Opening the input stream](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#opening-the-input-stream)
        2.   [8.4.2 Closing the input stream](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#closing-the-input-stream)
        3.   [8.4.3`document.write()`](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#document.write())
        4.   [8.4.4`document.writeln()`](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#document.writeln())

    2.   [8.5 DOM parsing and serialization APIs](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#dom-parsing-and-serialization)
        1.   [8.5.1 The `DOMParser` interface](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-domparser-interface)
        2.   [8.5.2 Unsafe HTML parsing methods](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#unsafe-html-parsing-methods)
        3.   [8.5.3 HTML serialization methods](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#html-serialization-methods)
        4.   [8.5.4 The `innerHTML` property](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-innerhtml-property)
        5.   [8.5.5 The `outerHTML` property](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-outerhtml-property)
        6.   [8.5.6 The `insertAdjacentHTML()` method](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-insertadjacenthtml()-method)
        7.   [8.5.7 The `createContextualFragment()` method](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-createcontextualfragment()-method)
        8.   [8.5.8 The `XMLSerializer` interface](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-xmlserializer-interface)

### 8.4 Dynamic markup insertion[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#dynamic-markup-insertion)

APIs for dynamically inserting markup into the document interact with the parser, and thus their behavior varies depending on whether they are used with [HTML documents](https://dom.spec.whatwg.org/#html-document) (and the [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser)) or [XML documents](https://dom.spec.whatwg.org/#xml-document) (and the [XML parser](https://html.spec.whatwg.org/multipage/xhtml.html#xml-parser)).

`Document` objects have a throw-on-dynamic-markup-insertion counter, which is used in conjunction with the [create an element for the token](https://html.spec.whatwg.org/multipage/parsing.html#create-an-element-for-the-token) algorithm to prevent [custom element constructors](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor) from being able to use `document.open()`, `document.close()`, and `document.write()` when they are invoked by the parser. Initially, the counter must be set to zero.

#### 8.4.1 Opening the input stream[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#opening-the-input-stream)

`document = document.open()`

[Document/open](https://developer.mozilla.org/en-US/docs/Web/API/Document/open "The Document.open() method opens a document for writing.")

Support in all current engines.

Firefox 1+Safari 11+Chrome 64+

* * *

Opera 51+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 47+

Causes the `Document` to be replaced in-place, as if it was a new `Document` object, but reusing the previous object, which is then returned.

The resulting `Document` has an HTML parser associated with it, which can be given data to parse using `document.write()`.

The method has no effect if the `Document` is still being parsed.

Throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if the `Document` is an [XML document](https://dom.spec.whatwg.org/#xml-document).

Throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if the parser is currently executing a [custom element constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor).

`window = document.open(url, name, features)`
Works like the `window.open()` method.

`Document` objects have an active parser was aborted boolean, which is used to prevent scripts from invoking the `document.open()` and `document.write()` methods (directly or indirectly) after the document's [active parser](https://html.spec.whatwg.org/multipage/dom.html#active-parser) has been aborted. It is initially false.

The document open steps, given a document, are as follows:

1.   If document is an [XML document](https://dom.spec.whatwg.org/#xml-document), then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

2.   If document's [throw-on-dynamic-markup-insertion counter](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#throw-on-dynamic-markup-insertion-counter) is greater than 0, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

3.   Let entryDocument be the [entry global object](https://html.spec.whatwg.org/multipage/webappapis.html#entry-global-object)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window).

4.   If document's [origin](https://dom.spec.whatwg.org/#concept-document-origin) is not [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) to entryDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin), then throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException`.

5.   If document has an [active parser](https://html.spec.whatwg.org/multipage/dom.html#active-parser) whose [script nesting level](https://html.spec.whatwg.org/multipage/parsing.html#script-nesting-level) is greater than 0, then return document.

This basically causes `document.open()` to be ignored when it's called in an inline script found during parsing, while still letting it have an effect when called from a non-parser task such as a timer callback or event handler.

6.   Similarly, if document's [unload counter](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-counter) is greater than 0, then return document.

This basically causes `document.open()` to be ignored when it's called from a `beforeunload`, `pagehide`, or `unload` event handler while the `Document` is being unloaded.

7.   If document's [active parser was aborted](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#active-parser-was-aborted) is true, then return document.

This notably causes `document.open()` to be ignored if it is called after a [navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) has started, but only during the initial parse. See [issue #4723](https://github.com/whatwg/html/issues/4723) for more background.

8.   If document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) is non-null and document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation) is a [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id), then [stop loading](https://html.spec.whatwg.org/multipage/document-lifecycle.html#nav-stop)document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable).

9.   For each [shadow-including inclusive descendant](https://dom.spec.whatwg.org/#concept-shadow-including-inclusive-descendant)node of document, [erase all event listeners and handlers](https://html.spec.whatwg.org/multipage/webappapis.html#erase-all-event-listeners-and-handlers) given node.

10.   If document is the [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window) of document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), then [erase all event listeners and handlers](https://html.spec.whatwg.org/multipage/webappapis.html#erase-all-event-listeners-and-handlers) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global).

11.   [Replace all](https://dom.spec.whatwg.org/#concept-node-replace-all) with null within document.

12.   If document is [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then:

    1.   Let newURL be a copy of entryDocument's [URL](https://dom.spec.whatwg.org/#concept-document-url).

    2.   If entryDocument is not document, then set newURL's [fragment](https://url.spec.whatwg.org/#concept-url-fragment) to null.

    3.   Run the [URL and history update steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#url-and-history-update-steps) with document and newURL.

13.   Set document's [is initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank) to false.

14.   If document's [iframe load in progress](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-load-in-progress) flag is set, then set document's [mute iframe load](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#mute-iframe-load) flag.

15.   Set document to [no-quirks mode](https://dom.spec.whatwg.org/#concept-document-no-quirks).

16.   Create a new [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) and associate it with document. This is a script-created parser (meaning that it can be closed by the `document.open()` and `document.close()` methods, and that the tokenizer will wait for an explicit call to `document.close()` before emitting an end-of-file token). The encoding [confidence](https://html.spec.whatwg.org/multipage/parsing.html#concept-encoding-confidence) is _irrelevant_.

17.   Set the [insertion point](https://html.spec.whatwg.org/multipage/parsing.html#insertion-point) to point at just before the end of the [input stream](https://html.spec.whatwg.org/multipage/parsing.html#input-stream) (which at this point will be empty).

18.   [Update the current document readiness](https://html.spec.whatwg.org/multipage/dom.html#update-the-current-document-readiness) of document to "`loading`".

This causes a `readystatechange` event to fire, but the event is actually unobservable to author code, because of the previous step which [erased all event listeners and handlers](https://html.spec.whatwg.org/multipage/webappapis.html#erase-all-event-listeners-and-handlers) that could observe it.

19.   Return document.

The [document open steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#document-open-steps) do not affect whether a `Document` is [ready for post-load tasks](https://html.spec.whatwg.org/multipage/parsing.html#ready-for-post-load-tasks) or [completely loaded](https://html.spec.whatwg.org/multipage/document-lifecycle.html#completely-loaded).

The 
```
open(unused1,
  unused2)
```
 method must return the result of running the [document open steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#document-open-steps) with [this](https://webidl.spec.whatwg.org/#this).

[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#dom-document-open-unused-arguments)The unused1 and unused2 arguments are ignored, but kept in the IDL to allow code that calls the function with one or two arguments to continue working. They are necessary due to Web IDL [overload resolution algorithm](https://webidl.spec.whatwg.org/#dfn-overload-resolution-algorithm) rules, which would throw a `TypeError` exception for such calls had the arguments not been there. [whatwg/webidl issue #581](https://github.com/whatwg/webidl/issues/581) investigates changing the algorithm to allow for their removal. [[WEBIDL]](https://html.spec.whatwg.org/multipage/references.html#refsWEBIDL)

#### 8.4.2 Closing the input stream[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#closing-the-input-stream)

`document.close()`

[Document/close](https://developer.mozilla.org/en-US/docs/Web/API/Document/close "The Document.close() method finishes writing to a document, opened with Document.open().")

Support in all current engines.

Firefox 1+Safari 11+Chrome 64+

* * *

Opera 51+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 47+

Closes the input stream that was opened by the `document.open()` method.

Throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if the `Document` is an [XML document](https://dom.spec.whatwg.org/#xml-document).

Throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if the parser is currently executing a [custom element constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor).

The `close()` method must run the following steps:

1.   If [this](https://webidl.spec.whatwg.org/#this) is an [XML document](https://dom.spec.whatwg.org/#xml-document), then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

2.   If [this](https://webidl.spec.whatwg.org/#this)'s [throw-on-dynamic-markup-insertion counter](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#throw-on-dynamic-markup-insertion-counter) is greater than zero, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

3.   If there is no [script-created parser](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#script-created-parser) associated with [this](https://webidl.spec.whatwg.org/#this), then return.

4.   Insert an [explicit "EOF" character](https://html.spec.whatwg.org/multipage/parsing.html#explicit-eof-character) at the end of the parser's [input stream](https://html.spec.whatwg.org/multipage/parsing.html#input-stream).

5.   If [this](https://webidl.spec.whatwg.org/#this)'s [pending parsing-blocking script](https://html.spec.whatwg.org/multipage/scripting.html#pending-parsing-blocking-script) is not null, then return.

6.   Run the tokenizer, processing resulting tokens as they are emitted, and stopping when the tokenizer reaches the [explicit "EOF" character](https://html.spec.whatwg.org/multipage/parsing.html#explicit-eof-character) or [spins the event loop](https://html.spec.whatwg.org/multipage/webappapis.html#spin-the-event-loop).

#### 8.4.3`document.write()`[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#document.write())

`document.write(...text)`

[Document/write](https://developer.mozilla.org/en-US/docs/Web/API/Document/write "The document.write() method writes a string of text to a document stream opened by document.open().")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 3+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

In general, adds the given string(s) to the `Document`'s input stream.

This method has very idiosyncratic behavior. In some cases, this method can affect the state of the [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) while the parser is running, resulting in a DOM that does not correspond to the source of the document (e.g. if the string written is the string "`<plaintext>`" or "`<!--`"). In other cases, the call can clear the current page first, as if `document.open()` had been called. In yet more cases, the method is simply ignored, or throws an exception. User agents are [explicitly allowed to avoid executing `script` elements inserted via this method](https://html.spec.whatwg.org/multipage/parsing.html#document-written-scripts-intervention). And to make matters even worse, the exact behavior of this method can in some cases be dependent on network latency, which can lead to failures that are very hard to debug. **For all these reasons, use of this method is strongly discouraged.**

Throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` when invoked on [XML documents](https://dom.spec.whatwg.org/#xml-document).

Throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if the parser is currently executing a [custom element constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor).

This method performs no sanitization to remove potentially-dangerous elements and attributes like `script` or [event handler content attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes).

`Document` objects have an ignore-destructive-writes counter, which is used in conjunction with the processing of `script` elements to prevent external scripts from being able to use `document.write()` to blow away the document by implicitly calling `document.open()`. Initially, the counter must be set to zero.

The document write steps, given a `Document` object document, a list text, a boolean lineFeed, and a string sink, are as follows:

1.   Let string be the empty string.

2.   Let isTrusted be false if text[contains](https://infra.spec.whatwg.org/#list-contain) a string; otherwise true.

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)value of text:

    1.   If value is a `TrustedHTML` object, then append value's associated [data](https://w3c.github.io/trusted-types/dist/spec/#trustedhtml-data) to string.

    2.   Otherwise, append value to string.

4.   If isTrusted is false, set string to the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedHTML`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), string, sink, and "`script`".

5.   If lineFeed is true, append U+000A LINE FEED to string.

6.   If document is an [XML document](https://dom.spec.whatwg.org/#xml-document), then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

7.   If document's [throw-on-dynamic-markup-insertion counter](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#throw-on-dynamic-markup-insertion-counter) is greater than 0, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

8.   If document's [active parser was aborted](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#active-parser-was-aborted) is true, then return.

9.   If the [insertion point](https://html.spec.whatwg.org/multipage/parsing.html#insertion-point) is undefined, then:

    1.   If document's [unload counter](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-counter) is greater than 0 or document's [ignore-destructive-writes counter](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#ignore-destructive-writes-counter) is greater than 0, then return.

    2.   Run the [document open steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#document-open-steps) with document.

10.   Insert string into the [input stream](https://html.spec.whatwg.org/multipage/parsing.html#input-stream) just before the [insertion point](https://html.spec.whatwg.org/multipage/parsing.html#insertion-point).

11.   If document's [pending parsing-blocking script](https://html.spec.whatwg.org/multipage/scripting.html#pending-parsing-blocking-script) is null, then have the [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) process string, one code point at a time, processing resulting tokens as they are emitted, and stopping when the tokenizer reaches the insertion point or when the processing of the tokenizer is aborted by the tree construction stage (this can happen if a `script` end tag token is emitted by the tokenizer).

If the `document.write()` method was called from script executing inline (i.e. executing because the parser parsed a set of `script` tags), then this is a [reentrant invocation of the parser](https://html.spec.whatwg.org/multipage/parsing.html#nestedParsing). If the [parser pause flag](https://html.spec.whatwg.org/multipage/parsing.html#parser-pause-flag) is set, the tokenizer will abort immediately and no HTML will be parsed, per the tokenizer's [parser pause flag check](https://html.spec.whatwg.org/multipage/parsing.html#check-parser-pause-flag).

The `document.write(...text)` method steps are to run the [document write steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#document-write-steps) with [this](https://webidl.spec.whatwg.org/#this), text, false, and "`Document write`".

#### 8.4.4`document.writeln()`[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#document.writeln())

`document.writeln(...text)`

[Document/writeln](https://developer.mozilla.org/en-US/docs/Web/API/Document/writeln "Writes a string of text followed by a newline character to a document.")

Support in all current engines.

Firefox 1+Safari 11+Chrome 64+

* * *

Opera 51+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 47+

Adds the given string(s) to the `Document`'s input stream, followed by a newline character. If necessary, calls the `open()` method implicitly first.

This method has very idiosyncratic behavior. **Use of this method is strongly discouraged, for the same reasons as `document.write()`.**

Throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` when invoked on [XML documents](https://dom.spec.whatwg.org/#xml-document).

Throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if the parser is currently executing a [custom element constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor).

This method performs no sanitization to remove potentially-dangerous elements and attributes like `script` or [event handler content attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes).

The `document.writeln(...text)` method steps are to run the [document write steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#document-write-steps) with [this](https://webidl.spec.whatwg.org/#this), text, true, and "`Document writeln`".

### 8.5 DOM parsing and serialization APIs[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#dom-parsing-and-serialization)

[DOMParser](https://developer.mozilla.org/en-US/docs/Web/API/DOMParser "The DOMParser interface provides the ability to parse XML or HTML source code from a string into a DOM Document.")

Support in all current engines.

Firefox 1+Safari 1.3+Chrome 1+

* * *

Opera 8+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

```
partial interface Element {
  [CEReactions] undefined setHTMLUnsafe((TrustedHTML or DOMString) html);
  DOMString getHTML(optional GetHTMLOptions options = {});

  [CEReactions] attribute (TrustedHTML or [LegacyNullToEmptyString] DOMString) innerHTML;
  [CEReactions] attribute (TrustedHTML or [LegacyNullToEmptyString] DOMString) outerHTML;
  [CEReactions] undefined insertAdjacentHTML(DOMString position, (TrustedHTML or DOMString) string);
};

partial interface ShadowRoot {
  [CEReactions] undefined setHTMLUnsafe((TrustedHTML or DOMString) html);
  DOMString getHTML(optional GetHTMLOptions options = {});

  [CEReactions] attribute (TrustedHTML or [LegacyNullToEmptyString] DOMString) innerHTML;
};

dictionary GetHTMLOptions {
  boolean serializableShadowRoots = false;
  sequence<ShadowRoot> shadowRoots = [];
};
```

#### 8.5.1 The `DOMParser` interface[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-domparser-interface)

The `DOMParser` interface allows authors to create new `Document` objects by parsing strings, as either HTML or XML.

`parser = new DOMParser()`

[DOMParser/DOMParser](https://developer.mozilla.org/en-US/docs/Web/API/DOMParser/DOMParser "The DOMParser() constructor creates a new DOMParser object. This object can be used to parse the text of a document using the parseFromString() method.")

Support in all current engines.

Firefox 1+Safari 1.3+Chrome 1+

* * *

Opera 8+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Constructs a new `DOMParser` object.

`document = parser.parseFromString(string, type)`

[DOMParser/parseFromString](https://developer.mozilla.org/en-US/docs/Web/API/DOMParser/parseFromString "The parseFromString() method of the DOMParser interface parses a string containing either HTML or XML, returning an HTMLDocument or an XMLDocument.")

Support in all current engines.

Firefox 1+Safari 1.3+Chrome 1+

* * *

Opera 8+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Parses string using either the HTML or XML parser, according to type, and returns the resulting `Document`. type can be "`text/html`" (which will invoke the HTML parser), or any of "`text/xml`", "`application/xml`", "`application/xhtml+xml`", or "`image/svg+xml`" (which will invoke the XML parser).

For the XML parser, if string cannot be parsed, then the returned `Document` will contain elements describing the resulting error.

Note that `script` elements are not evaluated during parsing, and the resulting document's [encoding](https://dom.spec.whatwg.org/#concept-document-encoding) will always be [UTF-8](https://encoding.spec.whatwg.org/#utf-8). The document's [URL](https://dom.spec.whatwg.org/#concept-document-url) will be inherited from parser's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global).

Values other than the above for type will cause a `TypeError` exception to be thrown.

The design of `DOMParser`, as a class that needs to be constructed and then have its `parseFromString()` method called, is an unfortunate historical artifact. If we were designing this functionality today it would be a standalone function. For parsing HTML, the modern alternative is `Document.parseHTMLUnsafe()`.

This method performs no sanitization to remove potentially-dangerous elements and attributes like `script` or [event handler content attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes).

```
[Exposed=Window]
interface DOMParser {
  constructor();

  [NewObject] Document parseFromString((TrustedHTML or DOMString) string, DOMParserSupportedType type);
};

enum DOMParserSupportedType {
  "text/html",
  "text/xml",
  "application/xml",
  "application/xhtml+xml",
  "image/svg+xml"
};
```

The `new DOMParser()` constructor steps are to do nothing.

The 
```
parseFromString(string,
  type)
```
 method steps are:

1.   Let compliantString be the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedHTML`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), string, "`DOMParser parseFromString`", and "`script`".

2.   Let document be a new `Document`, whose [content type](https://dom.spec.whatwg.org/#concept-document-content-type) is type and [URL](https://dom.spec.whatwg.org/#concept-document-url) is [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window)'s [URL](https://dom.spec.whatwg.org/#concept-document-url).

The document's [encoding](https://dom.spec.whatwg.org/#concept-document-encoding) will be left as its default, of [UTF-8](https://encoding.spec.whatwg.org/#utf-8). In particular, any XML declarations or `meta` elements found while parsing compliantString will have no effect.

3.   Switch on type:

"`text/html`"
    1.   [Parse HTML from a string](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#parse-html-from-a-string) given document and compliantString.

Since document does not have a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc), [scripting is disabled](https://html.spec.whatwg.org/multipage/webappapis.html#concept-n-script).

Otherwise
    1.   Create an [XML parser](https://html.spec.whatwg.org/multipage/xhtml.html#xml-parser)parser, associated with document, and with [XML scripting support disabled](https://html.spec.whatwg.org/multipage/xhtml.html#xml-scripting-support-disabled).

    2.   Parse compliantString using parser.

    3.   If the previous step resulted in an XML well-formedness or XML namespace well-formedness error, then:

        1.   [Assert](https://infra.spec.whatwg.org/#assert): document has no child nodes.

        2.   Let root be the result of [creating an element](https://dom.spec.whatwg.org/#concept-create-element) given document, "`parsererror`", and "`http://www.mozilla.org/newlayout/xml/parsererror.xml`".

        3.   Optionally, add attributes or children to root to describe the nature of the parsing error.

        4.   [Append](https://dom.spec.whatwg.org/#concept-node-append)root to document.

4.   Return document.

To parse HTML from a string, given a `Document`document and a [string](https://infra.spec.whatwg.org/#string)html:

1.   Set document's [type](https://dom.spec.whatwg.org/#concept-document-type) to "`html`".

2.   Create an [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser)parser, associated with document.

3.   Place html into the [input stream](https://html.spec.whatwg.org/multipage/parsing.html#input-stream) for parser. The encoding [confidence](https://html.spec.whatwg.org/multipage/parsing.html#concept-encoding-confidence) is _irrelevant_.

4.   Start parser and let it run until it has consumed all the characters just inserted into the input stream.

This might mutate the document's [mode](https://dom.spec.whatwg.org/#concept-document-mode).

#### 8.5.2 Unsafe HTML parsing methods[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#unsafe-html-parsing-methods)

`element.setHTMLUnsafe(html)`
Parses html using the HTML parser, and replaces the children of element with the result. element provides context for the HTML parser.

`shadowRoot.setHTMLUnsafe(html)`
Parses html using the HTML parser, and replaces the children of shadowRoot with the result. shadowRoot's [host](https://dom.spec.whatwg.org/#concept-documentfragment-host) provides context for the HTML parser.

`doc = Document.parseHTMLUnsafe(html)`
Parses html using the HTML parser, and returns the resulting `Document`.

Note that `script` elements are not evaluated during parsing, and the resulting document's [encoding](https://dom.spec.whatwg.org/#concept-document-encoding) will always be [UTF-8](https://encoding.spec.whatwg.org/#utf-8). The document's [URL](https://dom.spec.whatwg.org/#concept-document-url) will be `about:blank`.

These methods perform no sanitization to remove potentially-dangerous elements and attributes like `script` or [event handler content attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes).

* * *

#### 8.5.3 HTML serialization methods[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#html-serialization-methods)

`html = element.getHTML({ serializableShadowRoots, shadowRoots })`
Returns the result of serializing element to HTML. [Shadow roots](https://dom.spec.whatwg.org/#concept-shadow-root) within element are serialized according to the provided options:

*   If `serializableShadowRoots` is true, then all shadow roots marked as [serializable](https://dom.spec.whatwg.org/#shadowroot-serializable) are serialized.

*   If the `shadowRoots` array is provided, then all shadow roots specified in the array are serialized, regardless of whether or not they are marked as serializable.

If neither option is provided, then no shadow roots are serialized.

`html = shadowRoot.getHTML({ serializableShadowRoots, shadowRoots })`
Returns the result of serializing shadowRoot to HTML, using its [shadow host](https://dom.spec.whatwg.org/#concept-documentfragment-host) as the context element. [Shadow roots](https://dom.spec.whatwg.org/#concept-shadow-root) within shadowRoot are serialized according to the provided options, as above.

#### 8.5.4 The `innerHTML` property[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-innerhtml-property)

The `innerHTML` property has a number of outstanding issues in the DOM Parsing and Serialization[issue tracker](https://github.com/w3c/DOM-Parsing/issues), documenting various problems with its specification.

`element.innerHTML`
Returns a fragment of HTML or XML that represents the element's contents.

In the case of an XML document, throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if the element cannot be serialized to XML.

`element.innerHTML = value`
Replaces the contents of the element with nodes parsed from the given string.

In the case of an XML document, throws a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException` if the given string is not well-formed.

`shadowRoot.innerHTML`
Returns a fragment of HTML that represents the shadow roots's contents.

`shadowRoot.innerHTML = value`
Replaces the contents of the shadow root with nodes parsed from the given string.

These properties' setters perform no sanitization to remove potentially-dangerous elements and attributes like `script` or [event handler content attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes).

`Element`'s `innerHTML` getter steps are to return the result of running [fragment serializing algorithm steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#fragment-serializing-algorithm-steps) with [this](https://webidl.spec.whatwg.org/#this) and true.

`ShadowRoot`'s `innerHTML` getter steps are to return the result of running [fragment serializing algorithm steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#fragment-serializing-algorithm-steps) with [this](https://webidl.spec.whatwg.org/#this) and true.

`Element`'s `innerHTML` setter steps are:

1.   Let compliantString be the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedHTML`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), the given value, "`Element innerHTML`", and "`script`".

2.   Let context be [this](https://webidl.spec.whatwg.org/#this).

3.   Let fragment be the result of invoking the [fragment parsing algorithm steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#fragment-parsing-algorithm-steps) with context and compliantString.

4.   If context is a `template` element, then set context to the `template` element's [template contents](https://html.spec.whatwg.org/multipage/scripting.html#template-contents) (a `DocumentFragment`).

Setting `innerHTML` on a `template` element will replace all the nodes in its [template contents](https://html.spec.whatwg.org/multipage/scripting.html#template-contents) rather than its [children](https://dom.spec.whatwg.org/#concept-tree-child).

5.   [Replace all](https://dom.spec.whatwg.org/#concept-node-replace-all) with fragment within context.

`ShadowRoot`'s `innerHTML` setter steps are:

1.   Let compliantString be the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedHTML`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), the given value, "`ShadowRoot innerHTML`", and "`script`".

2.   Let context be [this](https://webidl.spec.whatwg.org/#this)'s [host](https://dom.spec.whatwg.org/#concept-documentfragment-host).

3.   Let fragment be the result of invoking the [fragment parsing algorithm steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#fragment-parsing-algorithm-steps) with context and compliantString.

4.   [Replace all](https://dom.spec.whatwg.org/#concept-node-replace-all) with fragment within [this](https://webidl.spec.whatwg.org/#this).

#### 8.5.5 The `outerHTML` property[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-outerhtml-property)

The `outerHTML` property has a number of outstanding issues in the DOM Parsing and Serialization[issue tracker](https://github.com/w3c/DOM-Parsing/issues), documenting various problems with its specification.

`element.outerHTML`
Returns a fragment of HTML or XML that represents the element and its contents.

In the case of an XML document, throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if the element cannot be serialized to XML.

`element.outerHTML = value`
Replaces the element with nodes parsed from the given string.

In the case of an XML document, throws a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException` if the given string is not well-formed.

Throws a ["`NoModificationAllowedError`"](https://webidl.spec.whatwg.org/#nomodificationallowederror)`DOMException` if the parent of the element is a [`Document`](https://html.spec.whatwg.org/multipage/dom.html#document).

This property's setter performs no sanitization to remove potentially-dangerous elements and attributes like `script` or [event handler content attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes).

`Element`'s `outerHTML` getter steps are:

1.   Let element be a fictional node whose only child is [this](https://webidl.spec.whatwg.org/#this).

2.   Return the result of running [fragment serializing algorithm steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#fragment-serializing-algorithm-steps) with element and true.

`Element`'s `outerHTML` setter steps are:

1.   Let compliantString be the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedHTML`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), the given value, "`Element outerHTML`", and "`script`".

2.   Let parent be [this](https://webidl.spec.whatwg.org/#this)'s [parent](https://dom.spec.whatwg.org/#concept-tree-parent).

3.   If parent is null, return. There would be no way to obtain a reference to the nodes created even if the remaining steps were run.

4.   If parent is a `Document`, throw a ["`NoModificationAllowedError`"](https://webidl.spec.whatwg.org/#nomodificationallowederror)`DOMException`.

5.   If parent is a `DocumentFragment`, set parent to the result of [creating an element](https://dom.spec.whatwg.org/#concept-create-element) given [this](https://webidl.spec.whatwg.org/#this)'s [node document](https://dom.spec.whatwg.org/#concept-node-document), "`body`", and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace).

6.   Let fragment be the result of invoking the [fragment parsing algorithm steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#fragment-parsing-algorithm-steps) given parent and compliantString.

7.   [Replace](https://dom.spec.whatwg.org/#concept-node-replace)[this](https://webidl.spec.whatwg.org/#this) with fragment within [this](https://webidl.spec.whatwg.org/#this)'s [parent](https://dom.spec.whatwg.org/#concept-tree-parent).

#### 8.5.6 The `insertAdjacentHTML()` method[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-insertadjacenthtml()-method)

The `insertAdjacentHTML()` method has a number of outstanding issues in the DOM Parsing and Serialization[issue tracker](https://github.com/w3c/DOM-Parsing/issues), documenting various problems with its specification.

`element.insertAdjacentHTML(position, string)`
Parses string as HTML or XML and inserts the resulting nodes into the tree in the position given by the position argument, as follows:

"`beforebegin`"Before the element itself (i.e., after element's previous sibling)"`afterbegin`"Just inside the element, before its first child."`beforeend`"Just inside the element, after its last child."`afterend`"After the element itself (i.e., before element's next sibling)
Throws a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException` if the arguments have invalid values (e.g., in the case of an [XML document](https://dom.spec.whatwg.org/#xml-document), if the given string is not well-formed).

Throws a ["`NoModificationAllowedError`"](https://webidl.spec.whatwg.org/#nomodificationallowederror)`DOMException` if the given position isn't possible (e.g. inserting elements after the root element of a `Document`).

This method performs no sanitization to remove potentially-dangerous elements and attributes like `script` or [event handler content attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes).

`Element`'s 
```
insertAdjacentHTML(position,
  string)
```
 method steps are:

1.   Let compliantString be the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedHTML`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), string, "`Element insertAdjacentHTML`", and "`script`".

2.   Let context be null.

3.   Use the first matching item from this list:

If position is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`beforebegin`"If position is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`afterend`"
    1.   Set context to [this](https://webidl.spec.whatwg.org/#this)'s [parent](https://html.spec.whatwg.org/multipage/nav-history-apis.html#dom-parent).

    2.   If context is null or a `Document`, throw a ["`NoModificationAllowedError`"](https://webidl.spec.whatwg.org/#nomodificationallowederror)`DOMException`.

If position is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`afterbegin`"If position is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`beforeend`"Set context to [this](https://webidl.spec.whatwg.org/#this).Otherwise
Throw a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException`.

4.   If context is not an `Element` or all of the following are true:

    *   context's [node document](https://dom.spec.whatwg.org/#concept-node-document) is an HTML document;

    *   context's [local name](https://dom.spec.whatwg.org/#concept-element-local-name) is "`html`"; and

    *   context's [namespace](https://dom.spec.whatwg.org/#concept-element-namespace) is the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace),

then set context to the result of [creating an element](https://dom.spec.whatwg.org/#concept-create-element) given [this](https://webidl.spec.whatwg.org/#this)'s [node document](https://dom.spec.whatwg.org/#concept-node-document), "`body`", and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace).

5.   Let fragment be the result of invoking the [fragment parsing algorithm steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#fragment-parsing-algorithm-steps) with context and compliantString.

6.   Use the first matching item from this list: If position is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`beforebegin`"
[Insert](https://dom.spec.whatwg.org/#concept-node-insert)fragment into [this](https://webidl.spec.whatwg.org/#this)'s [parent](https://html.spec.whatwg.org/multipage/nav-history-apis.html#dom-parent) before [this](https://webidl.spec.whatwg.org/#this).

If position is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`afterbegin`"
[Insert](https://dom.spec.whatwg.org/#concept-node-insert)fragment into [this](https://webidl.spec.whatwg.org/#this) before its [first child](https://dom.spec.whatwg.org/#concept-tree-first-child).

If position is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`beforeend`"
[Append](https://dom.spec.whatwg.org/#concept-node-append)fragment to [this](https://webidl.spec.whatwg.org/#this).

If position is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`afterend`"
[Insert](https://dom.spec.whatwg.org/#concept-node-insert)fragment into [this](https://webidl.spec.whatwg.org/#this)'s [parent](https://html.spec.whatwg.org/multipage/nav-history-apis.html#dom-parent) before [this](https://webidl.spec.whatwg.org/#this)'s [next sibling](https://dom.spec.whatwg.org/#concept-tree-next-sibling).

As with other direct `Node`-manipulation APIs (and unlike `innerHTML`), `insertAdjacentHTML()` does not include any special handling for `template` elements. In most cases you will want to use `templateEl.content.insertAdjacentHTML()` instead of directly manipulating the child nodes of a `template` element.

#### 8.5.7 The `createContextualFragment()` method[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-createcontextualfragment()-method)

The `createContextualFragment()` method has a number of outstanding issues in the DOM Parsing and Serialization[issue tracker](https://github.com/w3c/DOM-Parsing/issues), documenting various problems with its specification.

`docFragment = range.createContextualFragment(string)`
Returns a `DocumentFragment` created from the markup string string using range's [start node](https://dom.spec.whatwg.org/#concept-range-start-node) as the context in which fragment is parsed.

This method performs no sanitization to remove potentially-dangerous elements and attributes like `script` or [event handler content attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes).

```
partial interface Range {
  [CEReactions, NewObject] DocumentFragment createContextualFragment((TrustedHTML or DOMString) string);
};
```

`Range`'s `createContextualFragment(string)` method steps are:

1.   Let compliantString be the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedHTML`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), string, "`Range createContextualFragment`", and "`script`".

2.   Let node be [this](https://webidl.spec.whatwg.org/#this)'s [start node](https://dom.spec.whatwg.org/#concept-range-start-node).

3.   Let element be null.

4.   If node[implements](https://webidl.spec.whatwg.org/#implements)`Element`, set element to node.

5.   Otherwise, if node[implements](https://webidl.spec.whatwg.org/#implements)`Text` or , set element to node's [parent element](https://dom.spec.whatwg.org/#parent-element).

6.   If element is null or all of the following are true:

    *   element's [node document](https://dom.spec.whatwg.org/#concept-node-document) is an HTML document;

    *   element's [local name](https://dom.spec.whatwg.org/#concept-element-local-name) is "`html`"; and

    *   element's [namespace](https://dom.spec.whatwg.org/#concept-element-namespace) is the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace),

then set element to the result of [creating an element](https://dom.spec.whatwg.org/#concept-create-element) given [this](https://webidl.spec.whatwg.org/#this)'s [node document](https://dom.spec.whatwg.org/#concept-node-document), "`body`", and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace).

7.   Return the result of invoking the [fragment parsing algorithm steps](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#fragment-parsing-algorithm-steps) with element, compliantString, and [Fragment](https://html.spec.whatwg.org/multipage/parsing.html#scripting-mode-fragment).

#### 8.5.8 The `XMLSerializer` interface[](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#the-xmlserializer-interface)

The `XMLSerializer` interface has a number of outstanding issues in the DOM Parsing and Serialization[issue tracker](https://github.com/w3c/DOM-Parsing/issues), documenting various problems with its specification. The remainder of DOM Parsing and Serialization will be gradually upstreamed to this specification.

`xmlSerializer = new XMLSerializer()`
Constructs a new `XMLSerializer` object.

`string = xmlSerializer.serializeToString(root)`
Returns the result of serializing root to XML.

Throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if root cannot be serialized to XML.

The design of `XMLSerializer`, as a class that needs to be constructed and then have its `serializeToString()` method called, is an unfortunate historical artifact. If we were designing this functionality today it would be a standalone function.

```
[Exposed=Window]
interface XMLSerializer {
  constructor();

  DOMString serializeToString(Node root);
};
```

The `new XMLSerializer()` constructor steps are to do nothing.

The `serializeToString(root)` method steps are:

1.   Return the [XML serialization](https://w3c.github.io/DOM-Parsing/#dfn-xml-serialization) of root given false.

[← 8 Web application APIs](https://html.spec.whatwg.org/multipage/webappapis.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [8.6 Timers →](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html)
