# Source: https://html.spec.whatwg.org/multipage/nav-history-apis.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/nav-history-apis.html

Markdown Content:
HTML

Living Standard — Last Updated 16 March 2026

← 7 Loading web pages — Table of Contents — 7.3 Infrastructure for sequences of documents →
7.2 APIs related to navigation and session history
7.2.1 Security infrastructure for Window, WindowProxy, and Location objects
7.2.1.1 Integration with IDL
7.2.1.2 Shared internal slot: [[CrossOriginPropertyDescriptorMap]]
7.2.1.3 Shared abstract operations
7.2.1.3.1 CrossOriginProperties ( O )
7.2.1.3.2 CrossOriginPropertyFallback ( P )
7.2.1.3.3 IsPlatformObjectSameOrigin ( O )
7.2.1.3.4 CrossOriginGetOwnPropertyHelper ( O, P )
7.2.1.3.5 CrossOriginGet ( O, P, Receiver )
7.2.1.3.6 CrossOriginSet ( O, P, V, Receiver )
7.2.1.3.7 CrossOriginOwnPropertyKeys ( O )
7.2.2 The Window object
7.2.2.1 Opening and closing windows
7.2.2.2 Indexed access on the Window object
7.2.2.3 Named access on the Window object
7.2.2.4 Accessing related windows
7.2.2.5 Historical browser interface element APIs
7.2.2.6 Script settings for Window objects
7.2.3 The WindowProxy exotic object
7.2.3.1 [[GetPrototypeOf]] ( )
7.2.3.2 [[SetPrototypeOf]] ( V )
7.2.3.3 [[IsExtensible]] ( )
7.2.3.4 [[PreventExtensions]] ( )
7.2.3.5 [[GetOwnProperty]] ( P )
7.2.3.6 [[DefineOwnProperty]] ( P, Desc )
7.2.3.7 [[Get]] ( P, Receiver )
7.2.3.8 [[Set]] ( P, V, Receiver )
7.2.3.9 [[Delete]] ( P )
7.2.3.10 [[OwnPropertyKeys]] ( )
7.2.4 The Location interface
7.2.4.1 [[GetPrototypeOf]] ( )
7.2.4.2 [[SetPrototypeOf]] ( V )
7.2.4.3 [[IsExtensible]] ( )
7.2.4.4 [[PreventExtensions]] ( )
7.2.4.5 [[GetOwnProperty]] ( P )
7.2.4.6 [[DefineOwnProperty]] ( P, Desc )
7.2.4.7 [[Get]] ( P, Receiver )
7.2.4.8 [[Set]] ( P, V, Receiver )
7.2.4.9 [[Delete]] ( P )
7.2.4.10 [[OwnPropertyKeys]] ( )
7.2.5 The History interface
7.2.6 The navigation API
7.2.6.1 Introduction
7.2.6.2 The Navigation interface
7.2.6.3 Core infrastructure
7.2.6.4 Initializing and updating the entry list
7.2.6.5 The NavigationHistoryEntry interface
7.2.6.6 The history entry list
7.2.6.7 Initiating navigations
7.2.6.8 Ongoing navigation tracking
7.2.6.9 The NavigationActivation interface
7.2.6.10 The navigate event
7.2.6.10.1 The NavigateEvent interface
7.2.6.10.2 The NavigationPrecommitController interface
7.2.6.10.3 The NavigationDestination interface
7.2.6.10.4 Firing the event
7.2.6.10.5 Scroll and focus behavior
7.2.7 Event interfaces
7.2.7.1 The NavigationCurrentEntryChangeEvent interface
7.2.7.2 The PopStateEvent interface
7.2.7.3 The HashChangeEvent interface
7.2.7.4 The PageSwapEvent interface
7.2.7.5 The PageRevealEvent interface
7.2.7.6 The PageTransitionEvent interface
7.2.7.7 The BeforeUnloadEvent interface
7.2.8 The NotRestoredReasons interface
7.2 APIs related to navigation and session history
7.2.1 Security infrastructure for Window, WindowProxy, and Location objects

Although typically objects cannot be accessed across origins, the web platform would not be true to itself if it did not have some legacy exceptions to that rule that the web depends upon.

This section uses the terminology and typographic conventions from the JavaScript specification. [JAVASCRIPT]

7.2.1.1 Integration with IDL

When perform a security check is invoked, with a platformObject, identifier, and type, run these steps:

If platformObject is not a Window or Location object, then return.

For each e of CrossOriginProperties(platformObject):

If SameValue(e.[[Property]], identifier) is true, then:

If type is "method" and e has neither [[NeedsGet]] nor [[NeedsSet]], then return.

Otherwise, if type is "getter" and e.[[NeedsGet]] is true, then return.

Otherwise, if type is "setter" and e.[[NeedsSet]] is true, then return.

If IsPlatformObjectSameOrigin(platformObject) is false, then throw a "SecurityError" DOMException.

7.2.1.2 Shared internal slot: [[CrossOriginPropertyDescriptorMap]]

Window and Location objects both have a [[CrossOriginPropertyDescriptorMap]] internal slot, whose value is initially an empty map.

The [[CrossOriginPropertyDescriptorMap]] internal slot contains a map with entries whose keys are (currentGlobal, objectGlobal, propertyKey)-tuples and values are property descriptors, as a memoization of what is visible to scripts when currentGlobal inspects a Window or Location object from objectGlobal. It is filled lazily by CrossOriginGetOwnPropertyHelper, which consults it on future lookups.

User agents should allow a value held in the map to be garbage collected along with its corresponding key when nothing holds a reference to any part of the value. That is, as long as garbage collection is not observable.

For example, with const href = Object.getOwnPropertyDescriptor(crossOriginLocation, "href").set the value and its corresponding key in the map cannot be garbage collected as that would be observable.

User agents may have an optimization whereby they remove key-value pairs from the map when document.domain is set. This is not observable as document.domain cannot revisit an earlier value.

For example, setting document.domain to "example.com" on www.example.com means user agents can remove all key-value pairs from the map where part of the key is www.example.com, as that can never be part of the origin again and therefore the corresponding value could never be retrieved from the map.

7.2.1.3 Shared abstract operations
7.2.1.3.1 CrossOriginProperties ( O )

Assert: O is a Location or Window object.

If O is a Location object, then return « { [[Property]]: "href", [[NeedsGet]]: false, [[NeedsSet]]: true }, { [[Property]]: "replace" } ».

Return « { [[Property]]: "window", [[NeedsGet]]: true, [[NeedsSet]]: false }, { [[Property]]: "self", [[NeedsGet]]: true, [[NeedsSet]]: false }, { [[Property]]: "location", [[NeedsGet]]: true, [[NeedsSet]]: true }, { [[Property]]: "close" }, { [[Property]]: "closed", [[NeedsGet]]: true, [[NeedsSet]]: false }, { [[Property]]: "focus" }, { [[Property]]: "blur" }, { [[Property]]: "frames", [[NeedsGet]]: true, [[NeedsSet]]: false }, { [[Property]]: "length", [[NeedsGet]]: true, [[NeedsSet]]: false }, { [[Property]]: "top", [[NeedsGet]]: true, [[NeedsSet]]: false }, { [[Property]]: "opener", [[NeedsGet]]: true, [[NeedsSet]]: false }, { [[Property]]: "parent", [[NeedsGet]]: true, [[NeedsSet]]: false }, { [[Property]]: "postMessage" } ».

This abstract operation does not return a Completion Record.

Indexed properties do not need to be safelisted in this algorithm, as they are handled directly by the WindowProxy object.

A JavaScript property name P is a cross-origin accessible window property name if it is "window", "self", "location", "close", "closed", "focus", "blur", "frames", "length", "top", "opener", "parent", "postMessage", or an array index property name.

7.2.1.3.2 CrossOriginPropertyFallback ( P )

If P is "then", %Symbol.toStringTag%, %Symbol.hasInstance%, or %Symbol.isConcatSpreadable%, then return PropertyDescriptor { [[Value]]: undefined, [[Writable]]: false, [[Enumerable]]: false, [[Configurable]]: true }.

Throw a "SecurityError" DOMException.

7.2.1.3.3 IsPlatformObjectSameOrigin ( O )

Return true if the current settings object's origin is same origin-domain with O's relevant settings object's origin, and false otherwise.

This abstract operation does not return a Completion Record.

Here the current settings object roughly corresponds to the "caller", because this check occurs before the execution context for the getter/setter/method in question makes its way onto the JavaScript execution context stack. For example, in the code w.document, this step is invoked before the document getter is reached as part of the [[Get]] algorithm for the WindowProxy w.

7.2.1.3.4 CrossOriginGetOwnPropertyHelper ( O, P )

If this abstract operation returns undefined and there is no custom behavior, the caller needs to throw a "SecurityError" DOMException. In practice this is handled by the caller calling CrossOriginPropertyFallback.

Let crossOriginKey be a tuple consisting of the current settings object, O's relevant settings object, and P.

For each e of CrossOriginProperties(O):

If SameValue(e.[[Property]], P) is true, then:

If the value of the [[CrossOriginPropertyDescriptorMap]] internal slot of O contains an entry whose key is crossOriginKey, then return that entry's value.

Let originalDesc be OrdinaryGetOwnProperty(O, P).

Let crossOriginDesc be undefined.

If e.[[NeedsGet]] and e.[[NeedsSet]] are absent, then:

Let value be originalDesc.[[Value]].

If IsCallable(value) is true, then set value to an anonymous built-in function, created in the current realm, that performs the same steps as the IDL operation P on object O.

Set crossOriginDesc to PropertyDescriptor { [[Value]]: value, [[Enumerable]]: false, [[Writable]]: false, [[Configurable]]: true }.

Otherwise:

Let crossOriginGet be undefined.

If e.[[NeedsGet]] is true, then set crossOriginGet to an anonymous built-in function, created in the current realm, that performs the same steps as the getter of the IDL attribute P on object O.

Let crossOriginSet be undefined.

If e.[[NeedsSet]] is true, then set crossOriginSet to an anonymous built-in function, created in the current realm, that performs the same steps as the setter of the IDL attribute P on object O.

Set crossOriginDesc to PropertyDescriptor { [[Get]]: crossOriginGet, [[Set]]: crossOriginSet, [[Enumerable]]: false, [[Configurable]]: true }.

Create an entry in the value of the [[CrossOriginPropertyDescriptorMap]] internal slot of O with key crossOriginKey and value crossOriginDesc.

Return crossOriginDesc.

Return undefined.

This abstract operation does not return a Completion Record.

The reason that the property descriptors produced here are configurable is to preserve the invariants of the essential internal methods required by the JavaScript specification. In particular, since the value of the property can change as a consequence of navigation, it is required that the property be configurable. (However, see tc39/ecma262 issue #672 and references to it elsewhere in this specification for cases where we are not able to preserve these invariants, for compatibility with existing web content.) [JAVASCRIPT]

The reason the property descriptors are non-enumerable, despite this mismatching the same-origin behavior, is for compatibility with existing web content. See issue #3183 for details.

7.2.1.3.5 CrossOriginGet ( O, P, Receiver )

Let desc be ? O.[[GetOwnProperty]](P).

Assert: desc is not undefined.

If IsDataDescriptor(desc) is true, then return desc.[[Value]].

Assert: IsAccessorDescriptor(desc) is true.

Let getter be desc.[[Get]].

If getter is undefined, then throw a "SecurityError" DOMException.

Return ? Call(getter, Receiver).

7.2.1.3.6 CrossOriginSet ( O, P, V, Receiver )

Let desc be ? O.[[GetOwnProperty]](P).

Assert: desc is not undefined.

If desc.[[Set]] is present and its value is not undefined, then:

Perform ? Call(desc.[[Set]], Receiver, « V »).

Return true.

Throw a "SecurityError" DOMException.

7.2.1.3.7 CrossOriginOwnPropertyKeys ( O )

Let keys be a new empty List.

For each e of CrossOriginProperties(O), append e.[[Property]] to keys.

Return the concatenation of keys and « "then", %Symbol.toStringTag%, %Symbol.hasInstance%, %Symbol.isConcatSpreadable% ».

This abstract operation does not return a Completion Record.

7.2.2 The Window object
✔MDN
[Global=Window,
 Exposed=Window,
 LegacyUnenumerableNamedProperties]
interface Window : EventTarget {
  // the current browsing context
  [LegacyUnforgeable] readonly attribute WindowProxy window;
  [Replaceable] readonly attribute WindowProxy self;
  [LegacyUnforgeable] readonly attribute Document document;
  attribute DOMString name; 
  [PutForwards=href, LegacyUnforgeable] readonly attribute Location location;
  readonly attribute History history;
  [Replaceable] readonly attribute Navigation navigation;
  readonly attribute CustomElementRegistry customElements;
  [Replaceable] readonly attribute BarProp locationbar;
  [Replaceable] readonly attribute BarProp menubar;
  [Replaceable] readonly attribute BarProp personalbar;
  [Replaceable] readonly attribute BarProp scrollbars;
  [Replaceable] readonly attribute BarProp statusbar;
  [Replaceable] readonly attribute BarProp toolbar;
  attribute DOMString status;
  undefined close();
  readonly attribute boolean closed;
  undefined stop();
  undefined focus();
  undefined blur();

  // other browsing contexts
  [Replaceable] readonly attribute WindowProxy frames;
  [Replaceable] readonly attribute unsigned long length;
  [LegacyUnforgeable] readonly attribute WindowProxy? top;
  attribute any opener;
  [Replaceable] readonly attribute WindowProxy? parent;
  readonly attribute Element? frameElement;
  WindowProxy? open(optional USVString url = "", optional DOMString target = "_blank", optional [LegacyNullToEmptyString] DOMString features = "");

  // Since this is the global object, the IDL named getter adds a NamedPropertiesObject exotic
  // object on the prototype chain. Indeed, this does not make the global object an exotic object.
  // Indexed access is taken care of by the WindowProxy exotic object.
  getter object (DOMString name);

  // the user agent
  readonly attribute Navigator navigator;
  [Replaceable] readonly attribute Navigator clientInformation; // legacy alias of .navigator
  readonly attribute boolean originAgentCluster;

  // user prompts
  undefined alert();
  undefined alert(DOMString message);
  boolean confirm(optional DOMString message = "");
  DOMString? prompt(optional DOMString message = "", optional DOMString default = "");
  undefined print();

  undefined postMessage(any message, USVString targetOrigin, optional sequence<object> transfer = []);
  undefined postMessage(any message, optional WindowPostMessageOptions options = {});

  // also has obsolete members
};
Window includes GlobalEventHandlers;
Window includes WindowEventHandlers;

dictionary WindowPostMessageOptions : StructuredSerializeOptions {
  USVString targetOrigin = "/";
};
window.window
✔MDN
window.frames
✔MDN
window.self
✔MDN

These attributes all return window.

window.document
✔MDN

Returns the Document associated with window.

document.defaultView
✔MDN

Returns the Window associated with document, if there is one, or null otherwise.

The Window object has an associated Document, which is a Document object. It is set when the Window object is created, and only ever changed during navigation from the initial about:blank Document.

A Window's browsing context is its associated Document's browsing context. It is either null or a browsing context.

A Window's navigable is the navigable whose active document is the Window's associated Document's, or null if there is no such navigable.

The window, frames, and self getter steps are to return this's relevant realm.[[GlobalEnv]].[[GlobalThisValue]].

The document getter steps are to return this's associated Document.

The Document object associated with a Window object can change in exactly one case: when the navigate algorithm creates a new Document object for the first page loaded in a browsing context. In that specific case, the Window object of the initial about:blank page is reused and gets a new Document object.

The defaultView getter steps are:

If this's browsing context is null, then return null.

Return this's browsing context's WindowProxy object.

✔MDN

For historical reasons, Window objects must also have a writable, configurable, non-enumerable property named HTMLDocument whose value is the Document interface object.

7.2.2.1 Opening and closing windows
window = window.open([ url [, target [, features ] ] ])
✔MDN

Opens a window to show url (defaults to "about:blank"), and returns it. target (defaults to "_blank") gives the name of the new window. If a window already exists with that name, it is reused. The features argument can contain a set of comma-separated tokens:

"noopener"
"noreferrer"

These behave equivalently to the noopener and noreferrer link types on hyperlinks.

"popup"

Encourages user agents to provide a minimal web browser user interface for the new window. (Impacts the visible getter on all BarProp objects as well.)

globalThis.open("https://email.example/message/CAOOOkFcWW97r8yg=SsWg7GgCmp4suVX9o85y8BvNRqMjuc5PXg", undefined, "noopener,popup");
window.name [ = value ]
✔MDN

Returns the name of the window.

Can be set, to change the name.

window.close()
✔MDN

Closes the window.

window.closed
✔MDN

Returns true if the window has been closed, false otherwise.

window.stop()
✔MDN

Cancels the document load.

To get noopener for window open, given a Document sourceDocument, an ordered map tokenizedFeatures, and a URL record-or-null url, perform the following steps. They return a boolean.

If url is not null and url's blob URL entry is not null:

Let blobOrigin be url's blob URL entry's environment's origin.

Let topLevelOrigin be sourceDocument's relevant settings object's top-level origin.

If blobOrigin is not same site with topLevelOrigin, then return true.

Let noopener be false.

If tokenizedFeatures["noopener"] exists, then set noopener to the result of parsing tokenizedFeatures["noopener"] as a boolean feature.

Return noopener.

The window open steps, given a string url, a string target, and a string features, are as follows:

If the event loop's termination nesting level is nonzero, then return null.

Let sourceDocument be the entry global object's associated Document.

Let urlRecord be null.

If url is not the empty string, then:

Set urlRecord to the result of encoding-parsing a URL given url, relative to sourceDocument.

If urlRecord is failure, then throw a "SyntaxError" DOMException.

If target is the empty string, then set target to "_blank".

Let tokenizedFeatures be the result of tokenizing features.

Let noreferrer be false.

If tokenizedFeatures["noreferrer"] exists, then set noreferrer to the result of parsing tokenizedFeatures["noreferrer"] as a boolean feature.

Let noopener be the result of getting noopener for window open with sourceDocument, tokenizedFeatures, and urlRecord.

Remove tokenizedFeatures["noopener"] and tokenizedFeatures["noreferrer"].

Let referrerPolicy be the empty string.

If noreferrer is true, then set noopener to true and set referrerPolicy to "no-referrer".

Let targetNavigable and windowType be the result of applying the rules for choosing a navigable given target, sourceDocument's node navigable, and noopener.

If there is a user agent that supports control-clicking a link to open it in a new tab, and the user control-clicks on an element whose onclick handler uses the window.open() API to open a page in an iframe element, the user agent could override the selection of the target browsing context to instead target a new tab.

If targetNavigable is null, then return null.

If windowType is either "new and unrestricted" or "new with no opener", then:

Set targetNavigable's active browsing context's is popup to the result of checking if a popup window is requested, given tokenizedFeatures.

Set up browsing context features for targetNavigable's active browsing context given tokenizedFeatures. [CSSOMVIEW]

If urlRecord is null, then set urlRecord to a URL record representing about:blank.

If urlRecord matches about:blank, then perform the URL and history update steps given targetNavigable's active document and urlRecord.

This is necessary in case url is something like about:blank?foo. If url is just plain about:blank, this will do nothing.

Otherwise, navigate targetNavigable to urlRecord using sourceDocument, with referrerPolicy set to referrerPolicy and exceptionsEnabled set to true.

Otherwise:

If urlRecord is not null, then navigate targetNavigable to urlRecord using sourceDocument, with referrerPolicy set to referrerPolicy and exceptionsEnabled set to true.

If noopener is false, then set targetNavigable's active browsing context's opener browsing context to sourceDocument's browsing context.

If noopener is true or windowType is "new with no opener", then return null.

Return targetNavigable's active WindowProxy.

The open(url, target, features) method steps are to run the window open steps with url, target, and features.

The method provides a mechanism for navigating an existing browsing context or opening and navigating an auxiliary browsing context.

To tokenize the features argument:

Let tokenizedFeatures be a new ordered map.

Let position point at the first code point of features.

While position is not past the end of features:

Let name be the empty string.

Let value be the empty string.

Collect a sequence of code points that are feature separators from features given position. This skips past leading separators before the name.

Collect a sequence of code points that are not feature separators from features given position. Set name to the collected characters, converted to ASCII lowercase.

Set name to the result of normalizing the feature name name.

While position is not past the end of features and the code point at position in features is not U+003D (=):

If the code point at position in features is U+002C (,), or if it is not a feature separator, then break.

Advance position by 1.

This skips to the first U+003D (=) but does not skip past a U+002C (,) or a non-separator.

If the code point at position in features is a feature separator:

While position is not past the end of features and the code point at position in features is a feature separator:

If the code point at position in features is U+002C (,), then break.

Advance position by 1.

This skips to the first non-separator but does not skip past a U+002C (,).

Collect a sequence of code points that are not feature separators code points from features given position. Set value to the collected code points, converted to ASCII lowercase.

If name is not the empty string, then set tokenizedFeatures[name] to value.

Return tokenizedFeatures.

To check if a window feature is set, given tokenizedFeatures, featureName, and defaultValue:

If tokenizedFeatures[featureName] exists, then return the result of parsing tokenizedFeatures[featureName] as a boolean feature.

Return defaultValue.

To check if a popup window is requested, given tokenizedFeatures:

If tokenizedFeatures is empty, then return false.

If tokenizedFeatures["popup"] exists, then return the result of parsing tokenizedFeatures["popup"] as a boolean feature.

Let location be the result of checking if a window feature is set, given tokenizedFeatures, "location", and false.

Let toolbar be the result of checking if a window feature is set, given tokenizedFeatures, "toolbar", and false.

If location and toolbar are both false, then return true.

Let menubar be the result of checking if a window feature is set, given tokenizedFeatures, "menubar", and false.

If menubar is false, then return true.

Let resizable be the result of checking if a window feature is set, given tokenizedFeatures, "resizable", and true.

If resizable is false, then return true.

Let scrollbars be the result of checking if a window feature is set, given tokenizedFeatures, "scrollbars", and false.

If scrollbars is false, then return true.

Let status be the result of checking if a window feature is set, given tokenizedFeatures, "status", and false.

If status is false, then return true.

Return false.

A code point is a feature separator if it is ASCII whitespace, U+003D (=), or U+002C (,).

For legacy reasons, there are some aliases of some feature names. To normalize a feature name name, switch on name:

"screenx"
Return "left".
"screeny"
Return "top".
"innerwidth"
Return "width".
"innerheight"
Return "height".
Anything else
Return name.

To parse a boolean feature given a string value:

If value is the empty string, then return true.

If value is "yes", then return true.

If value is "true", then return true.

Let parsed be the result of parsing value as an integer.

If parsed is an error, then set it to 0.

Return false if parsed is 0, and true otherwise.

The name getter steps are:

If this's navigable is null, then return the empty string.

Return this's navigable's target name.

The name setter steps are:

If this's navigable is null, then return.

Set this's navigable's active session history entry's document state's navigable target name to the given value.

The name gets reset when the navigable is navigated to another origin.

The close() method steps are:

Let thisTraversable be this's navigable.

If thisTraversable is not a top-level traversable, then return.

If thisTraversable's is closing is true, then return.

Let browsingContext be thisTraversable's active browsing context.

Let sourceSnapshotParams be the result of snapshotting source snapshot params given thisTraversable's active document.

If all the following are true:

thisTraversable is script-closable;

the incumbent global object's browsing context is familiar with browsingContext; and

the incumbent global object's navigable is allowed by sandboxing to navigate thisTraversable, given sourceSnapshotParams,

then:

Set thisTraversable's is closing to true.

Queue a task on the DOM manipulation task source to definitely close thisTraversable.

A navigable is script-closable if it is a top-level traversable, and any of the following are true:

its is created by web content is true; or
its session history entries's size is 1.

The closed getter steps are to return true if this's browsing context is null or its is closing is true; otherwise false.

The stop() method steps are:

If this's navigable is null, then return.

Stop loading this's navigable.

7.2.2.2 Indexed access on the Window object
window.length
✔MDN

Returns the number of document-tree child navigables.

window[index]

Returns the WindowProxy corresponding to the indicated document-tree child navigables.

The length getter steps are to return this's associated Document's document-tree child navigables's size.

Indexed access to document-tree child navigables is defined through the [[GetOwnProperty]] internal method of the WindowProxy object.

7.2.2.3 Named access on the Window object
window[name]

Returns the indicated element or collection of elements.

As a general rule, relying on this will lead to brittle code. Which IDs end up mapping to this API can vary over time, as new features are added to the web platform, for example. Instead of this, use document.getElementById() or document.querySelector().

The document-tree child navigable target name property set of a Window object window is the return value of running these steps:

Let children be the document-tree child navigables of window's associated Document.

Let firstNamedChildren be an empty ordered set.

For each navigable of children:

Let name be navigable's target name.

If name is the empty string, then continue.

If firstNamedChildren contains a navigable whose target name is name, then continue.

Append navigable to firstNamedChildren.

Let names be an empty ordered set.

For each navigable of firstNamedChildren:

Let name be navigable's target name.

If navigable's active document's origin is same origin with window's relevant settings object's origin, then append name to names.

Return names.

The two seperate iterations mean that in the following example, hosted on https://example.org/, assuming https://elsewhere.example/ sets window.name to "spices", evaluating window.spices after everything has loaded will yield undefined:

<iframe src=https://elsewhere.example.com/></iframe>
<iframe name=spices></iframe>

The Window object supports named properties. The supported property names of a Window object window at any moment consist of the following, in tree order according to the element that contributed them, ignoring later duplicates:

window's document-tree child navigable target name property set;

the value of the name content attribute for all embed, form, img, and object elements that have a non-empty name content attribute and are in a document tree with window's associated Document as their root; and

the value of the id content attribute for all HTML elements that have a non-empty id content attribute and are in a document tree with window's associated Document as their root.

To determine the value of a named property name in a Window object window, the user agent must return the value obtained using the following steps:

Let objects be the list of named objects of window with the name name.

There will be at least one such object, since the algorithm would otherwise not have been invoked by Web IDL.

If objects contains a navigable, then:

Let container be the first navigable container in window's associated Document's descendants whose content navigable is in objects.

Return container's content navigable's active WindowProxy.

Otherwise, if objects has only one element, return that element.

Otherwise, return an HTMLCollection rooted at window's associated Document, whose filter matches only named objects of window with the name name. (By definition, these will all be elements.)

Named objects of Window object window with the name name, for the purposes of the above algorithm, consist of the following:

document-tree child navigables of window's associated Document whose target name is name;

embed, form, img, or object elements that have a name content attribute whose value is name and are in a document tree with window's associated Document as their root; and

HTML elements that have an id content attribute whose value is name and are in a document tree with window's associated Document as their root.

Since the Window interface has the [Global] extended attribute, its named properties follow the rules for named properties objects rather than legacy platform objects.

7.2.2.4 Accessing related windows
window.top
✔MDN

Returns the WindowProxy for the top-level traversable.

window.opener [ = value ]
✔MDN

Returns the WindowProxy for the opener browsing context.

Returns null if there isn't one or if it has been set to null.

Can be set to null.

window.parent
✔MDN

Returns the WindowProxy for the parent navigable.

window.frameElement
✔MDN

Returns the navigable container element.

Returns null if there isn't one, and in cross-origin situations.

The top getter steps are:

If this's navigable is null, then return null.

Return this's navigable's top-level traversable's active WindowProxy.

The opener getter steps are:

Let current be this's browsing context.

If current is null, then return null.

If current's opener browsing context is null, then return null.

Return current's opener browsing context's WindowProxy object.

The opener setter steps are:

If the given value is null and this's browsing context is non-null, then set this's browsing context's opener browsing context to null.

If the given value is non-null, then perform ? DefinePropertyOrThrow(this, "opener", { [[Value]]: the given value, [[Writable]]: true, [[Enumerable]]: true, [[Configurable]]: true }).

Setting window.opener to null clears the opener browsing context reference. In practice, this prevents future scripts from accessing their opener browsing context's Window object.

By default, scripts can access their opener browsing context's Window object through the window.opener getter. E.g., a script can set window.opener.location, causing the opener browsing context to navigate.

The parent getter steps are:

Let navigable be this's navigable.

If navigable is null, then return null.

If navigable's parent is not null, then set navigable to navigable's parent.

Return navigable's active WindowProxy.

The frameElement getter steps are:

Let current be this's node navigable.

If current is null, then return null.

Let container be current's container.

If container is null, then return null.

If container's node document's origin is not same origin-domain with the current settings object's origin, then return null.

Return container.

An example of when these properties can return null is as follows:

<!DOCTYPE html>
<iframe></iframe>

<script>
"use strict";
const element = document.querySelector("iframe");
const iframeWindow = element.contentWindow;
element.remove();

console.assert(iframeWindow.top === null);
console.assert(iframeWindow.parent === null);
console.assert(iframeWindow.frameElement === null);
</script>

Here the browsing context corresponding to iframeWindow was nulled out when element was removed from the document.

7.2.2.5 Historical browser interface element APIs

For historical reasons, the Window interface had some properties that represented the visibility of certain web browser interface elements.

For privacy and interoperability reasons, those properties now return values that represent whether the Window's browsing context's is popup property is true or false.

Each interface element is represented by a BarProp object:

✔MDN
[Exposed=Window]
interface BarProp {
  readonly attribute boolean visible;
};
window.locationbar.visible
✔MDN
window.menubar.visible
✔MDN
window.personalbar.visible
✔MDN
window.scrollbars.visible
✔MDN
window.statusbar.visible
✔MDN
window.toolbar.visible
✔MDN

Returns true if the Window is not a popup; otherwise, returns false.

✔MDN

The visible getter steps are:

Let browsingContext be this's relevant global object's browsing context.

If browsingContext is null, then return true.

Return the negation of browsingContext's top-level browsing context's is popup.

The following BarProp objects must exist for each Window object:

The location bar BarProp object
Historically represented the user interface element that contains a control that displays the browser's location bar.
The menu bar BarProp object
Historically represented the user interface element that contains a list of commands in menu form, or some similar interface concept.
The personal bar BarProp object
Historically represented the user interface element that contains links to the user's favorite pages, or some similar interface concept.
The scrollbar BarProp object
Historically represented the user interface element that contains a scrolling mechanism, or some similar interface concept.
The status bar BarProp object
Historically represented a user interface element found immediately below or after the document, as appropriate for the user's media, which typically provides information about ongoing network activity or information about elements that the user's pointing device is currently indicating.
The toolbar BarProp object
Historically represented the user interface element found immediately above or before the document, as appropriate for the user's media, which typically provides session history traversal controls (back and forward buttons, reload buttons, etc.).

The locationbar attribute must return the location bar BarProp object.

The menubar attribute must return the menu bar BarProp object.

The personalbar attribute must return the personal bar BarProp object.

The scrollbars attribute must return the scrollbar BarProp object.

The statusbar attribute must return the status bar BarProp object.

The toolbar attribute must return the toolbar BarProp object.

For historical reasons, the status attribute on the Window object must, on getting, return the last string it was set to, and on setting, must set itself to the new value. When the Window object is created, the attribute must be set to the empty string. It does not do anything else.

7.2.2.6 Script settings for Window objects

To set up a window environment settings object, given a URL creationURL, a JavaScript execution context execution context, null or an environment reservedEnvironment, a URL topLevelCreationURL, and an origin topLevelOrigin, run these steps:

Let realm be the value of execution context's Realm component.

Let window be realm's global object.

Let settings object be a new environment settings object whose algorithms are defined as follows:

The realm execution context

Return execution context.

The module map

Return the module map of window's associated Document.

The API base URL

Return the current base URL of window's associated Document.

The origin

Return the origin of window's associated Document.

The has cross-site ancestor

If window's navigable's parent is null, then return false.

Let parentDocument be window's navigable's parent's active document.

If parentDocument's relevant settings object's has cross-site ancestor is true, then return true.

If parentDocument's origin is not same site with window's associated Document's origin, then return true.

Return false.

The policy container

Return the policy container of window's associated Document.

The cross-origin isolated capability

Return true if both of the following hold, and false otherwise:

realm's agent cluster's cross-origin-isolation mode is "concrete", and

window's associated Document is allowed to use the "cross-origin-isolated" feature.

The time origin

Return window's associated Document's load timing info's navigation start time.

If reservedEnvironment is non-null, then:

Set settings object's id to reservedEnvironment's id, target browsing context to reservedEnvironment's target browsing context, and active service worker to reservedEnvironment's active service worker.

Set reservedEnvironment's id to the empty string.

The identity of the reserved environment is considered to be fully transferred to the created environment settings object. The reserved environment is not searchable by the environment’s id from this point on.

Otherwise, set settings object's id to a new unique opaque string, settings object's target browsing context to null, and settings object's active service worker to null.

Set settings object's creation URL to creationURL, settings object's top-level creation URL to topLevelCreationURL, and settings object's top-level origin to topLevelOrigin.

Set realm's [[HostDefined]] field to settings object.

7.2.3 The WindowProxy exotic object

A WindowProxy is an exotic object that wraps a Window ordinary object, indirecting most operations through to the wrapped object. Each browsing context has an associated WindowProxy object. When the browsing context is navigated, the Window object wrapped by the browsing context's associated WindowProxy object is changed.

The WindowProxy exotic object must use the ordinary internal methods except where it is explicitly specified otherwise below.

There is no WindowProxy interface object.

Every WindowProxy object has a [[Window]] internal slot representing the wrapped Window object.

Although WindowProxy is named as a "proxy", it does not do polymorphic dispatch on its target's internal methods as a real proxy would, due to a desire to reuse machinery between WindowProxy and Location objects. As long as the Window object remains an ordinary object this is unobservable and can be implemented either way.

7.2.3.1 [[GetPrototypeOf]] ( )

Let W be the value of the [[Window]] internal slot of this.

If IsPlatformObjectSameOrigin(W) is true, then return ! OrdinaryGetPrototypeOf(W).

Return null.

7.2.3.2 [[SetPrototypeOf]] ( V )

Return ! SetImmutablePrototype(this, V).

7.2.3.3 [[IsExtensible]] ( )

Return true.

7.2.3.4 [[PreventExtensions]] ( )

Return false.

7.2.3.5 [[GetOwnProperty]] ( P )

Let W be the value of the [[Window]] internal slot of this.

If P is an array index property name, then:

Let index be ! ToUint32(P).

Let children be the document-tree child navigables of W's associated Document.

Let value be undefined.

If index is less than children's size, then:

Sort children in ascending order, with navigableA being less than navigableB if navigableA's container was inserted into W's associated Document earlier than navigableB's container was.

Set value to children[index]'s active WindowProxy.

If value is undefined, then:

If IsPlatformObjectSameOrigin(W) is true, then return undefined.

Throw a "SecurityError" DOMException.

Return PropertyDescriptor { [[Value]]: value, [[Writable]]: false, [[Enumerable]]: true, [[Configurable]]: true }.

If IsPlatformObjectSameOrigin(W) is true, then return ! OrdinaryGetOwnProperty(W, P).

This is a willful violation of the JavaScript specification's invariants of the essential internal methods to maintain compatibility with existing web content. See tc39/ecma262 issue #672 for more information. [JAVASCRIPT]

Let property be CrossOriginGetOwnPropertyHelper(W, P).

If property is not undefined, then return property.

If property is undefined and P is in W's document-tree child navigable target name property set, then:

Let value be the active WindowProxy of the named object of W with the name P.

Return PropertyDescriptor { [[Value]]: value, [[Enumerable]]: false, [[Writable]]: false, [[Configurable]]: true }.

The reason the property descriptors are non-enumerable, despite this mismatching the same-origin behavior, is for compatibility with existing web content. See issue #3183 for details.

Return ? CrossOriginPropertyFallback(P).

7.2.3.6 [[DefineOwnProperty]] ( P, Desc )

Let W be the value of the [[Window]] internal slot of this.

If IsPlatformObjectSameOrigin(W) is true, then:

If P is an array index property name, return false.

Return ? OrdinaryDefineOwnProperty(W, P, Desc).

This is a willful violation of the JavaScript specification's invariants of the essential internal methods to maintain compatibility with existing web content. See tc39/ecma262 issue #672 for more information. [JAVASCRIPT]

Throw a "SecurityError" DOMException.

7.2.3.7 [[Get]] ( P, Receiver )

Let W be the value of the [[Window]] internal slot of this.

Check if an access between two browsing contexts should be reported, given the current global object's browsing context, W's browsing context, P, and the current settings object.

If IsPlatformObjectSameOrigin(W) is true, then return ? OrdinaryGet(this, P, Receiver).

Return ? CrossOriginGet(this, P, Receiver).

this is passed rather than W as OrdinaryGet and CrossOriginGet will invoke the [[GetOwnProperty]] internal method.

7.2.3.8 [[Set]] ( P, V, Receiver )

Let W be the value of the [[Window]] internal slot of this.

Check if an access between two browsing contexts should be reported, given the current global object's browsing context, W's browsing context, P, and the current settings object.

If IsPlatformObjectSameOrigin(W) is true, then:

If P is an array index property name, then return false.

Return ? OrdinarySet(W, P, V, Receiver).

Return ? CrossOriginSet(this, P, V, Receiver).

this is passed rather than W as CrossOriginSet will invoke the [[GetOwnProperty]] internal method.

7.2.3.9 [[Delete]] ( P )

Let W be the value of the [[Window]] internal slot of this.

If IsPlatformObjectSameOrigin(W) is true, then:

If P is an array index property name, then:

Let desc be ! this.[[GetOwnProperty]](P).

If desc is undefined, then return true.

Return false.

Return ? OrdinaryDelete(W, P).

Throw a "SecurityError" DOMException.

7.2.3.10 [[OwnPropertyKeys]] ( )

Let W be the value of the [[Window]] internal slot of this.

Let maxProperties be W's associated Document's document-tree child navigables's size.

Let keys be the range 0 to maxProperties, exclusive.

If IsPlatformObjectSameOrigin(W) is true, then return the concatenation of keys and OrdinaryOwnPropertyKeys(W).

Return the concatenation of keys and ! CrossOriginOwnPropertyKeys(W).

7.2.4 The Location interface
✔MDN

Each Window object is associated with a unique instance of a Location object, allocated when the Window object is created.

The Location exotic object is defined through a mishmash of IDL, invocation of JavaScript internal methods post-creation, and overridden JavaScript internal methods. Coupled with its scary security policy, please take extra care while implementing this excrescence.

To create a Location object, run these steps:

Let location be a new Location platform object.

Let valueOf be location's relevant realm.[[Intrinsics]].[[%Object.prototype.valueOf%]].

Perform ! location.[[DefineOwnProperty]]("valueOf", { [[Value]]: valueOf, [[Writable]]: false, [[Enumerable]]: false, [[Configurable]]: false }).

Perform ! location.[[DefineOwnProperty]](%Symbol.toPrimitive%, { [[Value]]: undefined, [[Writable]]: false, [[Enumerable]]: false, [[Configurable]]: false }).

Set the value of the [[DefaultProperties]] internal slot of location to location.[[OwnPropertyKeys]]().

Return location.

The addition of valueOf and %Symbol.toPrimitive% own data properties, as well as the fact that all of Location's IDL attributes are marked [LegacyUnforgeable], is required by legacy code that consulted the Location interface, or stringified it, to determine the document URL, and then used it in a security-sensitive way. In particular, the valueOf, %Symbol.toPrimitive%, and [LegacyUnforgeable] stringifier mitigations ensure that code such as foo[location] = bar or location + "" cannot be misdirected.

document.location [ = value ]
window.location [ = value ]

Returns a Location object with the current page's location.

Can be set, to navigate to another page.

The Document object's location getter steps are to return this's relevant global object's Location object, if this is fully active, and null otherwise.

The Window object's location getter steps are to return this's Location object.

Location objects provide a representation of the URL of their associated Document, as well as methods for navigating and reloading the associated navigable.

[Exposed=Window]
interface Location { // but see also additional creation steps and overridden internal methods
  [LegacyUnforgeable] stringifier attribute USVString href;
  [LegacyUnforgeable] readonly attribute USVString origin;
  [LegacyUnforgeable] attribute USVString protocol;
  [LegacyUnforgeable] attribute USVString host;
  [LegacyUnforgeable] attribute USVString hostname;
  [LegacyUnforgeable] attribute USVString port;
  [LegacyUnforgeable] attribute USVString pathname;
  [LegacyUnforgeable] attribute USVString search;
  [LegacyUnforgeable] attribute USVString hash;

  [LegacyUnforgeable] undefined assign(USVString url);
  [LegacyUnforgeable] undefined replace(USVString url);
  [LegacyUnforgeable] undefined reload();

  [LegacyUnforgeable] readonly attribute DOMStringList ancestorOrigins;
};
location.toString()
location.href
✔MDN

Returns the Location object's URL.

Can be set, to navigate to the given URL.

location.origin
✔MDN

Returns the Location object's URL's origin.

location.protocol
✔MDN

Returns the Location object's URL's scheme.

Can be set, to navigate to the same URL with a changed scheme.

location.host
✔MDN

Returns the Location object's URL's host and port (if different from the default port for the scheme).

Can be set, to navigate to the same URL with a changed host and port.

location.hostname
✔MDN

Returns the Location object's URL's host.

Can be set, to navigate to the same URL with a changed host.

location.port
✔MDN

Returns the Location object's URL's port.

Can be set, to navigate to the same URL with a changed port.

location.pathname
✔MDN

Returns the Location object's URL's path.

Can be set, to navigate to the same URL with a changed path.

location.search
✔MDN

Returns the Location object's URL's query (includes leading "?" if non-empty).

Can be set, to navigate to the same URL with a changed query (ignores leading "?").

location.hash
✔MDN

Returns the Location object's URL's fragment (includes leading "#" if non-empty).

Can be set, to navigate to the same URL with a changed fragment (ignores leading "#").

location.assign(url)
✔MDN

Navigates to the given URL.

location.replace(url)
✔MDN

Removes the current page from the session history and navigates to the given URL.

location.reload()
✔MDN

Reloads the current page.

location.ancestorOrigins
MDN

Returns a DOMStringList object listing the origins of the ancestor navigables' active documents.

A Location object has an associated relevant Document, which is its relevant global object's browsing context's active document, if this Location object's relevant global object's browsing context is non-null, and null otherwise.

A Location object has an associated url, which is this Location object's relevant Document's URL, if this Location object's relevant Document is non-null, and about:blank otherwise.

To Location-object navigate a Location object location to a URL url, optionally given a NavigationHistoryBehavior historyHandling (default "auto"):

Let navigable be location's relevant global object's navigable.

Let sourceDocument be the incumbent global object's associated Document.

If location's relevant Document is not yet completely loaded, and the incumbent global object does not have transient activation, then set historyHandling to "replace".

Navigate navigable to url using sourceDocument, with exceptionsEnabled set to true and historyHandling set to historyHandling.

The href getter steps are:

If this's relevant Document is non-null and its origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Return this's url, serialized.

The href setter steps are:

If this's relevant Document is null, then return.

Let url be the result of encoding-parsing a URL given the given value, relative to the entry settings object.

If url is failure, then throw a "SyntaxError" DOMException.

Location-object navigate this to url.

The href setter intentionally has no security check.

The origin getter steps are:

If this's relevant Document is non-null and its origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Return the serialization of this's url's origin.

The protocol getter steps are:

If this's relevant Document is non-null and its origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Return this's url's scheme, followed by ":".

The protocol setter steps are:

If this's relevant Document is null, then return.

If this's relevant Document's origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Let copyURL be a copy of this's url.

Let possibleFailure be the result of basic URL parsing the given value, followed by ":", with copyURL as url and scheme start state as state override.

Because the URL parser ignores multiple consecutive colons, providing a value of "https:" (or even "https::::") is the same as providing a value of "https".

If possibleFailure is failure, then throw a "SyntaxError" DOMException.

If copyURL's scheme is not an HTTP(S) scheme, then terminate these steps.

Location-object navigate this to copyURL.

The host getter steps are:

If this's relevant Document is non-null and its origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Let url be this's url.

If url's host is null, return the empty string.

If url's port is null, return url's host, serialized.

Return url's host, serialized, followed by ":" and url's port, serialized.

The host setter steps are:

If this's relevant Document is null, then return.

If this's relevant Document's origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Let copyURL be a copy of this's url.

If copyURL has an opaque path, then return.

Basic URL parse the given value, with copyURL as url and host state as state override.

Location-object navigate this to copyURL.

The hostname getter steps are:

If this's relevant Document is non-null and its origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

If this's url's host is null, return the empty string.

Return this's url's host, serialized.

The hostname setter steps are:

If this's relevant Document is null, then return.

If this's relevant Document's origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Let copyURL be a copy of this's url.

If copyURL has an opaque path, then return.

Basic URL parse the given value, with copyURL as url and hostname state as state override.

Location-object navigate this to copyURL.

The port getter steps are:

If this's relevant Document is non-null and its origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

If this's url's port is null, return the empty string.

Return this's url's port, serialized.

The port setter steps are:

If this's relevant Document is null, then return.

If this's relevant Document's origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Let copyURL be a copy of this's url.

If copyURL cannot have a username/password/port, then return.

If the given value is the empty string, then set copyURL's port to null.

Otherwise, basic URL parse the given value, with copyURL as url and port state as state override.

Location-object navigate this to copyURL.

The pathname getter steps are:

If this's relevant Document is non-null and its origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Return the result of URL path serializing this Location object's url.

The pathname setter steps are:

If this's relevant Document is null, then return.

If this's relevant Document's origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Let copyURL be a copy of this's url.

If copyURL has an opaque path, then return.

Set copyURL's path to the empty list.

Basic URL parse the given value, with copyURL as url and path start state as state override.

Location-object navigate this to copyURL.

The search getter steps are:

If this's relevant Document is non-null and its origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

If this's url's query is either null or the empty string, return the empty string.

Return "?", followed by this's url's query.

The search setter steps are:

If this's relevant Document is null, then return.

If this's relevant Document's origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Let copyURL be a copy of this's url.

If the given value is the empty string, set copyURL's query to null.

Otherwise, run these substeps:

Let input be the given value with a single leading "?" removed, if any.

Set copyURL's query to the empty string.

Basic URL parse input, with null, the relevant Document's document's character encoding, copyURL as url, and query state as state override.

Location-object navigate this to copyURL.

The hash getter steps are:

If this's relevant Document is non-null and its origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

If this's url's fragment is either null or the empty string, return the empty string.

Return "#", followed by this's url's fragment.

The hash setter steps are:

If this's relevant Document is null, then return.

If this's relevant Document's origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Let copyURL be a copy of this's url.

Let thisURLFragment be copyURL's fragment if it is non-null; otherwise the empty string.

Let input be the given value with a single leading "#" removed, if any.

Set copyURL's fragment to the empty string.

Basic URL parse input, with copyURL as url and fragment state as state override.

If copyURL's fragment is thisURLFragment, then return.

This bailout is necessary for compatibility with deployed content, which redundantly sets location.hash on scroll. It does not apply to other mechanisms of fragment navigation, such as the location.href setter or location.assign().

Location-object navigate this to copyURL.

Unlike the equivalent API for the a and area elements, the hash setter does not special case the empty string, to remain compatible with deployed scripts.

The assign(url) method steps are:

If this's relevant Document is null, then return.

If this's relevant Document's origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Let urlRecord be the result of encoding-parsing a URL given url, relative to the entry settings object.

If urlRecord is failure, then throw a "SyntaxError" DOMException.

Location-object navigate this to urlRecord.

The replace(url) method steps are:

If this's relevant Document is null, then return.

Let urlRecord be the result of encoding-parsing a URL given url, relative to the entry settings object.

If urlRecord is failure, then throw a "SyntaxError" DOMException.

Location-object navigate this to urlRecord given "replace".

The replace() method intentionally has no security check.

The reload() method steps are:

Let document be this's relevant Document.

If document is null, then return.

If document's origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Reload document's node navigable.

A Location object has an associated empty DOMStringList which is a DOMStringList object whose associated list is an empty list.

This object cannot carry state across navigations because it is only returned when there is no relevant Document, in which case it's not possible to navigate, and it's not possible to return to a non-null relevant Document.

The ancestorOrigins getter steps are:

If this's relevant Document is null, then return this's empty DOMStringList.

If this's relevant Document's origin is not same origin-domain with the entry settings object's origin, then throw a "SecurityError" DOMException.

Assert: this's relevant Document's ancestor origins list is not null.

Otherwise, return this's relevant Document's ancestor origins list.

As explained earlier, the Location exotic object requires additional logic beyond IDL for security purposes. The Location object must use the ordinary internal methods except where it is explicitly specified otherwise below.

Also, every Location object has a [[DefaultProperties]] internal slot representing its own properties at time of its creation.

7.2.4.1 [[GetPrototypeOf]] ( )

If IsPlatformObjectSameOrigin(this) is true, then return ! OrdinaryGetPrototypeOf(this).

Return null.

7.2.4.2 [[SetPrototypeOf]] ( V )

Return ! SetImmutablePrototype(this, V).

7.2.4.3 [[IsExtensible]] ( )

Return true.

7.2.4.4 [[PreventExtensions]] ( )

Return false.

7.2.4.5 [[GetOwnProperty]] ( P )

If IsPlatformObjectSameOrigin(this) is true, then:

Let desc be OrdinaryGetOwnProperty(this, P).

If the value of the [[DefaultProperties]] internal slot of this contains P, then set desc.[[Configurable]] to true.

Return desc.

Let property be CrossOriginGetOwnPropertyHelper(this, P).

If property is not undefined, then return property.

Return ? CrossOriginPropertyFallback(P).

7.2.4.6 [[DefineOwnProperty]] ( P, Desc )

If IsPlatformObjectSameOrigin(this) is true, then:

If the value of the [[DefaultProperties]] internal slot of this contains P, then return false.

Return ? OrdinaryDefineOwnProperty(this, P, Desc).

Throw a "SecurityError" DOMException.

7.2.4.7 [[Get]] ( P, Receiver )

If IsPlatformObjectSameOrigin(this) is true, then return ? OrdinaryGet(this, P, Receiver).

Return ? CrossOriginGet(this, P, Receiver).

7.2.4.8 [[Set]] ( P, V, Receiver )

If IsPlatformObjectSameOrigin(this) is true, then return ? OrdinarySet(this, P, V, Receiver).

Return ? CrossOriginSet(this, P, V, Receiver).

7.2.4.9 [[Delete]] ( P )

If IsPlatformObjectSameOrigin(this) is true, then return ? OrdinaryDelete(this, P).

Throw a "SecurityError" DOMException.

7.2.4.10 [[OwnPropertyKeys]] ( )

If IsPlatformObjectSameOrigin(this) is true, then return OrdinaryOwnPropertyKeys(this).

Return CrossOriginOwnPropertyKeys(this).

7.2.5 The History interface
✔MDN
enum ScrollRestoration { "auto", "manual" };

[Exposed=Window]
interface History {
  readonly attribute unsigned long length;
  attribute ScrollRestoration scrollRestoration;
  readonly attribute any state;
  undefined go(optional long delta = 0);
  undefined back();
  undefined forward();
  undefined pushState(any data, DOMString unused, optional USVString? url = null);
  undefined replaceState(any data, DOMString unused, optional USVString? url = null);
};
history.length
✔MDN

Returns the number of overall session history entries for the current traversable navigable.

history.scrollRestoration
✔MDN

Returns the scroll restoration mode of the active session history entry.

history.scrollRestoration = value

Set the scroll restoration mode of the active session history entry to value.

history.state
✔MDN

Returns the classic history API state of the active session history entry, deserialized into a JavaScript value.

history.go()

Reloads the current page.

history.go(delta)
✔MDN

Goes back or forward the specified number of steps in the overall session history entries list for the current traversable navigable.

A zero delta will reload the current page.

If the delta is out of range, does nothing.

history.back()
✔MDN

Goes back one step in the overall session history entries list for the current traversable navigable.

If there is no previous page, does nothing.

history.forward()
✔MDN

Goes forward one step in the overall session history entries list for the current traversable navigable.

If there is no next page, does nothing.

history.pushState(data, "")
✔MDN

Adds a new entry into session history with its classic history API state set to a serialization of data. The active history entry's URL will be copied over and used for the new entry's URL.

(The second parameter exists for historical reasons, and cannot be omitted; passing the empty string is traditional.)

history.pushState(data, "", url)

Adds a new entry into session history with its classic history API state set to a serialization of data, and with its URL set to url.

If the current Document cannot have its URL rewritten to url, a "SecurityError" DOMException will be thrown.

(The second parameter exists for historical reasons, and cannot be omitted; passing the empty string is traditional.)

history.replaceState(data, "")
✔MDN

Updates the classic history API state of the active session history entry to a structured clone of data.

(The second parameter exists for historical reasons, and cannot be omitted; passing the empty string is traditional.)

history.replaceState(data, "", url)

Updates the classic history API state of the active session history entry to a structured clone of data, and its URL to url.

If the current Document cannot have its URL rewritten to url, a "SecurityError" DOMException will be thrown.

(The second parameter exists for historical reasons, and cannot be omitted; passing the empty string is traditional.)

A Document has a history object, a History object.

The history getter steps are to return this's associated Document's history object.

Each History object has state, initially null.

Each History object has a length, a non-negative integer, initially 0.

Each History object has an index, a non-negative integer, initially 0.

Although the index is not directly exposed, it can be inferred from changes to the length during synchronous navigations. In fact, that is what it's used for.

The length getter steps are:

If this's relevant global object's associated Document is not fully active, then throw a "SecurityError" DOMException.

Return this's length.

The scrollRestoration getter steps are:

If this's relevant global object's associated Document is not fully active, then throw a "SecurityError" DOMException.

Return this's relevant global object's navigable's active session history entry's scroll restoration mode.

The scrollRestoration setter steps are:

If this's relevant global object's associated Document is not fully active, then throw a "SecurityError" DOMException.

Set this's relevant global object's navigable's active session history entry's scroll restoration mode to the given value.

The state getter steps are:

If this's relevant global object's associated Document is not fully active, then throw a "SecurityError" DOMException.

Return this's state.

The go(delta) method steps are to delta traverse this given delta.

The back() method steps are to delta traverse this given −1.

The forward() method steps are to delta traverse this given +1.

To delta traverse a History object history given an integer delta:

Let document be history's relevant global object's associated Document.

If document is not fully active, then throw a "SecurityError" DOMException.

If delta is 0, then reload document's node navigable, and return.

Traverse the history by a delta given document's node navigable's traversable navigable, delta, and with sourceDocument set to document.

The pushState(data, unused, url) method steps are to run the shared history push/replace state steps given this, data, url, and "push".

The replaceState(data, unused, url) method steps are to run the shared history push/replace state steps given this, data, url, and "replace".

The shared history push/replace state steps, given a History history, a value data, a scalar value string-or-null url, and a history handling behavior historyHandling, are:

Let document be history's relevant global object's associated Document.

If document is not fully active, then throw a "SecurityError" DOMException.

Optionally, throw a "SecurityError" DOMException. (For example, the user agent might disallow calls to these methods that are invoked on a timer, or from event listeners that are not triggered in response to a clear user action, or that are invoked in rapid succession.)

Let serializedData be StructuredSerializeForStorage(data). Rethrow any exceptions.

Let newURL be document's URL.

If url is not null or the empty string, then:

Set newURL to the result of encoding-parsing a URL given url, relative to the relevant settings object of history.

If newURL is failure, then throw a "SecurityError" DOMException.

If document cannot have its URL rewritten to newURL, then throw a "SecurityError" DOMException.

The special case for the empty string here is historical, and leads to different resulting URLs when comparing code such as location.href = "" (which performs URL parsing on the empty string) versus history.pushState(null, "", "") (which bypasses it).

Let navigation be history's relevant global object's navigation API.

Let continue be the result of firing a push/replace/reload navigate event at navigation with navigationType set to historyHandling, isSameDocument set to true, destinationURL set to newURL, and classicHistoryAPIState set to serializedData.

If continue is false, then return.

Run the URL and history update steps given document and newURL, with serializedData set to serializedData and historyHandling set to historyHandling.

User agents may limit the number of state objects added to the session history per page. If a page hits the implementation-defined limit, user agents must remove the entry immediately after the first entry for that Document object in the session history after having added the new entry. (Thus the state history acts as a FIFO buffer for eviction, but as a LIFO buffer for navigation.)

A Document document can have its URL rewritten to a URL targetURL if the following algorithm returns true:

Let documentURL be document's URL.

If targetURL and documentURL differ in their scheme, username, password, host, or port components, then return false.

If targetURL's scheme is an HTTP(S) scheme, then return true.

Differences in path, query, and fragment are allowed for http: and https: URLs.

If targetURL's scheme is "file", then:

If targetURL and documentURL differ in their path component, then return false.

Return true.

Differences in query and fragment are allowed for file: URLs.

If targetURL and documentURL differ in their path component or query components, then return false.

Only differences in fragment are allowed for other types of URLs.

Return true.

document's URL	targetURL	can have its URL rewritten
https://example.com/home	https://example.com/home#about	✅
https://example.com/home	https://example.com/home?page=shop	✅
https://example.com/home	https://example.com/shop	✅
https://example.com/home	https://user:pass@example.com/home	❌
https://example.com/home	http://example.com/home	❌
file:///path/to/x	file:///path/to/x#hash	✅
file:///path/to/x	file:///path/to/x?search	✅
file:///path/to/x	file:///path/to/y	❌
about:blank	about:blank#hash	✅
about:blank	about:blank?search	❌
about:blank	about:srcdoc	❌
data:text/html,foo	data:text/html,foo#hash	✅
data:text/html,foo	data:text/html,foo?search	❌
data:text/html,foo	data:text/html,bar	❌
data:text/html,foo	data:bar	❌
blob:https://example.com/77becafe-657b-4fdc-8bd3-e83aaa5e8f43	blob:https://example.com/77becafe-657b-4fdc-8bd3-e83aaa5e8f43#hash	✅
blob:https://example.com/77becafe-657b-4fdc-8bd3-e83aaa5e8f43	blob:https://example.com/77becafe-657b-4fdc-8bd3-e83aaa5e8f43?search	❌
blob:https://example.com/77becafe-657b-4fdc-8bd3-e83aaa5e8f43	blob:https://example.com/anything	❌
blob:https://example.com/77becafe-657b-4fdc-8bd3-e83aaa5e8f43	blob:path	❌

Note how only the URL of the Document matters, and not its origin. They can mismatch in cases like about:blank Documents with inherited origins, in sandboxed iframes, or when the document.domain setter has been used.

Consider a game where the user can navigate along a line, such that the user is always at some coordinate, and such that the user can bookmark the page corresponding to a particular coordinate, to return to it later.

A static page implementing the x=5 position in such a game could look like the following:

<!DOCTYPE HTML>
<!-- this is https://example.com/line?x=5 -->
<html lang="en">
<title>Line Game - 5</title>
<p>You are at coordinate 5 on the line.</p>
<p>
 <a href="?x=6">Advance to 6</a> or
 <a href="?x=4">retreat to 4</a>?
</p>

The problem with such a system is that each time the user clicks, the whole page has to be reloaded. Here instead is another way of doing it, using script:

<!DOCTYPE HTML>
<!-- this starts off as https://example.com/line?x=5 -->
<html lang="en">
<title>Line Game - 5</title>
<p>You are at coordinate <span id="coord">5</span> on the line.</p>
<p>
 <a href="?x=6" onclick="go(1); return false;">Advance to 6</a> or
 <a href="?x=4" onclick="go(-1); return false;">retreat to 4</a>?
</p>
<script>
 var currentPage = 5; // prefilled by server
 function go(d) {
   setupPage(currentPage + d);
   history.pushState(currentPage, "", '?x=' + currentPage);
 }
 onpopstate = function(event) {
   setupPage(event.state);
 }
 function setupPage(page) {
   currentPage = page;
   document.title = 'Line Game - ' + currentPage;
   document.getElementById('coord').textContent = currentPage;
   document.links[0].href = '?x=' + (currentPage+1);
   document.links[0].textContent = 'Advance to ' + (currentPage+1);
   document.links[1].href = '?x=' + (currentPage-1);
   document.links[1].textContent = 'retreat to ' + (currentPage-1);
 }
</script>

In systems without script, this still works like the previous example. However, users that do have script support can now navigate much faster, since there is no network access for the same experience. Furthermore, contrary to the experience the user would have with just a naïve script-based approach, bookmarking and navigating the session history still work.

In the example above, the data argument to the pushState() method is the same information as would be sent to the server, but in a more convenient form, so that the script doesn't have to parse the URL each time the user navigates.

Most applications want to use the same scroll restoration mode value for all of their history entries. To achieve this they can set the scrollRestoration attribute as soon as possible (e.g., in the first script element in the document's head element) to ensure that any entry added to the history session gets the desired scroll restoration mode.

<head>
  <script>
       if ('scrollRestoration' in history)
            history.scrollRestoration = 'manual';
  </script>
</head>
   
7.2.6 The navigation API
7.2.6.1 Introduction

This section is non-normative.

The navigation API, provided by the global navigation property, provides a modern and web application-focused way of managing navigations and history entries. It is a successor to the classic location and history APIs.

One ability the API provides is inspecting session history entries. For example, the following will display the entries' URLs in an ordered list:

const ol = document.createElement("ol");
ol.start = 0; // so that the list items' ordinal values match up with the entry indices

for (const entry of navigation.entries()) {
  const li = document.createElement("li");

  if (entry.index < navigation.currentEntry.index) {
    li.className = "backward";
  } else if (entry.index > navigation.currentEntry.index) {
    li.className = "forward";
  } else {
    li.className = "current";
  }

  li.textContent = entry.url;
  ol.append(li);
}

The navigation.entries() array contains NavigationHistoryEntry instances, which have other useful properties in addition to the url and index properties shown here. Note that the array only contains NavigationHistoryEntry objects that represent the current navigable, and thus its contents are not impacted by navigations inside navigable containers such as iframes, or by navigations of the parent navigable in cases where the navigation API is itself being used inside an iframe. Additionally, it only contains NavigationHistoryEntry objects representing same-origin session history entries, meaning that if the user has visited other origins before or after the current one, there will not be corresponding NavigationHistoryEntrys.

The navigation API can also be used to navigate, reload, or traverse through the history:

<button onclick="navigation.reload()">Reload</button>

<input type="url" id="navigationURL">
<button onclick="navigation.navigate(navigationURL.value)">Navigate</button>

<button id="backButton" onclick="navigation.back()">Back</button>
<button id="forwardButton" onclick="navigation.forward()">Forward</button>

<select id="traversalDestinations"></select>
<button id="goButton" onclick="navigation.traverseTo(traversalDestinations.value)">Traverse To</button>

<script>
backButton.disabled = !navigation.canGoBack;
forwardButton.disabled = !navigation.canGoForward;

for (const entry of navigation.entries()) {
  traversalDestinations.append(new Option(entry.url, entry.key));
}
</script>

Note that traversals are again limited to same-origin destinations, meaning that, for example, navigation.canGoBack will be false if the previous session history entry is for a page from another origin.

The most powerful part of the navigation API is the navigate event, which fires whenever almost any navigation or traversal occurs in the current navigable:

navigation.onnavigate = event => {
  console.log(event.navigationType); // "push", "replace", "reload", or "traverse"
  console.log(event.destination.url);
  console.log(event.userInitiated);
  // ... and other useful properties
};

(The event will not fire for location bar-initiated navigations, or navigations initiated from other windows, when the destination of the navigation is a new document.)

Much of the time, the event's cancelable property will be true, meaning this event can be canceled using preventDefault():

navigation.onnavigate = event => {
  if (event.cancelable && isDisallowedURL(event.destination.url)) {
    alert(`Please don't go to ${event.destination.url}!`);
    event.preventDefault();
  }
};


The cancelable property will be false for some "traverse" navigations, such as those taking place inside child navigables, those crossing to new origins, or when the user attempts to traverse again shortly after a previous call to preventDefault() prevented them from doing so.

The NavigateEvent's intercept() method allows intercepting a navigation and converting it into a same-document navigation:

navigation.addEventListener("navigate", e => {
  // Some navigations, e.g. cross-origin navigations, we cannot intercept.
  // Let the browser handle those normally.
  if (!e.canIntercept) {
    return;
  }

  // Similarly, don't intercept fragment navigations or downloads.
  if (e.hashChange || e.downloadRequest !== null) {
    return;
  }

  const url = new URL(event.destination.url);

  if (url.pathname.startsWith("/articles/")) {
    e.intercept({
      async handler() {
        // The URL has already changed, so show a placeholder while
        // fetching the new content, such as a spinner or loading page.
        renderArticlePagePlaceholder();

        // Fetch the new content and display when ready.
        const articleContent = await getArticleContent(url.pathname, { signal: e.signal });
        renderArticlePage(articleContent);
      }
    });
  }
});

Note that the handler function can return a promise to represent the asynchronous progress, and success or failure, of the navigation. While the promise is still pending, browser UI can treat the navigation as ongoing (e.g., by presenting a loading spinner). Other parts of the navigation API are also sensitive to these promises, such as the return value of navigation.navigate():

const { committed, finished } = await navigation.navigate("/articles/the-navigation-api-is-cool");

// The committed promise will fulfill once the URL has changed, which happens
// immediately (as long as the NavigateEvent wasn't canceled).
await committed;

// The finished promise will fulfill once the Promise returned by handler() has
// fulfilled, which happens once the article is downloaded and rendered. (Or,
// it will reject, if handler() fails along the way).
await finished;
7.2.6.2 The Navigation interface
[Exposed=Window]
interface Navigation : EventTarget {
  sequence<NavigationHistoryEntry> entries();
  readonly attribute NavigationHistoryEntry? currentEntry;
  undefined updateCurrentEntry(NavigationUpdateCurrentEntryOptions options);
  readonly attribute NavigationTransition? transition;
  readonly attribute NavigationActivation? activation;

  readonly attribute boolean canGoBack;
  readonly attribute boolean canGoForward;

  NavigationResult navigate(USVString url, optional NavigationNavigateOptions options = {});
  NavigationResult reload(optional NavigationReloadOptions options = {});

  NavigationResult traverseTo(DOMString key, optional NavigationOptions options = {});
  NavigationResult back(optional NavigationOptions options = {});
  NavigationResult forward(optional NavigationOptions options = {});

  attribute EventHandler onnavigate;
  attribute EventHandler onnavigatesuccess;
  attribute EventHandler onnavigateerror;
  attribute EventHandler oncurrententrychange;
};

dictionary NavigationUpdateCurrentEntryOptions {
  required any state;
};

dictionary NavigationOptions {
  any info;
};

dictionary NavigationNavigateOptions : NavigationOptions {
  any state;
  NavigationHistoryBehavior history = "auto";
};

dictionary NavigationReloadOptions : NavigationOptions {
  any state;
};

dictionary NavigationResult {
  Promise<NavigationHistoryEntry> committed;
  Promise<NavigationHistoryEntry> finished;
};

enum NavigationHistoryBehavior {
  "auto",
  "push",
  "replace"
};

Each Window has an associated navigation API, which is a Navigation object. Upon creation of the Window object, its navigation API must be set to a new Navigation object created in the Window object's relevant realm.

The navigation getter steps are to return this's navigation API.

The following are the event handlers (and their corresponding event handler event types) that must be supported, as event handler IDL attributes, by all objects implementing the Navigation interface:

Event handler	Event handler event type
onnavigate	navigate
onnavigatesuccess	navigatesuccess
onnavigateerror	navigateerror
oncurrententrychange	currententrychange
7.2.6.3 Core infrastructure

Each Navigation has an associated entry list, a list of NavigationHistoryEntry objects, initially empty.

Each Navigation has an associated current entry index, an integer, initially −1.

The current entry of a Navigation navigation is the result of running the following steps:

If navigation has entries and events disabled, then return null.

Assert: navigation's current entry index is not −1.

Return navigation's entry list[navigation's current entry index].

A Navigation navigation has entries and events disabled if the following steps return true:

Let document be navigation's relevant global object's associated Document.

If document is not fully active, then return true.

If document's is initial about:blank is true, then return true.

If document's origin is opaque, then return true.

Return false.

To get the navigation API entry index of a session history entry she within a Navigation navigation:

Let index be 0.

For each nhe of navigation's entry list:

If nhe's session history entry is equal to she, then return index.

Increment index by 1.

Return −1.

A key type used throughout the navigation API is the NavigationType enumeration:

enum NavigationType {
 "push",
 "replace",
 "reload",
 "traverse"
};

This captures the main web developer-visible types of "navigations", which (as noted elsewhere) do not exactly correspond to this standard's singular navigate algorithm. The meaning of each value is the following:

"push"
Corresponds to calls to navigate where the history handling behavior ends up as "push", or to history.pushState().
"replace"
Corresponds to calls to navigate where the history handling behavior ends up as "replace", or to history.replaceState().
"reload"
Corresponds to calls to reload.
"traverse"
Corresponds to calls to traverse the history by a delta.

The value space of the NavigationType enumeration is a superset of the value space of the specification-internal history handling behavior type. Several parts of this standard make use of this overlap, by passing in a history handling behavior to an algorithm that expects a NavigationType.

7.2.6.4 Initializing and updating the entry list

To initialize the navigation API entries for a new document given a Navigation navigation, a list of session history entries newSHEs, and a session history entry initialSHE:

Assert: navigation's entry list is empty.

Assert: navigation's current entry index is −1.

If navigation has entries and events disabled, then return.

For each newSHE of newSHEs:

Let newNHE be a new NavigationHistoryEntry created in the relevant realm of navigation.

Set newNHE's session history entry to newSHE.

Append newNHE to navigation's entry list.

newSHEs will have originally come from getting session history entries for the navigation API, and thus each newSHE will be contiguous same origin with initialSHE.

Set navigation's current entry index to the result of getting the navigation API entry index of initialSHE within navigation.

To update the navigation API entries for reactivation given a Navigation navigation, a list of session history entries newSHEs, and a session history entry reactivatedSHE:

If navigation has entries and events disabled, then return.

Let newNHEs be a new empty list.

Let oldNHEs be a clone of navigation's entry list.

For each newSHE of newSHEs:

Let newNHE be null.

If oldNHEs contains a NavigationHistoryEntry matchingOldNHE whose session history entry is newSHE, then:

Set newNHE to matchingOldNHE.

Remove matchingOldNHE from oldNHEs.

Otherwise:

Set newNHE to a new NavigationHistoryEntry created in the relevant realm of navigation.

Set newNHE's session history entry to newSHE.

Append newNHE to newNHEs.

newSHEs will have originally come from getting session history entries for the navigation API, and thus each newSHE will be contiguous same origin with reactivatedSHE.

By the end of this loop, all NavigationHistoryEntrys that remain in oldNHEs represent session history entries which have been disposed while the Document was in bfcache.

Set navigation's entry list to newNHEs.

Set navigation's current entry index to the result of getting the navigation API entry index of reactivatedSHE within navigation.

Queue a global task on the navigation and traversal task source given navigation's relevant global object to run the following steps:

For each disposedNHE of oldNHEs:

Fire an event named dispose at disposedNHE.

We delay these steps by a task to ensure that dispose events will fire after the pageshow event. This ensures that pageshow is the first event a page receives upon reactivation.

(However, the rest of this algorithm runs before the pageshow event fires. This ensures that navigation.entries() and navigation.currentEntry will have correctly-updated values during any pageshow event handlers.)

To update the navigation API entries for a same-document navigation given a Navigation navigation, a session history entry destinationSHE, and a NavigationType navigationType:

If navigation has entries and events disabled, then return.

Let oldCurrentNHE be the current entry of navigation.

Let disposedNHEs be a new empty list.

If navigationType is "traverse", then:

Set navigation's current entry index to the result of getting the navigation API entry index of destinationSHE within navigation.

Assert: navigation's current entry index is not −1.

This algorithm is only called for same-document traversals. Cross-document traversals will instead call either initialize the navigation API entries for a new document or update the navigation API entries for reactivation.

Otherwise, if navigationType is "push", then:

Set navigation's current entry index to navigation's current entry index + 1.

Let i be navigation's current entry index.

While i < navigation's entry list's size:

Append navigation's entry list[i] to disposedNHEs.

Set i to i + 1.

Remove all items in disposedNHEs from navigation's entry list.

Otherwise, if navigationType is "replace", then:

Append oldCurrentNHE to disposedNHEs.

If navigationType is "push" or "replace", then:

Let newNHE be a new NavigationHistoryEntry created in the relevant realm of navigation.

Set newNHE's session history entry to destinationSHE.

Set navigation's entry list[navigation's current entry index] to newNHE.

If navigation's ongoing API method tracker is non-null, then notify about the committed-to entry given navigation's ongoing API method tracker and the current entry of navigation.

It is important to do this before firing the dispose or currententrychange events, since event handlers could start another navigation, or otherwise change the value of navigation's ongoing API method tracker.

Prepare to run script given navigation's relevant settings object.

See the discussion for other navigation API events to understand why we do this.

Fire an event named currententrychange at navigation using NavigationCurrentEntryChangeEvent, with its navigationType attribute initialized to navigationType and its from initialized to oldCurrentNHE.

For each disposedNHE of disposedNHEs:

Fire an event named dispose at disposedNHE.

Clean up after running script given navigation's relevant settings object.

In implementations, same-document navigations can cause session history entries to be disposed by falling off the back of the session history entry list. This is not yet handled by the above algorithm (or by any other part of this standard). See issue #8620 to track progress on defining the correct behavior in such cases.

7.2.6.5 The NavigationHistoryEntry interface
[Exposed=Window]
interface NavigationHistoryEntry : EventTarget {
  readonly attribute USVString? url;
  readonly attribute DOMString key;
  readonly attribute DOMString id;
  readonly attribute long long index;
  readonly attribute boolean sameDocument;

  any getState();

  attribute EventHandler ondispose;
};
entry.url

The URL of this navigation history entry.

This can return null if the entry corresponds to a different Document than the current one (i.e., if sameDocument is false), and that Document was fetched with a referrer policy of "no-referrer" or "origin", since that indicates the Document in question is hiding its URL even from other same-origin pages.

entry.key

A user agent-generated random UUID string representing this navigation history entry's place in the navigation history list. This value will be reused by other NavigationHistoryEntry instances that replace this one due to "replace" navigations, and will survive reloads and session restores.

This is useful for navigating back to this entry in the navigation history list, using navigation.traverseTo(key).

entry.id

A user agent-generated random UUID string representing this specific navigation history entry. This value will not be reused by other NavigationHistoryEntry instances. This value will survive reloads and session restores.

This is useful for associating data with this navigation history entry using other storage APIs.

entry.index

The index of this NavigationHistoryEntry within navigation.entries(), or −1 if the entry is not in the navigation history entry list.

entry.sameDocument

Indicates whether or not this navigation history entry is for the same Document as the current one, or not. This will be true, for example, when the entry represents a fragment navigation or single-page app navigation.

entry.getState()

Returns the deserialization of the state stored in this entry, which was added to the entry using navigation.navigate() or navigation.updateCurrentEntry(). This state survives reloads and session restores.

Note that in general, unless the state value is a primitive, entry.getState() !== entry.getState(), since a fresh deserialization is returned each time.

This state is unrelated to the classic history API's history.state.

Each NavigationHistoryEntry has an associated session history entry, which is a session history entry.

The key of a NavigationHistoryEntry nhe is given by the return value of the following algorithm:

If nhe's relevant global object's associated Document is not fully active, then return the empty string.

Return nhe's session history entry's navigation API key.

The ID of a NavigationHistoryEntry nhe is given by the return value of the following algorithm:

If nhe's relevant global object's associated Document is not fully active, then return the empty string.

Return nhe's session history entry's navigation API ID.

The index of a NavigationHistoryEntry nhe is given by the return value of the following algorithm:

If nhe's relevant global object's associated Document is not fully active, then return −1.

Return the result of getting the navigation API entry index of this's session history entry within this's relevant global object's navigation API.

The url getter steps are:

Let document be this's relevant global object's associated Document.

If document is not fully active, then return the empty string.

Let she be this's session history entry.

If she's document does not equal document, and she's document state's request referrer policy is "no-referrer" or "origin", then return null.

Return she's URL, serialized.

The key getter steps are to return this's key.

The id getter steps are to return this's ID.

The index getter steps are to return this's index.

The sameDocument getter steps are:

Let document be this's relevant global object's associated Document.

If document is not fully active, then return false.

Return true if this's session history entry's document equals document, and false otherwise.

The getState() method steps are:

If this's relevant global object's associated Document is not fully active, then return undefined.

Return StructuredDeserialize(this's session history entry's navigation API state). Rethrow any exceptions.

This can in theory throw an exception, if attempting to deserialize a large ArrayBuffer when not enough memory is available.

The following are the event handlers (and their corresponding event handler event types) that must be supported, as event handler IDL attributes, by all objects implementing the NavigationHistoryEntry interface:

Event handler	Event handler event type
ondispose	dispose
7.2.6.6 The history entry list
entries = navigation.entries()

Returns an array of NavigationHistoryEntry instances represent the current navigation history entry list, i.e., all session history entries for this navigable that are same origin and contiguous to the current session history entry.

navigation.currentEntry

Returns the NavigationHistoryEntry corresponding to the current session history entry.

navigation.updateCurrentEntry({ state })

Updates the navigation API state of the current session history entry, without performing a navigation like navigation.reload() would do.

This method is best used to capture updates to the page that have already happened, and need to be reflected into the navigation API state. For cases where the state update is meant to drive a page update, instead use navigation.navigate() or navigation.reload(), which will trigger a navigate event.

navigation.canGoBack

Returns true if the current current session history entry (i.e., currentEntry) is not the first one in the navigation history entry list (i.e., in entries()). This means that there is a previous session history entry for this navigable, and its document state's origin is same origin with the current Document's origin.

navigation.canGoForward

Returns true if the current current session history entry (i.e., currentEntry) is not the last one in the navigation history entry list (i.e., in entries()). This means that there is a next session history entry for this navigable, and its document state's origin is same origin with the current Document's origin.

The entries() method steps are:

If this has entries and events disabled, then return the empty list.

Return this's entry list.

Recall that because of Web IDL's sequence type conversion rules, this will create a new JavaScript array object on each call. That is, navigation.entries() !== navigation.entries().

The currentEntry getter steps are to return the current entry of this.

The updateCurrentEntry(options) method steps are:

Let current be the current entry of this.

If current is null, then throw an "InvalidStateError" DOMException.

Let serializedState be StructuredSerializeForStorage(options["state"]), rethrowing any exceptions.

Set current's session history entry's navigation API state to serializedState.

Fire an event named currententrychange at this using NavigationCurrentEntryChangeEvent, with its navigationType attribute initialized to null and its from initialized to current.

The canGoBack getter steps are:

If this has entries and events disabled, then return false.

Assert: this's current entry index is not −1.

If this's current entry index is 0, then return false.

Return true.

The canGoForward getter steps are:

If this has entries and events disabled, then return false.

Assert: this's current entry index is not −1.

If this's current entry index is equal to this's entry list's size − 1, then return false.

Return true.

7.2.6.7 Initiating navigations
{ committed, finished } = navigation.navigate(url)
{ committed, finished } = navigation.navigate(url, options)

Navigates the current page to the given url. options can contain the following values:

history can be set to "replace" to replace the current session history entry, instead of pushing a new one.

info can be set to any value; it will populate the info property of the corresponding NavigateEvent.

state can be set to any serializable value; it will populate the state retrieved by navigation.currentEntry.getState() once the navigation completes, for same-document navigations. (It will be ignored for navigations that end up cross-document.)

By default this will perform a full navigation (i.e., a cross-document navigation, unless the given URL differs only in a fragment from the current one). The navigateEvent.intercept() method can be used to convert it into a same-document navigation.

The returned promises will behave as follows:

For navigations that get aborted, both promises will reject with an "AbortError" DOMException.

For same-document navigations created by using the navigateEvent.intercept() method, committed will fulfill after the navigation commits, and finished will fulfill or reject according to any promsies returned by handlers passed to intercept().

For other same-document navigations (e.g., non-intercepted fragment navigations), both promises will fulfill immediately.

For cross-document navigations, or navigations that result in 204 or 205 statuses or `Content-Disposition: attachment` header fields from the server (and thus do not actually navigate), both promises will never settle.

In all cases, when the returned promises fulfill, it will be with the NavigationHistoryEntry that was navigated to.

{ committed, finished } = navigation.reload(options)

Reloads the current page. options can contain info and state, which behave as described above.

The default behavior of performing a from-network-or-cache reload of the current page can be overriden by the using the navigateEvent.intercept() method. Doing so will mean this call only updates state or passes along the appropriate info, plus performing whater actions the navigate event handlers see fit to carry out.

The returned promises will behave as follows:

If the reload is intercepted by using the navigateEvent.intercept() method, committed will fulfill after the navigation commits, and finished will fulfill or reject according to any promsies returned by handlers passed to intercept().

Otherwise, both promises will never settle.

{ committed, finished } = navigation.traverseTo(key)
{ committed, finished } = navigation.traverseTo(key, { info })

Traverses to the closest session history entry that matches the NavigationHistoryEntry with the given key. info can be set to any value; it will populate the info property of the corresponding NavigateEvent.

If a traversal to that session history entry is already in progress, then this will return the promises for that original traversal, and info will be ignored.

The returned promises will behave as follows:

If there is no NavigationHistoryEntry in navigation.entries() whose key matches key, both promises will reject with an "InvalidStateError" DOMException.

For same-document traversals intercepted by the navigateEvent.intercept() method, committed will fulfill as soon as the traversal is processed and navigation.currentEntry is updated, and finished will fulfill or reject according to any promsies returned by the handlers passed to intercept().

For non-intercepted same-document travesals, both promises will fulfill as soon as the traversal is processed and navigation.currentEntry is updated.

For cross-document traversals, including attempted cross-document traversals that end up resulting in a 204 or 205 statuses or `Content-Disposition: attachment` header fields from the server (and thus do not actually traverse), both promises will never settle.

{ committed, finished } = navigation.back(key)
{ committed, finished } = navigation.back(key, { info })

Traverses to the closest previous session history entry which results in this navigable traversing, i.e., which corresponds to a different NavigationHistoryEntry and thus will cause navigation.currentEntry to change. info can be set to any value; it will populate the info property of the corresponding NavigateEvent.

If a traversal to that session history entry is already in progress, then this will return the promises for that original traversal, and info will be ignored.

The returned promises behave equivalently to those returned by traverseTo().

{ committed, finished } = navigation.forward(key)
{ committed, finished } = navigation.forward(key, { info })

Traverses to the closest forward session history entry which results in this navigable traversing, i.e., which corresponds to a different NavigationHistoryEntry and thus will cause navigation.currentEntry to change. info can be set to any value; it will populate the info property of the corresponding NavigateEvent.

If a traversal to that session history entry is already in progress, then this will return the promises for that original traversal, and info will be ignored.

The returned promises behave equivalently to those returned by traverseTo().

The navigate(url, options) method steps are:

Let urlRecord be the result of parsing a URL given url, relative to this's relevant settings object.

If urlRecord is failure, then return an early error result for a "SyntaxError" DOMException.

If urlRecord's scheme is "javascript", then return an early error result for a "NotSupportedError" DOMException.

Let document be this's relevant global object's associated Document.

If options["history"] is "push", and the navigation must be a replace given urlRecord and document, then return an early error result for a "NotSupportedError" DOMException.

Let state be options["state"], if it exists; otherwise, undefined.

Let serializedState be StructuredSerializeForStorage(state). If this throws an exception, then return an early error result for that exception.

It is important to perform this step early, since serialization can invoke web developer code, which in turn might change various things we check in later steps.

If document is not fully active, then return an early error result for an "InvalidStateError" DOMException.

If document's unload counter is greater than 0, then return an early error result for an "InvalidStateError" DOMException.

Let info be options["info"], if it exists; otherwise, undefined.

Let apiMethodTracker be the result of setting up a navigate/reload API method tracker for this given info and serializedState.

Navigate document's node navigable to urlRecord using document, with historyHandling set to options["history"], navigationAPIState set to serializedState, and apiMethodTracker set to apiMethodTracker.

Unlike location.assign() and friends, which are exposed across origin-domain boundaries, navigation.navigate() can only be accessed by code with direct synchronous access to the window.navigation property. Thus, we avoid the complications about attributing the source document of the navigation, and we don't need to deal with the allowed by sandboxing to navigate check and its acccompanying exceptionsEnabled flag. We just treat all navigations as if they come from the Document corresponding to this Navigation object itself (i.e., document).

Return a navigation API method tracker-derived result for apiMethodTracker.

The reload(options) method steps are:

Let document be this's relevant global object's associated Document.

Let serializedState be StructuredSerializeForStorage(undefined).

If options["state"] exists, then set serializedState to StructuredSerializeForStorage(options["state"]). If this throws an exception, then return an early error result for that exception.

It is important to perform this step early, since serialization can invoke web developer code, which in turn might change various things we check in later steps.

Otherwise:

Let current be the current entry of this.

If current is not null, then set serializedState to current's session history entry's navigation API state.

If document is not fully active, then return an early error result for an "InvalidStateError" DOMException.

If document's unload counter is greater than 0, then return an early error result for an "InvalidStateError" DOMException.

Let info be options["info"], if it exists; otherwise, undefined.

Let apiMethodTracker be the result of setting up a navigate/reload API method tracker for this given info and serializedState.

Reload document's node navigable with navigationAPIState set to serializedState and apiMethodTracker set to apiMethodTracker.

Return a navigation API method tracker-derived result for apiMethodTracker.

The traverseTo(key, options) method steps are:

If this's current entry index is −1, then return an early error result for an "InvalidStateError" DOMException.

If this's entry list does not contain a NavigationHistoryEntry whose session history entry's navigation API key equals key, then return an early error result for an "InvalidStateError" DOMException.

Return the result of performing a navigation API traversal given this, key, and options.

The back(options) method steps are:

If this's current entry index is −1 or 0, then return an early error result for an "InvalidStateError" DOMException.

Let key be this's entry list[this's current entry index − 1]'s session history entry's navigation API key.

Return the result of performing a navigation API traversal given this, key, and options.

The forward(options) method steps are:

If this's current entry index is −1 or is equal to this's entry list's size − 1, then return an early error result for an "InvalidStateError" DOMException.

Let key be this's entry list[this's current entry index + 1]'s session history entry's navigation API key.

Return the result of performing a navigation API traversal given this, key, and options.

To perform a navigation API traversal given a Navigation navigation, a string key, and a NavigationOptions options:

Let document be navigation's relevant global object's associated Document.

If document is not fully active, then return an early error result for an "InvalidStateError" DOMException.

If document's unload counter is greater than 0, then return an early error result for an "InvalidStateError" DOMException.

Let current be the current entry of navigation.

If key equals current's session history entry's navigation API key, then return «[ "committed" → a promise resolved with current, "finished" → a promise resolved with current ]».

If navigation's upcoming traverse API method trackers[key] exists, then return a navigation API method tracker-derived result for navigation's upcoming traverse API method trackers[key].

Let info be options["info"], if it exists; otherwise, undefined.

Let apiMethodTracker be the result of adding an upcoming traverse API method tracker for navigation given key and info.

Let navigable be document's node navigable.

Let traversable be navigable's traversable navigable.

Let sourceSnapshotParams be the result of snapshotting source snapshot params given document.

Append the following session history traversal steps to traversable:

Let navigableSHEs be the result of getting session history entries given navigable.

Let targetSHE be the session history entry in navigableSHEs whose navigation API key is key. If no such entry exists, then:

Queue a global task on the navigation and traversal task source given navigation's relevant global object to reject the finished promise for apiMethodTracker with an "InvalidStateError" DOMException.

Abort these steps.

This path is taken if navigation's entry list was outdated compared to navigableSHEs, which can occur for brief periods while all the relevant threads and processes are being synchronized in reaction to a history change.

If targetSHE is navigable's active session history entry, then:

Queue a global task on the navigation and traversal task source given navigation's relevant global object to reject the finished promise for apiMethodTracker with an "InvalidStateError" DOMException.

Abort these steps.

This can occur if a previously queued traversal already took us to this session history entry.

Let result be the result of applying the traverse history step given by targetSHE's step to traversable, given sourceSnapshotParams, navigable, and "none".

If result is "canceled-by-beforeunload", then queue a global task on the navigation and traversal task source given navigation's relevant global object to reject the finished promise for apiMethodTracker with a new "AbortError" DOMException created in navigation's relevant realm.

If result is "initiator-disallowed", then queue a global task on the navigation and traversal task source given navigation's relevant global object to reject the finished promise for apiMethodTracker with a new "SecurityError" DOMException created in navigation's relevant realm.

When result is "canceled-by-beforeunload" or "initiator-disallowed", the navigate event was never fired, aborting the ongoing navigation would not be correct; it would result in a navigateerror event without a preceding navigate event.

In the "canceled-by-navigate" case, navigate is fired, but the inner navigate event firing algorithm will take care of aborting the ongoing navigation.

Return a navigation API method tracker-derived result for apiMethodTracker.

An early error result for an exception e is a NavigationResult dictionary instance given by «[ "committed" → a promise rejected with e, "finished" → a promise rejected with e ]».

To compute the navigation API method tracker-derived result for a navigation API method tracker-or-null apiMethodTracker:

If apiMethodTracker is pending, then return an early error result for an "AbortError" DOMException.

Return a NavigationResult dictionary instance given by «[ "committed" → apiMethodTracker's committed promise, "finished" → apiMethodTracker's finished promise ]».

7.2.6.8 Ongoing navigation tracking

During any given navigation (in the broad sense of the word), the Navigation object needs to keep track of the following:

For all navigations
State	Duration	Explanation
The NavigateEvent	For the duration of event firing	So that if the navigation is canceled while the event is firing, we can cancel the event
The event's abort controller	Until all promises returned from handlers passed to intercept() have settled	So that if the navigation is canceled, we can signal abort
Whether a new element was focused	Until all promises returned from handlers passed to intercept() have settled	So that if one was, focus is not reset
The NavigationHistoryEntry being navigated to	From when it is determined, until all promises returned from handlers passed to intercept() have settled	So that we know what to resolve any committed and finished promises with
Any finished promise that was returned	Until all promises returned from handlers passed to intercept() have settled	So that we can resolve or reject it appropriately
For non-"traverse" navigations
State	Duration	Explanation
Any state	For the duration of event firing	So that we can update the current entry's navigation API state if the event finishes firing without being canceled
For "traverse" navigations
State	Duration	Explanation
Any info	Until the task is queued to fire the navigate event	So that we can use it to fire the navigate after the trip through the session history traversal queue.
Any committed promise that was returned	Until the session history is updated (inside that same task)	So that we can resolve or reject it appropriately
Whether intercept() was called	Until the session history is updated (inside that same task)	So that we can suppress the normal scroll restoration logic in favor of the behavior given by the scroll option

We also cannot assume there is only a single navigation requested at any given time, due to web developer code such as:

const p1 = navigation.navigate(url1).finished;
const p2 = navigation.navigate(url2).finished;

That is, in this scenario, we need to ensure that while navigating to url2, we still have the promise p1 around so that we can reject it. We can't just get rid of any ongoing navigation promises the moment the second call to navigate() happens.

We end up accomplishing all this by associating the following with each Navigation:

Ongoing navigate event, a NavigateEvent or null, initially null.

Focus changed during ongoing navigation, a boolean, initially false.

Suppress normal scroll restoration during ongoing navigation, a boolean, initially false.

Ongoing API method tracker, a navigation API method tracker or null, initially null.

Upcoming traverse API method trackers, an ordered map from strings to navigation API method trackers, initially empty.

The state here that is not stored in navigation API method trackers is state which needs to be tracked even for navigations that are not initiated via navigation API methods.

A navigation API method tracker is a struct with the following items:

A navigation object, a Navigation

A key, a string or null

An info, a JavaScript value

A serialized state, a serialized state or null

A committed-to entry, a NavigationHistoryEntry or null

A committed promise, a promise

A finished promise, a promise

A pending, a boolean.

All this state is then managed via the following algorithms.

To set up a navigate/reload API method tracker given a Navigation navigation, a JavaScript value info, and a serialized state-or-null serializedState:

Let committedPromise and finishedPromise be new promises created in navigation's relevant realm.

Mark as handled finishedPromise.

The web developer doesn’t necessarily care about finishedPromise being rejected:

They might only care about committedPromise.

They could be doing multiple synchronous navigations within the same task, in which case all but the last will be aborted (causing their finishedPromise to reject). This could be an application bug, but also could just be an emergent feature of disparate parts of the application overriding each others' actions.

They might prefer to listen to other transition-failure signals instead of finishedPromise, e.g., the navigateerror event, or the navigation.transition.finished promise.

As such, we mark it as handled to ensure that it never triggers unhandledrejection events.

Return a new navigation API method tracker with:

navigation object
navigation
key
null
info
info
serialized state
serializedState
committed-to entry
null
committed promise
committedPromise
finished promise
finishedPromise
pending
false if navigation has entries and events disabled; otherwise true

To add an upcoming traverse API method tracker given a Navigation navigation, a string destinationKey, and a JavaScript value info:

Let committedPromise and finishedPromise be new promises created in navigation's relevant realm.

Mark as handled finishedPromise.

See the previous discussion about why this is done.

Let apiMethodTracker be a new navigation API method tracker with:

navigation object
navigation
key
destinationKey
info
info
serialized state
null
committed-to entry
null
committed promise
committedPromise
finished promise
finishedPromise
pending
false

Set navigation's upcoming traverse API method trackers[destinationKey] to apiMethodTracker.

Return apiMethodTracker.

To clean up a navigation API method tracker apiMethodTracker:

Let navigation be apiMethodTracker's navigation object.

If navigation's ongoing API method tracker is apiMethodTracker, then set navigation's ongoing API method tracker to null.

Otherwise:

Let key be apiMethodTracker's key.

Assert: key is not null.

Assert: navigation's upcoming traverse API method trackers[key] exists.

Remove navigation's upcoming traverse API method trackers[key].

To notify about the committed-to entry given a navigation API method tracker apiMethodTracker and a NavigationHistoryEntry nhe:

Set apiMethodTracker's committed-to entry to nhe.

If apiMethodTracker's serialized state is not null, then set nhe's session history entry's navigation API state to apiMethodTracker's serialized state.

If it's null, then we're traversing to nhe via navigation.traverseTo(), which does not allow changing the state.

At this point, apiMethodTracker's serialized state is no longer needed. Implementations might want to clear it out to avoid keeping it alive for the lifetime of the navigation API method tracker.

Resolve apiMethodTracker's committed promise with nhe.

At this point, apiMethodTracker's committed promise is only needed in cases where it has not yet been returned to author code. Implementations might want to clear it out to avoid keeping it alive for the lifetime of the navigation API method tracker.

To resolve the finished promise for a navigation API method tracker apiMethodTracker:

Assert: apiMethodTracker's committed-to entry is not null.

Resolve apiMethodTracker's finished promise with its committed-to entry.

Clean up apiMethodTracker.

To reject the finished promise for a navigation API method tracker apiMethodTracker with a JavaScript value exception:

Reject apiMethodTracker's committed promise with exception.

This will do nothing if apiMethodTracker's committed promise was previously resolved via notify about the committed-to entry.

Reject apiMethodTracker's finished promise with exception.

Clean up apiMethodTracker.

To abort the ongoing navigation given a Navigation navigation and an optional DOMException error:

Let event be navigation's ongoing navigate event.

Assert: event is not null.

Set navigation's focus changed during ongoing navigation to false.

Set navigation's suppress normal scroll restoration during ongoing navigation to false.

If error was not given, then let error be a new "AbortError" DOMException created in navigation's relevant realm.

If event's dispatch flag is set, then set event's canceled flag to true.

Abort event given error.

To abort a NavigateEvent event given reason:

Let navigation be event's relevant global object's navigation API.

Signal abort on event's abort controller given reason.

Let errorInfo be the result of extracting error information from reason.

For example, if this algorithm is reached because of a call to window.stop(), these properties would probably end up initialized based on the line of script that called window.stop(). But if it's because the user clicked the stop button, these properties would probably end up with default values like the empty string or 0.

Set navigation's ongoing navigate event to null.

If navigation's ongoing API method tracker is non-null, then reject the finished promise for apiMethodTracker with reason.

Fire an event named navigateerror at navigation using ErrorEvent, with additional attributes initialized according to errorInfo.

If navigation's transition is null, then return.

Reject navigation's transition's committed promise with reason.

Reject navigation's transition's finished promise with reason.

Set navigation's transition to null.

To inform the navigation API about aborting navigation in a navigable navigable:

If this algorithm is running on navigable's active window's relevant agent's event loop, then continue on to the following steps. Otherwise, queue a global task on the navigation and traversal task source given navigable's active window to run the following steps.

Let navigation be navigable's active window's navigation API.

While navigation's ongoing navigate event is not null:

Abort the ongoing navigation given navigation.

If there is an ongoing cross-document navigation, this means it will be signaled to the navigation API as aborted, e.g., by firing navigateerror events. This is somewhat accurate, since the next navigation the Document experiences will be this same-document navigation, so a developer which was expecting the next navigation completion to be that of the cross-document navigation gets a useful signal that this did not happen. However, it is also somewhat inaccurate, as the browser will continue to process the ongoing cross-document navigation (applying it after this same-document one synchronously finishes).

Ultimately, the navigation API gets a bit messy with overlapping cross- and same-document navigations, as the ongoing navigation tracking machinery and APIs are built to expose only a single ongoing navigation. Web developers will be best-served if they do not create such overlapping situations, e.g., by awaiting promises returned from navigation.navigate() before starting new navigations.

This is a loop, since abort the ongoing navigation can run JavaScript (e.g., via the navigateerror event), which might start a new navigation. Since such a newly-started navigation will be superseded by the completion of this navigation, it gets signaled to the navigation API as aborted.

To inform the navigation API about child navigable destruction given a navigable navigable:

Inform the navigation API about aborting navigation in navigable.

Let navigation be navigable's active window's navigation API.

Let traversalAPIMethodTrackers be a clone of navigation's upcoming traverse API method trackers.

For each apiMethodTracker of traversalAPIMethodTrackers: reject the finished promise for apiMethodTracker with a new "AbortError" DOMException created in navigation's relevant realm.

The ongoing navigation concept is most-directly exposed to web developers through the navigation.transition property, which is an instance of the NavigationTransition interface:

[Exposed=Window]
interface NavigationTransition {
  readonly attribute NavigationType navigationType;
  readonly attribute NavigationHistoryEntry from;
  readonly attribute NavigationDestination to;
  readonly attribute Promise<undefined> committed;
  readonly attribute Promise<undefined> finished;
};
navigation.transition

A NavigationTransition representing any ongoing navigation that hasn't yet reached the navigatesuccess or navigateerror stage, if one exists; or null, if there is no such transition ongoing.

Since navigation.currentEntry (and other properties like location.href) are updated immediately upon navigation, this navigation.transition property is useful for determining when such navigations are not yet fully settled, according to any handlers passed to navigateEvent.intercept().

navigation.transition.navigationType

One of "push", "replace", "reload", or "traverse", indicating what type of navigation this transition is for.

navigation.transition.from

The NavigationHistoryEntry from which the transition is coming. This can be useful to compare against navigation.currentEntry.

navigation.transition.to

The NavigationDestination of the transition. This can be useful as a way to reflect a current navigation's destination's url without having to listen to the navigate event.

navigation.transition.committed

A promise which fulfills once the navigation.currentEntry and URL change. This occurs after all of its precommit handlers are fulfilled. The promise rejects if one or more of the precommit handlers rejects.

navigation.transition.finished

A promise which fulfills at the same time as the navigatesuccess fires, or rejects at the same time the navigateerror event fires.

Each Navigation has a transition, which is a NavigationTransition or null, initially null.

The transition getter steps are to return this's transition.

Each NavigationTransition has an associated navigation type, which is a NavigationType.

Each NavigationTransition has an associated from entry, which is a NavigationHistoryEntry.

Each NavigationTransition has an associated destination, which is a NavigationDestination.

Each NavigationTransition has an associated committed promise, which is a promise.

Each NavigationTransition has an associated finished promise, which is a promise.

The navigationType getter steps are to return this's navigation type.

The from getter steps are to return this's from entry.

The to getter steps are to return this's destination.

The committed getter steps are to return this's committed promise.

The finished getter steps are to return this's finished promise.

7.2.6.9 The NavigationActivation interface
[Exposed=Window]
interface NavigationActivation {
  readonly attribute NavigationHistoryEntry? from;
  readonly attribute NavigationHistoryEntry entry;
  readonly attribute NavigationType navigationType;
};
navigation.activation

A NavigationActivation containing information about the most recent cross-document navigation, the navigation that "activated" this Document.

While navigation.currentEntry and the Document's URL can be updated regularly due to same-document navigations, navigation.activation stays constant, and its properties are only updated if the Document is reactivated from history.

navigation.activation.entry

A NavigationHistoryEntry, equivalent to the value of the navigation.currentEntry property at the moment the Document was activated.

navigation.activation.from

A NavigationHistoryEntry, representing the Document that was active right before the current Document. This will have a value null in case the previous Document was not same origin with this one or if it was the initial about:blank Document.

There are some cases in which either the from or entry NavigationHistoryEntry objects would not be viable targets for the traverseTo() method, as they might not be retained in history. For example, the Document can be activated using location.replace() or its initial entry could be replaced by history.replaceState(). However, those entries' url property and getState() method are still accessible.

navigation.activation.navigationType

One of "push", "replace", "reload", or "traverse", indicating what type of navigation activated this Document.

Each Navigation has an associated activation, which is null or a NavigationActivation object, initially null.

Each NavigationActivation has:

old entry, null or a NavigationHistoryEntry.

new entry, null or a NavigationHistoryEntry.

navigation type, a NavigationType.

The activation getter steps are to return this's activation.

The from getter steps are to return this's old entry.

The entry getter steps are to return this's new entry.

The navigationType getter steps are to return this's navigation type.

7.2.6.10 The navigate event

A major feature of the navigation API is the navigate event. This event is fired on any navigation (in the broad sense of the word), allowing web developers to monitor such outgoing navigations. In many cases, the event is cancelable, which allows preventing the navigation from happening. And in others, the navigation can be intercepted and replaced with a same-document navigation by using the intercept() method of the NavigateEvent class.

7.2.6.10.1 The NavigateEvent interface
[Exposed=Window]
interface NavigateEvent : Event {
  constructor(DOMString type, NavigateEventInit eventInitDict);

  readonly attribute NavigationType navigationType;
  readonly attribute NavigationDestination destination;
  readonly attribute boolean canIntercept;
  readonly attribute boolean userInitiated;
  readonly attribute boolean hashChange;
  readonly attribute AbortSignal signal;
  readonly attribute FormData? formData;
  readonly attribute DOMString? downloadRequest;
  readonly attribute any info;
  readonly attribute boolean hasUAVisualTransition;
  readonly attribute Element? sourceElement;

  undefined intercept(optional NavigationInterceptOptions options = {});
  undefined scroll();
};

dictionary NavigateEventInit : EventInit {
  NavigationType navigationType = "push";
  required NavigationDestination destination;
  boolean canIntercept = false;
  boolean userInitiated = false;
  boolean hashChange = false;
  required AbortSignal signal;
  FormData? formData = null;
  DOMString? downloadRequest = null;
  any info;
  boolean hasUAVisualTransition = false;
  Element? sourceElement = null;
};

dictionary NavigationInterceptOptions {
  NavigationPrecommitHandler precommitHandler;
  NavigationInterceptHandler handler;
  NavigationFocusReset focusReset;
  NavigationScrollBehavior scroll;
};

enum NavigationFocusReset {
  "after-transition",
  "manual"
};

enum NavigationScrollBehavior {
  "after-transition",
  "manual"
};

callback NavigationInterceptHandler = Promise<undefined> ();
event.navigationType

One of "push", "replace", "reload", or "traverse", indicating what type of navigation this is.

event.destination

A NavigationDestination representing the destination of the navigation.

event.canIntercept

True if intercept() can be called to intercept this navigation and convert it into a same-document navigation, replacing its usual behavior; false otherwise.

Generally speaking, this will be true whenever the current Document can have its URL rewritten to the destination URL, except for in the case of cross-document "traverse" navigations, where it will always be false.

event.userInitiated

True if this navigation was due to a user clicking on an a element, submitting a form element, or using the browser UI to navigate; false otherwise.

event.hashChange

True for a fragment navigation; false otherwise.

event.signal

An AbortSignal which will become aborted if the navigation gets canceled, e.g., by the user pressing their browser's "Stop" button, or by another navigation interrupting this one.

The expected pattern is for developers to pass this along to any async operations, such as fetch(), which they perform as part of handling this navigation.

event.formData

The FormData representing the submitted form entries for this navigation, if this navigation is a "push" or "replace" navigation representing a POST form submission; null otherwise.

(Notably, this will be null even for "reload" or "traverse" navigations that are revisiting a session history entry that was originally created from a form submission.)

event.downloadRequest

Represents whether or not this navigation was requested to be a download, by using an a or area element's download attribute:

If a download was not requested, then this property is null.

If a download was requested, returns the filename that was supplied as the download attribute's value. (This could be the empty string.)

Note that a download being requested does not always mean that a download will happen: for example, a download might be blocked by browser security policies, or end up being treated as a "push" navigation for unspecified reasons.

Similarly, a navigation might end up being a download even if it was not requested to be one, due to the destination server responding with a `Content-Disposition: attachment` header.

Finally, note that the navigate event will not fire at all for downloads initiated using browser UI affordances, e.g., those created by right-clicking and choosing to save the target of a link.

event.info

An arbitrary JavaScript value passed via one of the navigation API methods which initiated this navigation, or undefined if the navigation was initiated by the user or by a different API.

event.hasUAVisualTransition

Returns true if the user agent performed a visual transition for this navigation before dispatching this event. If true, the best user experience will be given if the author synchronously updates the DOM to the post-navigation state.

event.sourceElement

Returns the Element responsible for this navigation. This can be an aor area element, a submit button, or a submitted form element.

event.intercept({ precommitHandler, handler, focusReset, scroll })

Intercepts this navigation, preventing its normal handling and instead converting it into a same-document navigation of the same type to the destination URL.

The precommitHandler option can be a function that accepts a NavigationPrecommitController and returns a promise. The precommit handler function will run after the navigate event has finished firing, but before the navigation.currentEntry property has been updated. Returning a rejected promise will abort the navigation and its effect, such as updating the URL and session history. After all the precommit handlers are fulfilled, the navigation can proceed to commit and call the rest of the handlers. The precommitHandler option can only be passed when the event is cancelable: trying to pass a precommitHandler to a non-cancelable NavigateEvent will throw a "SecurityError" DOMException.

The handler option can be a function that returns a promise. The handler function will run after the navigate event has finished firing and the navigation.currentEntry property has been updated. This returned promise is used to signal the duration, and success or failure, of the navigation. After it settles, the browser signals to the user (e.g., via a loading spinner UI, or assistive technology) that the navigation is finished. Additionally, it fires navigatesuccess or navigateerror events as appropriate, which other parts of the web application can respond to.

By default, using this method will cause focus to reset when any handlers' returned promises settle. Focus will be reset to the first element with the autofocus attribute set, or the body element if the attribute isn't present. The focusReset option can be set to "manual" to avoid this behavior.

By default, using this method will delay the browser's scroll restoration logic for "traverse" or "reload" navigations, or its scroll-reset/scroll-to-a-fragment logic for "push" or "replace" navigations, until any handlers' returned promises settle. The scroll option can be set to "manual" to turn off any browser-driven scroll behavior entirely for this navigation, or scroll() can be called before the promise settles to trigger this behavior early.

This method will throw a "SecurityError" DOMException if canIntercept is false, or if isTrusted is false. It will throw an "InvalidStateError" DOMException if not called synchronously, during event dispatch.

event.scroll()

For "traverse" or "reload" navigations, restores the scroll position using the browser's usual scroll restoration logic.

For "push" or "replace" navigations, either resets the scroll position to the top of the document or scrolls to the fragment specified by destination.url if there is one.

If called more than once, or called after automatic post-transition scroll processing has happened due to the scroll option being left as "after-transition", or called before the navigation has committed, this method will throw an "InvalidStateError" DOMException.

Each NavigateEvent has an interception state, which is either "none", "intercepted", "committed", "scrolled", or "finished", initially "none".

Each NavigateEvent has a navigation precommit handler list, a list of NavigationPrecommitHandler callbacks, initially empty.

Each NavigateEvent has a navigation handler list, a list of NavigationInterceptHandler callbacks, initially empty.

Each NavigateEvent has a focus reset behavior, a NavigationFocusReset-or-null, initially null.

Each NavigateEvent has a scroll behavior, a NavigationScrollBehavior-or-null, initially null.

Each NavigateEvent has an abort controller, an AbortController-or-null, initially null.

Each NavigateEvent has a classic history API state, a serialized state or null. It is only used in some cases where the event's navigationType is "push" or "replace", and is set appropriately when the event is fired.

The navigationType, destination, canIntercept, userInitiated, hashChange, signal, formData, downloadRequest, info, hasUAVisualTransition, and sourceElement attributes must return the values they are initialized to.

The intercept(options) method steps are:

Perform shared checks given this.

If this's canIntercept attribute was initialized to false, then throw a "SecurityError" DOMException.

If this's dispatch flag is unset, then throw an "InvalidStateError" DOMException.

If options["precommitHandler"] exists, then:

If this's cancelable attribute is initialized to false, then throw an "InvalidStateError" DOMException.

Append options["precommitHandler"] to this's navigation precommit handler list.

Assert: this's interception state is either "none" or "intercepted".

Set this's interception state to "intercepted".

If options["handler"] exists, then append it to this's navigation handler list.

If options["focusReset"] exists, then:

If this's focus reset behavior is not null, and it is not equal to options["focusReset"], then the user agent may report a warning to the console indicating that the focusReset option for a previous call to intercept() was overridden by this new value, and the previous value will be ignored.

Set this's focus reset behavior to options["focusReset"].

If options["scroll"] exists, then:

If this's scroll behavior is not null, and it is not equal to options["scroll"], then the user agent may report a warning to the console indicating that the scroll option for a previous call to intercept() was overridden by this new value, and the previous value will be ignored.

Set this's scroll behavior to options["scroll"].

The scroll() method steps are:

Perform shared checks given this.

If this's interception state is not "committed", then throw an "InvalidStateError" DOMException.

Process scroll behavior given this.

To perform shared checks for a NavigateEvent event:

If event's relevant global object's associated Document is not fully active, then throw an "InvalidStateError" DOMException.

If event's isTrusted attribute was initialized to false, then throw a "SecurityError" DOMException.

If event's canceled flag is set, then throw an "InvalidStateError" DOMException.

7.2.6.10.2 The NavigationPrecommitController interface
[Exposed=Window]
  interface NavigationPrecommitController {
    undefined redirect(USVString url, optional NavigationNavigateOptions options = {});
    undefined addHandler(NavigationInterceptHandler handler);
  };

  callback NavigationPrecommitHandler = Promise<undefined> (NavigationPrecommitController controller);
precommitController.redirect(USVString url, NavigationNavigateOptions options)

For "push" or "replace" navigations, sets the destination.url to url.

If options is given, also sets the info and the resulting NavigationHistoryEntry's state to options's info and state, if they are present. The history option can also switch between "push" or "replace" navigations types.

For "reload" or "traverse" navigations, an "InvalidStateError" will be thrown.

If the current Document cannot have its URL rewritten to url, a "SecurityError" DOMException will be thrown.

precommitController.addHandler(NavigationInterceptHandler handler)

Adds a NavigationInterceptHandler callback that would be called once the navigation is committed, as if this method was passed to the navigateEvent.intercept() method as a handler.

Each NavigationPrecommitController has a NavigateEvent event.

The redirect(url, options) method steps are:

Assert: this's event's interception state is not "none".

Perform shared checks given this's event.

If this's event's interception state is not "intercepted", then throw an "InvalidStateError" DOMException.

If this's event's navigationType is neither "push" nor "replace", then throw an "InvalidStateError" DOMException.

Let document be this's relevant global object's associated Document.

Let destinationURL be the result of parsing url given document.

If destinationURL is failure, then throw a "SyntaxError" DOMException.

If document cannot have its URL rewritten to destinationURL, then throw a "SecurityError" DOMException.

If options["history"] is "push" or "replace", then set this's event's navigationType to options["history"].

If options["state"] exists, then:

Let serializedState be the result of calling StructuredSerializeForStorage(options["state"]). This may throw an exception.

Set this's event's destination's state to serializedState.

Set this's event's target's ongoing API method tracker's serialized state to serializedState.

Set this's event's destination's URL to destinationURL.

If options["info"] exists, then set this's event's info to options["info"].

The addHandler(handler,) method steps are:

Assert: this's event's interception state is not "none".

Perform shared checks given this's event.

If this's event's interception state is not "intercepted", then throw an "InvalidStateError" DOMException.

Append handler to this's event's navigation handler list.

7.2.6.10.3 The NavigationDestination interface
[Exposed=Window]
interface NavigationDestination {
  readonly attribute USVString url;
  readonly attribute DOMString key;
  readonly attribute DOMString id;
  readonly attribute long long index;
  readonly attribute boolean sameDocument;

  any getState();
};
event.destination.url

The URL being navigated to.

event.destination.key

The value of the key property of the destination NavigationHistoryEntry, if this is a "traverse" navigation, or the empty string otherwise.

event.destination.id

The value of the id property of the destination NavigationHistoryEntry, if this is a "traverse" navigation, or the empty string otherwise.

event.destination.index

The value of the index property of the destination NavigationHistoryEntry, if this is a "traverse" navigation, or −1 otherwise.

event.destination.sameDocument

Indicates whether or not this navigation is to the same Document as the current one, or not. This will be true, for example, in the case of fragment navigations or history.pushState() navigations.

Note that this property indicates the original nature of the navigation. If a cross-document navigation is converted into a same-document navigation using navigateEvent.intercept(), that will not change the value of this property.

event.destination.getState()

For "traverse" navigations, returns the deserialization of the state stored in the destination session history entry.

For "push" or "replace" navigations, returns the deserialization of the state passed to navigation.navigate(), if the navigation was initiated by that method, or undefined it if it wasn't.

For "reload" navigations, returns the deserialization of the state passed to navigation.reload(), if the reload was initiated by that method, or undefined it if it wasn't.

Each NavigationDestination has a URL, which is a URL.

Each NavigationDestination has an entry, which is a NavigationHistoryEntry or null.

It will be non-null if and only if the NavigationDestination corresponds to a "traverse" navigation.

Each NavigationDestination has a state, which is a serialized state.

Each NavigationDestination has an is same document, which is a boolean.

The url getter steps are to return this's URL, serialized.

The key getter steps are:

If this's entry is null, then return the empty string.

Return this's entry's key.

The id getter steps are:

If this's entry is null, then return the empty string.

Return this's entry's ID.

The index getter steps are:

If this's entry is null, then return −1.

Return this's entry's index.

The sameDocument getter steps are to return this's is same document.

The getState() method steps are to return StructuredDeserialize(this's state).

7.2.6.10.4 Firing the event

Other parts of the standard fire the navigate event, through a series of wrapper algorithms given in this section.

To fire a traverse navigate event at a Navigation navigation given a session history entry destinationSHE and an optional user navigation involvement userInvolvement (default "none"):

Let event be the result of creating an event given NavigateEvent, in navigation's relevant realm.

Set event's classic history API state to null.

Let destination be a new NavigationDestination created in navigation's relevant realm.

Set destination's URL to destinationSHE's URL.

Let destinationNHE be the NavigationHistoryEntry in navigation's entry list whose session history entry is destinationSHE, or null if no such NavigationHistoryEntry exists.

If destinationNHE is non-null, then:

Set destination's entry to destinationNHE.

Set destination's state to destinationSHE's navigation API state.

Otherwise,

Set destination's entry to null.

Set destination's state to StructuredSerializeForStorage(null).

Set destination's is same document to true if destinationSHE's document is equal to navigation's relevant global object's associated Document; otherwise false.

Return the result of performing the inner navigate event firing algorithm given navigation, "traverse", event, destination, userInvolvement, null, null, and null.

To fire a push/replace/reload navigate event at a Navigation navigation given a NavigationType navigationType, a URL destinationURL, a boolean isSameDocument, an optional user navigation involvement userInvolvement (default "none"), an optional Element-or-null sourceElement (default null), an optional entry list-or-null formDataEntryList (default null), an optional serialized state navigationAPIState (default StructuredSerializeForStorage(null)), an optional serialized state-or-null classicHistoryAPIState (default null), and an optional navigation API method tracker-or-null apiMethodTracker:

Let document be navigation's relevant global object's associated Document.

Inform the navigation API about aborting navigation in document's node navigable.

If navigation has entries and events disabled, and apiMethodTracker is not null:

Set apiMethodTracker's pending to false.

Set apiMethodTracker to null.

If navigation has entries and events disabled, then navigate() and reload() calls return promises that will never fulfill. We never create a NavigationHistoryEntry object for such Documents, there is no NavigationHistoryEntry to apply serializedState to, and there is no navigate event to include info with. So, we don't need to track this API method call after all. We need to check this after aborting previous navigations, in case the Document has became non-fully active as a result of a navigateerror event.

If document is not fully active, then return false.

Let event be the result of creating an event given NavigateEvent, in navigation's relevant realm.

Set event's classic history API state to classicHistoryAPIState.

Let destination be a new NavigationDestination created in navigation's relevant realm.

Set destination's URL to destinationURL.

Set destination's entry to null.

Set destination's state to navigationAPIState.

Set destination's is same document to isSameDocument.

Return the result of performing the inner navigate event firing algorithm given navigation, navigationType, event, destination, userInvolvement, sourceElement, formDataEntryList, null, and apiMethodTracker.

To fire a download request navigate event at a Navigation navigation given a URL destinationURL, a user navigation involvement userInvolvement, an Element-or-null sourceElement, and a string filename:

Let event be the result of creating an event given NavigateEvent, in navigation's relevant realm.

Set event's classic history API state to null.

Let destination be a new NavigationDestination created in navigation's relevant realm.

Set destination's URL to destinationURL.

Set destination's entry to null.

Set destination's state to StructuredSerializeForStorage(null).

Set destination's is same document to false.

Return the result of performing the inner navigate event firing algorithm given navigation, "push", event, destination, userInvolvement, sourceElement, null, and filename.

The inner navigate event firing algorithm consists of the following steps, given a Navigation navigation, a NavigationType navigationType, a NavigateEvent event, a NavigationDestination destination, a user navigation involvement userInvolvement, an Element-or-null sourceElement, an entry list-or-null formDataEntryList, a string-or-null downloadRequestFilename, and an optional navigation API method tracker-or-null apiMethodTracker (default null):

If navigation has entries and events disabled, then:

Assert: navigation's ongoing API method tracker is null.

Assert: navigation's upcoming traverse API method trackers is empty.

Assert: apiMethodTracker is null.

Return true.

These assertions holds because traverseTo(), back(), and forward() will immediately fail when entries and events are disabled (since there are no entries to traverse to).

Assert: navigation's ongoing API method tracker is null.

If destination's entry is non-null:

Assert: apiMethodTracker is null.

apiMethodTracker is passed as an argument only for navigate() and reload() calls.

Let destinationKey be destination's entry's key.

Assert: destinationKey is not the empty string.

If navigation's upcoming traverse API method trackers[destinationKey] exists:

Set apiMethodTracker to navigation's upcoming traverse API method trackers[destinationKey].

Remove navigation's upcoming traverse API method trackers[destinationKey].

If apiMethodTracker is null:

Let info be undefined.

Let serializedState be null.

Set apiMethodTracker to the result of setting up a navigate/reload API method tracker for this given info and serializedState.

Set navigation's ongoing API method tracker to apiMethodTracker.

Set apiMethodTracker's pending to false.

Let navigable be navigation's relevant global object's navigable.

Let document be navigation's relevant global object's associated Document.

If document can have its URL rewritten to destination's URL, and either destination's is same document is true or navigationType is not "traverse", then initialize event's canIntercept to true. Otherwise, initialize it to false.

Let traverseCanBeCanceled be true if all of the following are true:

navigable is a top-level traversable;

destination's is same document is true; and

either userInvolvement is not "browser UI", or navigation's relevant global object has history-action activation.

Otherwise, let it be false.

If either:

navigationType is not "traverse"; or

traverseCanBeCanceled is true,

then initialize event's cancelable to true. Otherwise, initialize it to false.

Initialize event's type to "navigate".

Initialize event's navigationType to navigationType.

Initialize event's destination to destination.

Initialize event's downloadRequest to downloadRequestFilename.

Initialize event's info to apiMethodTracker's info.

At this point apiMethodTracker's info is no longer needed and can be nulled out instead of keeping it alive for the lifetime of the navigation API method tracker.

Initialize event's hasUAVisualTransition to true if a visual transition, to display a cached rendered state of the document's latest entry, was done by the user agent. Otherwise, initialize it to false.

Initialize event's sourceElement to sourceElement.

Set event's abort controller to a new AbortController created in navigation's relevant realm.

Initialize event's signal to event's abort controller's signal.

Let currentURL be document's URL.

If all of the following are true:

event's classic history API state is null;

destination's is same document is true;

destination's URL equals currentURL with exclude fragments set to true; and

destination's URL's fragment is not identical to currentURL's fragment,

then initialize event's hashChange to true. Otherwise, initialize it to false.

The first condition here means that hashChange will be true for fragment navigations, but false for cases like history.pushState(undefined, "", "#fragment").

If userInvolvement is not "none", then initialize event's userInitiated to true. Otherwise, initialize it to false.

If formDataEntryList is not null, then initialize event's formData to a new FormData created in navigation's relevant realm, associated to formDataEntryList. Otherwise, initialize it to null.

Assert: navigation's ongoing navigate event is null.

Set navigation's ongoing navigate event to event.

Set navigation's focus changed during ongoing navigation to false.

Set navigation's suppress normal scroll restoration during ongoing navigation to false.

Let dispatchResult be the result of dispatching event at navigation.

If dispatchResult is false:

If navigationType is "traverse", then consume history-action user activation given navigation's relevant global object.

If event's abort controller's signal is not aborted, then abort the ongoing navigation given navigation.

Return false.

If event's interception state is not "none":

Let fromNHE be the current entry of navigation.

Assert: fromNHE is not null.

Set navigation's transition to a new NavigationTransition created in navigation's relevant realm, with

navigation type
navigationType
from entry
fromNHE
destination
event's destination
committed promise
a new promise created in navigation's relevant realm
finished promise
a new promise created in navigation's relevant realm

Mark as handled navigation's transition's finished promise.

See the discussion about other finished promises to understand why this is done.

Mark as handled navigation's transition's committed promise.

If event's navigation precommit handler list is empty then commit event given apiMethodTracker.

Otherwise:

Let precommitController be a new NavigationPrecommitController created in navigation's relevant realm, whose event is event.

Let precommitPromisesList be an empty list.

For each handler of event's navigation precommit handler list:

Append the result of invoking handler with « precommitController » to precommitPromisesList.

Wait for all precommitPromisesList with the following success steps: commit event given apiMethodTracker, and the following failure step given reason: process navigate event handler failure given event and reason.

If event's interception state is "none", then return true.

Return false.

To commit a navigate event given a NavigateEvent object event and a navigation API method tracker apiMethodTracker:

Let navigation be event's target.

Let navigable be event's relevant global object's navigable.

If event's relevant global object's associated Document is not fully active, then return.

If event's abort controller's signal is aborted, then return.

Let endResultIsSameDocument be true if event's interception state is not "none" or event's destination's is same document is true.

Prepare to run script given navigation's relevant settings object.

This is done to avoid the JavaScript execution context stack becoming empty right after any currententrychange event handlers run as a result of the URL and history update steps that could soon happen. If the stack were to become empty at that time, then it would immediately perform a microtask checkpoint, causing various promise fulfillment handlers to run interleaved with the event handlers and before any handlers passed to navigateEvent.intercept(). This is undesirable since it means promise handler ordering vs. currententrychange event handler ordering vs. intercept() handler ordering would be dependent on whether the navigation is happening with an empty JavaScript execution context stack (e.g., because the navigation was user-initiated) or with a nonempty one (e.g., because the navigation was caused by a JavaScript API call).

By inserting an otherwise-unnecessary JavaScript execution context onto the stack in this step, we essentially suppress the perform a microtask checkpoint algorithm until later, thus ensuring that the sequence is always: currententrychange event handlers, then intercept() handlers, then promise handlers.

If event's interception state is not "none":

Set event's interception state to "committed".

Switch on event's navigationType:

"push"
"replace"

Run the URL and history update steps given event's relevant global object's associated Document and event's destination's URL, with serializedData set to event's classic history API state and historyHandling set to event's navigationType.

"reload"

Update the navigation API entries for a same-document navigation given navigation, navigable's active session history entry, and "reload".

"traverse"

Set navigation's suppress normal scroll restoration during ongoing navigation to true.

If event's scroll behavior was set to "after-transition", then scroll restoration will happen as part of finishing the relevant NavigateEvent. Otherwise, there will be no scroll restoration. That is, no navigation which is intercepted by intercept() goes through the normal scroll restoration process; scroll restoration for such navigations is either done manually, by the web developer, or is done after the transition.

Let userInvolvement be "none".

If event's userInitiated is true, then set userInvolvement to "activation".

At this point after interception, it is not consequential whether the activation was a result of browser UI.

Append the following session history traversal steps to navigable's traversable navigable:

Resume applying the traverse history step given event's destination's entry's session history entry's step, navigable's traversable navigable, and userInvolvement.

If navigation's transition is not null, then resolve navigation's transition's committed promise with undefined.

If endResultIsSameDocument is true:

Let promisesList be an empty list.

Append apiMethodTracker's committed promise to promisesList.

For each handler of event's navigation handler list:

Append the result of invoking handler with an empty arguments list to promisesList.

Wait for all of promisesList, with the following success steps:

If event's relevant global object is not fully active, then abort these steps.

If event's abort controller's signal is aborted, then abort these steps.

Assert: event equals navigation's ongoing navigate event.

Set navigation's ongoing navigate event to null.

Finish event given true.

Resolve the finished promise for apiMethodTracker.

Fire an event named navigatesuccess at navigation.

If navigation's transition is not null, then resolve navigation's transition's finished promise with undefined.

Set navigation's transition to null.

and the following failure step given reason: process navigate event handler failure given event and reason.

Otherwise, clean up apiMethodTracker.

Clean up after running script given navigation's relevant settings object.

Per the previous note, this stops suppressing any potential promise handler microtasks, causing them to run at this point or later.

To process navigate event handler failure given a NavigateEvent object event and a reason:

If event's relevant global object's associated Document is not fully active, then return.

If event's abort controller's signal is aborted, then return.

Assert: event is event's relevant global object's navigation API's ongoing navigate event.

If event's interception state is not "intercepted", then finish event given false.

Abort event given reason.

7.2.6.10.5 Scroll and focus behavior

By calling navigateEvent.intercept(), web developers can suppress the normal scroll and focus behavior for same-document navigations, instead invoking cross-document navigation-like behavior at a later time. The algorithms in this section are called at those appropriate later points.

To finish a NavigateEvent event, given a boolean didFulfill:

Assert: event's interception state is not "finished".

If event's interception state is "intercepted", then:

Assert: didFulfill is false.

Assert: event's navigation precommit handler list is not empty.

Only precommit handlers can cancel a navigation before it is committed.

Set event's interception state to "finished".

Return.

If event's interception state is "none", then return.

Potentially reset the focus given event.

If didFulfill is true, then potentially process scroll behavior given event.

Set event's interception state to "finished".

To potentially reset the focus given a NavigateEvent event:

Assert: event's interception state is "committed" or "scrolled".

Let navigation be event's relevant global object's navigation API.

Let focusChanged be navigation's focus changed during ongoing navigation.

Set navigation's focus changed during ongoing navigation to false.

If focusChanged is true, then return.

If event's focus reset behavior is "manual", then return.

If it was left as null, then we treat that as "after-transition", and continue onward.

Let document be event's relevant global object's associated Document.

Let focusTarget be the autofocus delegate for document.

If focusTarget is null, then set focusTarget to document's body element.

If focusTarget is null, then set focusTarget to document's document element.

Run the focusing steps for focusTarget, with document's viewport as the fallback target.

Move the sequential focus navigation starting point to focusTarget.

To potentially process scroll behavior given a NavigateEvent event:

Assert: event's interception state is "committed" or "scrolled".

If event's interception state is "scrolled", then return.

If event's scroll behavior is "manual", then return.

If it was left as null, then we treat that as "after-transition", and continue onward.

Process scroll behavior given event.

To process scroll behavior given a NavigateEvent event:

Assert: event's interception state is "committed".

Set event's interception state to "scrolled".

If event's navigationType was initialized to "traverse" or "reload", then restore scroll position data given event's relevant global object's navigable's active session history entry.

Otherwise:

Let document be event's relevant global object's associated Document.

If document's indicated part is null, then scroll to the beginning of the document given document. [CSSOMVIEW]

Otherwise, scroll to the fragment given document.

7.2.7 Event interfaces

The NavigateEvent interface has its own dedicated section, due to its complexity.

7.2.7.1 The NavigationCurrentEntryChangeEvent interface
[Exposed=Window]
interface NavigationCurrentEntryChangeEvent : Event {
  constructor(DOMString type, NavigationCurrentEntryChangeEventInit eventInitDict);

  readonly attribute NavigationType? navigationType;
  readonly attribute NavigationHistoryEntry from;
};

dictionary NavigationCurrentEntryChangeEventInit : EventInit {
  NavigationType? navigationType = null;
  required NavigationHistoryEntry from;
};
event.navigationType

Returns the type of navigation which caused the current entry to change, or null if the change is due to navigation.updateCurrentEntry().

event.from

Returns the previous value of navigation.currentEntry, before the current entry changed.

If navigationType is null or "reload", then this value will be the same as navigation.currentEntry. In that case, the event signifies that the contents of the entry changed, even if we did not move to a new entry or replace the current one.

The navigationType and from attributes must return the values they were initialized to.

7.2.7.2 The PopStateEvent interface
✔MDN
[Exposed=Window]
interface PopStateEvent : Event {
  constructor(DOMString type, optional PopStateEventInit eventInitDict = {});

  readonly attribute any state;
  readonly attribute boolean hasUAVisualTransition;
};

dictionary PopStateEventInit : EventInit {
  any state = null;
  boolean hasUAVisualTransition = false;
};
event.state
✔MDN

Returns a copy of the information that was provided to pushState() or replaceState().

event.hasUAVisualTransition

Returns true if the user agent performed a visual transition for this navigation before dispatching this event. If true, the best user experience will be given if the author synchronously updates the DOM to the post-navigation state.

The state attribute must return the value it was initialized to. It represents the context information for the event, or null, if the state represented is the initial state of the Document.

The hasUAVisualTransition attribute must return the value it was initialized to.

7.2.7.3 The HashChangeEvent interface
✔MDN
[Exposed=Window]
interface HashChangeEvent : Event {
  constructor(DOMString type, optional HashChangeEventInit eventInitDict = {});

  readonly attribute USVString oldURL;
  readonly attribute USVString newURL;
};

dictionary HashChangeEventInit : EventInit {
  USVString oldURL = "";
  USVString newURL = "";
};
event.oldURL
✔MDN

Returns the URL of the session history entry that was previously current.

event.newURL
✔MDN

Returns the URL of the session history entry that is now current.

The oldURL attribute must return the value it was initialized to. It represents context information for the event, specifically the URL of the session history entry that was traversed from.

The newURL attribute must return the value it was initialized to. It represents context information for the event, specifically the URL of the session history entry that was traversed to.

7.2.7.4 The PageSwapEvent interface
[Exposed=Window]
interface PageSwapEvent : Event {
  constructor(DOMString type, optional PageSwapEventInit eventInitDict = {});
  readonly attribute NavigationActivation? activation;
  readonly attribute ViewTransition? viewTransition;
};

dictionary PageSwapEventInit : EventInit {
  NavigationActivation? activation = null;
  ViewTransition? viewTransition = null;
};
event.activation

A NavigationActivation object representing the destination and type of the cross-document navigation. This would be null for cross-origin navigations.

event.activation.entry

A NavigationHistoryEntry, representing the Document that is about to become active.

event.activation.from

A NavigationHistoryEntry, equivalent to the value of the navigation.currentEntry property at the moment the event is fired.

event.activation.navigationType

One of "push", "replace", "reload", or "traverse", indicating what type of navigation that is about to result in a page swap.

event.viewTransition

Returns the ViewTransition object that represents an outbound cross-document view transition, if such transition is active when the event is fired. Otherwise, returns null.

The activation and viewTransition attributes must return the values they were initialized to.

7.2.7.5 The PageRevealEvent interface
[Exposed=Window]
interface PageRevealEvent : Event {
  constructor(DOMString type, optional PageRevealEventInit eventInitDict = {});
  readonly attribute ViewTransition? viewTransition;
};

dictionary PageRevealEventInit : EventInit {
  ViewTransition? viewTransition = null;
};
event.viewTransition

Returns the ViewTransition object that represents an inbound cross-document view transition, if such transition is active when the event is fired. Otherwise, returns null.

The viewTransition attribute must return the value it was initialized to.

7.2.7.6 The PageTransitionEvent interface
✔MDN
[Exposed=Window]
interface PageTransitionEvent : Event {
  constructor(DOMString type, optional PageTransitionEventInit eventInitDict = {});

  readonly attribute boolean persisted;
};

dictionary PageTransitionEventInit : EventInit {
  boolean persisted = false;
};
event.persisted
✔MDN

For the pageshow event, returns false if the page is newly being loaded (and the load event will fire). Otherwise, returns true.

For the pagehide event, returns false if the page is going away for the last time. Otherwise, returns true, meaning that the page might be reused if the user navigates back to this page (if the Document's salvageable state stays true).

Things that can cause the page to be unsalvageable include:

The user agent decided to not keep the Document alive in a session history entry after unload

Having iframes that are not salvageable

Active WebSocket objects

Aborting a Document

The persisted attribute must return the value it was initialized to. It represents the context information for the event.

To fire a page transition event named eventName at a Window window with a boolean persisted, fire an event named eventName at window, using PageTransitionEvent, with the persisted attribute initialized to persisted, the cancelable attribute initialized to true, the bubbles attribute initialized to true, and legacy target override flag set.

The values for cancelable and bubbles don't make any sense, since canceling the event does nothing and it's not possible to bubble past the Window object. They are set to true for historical reasons.

7.2.7.7 The BeforeUnloadEvent interface
✔MDN
[Exposed=Window]
interface BeforeUnloadEvent : Event {
  attribute DOMString returnValue;
};

There are no BeforeUnloadEvent-specific initialization methods.

The BeforeUnloadEvent interface is a legacy interface which allows checking if unloading is canceled to be controlled not only by canceling the event, but by setting the returnValue attribute to a value besides the empty string. Authors should use the preventDefault() method, or other means of canceling events, instead of using returnValue.

The returnValue attribute controls the process of checking if unloading is canceled. When the event is created, the attribute must be set to the empty string. On getting, it must return the last value it was set to. On setting, the attribute must be set to the new value.

This attribute is a DOMString only for historical reasons. Any value besides the empty string will be treated as a request to ask the user for confirmation.

7.2.8 The NotRestoredReasons interface
[Exposed=Window]
interface NotRestoredReasonDetails {
  readonly attribute DOMString reason;
  [Default] object toJSON();
};

[Exposed=Window]
interface NotRestoredReasons {
  readonly attribute USVString? src;
  readonly attribute DOMString? id;
  readonly attribute DOMString? name;
  readonly attribute USVString? url;
  readonly attribute FrozenArray<NotRestoredReasonDetails>? reasons;
  readonly attribute FrozenArray<NotRestoredReasons>? children;
  [Default] object toJSON();
};
notRestoredReasonDetails.reason

Returns a string that explains the reason that prevented the document from being served from back/forward cache. See the definition of bfcache blocking details for the possible string values.

notRestoredReasons.src

Returns the src attribute of the document's node navigable's container if it is an iframe element. This can be null if not set or if it is not an iframe element.

notRestoredReasons.id

Returns the id attribute of the document's node navigable's container if it is an iframe element. This can be null if not set or if it is not an iframe element.

notRestoredReasons.name

Returns the name attribute of the document's node navigable's container if it is an iframe element. This can be null if not set or if it is not an iframe element.

notRestoredReasons.url

Returns the document's URL, or null if the document is in a cross-origin iframe. This is reported in addition to src because it is possible iframe navigated since the original src was set.

notRestoredReasons.reasons

Returns an array of NotRestoredReasonDetails for the document. This is null if the document is in a cross-origin iframe.

notRestoredReasons.children

Returns an array of NotRestoredReasons that are for the document’s children. This is null if the document is in a cross-origin iframe.

A NotRestoredReasonDetails object has a backing struct, a not restored reason details or null, initially null.

The reason getter steps are to return this's backing struct's reason.

To create a NotRestoredReasonDetails object given a not restored reason details backingStruct and a realm realm:

Let notRestoredReasonDetails be a new NotRestoredReasonDetails object created in realm.

Set notRestoredReasonDetails's backing struct to backingStruct.

Return notRestoredReasonDetails.

A not restored reason details is a struct with the following items:

reason, a string, initially empty.

The reason is a string that represents the reason that prevented the page from being restored from back/forward cache. The string is one of the following:

"fetch"
While unloading, a fetch initiated by this Document was still ongoing and was canceled, so the page was not in a state that could be stored in the back/forward cache.
"navigation-failure"
The original navigation that created this Document errored, so storing the resulting error document in the back/forward cache was prevented.
"parser-aborted"
The Document never finished its initial HTML parsing, so storing the unfinished document in the back/forward cache was prevented.
"websocket"
While unloading, an open WebSocket connection was shut down, so the page was not in a state that could be stored in the back/forward cache. [WEBSOCKETS]
"lock"
While unloading, held locks and lock requests were terminated, so the page was not in a state that could be stored in the back/forward cache. [WEBLOCKS]
"masked"
This Document has children that are in a cross-origin iframe, and they prevented back/forward cache; or this Document could not be back/forward cached for user agent-specific reasons, and the user agent has chosen not to use one of the more specific reasons from the list of user-agent specific blocking reasons.

In addition to the list above, a user agent might choose to expose a reason that prevented the page from being restored from back/forward cache for user-agent specific blocking reasons. These are one of the following strings:

"audio-capture"
The Document requested audio capture permission by using Media Capture and Streams's getUserMedia() with audio. [MEDIASTREAM]
"background-work"
The Document requested background work by calling SyncManager's register() method, PeriodicSyncManager's register() method, or BackgroundFetchManager's fetch() method.
"broadcastchannel-message"
While the page was stored in back/forward cache, a BroadcastChannel connection on the page received a message and message event was fired.
"idbversionchangeevent"
The Document had a pending IDBVersionChangeEvent while unloading. [INDEXEDDB]
"idledetector"
The Document had an active IdleDetector while unloading.
"keyboardlock"
While unloading, keyboard lock was still active because Keyboard's lock() method was called.
"mediastream"
A MediaStreamTrack was in the live state upon unloading. [MEDIASTREAM]
"midi"
The Document requested a MIDI permission by calling navigator.requestMIDIAccess().
"modals"
User prompts were shown while unloading.
"navigating"
While unloading, loading was still ongoing, and so the Document was not in a state that could be stored in back/forward cache.
"navigation-canceled"
The navigation request was canceled by calling window.stop() and the page was not in a state to be stored in back/forward cache.
"non-trivial-browsing-context-group"
The browsing context group of this Document had more than one top-level browsing context.
"otpcredential"
The Document created an OTPCredential.
"outstanding-network-request"
While unloading, the Document had outstanding network requests and was not in a state that could be stored in back/forward cache.
"paymentrequest"
The Document had an active PaymentRequest while unloading. [PAYMENTREQUEST]
"pictureinpicturewindow"
The Document had an active PictureInPictureWindow while unloading. [PICTUREINPICTURE]
"plugins"
The Document contained plugins.
"request-method-not-get"
The Document was created from an HTTP request whose method was not `GET`. [FETCH]
"response-auth-required"
The Document was created from an HTTP response that required HTTP authentication.
"response-cache-control-no-store"
The Document was created from an HTTP response whose `Cache-Control` header included the "no-store" token. [HTTP]
"response-cache-control-no-cache"
The Document was created from an HTTP response whose `Cache-Control` header included the "no-cache" token. [HTTP]
"response-keep-alive"
The Document was created from an HTTP response that contained a `Keep-Alive` header.
"response-scheme-not-http-or-https"
The Document was created from a response whose URL's scheme was not an HTTP(S) scheme. [FETCH]
"response-status-not-ok"
The Document was created from an HTTP response whose status was not an ok status. [FETCH]
"rtc"
While unloading, a RTCPeerConnection or RTCDataChannel was shut down, so the page was not in a state that could be stored in the back/forward cache. [WEBRTC]
"rtc-used-with-cache-control-no-store"
The Document was created from an HTTP response whose `Cache-Control` header included the "no-store" token, and it has created a RTCPeerConnection or RTCDataChannel which might be used to receive sensitive information, so the page was not in a state that could be stored in the back/forward cache. [HTTP] [WEBRTC]
"sensors"
The Document requested sensor access.
"serviceworker-added"
The Document's service worker client started to be controlled by a ServiceWorker while the page was in back/forward cache. [SW]
"serviceworker-claimed"
The Document's service worker client's active service worker was claimed while the page was in back/forward cache. [SW]
"serviceworker-postmessage"
The Document's service worker client's active service worker received a message while the page was in back/forward cache. [SW]
"serviceworker-version-activated"
The Document's service worker client's active service worker's version was activated while the page was in back/forward cache. [SW]
"serviceworker-unregistered"
The Document's service worker client's active service worker's service worker registration was unregistered while the page was in back/forward cache. [SW]
"sharedworker"
This Document was in the owner set of a SharedWorkerGlobalScope.

User agents that support the back/forward cache for documents using shared workers can use more specific reasons such as "sharedworker-message" or "sharedworker-with-no-active-client" instead of this general reason, since the usage of shared workers itself is supported outside of the cases described in those reasons.

"sharedworker-message"
While the page was stored in back/forward cache, a message was received from a SharedWorkerGlobalScope whose owner set contains this Document.
"sharedworker-with-no-active-client"
This Document was in the owner set of a SharedWorkerGlobalScope that is not actively needed.
"smartcardconnection"
The Document had an active SmartCardConnection while unloading.
"speechrecognition"
The Document had an active SpeechRecognition while unloading.
"storageaccess"
The Document requested storage access permission by using the Storage Access API.
"unload-listener"
The Document registered an event listener for the unload event.
"video-capture"
The Document requested video capture permission by using Media Capture and Streams's getUserMedia() with video. [MEDIASTREAM]
"webhid"
The Document called the WebHID API's requestDevice() method.
"webshare"
The Document used the Web Share API's navigator.share() method.
"websocket-used-with-cache-control-no-store"
The Document was created from an HTTP response whose `Cache-Control` header included the "no-store" token, and it has created a WebSocket connection which might be used to receive sensitive information, so the page was not in a state that could be stored in the back/forward cache. [HTTP] [WEBSOCKETS]
"webtransport"
While unloading, an open WebTransport connection was shut down, so the page was not in a state that could be stored in the back/forward cache. [WEBTRANSPORT]
"webtransport-used-with-cache-control-no-store"
The Document was created from an HTTP response whose `Cache-Control` header included the "no-store" token, and it has created a WebTransport connection which might be used to receive sensitive information, so the page was not in a state that could be stored in the back/forward cache. [HTTP] [WEBTRANSPORT]
"webxrdevice"
The Document created a XRSystem.

A NotRestoredReasons object has a backing struct, a not restored reasons or null, initially null.

A NotRestoredReasons object has a reasons array, a FrozenArray<NotRestoredReasonDetails> or null, initially null.

A NotRestoredReasons object has a children array, a FrozenArray<NotRestoredReasons> or null, initially null.

The src getter steps are to return this's backing struct's src.

The id getter steps are to return this's backing struct's id.

The name getter steps are to return this's backing struct's name.

The url getter steps are:

If this's backing struct's URL is null, then return null.

Return this's backing struct's URL, serialized.

The reasons getter steps are to return this's reasons array.

The children getter steps are to return this's children array.

To create a NotRestoredReasons object given a not restored reasons backingStruct and a realm realm:

Let notRestoredReasons be a new NotRestoredReasons object created in realm.

Set notRestoredReasons's backing struct to backingStruct.

If backingStruct's reasons is null, set notRestoredReasons's reasons array to null.

Otherwise:

Let reasonsArray be an empty list.

For each reason of backingStruct's reasons:

Create a NotRestoredReasonDetails object given reason and realm, and append it to reasonsArray.

Set notRestoredReasons's reasons array to the result of creating a frozen array given reasonsArray.

If backingStruct's children is null, set notRestoredReasons's children array to null.

Otherwise:

Let childrenArray be an empty list.

For each child of backingStruct's children:

Create a NotRestoredReasons object given child and realm and append it to childrenArray.

Set notRestoredReasons's children array to the result of creating a frozen array given childrenArray.

Return notRestoredReasons.

A not restored reasons is a struct with the following items:

src, a scalar value string or null, initially null.

id, a string or null, initially null.

name, a string or null, initially null.

url, a URL or null, initially null.

reasons, null or a list of not restored reason details, initially null.

children, null or a list of not restored reasons, initially null.

A Document's not restored reasons is its node navigable's active session history entry's document state's not restored reasons, if Document's node navigable is a top-level traversable; otherwise null.

← 7 Loading web pages — Table of Contents — 7.3 Infrastructure for sequences of documents →
