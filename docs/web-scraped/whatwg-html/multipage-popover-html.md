# Source: https://html.spec.whatwg.org/multipage/popover.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/popover.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 6.11 Drag and drop](https://html.spec.whatwg.org/multipage/dnd.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [7 Loading web pages →](https://html.spec.whatwg.org/multipage/browsers.html)
1.       1.   [6.12 The `popover` attribute](https://html.spec.whatwg.org/multipage/popover.html#the-popover-attribute)
        1.   [6.12.1 The popover target attributes](https://html.spec.whatwg.org/multipage/popover.html#the-popover-target-attributes)
        2.   [6.12.2 Popover light dismiss](https://html.spec.whatwg.org/multipage/popover.html#popover-light-dismiss)

### 6.12 The `popover` attribute[](https://html.spec.whatwg.org/multipage/popover.html#the-popover-attribute)

[Global_attributes/popover](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/popover "The popover global attribute is used to designate an element as a popover element.")

Support in all current engines.

Firefox🔰 114+Safari preview+Chrome 114+

* * *

Opera?Edge 114+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

All [HTML elements](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) may have the `popover` content attribute set. When specified, the element won't be rendered until it becomes shown, at which point it will be rendered on top of other page content.

The `popover` attribute is a global attribute that allows authors flexibility to ensure popover functionality can be applied to elements with the most relevant semantics.

The following demonstrates how one might create a popover sub-navigation list of links, within the global navigation for a website.

```
<ul>
  <li>
    <a href=...>All Products</a>
    <button popovertarget=sub-nav>
     <img src=down-arrow.png alt="Product pages">
    </button>
    <ul popover id=sub-nav>
     <li><a href=...>Shirts</a>
     <li><a href=...>Shoes</a>
     <li><a href=...>Hats etc.</a>
    </ul>
  </li>
  <!-- other list items and links here -->
</ul>
```

When using `popover` on elements without accessibility semantics, for instance the `div` element, authors should use the appropriate ARIA attributes to ensure the popover is accessible.

The following shows the baseline markup to create a custom menu popover, where the first menuitem will receive keyboard focus when the popover is invoked due to the use of the `autofocus` attribute. Navigating the menuitems with arrow keys and activation behaviors would still need author scripting. Additional requirements for building custom menus widgets are defined in the [WAI-ARIA specification](https://w3c.github.io/aria/#menu).

```
<button popovertarget=m>Actions</button>
<div role=menu id=m popover>
  <button role=menuitem tabindex=-1 autofocus>Edit</button>
  <button role=menuitem tabindex=-1>Hide</button>
  <button role=menuitem tabindex=-1>Delete</button>
</div>
```

A popover can be useful for rendering a status message, confirming the action performed by the user. The following demonstrates how one could reveal a popover in an `output` element.

```
<button id=submit>Submit</button>
<p><output><span popover=manual></span></output></p>

<script>
 const sBtn = document.getElementById("submit");
 const outSpan = document.querySelector("output [popover=manual]");
 let successMessage;
 let errorMessage;

 /* define logic for determining success of action
  and determining the appropriate success or error
  messages to use */

 sBtn.addEventListener("click", ()=> {
  if ( success ) {
   outSpan.textContent = successMessage;
  }
  else {
   outSpan.textContent = errorMessage;
  }
  outSpan.showPopover();

  setTimeout(function () {
   outSpan.hidePopover();
  }, 10000);
 });
</script>
```

Inserting a popover element into an `output` element will generally cause screen readers to announce the content when it becomes visible. Depending on the complexity or frequency of the content, this could be either useful or annoying to users of these assistive technologies. Keep this in mind when using the `output` element or other ARIA live regions to ensure the best user experience.

The `popover` attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | State | Brief description |
| --- | --- | --- |
| `auto` | Auto | Closes other popovers when opened; has [light dismiss](https://html.spec.whatwg.org/multipage/popover.html#popover-light-dismiss) and responds to [close requests](https://html.spec.whatwg.org/multipage/interaction.html#close-request). |
| `manual` | Manual | Does not close other popovers; does not [light dismiss](https://html.spec.whatwg.org/multipage/popover.html#popover-light-dismiss) or respond to [close requests](https://html.spec.whatwg.org/multipage/interaction.html#close-request). |
| `hint` | Hint | Closes other hint popovers when opened, but not other auto popovers; has [light dismiss](https://html.spec.whatwg.org/multipage/popover.html#popover-light-dismiss) and responds to [close requests](https://html.spec.whatwg.org/multipage/interaction.html#close-request). |

[HTMLElement/popover](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/popover "The popover property of the HTMLElement interface gets and sets an element's popover state via JavaScript (\"auto\" or \"manual\"), and can be used for feature detection.")

Support in all current engines.

Firefox🔰 114+Safari 17+Chrome 114+

* * *

Opera?Edge 114+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Every [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) has a popover visibility state, initially [hidden](https://html.spec.whatwg.org/multipage/popover.html#popover-hidden-state), with these potential values:

*   hidden

*   showing

Every `Document` has a popover pointerdown target, which is an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) or null, initially null.

Every [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) has a popover trigger, which is an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) or null, initially set to null.

Every [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) has a popover showing or hiding, which is a boolean, initially set to false.

Every [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements)popover toggle task tracker, which is a [toggle task tracker](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-tracker) or null, initially null.

Every [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) has a popover close watcher, which is a [close watcher](https://html.spec.whatwg.org/multipage/interaction.html#close-watcher) or null, initially null.

Every [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) has an opened in popover mode, which is a string or null, initially null.

The following [attribute change steps](https://dom.spec.whatwg.org/#concept-element-attributes-change-ext), given element, localName, oldValue, value, and namespace, are used for all [HTML elements](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements):

1.   If namespace is not null, then return.

2.   If localName is not `popover`, then return.

3.   If element's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is in the [showing state](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state) and oldValue and value are in different [states](https://html.spec.whatwg.org/multipage/popover.html#attr-popover), then run the [hide popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-algorithm) given element, true, true, false, and null.

`element.showPopover()`Shows the popover element by adding it to the top layer. If element's `popover` attribute is in the [Auto](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-auto-state) state, then this will also close all other [Auto](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-auto-state) popovers unless they are an ancestor of element according to the [topmost popover ancestor](https://html.spec.whatwg.org/multipage/popover.html#topmost-popover-ancestor) algorithm.`element.hidePopover()`Hides the popover element by removing it from the top layer and applying `display: none` to it.`element.togglePopover()`If the popover element is not showing, then this method shows it. Otherwise, this method hides it. This method returns true if the popover is open after calling it, otherwise false.

[HTMLElement/showPopover](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/showPopover "The showPopover() method of the HTMLElement interface shows a popover element (i.e. one that has a valid popover attribute) by adding it to the top layer.")

Support in all current engines.

Firefox🔰 114+Safari 17+Chrome 114+

* * *

Opera?Edge 114+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `showPopover(options)` method steps are:

1.   Let source be options["`source`"] if it [exists](https://infra.spec.whatwg.org/#map-exists); otherwise, null.

2.   Run [show popover](https://html.spec.whatwg.org/multipage/popover.html#show-popover) given [this](https://webidl.spec.whatwg.org/#this), true, and source.

To show popover, given an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements)element, a boolean throwExceptions, and an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) or null source:

1.   If the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given element, false, throwExceptions, and null is false, then return.

2.   Let document be element's [node document](https://dom.spec.whatwg.org/#concept-node-document).

3.   [Assert](https://infra.spec.whatwg.org/#assert): element's [popover trigger](https://html.spec.whatwg.org/multipage/popover.html#popover-trigger) is null.

4.   [Assert](https://infra.spec.whatwg.org/#assert): element is not in document's [top layer](https://drafts.csswg.org/css-position-4/#document-top-layer).

5.   Let nestedShow be element's [popover showing or hiding](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-or-hiding).

6.   Let fireEvents be the boolean negation of nestedShow.

7.   Set element's [popover showing or hiding](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-or-hiding) to true.

8.   Let cleanupShowingFlag be the following steps:

    1.   If nestedShow is false, then set element's [popover showing or hiding](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-or-hiding) to false.

9.   If the result of [firing an event](https://dom.spec.whatwg.org/#concept-event-fire) named `beforetoggle`, using `ToggleEvent`, with the `cancelable` attribute initialized to true, the `oldState` attribute initialized to "`closed`", the `newState` attribute initialized to "`open`", and the `source` attribute initialized to source at element is false, then run cleanupShowingFlag and return.

10.   If the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given element, false, throwExceptions, and document is false, then run cleanupShowingFlag and return.

[Check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) is called again because firing the `beforetoggle` event could have disconnected this element or changed its `popover` attribute.

11.   Let shouldRestoreFocus be false.

12.   Let originalType be the current state of element's `popover` attribute.

13.   Let stackToAppendTo be null.

14.   Let autoAncestor be the result of running the [topmost popover ancestor](https://html.spec.whatwg.org/multipage/popover.html#topmost-popover-ancestor) algorithm given element, document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list), source, and true.

15.   Let hintAncestor be the result of running the [topmost popover ancestor](https://html.spec.whatwg.org/multipage/popover.html#topmost-popover-ancestor) algorithm given element, document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list), source, and true.

16.   If originalType is the [Auto](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-auto-state) state, then:

    1.   Run [close entire popover list](https://html.spec.whatwg.org/multipage/popover.html#close-entire-popover-list) given document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list), shouldRestoreFocus, and fireEvents.

    2.   Let ancestor be the result of running the [topmost popover ancestor](https://html.spec.whatwg.org/multipage/popover.html#topmost-popover-ancestor) algorithm given element, document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list), source, and true.

    3.   If ancestor is null, then set ancestor to document.

    4.   Run [hide all popovers until](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) given ancestor, shouldRestoreFocus, and fireEvents.

    5.   Set stackToAppendTo to "`auto`".

17.   If originalType is the [Hint](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-hint-state) state, then:

    1.   If hintAncestor is not null, then:

        1.   Run [hide all popovers until](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) given hintAncestor, shouldRestoreFocus, and fireEvents.

        2.   Set stackToAppendTo to "`hint`".

    2.   Otherwise:

        1.   Run [close entire popover list](https://html.spec.whatwg.org/multipage/popover.html#close-entire-popover-list) given document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list), shouldRestoreFocus, and fireEvents.

        2.   If autoAncestor is not null, then:

            1.   Run [hide all popovers until](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) given autoAncestor, shouldRestoreFocus, and fireEvents.

            2.   Set stackToAppendTo to "`auto`".

        3.   Otherwise, set stackToAppendTo to "`hint`".

18.   If originalType is [Auto](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-auto-state) or [Hint](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-hint-state), then:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): stackToAppendTo is not null.

    2.   If originalType is not equal to the value of element's `popover` attribute, then:

        1.   If throwExceptions is true, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

        2.   Return.

    3.   If the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given element, false, throwExceptions, and document is false, then run cleanupShowingFlag and return.

[Check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) is called again because running [hide all popovers until](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) above could have fired the `beforetoggle` event, and an event handler could have disconnected this element or changed its `popover` attribute.

    4.   If the result of running [topmost auto or hint popover](https://html.spec.whatwg.org/multipage/popover.html#topmost-auto-popover) on document is null, then set shouldRestoreFocus to true.

This ensures that focus is returned to the previously-focused element only for the first popover in a stack.

    5.   If stackToAppendTo is "`auto`":

        1.   [Assert](https://infra.spec.whatwg.org/#assert): document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list) does not contain element.

        2.   Set element's [opened in popover mode](https://html.spec.whatwg.org/multipage/popover.html#opened-in-popover-mode) to "`auto`".

Otherwise:

        1.   [Assert](https://infra.spec.whatwg.org/#assert): stackToAppendTo is "`hint`".

        2.   [Assert](https://infra.spec.whatwg.org/#assert): document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list) does not contain element.

        3.   Set element's [opened in popover mode](https://html.spec.whatwg.org/multipage/popover.html#opened-in-popover-mode) to "`hint`".

    6.   Set element's [popover close watcher](https://html.spec.whatwg.org/multipage/popover.html#popover-close-watcher) to the result of [establishing a close watcher](https://html.spec.whatwg.org/multipage/interaction.html#establish-a-close-watcher) given element's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), with:

        *   _[cancelAction](https://html.spec.whatwg.org/multipage/interaction.html#create-close-watcher-cancelaction)_ being to return true.

        *   _[closeAction](https://html.spec.whatwg.org/multipage/interaction.html#create-close-watcher-closeaction)_ being to [hide a popover](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-algorithm) given element, true, true, false, and null.

        *   _[getEnabledState](https://html.spec.whatwg.org/multipage/interaction.html#create-close-watcher-getenabledstate)_ being to return true.

19.   Set element's [previously focused element](https://html.spec.whatwg.org/multipage/interactive-elements.html#previously-focused-element) to null.

20.   Let originallyFocusedElement be document's [focused area of the document](https://html.spec.whatwg.org/multipage/interaction.html#focused-area-of-the-document)'s [DOM anchor](https://html.spec.whatwg.org/multipage/interaction.html#dom-anchor).

21.   [Add an element to the top layer](https://drafts.csswg.org/css-position-4/#add-an-element-to-the-top-layer) given element.

22.   Set element's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) to [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state).

23.   Set element's [popover trigger](https://html.spec.whatwg.org/multipage/popover.html#popover-trigger) to source.

24.   Set element's [implicit anchor element](https://drafts.csswg.org/css-anchor-position/#implicit-anchor-element) to source.

25.   Run the [popover focusing steps](https://html.spec.whatwg.org/multipage/popover.html#popover-focusing-steps) given element.

26.   If shouldRestoreFocus is true and element's `popover` attribute is not in the [No Popover](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-none-state) state, then set element's [previously focused element](https://html.spec.whatwg.org/multipage/interactive-elements.html#previously-focused-element) to originallyFocusedElement.

27.   [Queue a popover toggle event task](https://html.spec.whatwg.org/multipage/popover.html#queue-a-popover-toggle-event-task) given element, "`closed`", "`open`", and source.

28.   Run cleanupShowingFlag.

To queue a popover toggle event task given an element element, a string oldState, a string newState, and an `Element` or null source:

1.   If element's [popover toggle task tracker](https://html.spec.whatwg.org/multipage/popover.html#popover-toggle-task-tracker) is not null, then:

    1.   Set oldState to element's [popover toggle task tracker](https://html.spec.whatwg.org/multipage/popover.html#popover-toggle-task-tracker)'s [old state](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-old-state).

    2.   Remove element's [popover toggle task tracker](https://html.spec.whatwg.org/multipage/popover.html#popover-toggle-task-tracker)'s [task](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-task) from its [task queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue).

    3.   Set element's [popover toggle task tracker](https://html.spec.whatwg.org/multipage/popover.html#popover-toggle-task-tracker) to null.

2.   [Queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) given the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) and element to run the following steps:

    1.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `toggle` at element, using `ToggleEvent`, with the `oldState` attribute initialized to oldState, the `newState` attribute initialized to newState, and the `source` attribute initialized to source.

    2.   Set element's [popover toggle task tracker](https://html.spec.whatwg.org/multipage/popover.html#popover-toggle-task-tracker) to null.

3.   Set element's [popover toggle task tracker](https://html.spec.whatwg.org/multipage/popover.html#popover-toggle-task-tracker) to a struct with [task](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-task) set to the just-queued [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) and [old state](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-old-state) set to oldState.

[HTMLElement/hidePopover](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/hidePopover "The hidePopover() method of the HTMLElement interface hides a popover element (i.e. one that has a valid popover attribute) by removing it from the top layer and styling it with display: none.")

Support in all current engines.

Firefox🔰 114+Safari 17+Chrome 114+

* * *

Opera?Edge 114+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `hidePopover()` method steps are:

1.   Run the [hide popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-algorithm) given [this](https://webidl.spec.whatwg.org/#this), true, true, true, and null.

To hide a popover given an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements)element, a boolean focusPreviousElement, a boolean fireEvents, a boolean throwExceptions, and an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) or null source:

1.   If the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given element, true, throwExceptions, and null is false, then return.

2.   Let document be element's [node document](https://dom.spec.whatwg.org/#concept-node-document).

3.   Let nestedHide be element's [popover showing or hiding](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-or-hiding).

4.   Set element's [popover showing or hiding](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-or-hiding) to true.

5.   If nestedHide is true, then set fireEvents to false.

6.   Let cleanupSteps be the following steps:

    1.   If nestedHide is false, then set element's [popover showing or hiding](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-or-hiding) to false.

    2.   If element's [popover close watcher](https://html.spec.whatwg.org/multipage/popover.html#popover-close-watcher) is not null, then:

        1.   [Destroy](https://html.spec.whatwg.org/multipage/interaction.html#close-watcher-destroy)element's [popover close watcher](https://html.spec.whatwg.org/multipage/popover.html#popover-close-watcher).

        2.   Set element's [popover close watcher](https://html.spec.whatwg.org/multipage/popover.html#popover-close-watcher) to null.

7.   If element's [opened in popover mode](https://html.spec.whatwg.org/multipage/popover.html#opened-in-popover-mode) is "`auto`" or "`hint`", then:

    1.   Run [hide all popovers until](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) given element, focusPreviousElement, and fireEvents.

    2.   If the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given element, true, and throwExceptions is false, then run cleanupSteps and return.

[Check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) is called again because running [hide all popovers until](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) could have disconnected element or changed its `popover` attribute.

8.   Let autoPopoverListContainsElement be true if document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list)'s last item is element, otherwise false.

9.   If fireEvents is true:

    1.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `beforetoggle`, using `ToggleEvent`, with the `oldState` attribute initialized to "`open`", the `newState` attribute initialized to "`closed`", and the `source` attribute set to source at element.

    2.   If autoPopoverListContainsElement is true and document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list)'s last item is not element, then run [hide all popovers until](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) given element, focusPreviousElement, and false.

    3.   If the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given element, true, throwExceptions, and null is false, then run cleanupSteps and return.

[Check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) is called again because firing the `beforetoggle` event could have disconnected element or changed its `popover` attribute.

    4.   [Request an element to be removed from the top layer](https://drafts.csswg.org/css-position-4/#request-an-element-to-be-removed-from-the-top-layer) given element.

    5.   Set element's [implicit anchor element](https://drafts.csswg.org/css-anchor-position/#implicit-anchor-element) to null.

10.   Otherwise, [remove an element from the top layer immediately](https://drafts.csswg.org/css-position-4/#remove-an-element-from-the-top-layer-immediately) given element.

11.   Set element's [popover trigger](https://html.spec.whatwg.org/multipage/popover.html#popover-trigger) to null.

12.   Set element's [opened in popover mode](https://html.spec.whatwg.org/multipage/popover.html#opened-in-popover-mode) to null.

13.   Set element's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) to [hidden](https://html.spec.whatwg.org/multipage/popover.html#popover-hidden-state).

14.   If fireEvents is true, then [queue a popover toggle event task](https://html.spec.whatwg.org/multipage/popover.html#queue-a-popover-toggle-event-task) given element, "`open`", "`closed`", and source.

15.   Let previouslyFocusedElement be element's [previously focused element](https://html.spec.whatwg.org/multipage/interactive-elements.html#previously-focused-element).

16.   If previouslyFocusedElement is not null, then:

    1.   Set element's [previously focused element](https://html.spec.whatwg.org/multipage/interactive-elements.html#previously-focused-element) to null.

    2.   If focusPreviousElement is true and document's [focused area of the document](https://html.spec.whatwg.org/multipage/interaction.html#focused-area-of-the-document)'s [DOM anchor](https://html.spec.whatwg.org/multipage/interaction.html#dom-anchor) is a [shadow-including inclusive descendant](https://dom.spec.whatwg.org/#concept-shadow-including-inclusive-descendant) of element, then run the [focusing steps](https://html.spec.whatwg.org/multipage/interaction.html#focusing-steps) for previouslyFocusedElement; the viewport should not be scrolled by doing this step.

17.   Run cleanupSteps.

[HTMLElement/togglePopover](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/togglePopover "The togglePopover() method of the HTMLElement interface toggles a popover element (i.e. one that has a valid popover attribute) between the hidden and showing states.")

Support in all current engines.

Firefox🔰 114+Safari 17+Chrome 114+

* * *

Opera?Edge 114+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `togglePopover(options)` method steps are:

1.   Let force be null.

2.   If options is a boolean, set force to options.

3.   Otherwise, if options["`force`"] [exists](https://infra.spec.whatwg.org/#map-exists), set force to options["`force`"].

4.   Let source be options["`source`"] if it [exists](https://infra.spec.whatwg.org/#map-exists); otherwise, null.

5.   If [this](https://webidl.spec.whatwg.org/#this)'s [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state), and force is null or false, then run the [hide popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-algorithm) given [this](https://webidl.spec.whatwg.org/#this), true, true, true, and null.

6.   Otherwise, if force is null or true, then run [show popover](https://html.spec.whatwg.org/multipage/popover.html#show-popover) given [this](https://webidl.spec.whatwg.org/#this), true, and source.

7.   Otherwise:

    1.   Let expectedToBeShowing be true if [this](https://webidl.spec.whatwg.org/#this)'s [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state); otherwise false.

    2.   Run [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given expectedToBeShowing, true, and null.

8.   Return true if [this](https://webidl.spec.whatwg.org/#this)'s [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state); otherwise false.

To hide all popovers until, given an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) or `Document`endpoint, a boolean focusPreviousElement, and a boolean fireEvents:

1.   If endpoint is an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) and endpoint is not in the [popover showing state](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state), then return.

2.   Let document be endpoint's [node document](https://dom.spec.whatwg.org/#concept-node-document).

3.   [Assert](https://infra.spec.whatwg.org/#assert): endpoint is a `Document` or endpoint's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state).

4.   [Assert](https://infra.spec.whatwg.org/#assert): endpoint is a `Document` or endpoint's `popover` attribute is in the [Auto](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-auto-state) state or endpoint's `popover` attribute is in the [Hint](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-hint-state) state.

5.   If endpoint is a `Document`:

    1.   Run [close entire popover list](https://html.spec.whatwg.org/multipage/popover.html#close-entire-popover-list) given document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list), focusPreviousElement, and fireEvents.

    2.   Run [close entire popover list](https://html.spec.whatwg.org/multipage/popover.html#close-entire-popover-list) given document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list), focusPreviousElement, and fireEvents.

    3.   Return.

6.   If document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list) contains endpoint:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): endpoint's `popover` attribute is in the [Hint](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-hint-state) state.

    2.   Run [hide popover stack until](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-stack-until) given endpoint, document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list), focusPreviousElement, and fireEvents.

    3.   Return.

7.   Run [close entire popover list](https://html.spec.whatwg.org/multipage/popover.html#close-entire-popover-list) given document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list), focusPreviousElement, and fireEvents.

8.   If document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list) does not contain endpoint, then return.

9.   Run [hide popover stack until](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-stack-until) given endpoint, document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list), focusPreviousElement, and fireEvents.

To hide popover stack until, given an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements)endpoint, a [list](https://infra.spec.whatwg.org/#list)popoverList, a boolean focusPreviousElement, and a boolean fireEvents:

1.   Let repeatingHide be false.

2.   Perform the following steps at least once:

    1.   Let lastToHide be null.

    2.   For each popover in popoverList:

        1.   If popover is endpoint, then [break](https://infra.spec.whatwg.org/#iteration-break).

        2.   Set lastToHide to popover.

    3.   If lastToHide is null, then return.

    4.   [While](https://infra.spec.whatwg.org/#iteration-while)lastToHide's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state):

        1.   [Assert](https://infra.spec.whatwg.org/#assert): popoverList is not empty.

        2.   Run the [hide popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-algorithm) given the last item in popoverList, focusPreviousElement, fireEvents, false, and null.

    5.   [Assert](https://infra.spec.whatwg.org/#assert): repeatingHide is false or popoverList's last item is endpoint.

    6.   Set repeatingHide to true if popoverList contains endpoint and popoverList's last item is not endpoint, otherwise false.

    7.   If repeatingHide is true, then set fireEvents to false.

and keep performing them [while](https://infra.spec.whatwg.org/#iteration-while)repeatingHide is true.

The [hide all popovers until algorithm](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) is used in several cases to hide all popovers that don't stay open when something happens. For example, during light-dismiss of a popover, this algorithm ensures that we close only the popovers that aren't related to the node clicked by the user.

To find the topmost popover ancestor, given a `Node`newPopoverOrTopLayerElement, a [list](https://infra.spec.whatwg.org/#list)popoverList, an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) or null source, and a boolean isPopover, perform the following steps. They return an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) or null.

The [topmost popover ancestor](https://html.spec.whatwg.org/multipage/popover.html#topmost-popover-ancestor) algorithm will return the topmost (latest in the [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list)) ancestor popover for the provided popover or top layer element. Popovers can be related to each other in several ways, creating a tree of popovers. There are two paths through which one popover (call it the "child" popover) can have a topmost ancestor popover (call it the "parent" popover):

1.   The popovers are nested within each other in the node tree. In this case, the descendant popover is the "child" and its topmost ancestor popover is the "parent".

2.   A popover trigger element (e.g., a `button`) has a `popovertarget` attribute pointing to a popover. In this case, the popover is the "child", and the popover subtree the trigger element is in is the "parent". The trigger element has to be in a popover and reference an open popover.

In each of the relationships formed above, the parent popover has to be strictly earlier in the [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list) than the child popover, or it does not form a valid ancestral relationship. This eliminates non-showing popovers and self-pointers (e.g., a popover containing an invoking element that points back to the containing popover), and it allows for the construction of a well-formed tree from the (possibly cyclic) graph of connections. Only [Auto](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-auto-state) popovers are considered.

If the provided element is a top layer element such as a `dialog` which is not showing as a popover, then [topmost popover ancestor](https://html.spec.whatwg.org/multipage/popover.html#topmost-popover-ancestor) will only look in the node tree to find the first popover.

1.   If isPopover is true:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): newPopoverOrTopLayerElement is an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements).

    2.   [Assert](https://infra.spec.whatwg.org/#assert): newPopoverOrTopLayerElement's `popover` attribute is not in the [No Popover State](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-none-state) or the [Manual](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-manual-state) state.

    3.   [Assert](https://infra.spec.whatwg.org/#assert): newPopoverOrTopLayerElement's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is not in the [popover showing state](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state).

2.   Otherwise:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): source is null.

3.   Let popoverPositions be an empty [ordered map](https://infra.spec.whatwg.org/#ordered-map).

4.   Let index be 0.

5.   For each popover of popoverList:

    1.   [Set](https://infra.spec.whatwg.org/#map-set)popoverPositions[popover] to index.

    2.   Increment index by 1.

6.   If isPopover is true, then [set](https://infra.spec.whatwg.org/#map-set)popoverPositions[newPopoverOrTopLayerElement] to index.

7.   Increment index by 1.

8.   Let topmostPopoverAncestor be null.

9.   Let checkAncestor be an algorithm which performs the following steps given candidate:

    1.   If candidate is null, then return.

    2.   Let okNesting be false.

    3.   Let candidateAncestor be null.

    4.   [While](https://infra.spec.whatwg.org/#iteration-while)okNesting is false:

        1.   Set candidateAncestor to the result of running [nearest inclusive open popover](https://html.spec.whatwg.org/multipage/popover.html#nearest-inclusive-open-popover) given candidate.

        2.   If candidateAncestor is null or popoverPositions does not contain candidateAncestor, then return.

        3.   [Assert](https://infra.spec.whatwg.org/#assert): candidateAncestor's `popover` attribute is not in the [Manual](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-manual-state) or [None](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-none-state) state.

        4.   Set okNesting to true if isPopover is false, newPopoverOrTopLayerElement's `popover` attribute is in the [Hint](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-hint-state) state, or candidateAncestor's `popover` attribute is in the [Auto](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-auto-state) state.

        5.   If okNesting is false, then set candidate to candidateAncestor's parent in the [flat tree](https://drafts.csswg.org/css-scoping/#flat-tree).

    5.   Let candidatePosition be popoverPositions[candidateAncestor].

    6.   If topmostPopoverAncestor is null or popoverPositions[topmostPopoverAncestor] is less than candidatePosition, then set topmostPopoverAncestor to candidateAncestor.

10.   Run checkAncestor given newPopoverOrTopLayerElement's parent node within the [flat tree](https://drafts.csswg.org/css-scoping/#flat-tree).

11.   Run checkAncestor given source.

12.   Return topmostPopoverAncestor.

To find the nearest inclusive open popover given a `Node`node, perform the following steps. They return an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) or null.

1.   Let currentNode be node.

2.   While currentNode is not null:

    1.   If currentNode's `popover` attribute is in the [Auto](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-auto-state) state or the [Hint](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-hint-state) state, and currentNode's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state), then return currentNode.

    2.   Set currentNode to currentNode's parent in the [flat tree](https://drafts.csswg.org/css-scoping/#flat-tree).

3.   Return null.

To find the topmost auto or hint popover given a `Document`document, perform the following steps. They return an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) or null.

1.   If document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list) is not empty, then return document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list)'s last element.

2.   If document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list) is not empty, then return document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list)'s last element.

3.   Return null.

To perform the popover focusing steps for an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements)subject:

1.   If the [allow focus steps](https://html.spec.whatwg.org/multipage/interaction.html#allow-focus-steps) given subject's [node document](https://dom.spec.whatwg.org/#concept-node-document) return false, then return.

2.   If subject is a `dialog` element, then run the [dialog focusing steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-focusing-steps) given subject and return.

3.   If subject has the `autofocus` attribute, then let control be subject.

4.   Otherwise, let control be the [autofocus delegate](https://html.spec.whatwg.org/multipage/interaction.html#autofocus-delegate) for subject given "`other`".

5.   If control is null, then return.

6.   Run the [focusing steps](https://html.spec.whatwg.org/multipage/interaction.html#focusing-steps) given control.

7.   Let topDocument be control's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-top)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

8.   If control's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is not the [same](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) as the [origin](https://dom.spec.whatwg.org/#concept-document-origin) of topDocument, then return.

9.   [Empty](https://infra.spec.whatwg.org/#list-empty)topDocument's [autofocus candidates](https://html.spec.whatwg.org/multipage/interaction.html#autofocus-candidates).

10.   Set topDocument's [autofocus processed flag](https://html.spec.whatwg.org/multipage/interaction.html#autofocus-processed-flag) to true.

To check popover validity for an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements)element given a boolean expectedToBeShowing, a boolean throwExceptions, and a `Document` or null expectedDocument, perform the following steps. They throw an exception or return a boolean.

1.   If element's `popover` attribute is in the [No Popover](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-none-state) state, then:

    1.   If throwExceptions is true, then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

    2.   Return false.

2.   If any of the following are true:

    *   expectedToBeShowing is true and element's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is not [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state); or

    *   expectedToBeShowing is false and element's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is not [hidden](https://html.spec.whatwg.org/multipage/popover.html#popover-hidden-state),

then return false.

3.   If any of the following are true:

    *   element is not [connected](https://dom.spec.whatwg.org/#connected);

    *   element's [node document](https://dom.spec.whatwg.org/#concept-node-document) is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active);

    *   expectedDocument is not null and element's [node document](https://dom.spec.whatwg.org/#concept-node-document) is not expectedDocument;

    *   element is a `dialog` element and its [is modal](https://html.spec.whatwg.org/multipage/interactive-elements.html#is-modal) is set to true; or

    *   element's [fullscreen flag](https://fullscreen.spec.whatwg.org/#fullscreen-flag) is set,

then:

    1.   If throwExceptions is true, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

    2.   Return false.

4.   Return true.

To get the showing auto popover list for a `Document`document:

1.   Let popovers be « ».

2.   [For each](https://infra.spec.whatwg.org/#list-iterate)`Element`element in document's [top layer](https://drafts.csswg.org/css-position-4/#document-top-layer):

    1.   If all of the following are true:

        *   element is an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements);

        *   element's [opened in popover mode](https://html.spec.whatwg.org/multipage/popover.html#opened-in-popover-mode) is "`auto`"; and

        *   element's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state),

then [append](https://infra.spec.whatwg.org/#list-append)element to popovers.

3.   Return popovers.

To get the showing hint popover list for a `Document`document:

1.   Let popovers be « ».

2.   [For each](https://infra.spec.whatwg.org/#list-iterate)`Element`element in document's [top layer](https://drafts.csswg.org/css-position-4/#document-top-layer):

    1.   If all of the following are true:

        *   element is an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements);

        *   element's [opened in popover mode](https://html.spec.whatwg.org/multipage/popover.html#opened-in-popover-mode) is "`hint`"; and

        *   element's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state),

then [append](https://infra.spec.whatwg.org/#list-append)element to popovers.

3.   Return popovers.

To close entire popover list given a [list](https://infra.spec.whatwg.org/#list)popoverList, a boolean focusPreviousElement, and a boolean fireEvents:

1.   While popoverList is not empty:

    1.   Run the [hide popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-algorithm) given popoverList's last item, focusPreviousElement, fireEvents, false, and null.

#### 6.12.1 The popover target attributes[](https://html.spec.whatwg.org/multipage/popover.html#the-popover-target-attributes)

[Buttons](https://html.spec.whatwg.org/multipage/forms.html#concept-button) may have the following content attributes:

*   `popovertarget`

*   `popovertargetaction`

If specified, the `popovertarget` attribute value must be the [ID](https://dom.spec.whatwg.org/#concept-id) of an element with a `popover` attribute in the same [tree](https://dom.spec.whatwg.org/#concept-tree) as the [button](https://html.spec.whatwg.org/multipage/forms.html#concept-button) with the `popovertarget` attribute.

The `popovertargetaction` attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | State | Brief description |
| --- | --- | --- |
| `toggle` | Toggle | Shows or hides the targeted popover element. |
| `show` | Show | Shows the targeted popover element. |
| `hide` | Hide | Hides the targeted popover element. |

Whenever possible ensure the popover element is placed immediately after its triggering element in the DOM. Doing so will help ensure that the popover is exposed in a logical programmatic reading order for users of assistive technology, such as screen readers.

The following shows how the `popovertarget` attribute in combination with the `popovertargetaction` attribute can be used to show and close a popover:

```
<button popovertarget="foo" popovertargetaction="show">
  Show a popover
</button>

<article popover="auto" id="foo">
  This is a popover article!
  <button popovertarget="foo" popovertargetaction="hide">Close</button>
</article>
```

If a `popovertargetaction` attribute is not specified, the default action will be to toggle the associated popover. The following shows how only specifying the `popovertarget` attribute on its invoking button can toggle a manual popover between its opened and closed states. A manual popover will not respond to [light dismiss](https://html.spec.whatwg.org/multipage/popover.html#popover-light-dismiss) or [close requests](https://html.spec.whatwg.org/multipage/interaction.html#close-request):

```
<input type="button" popovertarget="foo" value="Toggle the popover">

<div popover=manual id="foo">
  This is a popover!
</div>
```

[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom): 

[HTMLButtonElement/popoverTargetElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLButtonElement/popoverTargetElement "The popoverTargetElement property of the HTMLButtonElement interface gets and sets the popover element to control via a button.")

Support in all current engines.

Firefox🔰 114+Safari 17+Chrome 114+

* * *

Opera?Edge 114+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLInputElement/popoverTargetElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/popoverTargetElement "The popoverTargetElement property of the HTMLInputElement interface gets and sets the popover element to control via an <input> element of type=\"button\".")

Support in all current engines.

Firefox🔰 114+Safari 17+Chrome 114+

* * *

Opera?Edge 114+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

```
interface mixin PopoverTargetAttributes {
  [CEReactions, Reflect] attribute Element? popoverTargetElement;
  [CEReactions] attribute DOMString popoverTargetAction;
};
```

[HTMLButtonElement/popoverTargetAction](https://developer.mozilla.org/en-US/docs/Web/API/HTMLButtonElement/popoverTargetAction "The popoverTargetAction property of the HTMLButtonElement interface gets and sets the action to be performed (\"hide\", \"show\", or \"toggle\") on a popover element being controlled by a button.")

Support in all current engines.

Firefox🔰 114+Safari 17+Chrome 114+

* * *

Opera?Edge 114+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLInputElement/popoverTargetAction](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/popoverTargetAction "The popoverTargetAction property of the HTMLInputElement interface gets and sets the action to be performed (\"hide\", \"show\", or \"toggle\") on a popover element being controlled by an <input> element of type=\"button\".")

Support in all current engines.

Firefox🔰 114+Safari 17+Chrome 114+

* * *

Opera?Edge 114+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

To run the popover target attribute activation behavior given a `Node`node and a `Node`eventTarget:

1.   Let popover be node's [popover target element](https://html.spec.whatwg.org/multipage/popover.html#popover-target-element).

2.   If popover is null, then return.

3.   If eventTarget is a [shadow-including inclusive descendant](https://dom.spec.whatwg.org/#concept-shadow-including-inclusive-descendant) of popover and popover is a [shadow-including descendant](https://dom.spec.whatwg.org/#concept-shadow-including-descendant) of node, then return.

4.   If node's `popovertargetaction` attribute is in the [show](https://html.spec.whatwg.org/multipage/popover.html#attr-popovertargetaction-show) state and popover's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state), then return.

5.   If node's `popovertargetaction` attribute is in the [hide](https://html.spec.whatwg.org/multipage/popover.html#attr-popovertargetaction-hide) state and popover's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [hidden](https://html.spec.whatwg.org/multipage/popover.html#popover-hidden-state), then return.

6.   If popover's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state), then run the [hide popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-algorithm) given popover, true, true, false, and node.

7.   Otherwise, if popover's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [hidden](https://html.spec.whatwg.org/multipage/popover.html#popover-hidden-state) and the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given popover, false, false, and null is true, then run [show popover](https://html.spec.whatwg.org/multipage/popover.html#show-popover) given popover, false, and node.

To get the popover target element given a `Node`node, perform the following steps. They return an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) or null.

1.   If node is not a [button](https://html.spec.whatwg.org/multipage/forms.html#concept-button), then return null.

2.   If node is [disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-disabled), then return null.

3.   If node has a [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) and node is a [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button), then return null.

4.   Let popoverElement be the result of running node's [get the `popovertarget`-associated element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#attr-associated-element).

5.   If popoverElement is null, then return null.

6.   If popoverElement's `popover` attribute is in the [No Popover](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-none-state) state, then return null.

7.   Return popoverElement.

#### 6.12.2 Popover light dismiss[](https://html.spec.whatwg.org/multipage/popover.html#popover-light-dismiss)

"Light dismiss" means that clicking outside of a popover whose `popover` attribute is in the [Auto](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-auto-state) state will close the popover. This is in addition to how such popovers respond to [close requests](https://html.spec.whatwg.org/multipage/interaction.html#close-request).

To light dismiss open popovers, given a `PointerEvent`event:

1.   [Assert](https://infra.spec.whatwg.org/#assert): event's `isTrusted` attribute is true.

2.   Let target be event's [target](https://dom.spec.whatwg.org/#concept-event-target).

3.   Let document be target's [node document](https://dom.spec.whatwg.org/#concept-node-document).

4.   Let topmostPopover be the result of running [topmost auto popover](https://html.spec.whatwg.org/multipage/popover.html#topmost-auto-popover) given document.

5.   If topmostPopover is null, then return.

6.   If event's `type` is "`pointerdown`", then: set document's [popover pointerdown target](https://html.spec.whatwg.org/multipage/popover.html#popover-pointerdown-target) to the result of running [topmost clicked popover](https://html.spec.whatwg.org/multipage/popover.html#topmost-clicked-popover) given target.

7.   If event's `type` is "`pointerup`", then:

    1.   Let ancestor be the result of running [topmost clicked popover](https://html.spec.whatwg.org/multipage/popover.html#topmost-clicked-popover) given target.

    2.   Let sameTarget be true if ancestor is document's [popover pointerdown target](https://html.spec.whatwg.org/multipage/popover.html#popover-pointerdown-target).

    3.   Set document's [popover pointerdown target](https://html.spec.whatwg.org/multipage/popover.html#popover-pointerdown-target) to null.

    4.   If ancestor is null, then set ancestor to document.

    5.   If sameTarget is true, then run [hide all popovers until](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) given ancestor, false, and true.

To find the topmost clicked popover, given a `Node`node:

1.   Let clickedPopover be the result of running [nearest inclusive open popover](https://html.spec.whatwg.org/multipage/popover.html#nearest-inclusive-open-popover) given node.

2.   Let targetPopover be the result of running [nearest inclusive target popover](https://html.spec.whatwg.org/multipage/popover.html#nearest-inclusive-target-popover) given node.

3.   If the result of [getting the popover stack position](https://html.spec.whatwg.org/multipage/popover.html#get-the-popover-stack-position) given clickedPopover is greater than the result of [getting the popover stack position](https://html.spec.whatwg.org/multipage/popover.html#get-the-popover-stack-position) given targetPopover, then return clickedPopover.

4.   Return targetPopover.

To get the popover stack position, given an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements)popover:

1.   Let hintList be popover's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list).

2.   Let autoList be popover's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list).

3.   If popover is in hintList, then return the index of popover in hintList + the size of autoList + 1.

4.   If popover is in autoList, then return the index of popover in autoList + 1.

5.   Return 0.

To find the nearest inclusive target popover given a `Node`node:

1.   Let currentNode be node.

2.   While currentNode is not null:

    1.   Let targetPopover be currentNode's [popover target element](https://html.spec.whatwg.org/multipage/popover.html#popover-target-element).

    2.   If targetPopover is not null and targetPopover's `popover` attribute is in the [Auto](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-auto-state) state or the [Hint](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-hint-state) state, and targetPopover's [popover visibility state](https://html.spec.whatwg.org/multipage/popover.html#popover-visibility-state) is [showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state), then return targetPopover.

    3.   Set currentNode to currentNode's ancestor in the [flat tree](https://drafts.csswg.org/css-scoping/#flat-tree).

[← 6.11 Drag and drop](https://html.spec.whatwg.org/multipage/dnd.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [7 Loading web pages →](https://html.spec.whatwg.org/multipage/browsers.html)
