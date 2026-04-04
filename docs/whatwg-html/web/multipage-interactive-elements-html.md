# Source: https://html.spec.whatwg.org/multipage/interactive-elements.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/interactive-elements.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 4.10.18 Form control infrastructure](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.12 Scripting →](https://html.spec.whatwg.org/multipage/scripting.html)
1.       1.   [4.11 Interactive elements](https://html.spec.whatwg.org/multipage/interactive-elements.html#interactive-elements)
        1.   [4.11.1 The `details` element](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element)
        2.   [4.11.2 The `summary` element](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-summary-element)
        3.   [4.11.3 Commands](https://html.spec.whatwg.org/multipage/interactive-elements.html#commands)
            1.   [4.11.3.1 Facets](https://html.spec.whatwg.org/multipage/interactive-elements.html#facets-2)
            2.   [4.11.3.2 Using the `a` element to define a command](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-a-element-to-define-a-command)
            3.   [4.11.3.3 Using the `button` element to define a command](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-button-element-to-define-a-command)
            4.   [4.11.3.4 Using the `input` element to define a command](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-input-element-to-define-a-command)
            5.   [4.11.3.5 Using the `option` element to define a command](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-option-element-to-define-a-command)
            6.   [4.11.3.6 Using the `accesskey` attribute on a `legend` element to define a command](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-accesskey-attribute-on-a-legend-element-to-define-a-command)
            7.   [4.11.3.7 Using the `accesskey` attribute to define a command on other elements](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-accesskey-attribute-to-define-a-command-on-other-elements)

        4.   [4.11.4 The `dialog` element](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)
        5.   [4.11.5 Dialog light dismiss](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-light-dismiss)

### 4.11 Interactive elements[](https://html.spec.whatwg.org/multipage/interactive-elements.html#interactive-elements)

#### 4.11.1 The `details` element[](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element)

[Element/details](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details "The <details> HTML element creates a disclosure widget in which information is visible only when the widget is toggled into an \"open\" state. A summary or label must be provided using the <summary> element.")

Support in all current engines.

Firefox 49+Safari 6+Chrome 12+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android 49+Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLDetailsElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDetailsElement "The HTMLDetailsElement interface provides special properties (beyond the regular HTMLElement interface it also has available to it by inheritance) for manipulating <details> elements.")

Support in all current engines.

Firefox 49+Safari 6+Chrome 10+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android?

[HTMLDetailsElement/open](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDetailsElement/open "The open property of the HTMLDetailsElement interface is a boolean value reflecting the open HTML attribute, indicating whether the <details>'s contents (not counting the <summary>) is to be shown to the user.")

Support in all current engines.

Firefox 49+Safari 6+Chrome 10+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android?

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):One `summary` element followed by [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`name` — Name of group of mutually-exclusive `details` elements `open` — Whether the details are visible [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-details).[For implementers](https://w3c.github.io/html-aam/#el-details).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLDetailsElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute DOMString name;
  [CEReactions, Reflect] attribute boolean open;
};
```

The `details` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a disclosure widget from which the user can obtain additional information or controls.

As with all HTML elements, it is not conforming to use the `details` element when attempting to represent another type of control. For example, tab widgets and menu widgets are not disclosure widgets, so abusing the `details` element to implement these patterns is incorrect.

The `details` element is not appropriate for footnotes. Please see [the section on footnotes](https://html.spec.whatwg.org/multipage/semantics-other.html#footnotes) for details on how to mark up footnotes.

The first `summary` element child of the element, if any, [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the summary or legend of the details. If there is no child `summary` element, the user agent should provide its own legend (e.g. "Details").

The rest of the element's contents [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the additional information or controls.

The `name` content attribute gives the name of the group of related `details` elements that the element is a member of. Opening one member of this group causes other members of the group to close. If the attribute is specified, its value must not be the empty string.

Before using this feature, authors should consider whether this grouping of related `details` elements into an exclusive accordion is helpful or harmful to users. While using an exclusive accordion can reduce the maximum amount of space that a set of content can occupy, it can also frustrate users who have to open many items to find what they want or users who want to look at the contents of multiple items at the same time.

A document must not contain more than one `details` element in the same [details name group](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-name-group) that has the `open` attribute present. Authors must not use script to add `details` elements to a document in a way that would cause a [details name group](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-name-group) to have more than one `details` element with the `open` attribute present.

The group of elements that is created by a common `name` attribute is exclusive, meaning that at most one of the `details` elements can be open at once. While this exclusivity is enforced by user agents, the resulting enforcement immediately changes the `open` attributes in the markup. This requirement on authors forbids such misleading markup.

A document must not contain a `details` element that is a descendant of another `details` element in the same [details name group](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-name-group).

Documents that use the `name` attribute to group multiple related `details` elements should keep those related elements together in a containing element (such as a `section` element or `article` element). When it makes sense for the group to be introduced with a heading, authors should put that heading in a [heading](https://html.spec.whatwg.org/multipage/sections.html#concept-heading) element at the start of the containing element.

Visually and programmatically grouping related elements together can be important for accessible user experiences. This can help users understand the relationship between such elements. When related elements are in disparate sections of a web page rather than being grouped, the elements' relationships to each other can be less discoverable or understandable.

The `open` content attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute). If present, it indicates that both the summary and the additional information is to be shown to the user. If the attribute is absent, only the summary is to be shown.

When the element is created, if the attribute is absent, the additional information should be hidden; if the attribute is present, that information should be shown. Subsequently, if the attribute is removed, then the information should be hidden; if the attribute is added, the information should be shown.

The user agent should allow the user to request that the additional information be shown or hidden. To honor a request for the details to be shown, the user agent must [set](https://dom.spec.whatwg.org/#concept-element-attributes-set-value) the `open` attribute on the element to the empty string. To honor a request for the information to be hidden, the user agent must [remove](https://dom.spec.whatwg.org/#concept-element-attributes-remove) the `open` attribute from the element.

This ability to request that additional information be shown or hidden may simply be the [activation behavior](https://dom.spec.whatwg.org/#eventtarget-activation-behavior) of the appropriate `summary` element, in the case such an element exists. However, if no such element exists, user agents can still provide this ability through some other user interface affordance.

The details name group that contains a `details` element a also contains all the other `details` elements b that fulfill all of the following conditions:

*   Both a and b are in the same [tree](https://dom.spec.whatwg.org/#concept-tree).
*   They both have a `name` attribute, their `name` attributes are not the empty string, and the value of a's `name` attribute equals the value of b's `name` attribute.

Every `details` element has a details toggle task tracker, which is a [toggle task tracker](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-tracker) or null, initially null.

The following [attribute change steps](https://dom.spec.whatwg.org/#concept-element-attributes-change-ext), given element, localName, oldValue, value, and namespace, are used for all `details` elements:

1.   If namespace is not null, then return.

2.   If localName is `name`, then [ensure details exclusivity by closing the given element if needed](https://html.spec.whatwg.org/multipage/interactive-elements.html#ensure-details-exclusivity-by-closing-the-given-element-if-needed) given element.

3.   If localName is `open`, then:

    1.   If one of oldValue or value is null and the other is not null, run the following steps, which are known as the details notification task steps, for this `details` element:

When the `open` attribute is toggled several times in succession, the resulting tasks essentially get coalesced so that only one event is fired.

        1.   If oldValue is null, [queue a details toggle event task](https://html.spec.whatwg.org/multipage/interactive-elements.html#queue-a-details-toggle-event-task) given the `details` element, "`closed`", and "`open`".

        2.   Otherwise, [queue a details toggle event task](https://html.spec.whatwg.org/multipage/interactive-elements.html#queue-a-details-toggle-event-task) given the `details` element, "`open`", and "`closed`".

    2.   If oldValue is null and value is not null, then [ensure details exclusivity by closing other elements if needed](https://html.spec.whatwg.org/multipage/interactive-elements.html#ensure-details-exclusivity-by-closing-other-elements-if-needed) given element.

To be clear, these attribute change and insertion steps also run when an attribute or element is inserted via the parser.

To queue a details toggle event task given a `details` element element, a string oldState, and a string newState:

1.   If element's [details toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-toggle-task-tracker) is not null, then:

    1.   Set oldState to element's [details toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-toggle-task-tracker)'s [old state](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-old-state).

    2.   Remove element's [details toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-toggle-task-tracker)'s [task](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-task) from its [task queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue).

    3.   Set element's [details toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-toggle-task-tracker) to null.

2.   [Queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) given the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) and element to run the following steps:

    1.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `toggle` at element, using `ToggleEvent`, with the `oldState` attribute initialized to oldState and the `newState` attribute initialized to newState.

    2.   Set element's [details toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-toggle-task-tracker) to null.

3.   Set element's [details toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-toggle-task-tracker) to a struct with [task](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-task) set to the just-queued [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) and [old state](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-old-state) set to oldState.

To ensure details exclusivity by closing other elements if needed given a `details` element element:

1.   [Assert](https://infra.spec.whatwg.org/#assert): element has an `open` attribute.

2.   If element does not have a `name` attribute, or its `name` attribute is the empty string, then return.

3.   Let groupMembers be a list of elements, containing all elements in element's [details name group](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-name-group) except for element, in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

4.   [For each](https://infra.spec.whatwg.org/#list-iterate) element otherElement of groupMembers:

    1.   If the `open` attribute is set on otherElement, then:

        1.   [Assert](https://infra.spec.whatwg.org/#assert): otherElement is the only element in groupMembers that has the `open` attribute set.

        2.   [Remove](https://dom.spec.whatwg.org/#concept-element-attributes-remove) the `open` attribute on otherElement.

        3.   [Break](https://infra.spec.whatwg.org/#iteration-break).

To ensure details exclusivity by closing the given element if needed given a `details` element element:

1.   If element does not have an `open` attribute, then return.

2.   If element does not have a `name` attribute, or its `name` attribute is the empty string, then return.

3.   Let groupMembers be a list of elements, containing all elements in element's [details name group](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-name-group) except for element, in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

4.   [For each](https://infra.spec.whatwg.org/#list-iterate) element otherElement of groupMembers:

    1.   If the `open` attribute is set on otherElement, then:

        1.   [Remove](https://dom.spec.whatwg.org/#concept-element-attributes-remove) the `open` attribute on element.

        2.   [Break](https://infra.spec.whatwg.org/#iteration-break).

The following example shows the `details` element being used to hide technical details in a progress report.

```
<section class="progress window">
 <h1>Copying "Really Achieving Your Childhood Dreams"</h1>
 <details>
  <summary>Copying... <progress max="375505392" value="97543282"></progress> 25%</summary>
  <dl>
   <dt>Transfer rate:</dt> <dd>452KB/s</dd>
   <dt>Local filename:</dt> <dd>/home/rpausch/raycd.m4v</dd>
   <dt>Remote filename:</dt> <dd>/var/www/lectures/raycd.m4v</dd>
   <dt>Duration:</dt> <dd>01:16:27</dd>
   <dt>Color profile:</dt> <dd>SD (6-1-6)</dd>
   <dt>Dimensions:</dt> <dd>320×240</dd>
  </dl>
 </details>
</section>
```

The following shows how a `details` element can be used to hide some controls by default:

```
<details>
 <summary><label for=fn>Name & Extension:</label></summary>
 <p><input type=text id=fn name=fn value="Pillar Magazine.pdf">
 <p><label><input type=checkbox name=ext checked> Hide extension</label>
</details>
```

One could use this in conjunction with other `details` in a list to allow the user to collapse a set of fields down to a small set of headings, with the ability to open each one.

![Image 2](https://html.spec.whatwg.org/images/sample-details-1.png)![Image 3](https://html.spec.whatwg.org/images/sample-details-2.png)

In these examples, the summary really just summarizes what the controls can change, and not the actual values, which is less than ideal.

The following example shows the `name` attribute of the `details` element being used to create an exclusive accordion, a set of `details` elements where a user action to open one `details` element causes any open `details` to close.

```
<section class="characteristics">
 <details name="frame-characteristics">
  <summary>Material</summary>
  The picture frame is made of solid oak wood.
 </details>
 <details name="frame-characteristics">
  <summary>Size</summary>
  The picture frame fits a photo 40cm tall and 30cm wide.
  The frame is 45cm tall, 35cm wide, and 2cm thick.
 </details>
 <details name="frame-characteristics">
  <summary>Color</summary>
  The picture frame is available in its natural wood
  color, or with black stain.
 </details>
</section>
```

The following example shows what happens when the `open` attribute is set on a `details` element that is part of a set of elements using the `name` attribute to create an exclusive accordion.

Given the initial markup:

```
<section class="characteristics">
 <details name="frame-characteristics" id="d1" open>...</details>
 <details name="frame-characteristics" id="d2">...</details>
 <details name="frame-characteristics" id="d3">...</details>
</section>
```

and the script:

`document.getElementById("d2").setAttribute("open", "");`
then the resulting tree after the script executes will be equivalent to the markup:

```
<section class="characteristics">
 <details name="frame-characteristics" id="d1">...</details>
 <details name="frame-characteristics" id="d2" open>...</details>
 <details name="frame-characteristics" id="d3">...</details>
</section>
```

because setting the `open` attribute on `d2` removes it from `d1`.

The same happens when the user activates the `summary` element inside of `d2`.

Because the `open` attribute is added and removed automatically as the user interacts with the control, it can be used in CSS to style the element differently based on its state. Here, a style sheet is used to animate the color of the summary when the element is opened or closed:

```
<style>
 details > summary { transition: color 1s; color: black; }
 details[open] > summary { color: red; }
</style>
<details>
 <summary>Automated Status: Operational</summary>
 <p>Velocity: 12m/s</p>
 <p>Direction: North</p>
</details>
```

#### 4.11.2 The `summary` element[](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-summary-element)

[Element/summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary "The <summary> HTML element specifies a summary, caption, or legend for a <details> element's disclosure box. Clicking the <summary> element toggles the state of the parent <details> element open and closed.")

Support in all current engines.

Firefox 49+Safari 6+Chrome 12+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 4+Samsung Internet?Opera Android?

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):None.[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):As the [first child](https://dom.spec.whatwg.org/#concept-tree-first-child) of a `details` element.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), optionally intermixed with [heading content](https://html.spec.whatwg.org/multipage/dom.html#heading-content-2).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-summary).[For implementers](https://w3c.github.io/html-aam/#el-summary).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):Uses `HTMLElement`.
The `summary` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a summary, caption, or legend for the rest of the contents of the `summary` element's parent `details` element, if any.

A `summary` element is a summary for its parent details if the following algorithm returns true:

1.   If this `summary` element has no parent, then return false.

2.   Let parent be this `summary` element's parent.

3.   If parent is not a `details` element, then return false.

4.   If parent's first `summary` element child is not this `summary` element, then return false.

5.   Return true.

The [activation behavior](https://dom.spec.whatwg.org/#eventtarget-activation-behavior) of `summary` elements is to run the following steps:

1.   If this `summary` element is not the [summary for its parent details](https://html.spec.whatwg.org/multipage/interactive-elements.html#summary-for-its-parent-details), then return.

2.   Let parent be this `summary` element's parent.

3.   If the `open` attribute is present on parent, then [remove](https://dom.spec.whatwg.org/#concept-element-attributes-remove) it. Otherwise, [set](https://dom.spec.whatwg.org/#concept-element-attributes-set-value)parent's `open` attribute to the empty string.

This will then run the [details notification task steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#details-notification-task-steps).

#### 4.11.3 Commands[](https://html.spec.whatwg.org/multipage/interactive-elements.html#commands)

##### 4.11.3.1 Facets[](https://html.spec.whatwg.org/multipage/interactive-elements.html#facets-2)

A command is the abstraction behind menu items, buttons, and links. Once a command is defined, other parts of the interface can refer to the same command, allowing many access points to a single feature to share facets such as the [Disabled State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-disabledstate).

Commands are defined to have the following facets:

Label The name of the command as seen by the user.Access Key A key combination selected by the user agent that triggers the command. A command might not have an Access Key.Hidden State Whether the command is hidden or not (basically, whether it should be shown in menus).Disabled State Whether the command is relevant and can be triggered or not.Action The actual effect that triggering the command will have. This could be a scripted event handler, a [URL](https://url.spec.whatwg.org/#concept-url) to which to [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate), or a form submission.

User agents may expose the [commands](https://html.spec.whatwg.org/multipage/interactive-elements.html#concept-command) that match the following criteria:

*   The [Hidden State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-hiddenstate) facet is false (visible)

*   The element is [in a document](https://dom.spec.whatwg.org/#in-a-document) with a non-null [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc).

*   Neither the element nor any of its ancestors has a `hidden` attribute specified.

User agents are encouraged to do this especially for commands that have [Access Keys](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-accesskey), as a way to advertise those keys to the user.

For example, such commands could be listed in the user agent's menu bar.

##### 4.11.3.2 Using the `a` element to define a command[](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-a-element-to-define-a-command)

An `a` element with an `href` attribute [defines a command](https://html.spec.whatwg.org/multipage/interactive-elements.html#concept-command).

The [Hidden State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-hiddenstate) of the command is true (hidden) if the element has a `hidden` attribute, and false otherwise.

The [Disabled State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-disabledstate) facet of the command is true if the element or one of its ancestors is [inert](https://html.spec.whatwg.org/multipage/interaction.html#inert), and false otherwise.

##### 4.11.3.3 Using the `button` element to define a command[](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-button-element-to-define-a-command)

The [Label](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-label), [Access Key](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-accesskey), [Hidden State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-hiddenstate), and [Action](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-action) facets of the command are determined [as for `a` elements](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-a-element-to-define-a-command) (see the previous section).

The [Disabled State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-disabledstate) of the command is true if the element or one of its ancestors is [inert](https://html.spec.whatwg.org/multipage/interaction.html#inert), or if the element's [disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-disabled) state is set, and false otherwise.

##### 4.11.3.4 Using the `input` element to define a command[](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-input-element-to-define-a-command)

The [Label](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-label) of the command is determined as follows:

1.   If the `type` attribute is in one of the [Submit Button](https://html.spec.whatwg.org/multipage/input.html#submit-button-state-(type=submit)), [Reset Button](https://html.spec.whatwg.org/multipage/input.html#reset-button-state-(type=reset)), [Image Button](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)), or [Button](https://html.spec.whatwg.org/multipage/input.html#button-state-(type=button)) states, then the [Label](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-label) is the string given by the `value` attribute, if any, and a UA-dependent, locale-dependent value that the UA uses to label the button itself if the attribute is absent.

2.   Otherwise, if the element is a [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control), then the [Label](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-label) is the [descendant text content](https://dom.spec.whatwg.org/#concept-descendant-text-content) of the first `label` element in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) whose [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control) is the element in question. (In JavaScript terms, this is given by `element.labels[0].textContent`.)

3.   Otherwise, if the `value` attribute is present, then the [Label](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-label) is the value of that attribute.

4.   Otherwise, the [Label](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-label) is the empty string.

Even though the `value` attribute on `input` elements in the [Image Button](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)) state is non-conformant, the attribute can still contribute to the [Label](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-label) determination, if it is present and the Image Button's `alt` attribute is missing.

The [Hidden State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-hiddenstate) of the command is true (hidden) if the element has a `hidden` attribute, and false otherwise.

The [Disabled State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-disabledstate) of the command is true if the element or one of its ancestors is [inert](https://html.spec.whatwg.org/multipage/interaction.html#inert), or if the element's [disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-disabled) state is set, and false otherwise.

##### 4.11.3.5 Using the `option` element to define a command[](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-option-element-to-define-a-command)

An `option` element with an ancestor `select` element and either no `value` attribute or a `value` attribute that is not the empty string [defines a command](https://html.spec.whatwg.org/multipage/interactive-elements.html#concept-command).

The [Hidden State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-hiddenstate) of the command is true (hidden) if the element has a `hidden` attribute, and false otherwise.

The [Disabled State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-disabledstate) of the command is true if the element is [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-disabled), or if its nearest ancestor `select` element is [disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-disabled), or if it or one of its ancestors is [inert](https://html.spec.whatwg.org/multipage/interaction.html#inert), and false otherwise.

If the `option`'s nearest ancestor `select` element has a `multiple` attribute, the [Action](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-action) of the command is to [toggle](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-toggle) the `option` element. Otherwise, the [Action](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-action) is to [pick](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-pick) the `option` element.

##### 4.11.3.6 Using the `accesskey` attribute on a `legend` element to define a command[](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-accesskey-attribute-on-a-legend-element-to-define-a-command)

A `legend` element [defines a command](https://html.spec.whatwg.org/multipage/interactive-elements.html#concept-command) if all of the following are true:

*   It has an [assigned access key](https://html.spec.whatwg.org/multipage/interaction.html#assigned-access-key).

*   It is a child of a `fieldset` element.

*   Its parent has a descendant that [defines a command](https://html.spec.whatwg.org/multipage/interactive-elements.html#concept-command) that is neither a `label` element nor a `legend` element. This element, if it exists, is the `legend` element's `accesskey` delegatee.

The [Hidden State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-hiddenstate), [Disabled State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-disabledstate), and [Action](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-action) facets of the command are the same as the respective facets of [the `legend` element's `accesskey` delegatee](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-legend-element's-accesskey-delegatee).

In this example, the `legend` element specifies an `accesskey`, which, when activated, will delegate to the `input` element inside the `legend` element.

```
<fieldset>
 <legend accesskey=p>
  <label>I want <input name=pizza type=number step=1 value=1 min=0>
   pizza(s) with these toppings</label>
 </legend>
 <label><input name=pizza-cheese type=checkbox checked> Cheese</label>
 <label><input name=pizza-ham type=checkbox checked> Ham</label>
 <label><input name=pizza-pineapple type=checkbox> Pineapple</label>
</fieldset>
```

##### 4.11.3.7 Using the `accesskey` attribute to define a command on other elements[](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-accesskey-attribute-to-define-a-command-on-other-elements)

If one of the earlier sections that define elements that [define commands](https://html.spec.whatwg.org/multipage/interactive-elements.html#concept-command) define that this element [defines a command](https://html.spec.whatwg.org/multipage/interactive-elements.html#concept-command), then that section applies to this element, and this section does not. Otherwise, this section applies to that element.

The [Hidden State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-hiddenstate) of the command is true (hidden) if the element has a `hidden` attribute, and false otherwise.

The [Disabled State](https://html.spec.whatwg.org/multipage/interactive-elements.html#command-facet-disabledstate) of the command is true if the element or one of its ancestors is [inert](https://html.spec.whatwg.org/multipage/interaction.html#inert), and false otherwise.

#### 4.11.4 The `dialog` element[](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)

[Element/dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog "The <dialog> HTML element represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.")

Support in all current engines.

Firefox 98+Safari 15.4+Chrome 37+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLDialogElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement "The HTMLDialogElement interface provides methods to manipulate <dialog> elements. It inherits properties and methods from the HTMLElement interface.")

Support in all current engines.

Firefox 98+Safari 15.4+Chrome 37+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLDialogElement/open](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/open "The open property of the HTMLDialogElement interface is a boolean value reflecting the open HTML attribute, indicating whether the <dialog> is available for interaction.")

Support in all current engines.

Firefox 98+Safari 15.4+Chrome 37+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`closedby` — Which user actions will close the dialog `open` — Whether the dialog box is showing [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-dialog).[For implementers](https://w3c.github.io/html-aam/#el-dialog).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLDialogElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute boolean open;
  attribute DOMString returnValue;
  [CEReactions, ReflectSetter] attribute DOMString closedBy;
  [CEReactions] undefined show();
  [CEReactions] undefined showModal();
  [CEReactions] undefined close(optional DOMString returnValue);
  [CEReactions] undefined requestClose(optional DOMString returnValue);
};
```

The `dialog` element represents a transitory part of an application, in the form of a small window ("dialog box"), which the user interacts with to perform a task or gather information. Once the user is done, the dialog can be automatically closed by the application, or manually closed by the user.

Especially for modal dialogs, which are a familiar pattern across all types of applications, authors should work to ensure that dialogs in their web applications behave in a way that is familiar to users of non-web applications.

As with all HTML elements, it is not conforming to use the `dialog` element when attempting to represent another type of control. For example, context menus, tooltips, and popup listboxes are not dialog boxes, so abusing the `dialog` element to implement these patterns is incorrect.

An important part of user-facing dialog behavior is the placement of initial focus. The [dialog focusing steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-focusing-steps) attempt to pick a good candidate for initial focus when a dialog is shown, but might not be a substitute for authors carefully thinking through the correct choice to match user expectations for a specific dialog. As such, authors should use the `autofocus` attribute on the descendant element of the dialog that the user is expected to immediately interact with after the dialog opens. If there is no such element, then authors should use the `autofocus` attribute on the `dialog` element itself.

In the following example, a dialog is used for editing the details of a product in an inventory management web application.

```
<dialog>
  <label>Product Number <input type="text" readonly></label>
  <label>Product Name <input type="text" autofocus></label>
</dialog>
```

If the `autofocus` attribute was not present, the Product Number field would have been focused by the dialog focusing steps. Although that is reasonable behavior, the author determined that the more relevant field to focus was the Product Name field, as the Product Number field is readonly and expects no user input. So, the author used autofocus to override the default.

Even if the author wants to focus the Product Number field by default, they are best off explicitly specifying that by using autofocus on that `input` element. This makes the intent obvious to future readers of the code, and ensures the code stays robust in the face of future updates. (For example, if another developer added a close button, and positioned it in the node tree before the Product Number field).

Another important aspect of user behavior is whether dialogs are scrollable or not. In some cases, overflow (and thus scrollability) cannot be avoided, e.g., when it is caused by the user's high text zoom settings. But in general, scrollable dialogs are not expected by users. Adding large text nodes directly to dialog elements is particularly bad as this is likely to cause the dialog element itself to overflow. Authors are best off avoiding them.

The following terms of service dialog respects the above suggestions.

```
<dialog style="height: 80vh;">
  <div style="overflow: auto; height: 60vh;" autofocus>
    <p>By placing an order via this Web site on the first day of the fourth month of the year
    2010 Anno Domini, you agree to grant Us a non-transferable option to claim, for now and for
    ever more, your immortal soul.</p>
    <p>Should We wish to exercise this option, you agree to surrender your immortal soul,
    and any claim you may have on it, within 5 (five) working days of receiving written
    notification from  this site or one of its duly authorized minions.</p>
    <!-- ... etc., with many more <p> elements ... -->
  </div>
  <form method="dialog">
    <button type="submit" value="agree">Agree</button>
    <button type="submit" value="disagree">Disagree</button>
  </form>
</dialog>
```

Note how the [dialog focusing steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-focusing-steps) would have picked the scrollable `div` element by default, but similarly to the previous example, we have placed `autofocus` on the `div` so as to be more explicit and robust against future changes.

In contrast, if the `p` elements expressing the terms of service did not have such a wrapper `div` element, then the `dialog` itself would become scrollable, violating the above advice. Furthermore, in the absence of any `autofocus` attribute, such a markup pattern would have violated the above advice and tripped up the [dialog focusing steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-focusing-steps)'s default behavior, and caused focus to jump to the Agree `button`, which is a bad user experience.

This dialog box has some small print. The `strong` element is used to draw the user's attention to the more important part.

```
<dialog>
 <h1>Add to Wallet</h1>
 <p><strong><label for=amt>How many gold coins do you want to add to your wallet?</label></strong></p>
 <p><input id=amt name=amt type=number min=0 step=0.01 value=100></p>
 <p><small>You add coins at your own risk.</small></p>
 <p><label><input name=round type=checkbox> Only add perfectly round coins</label></p>
 <p><input type=button onclick="submit()" value="Add Coins"></p>
</dialog>
```

* * *

The `open` attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute). When specified, it indicates that the `dialog` element is active and that the user can interact with it.

The `closedby` content attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | State | Brief description |
| --- | --- | --- |
| `any` | Any | [Close requests](https://html.spec.whatwg.org/multipage/interaction.html#close-request) or clicks outside close the dialog. |
| `closerequest` | Close Request | [Close requests](https://html.spec.whatwg.org/multipage/interaction.html#close-request) close the dialog. |
| `none` | None | No user actions automatically close the dialog. |

The `closedby` attribute's _[invalid value default](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#invalid-value-default)_ and _[missing value default](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#missing-value-default)_ are both the Auto state.

The [Auto](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby-auto-state) state behaves as [Close Request](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby-closerequest-state) state when the `dialog` was shown using its `showModal()` method; otherwise the [None](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby-none-state) state.

A `dialog` element without an `open` attribute specified should not be shown to the user. This requirement may be implemented indirectly through the style layer. For example, user agents that [support the suggested default rendering](https://html.spec.whatwg.org/multipage/infrastructure.html#renderingUA) implement this requirement using the CSS rules described in the [Rendering section](https://html.spec.whatwg.org/multipage/rendering.html#rendering).

Removing the `open` attribute will usually hide the dialog. However, doing so has a number of strange additional consequences:

*   The `close` event will not be fired.

*   The `close()` method, and any [close requests](https://html.spec.whatwg.org/multipage/interaction.html#close-request), will no longer be able to close the dialog.

*   If the dialog was shown using its `showModal()` method, the `Document` will still be [blocked](https://html.spec.whatwg.org/multipage/interaction.html#blocked-by-a-modal-dialog).

For these reasons, it is generally better to never remove the `open` attribute manually. Instead, use the `requestClose()` or `close()` methods to close the dialog, or the `hidden` attribute to hide it.

The `tabindex` attribute must not be specified on `dialog` elements.

* * *

`dialog.show()`

[HTMLDialogElement/show](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/show "The show() method of the HTMLDialogElement interface displays the dialog modelessly, i.e. still allowing interaction with content outside of the dialog.")

Support in all current engines.

Firefox 98+Safari 15.4+Chrome 37+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Displays the `dialog` element.

`dialog.showModal()`

[HTMLDialogElement/showModal](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal "The showModal() method of the HTMLDialogElement interface displays the dialog as a modal, over the top of any other dialogs that might be present. It displays in the top layer, along with a ::backdrop pseudo-element. Interaction outside the dialog is blocked and the content outside it is rendered inert.")

Support in all current engines.

Firefox 98+Safari 15.4+Chrome 37+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Displays the `dialog` element and makes it the top-most modal dialog.

This method honors the `autofocus` attribute.

`dialog.close([ result ])`

[HTMLDialogElement/close](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close "The close() method of the HTMLDialogElement interface closes the <dialog>. An optional string may be passed as an argument, updating the returnValue of the dialog.")

Support in all current engines.

Firefox 98+Safari 15.4+Chrome 37+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Closes the `dialog` element.

The argument, if provided, provides a return value.

`dialog.requestClose([ result ])`
Acts as if a [close request](https://html.spec.whatwg.org/multipage/interaction.html#close-request) was sent targeting dialog, by first firing a `cancel` event, and if that event is not canceled with `preventDefault()`, proceeding to close the dialog in the same way as the `close()` method (including firing a `close` event).

This is a helper utility that can be used to consolidate cancelation and closing logic into the `cancel` and `close` event handlers, by having all non-[close request](https://html.spec.whatwg.org/multipage/interaction.html#close-request) closing affordances call this method.

Note that this method ignores the `closedby` attribute: that is, even if `closedby` is set to "`none`", the same behavior will apply.

The argument, if provided, provides a return value.

`dialog.returnValue [ = result ]`

[HTMLDialogElement/returnValue](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/returnValue "The returnValue property of the HTMLDialogElement interface gets or sets the return value for the <dialog>, usually to indicate which button the user pressed to close it.")

Support in all current engines.

Firefox 98+Safari 15.4+Chrome 37+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns the `dialog`'s return value.

Can be set, to update the return value.

The `show()` method steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this) has an `open` attribute and [is modal](https://html.spec.whatwg.org/multipage/interactive-elements.html#is-modal) of [this](https://webidl.spec.whatwg.org/#this) is false, then return.

2.   If [this](https://webidl.spec.whatwg.org/#this) has an `open` attribute, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

3.   If the result of [firing an event](https://dom.spec.whatwg.org/#concept-event-fire) named `beforetoggle`, using `ToggleEvent`, with the `cancelable` attribute initialized to true, the `oldState` attribute initialized to "`closed`", and the `newState` attribute initialized to "`open`" at [this](https://webidl.spec.whatwg.org/#this) is false, then return.

4.   If [this](https://webidl.spec.whatwg.org/#this) has an `open` attribute, then return.

5.   [Queue a dialog toggle event task](https://html.spec.whatwg.org/multipage/interactive-elements.html#queue-a-dialog-toggle-event-task) given [this](https://webidl.spec.whatwg.org/#this), "`closed`", "`open`", and null.

6.   Add an `open` attribute to [this](https://webidl.spec.whatwg.org/#this), whose value is the empty string.

7.   Set [this](https://webidl.spec.whatwg.org/#this)'s [previously focused element](https://html.spec.whatwg.org/multipage/interactive-elements.html#previously-focused-element) to the [focused](https://html.spec.whatwg.org/multipage/interaction.html#focused) element.

8.   Let document be [this](https://webidl.spec.whatwg.org/#this)'s [node document](https://dom.spec.whatwg.org/#concept-node-document).

9.   Let hideUntil be the result of running [topmost popover ancestor](https://html.spec.whatwg.org/multipage/popover.html#topmost-popover-ancestor) given [this](https://webidl.spec.whatwg.org/#this), document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list), null, and false.

10.   If hideUntil is null, then set hideUntil to the result of running [topmost popover ancestor](https://html.spec.whatwg.org/multipage/popover.html#topmost-popover-ancestor) given [this](https://webidl.spec.whatwg.org/#this), document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list), null, and false.

11.   If hideUntil is null, then set hideUntil to document.

12.   Run [hide all popovers until](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) given hideUntil, false, and true.

13.   Run the [dialog focusing steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-focusing-steps) given [this](https://webidl.spec.whatwg.org/#this).

The `showModal()` method steps are to [show a modal dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#show-a-modal-dialog) given [this](https://webidl.spec.whatwg.org/#this) and null.

The `close(returnValue)` method steps are:

1.   If returnValue is not given, then set it to null.

2.   [Close the dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#close-the-dialog)[this](https://webidl.spec.whatwg.org/#this) with returnValue and null.

The `requestClose(returnValue)` method steps are:

1.   If returnValue is not given, then set it to null.

2.   [Request to close the dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-request-close)[this](https://webidl.spec.whatwg.org/#this) with returnValue and null.

We use show/close as the verbs for `dialog` elements, as opposed to verb pairs that are more commonly thought of as antonyms such as show/hide or open/close, due to the following constraints:

*   Hiding a dialog is different from closing one. Closing a dialog gives it a return value, fires an event, unblocks the page for other dialogs, and so on. Whereas hiding a dialog is a purely visual property, and is something you can already do with the `hidden` attribute or by removing the `open` attribute. (See also the [note above](https://html.spec.whatwg.org/multipage/interactive-elements.html#note-dialog-remove-open-attribute) about removing the `open` attribute, and how hiding the dialog in that way is generally not desired.)

*   Showing a dialog is different from opening one. Opening a dialog consists of creating and showing that dialog (similar to how `window.open()` both creates and shows a new window). Whereas showing the dialog is the process of taking a `dialog` element that is already in the DOM, and making it interactive and visible to the user.

*   If we were to have a `dialog.open()` method despite the above, it would conflict with the `dialog.open` property.

Furthermore, a [survey](https://lists.whatwg.org/pipermail/whatwg-whatwg.org/2013-December/041799.html) of many other UI frameworks contemporary to the original design of the `dialog` element made it clear that the show/close verb pair was reasonably common.

In summary, it turns out that the implications of certain verbs, and how they are used in technology contexts, mean that paired actions such as showing and closing a dialog are not always expressible as antonyms.

The `returnValue` IDL attribute, on getting, must return the last value to which it was set. On setting, it must be set to the new value. When the element is created, it must be set to the empty string.

The `closedBy` getter steps are to return the keyword corresponding to the [computed closed-by state](https://html.spec.whatwg.org/multipage/interactive-elements.html#computed-closed-by-state) given [this](https://webidl.spec.whatwg.org/#this).

* * *

Each `Document` has a dialog pointerdown target, which is an [HTML dialog element](https://html.spec.whatwg.org/multipage/interactive-elements.html#htmldialogelement) or null, initially null.

Each [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) has a previously focused element which is null or an element, and it is initially null. When `showModal()` and `show()` are called, this element is set to the currently [focused](https://html.spec.whatwg.org/multipage/interaction.html#focused) element before running the [dialog focusing steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-focusing-steps). Elements with the `popover` attribute set this element to the currently [focused](https://html.spec.whatwg.org/multipage/interaction.html#focused) element during the [show popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#show-popover).

Each `dialog` element has a dialog toggle task tracker, which is a [toggle task tracker](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-tracker) or null, initially null.

Each `dialog` element has a close watcher, which is a [close watcher](https://html.spec.whatwg.org/multipage/interaction.html#close-watcher) or null, initially null.

Each `dialog` element has a request close return value, which is a string or null, initially null.

Each `dialog` element has a request close source element, which is an `Element` or null, initially null.

Each `dialog` element has an enable close watcher for request close boolean, initially false.

`dialog`'s [enable close watcher for request close](https://html.spec.whatwg.org/multipage/interactive-elements.html#enable-close-watcher-for-requestclose()) is used to force enable the dialog's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher) while [requesting to close](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-request-close) it. A dialog whose [computed closed-by state](https://html.spec.whatwg.org/multipage/interactive-elements.html#computed-closed-by-state) is the [None](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby-none-state) state would otherwise have a disabled [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher).

Each `dialog` element has an is modal boolean, initially false.

* * *

The following [attribute change steps](https://dom.spec.whatwg.org/#concept-element-attributes-change-ext), given element, localName, oldValue, value, and namespace are used for `dialog` elements:

1.   If namespace is not null, then return.

2.   If localName is not `open`, then return.

3.   If value is null and oldValue is not null, then run the [dialog cleanup steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-cleanup-steps) given element.

4.   If element's [node document](https://dom.spec.whatwg.org/#concept-node-document) is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then return.

5.   If element is not [connected](https://dom.spec.whatwg.org/#connected), then return.

This ensures that the dialog setup steps are not run on nodes that are disconnected, which would result in a [close watcher](https://html.spec.whatwg.org/multipage/interaction.html#close-watcher) being established. The [dialog cleanup steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-cleanup-steps) need no such guard.

6.   If value is not null and oldValue is null, then run the [dialog setup steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-setup-steps) given element.

To show a modal dialog given a `dialog` element subject and an `Element` or null source:

1.   If subject has an `open` attribute and [is modal](https://html.spec.whatwg.org/multipage/interactive-elements.html#is-modal) of subject is true, then return.

2.   If subject has an `open` attribute, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

3.   If subject's [node document](https://dom.spec.whatwg.org/#concept-node-document) is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

4.   If subject is not [connected](https://dom.spec.whatwg.org/#connected), then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

5.   If subject is in the [popover showing state](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state), then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

6.   If the result of [firing an event](https://dom.spec.whatwg.org/#concept-event-fire) named `beforetoggle`, using `ToggleEvent`, with the `cancelable` attribute initialized to true, the `oldState` attribute initialized to "`closed`", the `newState` attribute initialized to "`open`", and the `source` attribute initialized to source at subject is false, then return.

7.   If subject has an `open` attribute, then return.

8.   If subject is not [connected](https://dom.spec.whatwg.org/#connected), then return.

9.   If subject is in the [popover showing state](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state), then return.

10.   [Queue a dialog toggle event task](https://html.spec.whatwg.org/multipage/interactive-elements.html#queue-a-dialog-toggle-event-task) given subject, "`closed`", "`open`", and source.

11.   Add an `open` attribute to subject, whose value is the empty string.

12.   [Assert](https://infra.spec.whatwg.org/#assert): subject's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher) is not null.

13.   Set [is modal](https://html.spec.whatwg.org/multipage/interactive-elements.html#is-modal) of subject to true.

14.   Set subject's [node document](https://dom.spec.whatwg.org/#concept-node-document) to be [blocked by the modal dialog](https://html.spec.whatwg.org/multipage/interaction.html#blocked-by-a-modal-dialog)subject.

[](https://html.spec.whatwg.org/multipage/interactive-elements.html#note-dialog-plus-focus-fixup)This will cause the [focused area of the document](https://html.spec.whatwg.org/multipage/interaction.html#focused-area-of-the-document) to become [inert](https://html.spec.whatwg.org/multipage/interaction.html#inert) (unless that currently focused area is a [shadow-including descendant](https://dom.spec.whatwg.org/#concept-shadow-including-descendant) of subject). In such cases, the [focused area of the document](https://html.spec.whatwg.org/multipage/interaction.html#focused-area-of-the-document) will soon be [reset](https://html.spec.whatwg.org/multipage/webappapis.html#focus-fixup-rule) to the [viewport](https://drafts.csswg.org/css2/#viewport). In a couple steps we will attempt to find a better candidate to focus.

15.   If subject's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [top layer](https://drafts.csswg.org/css-position-4/#document-top-layer) does not already [contain](https://infra.spec.whatwg.org/#list-contain)subject, then [add an element to the top layer](https://drafts.csswg.org/css-position-4/#add-an-element-to-the-top-layer) given subject.

16.   Set subject's [previously focused element](https://html.spec.whatwg.org/multipage/interactive-elements.html#previously-focused-element) to the [focused](https://html.spec.whatwg.org/multipage/interaction.html#focused) element.

17.   Let document be subject's [node document](https://dom.spec.whatwg.org/#concept-node-document).

18.   Let hideUntil be the result of running [topmost popover ancestor](https://html.spec.whatwg.org/multipage/popover.html#topmost-popover-ancestor) given subject, document's [showing hint popover list](https://html.spec.whatwg.org/multipage/popover.html#showing-hint-popover-list), null, and false.

19.   If hideUntil is null, then set hideUntil to the result of running [topmost popover ancestor](https://html.spec.whatwg.org/multipage/popover.html#topmost-popover-ancestor) given subject, document's [showing auto popover list](https://html.spec.whatwg.org/multipage/popover.html#auto-popover-list), null, and false.

20.   If hideUntil is null, then set hideUntil to document.

21.   Run [hide all popovers until](https://html.spec.whatwg.org/multipage/popover.html#hide-all-popovers-until) given hideUntil, false, and true.

22.   Run the [dialog focusing steps](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-focusing-steps) given subject.

To set the dialog close watcher, given a `dialog` element dialog:

1.   [Assert](https://infra.spec.whatwg.org/#assert): dialog's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher) is null.

2.   [Assert](https://infra.spec.whatwg.org/#assert): dialog has an `open` attribute and dialog's [node document](https://dom.spec.whatwg.org/#concept-node-document) is [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active).

3.   Set dialog's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher) to the result of [establishing a close watcher](https://html.spec.whatwg.org/multipage/interaction.html#establish-a-close-watcher) given dialog's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), with:

    *   _[cancelAction](https://html.spec.whatwg.org/multipage/interaction.html#create-close-watcher-cancelaction)_ given canPreventClose being to return the result of [firing an event](https://dom.spec.whatwg.org/#concept-event-fire) named `cancel` at dialog, with the `cancelable` attribute initialized to canPreventClose.

    *   _[closeAction](https://html.spec.whatwg.org/multipage/interaction.html#create-close-watcher-closeaction)_ being to [close the dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#close-the-dialog) given dialog, dialog's [request close return value](https://html.spec.whatwg.org/multipage/interactive-elements.html#request-close-return-value), and dialog's [request close source element](https://html.spec.whatwg.org/multipage/interactive-elements.html#request-close-source-element).

    *   _[getEnabledState](https://html.spec.whatwg.org/multipage/interaction.html#create-close-watcher-getenabledstate)_ being to return true if dialog's [enable close watcher for request close](https://html.spec.whatwg.org/multipage/interactive-elements.html#enable-close-watcher-for-requestclose()) is true or dialog's [computed closed-by state](https://html.spec.whatwg.org/multipage/interactive-elements.html#computed-closed-by-state) is not [None](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby-none-state); otherwise false.

The [command steps](https://html.spec.whatwg.org/multipage/form-elements.html#command-steps) for `dialog` elements, given an element element, an element source, and a `command` attribute command, are:

1.   If element is in the [popover showing](https://html.spec.whatwg.org/multipage/popover.html#popover-showing-state) state, then return.

2.   If command is in the [Close](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-close-state) state and element has an `open` attribute, then [close the dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#close-the-dialog)element with source's [optional value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-optional-value) and source.

3.   If command is in the [Request Close](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-request-close-state) state and element has an `open` attribute, then [request to close the dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-request-close)element with source's [optional value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-optional-value) and source.

4.   If command is the [Show Modal](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-show-modal-state) state and element does not have an `open` attribute, then [show a modal dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#show-a-modal-dialog) given element and source.

The following buttons use `commandfor` to open and close a "confirm" `dialog` as modal when activated:

```
<button type=button
        commandfor="the-dialog"
        command="show-modal">
 Delete
</button>
<dialog id="the-dialog">
 <form action="/delete" method="POST">
  <button type="submit">
   Delete
  </button>
  <button commandfor="the-dialog"
          command="close">
   Cancel
  </button>
 </form>
</dialog>
```

When a `dialog` element subject is to be closed, with null or a string result and an `Element` or null source, run these steps:

1.   If subject does not have an `open` attribute, then return.

2.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `beforetoggle`, using `ToggleEvent`, with the `oldState` attribute initialized to "`open`", the `newState` attribute initialized to "`closed`", and the `source` attribute initialized to source at subject.

3.   If subject does not have an `open` attribute, then return.

4.   [Queue a dialog toggle event task](https://html.spec.whatwg.org/multipage/interactive-elements.html#queue-a-dialog-toggle-event-task) given subject, "`open`", "`closed`", and source.

5.   Remove subject's `open` attribute.

6.   If [is modal](https://html.spec.whatwg.org/multipage/interactive-elements.html#is-modal) of subject is true, then [request an element to be removed from the top layer](https://drafts.csswg.org/css-position-4/#request-an-element-to-be-removed-from-the-top-layer) given subject.

7.   Let wasModal be the value of subject's [is modal](https://html.spec.whatwg.org/multipage/interactive-elements.html#is-modal) flag.

8.   Set [is modal](https://html.spec.whatwg.org/multipage/interactive-elements.html#is-modal) of subject to false.

9.   If result is not null, then set subject's `returnValue` attribute to result.

10.   Set subject's [request close return value](https://html.spec.whatwg.org/multipage/interactive-elements.html#request-close-return-value) to null.

11.   Set subject's [request close source element](https://html.spec.whatwg.org/multipage/interactive-elements.html#request-close-source-element) to null.

12.   If subject's [previously focused element](https://html.spec.whatwg.org/multipage/interactive-elements.html#previously-focused-element) is not null, then:

    1.   Let element be subject's [previously focused element](https://html.spec.whatwg.org/multipage/interactive-elements.html#previously-focused-element).

    2.   Set subject's [previously focused element](https://html.spec.whatwg.org/multipage/interactive-elements.html#previously-focused-element) to null.

    3.   If subject's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [focused area of the document](https://html.spec.whatwg.org/multipage/interaction.html#focused-area-of-the-document)'s [DOM anchor](https://html.spec.whatwg.org/multipage/interaction.html#dom-anchor) is a [shadow-including inclusive descendant](https://dom.spec.whatwg.org/#concept-shadow-including-inclusive-descendant) of subject, or wasModal is true, then run the [focusing steps](https://html.spec.whatwg.org/multipage/interaction.html#focusing-steps) for element; the viewport should not be scrolled by doing this step.

13.   [Queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) on the [user interaction task source](https://html.spec.whatwg.org/multipage/webappapis.html#user-interaction-task-source) given the subject element to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `close` at subject.

To request to close`dialog` element subject, given null or a string returnValue and null or an `Element`source:

1.   If subject does not have an `open` attribute, then return.

2.   If subject is not [connected](https://dom.spec.whatwg.org/#connected) or subject's [node document](https://dom.spec.whatwg.org/#concept-node-document) is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then return.

3.   [Assert](https://infra.spec.whatwg.org/#assert): subject's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher) is not null.

4.   Set subject's [enable close watcher for request close](https://html.spec.whatwg.org/multipage/interactive-elements.html#enable-close-watcher-for-requestclose()) to true.

5.   Set subject's [request close return value](https://html.spec.whatwg.org/multipage/interactive-elements.html#request-close-return-value) to returnValue.

6.   Set subject's [request close source element](https://html.spec.whatwg.org/multipage/interactive-elements.html#request-close-source-element) to source.

7.   [Request to close](https://html.spec.whatwg.org/multipage/interaction.html#close-watcher-request-close)subject's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher) with false.

8.   Set subject's [enable close watcher for request close](https://html.spec.whatwg.org/multipage/interactive-elements.html#enable-close-watcher-for-requestclose()) to false.

To queue a dialog toggle event task given a `dialog` element element, a string oldState, a string newState, and an `Element` or null source:

1.   If element's [dialog toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-toggle-task-tracker) is not null, then:

    1.   Set oldState to element's [dialog toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-toggle-task-tracker)'s [old state](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-old-state).

    2.   Remove element's [dialog toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-toggle-task-tracker)'s [task](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-task) from its [task queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue).

    3.   Set element's [dialog toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-toggle-task-tracker) to null.

2.   [Queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) given the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) and element to run the following steps:

    1.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `toggle` at element, using `ToggleEvent`, with the `oldState` attribute initialized to oldState, the `newState` attribute initialized to newState, and the `source` attribute initialized to source.

    2.   Set element's [dialog toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-toggle-task-tracker) to null.

3.   Set element's [dialog toggle task tracker](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-toggle-task-tracker) to a struct with [task](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-task) set to the just-queued [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) and [old state](https://html.spec.whatwg.org/multipage/interaction.html#toggle-task-old-state) set to oldState.

To retrieve a dialog's computed closed-by state, given a `dialog`dialog:

1.   If the state of dialog's `closedby` attribute is [Auto](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby-auto-state):

    1.   If dialog's [is modal](https://html.spec.whatwg.org/multipage/interactive-elements.html#is-modal) is true, then return [Close Request](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby-closerequest-state).

    2.   Return [None](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby-none-state).

2.   Return the state of dialog's `closedby` attribute.

The dialog focusing steps, given a `dialog` element subject, are as follows:

1.   If the [allow focus steps](https://html.spec.whatwg.org/multipage/interaction.html#allow-focus-steps) given subject's [node document](https://dom.spec.whatwg.org/#concept-node-document) return false, then return.

2.   Let control be null.

3.   If subject has the `autofocus` attribute, then set control to subject.

4.   If control is null, then set control to the [focus delegate](https://html.spec.whatwg.org/multipage/interaction.html#focus-delegate) of subject.

5.   If control is null, then set control to subject.

6.   Run the [focusing steps](https://html.spec.whatwg.org/multipage/interaction.html#focusing-steps) for control.

If control is not [focusable](https://html.spec.whatwg.org/multipage/interaction.html#focusable), this will do nothing. This would only happen if subject had no focus delegate, and the user agent decided that `dialog` elements were not generally focusable. In that case, any [earlier modifications](https://html.spec.whatwg.org/multipage/interactive-elements.html#note-dialog-plus-focus-fixup) to the [focused area of the document](https://html.spec.whatwg.org/multipage/interaction.html#focused-area-of-the-document) will apply.

7.   Let topDocument be control's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-top)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

8.   If control's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is not the [same](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) as the [origin](https://dom.spec.whatwg.org/#concept-document-origin) of topDocument, then return.

9.   [Empty](https://infra.spec.whatwg.org/#list-empty)topDocument's [autofocus candidates](https://html.spec.whatwg.org/multipage/interaction.html#autofocus-candidates).

10.   Set topDocument's [autofocus processed flag](https://html.spec.whatwg.org/multipage/interaction.html#autofocus-processed-flag) to true.

The dialog cleanup steps, given a `dialog` element subject, are as follows:

1.   [Remove](https://infra.spec.whatwg.org/#list-remove)subject from subject's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [open dialogs list](https://html.spec.whatwg.org/multipage/dom.html#open-dialogs-list).

2.   If subject's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher) is not null, then:

    1.   [Destroy](https://html.spec.whatwg.org/multipage/interaction.html#close-watcher-destroy)subject's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher).

    2.   Set subject's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher) to null.

#### 4.11.5 Dialog light dismiss[](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-light-dismiss)

"Light dismiss" means that clicking outside of a `dialog` element whose `closedby` attribute is in the [Any](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby-any-state) state will close the `dialog` element. This is in addition to how such `dialog`s respond to [close requests](https://html.spec.whatwg.org/multipage/interaction.html#close-request).

To light dismiss open dialogs, given a `PointerEvent`event:

1.   [Assert](https://infra.spec.whatwg.org/#assert): event's `isTrusted` attribute is true.

2.   Let document be event's [target](https://dom.spec.whatwg.org/#concept-event-target)'s [node document](https://dom.spec.whatwg.org/#concept-node-document).

3.   If document's [open dialogs list](https://html.spec.whatwg.org/multipage/dom.html#open-dialogs-list) is [empty](https://infra.spec.whatwg.org/#list-is-empty), then return.

4.   Let ancestor be the result of running [nearest clicked dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#nearest-clicked-dialog) given event.

5.   If event's `type` is "`pointerdown`", then set document's [dialog pointerdown target](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-pointerdown-target) to ancestor.

6.   If event's `type` is "`pointerup`", then:

    1.   Let sameTarget be true if ancestor is document's [dialog pointerdown target](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-pointerdown-target).

    2.   Set document's [dialog pointerdown target](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-pointerdown-target) to null.

    3.   If sameTarget is false, then return.

    4.   Let topmostDialog be the last element of document's [open dialogs list](https://html.spec.whatwg.org/multipage/dom.html#open-dialogs-list).

    5.   If ancestor is topmostDialog, then return.

    6.   If topmostDialog's [computed closed-by state](https://html.spec.whatwg.org/multipage/interactive-elements.html#computed-closed-by-state) is not [Any](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby-any-state), then return.

    7.   [Assert](https://infra.spec.whatwg.org/#assert): topmostDialog's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher) is not null.

    8.   [Request to close](https://html.spec.whatwg.org/multipage/interaction.html#close-watcher-request-close)topmostDialog's [close watcher](https://html.spec.whatwg.org/multipage/interactive-elements.html#dialog-close-watcher) with false.

[Run light dismiss activities](https://html.spec.whatwg.org/multipage/interactive-elements.html#run-light-dismiss-activities) will be called by the [Pointer Events spec](https://github.com/w3c/pointerevents/pull/460) when the user clicks or touches anywhere on the page.

To find the nearest clicked dialog, given a `PointerEvent`event:

1.   Let target be event's [target](https://dom.spec.whatwg.org/#concept-event-target).

2.   If target is a `dialog` element, target has an `open` attribute, target's [is modal](https://html.spec.whatwg.org/multipage/interactive-elements.html#is-modal) is true, and event's `clientX` and `clientY` are outside the bounds of target, then return null.

The check for `clientX` and `clientY` is because a pointer event that hits the `::backdrop` pseudo element of a dialog will result in event having a target of the dialog element itself.

3.   Let currentNode be target.

4.   While currentNode is not null:

    1.   If currentNode is a `dialog` element and currentNode has an `open` attribute, then return currentNode.

    2.   Set currentNode to currentNode's parent in the [flat tree](https://drafts.csswg.org/css-scoping/#flat-tree).

5.   Return null.

[← 4.10.18 Form control infrastructure](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.12 Scripting →](https://html.spec.whatwg.org/multipage/scripting.html)
