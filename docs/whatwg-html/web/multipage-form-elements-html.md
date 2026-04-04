# Source: https://html.spec.whatwg.org/multipage/form-elements.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/form-elements.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 4.10.5 The input element](https://html.spec.whatwg.org/multipage/input.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.10.18 Form control infrastructure →](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html)
1.       1.           1.   [4.10.6 The `button` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element)
        2.   [4.10.7 The `select` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-select-element)
        3.   [4.10.8 The `datalist` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-datalist-element)
        4.   [4.10.9 The `optgroup` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-optgroup-element)
        5.   [4.10.10 The `option` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-option-element)
        6.   [4.10.11 The `textarea` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-textarea-element)
        7.   [4.10.12 The `output` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-output-element)
        8.   [4.10.13 The `progress` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-progress-element)
        9.   [4.10.14 The `meter` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-meter-element)
        10.   [4.10.15 The `fieldset` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-fieldset-element)
        11.   [4.10.16 The `legend` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-legend-element)
        12.   [4.10.17 The `selectedcontent` element](https://html.spec.whatwg.org/multipage/form-elements.html#the-selectedcontent-element)

#### 4.10.6 The `button` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element)

[Element/button](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button "The <button> HTML element is an interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it then performs an action, such as submitting a form or opening a dialog.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera 15+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 14+

[HTMLButtonElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLButtonElement "The HTMLButtonElement interface provides properties and methods (beyond the regular HTMLElement interface it also has available to it by inheritance) for manipulating <button> elements.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2).[Listed](https://html.spec.whatwg.org/multipage/forms.html#category-listed), [labelable](https://html.spec.whatwg.org/multipage/forms.html#category-label), [submittable](https://html.spec.whatwg.org/multipage/forms.html#category-submit), and [autocapitalize-and-autocorrect inheriting](https://html.spec.whatwg.org/multipage/forms.html#category-autocapitalize)[form-associated element](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected.As the first child of a `select` element.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but there must be no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendant and no descendant with the `tabindex` attribute specified. If the element is the first child of a `select` element, then it may also have zero or one descendant `selectedcontent` element.[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`command` — Indicates to the targeted element which action to take. `commandfor` — Targets another element to be invoked. `disabled` — Whether the form control is disabled `form` — Associates the element with a `form` element `formaction` — [URL](https://url.spec.whatwg.org/#concept-url) to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`formenctype` — [Entry list](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#entry-list) encoding type to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`formmethod` — Variant to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`formnovalidate` — Bypass form control validation for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`formtarget` — [Navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`name` — Name of the element to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2) and in the `form.elements` API `popovertarget` — Targets a popover element to toggle, show, or hide `popovertargetaction` — Indicates whether a targeted popover element is to be toggled, shown, or hidden `type` — Type of button `value` — Value to be used for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-button).[For implementers](https://w3c.github.io/html-aam/#el-button).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLButtonElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, ReflectSetter] attribute DOMString command;
  [CEReactions, Reflect] attribute Element? commandForElement;
  [CEReactions, Reflect] attribute boolean disabled;
  readonly attribute HTMLFormElement? form;
  [CEReactions, ReflectSetter] attribute USVString formAction;
  [CEReactions] attribute DOMString formEnctype;
  [CEReactions] attribute DOMString formMethod;
  [CEReactions, Reflect] attribute boolean formNoValidate;
  [CEReactions, Reflect] attribute DOMString formTarget;
  [CEReactions, Reflect] attribute DOMString name;
  [CEReactions, ReflectSetter] attribute DOMString type;
  [CEReactions, Reflect] attribute DOMString value;

  readonly attribute boolean willValidate;
  readonly attribute ValidityState validity;
  readonly attribute DOMString validationMessage;
  boolean checkValidity();
  boolean reportValidity();
  undefined setCustomValidity(DOMString error);

  readonly attribute NodeList labels;
};
HTMLButtonElement includes PopoverTargetAttributes;
```

The `button` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a button labeled by its contents.

The element is a [button](https://html.spec.whatwg.org/multipage/forms.html#concept-button).

The `type` attribute controls the behavior of the button when it is activated. It is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | State | Brief description |
| --- | --- | --- |
| `submit` | Submit Button | Submits the form. |
| `reset` | Reset Button | Resets the form. |
| `button` | Button | Does nothing. |

A `button` element is said to be a [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button) if any of the following are true:

*   the `type` attribute is in the [Auto](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-type-auto-state) state, both the `command` and `commandfor` content attributes are not present, and the [parent](https://dom.spec.whatwg.org/#concept-tree-parent) node is not a `select` element; or

*   the `type` attribute is in the [Submit Button](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-type-submit-state) state.

If a `button` element is the first [child](https://dom.spec.whatwg.org/#concept-tree-child) which is an [element](https://dom.spec.whatwg.org/#interface-element) of a `select` element, then it is [inert](https://html.spec.whatwg.org/multipage/interaction.html#inert).

If specified, the `commandfor` attribute value must be the [ID](https://dom.spec.whatwg.org/#concept-id) of an element in the same [tree](https://dom.spec.whatwg.org/#concept-tree) as the [button](https://html.spec.whatwg.org/multipage/forms.html#concept-button) with the `commandfor` attribute.

The `command` attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | State | Brief description |
| --- | --- | --- |
| `toggle-popover` | Toggle Popover | Shows or hides the targeted `popover` element. |
| `show-popover` | Show Popover | Shows the targeted `popover` element. |
| `hide-popover` | Hide Popover | Hides the targeted `popover` element. |
| `close` | Close | Closes the targeted `dialog` element. |
| `request-close` | Request Close | Requests to close the targeted `dialog` element. |
| `show-modal` | Show Modal | Opens the targeted `dialog` element as modal. |
| A [custom command keyword](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-custom) | Custom | Only dispatches the `command` event on the targeted element. |

A custom command keyword is a string that [starts with](https://infra.spec.whatwg.org/#string-starts-with) "`--`".

To determine if a command is valid for a target given a `command` attribute command and an element target:

1.   If command is in the [Unknown](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-unknown-state) state, then return false.

2.   If command is in the [Custom](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-custom-state) state, then return true.

3.   If target is not an [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements), then return false.

4.   If command is in any of the following states:

    *   [Toggle Popover](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-toggle-popover-state)

    *   [Show Popover](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-show-popover-state)

    *   [Hide Popover](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-hide-popover-state)

then return true.

5.   If this standard does not define [is valid command steps](https://html.spec.whatwg.org/multipage/form-elements.html#is-valid-command-steps) for target's [local name](https://dom.spec.whatwg.org/#concept-element-local-name), then return false.

6.   Otherwise, return the result of running target's corresponding [is valid command steps](https://html.spec.whatwg.org/multipage/form-elements.html#is-valid-command-steps) given command.

The intent is to avoid dispatching a command event on an element type that does not support that command.

However, element state is not considered. If an element can support a particular command, the event is dispatched, even if that element is in a state where it cannot execute that command.

This means, for example, that command events are dispatched for popover commands on all [HTML elements](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements), even if they do not have a `popover` attribute.

A `button` element element's [activation behavior](https://dom.spec.whatwg.org/#eventtarget-activation-behavior) given event is:

1.   If element is [disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-disabled), then return.

2.   If element's [node document](https://dom.spec.whatwg.org/#concept-node-document) is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then return.

3.   If element has a [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner):

    1.   If element is a [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button), then [submit](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-submit)element's [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) from element with _[userInvolvement](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#submit-user-involvement)_ set to event's [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#event-uni), and return.

    2.   If element's `type` attribute is in the [Reset Button](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-type-reset-state) state, then [reset](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-reset)element's [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner), and return.

    3.   If element's `type` attribute is in the [Auto](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-type-auto-state) state, then return.

4.   Let target be the result of running element's [get the `commandfor`-associated element](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#attr-associated-element).

5.   If target is not null:

    1.   Let command be element's `command` attribute.

    2.   If the result of [determining if a command is valid for a target](https://html.spec.whatwg.org/multipage/form-elements.html#determine-if-command-is-valid) given command and target is false, then return.

    3.   Let continue be the result of [firing an event](https://dom.spec.whatwg.org/#concept-event-fire) named `command` at target, using `CommandEvent`, with its `command` attribute initialized to command, its `source` attribute initialized to element, and its `cancelable` attribute initialized to true.

[DOM standard issue #1328](https://github.com/whatwg/dom/issues/1328) tracks how to better standardize associated event data in a way which makes sense on Events. Currently an event attribute initialized to a value cannot also have a getter, and so an internal slot (or map of additional fields) is required to properly specify this.

    4.   If continue is false, then return.

    5.   If target is not [connected](https://dom.spec.whatwg.org/#connected), then return.

    6.   If command is in the [Custom](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-custom-state) state, then return.

    7.   If command is in the [Hide Popover](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-hide-popover-state) state:

        1.   If the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given target, true, false, and null is true, then run the [hide popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-algorithm) given target, true, true, false, and element.

    8.   Otherwise, if command is in the [Toggle Popover](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-toggle-popover-state) state:

        1.   If the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given target, false, false, and null is true, then run the [show popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#show-popover) given target, false, and [this](https://webidl.spec.whatwg.org/#this).

        2.   Otherwise, if the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given target, true, false, and null is true, then run the [hide popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#hide-popover-algorithm) given target, true, true, false, and element.

    9.   Otherwise, if command is in the [Show Popover](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-show-popover-state) state:

        1.   If the result of running [check popover validity](https://html.spec.whatwg.org/multipage/popover.html#check-popover-validity) given target, false, false, and null is true, then run the [show popover algorithm](https://html.spec.whatwg.org/multipage/popover.html#show-popover) given target, false, and [this](https://webidl.spec.whatwg.org/#this).

    10.   Otherwise, if this standard defines [command steps](https://html.spec.whatwg.org/multipage/form-elements.html#command-steps) for target's [local name](https://dom.spec.whatwg.org/#concept-element-local-name), then run the corresponding [command steps](https://html.spec.whatwg.org/multipage/form-elements.html#command-steps) given target, element, and command.

6.   Otherwise, run the [popover target attribute activation behavior](https://html.spec.whatwg.org/multipage/popover.html#popover-target-attribute-activation-behavior) given element and event's [target](https://dom.spec.whatwg.org/#concept-event-target).

An [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) can have specific is valid command steps and command steps defined for the element's [local name](https://dom.spec.whatwg.org/#concept-element-local-name).

The `form` attribute is used to explicitly associate the `button` element with its [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner). The `name` attribute represents the element's name. The `disabled` attribute is used to make the control non-interactive and to prevent its value from being submitted. The `formaction`, `formenctype`, `formmethod`, `formnovalidate`, and `formtarget` attributes are [attributes for form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attributes-for-form-submission).

The `formnovalidate` attribute can be used to make submit buttons that do not trigger the constraint validation.

The `formaction`, `formenctype`, `formmethod`, `formnovalidate`, and `formtarget` must not be specified if the element is not a [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button).

The `command` getter steps are:

1.   Let command be [this](https://webidl.spec.whatwg.org/#this)'s `command` attribute.

2.   If command is in the [Custom](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-custom-state) state, then return command's value.

3.   If command is in the [Unknown](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-unknown-state) state, then return the empty string.

4.   Return the keyword corresponding to the value of command.

The `value` attribute gives the element's value for the purposes of form submission. The element's [value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-value) is the value of the element's `value` attribute, if there is one; otherwise the empty string. The element's [optional value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-optional-value) is the value of the element's `value` attribute, if there is one; otherwise null.

A button (and its value) is only included in the form submission if the button itself was used to initiate the form submission.

* * *

The `type` getter steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this) is a [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button), then return "`submit`".

2.   Let state be [this](https://webidl.spec.whatwg.org/#this)'s `type` attribute.

3.   [Assert](https://infra.spec.whatwg.org/#assert): state is not in the [Submit Button](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-type-submit-state) state.

4.   If state is in the [Auto](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-type-auto-state) state, then return "`button`".

5.   Return the keyword value corresponding to state.

The `willValidate`, `validity`, and `validationMessage` IDL attributes, and the `checkValidity()`, `reportValidity()`, and `setCustomValidity()` methods, are part of the [constraint validation API](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#the-constraint-validation-api). The `labels` IDL attribute provides a list of the element's `label`s. The `disabled`, `form`, and `name` IDL attributes are part of the element's forms API.

The following button is labeled "Show hint" and pops up a dialog box when activated:

```
<button type=button
        onclick="alert('This 15-20 minute piece was composed by George Gershwin.')">
 Show hint
</button>
```

The following shows how [buttons](https://html.spec.whatwg.org/multipage/forms.html#concept-button) can use `commandfor` to show and hide an element with the `popover` attribute when activated:

```
<button type=button
        commandfor="the-popover"
        command="show-popover">
 Show menu
</button>
<div popover
     id="the-popover">
 <button commandfor="the-popover"
         command="hide-popover">
  Hide menu
 </button>
</div>
```

The following shows how buttons can use `commandfor` with a [custom command keyword](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command-custom) on an element, demonstrating how one could use custom commands for unspecified behavior:

```
<button type=button
        commandfor="the-image"
        command="--rotate-landscape">
 Rotate Left
</button>
<button type=button
        commandfor="the-image"
        command="--rotate-portrait">
 Rotate Right
</button>
<img id="the-image"
     src="photo.jpg">
<script>
  const image = document.getElementById("the-image");
  image.addEventListener("command", (event) => {
   if ( event.command == "--rotate-landscape" ) {
    event.target.style.rotate = "-90deg"
   } else if ( event.command == "--rotate-portrait" ) {
    event.target.style.rotate = "0deg"
   }
  });
</script>
```

#### 4.10.7 The `select` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-select-element)

[Element/select](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select "The <select> HTML element represents a control that provides a menu of options.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 2+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android 4+Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 10.1+

[HTMLSelectElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement "The HTMLSelectElement interface represents a <select> HTML Element. These elements also share all of the properties and methods of other HTML elements via the HTMLElement interface.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 2+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 1+

* * *

Firefox Android 4+Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 10.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2).[Listed](https://html.spec.whatwg.org/multipage/forms.html#category-listed), [labelable](https://html.spec.whatwg.org/multipage/forms.html#category-label), [submittable](https://html.spec.whatwg.org/multipage/forms.html#category-submit), [resettable](https://html.spec.whatwg.org/multipage/forms.html#category-reset), and [autocapitalize-and-autocorrect inheriting](https://html.spec.whatwg.org/multipage/forms.html#category-autocapitalize)[form-associated element](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):Zero or one `button` elements if the `select` is a [drop-down box](https://html.spec.whatwg.org/multipage/rendering.html#drop-down-box), followed by zero or more [`select` element inner content elements](https://html.spec.whatwg.org/multipage/dom.html#select-element-inner-content-elements-2).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`autocomplete` — Hint for form autofill feature `disabled` — Whether the form control is disabled `form` — Associates the element with a `form` element `multiple` — Whether to allow multiple values `name` — Name of the element to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2) and in the `form.elements` API `required` — Whether the control is required for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`size` — Size of the control [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):If the element has a `multiple` attribute or a `size` attribute with a value > 1: [for authors](https://w3c.github.io/html-aria/#el-select-multiple-or-size-greater-1); [for implementers](https://w3c.github.io/html-aam/#el-select-listbox).Otherwise: [for authors](https://w3c.github.io/html-aria/#el-select); [for implementers](https://w3c.github.io/html-aam/#el-select-combobox).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLSelectElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, ReflectSetter] attribute DOMString autocomplete;
  [CEReactions, Reflect] attribute boolean disabled;
  readonly attribute HTMLFormElement? form;
  [CEReactions, Reflect] attribute boolean multiple;
  [CEReactions, Reflect] attribute DOMString name;
  [CEReactions, Reflect] attribute boolean required;
  [CEReactions, Reflect, ReflectDefault=0] attribute unsigned long size;
  

  readonly attribute DOMString type;

  [SameObject] readonly attribute HTMLOptionsCollection options;
  [CEReactions] attribute unsigned long length;
  getter HTMLOptionElement? item(unsigned long index);
  HTMLOptionElement? namedItem(DOMString name);
  [CEReactions] undefined add((HTMLOptionElement or HTMLOptGroupElement) element, optional (HTMLElement or long)? before = null);
  [CEReactions] undefined remove(); // ChildNode overload
  [CEReactions] undefined remove(long index);
  [CEReactions] setter undefined (unsigned long index, HTMLOptionElement? option);

  [SameObject] readonly attribute HTMLCollection selectedOptions;
  attribute long selectedIndex;
  attribute DOMString value;

  readonly attribute boolean willValidate;
  readonly attribute ValidityState validity;
  readonly attribute DOMString validationMessage;
  boolean checkValidity();
  boolean reportValidity();
  undefined setCustomValidity(DOMString error);

  undefined showPicker();

  readonly attribute NodeList labels;
};
```

The `select` element represents a control for selecting amongst a set of options.

[Attributes/multiple](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/multiple "The Boolean multiple attribute, if set, means the form control accepts one or more values. Valid for the email and file input types and the <select>, the manner by which the user opts for multiple values depends on the form control.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `multiple` attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute). If the attribute is present, then the `select` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a control for selecting zero or more options from the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list). If the attribute is absent, then the `select` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a control for selecting a single option from the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list).

[Attributes/size](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/size "The size attribute defines the width of the <input> and the height of the <select> element. For the input, if the type attribute is text or password then it's the number of characters. This must be an integer value of 0 or higher. If no size is specified, or an invalid value is specified, the input has no size declared, and the form control will be the default width based on the user agent. If CSS targets the element with properties impacting the width, CSS takes precedence.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `size` attribute gives the number of options to show to the user. The `size` attribute, if specified, must have a value that is a [valid non-negative integer](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-non-negative-integer) greater than zero.

[Attributes/required](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/required "The Boolean required attribute, if present, indicates that the user must specify a value for the input before the owning form can be submitted.")

Support in all current engines.

Firefox 4+Safari 5.1+Chrome 10+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `required` attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute). When specified, the user will be required to select a value before submitting the form.

The `form` attribute is used to explicitly associate the `select` element with its [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner). The `name` attribute represents the element's name. The `disabled` attribute is used to make the control non-interactive and to prevent its value from being submitted. The `autocomplete` attribute controls how the user agent provides autofill behavior.

If a `select` element has a `required` attribute specified, and has a [display size](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-size) of 1; and if the [value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-value) of the first `option` element in the `select` element's [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) (if any) is the empty string, and that `option` element's parent node is the `select` element (and not an `optgroup` element), then that `option` is the `select` element's placeholder label option.

If a `select` element has a `required` attribute specified, does not have a `multiple` attribute specified, and has a [display size](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-size) of 1, then the `select` element must have a [placeholder label option](https://html.spec.whatwg.org/multipage/form-elements.html#placeholder-label-option).

In practice, the requirement stated in the paragraph above can only apply when a `select` element does not have a `size` attribute with a value greater than 1.

* * *

**Constraint validation**: If the element has its `required` attribute specified, and either none of the `option` elements in the `select` element's [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) have their [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true, or the only `option` element in the `select` element's [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) with its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true is the [placeholder label option](https://html.spec.whatwg.org/multipage/form-elements.html#placeholder-label-option), then the element is [suffering from being missing](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#suffering-from-being-missing).

The [reset algorithm](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-reset-control) for a `select` element selectElement is:

1.   Set selectElement's [user validity](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#user-validity) to false.

2.   [For each](https://infra.spec.whatwg.org/#list-iterate)optionElement of selectElement's [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list):

    1.   If optionElement has a `selected` attribute, then set optionElement's [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) to true; otherwise set it to false.

    2.   Set optionElement's [dirtiness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-dirtiness) to false.

3.   Run the [selectedness setting algorithm](https://html.spec.whatwg.org/multipage/form-elements.html#selectedness-setting-algorithm) given selectElement.

* * *

The user agent should allow the user to pick an `option` element from a `select` element in its [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) (either through a click, or through unfocusing the element after changing its value, or through a [menu command](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-option-element-to-define-a-command), or through any other mechanism) by running the [pick an option](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-pick) algorithm given the `select` element, the `option` element, and if the [`select`'s `option`s are being rendered with base appearance](https://html.spec.whatwg.org/multipage/rendering.html#select's-options-are-being-rendered-with-base-appearance), a corresponding `keydown` or `mouseup` event, otherwise null.

If the `multiple` attribute is absent, whenever an `option` element in the `select` element's [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) has its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true, and whenever an `option` element with its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true is added to the `select` element's [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list), the user agent must set the [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) of all the other `option` elements in its [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) to false.

If the `multiple` attribute is absent and the element's [display size](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-size) is greater than 1, then the user agent should also allow the user to request that the `option` whose [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) is true, if any, be unselected. Upon this request being conveyed to the user agent, and before the relevant user interaction event is queued (e.g. before the `click` event), the user agent must set the [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) of that `option` element to false, set its [dirtiness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-dirtiness) to true, and then [send `select` update notifications](https://html.spec.whatwg.org/multipage/form-elements.html#send-select-update-notifications).

If the `select` is being rendered with [base appearance](https://drafts.csswg.org/css-ui/#base-appearance), then the user agent should allow the user to focus another option given the new `option` element to focus option and a `keydown` event event:

1.   If event's [canceled flag](https://dom.spec.whatwg.org/#canceled-flag) is set, then return.

2.   Run the [focusing steps](https://html.spec.whatwg.org/multipage/interaction.html#focusing-steps) on option.

Implementations commonly allow the user to focus the next or previous option via the arrow-up and arrow-down keys, focus the first or last option via the Home or End keys, or focus the first or last option in the viewport of the picker via the PageUp or PageDown keys.

Which particular keys of the keyboard cause these actions might differ across implementations and platforms. The ARIA Authoring Practices Guide has good [recommendations](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-select-only/) for this behavior.

If the `multiple` attribute is present, and the element is not [disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-disabled), then the user agent should allow the user to toggle the [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) of the `option` elements in its [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) that are themselves not [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-disabled). Upon such an element being [toggled](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-toggle) (either through a click, or through a [menu command](https://html.spec.whatwg.org/multipage/interactive-elements.html#using-the-option-element-to-define-a-command), or any other mechanism), and before the relevant user interaction event is queued (e.g. before a related `click` event), the [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) of the `option` element must be changed (from true to false or false to true), the [dirtiness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-dirtiness) of the element must be set to true, and the user agent must [send `select` update notifications](https://html.spec.whatwg.org/multipage/form-elements.html#send-select-update-notifications).

* * *

The display size of a `select` element is the result of applying the [rules for parsing non-negative integers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-non-negative-integers) to the value of the element's `size` attribute, if it has one and parsing it is successful. If applying those rules to the attribute's value is not successful, or if the `size` attribute is absent, then the element's [display size](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-size) is 4 if the element's `multiple` content attribute is present, and 1 otherwise.

To get the list of options given a `select` element select:

1.   Let options be « ».

2.   Let node be the [first child](https://dom.spec.whatwg.org/#concept-tree-first-child) of select in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

3.   [While](https://infra.spec.whatwg.org/#iteration-while)node is not null:

    1.   If node is an `option` element, then [append](https://infra.spec.whatwg.org/#list-append)node to options.

    2.   If any of the following conditions are true:

        *   node is a `select` element;

        *   node is an `hr` element;

        *   node is an `option` element;

        *   node is a `datalist` element;

        *   node is an `optgroup` element and node has an [ancestor](https://dom.spec.whatwg.org/#concept-tree-ancestor)`optgroup` in between itself and select,

then set node to the next [descendant](https://dom.spec.whatwg.org/#concept-tree-descendant) of select in [tree order](https://dom.spec.whatwg.org/#concept-tree-order), excluding node's [descendants](https://dom.spec.whatwg.org/#concept-tree-descendant), if any such node exists; otherwise null.

Otherwise, set node to the next [descendant](https://dom.spec.whatwg.org/#concept-tree-descendant) of select in [tree order](https://dom.spec.whatwg.org/#concept-tree-order), if any such node exists; otherwise null.

4.   Return options.

If an `option` element in the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list)asks for a reset, then run that `select` element's [selectedness setting algorithm](https://html.spec.whatwg.org/multipage/form-elements.html#selectedness-setting-algorithm).

The selectedness setting algorithm, given a `select` element element, is to run the following steps:

1.   If element's `multiple` attribute is absent, and element's [display size](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-size) is 1, and no `option` elements in the element's [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) have their [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true, then set the [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) of the first `option` element in the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) that is not [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-disabled), if any, to true, and return.

2.   If element's `multiple` attribute is absent, and two or more `option` elements in element's [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) have their [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true, then set the [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) of all but the last `option` element with its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true in the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) to false.

* * *

`select.type`

[HTMLSelectElement/type](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/type "The HTMLSelectElement.type read-only property returns the form control's type.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 2+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 1+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Returns "`select-multiple`" if the element has a `multiple` attribute, and "`select-one`" otherwise.

`select.options`

[HTMLSelectElement/options](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/options "The HTMLSelectElement.options read-only property returns a HTMLOptionsCollection of the <option> elements contained by the <select> element.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Returns an `HTMLOptionsCollection` of the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list).

`select.length [ = value ]`
Returns the number of elements in the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list).

When set to a smaller number, truncates the number of `option` elements in the `select`.

When set to a greater number, adds new blank `option` elements to the `select`.

`element = select.item(index)`

[HTMLSelectElement/item](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/item "The HTMLSelectElement.item() method returns the Element corresponding to the HTMLOptionElement whose position in the options list corresponds to the index given in the parameter, or null if there are none.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

`select[index]`
Returns the item with index index from the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list). The items are sorted in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

`element = select.namedItem(name)`

[HTMLSelectElement/namedItem](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/namedItem "The HTMLSelectElement.namedItem() method returns the HTMLOptionElement corresponding to the HTMLOptionElement whose name or id match the specified name, or null if no option matches.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 6+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Returns the first item with [ID](https://dom.spec.whatwg.org/#concept-id) or `name`name from the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list).

Returns null if no element with that [ID](https://dom.spec.whatwg.org/#concept-id) could be found.

`select.add(element [, before ])`

[HTMLSelectElement/add](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/add "The HTMLSelectElement.add() method adds an element to the collection of option elements for this select element.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Inserts element before the node given by before.

The before argument can be a number, in which case element is inserted before the item with that number, or an element from the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list), in which case element is inserted before that element.

If before is omitted, null, or a number out of range, then element will be added at the end of the list.

This method will throw a ["`HierarchyRequestError`"](https://webidl.spec.whatwg.org/#hierarchyrequesterror)`DOMException` if element is an ancestor of the element into which it is to be inserted.

`select.selectedOptions`

[HTMLSelectElement/selectedOptions](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/selectedOptions "The read-only HTMLSelectElement property selectedOptions contains a list of the <option> elements contained within the <select> element that are currently selected. The list of selected options is an HTMLCollection object with one entry per currently selected option.")

Support in all current engines.

Firefox 26+Safari 6+Chrome 19+

* * *

Opera 9+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Returns an `HTMLCollection` of the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) that are selected.

`select.selectedIndex [ = value ]`

[HTMLSelectElement/selectedIndex](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/selectedIndex "The HTMLSelectElement.selectedIndex property is a long that reflects the index of the first or last selected <option> element, depending on the value of multiple. The value -1 indicates that no element is selected.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Returns the index of the first selected item, if any, or −1 if there is no selected item.

Can be set, to change the selection.

`select.value [ = value ]`
Returns the [value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-value) of the first selected item, if any, or the empty string if there is no selected item.

Can be set, to change the selection.

`select.showPicker()`
Shows any applicable picker UI for select, so that the user can select a value.

Throws an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if select is not [mutable](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-mutable).

Throws a ["`NotAllowedError`"](https://webidl.spec.whatwg.org/#notallowederror)`DOMException` if called without [transient user activation](https://html.spec.whatwg.org/multipage/interaction.html#transient-activation).

Throws a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException` if select is inside a cross-origin `iframe`.

Throws a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException` if select is not [being rendered](https://html.spec.whatwg.org/multipage/rendering.html#being-rendered).

The `type` IDL attribute, on getting, must return the string "`select-one`" if the `multiple` attribute is absent, and the string "`select-multiple`" if the `multiple` attribute is present.

The `options` IDL attribute must return an `HTMLOptionsCollection` rooted at the `select` node, whose filter matches the elements in the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list).

The `options` collection is also mirrored on the `HTMLSelectElement` object. The [supported property indices](https://webidl.spec.whatwg.org/#dfn-supported-property-indices) at any instant are the indices supported by the object returned by the `options` attribute at that instant.

The `length` IDL attribute must return the number of nodes [represented](https://dom.spec.whatwg.org/#represented-by-the-collection) by the `options` collection. On setting, it must act like the attribute of the same name on the `options` collection.

The `item(index)` method must return the value returned by [the method of the same name](https://dom.spec.whatwg.org/#dom-htmlcollection-item) on the `options` collection, when invoked with the same argument.

The `namedItem(name)` method must return the value returned by [the method of the same name](https://dom.spec.whatwg.org/#dom-htmlcollection-nameditem) on the `options` collection, when invoked with the same argument.

Similarly, the `add(element, before)` method must act like its namesake method on that same `options` collection.

[HTMLSelectElement/remove](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/remove "The HTMLSelectElement.remove() method removes the element at the specified index from the options collection for this select element.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

The `remove()` method must act like its namesake method on that same `options` collection when it has arguments, and like its namesake method on the `ChildNode` interface implemented by the `HTMLSelectElement` ancestor interface `Element` when it has no arguments.

The `selectedOptions` IDL attribute must return an `HTMLCollection` rooted at the `select` node, whose filter matches the elements in the [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) that have their [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true.

The `selectedIndex` getter steps are to return the [index](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-index) of the first `option` element in [this](https://webidl.spec.whatwg.org/#this)'s [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) that has its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true, if any. If there isn't one, then return −1.

The `selectedIndex` setter steps are:

1.   Let firstMatchingOption be null.

2.   For each option of [this](https://webidl.spec.whatwg.org/#this)'s [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list):

    1.   Set option's [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) to false.

    2.   If firstMatchingOption is null and option's [index](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-index) is equal to the given value, then set firstMatchingOption to option.

3.   If firstMatchingOption is not null, then set firstMatchingOption's [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) to true and set firstMatchingOption's [dirtiness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-dirtiness) to true.

4.   Run [update a `select`'s `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#update-a-select's-selectedcontent) given [this](https://webidl.spec.whatwg.org/#this).

This can result in no element having a [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true even in the case of the `select` element having no `multiple` attribute and a [display size](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-size) of 1.

The `value` getter steps are to return the [value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-value) of the first `option` element in [this](https://webidl.spec.whatwg.org/#this)'s [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) that has its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true, if any. If there isn't one, then return the empty string.

The `value` setter steps are:

1.   Let firstMatchingOption be null.

2.   For each option of [this](https://webidl.spec.whatwg.org/#this)'s [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list):

    1.   Set option's [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) to false.

    2.   If firstMatchingOption is null and option's [value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-value) is equal to the given value, then set firstMatchingOption to option.

3.   If firstMatchingOption is not null, then set firstMatchingOption's [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) to true and set firstMatchingOption's [dirtiness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-dirtiness) to true.

4.   Run [update a `select`'s `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#update-a-select's-selectedcontent) given [this](https://webidl.spec.whatwg.org/#this).

This can result in no element having a [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) set to true even in the case of the `select` element having no `multiple` attribute and a [display size](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-size) of 1.

For historical reasons, the default value of the `size` IDL attribute does not return the actual size used, which, in the absence of the `size` content attribute, is either 1 or 4 depending on the presence of the `multiple` attribute.

The `willValidate`, `validity`, and `validationMessage` IDL attributes, and the `checkValidity()`, `reportValidity()`, and `setCustomValidity()` methods, are part of the [constraint validation API](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#the-constraint-validation-api). The `labels` IDL attribute provides a list of the element's `label`s. The `disabled`, `form`, and `name` IDL attributes are part of the element's forms API.

* * *

The following example shows how a `select` element can be used to offer the user with a set of options from which the user can select a single option. The default option is preselected.

```
<p>
 <label for="unittype">Select unit type:</label>
 <select id="unittype" name="unittype">
  <option value="1"> Miner </option>
  <option value="2"> Puffer </option>
  <option value="3" selected> Snipey </option>
  <option value="4"> Max </option>
  <option value="5"> Firebot </option>
 </select>
</p>
```

When there is no default option, a placeholder can be used instead:

```
<select name="unittype" required>
 <option value=""> Select unit type </option>
 <option value="1"> Miner </option>
 <option value="2"> Puffer </option>
 <option value="3"> Snipey </option>
 <option value="4"> Max </option>
 <option value="5"> Firebot </option>
</select>
```

Here, the user is offered a set of options from which they can select any number. By default, all five options are selected.

```
<p>
 <label for="allowedunits">Select unit types to enable on this map:</label>
 <select id="allowedunits" name="allowedunits" multiple>
  <option value="1" selected> Miner </option>
  <option value="2" selected> Puffer </option>
  <option value="3" selected> Snipey </option>
  <option value="4" selected> Max </option>
  <option value="5" selected> Firebot </option>
 </select>
</p>
```

Sometimes, a user has to select one or more items. This example shows such an interface.

```
<label>
 Select the songs from that you would like on your Act II Mix Tape:
 <select multiple required name="act2">
  <option value="s1">It Sucks to Be Me (Reprise)
  <option value="s2">There is Life Outside Your Apartment
  <option value="s3">The More You Ruv Someone
  <option value="s4">Schadenfreude
  <option value="s5">I Wish I Could Go Back to College
  <option value="s6">The Money Song
  <option value="s7">School for Monsters
  <option value="s8">The Money Song (Reprise)
  <option value="s9">There's a Fine, Fine Line (Reprise)
  <option value="s10">What Do You Do With a B.A. in English? (Reprise)
  <option value="s11">For Now
 </select>
</label>
```

Occasionally it can be useful to have a separator:

```
<label>
 Select the song to play next:
 <select required name="next">
  <option value="sr">Random
  <hr>
  <option value="s1">It Sucks to Be Me (Reprise)
  <option value="s2">There is Life Outside Your Apartment
  …
```

Here is an example which uses `div`, `legend`, `img`, `button`, and `selectedcontent` elements:

```
<select>
  <button>
    <selectedcontent></selectedcontent>
  </button>
  <div class="border">
    <optgroup>
      <legend>WHATWG Specifications</legend>
      <option>
        <img src="html.jpg" alt="">
        HTML
      </option>
      <option>
        <img src="dom.jpg" alt="">
        DOM
      </option>
    </optgroup>
  </div>
  <div class="border">
    <optgroup>
      <legend>W3C Specifications</legend>
      <option>
        <img src="forms.jpg" alt="">
        CSS Form Control Styling
      </option>
      <option>
        <img src="pseudo.jpg" alt="">
        CSS Pseudo-Elements
      </option>
    <optgroup>
  </div>
</select>
```

[](https://html.spec.whatwg.org/multipage/form-elements.html#note-first-button-in-select-not-submit)The first child `button` element as allowed by the content model of `select` is not a submit button. It is used to replace the in-page rendering of the `select` element. Its form submission behavior is prevented because it is [inert](https://html.spec.whatwg.org/multipage/interaction.html#inert).

#### 4.10.8 The `datalist` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-datalist-element)

[Element/datalist](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist "The <datalist> HTML element contains a set of <option> elements that represent the permissible or recommended options available to choose from within other controls.")

Firefox🔰 4+Safari 12.1+Chrome 20+

* * *

Opera 9.5+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android🔰 79+Safari iOS?Chrome Android 33+WebView Android?Samsung Internet?Opera Android?

[HTMLDataListElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDataListElement "The HTMLDataListElement interface provides special properties (beyond the HTMLElement object interface it also has available to it by inheritance) to manipulate <datalist> elements and their content.")

Support in all current engines.

Firefox 4+Safari 12.1+Chrome 20+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 4.4.3+Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):Either: [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).Or: Zero or more `option` and [script-supporting](https://html.spec.whatwg.org/multipage/dom.html#script-supporting-elements-2) elements.[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-datalist).[For implementers](https://w3c.github.io/html-aam/#el-datalist).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLDataListElement : HTMLElement {
  [HTMLConstructor] constructor();

  [SameObject] readonly attribute HTMLCollection options;
};
```

The `datalist` element represents a set of `option` elements that represent predefined options for other controls. In the rendering, the `datalist` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) nothing and it, along with its children, should be hidden.

The `datalist` element can be used in two ways. In the simplest case, the `datalist` element has just `option` element children.

```
<label>
 Animal:
 <input name=animal list=animals>
 <datalist id=animals>
  <option value="Cat">
  <option value="Dog">
 </datalist>
</label>
```

In the more elaborate case, the `datalist` element can be given contents that are to be displayed for down-level clients that don't support `datalist`. In this case, the `option` elements are provided inside a `select` element inside the `datalist` element.

```
<label>
 Animal:
 <input name=animal list=animals>
</label>
<datalist id=animals>
 <label>
  or select from the list:
  <select name=animal>
   <option value="">
   <option>Cat
   <option>Dog
  </select>
 </label>
</datalist>
```

The `datalist` element is hooked up to an `input` element using the `list` attribute on the `input` element.

Each `option` element that is a descendant of the `datalist` element, that is not [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-disabled), and whose [value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-value) is a string that isn't the empty string, represents a suggestion. Each suggestion has a [value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-value) and a [label](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-label).

`datalist.options`
Returns an `HTMLCollection` of the `option` elements of the `datalist` element.

The `options` IDL attribute must return an `HTMLCollection` rooted at the `datalist` node, whose filter matches `option` elements.

#### 4.10.9 The `optgroup` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-optgroup-element)

[Element/optgroup](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup "The <optgroup> HTML element creates a grouping of options within a <select> element.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLOptGroupElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOptGroupElement "The HTMLOptGroupElement interface provides special properties and methods (beyond the regular HTMLElement object interface they also have available to them by inheritance) for manipulating the layout and presentation of <optgroup> elements.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[`select` element inner content elements](https://html.spec.whatwg.org/multipage/dom.html#select-element-inner-content-elements-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):As a descendant of a `select` element.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):Zero or one `legend` element followed by zero or more [`optgroup` element inner content elements](https://html.spec.whatwg.org/multipage/dom.html#optgroup-element-inner-content-elements-2).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):An `optgroup` element's [end tag](https://html.spec.whatwg.org/multipage/syntax.html#syntax-end-tag) can be omitted if the `optgroup` element is immediately followed by another `optgroup` element, if it is immediately followed by an `hr` element, or if there is no more content in the parent element.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`disabled` — Whether the form control is disabled `label` — User-visible label [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-optgroup).[For implementers](https://w3c.github.io/html-aam/#el-optgroup).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLOptGroupElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute boolean disabled;
  [CEReactions, Reflect] attribute DOMString label;
};
```

The `optgroup` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a [group of `option` elements](https://html.spec.whatwg.org/multipage/form-elements.html#optgroup-option-group) with a common label.

The element's group of `option` elements consists of the `option` elements that are descendants of the `optgroup` element.

When showing `option` elements in `select` elements, user agents should show the `option` elements of such groups as being related to each other and separate from other `option` elements.

[Attributes/disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/disabled "The Boolean disabled attribute, when present, makes the element not mutable, focusable, or even submitted with the form. The user can neither edit nor focus on the control, nor its form control descendants.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `disabled` attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute) and can be used to [disable](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-disabled) a [group of `option` elements](https://html.spec.whatwg.org/multipage/form-elements.html#optgroup-option-group) together.

The `label` attribute must be specified if the `optgroup` has no child `legend` element.

To get an `optgroup` element's label, given an `optgroup`optgroup:

1.   If optgroup has a child `legend` element, then return the result of [stripping and collapsing ASCII whitespace](https://infra.spec.whatwg.org/#strip-and-collapse-ascii-whitespace) from the concatenation of [data](https://dom.spec.whatwg.org/#concept-cd-data) of all the `Text` node descendants of optgroup's first child `legend` element, in [tree order](https://dom.spec.whatwg.org/#concept-tree-order), excluding any that are descendants of descendants of the `legend` that are themselves `script` or [SVG `script`](https://svgwg.org/svg2-draft/interact.html#ScriptElement) elements.

2.   Otherwise, return the value of optgroup's `label` attribute.

The value of the [`optgroup` label algorithm](https://html.spec.whatwg.org/multipage/form-elements.html#concept-optgroup-label) gives the name of the group, for the purposes of the user interface. User agents should use this attribute's value when labeling the group of `option` elements in a `select` element.

There is no way to select an `optgroup` element. Only `option` elements can be selected. An `optgroup` element merely provides a label for a group of `option` elements.

The following snippet shows how a set of lessons from three courses could be offered in a `select` drop-down widget:

```
<form action="courseselector.dll" method="get">
 <p>Which course would you like to watch today?
 <p><label>Course:
  <select name="c">
   <optgroup label="8.01 Physics I: Classical Mechanics">
    <option value="8.01.1">Lecture 01: Powers of Ten
    <option value="8.01.2">Lecture 02: 1D Kinematics
    <option value="8.01.3">Lecture 03: Vectors
   <optgroup label="8.02 Electricity and Magnetism">
    <option value="8.02.1">Lecture 01: What holds our world together?
    <option value="8.02.2">Lecture 02: Electric Field
    <option value="8.02.3">Lecture 03: Electric Flux
   <optgroup label="8.03 Physics III: Vibrations and Waves">
    <option value="8.03.1">Lecture 01: Periodic Phenomenon
    <option value="8.03.2">Lecture 02: Beats
    <option value="8.03.3">Lecture 03: Forced Oscillations with Damping
  </select>
 </label>
 <p><input type=submit value="▶ Play">
</form>
```

#### 4.10.10 The `option` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-option-element)

[Element/option](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option "The <option> HTML element is used to define an item contained in a <select>, an <optgroup>, or a <datalist> element. As such, <option> can represent menu items in popups and other lists of items in an HTML document.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLOptionElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOptionElement "The HTMLOptionElement interface represents <option> elements and inherits all properties and methods of the HTMLElement interface.")

Support in all current engines.

Firefox 1+Safari 1.2+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[`select` element inner content elements](https://html.spec.whatwg.org/multipage/dom.html#select-element-inner-content-elements-2).[`optgroup` element inner content elements](https://html.spec.whatwg.org/multipage/dom.html#optgroup-element-inner-content-elements-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):As a descendant of a `select` element.As a descendant of a `datalist` element.As a descendant of an `optgroup` element.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):If the element has a `label` attribute and a `value` attribute: [Nothing](https://html.spec.whatwg.org/multipage/dom.html#concept-content-nothing).If the element has a `label` attribute but no `value` attribute: [Text](https://html.spec.whatwg.org/multipage/dom.html#text-content).If the element has no `label` attribute and is not a descendant of a `datalist` element: Zero or more [`option` element inner content elements](https://html.spec.whatwg.org/multipage/dom.html#option-element-inner-content-elements-2).If the element has no `label` attribute and is a descendant of a `datalist` element: [Text](https://html.spec.whatwg.org/multipage/dom.html#text-content).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):An `option` element's [end tag](https://html.spec.whatwg.org/multipage/syntax.html#syntax-end-tag) can be omitted if the `option` element is immediately followed by another `option` element, if it is immediately followed by an `optgroup` element, if it is immediately followed by an `hr` element, or if there is no more content in the parent element.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`disabled` — Whether the form control is disabled `label` — User-visible label `selected` — Whether the option is selected by default `value` — Value to be used for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-option).[For implementers](https://w3c.github.io/html-aam/#el-option).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window,
 LegacyFactoryFunction=Option(optional DOMString text = "", optional DOMString value, optional boolean defaultSelected = false, optional boolean selected = false)]
interface HTMLOptionElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute boolean disabled;
  readonly attribute HTMLFormElement? form;
  [CEReactions, ReflectSetter] attribute DOMString label;
  [CEReactions, Reflect="selected"] attribute boolean defaultSelected;
  attribute boolean selected;
  [CEReactions, ReflectSetter] attribute DOMString value;

  [CEReactions] attribute DOMString text;
  readonly attribute long index;
};
```

The `option` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) an option in a `select` element or as part of a list of suggestions in a `datalist` element.

In certain circumstances described in the definition of the `select` element, an `option` element can be a `select` element's [placeholder label option](https://html.spec.whatwg.org/multipage/form-elements.html#placeholder-label-option). A [placeholder label option](https://html.spec.whatwg.org/multipage/form-elements.html#placeholder-label-option) does not represent an actual option, but instead represents a label for the `select` control.

[Attributes/disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/disabled "The Boolean disabled attribute, when present, makes the element not mutable, focusable, or even submitted with the form. The user can neither edit nor focus on the control, nor its form control descendants.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `disabled` attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute). An `option` element option is disabled if the following steps return true:

1.   If option's `disabled` attribute is present, then return true.

2.   For each ancestor of option's [ancestors](https://dom.spec.whatwg.org/#concept-tree-ancestor) in reverse [tree order](https://dom.spec.whatwg.org/#concept-tree-order):

    1.   If ancestor is a `select`, `hr`, `datalist`, or `option` element, then return false.

    2.   If ancestor is an `optgroup` element, then return true if ancestor's `disabled` attribute is present; otherwise false.

3.   Return false.

An `option` element that is [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#attr-option-disabled) must prevent any `click` events that are [queued](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-task) on the [user interaction task source](https://html.spec.whatwg.org/multipage/webappapis.html#user-interaction-task-source) from being dispatched on the element.

Being [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-disabled) does not prevent all modifications to the `option` element. For example, its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) could be modified programmatically from JavaScript. Or, it could be indirectly modified by user action, e.g., if other non-disabled `option` elements in the `select` element were modified.

The `label` attribute provides a label for element. The label of an `option` element is the value of the `label` content attribute, if there is one and its value is not the empty string, or, otherwise, the value of the element's `text` IDL attribute.

The `label` content attribute, if specified, must not be empty.

The `value` attribute provides a value for element. The value of an `option` element is the value of the `value` content attribute, if there is one, or, if there is not, the result of [collect option text](https://html.spec.whatwg.org/multipage/form-elements.html#collect-option-text) given [this](https://webidl.spec.whatwg.org/#this) and false.

The `selected` attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute). It represents the default [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) of the element.

The dirtiness of an `option` element is a boolean state, initially false. It controls whether adding or removing the `selected` content attribute has any effect.

The selectedness of an `option` element is a boolean state, initially false. Except where otherwise specified, when the element is created, its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) must be set to true if the element has a `selected` attribute. Whenever an `option` element's `selected` attribute is added, if its [dirtiness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-dirtiness) is false, its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) must be set to true. Whenever an `option` element's `selected` attribute is _removed_, if its [dirtiness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-dirtiness) is false, its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) must be set to false.

The `Option()` constructor, when called with three or fewer arguments, overrides the initial state of the [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) state to always be false even if the third argument is true (implying that a `selected` attribute is to be set). The fourth argument can be used to explicitly set the initial [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) state when using the constructor.

A `select` element whose `multiple` attribute is not specified must not have more than one descendant `option` element with its `selected` attribute set.

An `option` element's index is the number of `option` elements that are in the same [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) but that come before it in [tree order](https://dom.spec.whatwg.org/#concept-tree-order). If the `option` element is not in a [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list), then the `option` element's [index](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-index) is zero.

Each `option` element has a cached nearest ancestor `select` element, which is a `select` element or null, initially set to null.

To update an `option`'s nearest ancestor `select`, given an `option`option:

1.   Let oldSelect be option's [cached nearest ancestor `select` element](https://html.spec.whatwg.org/multipage/form-elements.html#cached-nearest-ancestor-select-element).

2.   Let newSelect be option's [`option` element nearest ancestor `select`](https://html.spec.whatwg.org/multipage/form-elements.html#option-element-nearest-ancestor-select).

3.   If oldSelect is not newSelect:

    1.   If oldSelect is not null, then run the [selectedness setting algorithm](https://html.spec.whatwg.org/multipage/form-elements.html#selectedness-setting-algorithm) given oldSelect.

    2.   If newSelect is not null, then run the [selectedness setting algorithm](https://html.spec.whatwg.org/multipage/form-elements.html#selectedness-setting-algorithm) given newSelect.

4.   Set option's [cached nearest ancestor `select` element](https://html.spec.whatwg.org/multipage/form-elements.html#cached-nearest-ancestor-select-element) to newSelect.

To get the `option` element nearest ancestor `select` given an `option`option, run these steps. They return a `select` or null.

1.   Let ancestorOptgroup be null.

2.   For each ancestor of option's [ancestors](https://dom.spec.whatwg.org/#concept-tree-ancestor), in reverse [tree order](https://dom.spec.whatwg.org/#concept-tree-order):

    1.   If ancestor is a `datalist`, `hr`, or `option` element, then return null.

    2.   If ancestor is an `optgroup` element:

        1.   If ancestorOptgroup is not null, then return null.

        2.   Set ancestorOptgroup to ancestor.

    3.   If ancestor is a `select`, then return ancestor.

3.   Return null.

To maybe clone an `option` into `selectedcontent`, given an `option`option:

1.   Let select be option's [`option` element nearest ancestor `select`](https://html.spec.whatwg.org/multipage/form-elements.html#option-element-nearest-ancestor-select).

2.   If all of the following conditions are true:

    *   select is not null;

    *   option's [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) is true; and

    *   select's [enabled `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#select-enabled-selectedcontent) is not null,

then run [clone an `option` into a `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#clone-an-option-into-a-selectedcontent) given option and select's [enabled `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#select-enabled-selectedcontent).

To clone selected `option` into `select` button, given a `select` element select:

1.   Let option be the first element of select's [option list](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) whose [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) is set to true, if such an element exists; otherwise null.

2.   Let text be the empty string.

3.   If option is not null, then set text to option's [label](https://html.spec.whatwg.org/multipage/form-elements.html#dom-option-label).

4.   Set select's [select fallback button text](https://html.spec.whatwg.org/multipage/rendering.html#select-fallback-button-text) to text.

`option.selected`
Returns true if the element is selected, and false otherwise.

Can be set, to override the current state of the element.

`option.index`
Returns the index of the element in its `select` element's `options` list.

`option.form`
Returns the element's `form` element, if any, or null otherwise.

`option.text`
Same as `textContent`, except that spaces are collapsed and `script` elements are skipped.

`option = new Option([ text [, value [, defaultSelected [, selected ] ] ] ])`

[HTMLOptionElement/Option](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOptionElement/Option "The Option() constructor creates a new HTMLOptionElement.")

Support in all current engines.

Firefox 1+Safari 1.2+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Returns a new `option` element.

The text argument sets the contents of the element.

The value argument sets the `value` attribute.

The defaultSelected argument sets the `selected` attribute.

The selected argument sets whether or not the element is selected. If it is omitted, even if the defaultSelected argument is true, the element is not selected.

The `label` getter steps are:

1.   Let attribute be [this](https://webidl.spec.whatwg.org/#this)'s `label` attribute.

2.   If attribute is null, then return [this](https://webidl.spec.whatwg.org/#this)'s [label](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-label).

3.   Return attribute's [value](https://dom.spec.whatwg.org/#concept-attribute-value).

The `value` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-value).

The `selected` IDL attribute, on getting, must return true if the element's [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) is true, and false otherwise. On setting, it must set the element's [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) to the new value, set its [dirtiness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-dirtiness) to true, and then cause the element to [ask for a reset](https://html.spec.whatwg.org/multipage/form-elements.html#ask-for-a-reset).

The `index` IDL attribute must return the element's [index](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-index).

The `text` getter steps are to return the result of [collect option text](https://html.spec.whatwg.org/multipage/form-elements.html#collect-option-text) given [this](https://webidl.spec.whatwg.org/#this) and false.

The `form` getter steps are:

1.   Let select be [this](https://webidl.spec.whatwg.org/#this)'s [`option` element nearest ancestor `select`](https://html.spec.whatwg.org/multipage/form-elements.html#option-element-nearest-ancestor-select).

2.   If select is null, then return null.

3.   Return select's [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner).

A legacy factory function is provided for creating `HTMLOptionElement` objects (in addition to the factory methods from DOM such as `createElement()`): 
```
Option(text, value,
  defaultSelected, selected)
```
. When invoked, the legacy factory function must perform the following steps:

1.   Let document be the [current global object](https://html.spec.whatwg.org/multipage/webappapis.html#current-global-object)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window).

2.   Let option be the result of [creating an element](https://dom.spec.whatwg.org/#concept-create-element) given document, "`option`", and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace).

3.   If text is not the empty string, then append to option a new `Text` node whose data is text.

4.   If value is given, then [set an attribute value](https://dom.spec.whatwg.org/#concept-element-attributes-set-value) for option using "`value`" and value.

5.   If defaultSelected is true, then [set an attribute value](https://dom.spec.whatwg.org/#concept-element-attributes-set-value) for option using "`selected`" and the empty string.

6.   If selected is true, then set option's [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) to true; otherwise set its [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) to false (even if defaultSelected is true).

7.   Return option.

To collect option text, given an `option` element option and a boolean includeAltText:

1.   Let text be the empty string.

2.   For each [descendant](https://dom.spec.whatwg.org/#concept-tree-descendant)descendant of option in [tree order](https://dom.spec.whatwg.org/#concept-tree-order):

    1.   If descendant is a `script` or [SVG `script`](https://svgwg.org/svg2-draft/interact.html#ScriptElement) element, then [continue](https://infra.spec.whatwg.org/#iteration-continue) skipping all [descendants](https://dom.spec.whatwg.org/#concept-tree-descendant) of descendant.

    2.   If descendant is a `Text` node, then set text to the concatenation of text and descendant's [data](https://dom.spec.whatwg.org/#concept-cd-data).

    3.   If descendant is an `img` element and includeAltText is true, then:

        1.   If the value of descendant's `alt` attribute is not empty, then set text to the concatenation of text, `" "`, the value of descendant's `alt` attribute, and `" "`.

        2.   [Continue](https://infra.spec.whatwg.org/#iteration-continue) skipping all [descendants](https://dom.spec.whatwg.org/#concept-tree-descendant) of descendant.

3.   Return the result of [strip and collapse ASCII whitespace](https://infra.spec.whatwg.org/#strip-and-collapse-ascii-whitespace) given text.

[](https://html.spec.whatwg.org/multipage/form-elements.html#note-option-no-value)When no `value` attribute is set on the `option` element, its text contents are used to generate a submittable value. In the case that the `option` element has child elements, this can lead to unexpected results such as `option` elements which render differently but have the same value. In order to address this, setting the `value` attribute on `option` elements is recommended.

#### 4.10.11 The `textarea` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-textarea-element)

[Element/textarea](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea "The <textarea> HTML element represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example a comment on a review or feedback form.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS 3+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLTextAreaElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTextAreaElement "The HTMLTextAreaElement interface provides special properties and methods for manipulating the layout and presentation of <textarea> elements.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 8+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 10.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2).[Listed](https://html.spec.whatwg.org/multipage/forms.html#category-listed), [labelable](https://html.spec.whatwg.org/multipage/forms.html#category-label), [submittable](https://html.spec.whatwg.org/multipage/forms.html#category-submit), [resettable](https://html.spec.whatwg.org/multipage/forms.html#category-reset), and [autocapitalize-and-autocorrect inheriting](https://html.spec.whatwg.org/multipage/forms.html#category-autocapitalize)[form-associated element](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Text](https://html.spec.whatwg.org/multipage/dom.html#text-content).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`autocomplete` — Hint for form autofill feature `cols` — Maximum number of characters per line `dirname` — Name of form control to use for sending the element's [directionality](https://html.spec.whatwg.org/multipage/dom.html#the-directionality) in [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`disabled` — Whether the form control is disabled `form` — Associates the element with a `form` element `maxlength` — Maximum [length](https://infra.spec.whatwg.org/#string-length) of value `minlength` — Minimum [length](https://infra.spec.whatwg.org/#string-length) of value `name` — Name of the element to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2) and in the `form.elements` API `placeholder` — User-visible label to be placed within the form control `readonly` — Whether to allow the value to be edited by the user `required` — Whether the control is required for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`rows` — Number of lines to show `wrap` — How the value of the form control is to be wrapped for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-textarea).[For implementers](https://w3c.github.io/html-aam/#el-textarea).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLTextAreaElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, ReflectSetter] attribute DOMString autocomplete;
  [CEReactions, ReflectPositiveWithFallback, ReflectDefault=20] attribute unsigned long cols;
  [CEReactions, Reflect] attribute DOMString dirName;
  [CEReactions, Reflect] attribute boolean disabled;
  readonly attribute HTMLFormElement? form;
  [CEReactions, ReflectNonNegative] attribute long maxLength;
  [CEReactions, ReflectNonNegative] attribute long minLength;
  [CEReactions, Reflect] attribute DOMString name;
  [CEReactions, Reflect] attribute DOMString placeholder;
  [CEReactions, Reflect] attribute boolean readOnly;
  [CEReactions, Reflect] attribute boolean required;
  [CEReactions, ReflectPositiveWithFallback, ReflectDefault=2] attribute unsigned long rows;
  [CEReactions, Reflect] attribute DOMString wrap;

  readonly attribute DOMString type;
  [CEReactions] attribute DOMString defaultValue;
  attribute [LegacyNullToEmptyString] DOMString value;
  readonly attribute unsigned long textLength;

  readonly attribute boolean willValidate;
  readonly attribute ValidityState validity;
  readonly attribute DOMString validationMessage;
  boolean checkValidity();
  boolean reportValidity();
  undefined setCustomValidity(DOMString error);

  readonly attribute NodeList labels;

  undefined select();
  attribute unsigned long selectionStart;
  attribute unsigned long selectionEnd;
  attribute DOMString selectionDirection;
  undefined setRangeText(DOMString replacement);
  undefined setRangeText(DOMString replacement, unsigned long start, unsigned long end, optional SelectionMode selectionMode = "preserve");
  undefined setSelectionRange(unsigned long start, unsigned long end, optional DOMString direction);
};
```

The `textarea` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a multiline plain text edit control for the element's raw value. The contents of the control represent the control's default value.

The [raw value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-textarea-raw-value) of a `textarea` control must be initially the empty string.

This element [has rendering requirements involving the bidirectional algorithm](https://html.spec.whatwg.org/multipage/dom.html#bidireq).

The `readonly` attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute) used to control whether the text can be edited by the user or not.

In this example, a text control is marked read-only because it represents a read-only file:

```
Filename: <code>/etc/bash.bashrc</code>
<textarea name="buffer" readonly>
# System-wide .bashrc file for interactive bash(1) shells.

# To enable the settings / commands in this file for login shells as well,
# this file has to be sourced in /etc/profile.

# If not running interactively, don't do anything
[ -z "$PS1" ] &amp;&amp; return

...</textarea>
```

A `textarea` element is [mutable](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-mutable) if it is neither [disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-disabled) nor has a `readonly` attribute specified.

When a `textarea` is [mutable](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-mutable), its [raw value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-textarea-raw-value) should be editable by the user: the user agent should allow the user to edit, insert, and remove text, and to insert and remove line breaks in the form of U+000A LINE FEED (LF) characters. Any time the user causes the element's [raw value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-textarea-raw-value) to change, the user agent must [queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) on the [user interaction task source](https://html.spec.whatwg.org/multipage/webappapis.html#user-interaction-task-source) given the `textarea` element to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `input` at the `textarea` element, with the `bubbles` and `composed` attributes initialized to true. User agents may wait for a suitable break in the user's interaction before queuing the task; for example, a user agent could wait for the user to have not hit a key for 100ms, so as to only fire the event when the user pauses, instead of continuously for each keystroke.

A `textarea` element's [dirty value flag](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-dirty) must be set to true whenever the user interacts with the control in a way that changes the [raw value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-textarea-raw-value).

The [cloning steps](https://dom.spec.whatwg.org/#concept-node-clone-ext) for `textarea` elements given node, copy, and subtree are to propagate the [raw value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-textarea-raw-value) and [dirty value flag](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-dirty) from node to copy.

If the element is [mutable](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-mutable), the user agent should allow the user to change the writing direction of the element, setting it either to a left-to-right writing direction or a right-to-left writing direction. If the user does so, the user agent must then run the following steps:

1.   Set the element's `dir` attribute to "`ltr`" if the user selected a left-to-right writing direction, and "`rtl`" if the user selected a right-to-left writing direction.

2.   [Queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) on the [user interaction task source](https://html.spec.whatwg.org/multipage/webappapis.html#user-interaction-task-source) given the `textarea` element to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `input` at the `textarea` element, with the `bubbles` and `composed` attributes initialized to true.

The `cols` attribute specifies the expected maximum number of characters per line. If the `cols` attribute is specified, its value must be a [valid non-negative integer](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-non-negative-integer) greater than zero. If applying the [rules for parsing non-negative integers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-non-negative-integers) to the attribute's value results in a number greater than zero, then the element's character width is that value; otherwise, it is 20.

The user agent may use the `textarea` element's [character width](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-cols-value) as a hint to the user as to how many characters the server prefers per line (e.g. for visual user agents by making the width of the control be that many characters). In visual renderings, the user agent should wrap the user's input in the rendering so that each line is no wider than this number of characters.

The `rows` attribute specifies the number of lines to show. If the `rows` attribute is specified, its value must be a [valid non-negative integer](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-non-negative-integer) greater than zero. If applying the [rules for parsing non-negative integers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-non-negative-integers) to the attribute's value results in a number greater than zero, then the element's character height is that value; otherwise, it is 2.

Visual user agents should set the height of the control to the number of lines given by [character height](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-rows-value).

The `wrap` attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | State | Brief description |
| --- | --- | --- |
| `soft` | Soft | Text is not to be wrapped when submitted (though can still be wrapped in the rendering). |
| `hard` | Hard | Text is to have newlines added by the user agent so that the text is wrapped when it is submitted. |

If the element's `wrap` attribute is in the [Hard](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-wrap-hard-state) state, the `cols` attribute must be specified.

For historical reasons, the element's value is normalized in three different ways for three different purposes. The [raw value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-textarea-raw-value) is the value as it was originally set. It is not normalized. The [API value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-api-value) is the value used in the `value` IDL attribute, `textLength` IDL attribute, and by the `maxlength` and `minlength` content attributes. It is normalized so that line breaks use U+000A LINE FEED (LF) characters. Finally, there is the [value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-value), as used in form submission and other processing models in this specification. It is normalized as for the [API value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-api-value), and in addition, if necessary given the element's `wrap` attribute, additional line breaks are inserted to wrap the text at the given width.

The element's [value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-value) is defined to be the element's [API value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-textarea-raw-value) with the [textarea wrapping transformation](https://html.spec.whatwg.org/multipage/form-elements.html#textarea-wrapping-transformation) applied. The textarea wrapping transformation is the following algorithm, as applied to a string:

1.   If the element's `wrap` attribute is in the [Hard](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-wrap-hard-state) state, insert U+000A LINE FEED (LF) characters into the string using an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) algorithm so that each line has no more than [character width](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-cols-value) characters. For the purposes of this requirement, lines are delimited by the start of the string, the end of the string, and U+000A LINE FEED (LF) characters.

The `maxlength` attribute is a [form control `maxlength` attribute](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-maxlength).

If the `textarea` element has a [maximum allowed value length](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#maximum-allowed-value-length), then the element's children must be such that the [length](https://infra.spec.whatwg.org/#string-length) of the value of the element's [descendant text content](https://dom.spec.whatwg.org/#concept-descendant-text-content) with [newlines normalized](https://infra.spec.whatwg.org/#normalize-newlines) is less than or equal to the element's [maximum allowed value length](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#maximum-allowed-value-length).

The `minlength` attribute is a [form control `minlength` attribute](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-minlength).

The `required` attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute). When specified, the user will be required to enter a value before submitting the form.

**Constraint validation**: If the element has its `required` attribute specified, and the element is [mutable](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-mutable), and the element's [value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-value) is the empty string, then the element is [suffering from being missing](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#suffering-from-being-missing).

The `placeholder` attribute represents a _short_ hint (a word or short phrase) intended to aid the user with data entry when the control has no value. A hint could be a sample value or a brief description of the expected format.

The `placeholder` attribute should not be used as an alternative to a `label`. For a longer hint or other advisory text, the `title` attribute is more appropriate.

These mechanisms are very similar but subtly different: the hint given by the control's `label` is shown at all times; the short hint given in the `placeholder` attribute is shown before the user enters a value; and the hint in the `title` attribute is shown when the user requests further help.

User agents should present this hint to the user when the element's [value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-value) is the empty string and the control is not [focused](https://html.spec.whatwg.org/multipage/interaction.html#focused) (e.g. by displaying it inside a blank unfocused control). All U+000D CARRIAGE RETURN U+000A LINE FEED character pairs (CRLF) in the hint, as well as all other U+000D CARRIAGE RETURN (CR) and U+000A LINE FEED (LF) characters in the hint, must be treated as line breaks when rendering the hint.

If a user agent normally doesn't show this hint to the user when the control is [focused](https://html.spec.whatwg.org/multipage/interaction.html#focused), then the user agent should nonetheless show the hint for the control if it was focused as a result of the `autofocus` attribute, since in that case the user will not have had an opportunity to examine the control before focusing it.

The `name` attribute represents the element's name. The `dirname` attribute controls how the element's [directionality](https://html.spec.whatwg.org/multipage/dom.html#the-directionality) is submitted. The `disabled` attribute is used to make the control non-interactive and to prevent its value from being submitted. The `form` attribute is used to explicitly associate the `textarea` element with its [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner). The `autocomplete` attribute controls how the user agent provides autofill behavior.

`textarea.type`
Returns the string "`textarea`".

`textarea.value`
Returns the current value of the element.

Can be set, to change the value.

The `type` IDL attribute must return the value "`textarea`".

The `defaultValue` attribute's getter must return the element's [child text content](https://dom.spec.whatwg.org/#concept-child-text-content).

The `defaultValue` attribute's setter must [string replace all](https://dom.spec.whatwg.org/#string-replace-all) with the given value within this element.

The `textLength` IDL attribute must return the [length](https://infra.spec.whatwg.org/#string-length) of the element's [API value](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-api-value).

The `willValidate`, `validity`, and `validationMessage` IDL attributes, and the `checkValidity()`, `reportValidity()`, and `setCustomValidity()` methods, are part of the [constraint validation API](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#the-constraint-validation-api). The `labels` IDL attribute provides a list of the element's `label`s. The `select()`, `selectionStart`, `selectionEnd`, `selectionDirection`, `setRangeText()`, and `setSelectionRange()` methods and IDL attributes expose the element's text selection. The `disabled`, `form`, and `name` IDL attributes are part of the element's forms API.

Here is an example of a `textarea` being used for unrestricted free-form text input in a form:

`<p>If you have any comments, please let us know: <textarea cols=80 name=comments></textarea></p>`
To specify a maximum length for the comments, one can use the `maxlength` attribute:

`<p>If you have any short comments, please let us know: <textarea cols=80 name=comments maxlength=200></textarea></p>`
To give a default value, text can be included inside the element:

`<p>If you have any comments, please let us know: <textarea cols=80 name=comments>You rock!</textarea></p>`
You can also give a minimum length. Here, a letter needs to be filled out by the user; a template (which is shorter than the minimum length) is provided, but is insufficient to submit the form:

```
<textarea required minlength="500">Dear Madam Speaker,

Regarding your letter dated ...

...

Yours Sincerely,

...</textarea>
```

A placeholder can be given as well, to suggest the basic form to the user, without providing an explicit template:

```
<textarea placeholder="Dear Francine,

They closed the parks this week, so we won't be able to
meet your there. Should we just have dinner?

Love,
Daddy"></textarea>
```

To have the browser submit [the directionality](https://html.spec.whatwg.org/multipage/dom.html#the-directionality) of the element along with the value, the `dirname` attribute can be specified:

```
<p>If you have any comments, please let us know (you may use either English or Hebrew for your comments):
<textarea cols=80 name=comments dirname=comments.dir></textarea></p>
```

#### 4.10.12 The `output` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-output-element)

[Element/output](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output "The <output> HTML element is a container element into which a site or app can inject the results of a calculation or the outcome of a user action.")

Support in all current engines.

Firefox 4+Safari 7+Chrome 10+

* * *

Opera 11+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

[HTMLOutputElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOutputElement "The HTMLOutputElement interface provides properties and methods (beyond those inherited from HTMLElement) for manipulating the layout and presentation of <output> elements.")

Support in all current engines.

Firefox 4+Safari 5.1+Chrome 9+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)14+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 3+Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Listed](https://html.spec.whatwg.org/multipage/forms.html#category-listed), [labelable](https://html.spec.whatwg.org/multipage/forms.html#category-label), [resettable](https://html.spec.whatwg.org/multipage/forms.html#category-reset), and [autocapitalize-and-autocorrect inheriting](https://html.spec.whatwg.org/multipage/forms.html#category-autocapitalize)[form-associated element](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`for` — Specifies controls from which the output was calculated `form` — Associates the element with a `form` element `name` — Name of the element to use in the `form.elements` API.[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-output).[For implementers](https://w3c.github.io/html-aam/#el-output).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLOutputElement : HTMLElement {
  [HTMLConstructor] constructor();

  [SameObject, PutForwards=value, Reflect="for"] readonly attribute DOMTokenList htmlFor;
  readonly attribute HTMLFormElement? form;
  [CEReactions, Reflect] attribute DOMString name;

  readonly attribute DOMString type;
  [CEReactions] attribute DOMString defaultValue;
  [CEReactions] attribute DOMString value;

  readonly attribute boolean willValidate;
  readonly attribute ValidityState validity;
  readonly attribute DOMString validationMessage;
  boolean checkValidity();
  boolean reportValidity();
  undefined setCustomValidity(DOMString error);

  readonly attribute NodeList labels;
};
```

The `output` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the result of a calculation performed by the application, or the result of a user action.

This element can be contrasted with the `samp` element, which is the appropriate element for quoting the output of other programs run previously.

[Attributes/for](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/for "The for attribute is an allowed attribute for <label> and <output>. When used on a <label> element it indicates the form element that this label describes. When used on an <output> element it allows for an explicit relationship between the elements that represent values which are used in the output.")

Support in all current engines.

Firefox 4+Safari 7+Chrome 10+

* * *

Opera 11+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

The `for` content attribute allows an explicit relationship to be made between the result of a calculation and the elements that represent the values that went into the calculation or that otherwise influenced the calculation. The `for` attribute, if specified, must contain a string consisting of an [unordered set of unique space-separated tokens](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#unordered-set-of-unique-space-separated-tokens), none of which are [identical to](https://infra.spec.whatwg.org/#string-is) another token and each of which must have the value of an [ID](https://dom.spec.whatwg.org/#concept-id) of an element in the same [tree](https://dom.spec.whatwg.org/#concept-tree).

The `form` attribute is used to explicitly associate the `output` element with its [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner). The `name` attribute represents the element's name. The `output` element is associated with a form so that it can be easily [referenced](https://html.spec.whatwg.org/multipage/dom.html#referenced) from the event handlers of form controls; the element's value itself is not submitted when the form is submitted.

The element has a default value override (null or a string). Initially it must be null.

The element's default value is determined by the following steps:

1.   If this element's [default value override](https://html.spec.whatwg.org/multipage/form-elements.html#concept-output-default-value-override) is non-null, then return it.

2.   Return this element's [descendant text content](https://dom.spec.whatwg.org/#concept-descendant-text-content).

`output.value [ = value ]`
Returns the element's current value.

Can be set, to change the value.

`output.defaultValue [ = value ]`
Returns the element's current default value.

Can be set, to change the default value.

`output.type`
Returns the string "`output`".

The `defaultValue` getter steps are to return the result of running [this](https://webidl.spec.whatwg.org/#this)'s [default value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-output-default-value).

The `type` getter steps are to return "`output`".

The `willValidate`, `validity`, and `validationMessage` IDL attributes, and the `checkValidity()`, `reportValidity()`, and `setCustomValidity()` methods, are part of the [constraint validation API](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#the-constraint-validation-api). The `labels` IDL attribute provides a list of the element's `label`s. The `form` and `name` IDL attributes are part of the element's forms API.

A simple calculator could use `output` for its display of calculated results:

```
<form onsubmit="return false" oninput="o.value = a.valueAsNumber + b.valueAsNumber">
 <input id=a type=number step=any> +
 <input id=b type=number step=any> =
 <output id=o for="a b"></output>
</form>
```

In this example, an `output` element is used to report the results of a calculation performed by a remote server, as they come in:

```
<output id="result"></output>
<script>
 var primeSource = new WebSocket('ws://primes.example.net/');
 primeSource.onmessage = function (event) {
   document.getElementById('result').value = event.data;
 }
</script>
```

#### 4.10.13 The `progress` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-progress-element)

[Element/progress](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress "The <progress> HTML element displays an indicator showing the completion progress of a task, typically displayed as a progress bar.")

Support in all current engines.

Firefox 6+Safari 6+Chrome 6+

* * *

Opera 11+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 7+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

[HTMLProgressElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLProgressElement "The HTMLProgressElement interface provides special properties and methods (beyond the regular HTMLElement interface it also has available to it by inheritance) for manipulating the layout and presentation of <progress> elements.")

Support in all current engines.

Firefox 6+Safari 6+Chrome 6+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but there must be no `progress` element descendants.[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`value` — Current value of the element `max` — Upper bound of range [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-progress).[For implementers](https://w3c.github.io/html-aam/#el-progress).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLProgressElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, ReflectSetter] attribute double value;
  [CEReactions, ReflectPositive, ReflectDefault=1.0] attribute double max;
  readonly attribute double position;
  readonly attribute NodeList labels;
};
```

The `progress` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the completion progress of a task. The progress is either indeterminate, indicating that progress is being made but that it is not clear how much more work remains to be done before the task is complete (e.g. because the task is waiting for a remote host to respond), or the progress is a number in the range zero to a maximum, giving the fraction of work that has so far been completed.

[Attributes/max](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/max "The max attribute defines the maximum value that is acceptable and valid for the input containing the attribute. If the value of the element is greater than this, the element fails validation. This value must be greater than or equal to the value of the min attribute. If the max attribute is present but is not specified or is invalid, no max value is applied. If the max attribute is valid and a non-empty value is greater than the maximum allowed by the max attribute, constraint validation will prevent form submission.")

Support in all current engines.

Firefox 6+Safari 6+Chrome 6+

* * *

Opera 11+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 7+Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

There are two attributes that determine the current task completion represented by the element. The `value` attribute specifies how much of the task has been completed, and the `max` attribute specifies how much work the task requires in total. The units are arbitrary and not specified.

To make a determinate progress bar, add a `value` attribute with the current progress (either a number from 0.0 to 1.0, or, if the `max` attribute is specified, a number from 0 to the value of the `max` attribute). To make an indeterminate progress bar, remove the `value` attribute.

Authors are encouraged to also include the current value and the maximum value inline as text inside the element, so that the progress is made available to users of legacy user agents.

Here is a snippet of a web application that shows the progress of some automated task:

```
<section>
 <h2>Task Progress</h2>
 <p>Progress: <progress id=p max=100><span>0</span>%</progress></p>
 <script>
  var progressBar = document.getElementById('p');
  function updateProgress(newValue) {
    progressBar.value = newValue;
    progressBar.getElementsByTagName('span')[0].textContent = newValue;
  }
 </script>
</section>
```

(The `updateProgress()` method in this example would be called by some other code on the page to update the actual progress bar as the task progressed.)

The `value` and `max` attributes, when present, must have values that are [valid floating-point numbers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-floating-point-number). The `value` attribute, if present, must have a value greater than or equal to zero, and less than or equal to the value of the `max` attribute, if present, or 1.0, otherwise. The `max` attribute, if present, must have a value greater than zero.

The `progress` element is the wrong element to use for something that is just a gauge, as opposed to task progress. For instance, indicating disk space usage using `progress` would be inappropriate. Instead, the `meter` element is available for such use cases.

**User agent requirements**: If the `value` attribute is omitted, then the progress bar is an indeterminate progress bar. Otherwise, it is a determinate progress bar.

If the progress bar is a determinate progress bar and the element has a `max` attribute, the user agent must parse the `max` attribute's value according to the [rules for parsing floating-point number values](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-floating-point-number-values). If this does not result in an error, and if the parsed value is greater than zero, then the maximum value of the progress bar is that value. Otherwise, if the element has no `max` attribute, or if it has one but parsing it resulted in an error, or if the parsed value was less than or equal to zero, then the [maximum value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-maximum) of the progress bar is 1.0.

If the progress bar is a determinate progress bar, user agents must parse the `value` attribute's value according to the [rules for parsing floating-point number values](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-floating-point-number-values). If this does not result in an error and the parsed value is greater than zero, then the value of the progress bar is that parsed value. Otherwise, if parsing the `value` attribute's value resulted in an error or a number less than or equal to zero, then the [value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-value) of the progress bar is zero.

If the progress bar is a determinate progress bar, then the current value is the [maximum value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-maximum), if [value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-value) is greater than the [maximum value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-maximum), and [value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-value) otherwise.

**UA requirements for showing the progress bar**: When representing a `progress` element to the user, the UA should indicate whether it is a determinate or indeterminate progress bar, and in the former case, should indicate the relative position of the [current value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-current-value) relative to the [maximum value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-maximum).

`progress.position`
For a determinate progress bar (one with known current and maximum values), returns the result of dividing the current value by the maximum value.

For an indeterminate progress bar, returns −1.

If the progress bar is an indeterminate progress bar, then the `position` IDL attribute must return −1. Otherwise, it must return the result of dividing the [current value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-current-value) by the [maximum value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-maximum).

The `value` getter steps are to return 0 if [this](https://webidl.spec.whatwg.org/#this) is an indeterminate progress bar; otherwise [this](https://webidl.spec.whatwg.org/#this)'s [current value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-progress-value).

Setting the `value` IDL attribute to itself when the corresponding content attribute is absent would change the progress bar from an indeterminate progress bar to a determinate progress bar with no progress.

The `labels` IDL attribute provides a list of the element's `label`s.

#### 4.10.14 The `meter` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-meter-element)

[Element/meter](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter "The <meter> HTML element represents either a scalar value within a known range or a fractional value.")

Support in all current engines.

Firefox 16+Safari 6+Chrome 6+

* * *

Opera 11+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS 10.3+Chrome Android?WebView Android No Samsung Internet?Opera Android 11+

[HTMLMeterElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMeterElement "The HTML <meter> elements expose the HTMLMeterElement interface, which provides special properties and methods (beyond the HTMLElement object interface they also have available to them by inheritance) for manipulating the layout and presentation of <meter> elements.")

Support in all current engines.

Firefox 16+Safari 6+Chrome 6+

* * *

Opera 11+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 11+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but there must be no `meter` element descendants.[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`value` — Current value of the element `min` — Lower bound of range `max` — Upper bound of range `low` — High limit of low range `high` — Low limit of high range `optimum` — Optimum value in gauge [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-meter).[For implementers](https://w3c.github.io/html-aam/#el-meter).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLMeterElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, ReflectSetter] attribute double value;
  [CEReactions, ReflectSetter] attribute double min;
  [CEReactions, ReflectSetter] attribute double max;
  [CEReactions, ReflectSetter] attribute double low;
  [CEReactions, ReflectSetter] attribute double high;
  [CEReactions, ReflectSetter] attribute double optimum;
  readonly attribute NodeList labels;
};
```

The `meter` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a scalar measurement within a known range, or a fractional value; for example disk usage, the relevance of a query result, or the fraction of a voting population to have selected a particular candidate.

This is also known as a gauge.

The `meter` element should not be used to indicate progress (as in a progress bar). For that role, HTML provides a separate `progress` element.

The `meter` element also does not represent a scalar value of arbitrary range — for example, it would be wrong to use this to report a weight, or height, unless there is a known maximum value.

There are six attributes that determine the semantics of the gauge represented by the element.

[Attributes/max](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/max "The max attribute defines the maximum value that is acceptable and valid for the input containing the attribute. If the value of the element is greater than this, the element fails validation. This value must be greater than or equal to the value of the min attribute. If the max attribute is present but is not specified or is invalid, no max value is applied. If the max attribute is valid and a non-empty value is greater than the maximum allowed by the max attribute, constraint validation will prevent form submission.")

Support in all current engines.

Firefox 16+Safari 6+Chrome 6+

* * *

Opera 11+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS 10.3+Chrome Android?WebView Android No Samsung Internet?Opera Android 11+

[Attributes/min](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/min "The min attribute defines the minimum value that is acceptable and valid for the input containing the attribute. If the value of the element is less than this, the element fails validation. This value must be less than or equal to the value of the max attribute.")

Support in all current engines.

Firefox 16+Safari 6+Chrome 6+

* * *

Opera 11+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS 10.3+Chrome Android?WebView Android No Samsung Internet?Opera Android 11+

The `min` attribute specifies the lower bound of the range, and the `max` attribute specifies the upper bound. The `value` attribute specifies the value to have the gauge indicate as the "measured" value.

The other three attributes can be used to segment the gauge's range into "low", "medium", and "high" parts, and to indicate which part of the gauge is the "optimum" part. The `low` attribute specifies the range that is considered to be the "low" part, and the `high` attribute specifies the range that is considered to be the "high" part. The `optimum` attribute gives the position that is "optimum"; if that is higher than the "high" value then this indicates that the higher the value, the better; if it's lower than the "low" mark then it indicates that lower values are better, and naturally if it is in between then it indicates that neither high nor low values are good.

**Authoring requirements**: The `value` attribute must be specified. The `value`, `min`, `low`, `high`, `max`, and `optimum` attributes, when present, must have values that are [valid floating-point numbers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-floating-point-number).

In addition, the attributes' values are further constrained:

Let value be the `value` attribute's number.

If the `min` attribute is specified, then let minimum be that attribute's value; otherwise, let it be 0.

If the `max` attribute is specified, then let maximum be that attribute's value; otherwise, let it be 1.0.

The following inequalities must hold, as applicable:

*   minimum ≤ value ≤ maximum

*   minimum ≤ `low` ≤ maximum (if `low` is specified)

*   minimum ≤ `high` ≤ maximum (if `high` is specified)

*   minimum ≤ `optimum` ≤ maximum (if `optimum` is specified)

*   `low` ≤ `high` (if both `low` and `high` are specified)

If no minimum or maximum is specified, then the range is assumed to be 0..1, and the value thus has to be within that range.

Authors are encouraged to include a textual representation of the gauge's state in the element's contents, for users of user agents that do not support the `meter` element.

When used with [microdata](https://html.spec.whatwg.org/multipage/microdata.html#microdata), the `meter` element's `value` attribute provides the element's machine-readable value.

The following examples show three gauges that would all be three-quarters full:

`Storage space usage: <meter value=6 max=8>6 blocks used (out of 8 total)</meter>``Voter turnout: <meter value=0.75><img alt="75%" src="graph75.png"></meter>``Tickets sold: <meter min="0" max="100" value="75"></meter>`
The following example is incorrect use of the element, because it doesn't give a range (and since the default maximum is 1, both of the gauges would end up looking maxed out):

```
<p>The grapefruit pie had a radius of <meter value=12>12cm</meter>
and a height of <meter value=2>2cm</meter>.</p> <!-- BAD! -->
```

Instead, one would either not include the meter element, or use the meter element with a defined range to give the dimensions in context compared to other pies:

```
<p>The grapefruit pie had a radius of 12cm and a height of
2cm.</p>
<dl>
 <dt>Radius: <dd> <meter min=0 max=20 value=12>12cm</meter>
 <dt>Height: <dd> <meter min=0 max=10 value=2>2cm</meter>
</dl>
```

There is no explicit way to specify units in the `meter` element, but the units may be specified in the `title` attribute in free-form text.

The example above could be extended to mention the units:

```
<dl>
 <dt>Radius: <dd> <meter min=0 max=20 value=12 title="centimeters">12cm</meter>
 <dt>Height: <dd> <meter min=0 max=10 value=2 title="centimeters">2cm</meter>
</dl>
```

**User agent requirements**: User agents must parse the `min`, `max`, `value`, `low`, `high`, and `optimum` attributes using the [rules for parsing floating-point number values](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-floating-point-number-values).

User agents must then use all these numbers to obtain values for six points on the gauge, as follows. (The order in which these are evaluated is important, as some of the values refer to earlier ones.)

The minimum value
If the `min` attribute is specified and a value could be parsed out of it, then the minimum value is that value. Otherwise, the minimum value is zero.

The maximum value
If the `max` attribute is specified and a value could be parsed out of it, then the candidate maximum value is that value. Otherwise, the candidate maximum value is 1.0.

If the candidate maximum value is greater than or equal to the minimum value, then the maximum value is the candidate maximum value. Otherwise, the maximum value is the same as the minimum value.

The actual value
If the `value` attribute is specified and a value could be parsed out of it, then that value is the candidate actual value. Otherwise, the candidate actual value is zero.

If the candidate actual value is less than the minimum value, then the actual value is the minimum value.

Otherwise, if the candidate actual value is greater than the maximum value, then the actual value is the maximum value.

Otherwise, the actual value is the candidate actual value.

The low boundary
If the `low` attribute is specified and a value could be parsed out of it, then the candidate low boundary is that value. Otherwise, the candidate low boundary is the same as the minimum value.

If the candidate low boundary is less than the minimum value, then the low boundary is the minimum value.

Otherwise, if the candidate low boundary is greater than the maximum value, then the low boundary is the maximum value.

Otherwise, the low boundary is the candidate low boundary.

The high boundary
If the `high` attribute is specified and a value could be parsed out of it, then the candidate high boundary is that value. Otherwise, the candidate high boundary is the same as the maximum value.

If the candidate high boundary is less than the low boundary, then the high boundary is the low boundary.

Otherwise, if the candidate high boundary is greater than the maximum value, then the high boundary is the maximum value.

Otherwise, the high boundary is the candidate high boundary.

The optimum point
If the `optimum` attribute is specified and a value could be parsed out of it, then the candidate optimum point is that value. Otherwise, the candidate optimum point is the midpoint between the minimum value and the maximum value.

If the candidate optimum point is less than the minimum value, then the optimum point is the minimum value.

Otherwise, if the candidate optimum point is greater than the maximum value, then the optimum point is the maximum value.

Otherwise, the optimum point is the candidate optimum point.

All of which will result in the following inequalities all being true:

*   minimum value ≤ actual value ≤ maximum value

*   minimum value ≤ low boundary ≤ high boundary ≤ maximum value

*   minimum value ≤ optimum point ≤ maximum value

**UA requirements for regions of the gauge**: If the optimum point is equal to the low boundary or the high boundary, or anywhere in between them, then the region between the low and high boundaries of the gauge must be treated as the optimum region, and the low and high parts, if any, must be treated as suboptimal. Otherwise, if the optimum point is less than the low boundary, then the region between the minimum value and the low boundary must be treated as the optimum region, the region from the low boundary up to the high boundary must be treated as a suboptimal region, and the remaining region must be treated as an even less good region. Finally, if the optimum point is higher than the high boundary, then the situation is reversed; the region between the high boundary and the maximum value must be treated as the optimum region, the region from the high boundary down to the low boundary must be treated as a suboptimal region, and the remaining region must be treated as an even less good region.

**UA requirements for showing the gauge**: When representing a `meter` element to the user, the UA should indicate the relative position of the actual value to the minimum and maximum values, and the relationship between the actual value and the three regions of the gauge.

The following markup:

```
<h3>Suggested groups</h3>
<menu>
 <li><a href="?cmd=hsg" onclick="hideSuggestedGroups()">Hide suggested groups</a></li>
</menu>
<ul>
 <li>
  <p><a href="/group/comp.infosystems.www.authoring.stylesheets/view">comp.infosystems.www.authoring.stylesheets</a> -
     <a href="/group/comp.infosystems.www.authoring.stylesheets/subscribe">join</a></p>
  <p>Group description: <strong>Layout/presentation on the WWW.</strong></p>
  <p><meter value="0.5">Moderate activity,</meter> Usenet, 618 subscribers</p>
 </li>
 <li>
  <p><a href="/group/netscape.public.mozilla.xpinstall/view">netscape.public.mozilla.xpinstall</a> -
     <a href="/group/netscape.public.mozilla.xpinstall/subscribe">join</a></p>
  <p>Group description: <strong>Mozilla XPInstall discussion.</strong></p>
  <p><meter value="0.25">Low activity,</meter> Usenet, 22 subscribers</p>
 </li>
 <li>
  <p><a href="/group/mozilla.dev.general/view">mozilla.dev.general</a> -
     <a href="/group/mozilla.dev.general/subscribe">join</a></p>
  <p><meter value="0.25">Low activity,</meter> Usenet, 66 subscribers</p>
 </li>
</ul>
```

Might be rendered as follows:

![Image 2: With the <meter> elements rendered as inline green bars of varying lengths.](https://html.spec.whatwg.org/images/sample-meter.png)

User agents may combine the value of the `title` attribute and the other attributes to provide context-sensitive help or inline text detailing the actual values.

For example, the following snippet:

`<meter min=0 max=60 value=23.2 title=seconds></meter>`
...might cause the user agent to display a gauge with a tooltip saying "Value: 23.2 out of 60." on one line and "seconds" on a second line.

The `value` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [actual value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-meter-actual).

The `min` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [minimum value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-meter-minimum).

The `max` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [maximum value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-meter-maximum).

The `low` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [low boundary](https://html.spec.whatwg.org/multipage/form-elements.html#concept-meter-low).

The `high` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [high boundary](https://html.spec.whatwg.org/multipage/form-elements.html#concept-meter-high).

The `optimum` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [optimum value](https://html.spec.whatwg.org/multipage/form-elements.html#concept-meter-optimum).

The `labels` IDL attribute provides a list of the element's `label`s.

The following example shows how a gauge could fall back to localized or pretty-printed text.

```
<p>Disk usage: <meter min=0 value=170261928 max=233257824>170 261 928 bytes used
out of 233 257 824 bytes available</meter></p>
```

#### 4.10.15 The `fieldset` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-fieldset-element)

[Element/fieldset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset "The <fieldset> HTML element is used to group several controls as well as labels (<label>) within a web form.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera 15+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 14+

[HTMLFieldSetElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFieldSetElement "The HTMLFieldSetElement interface provides special properties and methods (beyond the regular HTMLElement interface it also has available to it by inheritance) for manipulating the layout and presentation of <fieldset> elements.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Listed](https://html.spec.whatwg.org/multipage/forms.html#category-listed) and [autocapitalize-and-autocorrect inheriting](https://html.spec.whatwg.org/multipage/forms.html#category-autocapitalize)[form-associated element](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):Optionally, a `legend` element, followed by [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`disabled` — Whether the descendant form controls, except any inside `legend`, are disabled `form` — Associates the element with a `form` element `name` — Name of the element to use in the `form.elements` API.[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-fieldset).[For implementers](https://w3c.github.io/html-aam/#el-fieldset).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLFieldSetElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute boolean disabled;
  readonly attribute HTMLFormElement? form;
  [CEReactions, Reflect] attribute DOMString name;

  readonly attribute DOMString type;

  [SameObject] readonly attribute HTMLCollection elements;

  readonly attribute boolean willValidate;
  [SameObject] readonly attribute ValidityState validity;
  readonly attribute DOMString validationMessage;
  boolean checkValidity();
  boolean reportValidity();
  undefined setCustomValidity(DOMString error);
};
```

The `fieldset` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a set of form controls (or other content) grouped together, optionally with a caption. The caption is given by the first `legend` element that is a child of the `fieldset` element, if any. The remainder of the descendants form the group.

[Element/fieldset#attr-disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset#attr-disabled "The <fieldset> HTML element is used to group several controls as well as labels (<label>) within a web form.")

Support in all current engines.

Firefox 4+Safari 6+Chrome 20+

* * *

Opera 12+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12+

The `disabled` attribute, when specified, causes all the form control descendants of the `fieldset` element, excluding those that are descendants of the `fieldset` element's first `legend` element child, if any, to be [disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-disabled).

A `fieldset` element is a disabled fieldset if it matches any of the following conditions:

*   Its `disabled` attribute is specified 
*   It is a descendant of another `fieldset` element whose `disabled` attribute is specified, and is _not_ a descendant of that `fieldset` element's first `legend` element child, if any.

The `form` attribute is used to explicitly associate the `fieldset` element with its [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner). The `name` attribute represents the element's name.

`fieldset.type`
Returns the string "fieldset".

`fieldset.elements`
Returns an `HTMLCollection` of the form controls in the element.

The `type` IDL attribute must return the string "`fieldset`".

The `elements` IDL attribute must return an `HTMLCollection` rooted at the `fieldset` element, whose filter matches [listed elements](https://html.spec.whatwg.org/multipage/forms.html#category-listed).

The `willValidate`, `validity`, and `validationMessage` attributes, and the `checkValidity()`, `reportValidity()`, and `setCustomValidity()` methods, are part of the [constraint validation API](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#the-constraint-validation-api). The `form` and `name` IDL attributes are part of the element's forms API.

This example shows a `fieldset` element being used to group a set of related controls:

```
<fieldset>
 <legend>Display</legend>
 <p><label><input type=radio name=c value=0 checked> Black on White</label>
 <p><label><input type=radio name=c value=1> White on Black</label>
 <p><label><input type=checkbox name=g> Use grayscale</label>
 <p><label>Enhance contrast <input type=range name=e list=contrast min=0 max=100 value=0 step=1></label>
 <datalist id=contrast>
  <option label=Normal value=0>
  <option label=Maximum value=100>
 </datalist>
</fieldset>
```

The following snippet shows a fieldset with a checkbox in the legend that controls whether or not the fieldset is enabled. The contents of the fieldset consist of two required text controls and an optional year/month control.

```
<fieldset name="clubfields" disabled>
 <legend> <label>
  <input type=checkbox name=club onchange="form.clubfields.disabled = !checked">
  Use Club Card
 </label> </legend>
 <p><label>Name on card: <input name=clubname required></label></p>
 <p><label>Card number: <input name=clubnum required pattern="[-0-9]+"></label></p>
 <p><label>Expiry date: <input name=clubexp type=month></label></p>
</fieldset>
```

You can also nest `fieldset` elements. Here is an example expanding on the previous one that does so:

```
<fieldset name="clubfields" disabled>
 <legend> <label>
  <input type=checkbox name=club onchange="form.clubfields.disabled = !checked">
  Use Club Card
 </label> </legend>
 <p><label>Name on card: <input name=clubname required></label></p>
 <fieldset name="numfields">
  <legend> <label>
   <input type=radio checked name=clubtype onchange="form.numfields.disabled = !checked">
   My card has numbers on it
  </label> </legend>
  <p><label>Card number: <input name=clubnum required pattern="[-0-9]+"></label></p>
 </fieldset>
 <fieldset name="letfields" disabled>
  <legend> <label>
   <input type=radio name=clubtype onchange="form.letfields.disabled = !checked">
   My card has letters on it
  </label> </legend>
  <p><label>Card code: <input name=clublet required pattern="[A-Za-z]+"></label></p>
 </fieldset>
</fieldset>
```

In this example, if the outer "Use Club Card" checkbox is not checked, everything inside the outer `fieldset`, including the two radio buttons in the legends of the two nested `fieldset`s, will be disabled. However, if the checkbox is checked, then the radio buttons will both be enabled and will let you select which of the two inner `fieldset`s is to be enabled.

This example shows a grouping of controls where the `legend` element both labels the grouping, and the nested heading element surfaces the grouping in the document outline:

```
<fieldset>
 <legend> <h2>
  How can we best reach you?
 </h2> </legend>
 <p> <label>
 <input type=radio checked name=contact_pref>
  Phone
 </label> </p>
 <p> <label>
  <input type=radio name=contact_pref>
  Text
 </label> </p>
 <p> <label>
  <input type=radio name=contact_pref>
  Email
 </label> </p>
</fieldset>
```

#### 4.10.16 The `legend` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-legend-element)

[Element/legend](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend "The <legend> HTML element represents a caption for the content of its parent <fieldset>.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 6+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLLegendElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLegendElement "The HTMLLegendElement is an interface allowing to access properties of the <legend> elements. It inherits properties and methods from the HTMLElement interface.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 6+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):None.[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):As the [first child](https://dom.spec.whatwg.org/#concept-tree-first-child) of a `fieldset` element.As the [first child](https://dom.spec.whatwg.org/#concept-tree-first-child) of an `optgroup` element.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):If the element is a child of an `optgroup` element: [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but there must be no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) and no descendant with the `tabindex` attribute.Otherwise: [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), optionally intermixed with [heading content](https://html.spec.whatwg.org/multipage/dom.html#heading-content-2).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-legend).[For implementers](https://w3c.github.io/html-aam/#el-legend).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLLegendElement : HTMLElement {
  [HTMLConstructor] constructor();

  readonly attribute HTMLFormElement? form;

  // also has obsolete members
};
```

The `legend` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a caption for the rest of the contents of the `legend` element's parent `fieldset` element, if any. Otherwise, if the `legend` has a parent `optgroup` element, then the `legend` represents the `optgroup`'s label.

`legend.form`
Returns the element's `form` element, if any, or null otherwise.

The `form` IDL attribute's behavior depends on whether the `legend` element is in a `fieldset` element or not. If the `legend` has a `fieldset` element as its parent, then the `form` IDL attribute must return the same value as the `form` IDL attribute on that `fieldset` element. Otherwise, it must return null.

#### 4.10.17 The `selectedcontent` element[](https://html.spec.whatwg.org/multipage/form-elements.html#the-selectedcontent-element)

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):As a descendant of a `button` element which is a child of a `select` element.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Nothing](https://html.spec.whatwg.org/multipage/dom.html#concept-content-nothing).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-selectedcontent).[For implementers](https://w3c.github.io/html-aam/#el-selectedcontent).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLSelectedContentElement : HTMLElement {
  [HTMLConstructor] constructor();
};
```

The `selectedcontent` element reflects the contents of a `select` element's currently selected `option` element. `selectedcontent` elements can be used to declaratively show the selected `option` element's contents within the `select` element's first child `button` element.

The `option` element's `label` attribute can be used to render a visible label for the option, but the `selectedcontent` element will not reflect the content of the `label` attribute.

Every `selectedcontent` element has a boolean disabled, which is initially false.

To update a `select`'s `selectedcontent` given a `select` element select:

1.   Let selectedcontent be the result of [get a `select`'s enabled `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#select-enabled-selectedcontent) given select.

2.   If selectedcontent is null, then return.

3.   Let option be the first `option` in select's [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) whose [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) is true, if any such `option` exists, otherwise null.

4.   If option is null, then run [clear a `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#clear-a-selectedcontent) given selectedcontent.

5.   Otherwise, run [clone an option into a `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#clone-an-option-into-a-selectedcontent) given option and selectedcontent.

To get a `select`'s enabled `selectedcontent` given a `select` element select:

1.   If select has the `multiple` attribute, then return null.

2.   Let selectedcontent be the first `selectedcontent` element [descendant](https://dom.spec.whatwg.org/#concept-tree-descendant) of select in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) if any such element exists; otherwise return null.

3.   If selectedcontent's [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#selectedcontent-disabled) is true, then return null.

4.   Return selectedcontent.

To clone an `option` into a `selectedcontent`, given an `option` element option and a `selectedcontent` element selectedcontent:

1.   Let documentFragment be a new `DocumentFragment` whose [node document](https://dom.spec.whatwg.org/#concept-node-document) is option's [node document](https://dom.spec.whatwg.org/#concept-node-document).

2.   For each child of option's [children](https://dom.spec.whatwg.org/#concept-tree-child):

    1.   Let childClone be the result of running [clone](https://dom.spec.whatwg.org/#concept-node-clone) given child with [subtree](https://dom.spec.whatwg.org/#clone-a-node-subtree) set to true.

    2.   [Append](https://dom.spec.whatwg.org/#concept-node-append)childClone to documentFragment.

3.   [Replace all](https://dom.spec.whatwg.org/#concept-node-replace-all) with documentFragment within selectedcontent.

To clear a `selectedcontent` given a `selectedcontent` element selectedcontent:

1.   [Replace all](https://dom.spec.whatwg.org/#concept-node-replace-all) with null within selectedcontent.

To clear a `select`'s non-primary `selectedcontent` elements, given a `select` element select:

1.   Let passedFirstSelectedcontent be false.

2.   For each descendant of select's [descendants](https://dom.spec.whatwg.org/#concept-tree-descendant) in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) that is a `selectedcontent` element:

    1.   If passedFirstSelectedcontent is false, then set passedFirstSelectedcontent to true.

    2.   Otherwise, run [clear a `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#clear-a-selectedcontent) given descendant.

The `selectedcontent`[HTML element post-connection steps](https://html.spec.whatwg.org/multipage/infrastructure.html#html-element-post-connection-steps), given selectedcontent, are:

1.   Let nearestSelectAncestor be null.

2.   Set selectedcontent's [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#selectedcontent-disabled) to false.

3.   For each ancestor of selectedcontent's [ancestors](https://dom.spec.whatwg.org/#concept-tree-ancestor), in reverse [tree order](https://dom.spec.whatwg.org/#concept-tree-order):

    1.   If ancestor is a `select` element:

        1.   If nearestSelectAncestor is null, then set nearestSelectAncestor to select and [continue](https://infra.spec.whatwg.org/#iteration-continue).

        2.   Set selectedcontent's [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#selectedcontent-disabled) to true and [break](https://infra.spec.whatwg.org/#iteration-break).

    2.   If ancestor is an `option` element or a `selectedcontent` element, then set selectedcontent's [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#selectedcontent-disabled) to true and [break](https://infra.spec.whatwg.org/#iteration-break).

4.   If selectedcontent's [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#selectedcontent-disabled) is true, nearestSelectAncestor is null, or nearestSelectAncestor has the `multiple` attribute, then return.

5.   Run [update a `select`'s `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#update-a-select's-selectedcontent) given nearestSelectAncestor.

6.   Run [clear a `select`'s non-primary `selectedcontent` elements](https://html.spec.whatwg.org/multipage/form-elements.html#clear-a-select's-non-primary-selectedcontent-elements) given nearestSelectAncestor.

The `selectedcontent`[HTML element removing steps](https://html.spec.whatwg.org/multipage/infrastructure.html#html-element-removing-steps), given removedNode, isSubtreeRoot, and oldAncestor are:

1.   If removedNode's [disabled](https://html.spec.whatwg.org/multipage/form-elements.html#selectedcontent-disabled) is true, then return.

2.   For each ancestor of removedNode's [ancestors](https://dom.spec.whatwg.org/#concept-tree-ancestor), in reverse [tree order](https://dom.spec.whatwg.org/#concept-tree-order):

    1.   If ancestor is a `select` element, then return.

3.   For each ancestor of oldAncestor's [inclusive ancestors](https://dom.spec.whatwg.org/#concept-tree-inclusive-ancestor), in reverse [tree order](https://dom.spec.whatwg.org/#concept-tree-order):

    1.   If ancestor is a `select` element, then run [update a `select`'s `selectedcontent`](https://html.spec.whatwg.org/multipage/form-elements.html#update-a-select's-selectedcontent) given ancestor and return.

[← 4.10.5 The input element](https://html.spec.whatwg.org/multipage/input.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.10.18 Form control infrastructure →](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html)
