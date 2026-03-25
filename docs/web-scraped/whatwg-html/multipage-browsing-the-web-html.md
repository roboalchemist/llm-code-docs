# Source: https://html.spec.whatwg.org/multipage/browsing-the-web.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/browsing-the-web.html

Published Time: Mon, 16 Mar 2026 07:32:48 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 7.3 Infrastructure for sequences of documents](https://html.spec.whatwg.org/multipage/document-sequences.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [7.5 Document lifecycle →](https://html.spec.whatwg.org/multipage/document-lifecycle.html)
1.       1.   [7.4 Navigation and session history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-and-session-history)
        1.   [7.4.1 Session history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-infrastructure)
            1.   [7.4.1.1 Session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entries)
            2.   [7.4.1.2 Document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state)
            3.   [7.4.1.3 Centralized modifications of session history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#centralized-modifications-of-session-history)
            4.   [7.4.1.4 Low-level operations on session history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#low-level-operations-on-session-history)

        2.   [7.4.2 Navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigating-across-documents)
            1.   [7.4.2.1 Supporting concepts](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-supporting-concepts)
            2.   [7.4.2.2 Beginning navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#beginning-navigation)
            3.   [7.4.2.3 Ending navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ending-navigation)
                1.   [7.4.2.3.1 The usual cross-document navigation case](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-usual-cross-document-navigation-case)
                2.   [7.4.2.3.2 The `javascript:` URL special case](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-javascript:-url-special-case)
                3.   [7.4.2.3.3 Fragment navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scroll-to-fragid)
                4.   [7.4.2.3.4 Non-fetch schemes and external software](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-schemes-and-external-software)

            4.   [7.4.2.4 Preventing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#preventing-navigation)
            5.   [7.4.2.5 Aborting navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#aborting-navigation)

        3.   [7.4.3 Reloading and traversing](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reloading-and-traversing)
        4.   [7.4.4 Non-fragment synchronous "navigations"](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-non-frag-sync)
        5.   [7.4.5 Populating a session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#populating-a-session-history-entry)
        6.   [7.4.6 Applying the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#applying-the-history-step)
            1.   [7.4.6.1 Updating the traversable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#updating-the-traversable)
            2.   [7.4.6.2 Updating the document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#updating-the-document)
            3.   [7.4.6.3 Revealing the document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#revealing-the-document)
            4.   [7.4.6.4 Scrolling to a fragment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scrolling-to-a-fragment)
            5.   [7.4.6.5 Persisted history entry state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#persisted-user-state-restoration)

### 7.4 Navigation and session history[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-and-session-history)

Welcome to the dragon's maw. Navigation, session history, and the traversal through that session history are some of the most complex parts of this standard.

The basic concept may not seem so difficult:

*   The user is looking at a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) that is presenting its [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document). They [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) it to another [URL](https://url.spec.whatwg.org/#concept-url).

*   The browser fetches the given URL from the network, using it to [populate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-the-history-entry's-document) a new [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) with a newly-[created](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object)`Document`.

*   The browser updates the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)'s [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) to the newly-populated one, and thus updates the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) that it is showing to the user.

*   At some point later, the user [presses the browser back button](https://html.spec.whatwg.org/multipage/browsing-the-web.html#traverse-the-history-by-a-delta) to go back to the previous [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry).

*   The browser looks at the [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url) stored in that [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry), and uses it to re-fetch and [populate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-the-history-entry's-document) that entry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document).

*   The browser again updates the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)'s [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry).

You can see some of the intertwined complexity peeking through here, in how traversal can cause a navigation (i.e., a network fetch to a stored URL), and how a navigation necessarily needs to interface with the session history list to ensure that when it finishes the user is looking at the right thing. But the real problems come in with the various edge cases and interacting web platform features:

*   [Child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) (e.g., those contained in `iframe`s) can also navigate and traverse, but those navigations need to be linearized into [a single session history list](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries) since the user only has a single back/forward interface for the entire [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable) (e.g., browser tab).

*   Since the user can traverse back more than a single step in the session history (e.g., by holding down their back button), they can end up traversing multiple [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) at the same time when [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) are involved. This needs to be synchronized across all of the involved navigables, which might involve multiple [event loops](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop) or even [agent clusters](https://tc39.es/ecma262/#sec-agent-clusters).

*   During navigation, servers can respond with 204 or 205 status codes or with ``Content-Disposition: attachment`` headers, which cause navigation to abort and the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) to stay on its original [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document). (This is much worse if it happens during a traversal-initiated navigation!)

*   Various other HTTP headers, such as ``Location``, ``Refresh``, ``X-Frame-Options``, and those for Content Security Policy, contribute to either the [fetching process](https://html.spec.whatwg.org/multipage/browsing-the-web.html#create-navigation-params-by-fetching), or the [`Document`-creation process](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object), or both. The ``Cross-Origin-Opener-Policy`` header even contributes to the [browsing context selection and creation](https://html.spec.whatwg.org/multipage/browsers.html#browsing-context-group-switches-due-to-cross-origin-opener-policy) process!

*   Some navigations (namely [fragment navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scroll-to-fragid) and [single-page app navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-non-frag-sync)) are synchronous, meaning that JavaScript code expects to observe the navigation's results instantly. This then needs to be synchronized with the view of the session history that all other [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) in the tree see, which can be subject to race conditions and necessitate resolving conflicting views of the session history.

*   The platform has accumulated various exciting navigation-related features that need special-casing, such as `javascript:` URLs, `srcdoc``iframe`s, and the `beforeunload` event.

In what follows, we have attempted to guide the reader through these complexities by appropriately cordoning them off into labeled sections and algorithms, and giving appropriate words of introduction where possible. Nevertheless, if you wish to truly understand navigation and session history, [the usual advice](https://html.spec.whatwg.org/multipage/introduction.html#how-to-read-this-specification) will be invaluable.

#### 7.4.1 Session history[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-infrastructure)

##### 7.4.1.1 Session history entries[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entries)

A session history entry is a [struct](https://infra.spec.whatwg.org/#struct) with the following [items](https://infra.spec.whatwg.org/#struct-item):

*   step, a non-negative integer or "`pending`", initially "`pending`".

*   URL, a [URL](https://url.spec.whatwg.org/#concept-url)

*   document state, a [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-2).

*   classic history API state, which is [serialized state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#serialized-state), initially [StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage)(null).

*   navigation API state, which is a [serialized state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#serialized-state), initially [StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage)(undefined).

*   navigation API key, which is a string, initially set to the result of [generating a random UUID](https://w3c.github.io/webcrypto/#dfn-generate-a-random-uuid).

*   navigation API ID, which is a string, initially set to the result of [generating a random UUID](https://w3c.github.io/webcrypto/#dfn-generate-a-random-uuid).

*   scroll restoration mode, a [scroll restoration mode](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scroll-restoration-mode), initially "`auto`".

*   scroll position data, which is scroll position data for the [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [restorable scrollable regions](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restorable-scrollable-regions).

*   persisted user state, which is [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined), initially null

For example, some user agents might want to persist the values of form controls.

User agents that persist the value of form controls are encouraged to also persist their directionality (the value of the element's `dir` attribute). This prevents values from being displayed incorrectly after a history traversal when the user had originally entered the values with an explicit, non-default directionality.

To get a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)'s document, return its [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document).

* * *

Serialized state is a serialization (via [StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage)) of an object representing a user interface state. We sometimes informally refer to "state objects", which are the objects representing user interface state supplied by the author, or alternately the objects created by deserializing (via [StructuredDeserialize](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize)) serialized state.

Pages can [add](https://html.spec.whatwg.org/multipage/nav-history-apis.html#dom-history-pushstate)[serialized state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#serialized-state) to the session history. These are then [deserialized](https://html.spec.whatwg.org/multipage/structured-data.html#structureddeserialize) and [returned to the script](https://html.spec.whatwg.org/multipage/indices.html#event-popstate) when the user (or script) goes back in the history, thus enabling authors to use the "navigation" metaphor even in one-page applications.

[Serialized state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#serialized-state) is intended to be used for two main purposes: first, storing a preparsed description of the state in the [URL](https://url.spec.whatwg.org/#concept-url) so that in the simple case an author doesn't have to do the parsing (though one would still need the parsing for handling [URLs](https://url.spec.whatwg.org/#concept-url) passed around by users, so it's only a minor optimization). Second, so that the author can store state that one wouldn't store in the URL because it only applies to the current `Document` instance and it would have to be reconstructed if a new `Document` were opened.

An example of the latter would be something like keeping track of the precise coordinate from which a popup `div` was made to animate, so that if the user goes back, it can be made to animate to the same location. Or alternatively, it could be used to keep a pointer into a cache of data that would be fetched from the server based on the information in the [URL](https://url.spec.whatwg.org/#concept-url), so that when going back and forward, the information doesn't have to be fetched again.

* * *

A scroll restoration mode indicates whether the user agent should restore the persisted scroll position (if any) when traversing to an [entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry). A scroll restoration mode is one of the following:

"`auto`"The user agent is responsible for restoring the scroll position upon navigation."`manual`"The page is responsible for restoring the scroll position and the user agent does not attempt to do so automatically
##### 7.4.1.2 Document state[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state)

Document state holds state inside a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) regarding how to present and, if necessary, recreate, a `Document`. It has:

*   A document, a `Document` or null, initially null.

When a history entry is [active](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry), it has a `Document` in its [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state). However, when a `Document` is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), it's possible for it to be [destroyed](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document) to free resources. In such cases, this [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) item will be nulled out. The [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url) and other data in the [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) and [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state) is then used to bring a new `Document` into being to take the place of the original, in the case where the user agent finds itself having to traverse to the entry.

If the `Document` is _not_[destroyed](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document), then during [history traversal](https://html.spec.whatwg.org/multipage/browsing-the-web.html#traverse-the-history-by-a-delta), it can be [reactivated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reactivate-a-document). The cache in which browsers store such `Document`s is often called a _back-forward cache_, or _bfcache_ (or perhaps ["blazingly fast"](https://bugzilla.mozilla.org/show_bug.cgi?id=274784) cache). 
*   A history policy container, a [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container) or null, initially null.

*   A request referrer, which is "`no-referrer`", "`client`", or a [URL](https://url.spec.whatwg.org/#concept-url), initially "`client`".

*   A request referrer policy, which is a [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy), initially the [default referrer policy](https://w3c.github.io/webappsec-referrer-policy/#default-referrer-policy).

The [request referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer-policy) is distinct from the [history policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-history-policy-container)'s [referrer policy](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-referrer-policy). The former is used for fetches _of_ this document, whereas the latter controls fetches _by_ this document.

*   An initiator origin, which is an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) or null, initially null.

*   An origin, which is an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) or null, initially null.

This is the origin that we set "`about:`"-schemed `Document`s' [origin](https://dom.spec.whatwg.org/#concept-document-origin) to. We store it here because it is also used when restoring these `Document`s during traversal, since they are reconstructed locally without visiting the network. It is also used to compare the origin before and after the [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) is [repopulated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-the-history-entry's-document). If the origins change, the [navigable target name](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nav-target-name) is cleared.

*   An about base URL, which is a [URL](https://url.spec.whatwg.org/#concept-url) or null, initially null.

This will be populated only for "`about:`"-schemed `Document`s and will be the [fallback base URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#fallback-base-url) for those `Document`s. It is a snapshot of the initiator `Document`'s [document base URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-url).

*   Nested histories, a [list](https://infra.spec.whatwg.org/#list) of [nested histories](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history), initially an empty [list](https://infra.spec.whatwg.org/#list).

*   A resource, a string, [POST resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#post-resource) or null, initially null.

A string is treated as HTML. It's used to store the source of an [`iframe``srcdoc` document](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#an-iframe-srcdoc-document).

*   A reload pending boolean, initially false.

*   An ever populated boolean, initially false.

*   A navigable target name string, initially the empty string.

*   A not restored reasons, a [not restored reasons](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-struct) or null, initially null.

User agents may [destroy a document and its descendants](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document-and-its-descendants) given the [documents](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) of [document states](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-2) with non-null [documents](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document), as long as the `Document` is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active).

Apart from that restriction, this standard does not specify when user agents should destroy the [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) stored in a [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-2), versus keeping it cached.

* * *

A POST resource has:

*   A request body, a [byte sequence](https://infra.spec.whatwg.org/#byte-sequence) or failure.

This is only ever accessed [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel), so it doesn't need to be stored in memory. However, it must return the same [byte sequence](https://infra.spec.whatwg.org/#byte-sequence) each time. If this isn't possible due to resources changing on disk, or if resources can no longer be accessed, then this must be set to failure.

*   A request content-type, which is ``application/x-www-form-urlencoded``, ``multipart/form-data``, or ``text/plain``.

* * *

A nested history has:

*   An id, a [unique internal value](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#unique-internal-value).

This is used to associate the [nested history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history) with a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable).

*   Entries, a [list](https://infra.spec.whatwg.org/#list) of [session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry).

This will later contain ways to identify a child navigable across reloads.

* * *

* * *

Several contiguous entries in a session history can share the same [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state). This can occur when the initial entry is reached via normal [navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate), and the following entry is added via `history.pushState()`. Or it can occur via [navigation to a fragment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-fragid).

All entries that share the same [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state) (and that are therefore merely different states of one particular document) are contiguous by construction.

* * *

A `Document` has a latest entry, a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) or null.

This is the entry that was most recently represented by a given `Document`. A single `Document` can represent many [session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) over time, as many contiguous [session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) can share the same [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state) as explained above.

##### 7.4.1.3 Centralized modifications of session history[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#centralized-modifications-of-session-history)

To maintain a single source of truth, all modifications to a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)'s [session history entries](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries) need to be synchronized. This is especially important due to how session history is influenced by all of the descendant [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable), and thus by multiple [event loops](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop). To accomplish this, we use the [session history traversal parallel queue](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue) structure.

A session history traversal parallel queue is very similar to a [parallel queue](https://html.spec.whatwg.org/multipage/infrastructure.html#parallel-queue). It has an algorithm set, an [ordered set](https://infra.spec.whatwg.org/#ordered-set).

The [items](https://infra.spec.whatwg.org/#list-item) in a [session history traversal parallel queue](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue)'s [algorithm set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-algorithm-set) are either algorithm steps, or synchronous navigation steps, which are a particular brand of algorithm steps involving a target navigable (a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)).

To start a new session history traversal parallel queue:

1.   Let sessionHistoryTraversalQueue be a new [session history traversal parallel queue](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue).

2.   Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

    1.   While true:

        1.   If sessionHistoryTraversalQueue's [algorithm set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-algorithm-set) is empty, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

        2.   Let steps be the result of [dequeuing](https://infra.spec.whatwg.org/#queue-dequeue) from sessionHistoryTraversalQueue's [algorithm set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-algorithm-set).

        3.   Run steps.

3.   Return sessionHistoryTraversalQueue.

[Synchronous navigation steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-sync-nav-steps) are tagged in the [algorithm set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-algorithm-set) to allow them to conditionally "jump the queue". This is handled [within apply the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#sync-navigations-jump-queue).

Imagine the joint session history depicted by this [Jake diagram](https://html.spec.whatwg.org/multipage/document-sequences.html#jake-diagram):

|  | 0 | 1 |
| --- | --- |
| `top` | /a | /b |

And the following code runs at the top level:

```
history.back();
location.href = '#foo';
```

The desired result is:

|  | 0 | 1 | 2 |
| --- | --- | --- |
| `top` | /a | /b | /b#foo |

This isn't straightforward, as the sync navigation wins the race in terms of being observable, whereas the traversal wins the race in terms of queuing steps on the [session history traversal parallel queue](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue). To achieve this result, the following happens:

1.   `history.back()`[appends steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-traversal-steps) intended to traverse by a delta of −1.

2.   `location.href = '#foo'` synchronously changes the [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) entry to a newly-created one, with the URL `/b#foo`, and [appends synchronous steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-sync-nav-steps) to notify the central source of truth about that new entry. Note that this does _not_ yet update the [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry), [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step), or the [session history entries](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries) list; those updates cannot be done synchronously, and instead must be done as part of the queued steps.

3.   On the [session history traversal parallel queue](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue), the steps queued by `history.back()` run:

    1.   The target history step is determined to be 0: the [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) (i.e., 1) plus the intended delta of −1.

    2.   We enter the main [apply the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step) algorithm.

The entry at step 0, for the `/a` URL, has its [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)[populated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-the-history-entry's-document).

Meanwhile, the queue is checked for [synchronous navigation steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-sync-nav-steps). The steps queued by the `location.href` setter now run, and block the traversal from performing effects beyond document population (such as, unloading documents and switching active history entries) until they are finished. Those steps cause the following to happen:

        1.   The entry with URL `/b#foo` is added, with its [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) determined to be 2: the [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) (i.e., 1) plus 1.

        2.   We fully switch to that newly added entry, including a nested call to [apply the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step). This ultimately results in [updating the document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#update-document-for-history-step-application) by dispatching events like `hashchange`.

Only once that is all complete, and the `/a` history entry has been fully populated with a [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document), do we move on with applying the history step given the target step of 0.

At this point, the `Document` with URL `/b#foo`[unloads](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-a-document), and we finish moving to our target history step 0, which makes the entry with URL `/a` become the [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) and 0 become the [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step).

Here is another more complex example, involving races between populating two different `iframe`s, and a synchronous navigation once one of those iframes loads. We start with this setup:

|  | 0 | 1 | 2 |
| --- | --- | --- |
| `top` | /t |
| `frames[0]` | /i-0-a | /i-0-b |
| `frames[1]` | /i-1-a | /i-1-b |

and then call `history.go(-2)`. The following then occurs:

1.   `history.go(-2)`[appends steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-traversal-steps) intended to traverse by a delta of −2. Once those steps run:

    1.   The target step is determined to be 2 + (−2) = 0.

    2.   In parallel, the fetches are made to [populate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-the-history-entry's-document) the two iframes, fetching `/i-0-a` and `/i-1-a` respectively.

Meanwhile, the queue is checked for [synchronous navigation steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-sync-nav-steps). There aren't any right now.

    3.   In the fetch race, the fetch for `/i-0-a` wins. We proceed onward to finish all of [apply the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step)'s work for how the traversal impacts the `frames[0]`[navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable), including updating its [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) to the entry with URL `/i-0-a`.

    4.   Before the fetch for `/i-1-a` finishes, we reach the point where [scripts may run for the newly-created document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scripts-may-run-for-the-newly-created-document) in the `frames[0]`[navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document). Some such script does run:

`location.href = '#foo'`
This synchronously changes the `frames[0]` navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) entry to a newly-created one, with the URL `/i-0-a#foo`, and [appends synchronous steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-sync-nav-steps) to notify the central source of truth about that new entry.

Unlike in the [previous example](https://html.spec.whatwg.org/multipage/browsing-the-web.html#example-sync-navigation-steps-queue-jumping-basic), these synchronous steps do _not_ "jump the queue" and update the [traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable) before we finish the fetch for `/i-1-a`. This is because the navigable in question, `frames[0]`, has already been altered as part of the traversal, so we know that with the [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) being 2, adding the new entry as a step 3 doesn't make sense.

    5.   Once the fetch for `/i-1-a` finally finishes, we proceed to finish updating the `frames[1]`[navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) for the traversal, including updating its [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) to the entry with URL `/i-1-a`.

    6.   Now that both navigables have finished processing the traversal, we update the [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) to the target step of 0.

2.   Now we can process the steps that were queued for the synchronous navigation:

    1.   The `/i-0-a#foo` entry is added, with its [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) determined to be 1: the [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) (i.e., 0) plus 1. This also [clears existing forward history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#clear-the-forward-session-history).

    2.   We fully switch to that newly added entry, including calling [apply the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step). This ultimately results in [updating the document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#update-document-for-history-step-application) by dispatching events like `hashchange`, as well as updating the [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) to the target step of 1.

The end result is:

|  | 0 | 1 |
| --- | --- |
| `top` | /t |
| `frames[0]` | /i-0-a | /i-0-a#foo |
| `frames[1]` | /i-1-a |

##### 7.4.1.4 Low-level operations on session history[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#low-level-operations-on-session-history)

This section contains a miscellaneous grab-bag of operations that we perform throughout the standard when manipulating session history. The best way to get a sense of what they do is to look at their call sites.

To get session history entries of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable:

1.   Let traversable be navigable's [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable).

2.   [Assert](https://infra.spec.whatwg.org/#assert): this is running within traversable's [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue).

3.   If navigable is traversable, return traversable's [session history entries](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries).

4.   Let docStates be an empty [ordered set](https://infra.spec.whatwg.org/#ordered-set) of [document states](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-2).

5.   For each entry of traversable's [session history entries](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries), [append](https://infra.spec.whatwg.org/#set-append)entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state) to docStates.

6.   [For each](https://infra.spec.whatwg.org/#list-iterate)docState of docStates:

    1.   [For each](https://infra.spec.whatwg.org/#list-iterate)nestedHistory of docState's [nested histories](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nested-histories):

        1.   If nestedHistory's [id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history-id) equals navigable's [id](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-id), return nestedHistory's [entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history-entries).

        2.   For each entry of nestedHistory's [entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history-entries), [append](https://infra.spec.whatwg.org/#set-append)entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state) to docStates.

7.   [Assert](https://infra.spec.whatwg.org/#assert): this step is not reached.

To get session history entries for the navigation API of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable given an integer targetStep:

1.   Let rawEntries be the result of [getting session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-session-history-entries) for navigable.

2.   Let entriesForNavigationAPI be a new empty [list](https://infra.spec.whatwg.org/#list).

3.   Let startingIndex be the index of the [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) in rawEntries who has the greatest [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) less than or equal to targetStep.

See [this example](https://html.spec.whatwg.org/multipage/browsing-the-web.html#example-getting-the-target-history-entry) to understand why it's the greatest step less than or equal to targetStep.

4.   [Append](https://infra.spec.whatwg.org/#list-append)rawEntries[startingIndex] to entriesForNavigationAPI.

5.   Let startingOrigin be rawEntries[startingIndex]'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin).

6.   Let i be startingIndex − 1.

7.   While i> 0:

    1.   If rawEntries[i]'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin) is not [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with startingOrigin, then [break](https://infra.spec.whatwg.org/#iteration-break).

    2.   [Prepend](https://infra.spec.whatwg.org/#list-prepend)rawEntries[i] to entriesForNavigationAPI.

    3.   Set i to i − 1.

8.   Set i to startingIndex + 1.

9.   While i<rawEntries's [size](https://infra.spec.whatwg.org/#list-size):

    1.   If rawEntries[i]'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin) is not [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with startingOrigin, then [break](https://infra.spec.whatwg.org/#iteration-break).

    2.   [Append](https://infra.spec.whatwg.org/#list-append)rawEntries[i] to entriesForNavigationAPI.

    3.   Set i to i + 1.

10.   Return entriesForNavigationAPI.

To clear the forward session history of a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)navigable:

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running within navigable's [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue).

2.   Let step be the navigable's [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step).

3.   Let entryLists be the [ordered set](https://infra.spec.whatwg.org/#ordered-set) « navigable's [session history entries](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries) ».

4.   [For each](https://infra.spec.whatwg.org/#list-iterate)entryList of entryLists:

    1.   [Remove](https://infra.spec.whatwg.org/#list-remove) every [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) from entryList that has a [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) greater than step.

    2.   [For each](https://infra.spec.whatwg.org/#list-iterate)entry of entryList:

        1.   [For each](https://infra.spec.whatwg.org/#list-iterate)nestedHistory of entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [nested histories](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nested-histories), [append](https://infra.spec.whatwg.org/#set-append)nestedHistory's [entries list](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history-entries) to entryLists.

To get all used history steps that are part of [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable:

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running within traversable's [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue).

2.   Let steps be an empty [ordered set](https://infra.spec.whatwg.org/#ordered-set) of non-negative integers.

3.   Let entryLists be the [ordered set](https://infra.spec.whatwg.org/#ordered-set) « traversable's [session history entries](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries) ».

4.   [For each](https://infra.spec.whatwg.org/#list-iterate)entryList of entryLists:

    1.   [For each](https://infra.spec.whatwg.org/#list-iterate)entry of entryList:

        1.   [Append](https://infra.spec.whatwg.org/#set-append)entry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) to steps.

        2.   [For each](https://infra.spec.whatwg.org/#list-iterate)nestedHistory of entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [nested histories](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nested-histories), [append](https://infra.spec.whatwg.org/#set-append)nestedHistory's [entries list](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history-entries) to entryLists.

5.   Return steps, [sorted](https://infra.spec.whatwg.org/#list-sort-in-ascending-order).

#### 7.4.2 Navigation[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigating-across-documents)

Certain actions cause a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) to _[navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate)_ to a new resource.

For example, [following a hyperlink](https://html.spec.whatwg.org/multipage/links.html#following-hyperlinks-2), [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-submit), and the `window.open()` and `location.assign()` methods can all cause navigation.

Although in this standard the word "navigation" refers specifically to the [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm, this doesn't always line up with web developer or user perceptions. For example:

*   The [URL and history update steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#url-and-history-update-steps) are often used during so-called "single-page app navigations" or "same-document navigations", but they do not trigger the [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm.

*   [Reloads](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reload) and [traversals](https://html.spec.whatwg.org/multipage/browsing-the-web.html#traverse-the-history-by-a-delta) are sometimes talked about as a type of navigation, since all three will often [attempt to populate the history entry's document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-the-history-entry's-document) and thus could perform navigational fetches. See, e.g., the APIs exposed Navigation Timing. But they have their own entry point algorithms, separate from the [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm. [[NAVIGATIONTIMING]](https://html.spec.whatwg.org/multipage/references.html#refsNAVIGATIONTIMING)

*   Although [fragment navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-fragid) are always done through the [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm, a user might perceive them as more like jumping around a single page, than as a true navigation.

##### 7.4.2.1 Supporting concepts[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-supporting-concepts)

Before we can jump into the [navigation algorithm](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) itself, we need to establish several important structures that it uses.

The source snapshot params[struct](https://infra.spec.whatwg.org/#struct) is used to capture data from a `Document` initiating a navigation. It is snapshotted at the beginning of a navigation and used throughout the navigation's lifetime. It has the following [items](https://infra.spec.whatwg.org/#struct-item):

has transient activation a boolean sandboxing flags a [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set)allows downloading a boolean fetch client an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object) or null, only to be used as a [request client](https://fetch.spec.whatwg.org/#concept-request-client)source policy container a [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container)

To snapshot source snapshot params given a `Document`-or-null sourceDocument:

1.   If sourceDocument is null, then return a new [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params) with

[has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-activation)true[sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-sandbox)an empty [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set)[allows downloading](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-download)true[fetch client](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-client)null[source policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-policy-container)a new [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container)
This [only occurs](https://html.spec.whatwg.org/multipage/browsing-the-web.html#assert-null-sourcedocument) in the case of a browser UI-initiated navigation.

2.   Return a new [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params) with

[has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-activation)true if sourceDocument's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) has [transient activation](https://html.spec.whatwg.org/multipage/interaction.html#transient-activation); otherwise false[sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-sandbox)sourceDocument's [active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set)[allows downloading](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-download)false if sourceDocument's [active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set) has the [sandboxed downloads browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-downloads-browsing-context-flag) set; otherwise true[fetch client](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-client)sourceDocument's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)[source policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-policy-container)a [clone](https://html.spec.whatwg.org/multipage/browsers.html#clone-a-policy-container) of sourceDocument's [policy container](https://html.spec.whatwg.org/multipage/dom.html#concept-document-policy-container)

* * *

The target snapshot params[struct](https://infra.spec.whatwg.org/#struct) is used to capture data from a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) being navigated. Like [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params), it is snapshotted at the beginning of a navigation and used throughout the navigation's lifetime. It has the following [items](https://infra.spec.whatwg.org/#struct-item):

sandboxing flags a [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set)`iframe` element referrer policy a [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy)

* * *

Much of the navigation process is concerned with determining how to create a new `Document`, which ultimately happens in the [create and initialize a `Document` object](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object) algorithm. The parameters to that algorithm are tracked via a navigation params[struct](https://infra.spec.whatwg.org/#struct), which has the following [items](https://infra.spec.whatwg.org/#struct-item):

id null or a [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id)navigable the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) to be navigated request null or a [request](https://fetch.spec.whatwg.org/#concept-request) that started the navigation response a [response](https://fetch.spec.whatwg.org/#concept-response) that ultimately was navigated to (potentially a [network error](https://fetch.spec.whatwg.org/#concept-network-error))fetch controller null or a [fetch controller](https://fetch.spec.whatwg.org/#fetch-controller)commit early hints null or an algorithm accepting a `Document`, once it has been created COOP enforcement result an [opener policy enforcement result](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-result), used for reporting and potentially for causing a [browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#browsing-context-group-switches-due-to-cross-origin-opener-policy)reserved environment null or an [environment](https://html.spec.whatwg.org/multipage/webappapis.html#environment) reserved for the new `Document`origin an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) to use for the new `Document`policy container a [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container) to use for the new `Document`final sandboxing flag set a [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set) to impose on the new `Document``iframe` element referrer policy a [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy), used in the [internal ancestor origin objects list creation steps](https://html.spec.whatwg.org/multipage/dom.html#internal-ancestor-origin-objects-list-creation-steps)opener policy an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy) to use for the new `Document`navigation timing type a `NavigationTimingType` used for [creating the navigation timing entry](https://w3c.github.io/navigation-timing/#dfn-create-the-navigation-timing-entry) for the new `Document`about base URL a [URL](https://url.spec.whatwg.org/#concept-url) or null used to populate the new `Document`'s [about base URL](https://html.spec.whatwg.org/multipage/dom.html#concept-document-about-base-url)user involvement a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement) used when [obtaining a browsing context](https://html.spec.whatwg.org/multipage/browsers.html#obtain-browsing-context-navigation) for the new `Document`
Once a [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params) struct is created, this standard does not mutate any of its [items](https://infra.spec.whatwg.org/#struct-item). They are only passed onward to other algorithms.

* * *

A navigation ID is a UUID string generated during navigation. It is used to interface with the WebDriver BiDi specification as well as to track the [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation). [[WEBDRIVERBIDI]](https://html.spec.whatwg.org/multipage/references.html#refsWEBDRIVERBIDI)

* * *

After `Document` creation, the relevant [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)'s [session history](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries) gets updated. The `NavigationHistoryBehavior` enumeration is used to indicate the desired type of session history update to the [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm. It is one of the following:

"`push`"A regular navigation which adds a new [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry), and will [clear the forward session history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#clear-the-forward-session-history)."`replace`"A navigation that will replace the [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)."`auto`"The default value, which will be converted very early in the [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm into "`push`" or "`replace`". Usually it becomes "`push`", but under [certain circumstances](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-convert-to-replace) it becomes "`replace`" instead.
A history handling behavior is a `NavigationHistoryBehavior` that is either "`push`" or "`replace`", i.e., that has been resolved away from any initial "`auto`" value.

* * *

Various parts of the platform track whether a user is involved in a navigation. A user navigation involvement is one of the following:

"`browser UI`"The navigation was initiated by the user via browser UI mechanisms."`activation`"The navigation was initiated by the user via the [activation behavior](https://dom.spec.whatwg.org/#eventtarget-activation-behavior) of an element."`none`"The navigation was not initiated by the user.

For convenience at certain call sites, the user navigation involvement for an `Event`event is defined as follows:

1.   [Assert](https://infra.spec.whatwg.org/#assert): this algorithm is being called as part of an [activation behavior](https://dom.spec.whatwg.org/#eventtarget-activation-behavior) definition.

2.   [Assert](https://infra.spec.whatwg.org/#assert): event's `type` is "`click`".

3.   If event's `isTrusted` is initialized to true, then return "`activation`".

4.   Return "`none`".

##### 7.4.2.2 Beginning navigation[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#beginning-navigation)

To navigate a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable to a [URL](https://url.spec.whatwg.org/#concept-url)url using an optional `Document`-or-null sourceDocument (default null), with an optional [POST resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#post-resource), string, or null documentResource (default null), an optional [response](https://fetch.spec.whatwg.org/#concept-response)-or-null response (default null), an optional boolean exceptionsEnabled (default false), an optional `NavigationHistoryBehavior`historyHandling (default "`auto`"), an optional [serialized state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#serialized-state)-or-null navigationAPIState (default null), an optional [entry list](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#entry-list) or null formDataEntryList (default null), an optional [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy)referrerPolicy (default the empty string), an optional [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement (default "`none`"), an optional `Element`sourceElement (default null), an optional boolean initialInsertion (default false), and an optional [navigation API method tracker](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-api-method-tracker)-or-null apiMethodTracker (default null):

1.   Let cspNavigationType be "`form-submission`" if formDataEntryList is non-null; otherwise "`other`".

2.   Let sourceSnapshotParams be the result of [snapshotting source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#snapshotting-source-snapshot-params) given sourceDocument.

3.   Let initiatorOriginSnapshot be a new [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque).

4.   Let initiatorBaseURLSnapshot be `about:blank`.

5.   If sourceDocument is null:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): userInvolvement is "`browser UI`".

    2.   If url's [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is "`javascript`", then set initiatorOriginSnapshot to navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin).

6.   Otherwise:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): userInvolvement is not "`browser UI`".

    2.   If sourceDocument's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) is not [allowed by sandboxing to navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#allowed-to-navigate)navigable given sourceSnapshotParams:

        1.   If exceptionsEnabled is true, then throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException`.

        2.   Return.

    3.   Set initiatorOriginSnapshot to sourceDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin).

    4.   Set initiatorBaseURLSnapshot to sourceDocument's [document base URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-url).

7.   Let navigationId be the result of [generating a random UUID](https://w3c.github.io/webcrypto/#dfn-generate-a-random-uuid). [[WEBCRYPTO]](https://html.spec.whatwg.org/multipage/references.html#refsWEBCRYPTO)

8.   If the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent) is equal to navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent), then continue these steps. Otherwise, [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to continue these steps.

We do this because we are about to look at a lot of properties of navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document), which are in theory only accessible over in the appropriate [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop). (But, we do not want to unconditionally queue a task, since — for example — same-event-loop [fragment navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-fragid) need to take effect synchronously.)

Another implementation strategy would be to replicate the relevant information across event loops, or into a canonical "browser process", so that it can be consulted without queueing a task. This could give different results than what we specify here in edge cases, where the relevant properties have changed over in the target event loop but not yet been replicated. Further testing is needed to determine which of these strategies best matches browser behavior, in such racy edge cases. 
9.   If navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [unload counter](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-counter) is greater than 0, then invoke [WebDriver BiDi navigation failed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-failed) with navigable and a [WebDriver BiDi navigation status](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-status) whose [id](https://w3c.github.io/webdriver-bidi/#navigation-status-id) is navigationId, [status](https://w3c.github.io/webdriver-bidi/#navigation-status-status) is "`canceled`", and [url](https://w3c.github.io/webdriver-bidi/#navigation-status-url) is url, and return.

10.   Let container be navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container).

11.   If container is an `iframe` element and [will lazy load element steps](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#will-lazy-load-element-steps) given container returns true, then [stop intersection-observing a lazy loading element](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#stop-intersection-observing-a-lazy-loading-element)container and set container's [lazy load resumption steps](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-resumption-steps) to null.

12.   If historyHandling is "`auto`", then:

    1.   If url[equals](https://url.spec.whatwg.org/#concept-url-equals)navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [URL](https://dom.spec.whatwg.org/#concept-document-url), and initiatorOriginSnapshot is [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin), then set historyHandling to "`replace`".

    2.   Otherwise, set historyHandling to "`push`".

13.   If [the navigation must be a replace](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-navigation-must-be-a-replace) given url and navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document), then set historyHandling to "`replace`".

14.   If all of the following are true:

    *   documentResource is null;

    *   response is null;

    *   url[equals](https://url.spec.whatwg.org/#concept-url-equals)navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url) with [_exclude fragments_](https://url.spec.whatwg.org/#url-equals-exclude-fragments) set to true; and

    *   url's [fragment](https://url.spec.whatwg.org/#concept-url-fragment) is non-null,

then:

    1.   [Navigate to a fragment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-fragid) given navigable, url, historyHandling, userInvolvement, sourceElement, navigationAPIState, and navigationId.

    2.   Return.

15.   If navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) is non-null, then set navigable's [is delaying `load` events](https://html.spec.whatwg.org/multipage/document-sequences.html#delaying-load-events-mode) to true.

16.   Let targetSnapshotParams be the result of [snapshotting target snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#snapshotting-target-snapshot-params) given navigable.

17.   Invoke [WebDriver BiDi navigation started](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-started) with navigable and a new [WebDriver BiDi navigation status](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-status) whose [id](https://w3c.github.io/webdriver-bidi/#navigation-status-id) is navigationId, [status](https://w3c.github.io/webdriver-bidi/#navigation-status-status) is "`pending`", and [url](https://w3c.github.io/webdriver-bidi/#navigation-status-url) is url.

18.   If navigable's [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation) is "`traversal`", then:

    1.   Invoke [WebDriver BiDi navigation failed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-failed) with navigable and a new [WebDriver BiDi navigation status](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-status) whose [id](https://w3c.github.io/webdriver-bidi/#navigation-status-id) is navigationId, [status](https://w3c.github.io/webdriver-bidi/#navigation-status-status) is "`canceled`", and [url](https://w3c.github.io/webdriver-bidi/#navigation-status-url) is url.

    2.   Return.

Any attempts to navigate a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) that is currently [traversing](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-traverse-history-step) are ignored.

19.   [Set the ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#set-the-ongoing-navigation) for navigable to navigationId.

This will have the effect of aborting other ongoing navigations of navigable, since at certain points during navigation changes to the [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation) will cause further work to be abandoned.

20.   If url's [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is "`javascript`", then:

    1.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to [navigate to a `javascript:` URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-to-a-javascript:-url) given navigable, url, historyHandling, sourceSnapshotParams, initiatorOriginSnapshot, userInvolvement, cspNavigationType, initialInsertion, and navigationId.

    2.   Return.

21.   If all of the following are true:

    *   userInvolvement is not "
```
browser
     UI
```
";

    *   navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is [same origin-domain](https://html.spec.whatwg.org/multipage/browsers.html#same-origin-domain) with sourceDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin);

    *   navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [is initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank) is false; and

    *   url's [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is a [fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme),

then:

    1.   Let navigation be navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window)'s [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window-navigation-api).

    2.   Let entryListForFiring be formDataEntryList if documentResource is a [POST resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#post-resource); otherwise, null.

    3.   Let navigationAPIStateForFiring be navigationAPIState if navigationAPIState is not null; otherwise, [StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage)(undefined).

    4.   Let continue be the result of [firing a push/replace/reload `navigate` event](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-a-push/replace/reload-navigate-event) at navigation with _[navigationType](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-navigationtype)_ set to historyHandling, _[isSameDocument](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-issamedocument)_ set to false, _[userInvolvement](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-userinvolvement)_ set to userInvolvement, _[sourceElement](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-sourceelement)_ set to sourceElement, _[formDataEntryList](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-formdataentrylist)_ set to entryListForFiring, _[destinationURL](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-destinationurl)_ set to url, _[navigationAPIState](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-navigationapistate)_ set to navigationAPIStateForFiring, and _[apiMethodTracker](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-api-method-tracker)_ set to apiMethodTracker.

    5.   If continue is false, then return.

It is possible for navigations with userInvolvement of "`browser UI`" or initiated by a [cross origin-domain](https://html.spec.whatwg.org/multipage/browsers.html#same-origin-domain)sourceDocument to fire `navigate` events, if they go through the earlier [navigate to a fragment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-fragid) path.

22.   If sourceDocument is navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document), then [reserve deferred fetch quota](https://fetch.spec.whatwg.org/#reserve-deferred-fetch-quota) for navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container) given url's [origin](https://url.spec.whatwg.org/#concept-url-origin).

23.   [In parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel), run these steps:

    1.   Let unloadPromptCanceled be the result of [checking if unloading is canceled](https://html.spec.whatwg.org/multipage/browsing-the-web.html#checking-if-unloading-is-canceled) for navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [inclusive descendant navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#inclusive-descendant-navigables).

    2.   If unloadPromptCanceled is not "`continue`", or navigable's [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation) is no longer navigationId:

        1.   Invoke [WebDriver BiDi navigation failed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-failed) with navigable and a new [WebDriver BiDi navigation status](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-status) whose [id](https://w3c.github.io/webdriver-bidi/#navigation-status-id) is navigationId, [status](https://w3c.github.io/webdriver-bidi/#navigation-status-status) is "`canceled`", and [url](https://w3c.github.io/webdriver-bidi/#navigation-status-url) is url.

        2.   Abort these steps.

    3.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to [abort a document and its descendants](https://html.spec.whatwg.org/multipage/document-lifecycle.html#abort-a-document-and-its-descendants) given navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

    4.   Let documentState be a new [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-2) with

[request referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer-policy)referrerPolicy[initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin)initiatorOriginSnapshot[resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource)documentResource[navigable target name](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nav-target-name)navigable's [target name](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-target)
The [navigable target name](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nav-target-name) can get cleared under various conditions later in the navigation process, before the document state is finalized.

    5.   If url[matches `about:blank`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#matches-about:blank) or is `about:srcdoc`, then:

        1.   Set documentState's [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin) to initiatorOriginSnapshot.

        2.   Set documentState's [about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-about-base-url) to initiatorBaseURLSnapshot.

    6.   Let historyEntry be a new [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry), with its [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url) set to url and its [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state) set to documentState.

    7.   Let navigationParams be null.

    8.   If response is non-null:

[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#note-navigate-called-with-response)The [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm is only supplied with a [response](https://fetch.spec.whatwg.org/#concept-response) as part of the `object` and `embed` processing models, or for processing parts of [`multipart/x-mixed-replace` responses](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-multipart-x-mixed-replace) after the initial response.

        1.   Let sourcePolicyContainer be a [clone](https://html.spec.whatwg.org/multipage/browsers.html#clone-a-policy-container) of the sourceDocument's [policy container](https://html.spec.whatwg.org/multipage/dom.html#concept-document-policy-container), if sourceDocument is not null; otherwise null.

        2.   Let policyContainer be the result of [determining navigation params policy container](https://html.spec.whatwg.org/multipage/browsers.html#determining-navigation-params-policy-container) given response's [URL](https://fetch.spec.whatwg.org/#concept-response-url), null, sourcePolicyContainer, navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document)'s [policy container](https://html.spec.whatwg.org/multipage/dom.html#concept-document-policy-container), and null.

        3.   Let finalSandboxFlags be the [union](https://infra.spec.whatwg.org/#set-union) of targetSnapshotParams's [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params-sandbox) and policyContainer's [CSP list](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-csp-list)'s [CSP-derived sandboxing flags](https://html.spec.whatwg.org/multipage/browsers.html#csp-derived-sandboxing-flags).

        4.   Let responseOrigin be the result of [determining the origin](https://html.spec.whatwg.org/multipage/document-sequences.html#determining-the-origin) given response's [URL](https://fetch.spec.whatwg.org/#concept-response-url), finalSandboxFlags, and documentState's [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin).

        5.   Let coop be a new [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy).

        6.   Let coopEnforcementResult be a new [opener policy enforcement result](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-result) with

[url](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-url)response's [URL](https://fetch.spec.whatwg.org/#concept-response-url)[origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin)responseOrigin[opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-coop)coop
        7.   Set navigationParams to a new [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params), with

[id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-id)navigationId[navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable)navigable[request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request)null[response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)response[fetch controller](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-fetch-controller)null[commit early hints](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-commit-early-hints)null[COOP enforcement result](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop-enforcement-result)coopEnforcementResult[reserved environment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-reserved-environment)null[origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin)responseOrigin[policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-policy-container)policyContainer[final sandboxing flag set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-sandboxing)finalSandboxFlags[`iframe` element referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-iframe-referrer-policy)targetSnapshotParams's [`iframe` element referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params-iframe-referrer-policy)[opener policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop)coop[navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-nav-timing-type)"`navigate`"[about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-about-base-url)documentState's [about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-about-base-url)[user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-user-involvement)userInvolvement

    9.   [Attempt to populate the history entry's document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-the-history-entry's-document) for historyEntry, given navigable, "`navigate`", sourceSnapshotParams, targetSnapshotParams, userInvolvement, navigationId, navigationParams, cspNavigationType, with _[allowPOST](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-allow-post)_ set to true and _[completionSteps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-completion-steps)_ set to the following step:

        1.   [Append session history traversal steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-traversal-steps) to navigable's [traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable) to [finalize a cross-document navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#finalize-a-cross-document-navigation) given navigable, historyHandling, userInvolvement, and historyEntry.

##### 7.4.2.3 Ending navigation[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ending-navigation)

Although the usual cross-document navigation case will first foray into [populating a session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#populating-a-session-history-entry) with a `Document`, all navigations that don't get aborted will ultimately end up calling into one of the below algorithms.

###### 7.4.2.3.1 The usual cross-document navigation case[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-usual-cross-document-navigation-case)

To finalize a cross-document navigation given a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, a [history handling behavior](https://html.spec.whatwg.org/multipage/browsing-the-web.html#history-handling-behavior)historyHandling, a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement, and a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)historyEntry:

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running on navigable's [traversable navigable's](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable)[session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue).

2.   Set navigable's [is delaying `load` events](https://html.spec.whatwg.org/multipage/document-sequences.html#delaying-load-events-mode) to false.

3.   If historyEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) is null, then return.

This means that [attempting to populate the history entry's document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-the-history-entry's-document) ended up not creating a document, as a result of e.g., the navigation being canceled by a subsequent navigation, a 204 No Content response, etc.

4.   If all of the following are true:

    *   navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) is null;

    *   historyEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc) is not an [auxiliary browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#auxiliary-browsing-context) whose [opener browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-browsing-context) is non-null; and

    *   historyEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is not navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin),

then set historyEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [navigable target name](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nav-target-name) to the empty string.

5.   Let entryToReplace be navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) if historyHandling is "`replace`", otherwise null.

6.   Let traversable be navigable's [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable).

7.   Let targetStep be null.

8.   Let targetEntries be the result of [getting session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-session-history-entries) for navigable.

9.   If entryToReplace is null, then:

    1.   [Clear the forward session history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#clear-the-forward-session-history) of traversable.

    2.   Set targetStep to traversable's [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) + 1.

    3.   Set historyEntry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) to targetStep.

    4.   [Append](https://infra.spec.whatwg.org/#list-append)historyEntry to targetEntries.

Otherwise:

    1.   [Replace](https://infra.spec.whatwg.org/#list-replace)entryToReplace with historyEntry in targetEntries.

    2.   Set historyEntry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) to entryToReplace's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step).

    3.   If historyEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin) is [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with entryToReplace's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin), then set historyEntry's [navigation API key](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-navigation-api-key) to entryToReplace's [navigation API key](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-navigation-api-key).

    4.   Set targetStep to traversable's [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step).

10.   [Apply the push/replace history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-push/replace-history-step)targetStep to traversable given historyHandling and userInvolvement.

###### 7.4.2.3.2 The `javascript:` URL special case[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-javascript:-url-special-case)

`javascript:` URLs have a [dedicated label](https://github.com/whatwg/html/labels/topic%3A%20javascript%3A%20URLs) on the issue tracker documenting various problems with their specification.

To navigate to a `javascript:` URL, given a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)targetNavigable, a [URL](https://url.spec.whatwg.org/#concept-url)url, a [history handling behavior](https://html.spec.whatwg.org/multipage/browsing-the-web.html#history-handling-behavior)historyHandling, a [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params)sourceSnapshotParams, an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)initiatorOrigin, a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement, a string cspNavigationType, a boolean initialInsertion, and a [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id)navigationId:

1.   [Assert](https://infra.spec.whatwg.org/#assert): historyHandling is "`replace`".

2.   If targetNavigable's [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation) is no longer navigationId, then return.

3.   [Set the ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#set-the-ongoing-navigation) for targetNavigable to null.

4.   If initiatorOrigin is not [same origin-domain](https://html.spec.whatwg.org/multipage/browsers.html#same-origin-domain) with targetNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin), then return.

5.   Let request be a new [request](https://fetch.spec.whatwg.org/#concept-request) whose [URL](https://fetch.spec.whatwg.org/#concept-request-url) is url and whose [policy container](https://fetch.spec.whatwg.org/#concept-request-policy-container) is sourceSnapshotParams's [source policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-policy-container).

This is a synthetic [request](https://fetch.spec.whatwg.org/#concept-request) solely for plumbing into the next step. It will never hit the network.

6.   If the result of [should navigation request of type be blocked by Content Security Policy?](https://w3c.github.io/webappsec-csp/#should-block-navigation-request) given request and cspNavigationType is "`Blocked`", then return. [[CSP]](https://html.spec.whatwg.org/multipage/references.html#refsCSP)

7.   Let newDocument be the result of [evaluating a `javascript:` URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#evaluate-a-javascript:-url) given targetNavigable, url, initiatorOrigin, and userInvolvement.

8.   If newDocument is null:

    1.   If initialInsertion is true and targetNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [is initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank) is true, then run the [iframe load event steps](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-load-event-steps) given targetNavigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container).

    2.   Return.

In this case, some JavaScript code was executed, but no new `Document` was created, so we will not perform a navigation.

9.   [Assert](https://infra.spec.whatwg.org/#assert): initiatorOrigin is newDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin).

10.   Let entryToReplace be targetNavigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry).

11.   Let oldDocState be entryToReplace's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state).

12.   Let documentState be a new [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-2) with

[document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document)newDocument[history policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-history-policy-container)a [clone](https://html.spec.whatwg.org/multipage/browsers.html#clone-a-policy-container) of the oldDocState's [history policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-history-policy-container) if it is non-null; null otherwise[request referrer](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer)oldDocState's [request referrer](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer)[request referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer-policy)oldDocState's [request referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer-policy)or should this be the referrerPolicy that was passed to [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate)?[initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin)initiatorOrigin[origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin)initiatorOrigin[about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-about-base-url)oldDocState's [about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-about-base-url)[resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource)null[ever populated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-ever-populated)true[navigable target name](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nav-target-name)oldDocState's [navigable target name](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nav-target-name)
13.   Let historyEntry be a new [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry), with

[URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url)entryToReplace's [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url)[document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)documentState
For the [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url), we do _not_ use url, i.e. the actual `javascript:` URL that the [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm was called with. This means `javascript:` URLs are never stored in session history, and so can never be traversed to.

14.   [Append session history traversal steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-traversal-steps) to targetNavigable's [traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable) to [finalize a cross-document navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#finalize-a-cross-document-navigation) with targetNavigable, historyHandling, userInvolvement, and historyEntry.

To evaluate a `javascript:` URL given a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)targetNavigable, a [URL](https://url.spec.whatwg.org/#concept-url)url, an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)newDocumentOrigin, and a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement:

1.   Let urlString be the result of running the [URL serializer](https://url.spec.whatwg.org/#concept-url-serializer) on url.

2.   Let encodedScriptSource be the result of removing the leading "`javascript:`" from urlString.

3.   Let scriptSource be the [UTF-8 decoding](https://encoding.spec.whatwg.org/#utf-8-decode) of the [percent-decoding](https://url.spec.whatwg.org/#string-percent-decode) of encodedScriptSource.

4.   Let settings be targetNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

5.   Let baseURL be settings's [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url).

6.   Let script be the result of [creating a classic script](https://html.spec.whatwg.org/multipage/webappapis.html#creating-a-classic-script) given scriptSource, settings, baseURL, and the [default script fetch options](https://html.spec.whatwg.org/multipage/webappapis.html#default-script-fetch-options).

7.   Let evaluationStatus be the result of [running the classic script](https://html.spec.whatwg.org/multipage/webappapis.html#run-a-classic-script)script.

8.   Let result be null.

9.   If evaluationStatus is a normal completion, and evaluationStatus.[[Value]] is a String, then set result to evaluationStatus.[[Value]].

10.   Otherwise, return null.

11.   Let response be a new [response](https://fetch.spec.whatwg.org/#concept-response) with

[URL](https://fetch.spec.whatwg.org/#concept-response-url)targetNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [URL](https://dom.spec.whatwg.org/#concept-document-url)[header list](https://fetch.spec.whatwg.org/#concept-response-header-list)« (``Content-Type``, ``text/html;charset=utf-8``) »[body](https://fetch.spec.whatwg.org/#concept-response-body)the [UTF-8 encoding](https://encoding.spec.whatwg.org/#utf-8-encode) of result, [as a body](https://fetch.spec.whatwg.org/#byte-sequence-as-a-body)
The encoding to UTF-8 means that unpaired [surrogates](https://infra.spec.whatwg.org/#surrogate) will not roundtrip, once the HTML parser decodes the response body.

12.   Let policyContainer be targetNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [policy container](https://html.spec.whatwg.org/multipage/dom.html#concept-document-policy-container).

13.   Let finalSandboxFlags be policyContainer's [CSP list](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-csp-list)'s [CSP-derived sandboxing flags](https://html.spec.whatwg.org/multipage/browsers.html#csp-derived-sandboxing-flags).

14.   Let coop be targetNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [opener policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-coop).

15.   Let coopEnforcementResult be a new [opener policy enforcement result](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-result) with

[url](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-url)url[origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin)newDocumentOrigin[opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-coop)coop
16.   Let navigationParams be a new [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params), with

[id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-id)navigationId[navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable)targetNavigable[request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request)null this will cause the referrer of the resulting `Document` to be null; is that correct?[response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)response[fetch controller](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-fetch-controller)null[commit early hints](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-commit-early-hints)null[COOP enforcement result](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop-enforcement-result)coopEnforcementResult[reserved environment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-reserved-environment)null[origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin)newDocumentOrigin[policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-policy-container)policyContainer[final sandboxing flag set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-sandboxing)finalSandboxFlags[`iframe` element referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-iframe-referrer-policy)targetSnapshotParams's [`iframe` element referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params-iframe-referrer-policy)[opener policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop)coop[navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-nav-timing-type)"`navigate`"[about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-about-base-url)targetNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [about base URL](https://html.spec.whatwg.org/multipage/dom.html#concept-document-about-base-url)[user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-user-involvement)userInvolvement
17.   Return the result of [loading an HTML document](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-html) given navigationParams.

###### 7.4.2.3.3 Fragment navigations[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scroll-to-fragid)

To navigate to a fragment given a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, a [URL](https://url.spec.whatwg.org/#concept-url)url, a [history handling behavior](https://html.spec.whatwg.org/multipage/browsing-the-web.html#history-handling-behavior)historyHandling, a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement, an `Element`-or-null sourceElement, a [serialized state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#serialized-state)-or-null navigationAPIState, and a [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id)navigationId:

1.   Let navigation be navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window)'s [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window-navigation-api).

2.   Let destinationNavigationAPIState be navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [navigation API state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-navigation-api-state).

3.   If navigationAPIState is not null, then set destinationNavigationAPIState to navigationAPIState.

4.   Let continue be the result of [firing a push/replace/reload `navigate` event](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-a-push/replace/reload-navigate-event) at navigation with _[navigationType](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-navigationtype)_ set to historyHandling, _[isSameDocument](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-issamedocument)_ set to true, _[userInvolvement](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-userinvolvement)_ set to userInvolvement, _[sourceElement](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-sourceelement)_ set to sourceElement, _[destinationURL](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-destinationurl)_ set to url, and _[navigationAPIState](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-navigationapistate)_ set to destinationNavigationAPIState.

5.   If continue is false, then return.

6.   Let historyEntry be a new [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry), with

[URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url)url[document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)[navigation API state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-navigation-api-state)destinationNavigationAPIState[scroll restoration mode](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-scroll-restoration-mode)navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [scroll restoration mode](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-scroll-restoration-mode)For navigations performed with `navigation.navigate()`, the value provided by the `state` option is used for the new [navigation API state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-navigation-api-state). (This will set it to the serialization of undefined, if no value is provided for that option.) For other fragment navigations, including user-initiated ones, the [navigation API state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-navigation-api-state) is carried over from the previous entry.

The [classic history API state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-classic-history-api-state) is never carried over. 
7.   Let entryToReplace be navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) if historyHandling is "`replace`", otherwise null.

8.   Let history be navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [history object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#doc-history).

9.   Let scriptHistoryIndex be history's [index](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-index).

10.   Let scriptHistoryLength be history's [length](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-length).

11.   If historyHandling is "`push`", then:

    1.   Set history's [state](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-state) to null.

    2.   Increment scriptHistoryIndex.

    3.   Set scriptHistoryLength to scriptHistoryIndex + 1.

12.   Set navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [URL](https://dom.spec.whatwg.org/#concept-document-url) to url.

13.   Set navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) to historyEntry.

14.   [Update document for history step application](https://html.spec.whatwg.org/multipage/browsing-the-web.html#update-document-for-history-step-application) given navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document), historyEntry, true, scriptHistoryIndex, scriptHistoryLength, and historyHandling.

This algorithm will be called twice as a result of a single fragment navigation: once synchronously, where best-guess values scriptHistoryIndex and scriptHistoryLength are set, `history.state` is nulled out, and various events are fired; and once asynchronously, where the final values for index and length are set, `history.state` remains untouched, and no events are fired.

15.   [Scroll to the fragment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scroll-to-the-fragment-identifier) given navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

If the scrolling fails because the `Document` is new and the relevant [ID](https://dom.spec.whatwg.org/#concept-id) has not yet been parsed, then the second asynchronous call to [update document for history step application](https://html.spec.whatwg.org/multipage/browsing-the-web.html#update-document-for-history-step-application) will take care of scrolling.

16.   Let traversable be navigable's [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable).

17.   [Append the following session history synchronous navigation steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-sync-nav-steps) involving navigable to traversable:

    1.   [Finalize a same-document navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#finalize-a-same-document-navigation) given traversable, navigable, historyEntry, entryToReplace, historyHandling, and userInvolvement.

    2.   Invoke [WebDriver BiDi fragment navigated](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-fragment-navigated) with navigable and a new [WebDriver BiDi navigation status](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-status) whose [id](https://w3c.github.io/webdriver-bidi/#navigation-status-id) is navigationId, [url](https://w3c.github.io/webdriver-bidi/#navigation-status-url) is url, and [status](https://w3c.github.io/webdriver-bidi/#navigation-status-status) is "`complete`".

To finalize a same-document navigation given a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)targetNavigable, a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)targetEntry, a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)-or-null entryToReplace, a [history handling behavior](https://html.spec.whatwg.org/multipage/browsing-the-web.html#history-handling-behavior)historyHandling, and a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement:

This is used by both [fragment navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-fragid) and by the [URL and history update steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#url-and-history-update-steps), which are the only synchronous updates to session history. By virtue of being synchronous, those algorithms are performed outside of the [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable)'s [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue). This puts them out of sync with the [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable)'s [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step), so this algorithm is used to resolve conflicts due to race conditions.

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running on traversable's [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue).

2.   If targetNavigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) is not targetEntry, then return.

3.   Let targetStep be null.

4.   Let targetEntries be the result of [getting session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-session-history-entries) for targetNavigable.

5.   If entryToReplace is null, then:

    1.   [Clear the forward session history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#clear-the-forward-session-history) of traversable.

    2.   Set targetStep to traversable's [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) + 1.

    3.   Set targetEntry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) to targetStep.

    4.   [Append](https://infra.spec.whatwg.org/#list-append)targetEntry to targetEntries.

Otherwise:

    1.   [Replace](https://infra.spec.whatwg.org/#list-replace)entryToReplace with targetEntry in targetEntries.

    2.   Set targetEntry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) to entryToReplace's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step).

    3.   Set targetStep to traversable's [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step).

6.   [Apply the push/replace history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-push/replace-history-step)targetStep to traversable given historyHandling and userInvolvement.

This is done even for "`replace`" navigations, as it resolves race conditions across multiple synchronous navigations.

###### 7.4.2.3.4 Non-fetch schemes and external software[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-schemes-and-external-software)

The input to [attempt to create a non-fetch scheme document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-create-a-non-fetch-scheme-document) is the non-fetch scheme navigation params[struct](https://infra.spec.whatwg.org/#struct). It is a lightweight version of [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params) which only carries parameters relevant to the non-[fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme) navigation case. It has the following [items](https://infra.spec.whatwg.org/#struct-item):

id null or a [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id)navigable the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) experiencing the navigation URL a [URL](https://url.spec.whatwg.org/#concept-url)target snapshot sandboxing flags the [target snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params)'s [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params-sandbox) present during navigation source snapshot has transient activation a copy of the [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params)'s [has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-activation) boolean present during activation initiator origin
an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) possibly for use in a user-facing prompt to confirm the invocation of an external software package

This differs slightly from a [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin) in that a [non-fetch scheme navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-navigation-params)'s [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-initiator-origin) follows redirects up to the last [fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme) URL in a redirect chain that ends in a non-[fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme) URL.

navigation timing type a `NavigationTimingType` used for [creating the navigation timing entry](https://w3c.github.io/navigation-timing/#dfn-create-the-navigation-timing-entry) for the new `Document` (if one is created)user involvement a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement) used when [obtaining a browsing context](https://html.spec.whatwg.org/multipage/browsers.html#obtain-browsing-context-navigation) for the new `Document` (if one is created)

To attempt to create a non-fetch scheme document, given a [non-fetch scheme navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-navigation-params)navigationParams:

1.   Let url be navigationParams's [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-url).
2.   Let navigable be navigationParams's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-navigable).
3.   If url is to be handled using a mechanism that does not affect navigable, e.g., because url's [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is handled externally, then:

    1.   [Hand-off to external software](https://html.spec.whatwg.org/multipage/browsing-the-web.html#hand-off-to-external-software) given url, navigable, navigationParams's [target snapshot sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-target-sandbox), navigationParams's [source snapshot has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-source-activation), and navigationParams's [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-initiator-origin).

    2.   Return null.

4.   Handle url by displaying some sort of inline content, e.g., an error message because the specified scheme is not one of the supported protocols, or an inline prompt to allow the user to select [a registered handler](https://html.spec.whatwg.org/multipage/system-state.html#dom-navigator-registerprotocolhandler) for the given scheme. Return the result of [displaying the inline content](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-ua-inline) given navigable, navigationParams's [id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-id), navigationParams's [navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-nav-timing-type), and navigationParams's [user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-user-involvement).

In the case of a registered handler being used, [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) will be invoked with a new URL.

To hand-off to external software given a [URL](https://url.spec.whatwg.org/#concept-url) or [response](https://fetch.spec.whatwg.org/#concept-response)resource, a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, a [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set)sandboxFlags, a boolean hasTransientActivation, and an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)initiatorOrigin, user agents should:

1.   If all of the following are true:

    *   navigable is not a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable);

    *   sandboxFlags has its [sandboxed custom protocols navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-custom-protocols-navigation-browsing-context-flag) set; and

    *   sandboxFlags has its [sandboxed top-level navigation with user activation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-top-level-navigation-with-user-activation-browsing-context-flag) set, or hasTransientActivation is false,

then return without invoking the external software package.

Navigation inside an iframe toward external software can be seen by users as a new popup or a new top-level navigation. That's why its is allowed in sandboxed `iframe` only when one of `allow-popups`, `allow-top-navigation`, `allow-top-navigation-by-user-activation`, or `allow-top-navigation-to-custom-protocols` is specified.

2.   Perform the appropriate handoff of resource while attempting to mitigate the risk that this is an attempt to exploit the target software. For example, user agents could prompt the user to confirm that initiatorOrigin is to be allowed to invoke the external software in question. In particular, if hasTransientActivation is false, then the user agent should not invoke the external software package without prior user confirmation.

For example, there could be a vulnerability in the target software's URL handler which a hostile page would attempt to exploit by tricking a user into clicking a link.

##### 7.4.2.4 Preventing navigation[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#preventing-navigation)

A couple of scenarios can intervene early in the navigation process and put the whole thing to a halt. This can be especially exciting when multiple [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) are navigating at the same time, due to a session history traversal.

A [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)source is allowed by sandboxing to navigate a second [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)target, given a [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params)sourceSnapshotParams, if the following steps return true:

1.   If source is target, then return true.

2.   If source is an ancestor of target, then return true.

3.   If target is an ancestor of source, then:

    1.   If target is not a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable), then return true.

    2.   If sourceSnapshotParams's [has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-activation) is true, and sourceSnapshotParams's [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-sandbox)'s [sandboxed top-level navigation with user activation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-top-level-navigation-with-user-activation-browsing-context-flag) is set, then return false.

    3.   If sourceSnapshotParams's [has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-activation) is false, and sourceSnapshotParams's [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-sandbox)'s [sandboxed top-level navigation without user activation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-top-level-navigation-without-user-activation-browsing-context-flag) is set, then return false.

    4.   Return true.

4.   If target is a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable):

    1.   If source is the [one permitted sandboxed navigator](https://html.spec.whatwg.org/multipage/browsers.html#one-permitted-sandboxed-navigator) of target, then return true.

    2.   If sourceSnapshotParams's [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-sandbox)'s [sandboxed navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-navigation-browsing-context-flag) is set, then return false.

    3.   Return true.

5.   If sourceSnapshotParams's [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-sandbox)'s [sandboxed navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-navigation-browsing-context-flag) is set, then return false.

6.   Return true.

To check if unloading is canceled for a [list](https://infra.spec.whatwg.org/#list) of [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigablesThatNeedBeforeUnload, given an optional [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, an optional integer targetStep, and an optional [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvementForNavigateEvent, run these steps. They return "`canceled-by-beforeunload`", "`canceled-by-navigate`", or "`continue`".

1.   Let documentsToFireBeforeunload be the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of each [item](https://infra.spec.whatwg.org/#list-item) in navigablesThatNeedBeforeUnload.

2.   Let unloadPromptShown be false.

3.   Let finalStatus be "`continue`".

4.   If traversable was given, then:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): targetStep and userInvolvementForNavigateEvent were given.

    2.   Let targetEntry be the result of [getting the target history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-the-target-history-entry) given traversable and targetStep.

    3.   If targetEntry is not traversable's [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry), and targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin) is the [same](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) as traversable's [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry)'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin), then:

In this case, we're going to fire the `navigate` event for traversable here. Because [under some circumstances](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigate-event-traverse-can-be-canceled) it might be canceled, we need to do this separately from [other traversal `navigate` events](https://html.spec.whatwg.org/multipage/browsing-the-web.html#descendant-navigable-traversal-navigate-events), which happen later.

Additionally, because we want `beforeunload` events to fire before `navigate` events, this means we need to fire `beforeunload` for traversable here (if applicable), instead of doing it as part of the below loop over documentsToFireBeforeunload. 
        1.   Let eventsFired be false.

        2.   Let needsBeforeunload be true if navigablesThatNeedBeforeUnload[contains](https://infra.spec.whatwg.org/#list-contain)traversable; otherwise false.

        3.   If needsBeforeunload is true, then [remove](https://infra.spec.whatwg.org/#list-remove)traversable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) from documentsToFireBeforeunload.

        4.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given traversable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to perform the following steps:

            1.   If needsBeforeunload is true, then:

                1.   Let (unloadPromptShownForThisDocument, unloadPromptCanceledByThisDocument) be the result of running the [steps to fire `beforeunload`](https://html.spec.whatwg.org/multipage/browsing-the-web.html#steps-to-fire-beforeunload) given traversable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) and false.

                2.   If unloadPromptShownForThisDocument is true, then set unloadPromptShown to true.

                3.   If unloadPromptCanceledByThisDocument is true, then set finalStatus to "`canceled-by-beforeunload`".

            2.   If finalStatus is "`canceled-by-beforeunload`", then abort these steps.

            3.   Let navigation be traversable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window)'s [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window-navigation-api).

            4.   Let navigateEventResult be the result of [firing a traverse `navigate` event](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-a-traverse-navigate-event) at navigation given targetEntry and userInvolvementForNavigateEvent.

            5.   If navigateEventResult is false, then set finalStatus to "`canceled-by-navigate`".

            6.   Set eventsFired to true.

        5.   Wait until eventsFired is true.

        6.   If finalStatus is not "`continue`", then return finalStatus.

5.   Let totalTasks be the [size](https://infra.spec.whatwg.org/#list-size) of documentsToFireBeforeunload.

6.   Let completedTasks be 0.

7.   [For each](https://infra.spec.whatwg.org/#list-iterate)document of documentsToFireBeforeunload, [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to run the steps:

    1.   Let (unloadPromptShownForThisDocument, unloadPromptCanceledByThisDocument) be the result of running the [steps to fire `beforeunload`](https://html.spec.whatwg.org/multipage/browsing-the-web.html#steps-to-fire-beforeunload) given document and unloadPromptShown.

    2.   If unloadPromptShownForThisDocument is true, then set unloadPromptShown to true.

    3.   If unloadPromptCanceledByThisDocument is true, then set finalStatus to "`canceled-by-beforeunload`".

    4.   Increment completedTasks.

8.   Wait for completedTasks to be totalTasks.

9.   Return finalStatus.

The steps to fire `beforeunload` given a `Document`document and a boolean unloadPromptShown are:

1.   Let unloadPromptCanceled be false.

2.   Increase the document's [unload counter](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-counter) by 1.

3.   Increase document's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop)'s [termination nesting level](https://html.spec.whatwg.org/multipage/document-lifecycle.html#termination-nesting-level) by 1.

4.   Let eventFiringResult be the result of [firing an event](https://dom.spec.whatwg.org/#concept-event-fire) named `beforeunload` at document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), using `BeforeUnloadEvent`, with the `cancelable` attribute initialized to true.

5.   Decrease document's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop)'s [termination nesting level](https://html.spec.whatwg.org/multipage/document-lifecycle.html#termination-nesting-level) by 1.

6.   If all of the following are true:

    *   unloadPromptShown is false;

    *   document's [active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set) does not have its [sandboxed modals flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-modals-flag) set;

    *   document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) has [sticky activation](https://html.spec.whatwg.org/multipage/interaction.html#sticky-activation);

    *   eventFiringResult is false, or the `returnValue` attribute of event is not the empty string; and

    *   showing an unload prompt is unlikely to be annoying, deceptive, or pointless,

then:

    1.   Set unloadPromptShown to true.

    2.   Let userPromptHandler be the result of [WebDriver BiDi user prompt opened](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-user-prompt-opened) with document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), "`beforeunload`", and "".

    3.   If userPromptHandler is "`dismiss`", then set unloadPromptCanceled to true.

    4.   If userPromptHandler is "`none`", then:

        1.   Ask the user to confirm that they wish to unload the document, and [pause](https://html.spec.whatwg.org/multipage/webappapis.html#pause) while waiting for the user's response.

The message shown to the user is not customizable, but instead determined by the user agent. In particular, the actual value of the `returnValue` attribute is ignored.

        2.   If the user did not confirm the page navigation, then set unloadPromptCanceled to true.

    5.   Invoke [WebDriver BiDi user prompt closed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-user-prompt-closed) with document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), "`beforeunload`", and true if unloadPromptCanceled is false or false otherwise.

7.   Decrease document's [unload counter](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-counter) by 1.

8.   Return (unloadPromptShown, unloadPromptCanceled).

##### 7.4.2.5 Aborting navigation[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#aborting-navigation)

Each [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) has an ongoing navigation, which is a [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id), "`traversal`", or null, initially null. It is used to track navigation aborting and to prevent any navigations from taking place during [traversal](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-traverse-history-step).

#### 7.4.3 Reloading and traversing[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reloading-and-traversing)

To reload a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable given an optional [serialized state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#serialized-state)-or-null navigationAPIState (default null), an optional [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement (default "`none`"), and an optional [navigation API method tracker](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-api-method-tracker)-or-null apiMethodTracker (default null):

1.   If userInvolvement is not "`browser UI`", then:

    1.   Let navigation be navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window)'s [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window-navigation-api).

    2.   Let destinationNavigationAPIState be navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [navigation API state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-navigation-api-state).

    3.   If navigationAPIState is not null, then set destinationNavigationAPIState to navigationAPIState.

    4.   Let continue be the result of [firing a push/replace/reload `navigate` event](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-a-push/replace/reload-navigate-event) at navigation with _[navigationType](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-navigationtype)_ set to "`reload`", _[isSameDocument](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-issamedocument)_ set to false, _[userInvolvement](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-userinvolvement)_ set to userInvolvement, _[destinationURL](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-destinationurl)_ set to navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url), _[navigationAPIState](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-navigationapistate)_ set to destinationNavigationAPIState, and _[apiMethodTracker](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-navigate-prr-api-method-tracker)_ set to apiMethodTracker.

    5.   If continue is false, then return.

2.   Set navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending) to true.

3.   Let traversable be navigable's [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable).

4.   [Append the following session history traversal steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-traversal-steps) to traversable:

    1.   [Apply the reload history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-reload-history-step) to traversable given userInvolvement.

To traverse the history by a delta given a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, an integer delta, and an optional `Document`sourceDocument:

1.   Let sourceSnapshotParams and initiatorToCheck be null.

2.   Let userInvolvement be "
```
browser
   UI
```
".

3.   If sourceDocument is given, then:

    1.   Set sourceSnapshotParams to the result of [snapshotting source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#snapshotting-source-snapshot-params) given sourceDocument.

    2.   Set initiatorToCheck to sourceDocument's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable).

    3.   Set userInvolvement to "`none`".

4.   [Append the following session history traversal steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-traversal-steps) to traversable:

    1.   Let allSteps be the result of [getting all used history steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-all-used-history-steps) for traversable.

    2.   Let currentStepIndex be the index of traversable's [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) within allSteps.

    3.   Let targetStepIndex be currentStepIndex plus delta.

    4.   If allSteps[targetStepIndex] does not [exist](https://infra.spec.whatwg.org/#list-contain), then abort these steps.

    5.   [Apply the traverse history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-traverse-history-step)allSteps[targetStepIndex] to traversable, given sourceSnapshotParams, initiatorToCheck, and userInvolvement.

#### 7.4.4 Non-fragment synchronous "navigations"[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-non-frag-sync)

Apart from the [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm, [session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) can be pushed or replaced via one more mechanism, the [URL and history update steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#url-and-history-update-steps). The most well-known callers of these steps are the `history.replaceState()` and `history.pushState()` APIs, but various other parts of the standard also need to perform updates to the [active history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry), and they use these steps to do so.

The URL and history update steps, given a `Document`document, a [URL](https://url.spec.whatwg.org/#concept-url)newURL, an optional [serialized state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#serialized-state)-or-null serializedData (default null), and an optional [history handling behavior](https://html.spec.whatwg.org/multipage/browsing-the-web.html#history-handling-behavior)historyHandling (default "`replace`"), are:

1.   Let navigable be document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable).

2.   Let activeEntry be navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry).

3.   Let newEntry be a new [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry), with

[URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url)newURL[serialized state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-classic-history-api-state)if serializedData is not null, serializedData; otherwise activeEntry's [classic history API state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-classic-history-api-state)[document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)activeEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)[scroll restoration mode](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-scroll-restoration-mode)activeEntry's [scroll restoration mode](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-scroll-restoration-mode)[persisted user state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-other)activeEntry's [persisted user state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-other)
4.   If document's [is initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank) is true, then set historyHandling to "`replace`".

This means that `pushState()` on an [initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank)`Document` behaves as a `replaceState()` call.

5.   Let entryToReplace be activeEntry if historyHandling is "`replace`", otherwise null.

6.   If historyHandling is "`push`", then:

    1.   Increment document's [history object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#doc-history)'s [index](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-index).

    2.   Set document's [history object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#doc-history)'s [length](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-length) to its [index](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-index) + 1.

These are temporary best-guess values for immediate synchronous access.

7.   If serializedData is not null, then [restore the history object state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restore-the-history-object-state) given document and newEntry.

8.   [Set the URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#set-the-url) given document to newURL.

Since this is neither a [navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) nor a [history traversal](https://html.spec.whatwg.org/multipage/browsing-the-web.html#traverse-the-history-by-a-delta), it does not cause a `hashchange` event to be fired.

9.   Set document's [latest entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#latest-entry) to newEntry.

10.   Set navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) to newEntry.

11.   [Update the navigation API entries for a same-document navigation](https://html.spec.whatwg.org/multipage/nav-history-apis.html#update-the-navigation-api-entries-for-a-same-document-navigation) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window-navigation-api), newEntry, and historyHandling.

12.   Let traversable be navigable's [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable).

13.   [Append the following session history synchronous navigation steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-sync-nav-steps) involving navigable to traversable:

    1.   [Finalize a same-document navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#finalize-a-same-document-navigation) given traversable, navigable, newEntry, entryToReplace, historyHandling, and "`none`".

    2.   Invoke [WebDriver BiDi history updated](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-history-updated) with navigable.

Although both [fragment navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate-fragid) and the [URL and history update steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#url-and-history-update-steps) perform synchronous history updates, only fragment navigation contains a synchronous call to [update document for history step application](https://html.spec.whatwg.org/multipage/browsing-the-web.html#update-document-for-history-step-application). The [URL and history update steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#url-and-history-update-steps) instead perform a few select updates inside the above algorithm, omitting others. This is somewhat of an unfortunate historical accident, and generally leads to [web-developer sadness](https://github.com/whatwg/html/issues/5562) about the inconsistency. For example, this means that `popstate` events fire for fragment navigations, but not for `history.pushState()` calls.

#### 7.4.5 Populating a session history entry[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#populating-a-session-history-entry)

As explained in [the overview](https://html.spec.whatwg.org/multipage/browsing-the-web.html#history), both [navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigating-across-documents) and [traversal](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reloading-and-traversing) involve creating a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) and then attempting to populate its [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) member, so that it can be presented inside the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable).

This involves either: using [an already-given response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#note-navigate-called-with-response); using the [srcdoc resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource) stored in the [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry); or [fetching](https://html.spec.whatwg.org/multipage/browsing-the-web.html#create-navigation-params-by-fetching). The process has several failure modes, which can either result in doing nothing (leaving the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) on its currently-[active](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)`Document`) or can result in populating the [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) with an [error document](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-ua-inline).

To attempt to populate the history entry's document for a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)entry, given a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, a `NavigationTimingType`navTimingType, a [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params)sourceSnapshotParams, a [target snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params)targetSnapshotParams, a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement, an optional [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id)-or-null navigationId (default null), an optional [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params)-or-null navigationParams (default null), an optional string cspNavigationType (default "`other`"), an optional boolean allowPOST (default false), and optional algorithm steps completionSteps (default an empty algorithm):

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel).

2.   [Assert](https://infra.spec.whatwg.org/#assert): if navigationParams is non-null, then navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response) is non-null.

3.   Let documentResource be entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource).

4.   If navigationParams is null, then:

    1.   If documentResource is a string, then set navigationParams to the result of [creating navigation params from a srcdoc resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#create-navigation-params-from-a-srcdoc-resource) given entry, navigable, targetSnapshotParams, userInvolvement, navigationId, and navTimingType.

    2.   Otherwise, if all of the following are true:

        *   entry's [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url)'s [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is a [fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme); and

        *   documentResource is null, or allowPOST is true and documentResource's [request body](https://html.spec.whatwg.org/multipage/browsing-the-web.html#post-resource-request-body) is not failure,

then set navigationParams to the result of [creating navigation params by fetching](https://html.spec.whatwg.org/multipage/browsing-the-web.html#create-navigation-params-by-fetching) given entry, navigable, sourceSnapshotParams, targetSnapshotParams, cspNavigationType, userInvolvement, navigationId, and navTimingType.

    3.   Otherwise, if entry's [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url)'s [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is not a [fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme), then set navigationParams to a new [non-fetch scheme navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-navigation-params), with

[id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-id)navigationId[navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-navigable)navigable[URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-url)entry's [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url)[target snapshot sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-target-sandbox)targetSnapshotParams's [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params-sandbox)[source snapshot has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-source-activation)sourceSnapshotParams's [has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-activation)[initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-initiator-origin)entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin)[navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-nav-timing-type)navTimingType[user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-user-involvement)userInvolvement

5.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source), given navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#active-window), to run these steps:

    1.   If navigable's [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation) no longer equals navigationId, then run completionSteps and abort these steps.

    2.   Let saveExtraDocumentState be true.

Usually, in the cases where we end up populating entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document), we then want to save some of the state from that `Document` into entry. This ensures that if there are future traversals to entry where its [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document)[has been destroyed](https://html.spec.whatwg.org/multipage/browsing-the-web.html#note-bfcache), we can use that state when creating a new `Document`.

However, in some specific cases, saving the state would be unhelpful. For those, we set saveExtraDocumentState to false later in this algorithm. 
    3.   If navigationParams is a [non-fetch scheme navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-navigation-params), then:

        1.   Set entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) to the result of running [attempt to create a non-fetch scheme document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-create-a-non-fetch-scheme-document) given navigationParams.

This can result in setting entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) to null, e.g., when [handing-off to external software](https://html.spec.whatwg.org/multipage/browsing-the-web.html#hand-off-to-external-software).

        2.   Set saveExtraDocumentState to false.

    4.   Otherwise, if any of the following are true:

        *   navigationParams is null;

        *   the result of [should navigation response to navigation request of type in target be blocked by Content Security Policy?](https://w3c.github.io/webappsec-csp/#should-block-navigation-response) given navigationParams's [request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request), navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response), navigationParams's [policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-policy-container)'s [CSP list](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-csp-list), cspNavigationType, and navigable is "`Blocked`";

        *   navigationParams's [reserved environment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-reserved-environment) is non-null and the result of [checking a navigation response's adherence to its embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#check-a-navigation-response's-adherence-to-its-embedder-policy) given navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response), navigable, and navigationParams's [policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-policy-container)'s [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-embedder-policy) is false; or

        *   the result of [checking a navigation response's adherence to ``X-Frame-Options``](https://html.spec.whatwg.org/multipage/speculative-loading.html#check-a-navigation-response's-adherence-to-x-frame-options) given navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response), navigable, navigationParams's [policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-policy-container)'s [CSP list](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-csp-list), and navigationParams's [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin) is false,

then:

        1.   Set entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) to the result of [creating a document for inline content that doesn't have a DOM](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-ua-inline), given navigable, null, navTimingType, and userInvolvement. The inline content should indicate to the user the sort of error that occurred.

        2.   [Make document unsalvageable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#make-document-unsalvageable) given entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) and "`navigation-failure`".

        3.   Set saveExtraDocumentState to false.

        4.   If navigationParams is not null, then:

            1.   Run the [environment discarding steps](https://html.spec.whatwg.org/multipage/webappapis.html#environment-discarding-steps) for navigationParams's [reserved environment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-reserved-environment).

            2.   Invoke [WebDriver BiDi navigation failed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-failed) with navigable and a new [WebDriver BiDi navigation status](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-status) whose [id](https://w3c.github.io/webdriver-bidi/#navigation-status-id) is navigationId, [status](https://w3c.github.io/webdriver-bidi/#navigation-status-status) is "`canceled`", and [url](https://w3c.github.io/webdriver-bidi/#navigation-status-url) is navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [URL](https://fetch.spec.whatwg.org/#concept-response-url).

    5.   Otherwise, if navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response) has a ``Content-Disposition`` header specifying the `attachment` disposition type, then:

        1.   Let sourceAllowsDownloading be sourceSnapshotParams's [allows downloading](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-download).

        2.   Let targetAllowsDownloading be false if navigationParams's [final sandboxing flag set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-sandboxing) has the [sandboxed downloads browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-downloads-browsing-context-flag) set; otherwise true.

        3.   Let uaAllowsDownloading be true.

        4.   Optionally, the user agent may set uaAllowsDownloading to false, if it believes doing so would safeguard the user from a potentially hostile download.

        5.   If sourceAllowsDownloading, targetAllowsDownloading, and uaAllowsDownloading are true, then:

            1.   [Handle as a download](https://html.spec.whatwg.org/multipage/links.html#handle-as-a-download)navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response) with navigable and navigationId.

This branch leaves entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) as null.

    6.   Otherwise, if navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [status](https://fetch.spec.whatwg.org/#concept-response-status) is not 204 and is not 205, then set entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) to the result of [loading a document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#loading-a-document) given navigationParams, sourceSnapshotParams, and entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin).

This can result in setting entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) to null, e.g., when [handing-off to external software](https://html.spec.whatwg.org/multipage/browsing-the-web.html#hand-off-to-external-software).

    7.   If entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) is not null, then:

        1.   Set entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [ever populated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-ever-populated) to true.

        2.   If saveExtraDocumentState is true:

            1.   Let document be entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document).

            2.   Set entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin) to document's [origin](https://dom.spec.whatwg.org/#concept-document-origin).

            3.   If document's [URL](https://dom.spec.whatwg.org/#concept-document-url)[requires storing the policy container in history](https://html.spec.whatwg.org/multipage/browsers.html#requires-storing-the-policy-container-in-history), then:

                1.   [Assert](https://infra.spec.whatwg.org/#assert): navigationParams is a [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params) (i.e., neither null nor a [non-fetch scheme navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-navigation-params)).

                2.   Set entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [history policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-history-policy-container) to navigationParams's [policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-policy-container).

        3.   If entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [request referrer](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer) is "`client`", and navigationParams is a [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params) (i.e., neither null nor a [non-fetch scheme navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-navigation-params)), then:

            1.   [Assert](https://infra.spec.whatwg.org/#assert): navigationParams's [request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request) is not null.

            2.   Set entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [request referrer](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer) to navigationParams's [request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request)'s [referrer](https://fetch.spec.whatwg.org/#concept-request-referrer).

    8.   Run completionSteps.

To create navigation params from a srcdoc resource given a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)entry, a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, a [target snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params)targetSnapshotParams, a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement, a [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id)-or-null navigationId, and a `NavigationTimingType`navTimingType:

1.   Let documentResource be entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource).

2.   Let response be a new [response](https://fetch.spec.whatwg.org/#concept-response) with

[URL](https://fetch.spec.whatwg.org/#concept-response-url)`about:srcdoc`[header list](https://fetch.spec.whatwg.org/#concept-response-header-list)« (``Content-Type``, ``text/html``) »[body](https://fetch.spec.whatwg.org/#concept-response-body)the [UTF-8 encoding](https://encoding.spec.whatwg.org/#utf-8-encode) of documentResource, [as a body](https://fetch.spec.whatwg.org/#byte-sequence-as-a-body)
3.   Let responseOrigin be the result of [determining the origin](https://html.spec.whatwg.org/multipage/document-sequences.html#determining-the-origin) given response's [URL](https://fetch.spec.whatwg.org/#concept-response-url), targetSnapshotParams's [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params-sandbox), and entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin).

4.   Let coop be a new [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy).

5.   Let coopEnforcementResult be a new [opener policy enforcement result](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-result) with

[url](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-url)response's [URL](https://fetch.spec.whatwg.org/#concept-response-url)[origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin)responseOrigin[opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-coop)coop
6.   Let policyContainer be the result of [determining navigation params policy container](https://html.spec.whatwg.org/multipage/browsers.html#determining-navigation-params-policy-container) given response's [URL](https://fetch.spec.whatwg.org/#concept-response-url), entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [history policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-history-policy-container), null, navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document)'s [policy container](https://html.spec.whatwg.org/multipage/dom.html#concept-document-policy-container), and null.

7.   Return a new [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params), with

[id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-id)navigationId[navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable)navigable[request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request)null[response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)response[fetch controller](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-fetch-controller)null[commit early hints](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-commit-early-hints)null[COOP enforcement result](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop-enforcement-result)coopEnforcementResult[reserved environment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-reserved-environment)null[origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin)responseOrigin[policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-policy-container)policyContainer[final sandboxing flag set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-sandboxing)targetSnapshotParams's [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params-sandbox)[`iframe` element referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-iframe-referrer-policy)targetSnapshotParams's [`iframe` element referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params-iframe-referrer-policy)[opener policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop)coop[navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-nav-timing-type)navTimingType[about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-about-base-url)entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-about-base-url)[user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-user-involvement)userInvolvement

To create navigation params by fetching given a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)entry, a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, a [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params)sourceSnapshotParams, a [target snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params)targetSnapshotParams, a string cspNavigationType, a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement, a [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id)-or-null navigationId, and a `NavigationTimingType`navTimingType, perform the following steps. They return a [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params), a [non-fetch scheme navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-navigation-params), or null.

This algorithm mutates entry.

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel).

2.   Let documentResource be entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource).

3.   Let request be a new [request](https://fetch.spec.whatwg.org/#concept-request), with

[url](https://fetch.spec.whatwg.org/#concept-request-url)entry's [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url)[client](https://fetch.spec.whatwg.org/#concept-request-client)sourceSnapshotParams's [fetch client](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-client)[destination](https://fetch.spec.whatwg.org/#concept-request-destination)"`document`" The destination is updated below when navigable has a [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container).[credentials mode](https://fetch.spec.whatwg.org/#concept-request-credentials-mode)"`include`"[use-URL-credentials flag](https://fetch.spec.whatwg.org/#concept-request-use-url-credentials-flag)set[redirect mode](https://fetch.spec.whatwg.org/#concept-request-redirect-mode)"`manual`"[replaces client id](https://fetch.spec.whatwg.org/#concept-request-replaces-client-id)navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [id](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-id)[mode](https://fetch.spec.whatwg.org/#concept-request-mode)"`navigate`"[referrer](https://fetch.spec.whatwg.org/#concept-request-referrer)entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [request referrer](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer)[referrer policy](https://fetch.spec.whatwg.org/#concept-request-referrer-policy)entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [request referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer-policy)[policy container](https://fetch.spec.whatwg.org/#concept-request-policy-container)sourceSnapshotParams's [source policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-policy-container)[traversable for user prompts](https://fetch.spec.whatwg.org/#concept-request-window)navigable's [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-top)
4.   If navigable is a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable), then set request's [top-level navigation initiator origin](https://fetch.spec.whatwg.org/#request-top-level-navigation-initiator-origin) to entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin).

5.   If request's [client](https://fetch.spec.whatwg.org/#concept-request-client) is null:

This [only occurs](https://html.spec.whatwg.org/multipage/browsing-the-web.html#assert-null-sourcedocument) in the case of a browser UI-initiated navigation.

    1.   Set request's [origin](https://fetch.spec.whatwg.org/#concept-request-origin) to a new [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque).

    2.   Set request's [service-workers mode](https://fetch.spec.whatwg.org/#request-service-workers-mode) to "`all`".

    3.   Set request's [referrer](https://fetch.spec.whatwg.org/#concept-request-referrer) to "`no-referrer`".

6.   If documentResource is a [POST resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#post-resource):

    1.   Set request's [method](https://fetch.spec.whatwg.org/#concept-request-method) to ``POST``.

    2.   Set request's [body](https://fetch.spec.whatwg.org/#concept-request-body) to documentResource's [request body](https://html.spec.whatwg.org/multipage/browsing-the-web.html#post-resource-request-body).

    3.   [Set](https://fetch.spec.whatwg.org/#concept-header-list-set) ``Content-Type`` to documentResource's [request content-type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#post-resource-request-content-type) in request's [header list](https://fetch.spec.whatwg.org/#concept-request-header-list).

7.   If entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending) is true, then set request's [reload-navigation flag](https://fetch.spec.whatwg.org/#concept-request-reload-navigation-flag).

8.   Otherwise, if entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [ever populated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-ever-populated) is true, then set request's [history-navigation flag](https://fetch.spec.whatwg.org/#concept-request-history-navigation-flag).

9.   If sourceSnapshotParams's [has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-activation) is true, then set request's [user-activation](https://fetch.spec.whatwg.org/#request-user-activation) to true.

10.   If navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container) is non-null:

    1.   If the navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container) has a [browsing context scope origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#browsing-context-scope-origin), then set request's [origin](https://fetch.spec.whatwg.org/#concept-request-origin) to that [browsing context scope origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#browsing-context-scope-origin).

    2.   Set request's [destination](https://fetch.spec.whatwg.org/#concept-request-destination) to navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container)'s [local name](https://dom.spec.whatwg.org/#concept-element-local-name).

    3.   If sourceSnapshotParams's [fetch client](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-client) is navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object), then set request's [initiator type](https://fetch.spec.whatwg.org/#request-initiator-type) to navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container)'s [local name](https://dom.spec.whatwg.org/#concept-element-local-name).

This ensure that only container-initiated navigations are reported to resource timing.

11.   Let response be null.

12.   Let responseOrigin be null.

13.   Let fetchController be null.

14.   Let coopEnforcementResult be a new [opener policy enforcement result](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-result), with

[url](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-url)navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [URL](https://dom.spec.whatwg.org/#concept-document-url)[origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin)navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin)[opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-coop)navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [opener policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-coop)[current context is navigation source](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-source)true if navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin) otherwise false
15.   Let finalSandboxFlags be an empty [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set).

16.   Let responsePolicyContainer be null.

17.   Let responseCOOP be a new [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy).

18.   Let locationURL be null.

19.   Let currentURL be request's [current URL](https://fetch.spec.whatwg.org/#concept-request-current-url).

20.   Let commitEarlyHints be null.

21.   While true:

    1.   If request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client) is not null and currentURL's [origin](https://url.spec.whatwg.org/#concept-url-origin) is not the [same](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) as request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client)'s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url)'s [origin](https://url.spec.whatwg.org/#concept-url-origin), then:

        1.   Run the [environment discarding steps](https://html.spec.whatwg.org/multipage/webappapis.html#environment-discarding-steps) for request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client).

        2.   Set request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client) to null.

        3.   Set commitEarlyHints to null.

Preloaded links from [early hint headers](https://html.spec.whatwg.org/multipage/semantics.html#early-hints-2) remain in the preload cache after a [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) redirect, but get discarded when the redirect is cross-origin.

    2.   If request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client) is null, then:

        1.   Let topLevelCreationURL be currentURL.

        2.   Let topLevelOrigin be null.

        3.   If navigable is not a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable), then:

            1.   Let parentEnvironment be navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

            2.   Set topLevelCreationURL to parentEnvironment's [top-level creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-creation-url).

            3.   Set topLevelOrigin to parentEnvironment's [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin).

        4.   Set request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client) to a new [environment](https://html.spec.whatwg.org/multipage/webappapis.html#environment) whose [id](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-id) is a unique opaque string, [target browsing context](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-target-browsing-context) is navigable's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc), [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url) is currentURL, [top-level creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-creation-url) is topLevelCreationURL, and [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin) is topLevelOrigin.

The created environment's [active service worker](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-active-service-worker) is set in the [Handle Fetch](https://w3c.github.io/ServiceWorker/#on-fetch-request-algorithm) algorithm during the fetch if the request URL matches a service worker registration. [[SW]](https://html.spec.whatwg.org/multipage/references.html#refsSW)

    3.   If the result of [should navigation request of type be blocked by Content Security Policy?](https://w3c.github.io/webappsec-csp/#should-block-navigation-request) given request and cspNavigationType is "`Blocked`", then set response to a [network error](https://fetch.spec.whatwg.org/#concept-network-error) and [break](https://infra.spec.whatwg.org/#iteration-break). [[CSP]](https://html.spec.whatwg.org/multipage/references.html#refsCSP)

    4.   Set response to null.

    5.   If fetchController is null, then set fetchController to the result of [fetching](https://fetch.spec.whatwg.org/#concept-fetch)request, with _[processEarlyHintsResponse](https://fetch.spec.whatwg.org/#fetch-processearlyhintsresponse)_ set to processEarlyHintsResponse as defined below, _[processResponse](https://fetch.spec.whatwg.org/#process-response)_ set to processResponse as defined below, and _[useParallelQueue](https://fetch.spec.whatwg.org/#fetch-useparallelqueue)_ set to true.

Let processEarlyHintsResponse be the following algorithm given a [response](https://fetch.spec.whatwg.org/#concept-response)earlyResponse:

        1.   If commitEarlyHints is null, then set commitEarlyHints to the result of [processing early hint headers](https://html.spec.whatwg.org/multipage/semantics.html#process-early-hint-headers) given earlyResponse and request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client).

Let processResponse be the following algorithm given a [response](https://fetch.spec.whatwg.org/#concept-response)fetchedResponse:

        1.   Set response to fetchedResponse.

    6.   Otherwise, [process the next manual redirect](https://fetch.spec.whatwg.org/#fetch-controller-process-the-next-manual-redirect) for fetchController.

This will result in calling the _[processResponse](https://fetch.spec.whatwg.org/#process-response)_ we supplied above, during our first iteration through the loop, and thus setting response.

Navigation handles redirects manually as navigation is the only place in the web platform that cares for redirects to `mailto:` URLs and such.

    7.   Wait until either response is non-null, or navigable's [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation) changes to no longer equal navigationId.

If the latter condition occurs, then [abort](https://fetch.spec.whatwg.org/#fetch-controller-abort)fetchController, and return.

Otherwise, proceed onward.

    8.   If request's [body](https://fetch.spec.whatwg.org/#concept-request-body) is null, then set entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource) to null.

Fetch unsets the [body](https://fetch.spec.whatwg.org/#concept-request-body) for particular redirects.

    9.   Set responsePolicyContainer to the result of [creating a policy container from a fetch response](https://html.spec.whatwg.org/multipage/browsers.html#creating-a-policy-container-from-a-fetch-response) given response and request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client).

    10.   Set finalSandboxFlags to the [union](https://infra.spec.whatwg.org/#set-union) of targetSnapshotParams's [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params-sandbox) and responsePolicyContainer's [CSP list](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-csp-list)'s [CSP-derived sandboxing flags](https://html.spec.whatwg.org/multipage/browsers.html#csp-derived-sandboxing-flags).

    11.   Set responseOrigin to the result of [determining the origin](https://html.spec.whatwg.org/multipage/document-sequences.html#determining-the-origin) given response's [URL](https://fetch.spec.whatwg.org/#concept-response-url), finalSandboxFlags, and entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin).

If response is a redirect, then response's [URL](https://fetch.spec.whatwg.org/#concept-response-url) will be the URL that led to the redirect to response's [location URL](https://fetch.spec.whatwg.org/#concept-response-location-url); it will not be the [location URL](https://fetch.spec.whatwg.org/#concept-response-location-url) itself.

    12.   If navigable is a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable), then:

        1.   Set responseCOOP to the result of [obtaining an opener policy](https://html.spec.whatwg.org/multipage/browsers.html#obtain-coop) given response and request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client).

        2.   Set coopEnforcementResult to the result of [enforcing the response's opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforce) given navigable's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc), response's [URL](https://fetch.spec.whatwg.org/#concept-response-url), responseOrigin, responseCOOP, coopEnforcementResult, and request's [referrer](https://fetch.spec.whatwg.org/#concept-request-referrer).

        3.   If finalSandboxFlags is not empty and responseCOOP's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value) is not "`unsafe-none`", then set response to an appropriate [network error](https://fetch.spec.whatwg.org/#concept-network-error) and [break](https://infra.spec.whatwg.org/#iteration-break).

This results in a network error as one cannot simultaneously provide a clean slate to a response using opener policy and sandbox the result of navigating to that response.

    13.   If response is not a [network error](https://fetch.spec.whatwg.org/#concept-network-error), navigable is a [child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable), and the result of performing a [cross-origin resource policy check](https://fetch.spec.whatwg.org/#cross-origin-resource-policy-check) with navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin), navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object), request's [destination](https://fetch.spec.whatwg.org/#concept-request-destination), response, and true is **blocked**, then set response to a [network error](https://fetch.spec.whatwg.org/#concept-network-error) and [break](https://infra.spec.whatwg.org/#iteration-break).

Here we're running the [cross-origin resource policy check](https://fetch.spec.whatwg.org/#cross-origin-resource-policy-check) against the [parent navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) rather than navigable itself. This is because we care about the same-originness of the embedded content against the parent context, not the navigation source.

    14.   Set locationURL to response's [location URL](https://fetch.spec.whatwg.org/#concept-response-location-url) given currentURL's [fragment](https://url.spec.whatwg.org/#concept-url-fragment).

    15.   If locationURL is failure or null, then [break](https://infra.spec.whatwg.org/#iteration-break).

    16.   [Assert](https://infra.spec.whatwg.org/#assert): locationURL is a [URL](https://url.spec.whatwg.org/#concept-url).

    17.   Set entry's [classic history API state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-classic-history-api-state) to [StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage)(null).

    18.   Let oldDocState be entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state).

    19.   Set entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state) to a new [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-2), with

[history policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-history-policy-container)a [clone](https://html.spec.whatwg.org/multipage/browsers.html#clone-a-policy-container) of the oldDocState's [history policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-history-policy-container) if it is non-null; null otherwise[request referrer](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer)oldDocState's [request referrer](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer)[request referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer-policy)oldDocState's [request referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer-policy)[initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin)oldDocState's [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin)[origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin)oldDocState's [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin)[about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-about-base-url)oldDocState's [about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-about-base-url)[resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource)oldDocState's [resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource)[ever populated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-ever-populated)oldDocState's [ever populated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-ever-populated)[navigable target name](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nav-target-name)oldDocState's [navigable target name](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nav-target-name)
For the navigation case, only entry referenced oldDocState, which was created [early in the navigate algorithm](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-create-document-state). So for navigations, this is functionally just an update to entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state). For the traversal case, it's possible adjacent [session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) also reference oldDocState, in which case they will continue doing so even after we've updated entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state).

oldDocState's [history policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-history-policy-container) is only ever non-null here in the traversal case, after we've populated it during a navigation to a URL that [requires storing the policy container in history](https://html.spec.whatwg.org/multipage/browsers.html#requires-storing-the-policy-container-in-history).

The setup is given by the following [Jake diagram](https://html.spec.whatwg.org/multipage/document-sequences.html#jake-diagram):

|  | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- |
| `top` | /a | /a#foo | /a#bar | /b |

Also assume that the [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state) shared by the entries in steps 0, 1, and 2 has a null [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document), i.e., [bfcache](https://html.spec.whatwg.org/multipage/browsing-the-web.html#note-bfcache) is not in play.

Now consider the scenario where we traverse back to step 2, but this time when fetching `/a`, the server responds with a ``Location`` header pointing to `/c`. That is, locationURL points to `/c` and so we have reached this step instead of [breaking](https://infra.spec.whatwg.org/#iteration-break) out of the loop.

In this case, we replace the [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state) of the [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) occupying step 2, but we do _not_ replace the document state of the entries occupying steps 0 and 1. The resulting [Jake diagram](https://html.spec.whatwg.org/multipage/document-sequences.html#jake-diagram) looks like this:

|  | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- |
| `top` | /a | /a#foo | /c#bar | /b |

Note that we perform this replacement even if we end up in a redirect chain back to the original URL, for example if `/c` itself had a ``Location`` header pointing to `/a`. Such a case would end up like so:

|  | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- |
| `top` | /a | /a#foo | /a#bar | /b | 
    20.   If locationURL's [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is not an [HTTP(S) scheme](https://fetch.spec.whatwg.org/#http-scheme), then:

        1.   Set entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-resource) to null.

        2.   [Break](https://infra.spec.whatwg.org/#iteration-break).

    21.   Set currentURL to locationURL.

    22.   Set entry's [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url) to currentURL.

By the end of this loop we will be in one of these scenarios:

    *   locationURL is failure, because of an unparseable ``Location`` header.

    *   locationURL is null, either because response is a [network error](https://fetch.spec.whatwg.org/#concept-network-error) or because we successfully fetched a non-[network error](https://fetch.spec.whatwg.org/#concept-network-error) HTTP(S) response with no ``Location`` header.

    *   locationURL is a [URL](https://url.spec.whatwg.org/#concept-url) with a non-[HTTP(S)](https://fetch.spec.whatwg.org/#http-scheme)[scheme](https://url.spec.whatwg.org/#concept-url-scheme).

22.   If locationURL is a [URL](https://url.spec.whatwg.org/#concept-url) whose [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is not a [fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme), then return a new [non-fetch scheme navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-navigation-params), with

[id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-id)navigationId[navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-navigable)navigable[URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-url)locationURL[target snapshot sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-target-sandbox)targetSnapshotParams's [sandboxing flags](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-snapshot-params-sandbox)[source snapshot has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-source-activation)sourceSnapshotParams's [has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-activation)[initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-initiator-origin)responseOrigin[navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-nav-timing-type)navTimingType[user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#non-fetch-scheme-params-user-involvement)userInvolvement
At this point, request's [current URL](https://fetch.spec.whatwg.org/#concept-request-current-url) is the last [URL](https://url.spec.whatwg.org/#concept-url) in the redirect chain with a [fetch](https://fetch.spec.whatwg.org/#fetch-scheme)[scheme](https://url.spec.whatwg.org/#concept-url-scheme) before redirecting to a non-[fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme)[URL](https://url.spec.whatwg.org/#concept-url). It is this [URL](https://url.spec.whatwg.org/#concept-url)'s [origin](https://url.spec.whatwg.org/#concept-url-origin) that will be used as the initiator origin for navigations to non-[fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme)[URLs](https://url.spec.whatwg.org/#concept-url).

23.   If any of the following are true:

    *   response is a [network error](https://fetch.spec.whatwg.org/#concept-network-error);

    *   locationURL is failure; or

    *   locationURL is a [URL](https://url.spec.whatwg.org/#concept-url) whose [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is a [fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme),

then return null.

We allow redirects to non-[fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme)[URLs](https://url.spec.whatwg.org/#concept-url), but redirects to [fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme)[URLs](https://url.spec.whatwg.org/#concept-url) that aren't [HTTP(S)](https://fetch.spec.whatwg.org/#http-scheme) are treated like network errors.

24.   [Assert](https://infra.spec.whatwg.org/#assert): locationURL is null and response is not a [network error](https://fetch.spec.whatwg.org/#concept-network-error).

25.   Let resultPolicyContainer be the result of [determining navigation params policy container](https://html.spec.whatwg.org/multipage/browsers.html#determining-navigation-params-policy-container) given response's [URL](https://fetch.spec.whatwg.org/#concept-response-url), entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [history policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-history-policy-container), sourceSnapshotParams's [source policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-policy-container), null, and responsePolicyContainer.

26.   If navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container) is an `iframe`, and response's [timing allow passed flag](https://fetch.spec.whatwg.org/#concept-response-timing-allow-passed) is set, then set navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container)'s [pending resource-timing start time](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-pending-resource-timing-start-time) to null.

If the `iframe` is allowed to report to resource timing, we don't need to run its fallback steps as the normal reporting would happen.

27.   Return a new [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params), with

[id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-id)navigationId[navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable)navigable[request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request)request[response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)response[fetch controller](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-fetch-controller)fetchController[commit early hints](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-commit-early-hints)commitEarlyHints[opener policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop)responseCOOP[reserved environment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-reserved-environment)request's [reserved client](https://fetch.spec.whatwg.org/#concept-request-reserved-client)[origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin)responseOrigin[policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-policy-container)resultPolicyContainer[final sandboxing flag set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-sandboxing)finalSandboxFlags[COOP enforcement result](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop-enforcement-result)coopEnforcementResult[navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-nav-timing-type)navTimingType[about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-about-base-url)entry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-about-base-url)[user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-user-involvement)userInvolvement

This definition is broken and needs investigation to see what it was intended to express: see [issue #4703](https://github.com/whatwg/html/issues/4703).

To load a document given [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params)navigationParams, [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params)sourceSnapshotParams, and [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)initiatorOrigin, perform the following steps. They return a `Document` or null.

1.   Let type be the [computed type](https://mimesniff.spec.whatwg.org/#computed-mime-type) of navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response).

2.   If the user agent has been configured to process resources of the given type using some mechanism other than rendering the content in a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable), then skip this step. Otherwise, if the type is one of the following types:

an [HTML MIME type](https://mimesniff.spec.whatwg.org/#html-mime-type)Return the result of [loading an HTML document](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-html), given navigationParams.an [XML MIME type](https://mimesniff.spec.whatwg.org/#xml-mime-type) that is not an [explicitly supported XML MIME type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#explicitly-supported-xml-mime-type)Return the result of [loading an XML document](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-xml) given navigationParams and type.a [JavaScript MIME type](https://mimesniff.spec.whatwg.org/#javascript-mime-type)a [JSON MIME type](https://mimesniff.spec.whatwg.org/#json-mime-type) that is not an [explicitly supported JSON MIME type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#explicitly-supported-json-mime-type)"`text/css`""`text/plain`""`text/vtt`"Return the result of [loading a text document](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-text) given navigationParams and type."`multipart/x-mixed-replace`"Return the result of [loading a `multipart/x-mixed-replace` document](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-multipart-x-mixed-replace), given navigationParams, sourceSnapshotParams, and initiatorOrigin.a supported image, video, or audio type Return the result of [loading a media document](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-media) given navigationParams and type."`application/pdf`""`text/pdf`"If the user agent's [PDF viewer supported](https://html.spec.whatwg.org/multipage/system-state.html#pdf-viewer-supported) is true, return the result of [creating a document for inline content that doesn't have a DOM](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-ua-inline) given navigationParams's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable), navigationParams's [id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-id), navigationParams's [navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-nav-timing-type), and navigationParams's [user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-user-involvement).
Otherwise, proceed onward.

An explicitly supported XML MIME type is an [XML MIME type](https://mimesniff.spec.whatwg.org/#xml-mime-type) for which the user agent is configured to use an external application to render the content, or for which the user agent has dedicated processing rules. For example, a web browser with a built-in Atom feed viewer would be said to explicitly support the `application/atom+xml` MIME type.

An explicitly supported JSON MIME type is a [JSON MIME type](https://mimesniff.spec.whatwg.org/#json-mime-type) for which the user agent is configured to use an external application to render the content, or for which the user agent has dedicated processing rules.

In both cases, the external application or user agent will either [display the content inline](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-ua-inline) directly in navigationParams's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable), or [hand it off to external software](https://html.spec.whatwg.org/multipage/browsing-the-web.html#hand-off-to-external-software). Both happen in the steps below.

3.   If, given type, the new resource is to be handled by displaying some sort of inline content, e.g., a native rendering of the content or an error message because the specified type is not supported, then return the result of [creating a document for inline content that doesn't have a DOM](https://html.spec.whatwg.org/multipage/document-lifecycle.html#navigate-ua-inline) given navigationParams's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable), navigationParams's [id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-id), navigationParams's [navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-nav-timing-type), and navigationParams's [user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-user-involvement).

4.   Otherwise, the document's type is such that the resource will not affect navigationParams's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable), e.g., because the resource is to be handed to an external application or because it is an unknown type that will be processed by [handle as a download](https://html.spec.whatwg.org/multipage/links.html#handle-as-a-download). [Hand-off to external software](https://html.spec.whatwg.org/multipage/browsing-the-web.html#hand-off-to-external-software) given navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response), navigationParams's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable), navigationParams's [final sandboxing flag set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-sandboxing), sourceSnapshotParams's [has transient activation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params-activation), and initiatorOrigin.

5.   Return null.

#### 7.4.6 Applying the history step[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#applying-the-history-step)

For both navigation and traversal, once we have an idea of where we want to head to in the session history, much of the work comes about in applying that notion to the [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable) and the relevant `Document`. For navigations, this work generally occurs toward the end of the process; for traversals, it is the beginning.

##### 7.4.6.1 Updating the traversable[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#updating-the-traversable)

Ensuring a [traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable) ends up at the right session history step is particularly complex, as it can involve coordinating across multiple [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) descendants of the traversable, [populating](https://html.spec.whatwg.org/multipage/browsing-the-web.html#populating-a-session-history-entry) them in parallel, and then synchronizing back up to ensure everyone has the same view of the result. This is further complicated by the existence of synchronous same-document navigations being mixed together with cross-document navigations, and how web pages have come to have certain relative timing expectations.

A changing navigable continuation state is used to store information during the [apply the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step) algorithm, allowing parts of the algorithm to continue only after other parts have finished. It is a [struct](https://infra.spec.whatwg.org/#struct) with:

displayed document A `Document`target entry A [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)navigable A [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)update only A boolean

* * *

Although all updates to the [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable) end up in the same [apply the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step) algorithm, each possible entry point comes along with some minor customizations:

To apply the push/replace history step given a non-negative integer step to a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, given a [history handling behavior](https://html.spec.whatwg.org/multipage/browsing-the-web.html#history-handling-behavior)historyHandling and a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement:

1.   Return the result of [applying the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step)step to traversable given false, null, null, userInvolvement, and historyHandling.

[Apply the push/replace history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-push/replace-history-step) never passes [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params) or an initiator [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) to [apply the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step). This is because those checks are done earlier in the [navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm.

[Apply the reload history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-reload-history-step) never passes [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params) or an initiator [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) to [apply the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step). This is because reloading is always treated as if it were done by the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) itself, even in cases like `parent.location.reload()`.

To apply the traverse history step given a non-negative integer step to a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, with [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params)sourceSnapshotParams, [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)initiatorToCheck, and [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement:

1.   Return the result of [applying the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step)step to traversable given true, sourceSnapshotParams, initiatorToCheck, userInvolvement, and "`traverse`".

To resume applying the traverse history step given a non-negative integer step, a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, and [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement, [apply](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step)step to traversable given false, null, null, userInvolvement, and "`traverse`".

When resuming a traverse, we are already past the cancelation, initiator, and source snapshot checks, and this traversal has already been determined to be a same-document traversal. Hence, we can pass false and null for those arguments.

* * *

Now for the algorithm itself.

To apply the history step given a non-negative integer step to a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, with boolean checkForCancelation, [source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#source-snapshot-params)-or-null sourceSnapshotParams, [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)-or-null initiatorToCheck, [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement, and `NavigationType`-or-null navigationType, perform the following steps. They return "`initiator-disallowed`", "`canceled-by-beforeunload`", "`canceled-by-navigate`", or "`applied`".

1.   [Assert](https://infra.spec.whatwg.org/#assert): This is running within traversable's [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue).

2.   Let targetStep be the result of [getting the used step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-the-used-step) given traversable and step.

3.   If initiatorToCheck is not null, then:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): sourceSnapshotParams is not null.

    2.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigable of [get all navigables whose current session history entry will change or reload](https://html.spec.whatwg.org/multipage/browsing-the-web.html#get-all-navigables-whose-current-session-history-entry-will-change-or-reload): if initiatorToCheck is not [allowed by sandboxing to navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#allowed-to-navigate)navigable given sourceSnapshotParams, then return "`initiator-disallowed`".

4.   Let navigablesCrossingDocuments be the result of [getting all navigables that might experience a cross-document traversal](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-all-navigables-that-might-experience-a-cross-document-traversal) given traversable and targetStep.

5.   If checkForCancelation is true, and the result of [checking if unloading is canceled](https://html.spec.whatwg.org/multipage/browsing-the-web.html#checking-if-unloading-is-canceled) given navigablesCrossingDocuments, traversable, targetStep, and userInvolvement is not "`continue`", then return that result.

6.   Let changingNavigables be the result of [get all navigables whose current session history entry will change or reload](https://html.spec.whatwg.org/multipage/browsing-the-web.html#get-all-navigables-whose-current-session-history-entry-will-change-or-reload) given traversable and targetStep.

7.   Let nonchangingNavigablesThatStillNeedUpdates be the result of [getting all navigables that only need history object length/index update](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-all-navigables-that-only-need-history-object-length/index-update) given traversable and targetStep.

8.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigable of changingNavigables:

    1.   Let targetEntry be the result of [getting the target history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-the-target-history-entry) given navigable and targetStep.

    2.   Set navigable's [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry) to targetEntry.

    3.   [Set the ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#set-the-ongoing-navigation) for navigable to "`traversal`".

9.   Let totalChangeJobs be the [size](https://infra.spec.whatwg.org/#list-size) of changingNavigables.

10.   Let completedChangeJobs be 0.

11.   Let changingNavigableContinuations be an empty [queue](https://infra.spec.whatwg.org/#queue) of [changing navigable continuation states](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-navigable-continuation-state).

This queue is used to split the operations on changingNavigables into two parts. Specifically, changingNavigableContinuations holds data for the [second part](https://html.spec.whatwg.org/multipage/browsing-the-web.html#continuations-dequeue).

12.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigable of changingNavigables, [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) of navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to run the steps:

This set of steps are split into two parts to allow synchronous navigations to be processed before documents unload. State is stored in changingNavigableContinuations for the [second part](https://html.spec.whatwg.org/multipage/browsing-the-web.html#continuations-dequeue).

    1.   Let displayedEntry be navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry).

    2.   Let targetEntry be navigable's [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry).

    3.   Let changingNavigableContinuation be a [changing navigable continuation state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-navigable-continuation-state) with:

[displayed document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-displayed-document)displayedEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)[target entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-target-entry)targetEntry[navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-navigable)navigable[update-only](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-update-only)false
    4.   If displayedEntry is targetEntry and targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending) is false, then:

        1.   Set changingNavigableContinuation's [update-only](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-update-only) to true.

        2.   [Enqueue](https://infra.spec.whatwg.org/#queue-enqueue)changingNavigableContinuation on changingNavigableContinuations.

        3.   Abort these steps.

This case occurs due to a [synchronous navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#finalize-a-same-document-navigation) which already updated the [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry).

    5.   Switch on navigationType:

"`reload`"
[Assert](https://infra.spec.whatwg.org/#assert): targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending) is true.

"`traverse`"
[Assert](https://infra.spec.whatwg.org/#assert): targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [ever populated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-ever-populated) is true.

"`replace`"
[Assert](https://infra.spec.whatwg.org/#assert): targetEntry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) is displayedEntry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) and targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [ever populated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-ever-populated) is false.

"`push`"
[Assert](https://infra.spec.whatwg.org/#assert): targetEntry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) is displayedEntry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) + 1 and targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [ever populated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-ever-populated) is false.

    6.   Let oldOrigin be targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin).

    7.   If all of the following are true:

        *   navigable is not traversable;

        *   targetEntry is not navigable's [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry); and

        *   oldOrigin is the [same](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) as navigable's [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry)'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin),

then:

        1.   Let navigation be navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window)'s [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window-navigation-api).

        2.   [Fire a traverse `navigate` event](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-a-traverse-navigate-event) at navigation given targetEntry and userInvolvement.

    8.   If targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) is null, or targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending) is true, then:

        1.   Let navTimingType be "`back_forward`" if targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) is null; otherwise "`reload`".

        2.   Let targetSnapshotParams be the result of [snapshotting target snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#snapshotting-target-snapshot-params) given navigable.

        3.   Let potentiallyTargetSpecificSourceSnapshotParams be sourceSnapshotParams.

        4.   If potentiallyTargetSpecificSourceSnapshotParams is null, then set it to the result of [snapshotting source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#snapshotting-source-snapshot-params) given navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

In this case there is no clear source of the traversal/reload. We treat this situation as if navigable navigated itself, but note that some properties of targetEntry's original initiator are preserved in targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state), such as the [initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin) and [referrer](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-request-referrer), which will appropriately influence the navigation.

        5.   Set targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending) to false.

        6.   Let allowPOST be targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending).

        7.   [In parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel), [attempt to populate the history entry's document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-the-history-entry's-document) for targetEntry, given navigable, potentiallyTargetSpecificSourceSnapshotParams, targetSnapshotParams, userInvolvement, with _[allowPOST](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-allow-post)_ set to allowPOST and [_completionSteps_](https://html.spec.whatwg.org/multipage/browsing-the-web.html#attempt-to-populate-completion-steps) set to [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to run afterDocumentPopulated.

Otherwise, run afterDocumentPopulated[immediately](https://html.spec.whatwg.org/multipage/infrastructure.html#immediately).

In both cases, let afterDocumentPopulated be the following steps:

        1.   If targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) is null, then set changingNavigableContinuation's [update-only](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-update-only) to true.

This means we tried to populate the document, but were unable to do so, e.g. because of the server returning a 204.

These kinds of failed navigations or traversals will not be signaled to the [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-api) (e.g., through the promises of any [navigation API method tracker](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-api-method-tracker), or the `navigateerror` event). Doing so would leak information about the timing of responses from other origins, in the cross-origin case, and providing different results in the cross-origin vs. same-origin cases was deemed too confusing.

However, implementations could use this opportunity to clear any promise handlers for the `navigation.transition.finished` promise, as they are guaranteed at this point to never run. And, they might wish to [report a warning to the console](https://console.spec.whatwg.org/#report-a-warning-to-the-console) if any part of the navigation API initiated these navigations, to make it clear to the web developer why their promises will never settle and events will never fire. 
        2.   If targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is not oldOrigin, then set targetEntry's [classic history API state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-classic-history-api-state) to [StructuredSerializeForStorage](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializeforstorage)(null).

This clears history state when the origin changed vs a previous load of targetEntry without a redirect occuring. This can happen due to a change in CSP sandbox headers.

        3.   If all of the following are true:

            *   navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) is null;

            *   targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc) is not an [auxiliary browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#auxiliary-browsing-context) whose [opener browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-browsing-context) is non-null; and

            *   targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is not oldOrigin,

then set targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [navigable target name](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nav-target-name) to the empty string.

        4.   [Enqueue](https://infra.spec.whatwg.org/#queue-enqueue)changingNavigableContinuation on changingNavigableContinuations.

The rest of this job [runs later](https://html.spec.whatwg.org/multipage/browsing-the-web.html#continuations-dequeue) in this algorithm.

13.   Let navigablesThatMustWaitBeforeHandlingSyncNavigation be an empty [set](https://infra.spec.whatwg.org/#ordered-set).

14.   While completedChangeJobs does not equal totalChangeJobs:

    1.   If traversable's [running nested apply history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-running-nested-apply-history-step) is false, then:

        1.   While traversable's [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue)'s [algorithm set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-algorithm-set)[contains](https://infra.spec.whatwg.org/#list-contain) one or more [synchronous navigation steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-sync-nav-steps) with a [target navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-sync-nav-steps-target-nav) not [contained](https://infra.spec.whatwg.org/#list-contain) in navigablesThatMustWaitBeforeHandlingSyncNavigation:

            1.   Let steps be the first [item](https://infra.spec.whatwg.org/#list-item) in traversable's [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue)'s [algorithm set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-algorithm-set) that is [synchronous navigation steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-sync-nav-steps) with a [target navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-sync-nav-steps-target-nav) not [contained](https://infra.spec.whatwg.org/#list-contain) in navigablesThatMustWaitBeforeHandlingSyncNavigation.

            2.   [Remove](https://infra.spec.whatwg.org/#list-remove)steps from traversable's [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue)'s [algorithm set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue-algorithm-set).

            3.   Set traversable's [running nested apply history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-running-nested-apply-history-step) to true.

            4.   Run steps.

            5.   Set traversable's [running nested apply history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-running-nested-apply-history-step) to false.

Synchronous navigations that are intended to take place before this traversal jump the queue at this point, so they can be added to the correct place in traversable's [session history entries](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries) before this traversal potentially unloads their document. [More details can be found here](https://html.spec.whatwg.org/multipage/browsing-the-web.html#sync-navigation-steps-queue-jumping-examples).

    2.   Let changingNavigableContinuation be the result of [dequeuing](https://infra.spec.whatwg.org/#queue-dequeue) from changingNavigableContinuations.

    3.   If changingNavigableContinuation is nothing, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    4.   Let displayedDocument be changingNavigableContinuation's [displayed document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-displayed-document).

    5.   Let targetEntry be changingNavigableContinuation's [target entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-target-entry).

    6.   Let navigable be changingNavigableContinuation's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-navigable).

    7.   Let (scriptHistoryLength, scriptHistoryIndex) be the result of [getting the history object length and index](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-the-history-object-length-and-index) given traversable and targetStep.

These values might have changed since they were last calculated.

    8.   [Append](https://infra.spec.whatwg.org/#list-append)navigable to navigablesThatMustWaitBeforeHandlingSyncNavigation.

Once a navigable has reached this point in traversal, additionally queued synchronous navigation steps are likely to be intended to occur after this traversal rather than before it, so they no longer jump the queue. [More details can be found here](https://html.spec.whatwg.org/multipage/browsing-the-web.html#sync-navigation-steps-queue-jumping-examples).

    9.   Let entriesForNavigationAPI be the result of [getting session history entries for the navigation API](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-session-history-entries-for-the-navigation-api) given navigable and targetStep.

    10.   If changingNavigableContinuation's [update-only](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-update-only) is true, or targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) is displayedDocument, then:

This is a same-document navigation: we proceed without unloading.

        1.   [Set the ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#set-the-ongoing-navigation) for navigable to null.

This allows new [navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) of navigable to start, whereas during the traversal they were blocked.

        2.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to perform afterPotentialUnloads.

    11.   Otherwise:

        1.   [Assert](https://infra.spec.whatwg.org/#assert): navigationType is not null.

        2.   [Deactivate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#deactivate-a-document-for-a-cross-document-navigation)displayedDocument, given userInvolvement, targetEntry, navigationType, and afterPotentialUnloads.

    12.   In both cases, let afterPotentialUnloads be the following steps:

        1.   Let previousEntry be navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry).

        2.   If changingNavigableContinuation's [update-only](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-update-only) is false, then [activate history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#activate-history-entry)targetEntry for navigable.

        3.   Let updateDocument be an algorithm step which performs [update document for history step application](https://html.spec.whatwg.org/multipage/browsing-the-web.html#update-document-for-history-step-application) given targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document), targetEntry, changingNavigableContinuation's [update-only](https://html.spec.whatwg.org/multipage/browsing-the-web.html#changing-nav-continuation-update-only), scriptHistoryLength, scriptHistoryIndex, navigationType, entriesForNavigationAPI, and previousEntry.

        4.   If targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) is equal to displayedDocument, then perform updateDocument.

        5.   Otherwise, [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to perform updateDocument.

        6.   Increment completedChangeJobs.

15.   Let totalNonchangingJobs be the [size](https://infra.spec.whatwg.org/#list-size) of nonchangingNavigablesThatStillNeedUpdates.

This step onwards deliberately waits for all the previous operations to complete, as they include [processing synchronous navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#sync-navigations-jump-queue) which will also post tasks to update history length and index.

16.   Let completedNonchangingJobs be 0.

17.   Let (scriptHistoryLength, scriptHistoryIndex) be the result of [getting the history object length and index](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-the-history-object-length-and-index) given traversable and targetStep.

18.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigable of nonchangingNavigablesThatStillNeedUpdates, [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to run the steps:

    1.   Let document be navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

    2.   Set document's [history object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#doc-history)'s [index](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-index) to scriptHistoryIndex.

    3.   Set document's [history object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#doc-history)'s [length](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-length) to scriptHistoryLength.

    4.   Increment completedNonchangingJobs.

19.   Wait for completedNonchangingJobs to equal totalNonchangingJobs.

20.   Set traversable's [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) to targetStep.

21.   Return "`applied`".

To deactivate a document for a cross-document navigation given a `Document`displayedDocument, a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userNavigationInvolvement, a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)targetEntry, a `NavigationType`navigationType, and afterPotentialUnloads, which is an algorithm that receives no arguments:

1.   Let navigable be displayedDocument's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable).

2.   Let potentiallyTriggerViewTransition be false.

3.   Let isBrowserUINavigation be true if userNavigationInvolvement is "`browser UI`"; otherwise false.

4.   Set potentiallyTriggerViewTransition to the result of calling [can navigation trigger a cross-document view-transition?](https://drafts.csswg.org/css-view-transitions-2/#can-navigation-trigger-a-cross-document-view-transition) given displayedDocument, targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document), navigationType, and isBrowserUINavigation.

5.   If potentiallyTriggerViewTransition is false, then:

    1.   Let firePageSwapBeforeUnload be the following step:

        1.   [Fire the `pageswap` event](https://html.spec.whatwg.org/multipage/browsing-the-web.html#fire-the-pageswap-event) given displayedDocument, targetEntry, navigationType, and null.

    2.   [Set the ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#set-the-ongoing-navigation) for navigable to null.

This allows new [navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) of navigable to start, whereas during the traversal they were blocked.

    3.   [Unload a document and its descendants](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-a-document-and-its-descendants) given displayedDocument, targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document), afterPotentialUnloads, and firePageSwapBeforeUnload.

6.   Otherwise, [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given navigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to run the steps:

    1.   Let proceedWithNavigationAfterViewTransitionCapture be the following step:

        1.   [Append the following session history traversal steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-traversal-steps) to navigable's [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable):

            1.   [Set the ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#set-the-ongoing-navigation) for navigable to null.

This allows new [navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) of navigable to start, whereas during the traversal they were blocked.

            2.   [Unload a document and its descendants](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-a-document-and-its-descendants) given displayedDocument, targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document), and afterPotentialUnloads.

    2.   Let viewTransition be the result of [setting up a cross-document view-transition](https://drafts.csswg.org/css-view-transitions-2/#setup-cross-document-view-transition) given displayedDocument, targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document), navigationType, and proceedWithNavigationAfterViewTransitionCapture.

    3.   [Fire the `pageswap` event](https://html.spec.whatwg.org/multipage/browsing-the-web.html#fire-the-pageswap-event) given displayedDocument, targetEntry, navigationType, and viewTransition.

    4.   If viewTransition is null, then run proceedWithNavigationAfterViewTransitionCapture.

In the case where a view transition started, the view transitions algorithms are responsible for calling proceedWithNavigationAfterViewTransitionCapture.

To fire the `pageswap` event given a `Document`displayedDocument, a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)targetEntry, a `NavigationType`navigationType, and a `ViewTransition`-or-null viewTransition:

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running as part of a [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) queued on displayedDocument's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop).

2.   Let navigation be displayedDocument's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window-navigation-api).

3.   Let activation be null.

4.   If all of the following are true:

    *   targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with displayedDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin); and

    *   targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [was created via cross-origin redirects](https://html.spec.whatwg.org/multipage/dom.html#was-created-via-cross-origin-redirects) is false, or targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [latest entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#latest-entry) is not null,

then:

    1.   Let destinationEntry be determined by switching on navigationType:

"`reload`"
The [current entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-current-entry) of navigation

"`traverse`"
The `NavigationHistoryEntry` in navigation's [entry list](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-entry-list) whose [session history entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nhe-she) is targetEntry

"`push`""`replace`"
A new `NavigationHistoryEntry` in displayedDocument's [relevant realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-realm) with its [session history entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nhe-she) set to targetEntry

    2.   Set activation to a [new](https://webidl.spec.whatwg.org/#new)`NavigationActivation` created in displayedDocument's [relevant realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-realm), with

[old entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nav-activation-old-entry)the [current entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-current-entry) of navigation[new entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nav-activation-new-entry)destinationEntry[navigation type](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nav-activation-navigation-type)navigationType

This means that a cross-origin redirect during a navigation would result in a null `activation` in the old document's `PageSwapEvent`, unless the new document is being restored from [bfcache](https://html.spec.whatwg.org/multipage/browsing-the-web.html#note-bfcache).

5.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `pageswap` at displayedDocument's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), using `PageSwapEvent` with its `activation` set to activation, and its `viewTransition` set to viewTransition.

To get the used step given a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, and a non-negative integer step, perform the following steps. They return a non-negative integer.

1.   Let steps be the result of [getting all used history steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-all-used-history-steps) within traversable.

2.   Return the greatest [item](https://infra.spec.whatwg.org/#list-item) in steps that is less than or equal to step.

This caters for situations where there's no [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) with [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step)step, due to the removal of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable).

To get the history object length and index given a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, and a non-negative integer step, perform the following steps. They return a [tuple](https://infra.spec.whatwg.org/#tuple) of two non-negative integers.

1.   Let steps be the result of [getting all used history steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-all-used-history-steps) within traversable.

2.   Let scriptHistoryLength be the [size](https://infra.spec.whatwg.org/#list-size) of steps.

3.   [Assert](https://infra.spec.whatwg.org/#assert): steps[contains](https://infra.spec.whatwg.org/#list-contain)step.

It is assumed that step has been adjusted by [getting the used step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-the-used-step).

4.   Let scriptHistoryIndex be the index of step in steps.

5.   Return (scriptHistoryLength, scriptHistoryIndex).

To get all navigables whose current session history entry will change or reload given a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, and a non-negative integer targetStep, perform the following steps. They return a [list](https://infra.spec.whatwg.org/#list) of [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable).

1.   Let results be an empty [list](https://infra.spec.whatwg.org/#list).

2.   Let navigablesToCheck be « traversable ».

This list is extended in the loop below.

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigable of navigablesToCheck:

    1.   Let targetEntry be the result of [getting the target history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-the-target-history-entry) given navigable and targetStep.

    2.   If targetEntry is not navigable's [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry) or targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending) is true, then [append](https://infra.spec.whatwg.org/#list-append)navigable to results.

    3.   If targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) is navigable's [document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document), and targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending) is false, then [extend](https://infra.spec.whatwg.org/#list-extend)navigablesToCheck with the [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) of navigable.

Adding [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) to navigablesToCheck means those navigables will also be checked by this loop. [Child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) are only checked if the navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) will not change as part of this traversal.

4.   Return results.

To get all navigables that only need history object length/index update given a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, and a non-negative integer targetStep, perform the following steps. They return a [list](https://infra.spec.whatwg.org/#list) of [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable).

Other [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) might not be impacted by the traversal. For example, if the response is a 204, the currently active document will remain. Additionally, going 'back' after a 204 will change the [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry), but the [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) will already be correct.

1.   Let results be an empty [list](https://infra.spec.whatwg.org/#list).

2.   Let navigablesToCheck be « traversable ».

This list is extended in the loop below.

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigable of navigablesToCheck:

    1.   Let targetEntry be the result of [getting the target history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-the-target-history-entry) given navigable and targetStep.

    2.   If targetEntry is navigable's [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry) and targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending) is false, then:

        1.   [Append](https://infra.spec.whatwg.org/#list-append)navigable to results.

        2.   [Extend](https://infra.spec.whatwg.org/#list-extend)navigablesToCheck with navigable's [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable).

Adding [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) to navigablesToCheck means those navigables will also be checked by this loop. [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) are only checked if the navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) will not change as part of this traversal.

4.   Return results.

To get the target history entry given a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, and a non-negative integer step, perform the following steps. They return a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry).

1.   Let entries be the result of [getting session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-session-history-entries) for navigable.

2.   Return the [item](https://infra.spec.whatwg.org/#list-item) in entries that has the greatest [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) less than or equal to step.

To see why [getting the target history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-the-target-history-entry) returns the entry with the greatest [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) less than or equal to the input step, consider the following [Jake diagram](https://html.spec.whatwg.org/multipage/document-sequences.html#jake-diagram):

|  | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- |
| `top` | /t | /t#foo |
| `frames[0]` | /i-0-a | /i-0-b |

For the input step 1, the target history entry for the `top` navigable is the `/t` entry, whose [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) is 0, while the target history entry for the `frames[0]` navigable is the `/i-0-b` entry, whose [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) is 1:

|  | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- |
| `top` | /t | /t#foo |
| `frames[0]` | /i-0-a | /i-0-b |

Similarly, given the input step 3 we get the `top` entry whose [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) is 3, and the `frames[0]` entry whose [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) is 1:

|  | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- |
| `top` | /t | /t#foo |
| `frames[0]` | /i-0-a | /i-0-b |

To get all navigables that might experience a cross-document traversal given a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable)traversable, and a non-negative integer targetStep, perform the following steps. They return a [list](https://infra.spec.whatwg.org/#list) of [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable).

From traversable's [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue)'s perspective, these documents are candidates for going cross-document during the traversal described by targetStep. They will not experience a cross-document traversal if the status code for their target document is HTTP 204 No Content.

Note that if a given [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) might experience a cross-document traversal, this algorithm will return [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) but not its [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable). Those would end up [unloaded](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-a-document), not traversed.

1.   Let results be an empty [list](https://infra.spec.whatwg.org/#list).

2.   Let navigablesToCheck be « traversable ».

This list is extended in the loop below.

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigable of navigablesToCheck:

    1.   Let targetEntry be the result of [getting the target history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-the-target-history-entry) given navigable and targetStep.

    2.   If targetEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) is not navigable's [document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) or targetEntry's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [reload pending](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-reload-pending) is true, then [append](https://infra.spec.whatwg.org/#list-append)navigable to results.

Although navigable's [active history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) can change synchronously, the new entry will always have the same `Document`, so accessing navigable's [document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) is reliable.

    3.   Otherwise, [extend](https://infra.spec.whatwg.org/#list-extend)navigablesToCheck with navigable's [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable).

Adding [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) to navigablesToCheck means those navigables will also be checked by this loop. [Child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) are only checked if the navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) will not change as part of this traversal.

4.   Return results.

##### 7.4.6.2 Updating the document[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#updating-the-document)

To update document for history step application given a `Document`document, a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)entry, a boolean doNotReactivate, integers scriptHistoryLength and scriptHistoryIndex, `NavigationType`-or-null navigationType, an optional [list](https://infra.spec.whatwg.org/#list) of [session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)entriesForNavigationAPI, and an optional [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)previousEntryForActivation:

1.   Let documentIsNew be true if document's [latest entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#latest-entry) is null; otherwise false.

2.   Let documentsEntryChanged be true if document's [latest entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#latest-entry) is not entry; otherwise false.

3.   Set document's [history object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#doc-history)'s [index](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-index) to scriptHistoryIndex.

4.   Set document's [history object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#doc-history)'s [length](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-length) to scriptHistoryLength.

5.   Let navigation be history's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window-navigation-api).

6.   If documentsEntryChanged is true, then:

    1.   Let oldURL be document's [latest entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#latest-entry)'s [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url).

    2.   Set document's [latest entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#latest-entry) to entry.

    3.   [Restore the history object state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restore-the-history-object-state) given document and entry.

    4.   If documentIsNew is false, then:

        1.   [Assert](https://infra.spec.whatwg.org/#assert): navigationType is not null.

        2.   [Update the navigation API entries for a same-document navigation](https://html.spec.whatwg.org/multipage/nav-history-apis.html#update-the-navigation-api-entries-for-a-same-document-navigation) given navigation, entry, and navigationType.

        3.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `popstate` at document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), using `PopStateEvent`, with the `state` attribute initialized to document's [history object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#doc-history)'s [state](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-history-state) and `hasUAVisualTransition` initialized to true if a visual transition, to display a cached rendered state of the [latest entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#latest-entry), was done by the user agent.

        4.   [Restore persisted state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restore-persisted-state) given entry.

        5.   If oldURL's [fragment](https://url.spec.whatwg.org/#concept-url-fragment) is not equal to entry's [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url)'s [fragment](https://url.spec.whatwg.org/#concept-url-fragment), then [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `hashchange` at document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), using `HashChangeEvent`, with the `oldURL` attribute initialized to the [serialization](https://url.spec.whatwg.org/#concept-url-serializer) of oldURL and the `newURL` attribute initialized to the [serialization](https://url.spec.whatwg.org/#concept-url-serializer) of entry's [URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url).

    5.   Otherwise:

        1.   [Assert](https://infra.spec.whatwg.org/#assert): entriesForNavigationAPI is given.

        2.   [Restore persisted state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restore-persisted-state) given entry.

        3.   [Initialize the navigation API entries for a new document](https://html.spec.whatwg.org/multipage/nav-history-apis.html#initialize-the-navigation-api-entries-for-a-new-document) given navigation, entriesForNavigationAPI, and entry.

7.   If all the following are true:

    *   previousEntryForActivation is given;

    *   navigationType is non-null; and

    *   navigationType is "`reload`" or previousEntryForActivation's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) is not document,

then:

    1.   If navigation's [activation](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-activation) is null, then set navigation's [activation](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-activation) to a new `NavigationActivation` object in navigation's [relevant realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-realm).

    2.   Let previousEntryIndex be the result of [getting the navigation API entry index](https://html.spec.whatwg.org/multipage/nav-history-apis.html#getting-the-navigation-api-entry-index) of previousEntryForActivation within navigation.

    3.   If previousEntryIndex is non-negative, then set activation's [old entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nav-activation-old-entry) to navigation's [entry list](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-entry-list)[previousEntryIndex].

    4.   Otherwise, if all the following are true:

        *   navigationType is "`replace`";

        *   previousEntryForActivation's [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin) is [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with document's [origin](https://dom.spec.whatwg.org/#concept-document-origin); and

        *   previousEntryForActivation's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank) is false,

then set activation's [old entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nav-activation-old-entry) to a new `NavigationHistoryEntry` in navigation's [relevant realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-realm), whose [session history entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nhe-she) is previousEntryForActivation.

    5.   Set activation's [new entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nav-activation-new-entry) to navigation's [current entry](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-current-entry).

    6.   Set activation's [navigation type](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nav-activation-navigation-type) to navigationType.

8.   If documentIsNew is true, then:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): document's [during-loading navigation ID for WebDriver BiDi](https://html.spec.whatwg.org/multipage/dom.html#concept-document-navigation-id) is not null.

    2.   Invoke [WebDriver BiDi navigation committed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-committed) with navigable and a new [WebDriver BiDi navigation status](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-status) whose [id](https://w3c.github.io/webdriver-bidi/#navigation-status-id) is document's [during-loading navigation ID for WebDriver BiDi](https://html.spec.whatwg.org/multipage/dom.html#concept-document-navigation-id), [status](https://w3c.github.io/webdriver-bidi/#navigation-status-status) is "`committed`", and [url](https://w3c.github.io/webdriver-bidi/#navigation-status-url) is document's [URL](https://dom.spec.whatwg.org/#concept-document-url).

    3.   [Try to scroll to the fragment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#try-to-scroll-to-the-fragment) for document.

    4.   At this point scripts may run for the newly-created document document.

9.   Otherwise, if documentsEntryChanged is false and doNotReactivate is false, then:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): entriesForNavigationAPI is given.

    2.   [Reactivate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reactivate-a-document)document given entry and entriesForNavigationAPI.

documentsEntryChanged can be false for one of two reasons: either we are restoring from [bfcache](https://html.spec.whatwg.org/multipage/browsing-the-web.html#note-bfcache), or we are asynchronously finishing up a synchronous navigation which already synchronously set document's [latest entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#latest-entry). The doNotReactivate argument distinguishes between these two cases.

To make active a `Document`document:

1.   Let window be document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global).

2.   Set document's [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc)'s `WindowProxy`'s [[[Window]]](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-windowproxy-window) internal slot value to window.

3.   Set document's [visibility state](https://html.spec.whatwg.org/multipage/interaction.html#visibility-state) to document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable)'s [system visibility state](https://html.spec.whatwg.org/multipage/document-sequences.html#system-visibility-state).

4.   [Queue](https://w3c.github.io/performance-timeline/#queue-a-performanceentry) a new `VisibilityStateEntry` whose [visibility state](https://html.spec.whatwg.org/multipage/interaction.html#visibilitystateentry-state) is document's [visibility state](https://html.spec.whatwg.org/multipage/interaction.html#visibility-state) and whose [timestamp](https://html.spec.whatwg.org/multipage/interaction.html#visibilitystateentry-timestamp) is zero.

5.   Set window's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [execution ready flag](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-execution-ready-flag).

To reactivate a `Document`document given a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)reactivatedEntry and a [list](https://infra.spec.whatwg.org/#list) of [session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)entriesForNavigationAPI:

This algorithm updates document after it has come out of [bfcache](https://html.spec.whatwg.org/multipage/browsing-the-web.html#note-bfcache), i.e., after it has been made [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active) again. Other specifications that want to watch for this change to the [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active) state are encouraged to add steps into this algorithm, so that the ordering of events that happen in effect of the change is clear.

1.   [For each](https://infra.spec.whatwg.org/#list-iterate)formControl of form controls in document with an [autofill field name](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill-field-name) of "`off`", invoke the [reset algorithm](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-reset-control) for formControl.

2.   If document's [suspended timer handles](https://html.spec.whatwg.org/multipage/document-lifecycle.html#suspended-timer-handles) is not [empty](https://infra.spec.whatwg.org/#list-is-empty):

    1.   [Assert](https://infra.spec.whatwg.org/#assert): document's [suspension time](https://html.spec.whatwg.org/multipage/document-lifecycle.html#suspension-time) is not zero.

    2.   Let suspendDuration be the [current high resolution time](https://w3c.github.io/hr-time/#dfn-current-high-resolution-time) minus document's [suspension time](https://html.spec.whatwg.org/multipage/document-lifecycle.html#suspension-time).

    3.   Let activeTimers be document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [map of active timers](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-active-timers).

    4.   For each handle in document's [suspended timer handles](https://html.spec.whatwg.org/multipage/document-lifecycle.html#suspended-timer-handles), if activeTimers[handle] [exists](https://infra.spec.whatwg.org/#map-exists), then increase activeTimers[handle] by suspendDuration.

3.   [Update the navigation API entries for reactivation](https://html.spec.whatwg.org/multipage/nav-history-apis.html#update-the-navigation-api-entries-for-reactivation) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window-navigation-api), entriesForNavigationAPI, and reactivatedEntry.

4.   If document's [current document readiness](https://html.spec.whatwg.org/multipage/dom.html#current-document-readiness) is "`complete`", and document's [page showing](https://html.spec.whatwg.org/multipage/document-lifecycle.html#page-showing) is false:

    1.   Set document's [page showing](https://html.spec.whatwg.org/multipage/document-lifecycle.html#page-showing) to true.

    2.   Set document's [has been revealed](https://html.spec.whatwg.org/multipage/browsing-the-web.html#has-been-revealed) to false.

    3.   [Update the visibility state](https://html.spec.whatwg.org/multipage/interaction.html#update-the-visibility-state) of document to "`visible`".

    4.   [Fire a page transition event](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-a-page-transition-event) named `pageshow` at document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) with true.

To try to scroll to the fragment for a `Document`document, perform the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

1.   Wait for an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) amount of time. (This is intended to allow the user agent to optimize the user experience in the face of performance concerns.)

2.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to run these steps:

    1.   If document has no parser, or its parser has [stopped parsing](https://html.spec.whatwg.org/multipage/parsing.html#stop-parsing), or the user agent has reason to believe the user is no longer interested in scrolling to the [fragment](https://url.spec.whatwg.org/#concept-url-fragment), then abort these steps.

    2.   [Scroll to the fragment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scroll-to-the-fragment-identifier) given document.

    3.   If document's [indicated part](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-indicated-part-of-the-document) is still null, then [try to scroll to the fragment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#try-to-scroll-to-the-fragment) for document.

To build not restored reasons for document state given `Document`document:

1.   Let notRestoredReasonsForDocument be a new [not restored reasons](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-struct).

2.   Set notRestoredReasonsForDocument's [URL](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-url) to document's [URL](https://dom.spec.whatwg.org/#concept-document-url).

3.   Let container be document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container).

4.   If container is an `iframe` element:

    1.   Let src be the empty string.

    2.   If container has a `src` attribute:

        1.   Let src be the result of [encoding-parsing-and-serializing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-and-serializing-a-url) given container's `src` attribute's value, relative to container's [node document](https://dom.spec.whatwg.org/#concept-node-document).

        2.   If src is failure, then set src to container's `src` attribute's value.

    3.   Set notRestoredReasonsForDocument's [src](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-src) to src.

    4.   Set notRestoredReasonsForDocument's [id](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-id) to container's `id` attribute's value, or the empty string if it has no such attribute.

    5.   Set notRestoredReasonsForDocument's [name](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-name) to container's `name` attribute's value, or the empty string if it has no such attribute.

5.   Set notRestoredReasonsForDocument's [reasons](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-reasons) to a [clone](https://infra.spec.whatwg.org/#list-clone) of document's [bfcache blocking details](https://html.spec.whatwg.org/multipage/dom.html#concept-document-bfcache-blocking-details).

6.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigable of document's [document-tree child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#document-tree-child-navigables):

    1.   Let childDocument be navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

    2.   [Build not restored reasons for document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#build-not-restored-reasons-for-document-state) given childDocument.

    3.   [Append](https://infra.spec.whatwg.org/#list-append)childDocument's [not restored reasons](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-nrr) to notRestoredReasonsForDocument's [children](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-children).

7.   Set document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [not restored reasons](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-not-restored-reasons) to notRestoredReasonsForDocument.

To build not restored reasons for a top-level traversable and its descendants given [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable)topLevelTraversable:

1.   [Build not restored reasons for document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#build-not-restored-reasons-for-document-state) given topLevelTraversable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

2.   Let crossOriginDescendants be an empty [list](https://infra.spec.whatwg.org/#list).

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)childNavigable of topLevelTraversable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [descendant navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#descendant-navigables):

    1.   If childNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is not [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with topLevelTraversable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin), then [append](https://infra.spec.whatwg.org/#list-append)childNavigable to crossOriginDescendants.

4.   Let crossOriginDescendantsPreventsBfcache be false.

5.   [For each](https://infra.spec.whatwg.org/#list-iterate)crossOriginNavigable of crossOriginDescendants:

    1.   Let reasonsForCrossOriginChild be crossOriginNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-2)'s [not restored reasons](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-not-restored-reasons).

    2.   If reasonsForCrossOriginChild's [reasons](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-reasons) is not empty, set crossOriginDescendantsPreventsBfcache to true.

    3.   Set reasonsForCrossOriginChild's [URL](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-url) to null.

    4.   Set reasonsForCrossOriginChild's [reasons](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-reasons) to null.

    5.   Set reasonsForCrossOriginChild's [children](https://html.spec.whatwg.org/multipage/nav-history-apis.html#nrr-children) to null.

6.   If crossOriginDescendantsPreventsBfcache is true, [make document unsalvageable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#make-document-unsalvageable) given topLevelTraversable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) and "`masked`".

##### 7.4.6.3 Revealing the document[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#revealing-the-document)

A `Document` has a boolean has been revealed, initially false. It is used to ensure that the event is fired once for each activation of the `Document` (once when it's rendered initially, and once for each [reactivation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#reactivate-a-document)).

To reveal a `Document`document:

1.   If document's [has been revealed](https://html.spec.whatwg.org/multipage/browsing-the-web.html#has-been-revealed) is true, then return.

2.   Set document's [has been revealed](https://html.spec.whatwg.org/multipage/browsing-the-web.html#has-been-revealed) to true.

3.   Let transition be the result of [resolving inbound cross-document view-transition](https://drafts.csswg.org/css-view-transitions-2/#resolve-inbound-cross-document-view-transition) for document.

4.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named at document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), using with its set to transition.

5.   If transition is not null, then:

    1.   [Prepare to run script](https://html.spec.whatwg.org/multipage/webappapis.html#prepare-to-run-script) given document's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

    2.   [Activate](https://drafts.csswg.org/css-view-transitions/#activate-view-transition)transition.

    3.   [Clean up after running script](https://html.spec.whatwg.org/multipage/webappapis.html#clean-up-after-running-script) given document's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

Activating a view transition might resolve/reject promises, so by wrapping the activation with prepare/cleanup we ensure those promises are handled before the next rendering step.

Though is guaranteed to be fired during the first [update the rendering](https://html.spec.whatwg.org/multipage/webappapis.html#update-the-rendering) step that displays an up-to-date version of the page, user agents are free to display a cached frame of the page before firing it. This prevents the presence of a handler from delaying the presentation of such cached frame.

##### 7.4.6.4 Scrolling to a fragment[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scrolling-to-a-fragment)

To scroll to the fragment given a `Document`document:

1.   If document's [indicated part](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-indicated-part-of-the-document) is null, then set document's [target element](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-element) to null.

2.   Otherwise, if document's [indicated part](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-indicated-part-of-the-document) is [top of the document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#top-of-the-document), then:

    1.   Set document's [target element](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-element) to null.

    2.   [Scroll to the beginning of the document](https://drafts.csswg.org/cssom-view/#scroll-to-the-beginning-of-the-document) for document. [[CSSOMVIEW]](https://html.spec.whatwg.org/multipage/references.html#refsCSSOMVIEW)

    3.   Return.

3.   Otherwise:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): document's [indicated part](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-indicated-part-of-the-document) is an element.

    2.   Let target be document's [indicated part](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-indicated-part-of-the-document).

    3.   Set document's [target element](https://html.spec.whatwg.org/multipage/browsing-the-web.html#target-element) to target.

    4.   Run the [ancestor revealing algorithm](https://html.spec.whatwg.org/multipage/interaction.html#ancestor-revealing-algorithm) on target.

    5.   [Scroll target into view](https://drafts.csswg.org/cssom-view/#scroll-a-target-into-view), with _behavior_ set to "auto", _block_ set to "start", and _inline_ set to "nearest". [[CSSOMVIEW]](https://html.spec.whatwg.org/multipage/references.html#refsCSSOMVIEW)

    6.   Run the [focusing steps](https://html.spec.whatwg.org/multipage/interaction.html#focusing-steps) for target, with the `Document`'s [viewport](https://drafts.csswg.org/css2/#viewport) as the _fallback target_.

    7.   Move the [sequential focus navigation starting point](https://html.spec.whatwg.org/multipage/interaction.html#sequential-focus-navigation-starting-point) to target.

A `Document`'s indicated part is the one that its [URL](https://dom.spec.whatwg.org/#concept-document-url)'s [fragment](https://url.spec.whatwg.org/#concept-url-fragment) identifies, or null if the fragment does not identify anything. The semantics of the [fragment](https://url.spec.whatwg.org/#concept-url-fragment) in terms of mapping it to a node is defined by the specification that defines the [MIME type](https://mimesniff.spec.whatwg.org/#mime-type) used by the `Document` (for example, the processing of [fragments](https://url.spec.whatwg.org/#concept-url-fragment) for [XML MIME types](https://mimesniff.spec.whatwg.org/#xml-mime-type) is the responsibility of RFC7303). [[RFC7303]](https://html.spec.whatwg.org/multipage/references.html#refsRFC7303)

There is also a target element for each `Document`, which is used in defining the `:target` pseudo-class and is updated by the above algorithm. It is initially null.

For an [HTML document](https://dom.spec.whatwg.org/#html-document)document, its [indicated part](https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-indicated-part-of-the-document) is the result of [selecting the indicated part](https://html.spec.whatwg.org/multipage/browsing-the-web.html#select-the-indicated-part) given document and document's [URL](https://dom.spec.whatwg.org/#concept-document-url).

To select the indicated part given a `Document`document and a [URL](https://url.spec.whatwg.org/#concept-url)url:

1.   If document's [URL](https://dom.spec.whatwg.org/#concept-document-url) does not [equal](https://url.spec.whatwg.org/#concept-url-equals)url with _[exclude fragments](https://url.spec.whatwg.org/#url-equals-exclude-fragments)_ set to true, then return null.

2.   Let fragment be url's [fragment](https://url.spec.whatwg.org/#concept-url-fragment).

3.   If fragment is the empty string, then return the special value top of the document.

4.   Let potentialIndicatedElement be the result of [finding a potential indicated element](https://html.spec.whatwg.org/multipage/browsing-the-web.html#find-a-potential-indicated-element) given document and fragment.

5.   If potentialIndicatedElement is not null, then return potentialIndicatedElement.

6.   Let fragmentBytes be the result of [percent-decoding](https://url.spec.whatwg.org/#string-percent-decode)fragment.

7.   Let decodedFragment be the result of running [UTF-8 decode without BOM](https://encoding.spec.whatwg.org/#utf-8-decode-without-bom) on fragmentBytes.

8.   Set potentialIndicatedElement to the result of [finding a potential indicated element](https://html.spec.whatwg.org/multipage/browsing-the-web.html#find-a-potential-indicated-element) given document and decodedFragment.

9.   If potentialIndicatedElement is not null, then return potentialIndicatedElement.

10.   If decodedFragment is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string `top`, then return the [top of the document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#top-of-the-document).

11.   Return null.

To find a potential indicated element given a `Document`document and a string fragment, run these steps:

1.   If there is an element [in the document tree](https://dom.spec.whatwg.org/#in-a-document-tree) whose [root](https://dom.spec.whatwg.org/#concept-tree-root) is document and that has an [ID](https://dom.spec.whatwg.org/#concept-id) equal to fragment, then return the first such element in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

2.   If there is an `a` element [in the document tree](https://dom.spec.whatwg.org/#in-a-document-tree) whose [root](https://dom.spec.whatwg.org/#concept-tree-root) is document that has a `name` attribute whose value is equal to fragment, then return the first such element in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

3.   Return null.

##### 7.4.6.5 Persisted history entry state[](https://html.spec.whatwg.org/multipage/browsing-the-web.html#persisted-user-state-restoration)

To save persisted state to a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)entry:

1.   Set the [scroll position data](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-scroll-position) of entry to contain the scroll positions for all of entry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [restorable scrollable regions](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restorable-scrollable-regions).

2.   Optionally, update entry's [persisted user state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-other) to reflect any state that the user agent wishes to persist, such as the values of form fields.

To restore persisted state from a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)entry:

1.   If entry's [scroll restoration mode](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-scroll-restoration-mode) is "`auto`", and entry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [navigation API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#window-navigation-api)'s [suppress normal scroll restoration during ongoing navigation](https://html.spec.whatwg.org/multipage/nav-history-apis.html#suppress-normal-scroll-restoration-during-ongoing-navigation) is false, then [restore scroll position data](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restore-scroll-position-data) given entry.

The user agent not restoring scroll positions does not imply that scroll positions will be left at any particular value (e.g., (0,0)). The actual scroll position depends on the navigation type and the user agent's particular caching strategy. So web applications cannot assume any particular scroll position but rather are urged to set it to what they want it to be.

If [suppress normal scroll restoration during ongoing navigation](https://html.spec.whatwg.org/multipage/nav-history-apis.html#suppress-normal-scroll-restoration-during-ongoing-navigation) is true, then [restoring scroll position data](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restore-scroll-position-data) might still happen at a later point, as part of [finishing](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigateevent-finish) the relevant `NavigateEvent`, or via a `navigateEvent.scroll()` method call.

2.   Optionally, update other aspects of entry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document) and its rendering, for instance values of form fields, that the user agent had previously recorded in entry's [persisted user state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-other).

This can even include updating the `dir` attribute of `textarea` elements or `input` elements whose `type` attribute is in the [Text](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)), [Search](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)), [Telephone](https://html.spec.whatwg.org/multipage/input.html#telephone-state-(type=tel)), [URL](https://html.spec.whatwg.org/multipage/input.html#url-state-(type=url)), or [Email](https://html.spec.whatwg.org/multipage/input.html#email-state-(type=email)) state, if the persisted state includes the directionality of user input in such controls.

Restoring the value of form controls as part of this process does not fire any `input` or `change` events, but can trigger the `formStateRestoreCallback` of [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element).

* * *

Each `Document` has a boolean has been scrolled by the user, initially false. If the user scrolls the document, the user agent must set that document's [has been scrolled by the user](https://html.spec.whatwg.org/multipage/browsing-the-web.html#has-been-scrolled-by-the-user) to true.

The restorable scrollable regions of a `Document`document are document's [viewport](https://drafts.csswg.org/css2/#viewport), and all of document's scrollable regions excepting any [navigable containers](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-container).

[Child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) scroll restoration is handled as part of state restoration for the [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) for those [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)' `Document`s.

To restore scroll position data given a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry)entry:

1.   Let document be entry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document).

2.   If document's [has been scrolled by the user](https://html.spec.whatwg.org/multipage/browsing-the-web.html#has-been-scrolled-by-the-user) is true, then the user agent should return.

3.   The user agent should attempt to use entry's [scroll position data](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-scroll-position) to restore the scroll positions of entry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document)'s [restorable scrollable regions](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restorable-scrollable-regions). The user agent may continue to attempt to do so periodically, until document's [has been scrolled by the user](https://html.spec.whatwg.org/multipage/browsing-the-web.html#has-been-scrolled-by-the-user) becomes true.

This is formulated as an _attempt_, which is potentially repeated until success or until the user scrolls, due to the fact that relevant content indicated by the [scroll position data](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-scroll-position) might take some time to load from the network.

Scroll restoration might be affected by scroll anchoring. [[CSSSCROLLANCHORING]](https://html.spec.whatwg.org/multipage/references.html#refsCSSSCROLLANCHORING)

[← 7.3 Infrastructure for sequences of documents](https://html.spec.whatwg.org/multipage/document-sequences.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [7.5 Document lifecycle →](https://html.spec.whatwg.org/multipage/document-lifecycle.html)
