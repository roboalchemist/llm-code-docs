# Source: https://html.spec.whatwg.org/multipage/document-sequences.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/document-sequences.html

Published Time: Mon, 16 Mar 2026 07:32:48 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 7.2 APIs related to navigation and session history](https://html.spec.whatwg.org/multipage/nav-history-apis.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [7.4 Navigation and session history →](https://html.spec.whatwg.org/multipage/browsing-the-web.html)
1.       1.   [7.3 Infrastructure for sequences of documents](https://html.spec.whatwg.org/multipage/document-sequences.html#infrastructure-for-sequences-of-documents)
        1.   [7.3.1 Navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigables)
            1.   [7.3.1.1 Traversable navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigables)
            2.   [7.3.1.2 Top-level traversables](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversables)
            3.   [7.3.1.3 Child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigables)
            4.   [7.3.1.4 Jake diagrams](https://html.spec.whatwg.org/multipage/document-sequences.html#jake-diagrams)
            5.   [7.3.1.5 Related navigable collections](https://html.spec.whatwg.org/multipage/document-sequences.html#related-navigable-collections)
            6.   [7.3.1.6 Navigable destruction](https://html.spec.whatwg.org/multipage/document-sequences.html#garbage-collection-and-browsing-contexts)
            7.   [7.3.1.7 Navigable target names](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-target-names)

        2.   [7.3.2 Browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#windows)
            1.   [7.3.2.1 Creating browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-browsing-contexts)
            2.   [7.3.2.2 Related browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#nested-browsing-contexts)
            3.   [7.3.2.3 Groupings of browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#groupings-of-browsing-contexts)

        3.   [7.3.3 Fully active documents](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active-documents)

### 7.3 Infrastructure for sequences of documents[](https://html.spec.whatwg.org/multipage/document-sequences.html#infrastructure-for-sequences-of-documents)

This standard contains several related concepts for grouping sequences of documents. As a brief, non-normative summary:

*   [Navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) are a user-facing representation of a sequence of documents, i.e., they represent something that can be navigated between documents. Typical examples are tabs or windows in a web browser, or `iframe`s, or `frame`s in a `frameset`.

*   [Traversable navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable) are a special type of navigable which control the session history of themselves and of their descendant navigables. That is, in addition to their own series of documents, they represent a tree of further series of documents, plus the ability to linearly traverse back and forward through a flattened view of this tree.

*   [Browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) are a developer-facing representation of a series of documents. They correspond 1:1 with `WindowProxy` objects. Each navigable can present a series of browsing contexts, with [switches](https://html.spec.whatwg.org/multipage/browsers.html#browsing-context-group-switches-due-to-cross-origin-opener-policy) between those browsing contexts occuring under certain well-defined circumstances.

Most of this standard works in the language of navigables, but certain APIs expose the existence of browsing context switches, and so some parts of the standard need to work in terms of browsing contexts.

#### 7.3.1 Navigables[](https://html.spec.whatwg.org/multipage/document-sequences.html#navigables)

A navigable presents a `Document` to the user via its [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry). Each navigable has:

*   An id, a [new unique internal value](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#new-unique-internal-value).

*   A parent, a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) or null.

*   A current session history entry, a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry).

This can only be modified within the [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue) of the parent [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable).

*   An active session history entry, a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry).

This can only be modified from the event loop of the [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document).

*   An is closing boolean, initially false.

This is only ever set to true for [top-level traversable navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable).

*   An is delaying `load` events boolean, initially false.

This is only ever set to true in cases where the navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) is non-null.

The [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry) and the [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) are usually the same, but they get out of sync when:

*   Synchronous navigations are performed. This causes the [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) to temporarily step ahead of the [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry).

*   A non-displayable, non-error response is received when [applying the history step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#apply-the-history-step). This updates the [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry) but leaves the [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) as-is.

* * *

A [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)'s active document is its [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document).

This can be safely read from within the [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue) of the navigable's [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-top). Although a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)'s [active history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) can change synchronously, the new entry will always have the same `Document`.

A [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)'s active browsing context is its [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc). If this [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) is a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable), then its [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc) will be a [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context).

A [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)'s active `WindowProxy` is its [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc)'s associated `WindowProxy`.

This will always equal the navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global); this is kept in sync by the [make active](https://html.spec.whatwg.org/multipage/browsing-the-web.html#make-active) algorithm.

* * *

To get the node navigable of a [node](https://dom.spec.whatwg.org/#interface-node)node, return the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) whose [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) is node's [node document](https://dom.spec.whatwg.org/#concept-node-document), or null if there is no such [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable).

* * *

To initialize the navigable[navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, given a [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-2)documentState and an optional [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)-or-null parent (default null):

1.   [Assert](https://infra.spec.whatwg.org/#assert): documentState's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) is non-null.

2.   Let entry be a new [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry), with

[URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-url)documentState's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document)'s [URL](https://dom.spec.whatwg.org/#concept-document-url)[document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)documentState
The caller of this algorithm is responsible for initializing entry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step); it will be left as "`pending`" until that is complete.

3.   Set navigable's [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry) to entry.

4.   Set navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) to entry.

5.   Set navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) to parent.

##### 7.3.1.1 Traversable navigables[](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigables)

A traversable navigable is a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) that also controls which [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) should be the [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry) and [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry) for itself and its descendant [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable).

In addition to the properties of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable), a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable) has:

*   A current session history step, a number, initially 0.

*   Session history entries, a [list](https://infra.spec.whatwg.org/#list) of [session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry), initially a new [list](https://infra.spec.whatwg.org/#list).

*   A session history traversal queue, a [session history traversal parallel queue](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-traversal-parallel-queue), the result of [starting a new session history traversal parallel queue](https://html.spec.whatwg.org/multipage/browsing-the-web.html#starting-a-new-session-history-traversal-parallel-queue).

*   A running nested apply history step boolean, initially false.

*   A system visibility state, which is either "`hidden`" or "`visible`".

See the [page visibility](https://html.spec.whatwg.org/multipage/interaction.html#page-visibility) section for the requirements on this item.

*   An is created by web content boolean, initially false.

To get the traversable navigable of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)inputNavigable:

1.   Let navigable be inputNavigable.

2.   While navigable is not a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable), set navigable to navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent).

3.   Return navigable.

##### 7.3.1.2 Top-level traversables[](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversables)

A top-level traversable is a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable) with a null [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent).

Currently, all [traversable navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable) are [top-level traversables](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable). Future proposals envision introducing non-top-level traversables.

A user agent holds a top-level traversable set (a [set](https://infra.spec.whatwg.org/#ordered-set) of [top-level traversables](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable)). These are typically presented to the user in the form of browser windows or browser tabs.

To get the top-level traversable of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)inputNavigable:

1.   Let navigable be inputNavigable.

2.   While navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) is not null, set navigable to navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent).

3.   Return navigable.

To create a fresh top-level traversable given a [URL](https://url.spec.whatwg.org/#concept-url)initialNavigationURL and an optional [POST resource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#post-resource)-or-null initialNavigationPostResource (default null):

1.   Let traversable be the result of [creating a new top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-top-level-traversable) given null and the empty string.

2.   [Navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate)traversable to initialNavigationURL using traversable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document), with _[documentResource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-resource)_ set to initialNavigationPostResource.

We treat these initial navigations as traversable navigating itself, which will ensure all relevant security checks pass.

3.   Return traversable.

##### 7.3.1.3 Child navigables[](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigables)

Certain elements (for example, `iframe` elements) can present a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) to the user. These elements are called navigable containers.

Each [navigable container](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-container) has a content navigable, which is either a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) or null. It is initially null.

The container of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable is the [navigable container](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-container) whose [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is navigable, or null if there is no such element.

The container document of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable is the result of running these steps:

1.   If navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container) is null, then return null.

2.   Return navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container)'s [node document](https://dom.spec.whatwg.org/#concept-node-document).

This is equal to navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container)'s [shadow-including root](https://dom.spec.whatwg.org/#concept-shadow-including-root) as navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container) has to be [connected](https://dom.spec.whatwg.org/#connected).

The container document of a `Document`document is the result of running these steps:

1.   If document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) is null, then return null.

2.   Return document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document).

A [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable is a child navigable of another navigable potentialParent when navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) is potentialParent. We can also just say that a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) "is a [child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable)", which means that its [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) is non-null.

All [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) are the [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) of their [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container).

The content document of a [navigable container](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-container)container is the result of running these steps:

1.   If container's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is null, then return null.

2.   Let document be container's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

3.   If document's [origin](https://dom.spec.whatwg.org/#concept-document-origin) and container's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) are not [same origin-domain](https://html.spec.whatwg.org/multipage/browsers.html#same-origin-domain), then return null.

4.   Return document.

The content window of a [navigable container](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-container)container is the result of running these steps:

1.   If container's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is null, then return null.

2.   Return container's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable)'s [active `WindowProxy`](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-wp)'s object.

* * *

To create a new child navigable, given an element element:

1.   Let parentNavigable be element's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable).

2.   Let group be element's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc)'s [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group).

3.   Let browsingContext and document be the result of [creating a new browsing context and document](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-browsing-context) given element's [node document](https://dom.spec.whatwg.org/#concept-node-document), element, and group.

4.   Let targetName be null.

5.   If element has a `name` content attribute, then set targetName to the value of that attribute.

6.   Let documentState be a new [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-2), with

[document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document)document[initiator origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-initiator-origin)document's [origin](https://dom.spec.whatwg.org/#concept-document-origin)[origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-origin)document's [origin](https://dom.spec.whatwg.org/#concept-document-origin)[navigable target name](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nav-target-name)targetName[about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-about-base-url)document's [about base URL](https://html.spec.whatwg.org/multipage/dom.html#concept-document-about-base-url)
7.   Let navigable be a new [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable).

8.   [Initialize the navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#initialize-the-navigable)navigable given documentState and parentNavigable.

9.   Set element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) to navigable.

10.   Let historyEntry be navigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry).

11.   Let traversable be parentNavigable's [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable).

12.   [Append the following session history traversal steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-traversal-steps) to traversable:

    1.   Let parentDocState be parentNavigable's [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state).

    2.   Let parentNavigableEntries be the result of [getting session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#getting-session-history-entries) for parentNavigable.

    3.   Let targetStepSHE be the first [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry) in parentNavigableEntries whose [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state) equals parentDocState.

    4.   Set historyEntry's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step) to targetStepSHE's [step](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-step).

    5.   Let nestedHistory be a new [nested history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history) whose [id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history-id) is navigable's [id](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-id) and [entries list](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history-entries) is « historyEntry ».

    6.   [Append](https://infra.spec.whatwg.org/#list-append)nestedHistory to parentDocState's [nested histories](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nested-histories).

    7.   [Update for navigable creation/destruction](https://html.spec.whatwg.org/multipage/browsing-the-web.html#update-for-navigable-creation/destruction) given traversable.

13.   Invoke [WebDriver BiDi navigable created](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigable-created) with traversable.

##### 7.3.1.4 Jake diagrams[](https://html.spec.whatwg.org/multipage/document-sequences.html#jake-diagrams)

A useful method for visualizing sequences of documents, and in particular [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) and their [session history entries](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry), is the Jake diagram. A typical Jake diagram is the following:

|  | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| `top` | /t-a | /t-a#foo | /t-b |
| `frames[0]` | /i-0-a | /i-0-b |
| `frames[1]` | /i-1-a | /i-1-b |

Here, each numbered column denotes a possible value for the traversable's [session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step). Each labeled row depicts a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable), as it transitions between different URLs and documents. The first, labeled `top`, being the [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable), and the others being [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable). The documents are given by the background color of each cell, with a new background color indicating a new document in that [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable). The URLs are given by the text content of the cells; usually they are given as [relative URLs](https://url.spec.whatwg.org/#syntax-url-relative) for brevity, unless a cross-origin case is specifically under investigation. A given navigable might not exist at a given step, in which case the corresponding cells are empty. The bold-italic step number depicts the [current session history step](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-current-session-history-step) of the traversable, and all cells with bold-italic URLs represent the [current session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-current-history-entry) for that row's navigable.

Thus, the above Jake diagram depicts the following sequence of events:

1.   A [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable) is created, starting at the URL `/t-a`, with two [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) starting at `/i-0-a` and `/i-1-a` respectively.

2.   The first child navigable is [navigated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) to another document, with URL `/i-0-b`.

3.   The second child navigable is [navigated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) to another document, with URL `/i-1-b`.

4.   The top-level traversable is [navigated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) to the _same_ document, updating its URL to `/t-a#foo`.

5.   The top-level traversable is [navigated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) to another document, with URL `/t-b`. (Notice how this document, of course, does not carry over the old document's child navigables.)

6.   The traversable was [traversed by a delta](https://html.spec.whatwg.org/multipage/browsing-the-web.html#traverse-the-history-by-a-delta) of −3, back to step 1.

[Jake diagrams](https://html.spec.whatwg.org/multipage/document-sequences.html#jake-diagram) are a powerful tool for visualizing the interactions of multiple navigables, navigations, and traversals. They cannot capture every possible interaction — for example, they only work with a single level of nesting — but we will have ocassion to use them to illustrate several complex situations throughout this standard.

[Jake diagrams](https://html.spec.whatwg.org/multipage/document-sequences.html#jake-diagram) are named after their creator, the inimitable Jake Archibald.

It is often helpful in this standard's algorithms to look at collections of [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) starting at a given . This section contains a curated set of algorithms for collecting those navigables.

The return values of these algorithms are ordered so that parents appears before their children. Callers rely on this ordering.

Starting with a , rather than a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable), is generally better because it makes the caller cognizant of whether they are starting with a [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active) or not. Although non-[fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active) s do have ancestor and descendant navigables, they often behave as if they don't (e.g., in the getter).

The ancestor navigables of a document are given by these steps:

1.   Let navigable be document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent).

2.   Let ancestors be an empty list.

3.   While navigable is not null:

    1.   [Prepend](https://infra.spec.whatwg.org/#list-prepend)navigable to ancestors.

    2.   Set navigable to navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent).

4.   Return ancestors.

The inclusive ancestor navigables of a document are given by these steps:

1.   Let navigables be document's [ancestor navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#ancestor-navigables).

2.   [Append](https://infra.spec.whatwg.org/#list-append)document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) to navigables.

3.   Return navigables.

The descendant navigables of a document are given by these steps:

1.   Let navigables be new [list](https://infra.spec.whatwg.org/#list).

2.   Let navigableContainers be a [list](https://infra.spec.whatwg.org/#list) of all [shadow-including descendants](https://dom.spec.whatwg.org/#concept-shadow-including-descendant) of document that are [navigable containers](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-container), in [shadow-including tree order](https://dom.spec.whatwg.org/#concept-shadow-including-tree-order).

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigableContainer of navigableContainers:

    1.   If navigableContainer's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is null, then continue.

    2.   [Extend](https://infra.spec.whatwg.org/#list-extend)navigables with navigableContainer's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [inclusive descendant navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#inclusive-descendant-navigables).

4.   Return navigables.

The inclusive descendant navigables of a document are given by these steps:

1.   Let navigables be « document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) ».

2.   [Extend](https://infra.spec.whatwg.org/#list-extend)navigables with document's [descendant navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#descendant-navigables).

3.   Return navigables.

These descendant-collecting algorithms are described as looking at the DOM tree of descendant objects. In reality, this is often not feasible since the DOM tree can be in another process from the caller of the algorithm. Instead, implementations generally replicate the appropriate trees across processes.

The document-tree child navigables of a document are given by these steps:

1.   If document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) is null, then return the empty list.

2.   Let navigables be new [list](https://infra.spec.whatwg.org/#list).

3.   Let navigableContainers be a [list](https://infra.spec.whatwg.org/#list) of all [descendants](https://dom.spec.whatwg.org/#concept-tree-descendant) of document that are [navigable containers](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-container), in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

4.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigableContainer of navigableContainers:

    1.   If navigableContainer's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is null, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    2.   [Append](https://infra.spec.whatwg.org/#list-append)navigableContainer's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) to navigables.

5.   Return navigables.

##### 7.3.1.6 Navigable destruction[](https://html.spec.whatwg.org/multipage/document-sequences.html#garbage-collection-and-browsing-contexts)

To destroy a child navigable given a [navigable container](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-container)container:

1.   Let navigable be container's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable).

2.   If navigable is null, then return.

3.   Set container's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) to null.

4.   [Inform the navigation API about child navigable destruction](https://html.spec.whatwg.org/multipage/nav-history-apis.html#inform-the-navigation-api-about-child-navigable-destruction) given navigable.

5.   [Destroy a document and its descendants](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document-and-its-descendants) given navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

6.   Let parentDocState be container's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state).

7.   [Remove](https://infra.spec.whatwg.org/#list-remove) the [nested history](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history) from parentDocState's [nested histories](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-nested-histories) whose [id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#nested-history-id) equals navigable's [id](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-id).

8.   Let traversable be container's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable).

9.   [Append the following session history traversal steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-traversal-steps) to traversable:

    1.   [Update for navigable creation/destruction](https://html.spec.whatwg.org/multipage/browsing-the-web.html#update-for-navigable-creation/destruction) given traversable.

10.   Invoke [WebDriver BiDi navigable destroyed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigable-destroyed) with navigable.

To destroy a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable)traversable:

1.   Let browsingContext be traversable's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc).

2.   [For each](https://infra.spec.whatwg.org/#list-iterate)historyEntry in traversable's [session history entries](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-entries)in what order?:

    1.   Let document be historyEntry's [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document).

    2.   If document is not null, then [destroy a document and its descendants](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document-and-its-descendants) given document.

3.   [Remove](https://html.spec.whatwg.org/multipage/document-sequences.html#bcg-remove)browsingContext.

4.   Remove traversable from the user interface (e.g., close or hide its tab in a tabbed browser).

5.   [Remove](https://infra.spec.whatwg.org/#list-remove)traversable from the user agent's [top-level traversable set](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable-set).

6.   Invoke [WebDriver BiDi navigable destroyed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigable-destroyed) with traversable.

User agents may [destroy a top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#destroy-a-top-level-traversable) at any time (typically, [in response to user requests](https://html.spec.whatwg.org/multipage/speculative-loading.html#nav-traversal-ui)).

To close a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable)traversable:

1.   If traversable's [is closing](https://html.spec.whatwg.org/multipage/document-sequences.html#is-closing) is true, then return.

2.   [Definitely close](https://html.spec.whatwg.org/multipage/document-sequences.html#definitely-close-a-top-level-traversable)traversable.

To definitely close a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable)traversable:

1.   Let toUnload be traversable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [inclusive descendant navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#inclusive-descendant-navigables).

2.   If the result of [checking if unloading is canceled](https://html.spec.whatwg.org/multipage/browsing-the-web.html#checking-if-unloading-is-canceled) for toUnload is not "`continue`", then return.

3.   [Append the following session history traversal steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#tn-append-session-history-traversal-steps) to traversable:

    1.   Let afterAllUnloads be an algorithm step which [destroys](https://html.spec.whatwg.org/multipage/document-sequences.html#destroy-a-top-level-traversable)traversable.

    2.   [Unload a document and its descendants](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-a-document-and-its-descendants) given traversable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document), null, and afterAllUnloads.

The [close](https://html.spec.whatwg.org/multipage/document-sequences.html#close-a-top-level-traversable) vs. [definitely close](https://html.spec.whatwg.org/multipage/document-sequences.html#definitely-close-a-top-level-traversable) separation allows other specifications to call [close](https://html.spec.whatwg.org/multipage/document-sequences.html#close-a-top-level-traversable) and have it be a no-op if the top-level traversable is already closing due to JavaScript code calling `window.close()`.

##### 7.3.1.7 Navigable target names[](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable-target-names)

[Navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) can be given [target names](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-target), which are strings allowing certain APIs (such as `window.open()` or the `a` element's `target` attribute) to target [navigations](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) at that navigable.

A valid navigable target name is any string with at least one character that does not contain both an [ASCII tab or newline](https://infra.spec.whatwg.org/#ascii-tab-or-newline) and a U+003C (<), and it does not start with a U+005F (_). (Names starting with a U+005F (_) are reserved for special keywords.)

A valid navigable target name or keyword is any string that is either a [valid navigable target name](https://html.spec.whatwg.org/multipage/document-sequences.html#valid-navigable-target-name) or that is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for one of: `_blank`, `_self`, `_parent`, or `_top`.

These values have different meanings based on whether the page is sandboxed or not, as summarized in the following (non-normative) table. In this table, "current" means the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) that the link or script is in, "parent" means the [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) of the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) that the link or script is in, "top" means the [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-top) of the [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) that the link or script is in, "new" means a new [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable) with a null [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) (which may use an [auxiliary browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#auxiliary-browsing-context), subject to various user preferences and user agent policies), "none" means that nothing will happen, and "maybe new" means the same as "new" if the "`allow-popups`" keyword is also specified on the `sandbox` attribute (or if the user overrode the sandboxing), and the same as "none" otherwise.

| Keyword | Ordinary effect | Effect in an `iframe` with... |
| --- | --- | --- |
| `sandbox=""` | `sandbox="allow-top-navigation"` |
| none specified, for links and form submissions | current | current | current |
| empty string | current | current | current |
| `_blank` | new | maybe new | maybe new |
| `_self` | current | current | current |
| `_parent` if there isn't a parent | current | current | current |
| `_parent` if parent is also top | parent/top | none | parent/top |
| `_parent` if there is one and it's not top | parent | none | none |
| `_top` if top is current | current | current | current |
| `_top` if top is not current | top | none | top |
| name that doesn't exist | new | maybe new | maybe new |
| name that exists and is a descendant | specified descendant | specified descendant | specified descendant |
| name that exists and is current | current | current | current |
| name that exists and is an ancestor that is top | specified ancestor | none | specified ancestor/top |
| name that exists and is an ancestor that is not top | specified ancestor | none | none |
| other name that exists with common top | specified | none | none |
| name that exists with different top, if [familiar](https://html.spec.whatwg.org/multipage/document-sequences.html#familiar-with) and [one permitted sandboxed navigator](https://html.spec.whatwg.org/multipage/browsers.html#one-permitted-sandboxed-navigator) | specified | specified | specified |
| name that exists with different top, if [familiar](https://html.spec.whatwg.org/multipage/document-sequences.html#familiar-with) but not [one permitted sandboxed navigator](https://html.spec.whatwg.org/multipage/browsers.html#one-permitted-sandboxed-navigator) | specified | none | none |
| name that exists with different top, not [familiar](https://html.spec.whatwg.org/multipage/document-sequences.html#familiar-with) | new | maybe new | maybe new |

Most of the restrictions on sandboxed browsing contexts are applied by other algorithms, e.g. the [navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) algorithm, not [the rules for choosing a navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#the-rules-for-choosing-a-navigable) given below.

* * *

To find a navigable by target name given a string name and a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)currentNavigable:

1.   Let currentDocument be currentNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

2.   Let sourceSnapshotParams be the result of [snapshotting source snapshot params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#snapshotting-source-snapshot-params) given currentDocument.

3.   Let subtreesToSearch be an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) choice of one of the following:

    *   « currentNavigable's [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable), currentNavigable »

    *   the [inclusive ancestor navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#inclusive-ancestor-navigables) of currentDocument

[Issue #10848](https://github.com/whatwg/html/issues/10848) tracks settling on one of these two possibilities, to achieve interoperability.

4.   [For each](https://infra.spec.whatwg.org/#list-iterate)subtreeToSearch of subtreesToSearch, in reverse order:

    1.   Let documentToSearch be subtreeToSearch's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

    2.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigable of the [inclusive descendant navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#inclusive-descendant-navigables) of documentToSearch:

        1.   If currentNavigable is not [allowed by sandboxing to navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#allowed-to-navigate)navigable given sourceSnapshotParams, then optionally [continue](https://infra.spec.whatwg.org/#iteration-continue).

[Issue #10849](https://github.com/whatwg/html/issues/10849) tracks making this check required, to achieve interoperability.

        2.   If navigable's [target name](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-target) is name, then return navigable.

5.   Let currentTopLevelBrowsingContext be currentNavigable's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc)'s [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc).

6.   Let group be currentTopLevelBrowsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group).

7.   [For each](https://infra.spec.whatwg.org/#list-iterate)topLevelBrowsingContext of group's [browsing context set](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-set), in an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) order (the user agent should pick a consistent ordering, such as the most recently opened, most recently focused, or more closely related):

[Issue #10850](https://github.com/whatwg/html/issues/10850) tracks picking a specific ordering, to achieve interoperability.

    1.   If currentTopLevelBrowsingContext is topLevelBrowsingContext, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    2.   Let documentToSearch be topLevelBrowsingContext's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document).

    3.   [For each](https://infra.spec.whatwg.org/#list-iterate)navigable of the [inclusive descendant navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#inclusive-descendant-navigables) of documentToSearch:

        1.   If currentNavigable's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc) is not [familiar with](https://html.spec.whatwg.org/multipage/document-sequences.html#familiar-with)navigable's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc), then [continue](https://infra.spec.whatwg.org/#iteration-continue).

        2.   If currentNavigable is not [allowed by sandboxing to navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#allowed-to-navigate)navigable given sourceSnapshotParams, then optionally [continue](https://infra.spec.whatwg.org/#iteration-continue).

[Issue #10849](https://github.com/whatwg/html/issues/10849) tracks making this check required, to achieve interoperability.

        3.   If navigable's [target name](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-target) is name, then return navigable.

8.   Return null.

The rules for choosing a navigable, given a string name, a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)currentNavigable, and a boolean noopener are as follows:

1.   Let chosen be null.

2.   Let windowType be "`existing or none`".

3.   Let sandboxingFlagSet be currentNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set).

4.   If name is the empty string or an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for "`_self`", then set chosen to currentNavigable.

5.   Otherwise, if name is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for "`_parent`", set chosen to currentNavigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent), if any, and currentNavigable otherwise.

6.   Otherwise, if name is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for "`_top`", set chosen to currentNavigable's [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable).

7.   Otherwise, if name is not an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for "`_blank`" and noopener is false, then set chosen to the result of [finding a navigable by target name](https://html.spec.whatwg.org/multipage/document-sequences.html#find-a-navigable-by-target-name) given name and currentNavigable.

8.   If chosen is null, then a new [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable) is being requested, and what happens depends on the user agent's configuration and abilities — it is determined by the rules given for the first applicable option from the following list:

The user agent may inform the user that a popup has been blocked.

If sandboxingFlagSet has the [sandboxed auxiliary navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-auxiliary-navigation-browsing-context-flag) set
The user agent may report to a developer console that a popup has been blocked.

If the user agent has been configured such that in this instance it will create a new [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable)
    1.   [Consume user activation](https://html.spec.whatwg.org/multipage/interaction.html#consume-user-activation) of currentNavigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window).

    2.   Set windowType to "`new and unrestricted`".

    3.   Let currentDocument be currentNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

    4.   If currentDocument's [opener policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-coop)'s [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value) is "`same-origin`" or "`same-origin-plus-COEP`", and currentDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin) is not [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with currentDocument's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin), then:

        1.   Set noopener to true.

        2.   Set name to "`_blank`".

        3.   Set windowType to "`new with no opener`".

In the presence of an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy), nested documents that are cross-origin with their top-level browsing context's active document always set noopener to true.

    5.   Let targetName be the empty string.

    6.   If name is not an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for "`_blank`", then set targetName to name.

    7.   If noopener is true, then set chosen to the result of [creating a new top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-top-level-traversable) given null, targetName, and currentNavigable.

    8.   Otherwise:

        1.   Set chosen to the result of [creating a new top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-top-level-traversable) given currentNavigable's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc), targetName, and currentNavigable.

        2.   If sandboxingFlagSet's [sandboxed navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-navigation-browsing-context-flag) is set, then set chosen's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc)'s [one permitted sandboxed navigator](https://html.spec.whatwg.org/multipage/browsers.html#one-permitted-sandboxed-navigator) to currentNavigable's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc).

    9.   If sandboxingFlagSet's [sandbox propagates to auxiliary browsing contexts flag](https://html.spec.whatwg.org/multipage/browsers.html#sandbox-propagates-to-auxiliary-browsing-contexts-flag) is set, then all the flags that are set in sandboxingFlagSet must be set in chosen's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc)'s [popup sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#popup-sandboxing-flag-set).

    10.   Set chosen's [is created by web content](https://html.spec.whatwg.org/multipage/document-sequences.html#is-created-by-web-content) to true.

If the newly created [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)chosen is immediately [navigated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate), then the navigation will be done as a "`replace`" navigation.

If the user agent has been configured such that in this instance it will choose currentNavigable
Set chosen to currentNavigable.

If the user agent has been configured such that in this instance it will not find a navigable
Do nothing.

User agents are encouraged to provide a way for users to configure the user agent to always choose currentNavigable.

9.   Return chosen and windowType.

#### 7.3.2 Browsing contexts[](https://html.spec.whatwg.org/multipage/document-sequences.html#windows)

A browsing context is a programmatic representation of a series of documents, multiple of which can live within a single [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable). Each [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) has a corresponding `WindowProxy` object, as well as the following:

*   An opener browsing context, a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) or null, initially null.

*   An opener origin at creation, an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) or null, initially null.

*   An boolean, initially false.

The only mandatory impact in this specification of [is popup](https://html.spec.whatwg.org/multipage/document-sequences.html#is-popup) is on the `visible` getter of the relevant `BarProp` objects. However, user agents might also use it for [user interface considerations](https://html.spec.whatwg.org/multipage/speculative-loading.html#nav-traversal-ui).

*   An is auxiliary boolean, initially false.

*   An initial URL, a [URL](https://url.spec.whatwg.org/#concept-url) or null, initially null.

*   A virtual browsing context group ID integer, initially 0. This is used by [opener policy reporting](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value), to keep track of the browsing context group switches that would have happened if the report-only policy had been enforced.

A [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)'s top-level traversable is its [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-top).

A [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) whose [is auxiliary](https://html.spec.whatwg.org/multipage/document-sequences.html#is-auxiliary) is true is known as an auxiliary browsing context. Auxiliary browsing contexts are always [top-level browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context).

It's unclear whether a separate [is auxiliary](https://html.spec.whatwg.org/multipage/document-sequences.html#is-auxiliary) concept is necessary. In [issue #5680](https://github.com/whatwg/html/issues/5680), it is indicated that we may be able to simplify this by using whether or not the [opener browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-browsing-context) is null.

Modern specifications should avoid using the [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) concept in most cases, unless they are dealing with the subtleties of [browsing context group switches](https://html.spec.whatwg.org/multipage/browsers.html#browsing-context-group-switches-due-to-cross-origin-opener-policy) and [agent cluster allocation](https://html.spec.whatwg.org/multipage/document-sequences.html#agent-cluster-map). Instead, the `Document` and [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) concepts are usually more appropriate.

* * *

A `Document`'s browsing context is a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) or null, initially null.

A `Document` does not necessarily have a non-null [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc). In particular, data mining tools are likely to never instantiate browsing contexts. A `Document` created using an API such as `createDocument()` never has a non-null [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc). And the `Document` originally created for an `iframe` element, which has since been [removed from the document](https://html.spec.whatwg.org/multipage/infrastructure.html#remove-an-element-from-a-document), has no associated browsing context, since that browsing context was [nulled out](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document).

In general, there is a 1-to-1 mapping from the `Window` object to the `Document` object, as long as the `Document` object has a non-null [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc). There is one exception. A `Window` can be reused for the presentation of a second `Document` in the same [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context), such that the mapping is then 1-to-2. This occurs when a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) is [navigated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) from the [initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank)`Document` to another, which will be done with [replacement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigationhistorybehavior-replace).

##### 7.3.2.1 Creating browsing contexts[](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-browsing-contexts)

To create a new browsing context and document, given null or a `Document` object creator, null or an element embedder, and a [browsing context group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group)group:

1.   Let browsingContext be a new [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context).

2.   Let unsafeContextCreationTime be the [unsafe shared current time](https://w3c.github.io/hr-time/#dfn-unsafe-shared-current-time).

3.   Let creatorOrigin be null.

4.   Let creatorBaseURL be null.

5.   If creator is non-null, then:

    1.   Set creatorOrigin to creator's [origin](https://dom.spec.whatwg.org/#concept-document-origin).

    2.   Set creatorBaseURL to creator's [document base URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-url).

    3.   Set browsingContext's [virtual browsing context group ID](https://html.spec.whatwg.org/multipage/document-sequences.html#virtual-browsing-context-group-id) to creator's [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc)'s [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [virtual browsing context group ID](https://html.spec.whatwg.org/multipage/document-sequences.html#virtual-browsing-context-group-id).

6.   Let sandboxFlags be the result of [determining the creation sandboxing flags](https://html.spec.whatwg.org/multipage/browsers.html#determining-the-creation-sandboxing-flags) given browsingContext and embedder.

7.   Let origin be the result of [determining the origin](https://html.spec.whatwg.org/multipage/document-sequences.html#determining-the-origin) given `about:blank`, sandboxFlags, and creatorOrigin.

8.   Let permissionsPolicy be the result of [creating a permissions policy](https://w3c.github.io/webappsec-feature-policy/#create-for-navigable) given embedder and origin. [[PERMISSIONSPOLICY]](https://html.spec.whatwg.org/multipage/references.html#refsPERMISSIONSPOLICY)

9.   Let agent be the result of [obtaining a similar-origin window agent](https://html.spec.whatwg.org/multipage/webappapis.html#obtain-similar-origin-window-agent) given origin, group, and false.

10.   Let realm execution context be the result of [creating a new realm](https://html.spec.whatwg.org/multipage/webappapis.html#creating-a-new-javascript-realm) given agent and the following customizations:

    *   For the global object, create a new `Window` object.

    *   For the global **this** binding, use browsingContext's `WindowProxy` object.

11.   Let topLevelCreationURL be `about:blank` if embedder is null; otherwise embedder's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [top-level creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-creation-url).

12.   Let topLevelOrigin be origin if embedder is null; otherwise embedder's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin).

13.   [Set up a window environment settings object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#set-up-a-window-environment-settings-object) with `about:blank`, realm execution context, null, topLevelCreationURL, and topLevelOrigin.

14.   Let loadTimingInfo be a new [document load timing info](https://html.spec.whatwg.org/multipage/dom.html#document-load-timing-info) with its [navigation start time](https://html.spec.whatwg.org/multipage/dom.html#navigation-start-time) set to the result of calling [coarsen time](https://w3c.github.io/hr-time/#dfn-coarsen-time) with unsafeContextCreationTime and the new [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)'s [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-cross-origin-isolated-capability).

15.   Let document be a new `Document`, with:

[type](https://dom.spec.whatwg.org/#concept-document-type)"`html`"[content type](https://dom.spec.whatwg.org/#concept-document-content-type)"`text/html`"[mode](https://dom.spec.whatwg.org/#concept-document-mode)"`quirks`"[origin](https://dom.spec.whatwg.org/#concept-document-origin)origin[browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc)browsingContext[permissions policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-permissions-policy)permissionsPolicy[active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set)sandboxFlags[load timing info](https://html.spec.whatwg.org/multipage/dom.html#load-timing-info)loadTimingInfo[is initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank)true[about base URL](https://html.spec.whatwg.org/multipage/dom.html#concept-document-about-base-url)creatorBaseURL[allow declarative shadow roots](https://dom.spec.whatwg.org/#concept-document-allow-declarative-shadow-roots)true[custom element registry](https://dom.spec.whatwg.org/#document-custom-element-registry)a new `CustomElementRegistry` object
16.   Let iframeReferrerPolicy be the result of [determining the `iframe` element referrer policy](https://html.spec.whatwg.org/multipage/browsers.html#determining-the-iframe-element-referrer-policy) given embedder.

17.   Set document's [internal ancestor origin objects list](https://html.spec.whatwg.org/multipage/dom.html#concept-document-internal-ancestor-origin-objects-list) to the result of running the [internal ancestor origin objects list creation steps](https://html.spec.whatwg.org/multipage/dom.html#internal-ancestor-origin-objects-list-creation-steps) given document and iframeReferrerPolicy.

18.   Set document's [ancestor origins list](https://html.spec.whatwg.org/multipage/dom.html#concept-document-ancestor-origins-list) to the result of running the [ancestor origins list creation steps](https://html.spec.whatwg.org/multipage/dom.html#ancestor-origins-list-creation-steps) given document.

19.   If creator is non-null, then:

    1.   Set document's [referrer](https://html.spec.whatwg.org/multipage/dom.html#the-document's-referrer) to the [serialization](https://url.spec.whatwg.org/#concept-url-serializer) of creator's [URL](https://dom.spec.whatwg.org/#concept-document-url).

    2.   Set document's [policy container](https://html.spec.whatwg.org/multipage/dom.html#concept-document-policy-container) to a [clone](https://html.spec.whatwg.org/multipage/browsers.html#clone-a-policy-container) of creator's [policy container](https://html.spec.whatwg.org/multipage/dom.html#concept-document-policy-container).

    3.   If creator's [origin](https://dom.spec.whatwg.org/#concept-document-origin) is [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with creator's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin), then set document's [opener policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-coop) to creator's [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc)'s [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [opener policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-coop).

20.   [Assert](https://infra.spec.whatwg.org/#assert): document's [URL](https://dom.spec.whatwg.org/#concept-document-url) and document's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-creation-url) are `about:blank`.

21.   Mark document as [ready for post-load tasks](https://html.spec.whatwg.org/multipage/parsing.html#ready-for-post-load-tasks).

22.   [Populate with `html`/`head`/`body`](https://html.spec.whatwg.org/multipage/document-lifecycle.html#populate-with-html/head/body) given document.

23.   [Make active](https://html.spec.whatwg.org/multipage/browsing-the-web.html#make-active)document.

24.   [Completely finish loading](https://html.spec.whatwg.org/multipage/document-lifecycle.html#completely-finish-loading)document.

25.   Return browsingContext and document.

To create a new top-level browsing context and document:

1.   Let group and document be the result of [creating a new browsing context group and document](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-browsing-context-group-and-document).

2.   Return group's [browsing context set](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-set)[0] and document.

To create a new auxiliary browsing context and document, given a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)opener:

1.   Let openerTopLevelBrowsingContext be opener's [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-traversable)'s [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc).

2.   Let group be openerTopLevelBrowsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group).

3.   [Assert](https://infra.spec.whatwg.org/#assert): group is non-null, as [navigating](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) invokes this directly.

4.   Let browsingContext and document be the result of [creating a new browsing context and document](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-browsing-context) with opener's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document), null, and group.

5.   Set browsingContext's [is auxiliary](https://html.spec.whatwg.org/multipage/document-sequences.html#is-auxiliary) to true.

6.   [Append](https://html.spec.whatwg.org/multipage/document-sequences.html#bcg-append)browsingContext to group.

7.   Set browsingContext's [opener browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-browsing-context) to opener.

8.   Set browsingContext's [virtual browsing context group ID](https://html.spec.whatwg.org/multipage/document-sequences.html#virtual-browsing-context-group-id) to openerTopLevelBrowsingContext's [virtual browsing context group ID](https://html.spec.whatwg.org/multipage/document-sequences.html#virtual-browsing-context-group-id).

9.   Set browsingContext's [opener origin at creation](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-origin-at-creation) to opener's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin).

10.   Return browsingContext and document.

##### 7.3.2.2 Related browsing contexts[](https://html.spec.whatwg.org/multipage/document-sequences.html#nested-browsing-contexts)

A [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)potentialDescendant is said to be an ancestor of a browsing context potentialAncestor if the following algorithm returns true:

1.   Let potentialDescendantDocument be potentialDescendant's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document).

2.   If potentialDescendantDocument is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then return false.

3.   Let ancestorBCs be the list obtained by taking the [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc) of the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of each member of potentialDescendantDocument's [ancestor navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#ancestor-navigables).

4.   If ancestorBCs[contains](https://infra.spec.whatwg.org/#list-contain)potentialAncestor, then return true.

5.   Return false.

A top-level browsing context is a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) whose [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) is a [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#traversable-navigable).

It is _not_ required to be a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable).

The top-level browsing context of a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)start is the result of the following algorithm:

1.   If start's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document) is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then return null.

2.   Let navigable be start's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable).

3.   While navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent) is not null, set navigable to navigable's [parent](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent).

4.   Return navigable's [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc).

* * *

A [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)A is familiar with a second [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)B if the following algorithm returns true:

1.   If A's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with B's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin), then return true.

2.   If A's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc) is B, then return true.

3.   If B is an [auxiliary browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#auxiliary-browsing-context) and A is [familiar with](https://html.spec.whatwg.org/multipage/document-sequences.html#familiar-with)B's [opener browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-browsing-context), then return true.

4.   If there exists an [ancestor browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#ancestor-browsing-context) of B whose [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document) has the [same](https://html.spec.whatwg.org/multipage/browsers.html#same-origin)[origin](https://dom.spec.whatwg.org/#concept-document-origin) as the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document) of A, then return true.

This includes the case where A is an [ancestor browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#ancestor-browsing-context) of B.

5.   Return false.

##### 7.3.2.3 Groupings of browsing contexts[](https://html.spec.whatwg.org/multipage/document-sequences.html#groupings-of-browsing-contexts)

A [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context) has an associated group (null or a [browsing context group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group)). It is initially null.

A user agent holds a browsing context group set (a [set](https://infra.spec.whatwg.org/#ordered-set) of [browsing context groups](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group)).

A browsing context group holds a browsing context set (a [set](https://infra.spec.whatwg.org/#ordered-set) of [top-level browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context)).

A [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context) is added to the [group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group) when the group is [created](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-browsing-context-group-and-document). All subsequent [top-level browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context) added to the [group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group) will be [auxiliary browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#auxiliary-browsing-context).

A [browsing context group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group) has an associated agent cluster map (a weak [map](https://infra.spec.whatwg.org/#ordered-map) of [agent cluster keys](https://html.spec.whatwg.org/multipage/webappapis.html#agent-cluster-key) to [agent clusters](https://tc39.es/ecma262/#sec-agent-clusters)). User agents are responsible for collecting agent clusters when it is deemed that nothing can access them anymore.

A [browsing context group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group) has an associated historical agent cluster key map, which is a [map](https://infra.spec.whatwg.org/#ordered-map) of [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) to [agent cluster keys](https://html.spec.whatwg.org/multipage/webappapis.html#agent-cluster-key). This map is used to ensure the consistency of the [origin-keyed agent clusters](https://html.spec.whatwg.org/multipage/browsers.html#origin-keyed-agent-clusters) feature by recording what agent cluster keys were previously used for a given origin.

The [historical agent cluster key map](https://html.spec.whatwg.org/multipage/document-sequences.html#historical-agent-cluster-key-map) only ever gains entries over the lifetime of the browsing context group.

A [browsing context group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group) has a cross-origin isolation mode, which is a [cross-origin isolation mode](https://html.spec.whatwg.org/multipage/document-sequences.html#cross-origin-isolation-mode). It is initially "`none`".

A cross-origin isolation mode is one of three possible values: "`none`", "`logical`", or "`concrete`".

To create a new browsing context group and document:

1.   Let group be a new [browsing context group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group).

2.   [Append](https://infra.spec.whatwg.org/#set-append)group to the user agent's [browsing context group set](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group-set).

3.   Let browsingContext and document be the result of [creating a new browsing context and document](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-browsing-context) with null, null, and group.

4.   [Append](https://html.spec.whatwg.org/multipage/document-sequences.html#bcg-append)browsingContext to group.

5.   Return group and document.

To append a [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context)browsingContext to a [browsing context group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group)group:

1.   [Append](https://infra.spec.whatwg.org/#set-append)browsingContext to group's [browsing context set](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-set).

2.   Set browsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group) to group.

To remove a [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context)browsingContext:

1.   [Assert](https://infra.spec.whatwg.org/#assert): browsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group) is non-null.

2.   Let group be browsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group).

3.   Set browsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group) to null.

4.   [Remove](https://infra.spec.whatwg.org/#list-remove)browsingContext from group's [browsing context set](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-set).

5.   If group's [browsing context set](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-set)[is empty](https://infra.spec.whatwg.org/#list-is-empty), then [remove](https://infra.spec.whatwg.org/#list-remove)group from the user agent's [browsing context group set](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group-set).

[Append](https://html.spec.whatwg.org/multipage/document-sequences.html#bcg-append) and [remove](https://html.spec.whatwg.org/multipage/document-sequences.html#bcg-remove) are primitive operations that help define the lifetime of a [browsing context group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group). They are called by higher-level creation and destruction operations for `Document`s and [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context).

When there are no `Document` objects whose [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc) equals a given [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) (i.e., all such `Document`s have been [destroyed](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document)), and that [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)'s `WindowProxy` is eligible for garbage collection, then the [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) will never be accessed again. If it is a [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context), then at this point the user agent must [remove](https://html.spec.whatwg.org/multipage/document-sequences.html#bcg-remove) it.

#### 7.3.3 Fully active documents[](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active-documents)

A `Document`d is said to be fully active when d is the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, and either navigable is a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable) or navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document) is [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active).

Because they are associated with an element, [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) are always tied to a specific `Document`, their [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document), in their [parent navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-parent). User agents must not allow the user to interact with [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) whose [container documents](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document) are not themselves [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active).

The following example illustrates how a `Document` can be the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of its [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable), while not being [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active). Here `a.html` is loaded into a browser window, `b-1.html` starts out loaded into an `iframe` as shown, and `b-2.html` and `c.html` are omitted (they can simply be an empty document).

```
<!-- a.html -->
<!DOCTYPE html>
<html lang="en">
<title>Navigable A</title>

<iframe src="b-1.html"></iframe>
<button onclick="frames[0].location.href = 'b-2.html'">Click me</button>

<!-- b-1.html -->
<!DOCTYPE html>
<html lang="en">
<title>Navigable B</title>

<iframe src="c.html"></iframe>
```

At this point, the documents given by `a.html`, `b-1.html`, and `c.html` are all the [active documents](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of their respective [node navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable). They are also all [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active).

After clicking on the `button`, and thus loading a new `Document` from `b-2.html` into navigable B, we have the following results:

*   The `a.html``Document` remains both the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of navigable A, and [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active).

*   The `b-1.html``Document` is now _not_ the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of navigable B. As such it is also not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active).

*   The new `b-2.html``Document` is now the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of navigable B, and is also [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active).

*   The `c.html``Document` is still the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of navigable C. However, since C's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document) is the `b-1.html``Document`, which is itself not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), this means the `c.html``Document` is now not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active).

[← 7.2 APIs related to navigation and session history](https://html.spec.whatwg.org/multipage/nav-history-apis.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [7.4 Navigation and session history →](https://html.spec.whatwg.org/multipage/browsing-the-web.html)
