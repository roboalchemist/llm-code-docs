# Source: https://html.spec.whatwg.org/multipage/custom-elements.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/custom-elements.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 4.12.5 The canvas element](https://html.spec.whatwg.org/multipage/canvas.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.14 Common idioms without dedicated elements →](https://html.spec.whatwg.org/multipage/semantics-other.html)
1.       1.   [4.13 Custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements)
        1.   [4.13.1 Introduction](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-intro)
            1.   [4.13.1.1 Creating an autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-autonomous-example)
            2.   [4.13.1.2 Creating a form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-face-example)
            3.   [4.13.1.3 Creating a custom element with default accessible roles, states, and properties](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-accessibility-example)
            4.   [4.13.1.4 Creating a customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-customized-builtin-example)
            5.   [4.13.1.5 Drawbacks of autonomous custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-autonomous-drawbacks)
            6.   [4.13.1.6 Upgrading elements after their creation](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-upgrades-examples)
            7.   [4.13.1.7 Scoped custom element registries](https://html.spec.whatwg.org/multipage/custom-elements.html#scoped-custom-element-registries)
            8.   [4.13.1.8 Exposing custom element states](https://html.spec.whatwg.org/multipage/custom-elements.html#exposing-custom-element-states)

        2.   [4.13.2 Requirements for custom element constructors and reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-conformance)
            1.   [4.13.2.1 Preserving custom element state when moved](https://html.spec.whatwg.org/multipage/custom-elements.html#preserving-custom-element-state-when-moved)

        3.   [4.13.3 Core concepts](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-core-concepts)
        4.   [4.13.4 The `CustomElementRegistry` interface](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-api)
        5.   [4.13.5 Upgrades](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrades)
        6.   [4.13.6 Custom element reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reactions)
        7.   [4.13.7 Element internals](https://html.spec.whatwg.org/multipage/custom-elements.html#element-internals)
            1.   [4.13.7.1 The `ElementInternals` interface](https://html.spec.whatwg.org/multipage/custom-elements.html#the-elementinternals-interface)
            2.   [4.13.7.2 Shadow root access](https://html.spec.whatwg.org/multipage/custom-elements.html#shadow-root-access)
            3.   [4.13.7.3 Form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-elements)
            4.   [4.13.7.4 Accessibility semantics](https://html.spec.whatwg.org/multipage/custom-elements.html#accessibility-semantics)
            5.   [4.13.7.5 Custom state pseudo-class](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-state-pseudo-class)

### 4.13 Custom elements[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements)

[Using_custom_elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements "One of the key features of the Web Components standard is the ability to create custom elements that encapsulate your functionality on an HTML page, rather than having to make do with a long, nested batch of elements that together provide a custom page feature. This article introduces the use of the Custom Elements API.")

Support in all current engines.

Firefox 63+Safari 10.1+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

#### 4.13.1 Introduction[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-intro)

_This section is non-normative._

[Custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) provide a way for authors to build their own fully-featured DOM elements. Although authors could always use non-standard elements in their documents, with application-specific behavior added after the fact by scripting or similar, such elements have historically been non-conforming and not very functional. By [defining](https://html.spec.whatwg.org/multipage/custom-elements.html#element-definition) a custom element, authors can inform the parser how to properly construct an element and how elements of that class should react to changes.

Custom elements are part of a larger effort to "rationalise the platform", by explaining existing platform features (like the elements of HTML) in terms of lower-level author-exposed extensibility points (like custom element definition). Although today there are many limitations on the capabilities of custom elements—both functionally and semantically—that prevent them from fully explaining the behaviors of HTML's existing elements, we hope to shrink this gap over time.

##### 4.13.1.1 Creating an autonomous custom element[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-autonomous-example)

_This section is non-normative._

For the purposes of illustrating how to create an [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element), let's define a custom element that encapsulates rendering a small icon for a country flag. Our goal is to be able to use it like so:

`<flag-icon country="nl"></flag-icon>`
To do this, we first declare a class for the custom element, extending `HTMLElement`:

```
class FlagIcon extends HTMLElement {
  constructor() {
    super();
    this._countryCode = null;
  }

  static observedAttributes = ["country"];

  attributeChangedCallback(name, oldValue, newValue) {
    // name will always be "country" due to observedAttributes
    this._countryCode = newValue;
    this._updateRendering();
  }
  connectedCallback() {
    this._updateRendering();
  }

  get country() {
    return this._countryCode;
  }
  set country(v) {
    this.setAttribute("country", v);
  }

  _updateRendering() {
    // Left as an exercise for the reader. But, you'll probably want to
    // check this.ownerDocument.defaultView to see if we've been
    // inserted into a document with a browsing context, and avoid
    // doing any work if not.
  }
}
```

We then need to use this class to define the element:

`customElements.define("flag-icon", FlagIcon);`
At this point, our above code will work! The parser, whenever it sees the `flag-icon` tag, will construct a new instance of our `FlagIcon` class, and tell our code about its new `country` attribute, which we then use to set the element's internal state and update its rendering (when appropriate).

You can also create `flag-icon` elements using the DOM API:

```
const flagIcon = document.createElement("flag-icon")
flagIcon.country = "jp"
document.body.appendChild(flagIcon)
```

Finally, we can also use the [custom element constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor) itself. That is, the above code is equivalent to:

```
const flagIcon = new FlagIcon()
flagIcon.country = "jp"
document.body.appendChild(flagIcon)
```

##### 4.13.1.2 Creating a form-associated custom element[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-face-example)

_This section is non-normative._

Adding a static `formAssociated` property, with a true value, makes an [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element) a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element). The `ElementInternals` interface helps you to implement functions and properties common to form control elements.

```
class MyCheckbox extends HTMLElement {
  static formAssociated = true;
  static observedAttributes = ['checked'];

  constructor() {
    super();
    this._internals = this.attachInternals();
    this.addEventListener('click', this._onClick.bind(this));
  }

  get form() { return this._internals.form; }
  get name() { return this.getAttribute('name'); }
  get type() { return this.localName; }

  get checked() { return this.hasAttribute('checked'); }
  set checked(flag) { this.toggleAttribute('checked', Boolean(flag)); }

  attributeChangedCallback(name, oldValue, newValue) {
    // name will always be "checked" due to observedAttributes
    this._internals.setFormValue(this.checked ? 'on' : null);
  }

  _onClick(event) {
    this.checked = !this.checked;
  }
}
customElements.define('my-checkbox', MyCheckbox);
```

You can use the custom element `my-checkbox` like a built-in form-associated element. For example, putting it in `form` or `label` associates the `my-checkbox` element with them, and submitting the `form` will send data provided by `my-checkbox` implementation.

```
<form action="..." method="...">
  <label><my-checkbox name="agreed"></my-checkbox> I read the agreement.</label>
  <input type="submit">
</form>
```

##### 4.13.1.3 Creating a custom element with default accessible roles, states, and properties[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-accessibility-example)

_This section is non-normative._

By using the appropriate properties of `ElementInternals`, your custom element can have default accessibility semantics. The following code expands our form-associated checkbox from the previous section to properly set its default role and checkedness, as viewed by accessibility technology:

```
class MyCheckbox extends HTMLElement {
  static formAssociated = true;
  static observedAttributes = ['checked'];

  constructor() {
    super();
    this._internals = this.attachInternals();
    this.addEventListener('click', this._onClick.bind(this));

    this._internals.role = 'checkbox';
    this._internals.ariaChecked = 'false';
  }

  get form() { return this._internals.form; }
  get name() { return this.getAttribute('name'); }
  get type() { return this.localName; }

  get checked() { return this.hasAttribute('checked'); }
  set checked(flag) { this.toggleAttribute('checked', Boolean(flag)); }

  attributeChangedCallback(name, oldValue, newValue) {
    // name will always be "checked" due to observedAttributes
    this._internals.setFormValue(this.checked ? 'on' : null);
    this._internals.ariaChecked = this.checked;
  }

  _onClick(event) {
    this.checked = !this.checked;
  }
}
customElements.define('my-checkbox', MyCheckbox);
```

Note that, like for built-in elements, these are only defaults, and can be overridden by the page author using the `role` and `aria-*` attributes:

```
<!-- This markup is non-conforming -->
<input type="checkbox" checked role="button" aria-checked="false">
```

```
<!-- This markup is probably not what the custom element author intended -->
<my-checkbox role="button" checked aria-checked="false">
```

Custom element authors are encouraged to state what aspects of their accessibility semantics are strong native semantics, i.e., should not be overridden by users of the custom element. In our example, the author of the `my-checkbox` element would state that its [role](https://w3c.github.io/aria/#dfn-role) and `aria-checked` values are strong native semantics, thus discouraging code such as the above.

##### 4.13.1.4 Creating a customized built-in element[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-customized-builtin-example)

_This section is non-normative._

[Customized built-in elements](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) are a distinct kind of [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element), which are defined slightly differently and used very differently compared to [autonomous custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element). They exist to allow reuse of behaviors from the existing elements of HTML, by extending those elements with new custom functionality. This is important since many of the existing behaviors of HTML elements can unfortunately not be duplicated by using purely [autonomous custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element). Instead, [customized built-in elements](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) allow the installation of custom construction behavior, lifecycle hooks, and prototype chain onto existing elements, essentially "mixing in" these capabilities on top of the already-existing element.

[Customized built-in elements](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) require a distinct syntax from [autonomous custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element) because user agents and other software key off an element's local name in order to identify the element's semantics and behavior. That is, the concept of [customized built-in elements](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) building on top of existing behavior depends crucially on the extended elements retaining their original local name.

In this example, we'll be creating a [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) named `plastic-button`, which behaves like a normal button but gets fancy animation effects added whenever you click on it. We start by defining a class, just like before, although this time we extend `HTMLButtonElement` instead of `HTMLElement`:

```
class PlasticButton extends HTMLButtonElement {
  constructor() {
    super();

    this.addEventListener("click", () => {
      // Draw some fancy animation effects!
    });
  }
}
```

When defining our custom element, we have to also specify the `extends` option:

`customElements.define("plastic-button", PlasticButton, { extends: "button" });`
In general, the name of the element being extended cannot be determined simply by looking at what element interface it extends, as many elements share the same interface (such as `q` and `blockquote` both sharing `HTMLQuoteElement`).

To construct our [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) from parsed HTML source text, we use the `is` attribute on a `button` element:

`<button is="plastic-button">Click Me!</button>`
Trying to use a [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) as an [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element) will _not_ work; that is, 
```
<plastic-button>Click
  me?</plastic-button>
```
 will simply create an `HTMLElement` with no special behavior.

If you need to create a customized built-in element programmatically, you can use the following form of `createElement()`:

```
const plasticButton = document.createElement("button", { is: "plastic-button" });
plasticButton.textContent = "Click me!";
```

And as before, the constructor will also work:

```
const plasticButton2 = new PlasticButton();
console.log(plasticButton2.localName);  // will output "button"
console.assert(plasticButton2 instanceof PlasticButton);
console.assert(plasticButton2 instanceof HTMLButtonElement);
```

Note that when creating a customized built-in element programmatically, the `is` attribute will not be present in the DOM, since it was not explicitly set. However, [it will be added to the output when serializing](https://html.spec.whatwg.org/multipage/parsing.html#attr-is-during-serialization):

```
console.assert(!plasticButton.hasAttribute("is"));
console.log(plasticButton.outerHTML); // will output '<button is="plastic-button"></button>'
```

Regardless of how it is created, all of the ways in which `button` is special apply to such "plastic buttons" as well: their focus behavior, ability to participate in [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-submit), the `disabled` attribute, and so on.

[Customized built-in elements](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) are designed to allow extension of existing HTML elements that have useful user-agent supplied behavior or APIs. As such, they can only extend existing HTML elements defined in this specification, and cannot extend legacy elements such as `bgsound`, `blink`, `isindex`, `keygen`, `multicol`, `nextid`, or `spacer` that have been defined to use `HTMLUnknownElement` as their [element interface](https://dom.spec.whatwg.org/#concept-element-interface).

One reason for this requirement is future-compatibility: if a [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) was defined that extended a currently-unknown element, for example `combobox`, this would prevent this specification from defining a `combobox` element in the future, as consumers of the derived [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) would have come to depend on their base element having no interesting user-agent-supplied behavior.

##### 4.13.1.5 Drawbacks of autonomous custom elements[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-autonomous-drawbacks)

_This section is non-normative._

As specified below, and alluded to above, simply defining and using an element called `taco-button` does not mean that such elements [represent](https://html.spec.whatwg.org/multipage/dom.html#represents) buttons. That is, tools such as web browsers, search engines, or accessibility technology will not automatically treat the resulting element as a button just based on its defined name.

To convey the desired button semantics to a variety of users, while still using an [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element), a number of techniques would need to be employed:

*   The addition of the `tabindex` attribute would make the `taco-button`[focusable](https://html.spec.whatwg.org/multipage/interaction.html#focusable). Note that if the `taco-button` were to become logically disabled, the `tabindex` attribute would need to be removed.

*   The addition of an ARIA role and various ARIA states and properties helps convey semantics to accessibility technology. For example, setting the [role](https://w3c.github.io/aria/#dfn-role) to "`button`" will convey the semantics that this is a button, enabling users to successfully interact with the control using usual button-like interactions in their accessibility technology. Setting the `aria-label` property is necessary to give the button an [accessible name](https://w3c.github.io/aria/#dfn-accessible-name), instead of having accessibility technology traverse its child text nodes and announce them. And setting the `aria-disabled` state to "`true`" when the button is logically disabled conveys to accessibility technology the button's disabled state.

*   The addition of event handlers to handle commonly-expected button behaviors helps convey the semantics of the button to web browser users. In this case, the most relevant event handler would be one that proxies appropriate `keydown` events to become `click` events, so that you can activate the button both with keyboard and by clicking.

*   In addition to any default visual styling provided for `taco-button` elements, the visual styling will also need to be updated to reflect changes in logical state, such as becoming disabled; that is, whatever style sheet has rules for `taco-button` will also need to have rules for `taco-button[disabled]`.

With these points in mind, a full-featured `taco-button` that took on the responsibility of conveying button semantics (including the ability to be disabled) might look something like this:

```
class TacoButton extends HTMLElement {
  static observedAttributes = ["disabled"];

  constructor() {
    super();
    this._internals = this.attachInternals();
    this._internals.role = "button";

    this.addEventListener("keydown", e => {
      if (e.code === "Enter" || e.code === "Space") {
        this.dispatchEvent(new PointerEvent("click", {
          bubbles: true,
          cancelable: true
        }));
      }
    });

    this.addEventListener("click", e => {
      if (this.disabled) {
        e.preventDefault();
        e.stopImmediatePropagation();
      }
    });

    this._observer = new MutationObserver(() => {
      this._internals.ariaLabel = this.textContent;
    });
  }

  connectedCallback() {
    this.setAttribute("tabindex", "0");

    this._observer.observe(this, {
      childList: true,
      characterData: true,
      subtree: true
    });
  }

  disconnectedCallback() {
    this._observer.disconnect();
  }

  get disabled() {
    return this.hasAttribute("disabled");
  }
  set disabled(flag) {
    this.toggleAttribute("disabled", Boolean(flag));
  }

  attributeChangedCallback(name, oldValue, newValue) {
    // name will always be "disabled" due to observedAttributes
    if (this.disabled) {
      this.removeAttribute("tabindex");
      this._internals.ariaDisabled = "true";
    } else {
      this.setAttribute("tabindex", "0");
      this._internals.ariaDisabled = "false";
    }
  }
}
```

Even with this rather-complicated element definition, the element is not a pleasure to use for consumers: it will be continually "sprouting" `tabindex` attributes of its own volition, and its choice of `tabindex="0"` focusability behavior may not match the `button` behavior on the current platform. This is because as of now there is no way to specify default focus behavior for custom elements, forcing the use of the `tabindex` attribute to do so (even though it is usually reserved for allowing the consumer to override default behavior).

In contrast, a simple [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element), as shown in the previous section, would automatically inherit the semantics and behavior of the `button` element, with no need to implement these behaviors manually. In general, for any elements with nontrivial behavior and semantics that build on top of existing elements of HTML, [customized built-in elements](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) will be easier to develop, maintain, and consume.

##### 4.13.1.6 Upgrading elements after their creation[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-upgrades-examples)

_This section is non-normative._

Because [element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#element-definition) can occur at any time, a non-custom element could be [created](https://dom.spec.whatwg.org/#concept-create-element), and then later become a [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) after an appropriate [definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition) is registered. We call this process "upgrading" the element, from a normal element into a custom element.

[Upgrades](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrades) enable scenarios where it may be preferable for [custom element definitions](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition) to be registered after relevant elements have been initially created, such as by the parser. They allow progressive enhancement of the content in the custom element. For example, in the following HTML document the element definition for `img-viewer` is loaded asynchronously:

```
<!DOCTYPE html>
<html lang="en">
<title>Image viewer example</title>

<img-viewer filter="Kelvin">
  <img src="images/tree.jpg" alt="A beautiful tree towering over an empty savannah">
</img-viewer>

<script src="js/elements/img-viewer.js" async></script>
```

The definition for the `img-viewer` element here is loaded using a `script` element marked with the `async` attribute, placed after the `<img-viewer>` tag in the markup. While the script is loading, the `img-viewer` element will be treated as an undefined element, similar to a `span`. Once the script loads, it will define the `img-viewer` element, and the existing `img-viewer` element on the page will be upgraded, applying the custom element's definition (which presumably includes applying an image filter identified by the string "Kelvin", enhancing the image's visual appearance).

* * *

Note that [upgrades](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrades) only apply to elements in the document tree. (Formally, elements that are [connected](https://dom.spec.whatwg.org/#connected).) An element that is not inserted into a document will stay un-upgraded. An example illustrates this point:

```
<!DOCTYPE html>
<html lang="en">
<title>Upgrade edge-cases example</title>

<example-element></example-element>

<script>
  "use strict";

  const inDocument = document.querySelector("example-element");
  const outOfDocument = document.createElement("example-element");

  // Before the element definition, both are HTMLElement:
  console.assert(inDocument instanceof HTMLElement);
  console.assert(outOfDocument instanceof HTMLElement);

  class ExampleElement extends HTMLElement {}
  customElements.define("example-element", ExampleElement);

  // After element definition, the in-document element was upgraded:
  console.assert(inDocument instanceof ExampleElement);
  console.assert(!(outOfDocument instanceof ExampleElement));

  document.body.appendChild(outOfDocument);

  // Now that we've moved the element into the document, it too was upgraded:
  console.assert(outOfDocument instanceof ExampleElement);
</script>
```

##### 4.13.1.7 Scoped custom element registries[](https://html.spec.whatwg.org/multipage/custom-elements.html#scoped-custom-element-registries)

To allow multiple libraries to co-exist without explicit coordination, `CustomElementRegistry` can be used in a scoped fashion as well.

```
const scoped = new CustomElementRegistry();
scoped.define("example-element", ExampleElement);

const element = document.createElement("example-element", { customElementRegistry: scoped });
```

A node with an associated scoped `CustomElementRegistry` will use that registry for all its operations, such as when invoking `setHTMLUnsafe()`.

##### 4.13.1.8 Exposing custom element states[](https://html.spec.whatwg.org/multipage/custom-elements.html#exposing-custom-element-states)

Built-in elements provided by user agents have certain states that can change over time depending on user interaction and other factors, and are exposed to web authors through [pseudo-classes](https://drafts.csswg.org/selectors/#pseudo-class). For example, some form controls have the "invalid" state, which is exposed through the `:invalid`[pseudo-class](https://drafts.csswg.org/selectors/#pseudo-class).

Like built-in elements, [custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) can have various states to be in too, and [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) authors want to expose these states in a similar fashion as the built-in elements.

This is done via the `:state()` pseudo-class. A custom element author can use the `states` property of `ElementInternals` to add and remove such custom states, which are then exposed as arguments to the `:state()` pseudo-class.

The following shows how `:state()` can be used to style a custom checkbox element. Assume that `LabeledCheckbox` doesn't expose its "checked" state via a content attribute.

```
<script>
class LabeledCheckbox extends HTMLElement {
  constructor() {
    super();
    this._internals = this.attachInternals();
    this.addEventListener('click', this._onClick.bind(this));

    const shadowRoot = this.attachShadow({mode: 'closed'});
    shadowRoot.innerHTML =
      `<style>
       :host::before {
         content: '[ ]';
         white-space: pre;
         font-family: monospace;
       }
       :host(:state(checked))::before { content: '[x]' }
       </style>
       <slot>Label</slot>`;
  }

  get checked() { return this._internals.states.has('checked'); }

  set checked(flag) {
    if (flag)
      this._internals.states.add('checked');
    else
      this._internals.states.delete('checked');
  }

  _onClick(event) {
    this.checked = !this.checked;
  }
}

customElements.define('labeled-checkbox', LabeledCheckbox);
</script>

<style>
labeled-checkbox { border: dashed red; }
labeled-checkbox:state(checked) { border: solid; }
</style>

<labeled-checkbox>You need to check this</labeled-checkbox>
```

Custom pseudo-classes can even target shadow parts. An extension of the above example shows this:

```
<script>
class QuestionBox extends HTMLElement {
  constructor() {
    super();
    const shadowRoot = this.attachShadow({mode: 'closed'});
    shadowRoot.innerHTML =
      `<div><slot>Question</slot></div>
       <labeled-checkbox part='checkbox'>Yes</labeled-checkbox>`;
  }
}
customElements.define('question-box', QuestionBox);
</script>

<style>
question-box::part(checkbox) { color: red; }
question-box::part(checkbox):state(checked) { color: green; }
</style>

<question-box>Continue?</question-box>
```

#### 4.13.2 Requirements for custom element constructors and reactions[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-conformance)

When authoring [custom element constructors](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor), authors are bound by the following conformance requirements:

*   A parameter-less call to `super()` must be the first statement in the constructor body, to establish the correct prototype chain and **this** value before any further code is run.

*   A `return` statement must not appear anywhere inside the constructor body, unless it is a simple early-return (`return` or 
```
return
   this
```
).

*   The constructor must not use the `document.write()` or `document.open()` methods.

*   The element's attributes and children must not be inspected, as in the non-[upgrade](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrades) case none will be present, and relying on upgrades makes the element less usable.

*   The element must not gain any attributes or children, as this violates the expectations of consumers who use the `createElement` or `createElementNS` methods.

*   In general, work should be deferred to `connectedCallback` as much as possible—especially work involving fetching resources or rendering. However, note that `connectedCallback` can be called more than once, so any initialization work that is truly one-time will need a guard to prevent it from running twice.

*   In general, the constructor should be used to set up initial state and default values, and to set up event listeners and possibly a [shadow root](https://dom.spec.whatwg.org/#concept-shadow-root).

Several of these requirements are checked during [element creation](https://dom.spec.whatwg.org/#concept-create-element), either directly or indirectly, and failing to follow them will result in a custom element that cannot be instantiated by the parser or DOM APIs. This is true even if the work is done inside a constructor-initiated [microtask](https://html.spec.whatwg.org/multipage/webappapis.html#microtask), as a [microtask checkpoint](https://html.spec.whatwg.org/multipage/webappapis.html#perform-a-microtask-checkpoint) can occur immediately after construction.

When authoring [custom element reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-reaction), authors should avoid manipulating the node tree as this can lead to unexpected results.

An element's `connectedCallback` can be queued before the element is disconnected, but as the callback queue is still processed, it results in a `connectedCallback` for an element that is no longer connected:

```
class CParent extends HTMLElement {
  connectedCallback() {
    this.firstChild.remove();
  }
}
customElements.define("c-parent", CParent);

class CChild extends HTMLElement {
  connectedCallback() {
    console.log("CChild connectedCallback: isConnected =", this.isConnected);
  }
}
customElements.define("c-child", CChild);

const parent = new CParent(),
      child = new CChild();
parent.append(child);
document.body.append(parent);

// Logs:
// CChild connectedCallback: isConnected = false
```

##### 4.13.2.1 Preserving custom element state when moved[](https://html.spec.whatwg.org/multipage/custom-elements.html#preserving-custom-element-state-when-moved)

_This section is non-normative._

When manipulating the DOM tree, an element can be [moved](https://dom.spec.whatwg.org/#concept-node-move-ext) in the tree while connected. This applies to custom elements as well. By default, the "`disconnectedCallback`" and "`connectedCallback`" would be called on the element, one after the other. This is done to maintain compatibility with existing custom elements that predate the `moveBefore()` method. This means that by default, custom elements reset their state as if they were removed and re-inserted. In the example [above](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-autonomous-drawbacks-example), the impact would be that the observer would be disconnected and re-connected, and the tab index would be reset.

To opt in to a state-preserving behavior while [moving](https://dom.spec.whatwg.org/#concept-node-move-ext), the author can implement a "`connectedMoveCallback`". The existence of this callback, even if empty, would supersede the default behavior of calling "`disconnectedCallback`" and "`connectedCallback`". "`connectedMoveCallback`" can also be an appropriate place to execute logic that depends on the element's ancestors. For example:

```
class TacoButton extends HTMLElement {
  static observedAttributes = ["disabled"];

  constructor() {
    super();
    this._internals = this.attachInternals();
    this._internals.role = "button";

    this._observer = new MutationObserver(() => {
      this._internals.ariaLabel = this.textContent;
    });
  }

  _notifyMain() {
    if (this.parentElement.tagName === "MAIN") {
      // Execute logic that depends on ancestors.
    }
  }

  connectedCallback() {
    this.setAttribute("tabindex", "0");

    this._observer.observe(this, {
      childList: true,
      characterData: true,
      subtree: true
    });

    this._notifyMain();
  }

  disconnectedCallback() {
    this._observer.disconnect();
  }

  // Implementing this function would avoid resetting the tab index or re-registering the
  // mutation observer when this element is moved inside the DOM without being disconnected.
  connectedMoveCallback() {
    // The parent can change during a state-preserving move.
    this._notifyMain();
  }
}
```

#### 4.13.3 Core concepts[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-core-concepts)

A custom element is an element that is [custom](https://dom.spec.whatwg.org/#concept-element-custom). Informally, this means that its constructor and prototype are defined by the author, instead of by the user agent. This author-supplied constructor function is called the custom element constructor.

Two distinct types of [custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) can be defined:

[Global_attributes/is](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/is "The is global attribute allows you to specify that a standard HTML element should behave like a defined custom built-in element (see Using custom elements for more details).")

Firefox 63+Safari No Chrome 67+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

*   An autonomous custom element, which is defined with no `extends` option. These types of custom elements have a local name equal to their [defined name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name).

*   A customized built-in element, which is defined with an `extends` option. These types of custom elements have a local name equal to the value passed in their `extends` option, and their [defined name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name) is used as the value of the `is` attribute, which therefore must be a [valid custom element name](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name).

After a [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) is [created](https://dom.spec.whatwg.org/#concept-create-element), changing the value of the `is` attribute does not change the element's behavior, as it is saved on the element as its [`is` value](https://dom.spec.whatwg.org/#concept-element-is-value).

[Autonomous custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element) have the following element definition:

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).For [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element): [Listed](https://html.spec.whatwg.org/multipage/forms.html#category-listed), [labelable](https://html.spec.whatwg.org/multipage/forms.html#category-label), [submittable](https://html.spec.whatwg.org/multipage/forms.html#category-submit), and [resettable](https://html.spec.whatwg.org/multipage/forms.html#category-reset)[form-associated element](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Transparent](https://html.spec.whatwg.org/multipage/dom.html#transparent).[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes), except the `is` attribute`form`, for [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) — Associates the element with a `form` element `disabled`, for [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) — Whether the form control is disabled `readonly`, for [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) — Affects `willValidate`, plus any behavior added by the custom element author `name`, for [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) — Name of the element to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2) and in the `form.elements` API Any other attribute that has no namespace (see prose).[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):For [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element): [for authors](https://w3c.github.io/html-aria/#el-form-associated-custom-element); [for implementers](https://w3c.github.io/html-aam/#el-form-associated-custom-element).Otherwise: [for authors](https://w3c.github.io/html-aria/#el-autonomous-custom-element); [for implementers](https://w3c.github.io/html-aam/#el-autonomous-custom-element).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):Supplied by the element's author (inherits from `HTMLElement`)
An [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element) does not have any special meaning: it [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) its children. A [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) inherits the semantics of the element that it extends.

Any namespace-less attribute that is relevant to the element's functioning, as determined by the element's author, may be specified on an [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element), so long as the attribute name is a [valid attribute local name](https://dom.spec.whatwg.org/#valid-attribute-local-name) and contains no [ASCII upper alphas](https://infra.spec.whatwg.org/#ascii-upper-alpha). The exception is the `is` attribute, which must not be specified on an [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element) (and which will have no effect if it is).

[Customized built-in elements](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) follow the normal requirements for attributes, based on the elements they extend. To add custom attribute-based behavior, use `data-*` attributes.

* * *

An [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element) is called a form-associated custom element if the element is associated with a [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition) whose [form-associated](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-form-associated) field is set to true.

The `name` attribute represents the [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element)'s name. The `disabled` attribute is used to make the [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) non-interactive and to prevent its [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) from being submitted. The `form` attribute is used to explicitly associate the [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) with its [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner).

The `readonly` attribute of [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) specifies that the element is [barred from constraint validation](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#barred-from-constraint-validation). User agents don't provide any other behavior for the attribute, but custom element authors should, where possible, use its presence to make their control non-editable in some appropriate fashion, similar to the behavior for the [readonly](https://html.spec.whatwg.org/multipage/input.html#attr-input-readonly) attribute on built-in form controls.

The [reset algorithm](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-reset-control) for [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) is to [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with the element, callback name "`formResetCallback`", and « ».

* * *

A string name is a valid custom element name if all of the following are true:

*   name is a [valid element local name](https://dom.spec.whatwg.org/#valid-element-local-name);

This ensures the custom element can be created with `createElement()`.

*   name's 0th [code point](https://infra.spec.whatwg.org/#code-point) is an [ASCII lower alpha](https://infra.spec.whatwg.org/#ascii-lower-alpha);

This ensures the HTML parser will treat the name as a tag name instead of as text.

*   name does not contain any [ASCII upper alphas](https://infra.spec.whatwg.org/#ascii-upper-alpha);

This ensures the user agent can always treat HTML elements ASCII-case-insensitively.

*   name contains a U+002D (-); and

This is used for namespacing and to ensure forward compatibility (since no elements will be added to HTML, SVG, or MathML with hyphen-containing local names going forward).

*   name is not one of the following:

    *   "`annotation-xml`"
    *   "`color-profile`"
    *   "`font-face`"
    *   "`font-face-src`"
    *   "`font-face-uri`"
    *   "`font-face-format`"
    *   "`font-face-name`"
    *   "`missing-glyph`"

The list of names above is the summary of all hyphen-containing element names from the [applicable specifications](https://html.spec.whatwg.org/multipage/infrastructure.html#other-applicable-specifications), namely SVG 2 and MathML. [[SVG]](https://html.spec.whatwg.org/multipage/references.html#refsSVG)[[MATHML]](https://html.spec.whatwg.org/multipage/references.html#refsMATHML)

Apart from these restrictions, a large variety of names is allowed, to give maximum flexibility for use cases like `<math-α>` or `<emotion-😍>`.

* * *

A custom element definition describes a [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) and consists of:

A name A [valid custom element name](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name)A local name A local name A constructor A Web IDL `CustomElementConstructor` callback function type value wrapping the [custom element constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor)A list of observed attributes A `sequence<DOMString>`A collection of lifecycle callbacks A map, whose keys are the strings "`connectedCallback`", "`disconnectedCallback`", "`adoptedCallback`", "`connectedMoveCallback`", "`attributeChangedCallback`", "`formAssociatedCallback`", "`formDisabledCallback`", "`formResetCallback`", and "`formStateRestoreCallback`". The corresponding values are either a Web IDL `Function` callback function type value, or null. By default the value of each entry is null.A construction stack A list, initially empty, that is manipulated by the [upgrade an element](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-upgrade-an-element) algorithm and the [HTML element constructors](https://html.spec.whatwg.org/multipage/dom.html#html-element-constructors). Each entry in the list will be either an element or an _already constructed_ marker.A form-associated boolean If this is true, user agent treats elements associated to this [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition) as [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element).A disable internals boolean Controls `attachInternals()`. A disable shadow boolean Controls `attachShadow()`. 

To look up a custom element definition, given null or a `CustomElementRegistry` object registry, string-or-null namespace, string localName, and string-or-null is, perform the following steps. They will return either a [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition) or null:

1.   If registry is null, then return null.

2.   If namespace is not the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), then return null.

3.   If registry's [custom element definition set](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition-set)[contains](https://infra.spec.whatwg.org/#list-contain) an item with [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name) and [local name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-local-name) both equal to localName, then return that item.

4.   If registry's [custom element definition set](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition-set)[contains](https://infra.spec.whatwg.org/#list-contain) an item with [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name) equal to is and [local name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-local-name) equal to localName, then return that item.

5.   Return null.

#### 4.13.4 The `CustomElementRegistry` interface[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-api)

[CustomElementRegistry](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry "The CustomElementRegistry interface provides methods for registering custom elements and querying registered elements. To get an instance of it, use the window.customElements property.")

Support in all current engines.

Firefox 63+Safari 10.1+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Each [similar-origin window agent](https://html.spec.whatwg.org/multipage/webappapis.html#similar-origin-window-agent) has an associated active custom element constructor map, which is a [map](https://infra.spec.whatwg.org/#ordered-map) of constructors to `CustomElementRegistry` objects.

[Window/customElements](https://developer.mozilla.org/en-US/docs/Web/API/Window/customElements "The customElements read-only property of the Window interface returns a reference to the CustomElementRegistry object, which can be used to register new custom elements and get information about previously registered custom elements.")

Support in all current engines.

Firefox 63+Safari 10.1+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

```
[Exposed=Window]
interface CustomElementRegistry {
  constructor();

  [CEReactions] undefined define(DOMString name, CustomElementConstructor constructor, optional ElementDefinitionOptions options = {});
  (CustomElementConstructor or undefined) get(DOMString name);
  DOMString? getName(CustomElementConstructor constructor);
  Promise<CustomElementConstructor> whenDefined(DOMString name);
  [CEReactions] undefined upgrade(Node root);
  [CEReactions] undefined initialize(Node root);
};

callback CustomElementConstructor = HTMLElement ();

dictionary ElementDefinitionOptions {
  DOMString extends;
};
```

Every `CustomElementRegistry` has an is scoped, a boolean, initially false.

Every `CustomElementRegistry` has a scoped document set, a [set](https://infra.spec.whatwg.org/#ordered-set) of `Document` objects, initially « ».

Every `CustomElementRegistry` has a custom element definition set, a [set](https://infra.spec.whatwg.org/#ordered-set) of [custom element definitions](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition), initially « ». Lookup of items in this [set](https://infra.spec.whatwg.org/#ordered-set) uses their [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name), [local name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-local-name), or [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor).

Every `CustomElementRegistry` also has an element definition is running boolean which is used to prevent reentrant invocations of [element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#element-definition). It is initially false.

Every `CustomElementRegistry` also has a when-defined promise map, a [map](https://infra.spec.whatwg.org/#ordered-map) of [valid custom element names](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name) to promises. It is used to implement the `whenDefined()` method.

`registry = window.customElements`Returns the global's associated `Document`'s `CustomElementRegistry` object.`registry = new CustomElementRegistry()`Constructs a new `CustomElementRegistry` object, for scoped usage.
```
registry.define(name,
   constructor)
```

[CustomElementRegistry/define](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry/define "The define() method of the CustomElementRegistry interface defines a new custom element.")

Support in all current engines.

Firefox 63+Safari 10.1+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Defines a new [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element), mapping the given name to the given constructor as an [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element).
```
registry.define(name, constructor,
   { extends: baseLocalName })
```
Defines a new [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element), mapping the given name to the given constructor as a [customized built-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#customized-built-in-element) for the [element type](https://html.spec.whatwg.org/multipage/infrastructure.html#element-type) identified by the supplied baseLocalName. A ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException` will be thrown upon trying to extend a [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) or an unknown element, or when registry is not a global `CustomElementRegistry` object.`registry.get(name)`

[CustomElementRegistry/get](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry/get "The get() method of the CustomElementRegistry interface returns the constructor for a previously-defined custom element.")

Support in all current engines.

Firefox 63+Safari 10.1+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Retrieves the [custom element constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor) defined for the given [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name). Returns undefined if there is no [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition) with the given [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name).`registry.getName(constructor)`Retrieves the given name for a [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) defined for the given [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor). Returns null if there is no [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition) with the given [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor).`registry.whenDefined(name)`

[CustomElementRegistry/whenDefined](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry/whenDefined "The whenDefined() method of the CustomElementRegistry interface returns a Promise that resolves when the named element is defined.")

Support in all current engines.

Firefox 63+Safari 10.1+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns a promise that will be fulfilled with the [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element)'s constructor when a [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) becomes defined with the given name. (If such a [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) is already defined, the returned promise will be immediately fulfilled.) Returns a promise rejected with a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException` if not given a [valid custom element name](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name).`registry.upgrade(root)`

[CustomElementRegistry/upgrade](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry/upgrade "The upgrade() method of the CustomElementRegistry interface upgrades all shadow-containing custom elements in a Node subtree, even before they are connected to the main document.")

Support in all current engines.

Firefox 63+Safari 12.1+Chrome 68+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[Tries to upgrade](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-try-upgrade) all [shadow-including inclusive descendant](https://dom.spec.whatwg.org/#concept-shadow-including-inclusive-descendant) elements of root, even if they are not [connected](https://dom.spec.whatwg.org/#connected).`registry.initialize(root)`Each [inclusive descendant](https://dom.spec.whatwg.org/#concept-tree-inclusive-descendant) of root with a null registry will have it updated to this `CustomElementRegistry` object. A ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException` will be thrown if this `CustomElementRegistry` object is not for scoped usage and either root is a `Document` node or root's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [custom element registry](https://dom.spec.whatwg.org/#document-custom-element-registry) is not this `CustomElementRegistry` object.
The `new CustomElementRegistry()` constructor steps are to set [this](https://webidl.spec.whatwg.org/#this)'s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) to true.

Element definition is a process of adding a [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition) to the `CustomElementRegistry`. This is accomplished by the `define()` method.

The 
```
define(name, constructor,
  options)
```
 method steps are:

1.   If [IsConstructor](https://tc39.es/ecma262/#sec-isconstructor)(constructor) is false, then throw a `TypeError`.

2.   If name is not a [valid custom element name](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name), then throw a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException`.

3.   If [this](https://webidl.spec.whatwg.org/#this)'s [custom element definition set](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition-set)[contains](https://infra.spec.whatwg.org/#list-contain) an item with [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name)name, then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

4.   If [this](https://webidl.spec.whatwg.org/#this)'s [custom element definition set](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition-set)[contains](https://infra.spec.whatwg.org/#list-contain) an item with [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor)constructor, then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

5.   Let localName be name.

6.   Let extends be options["`extends`"] if it [exists](https://infra.spec.whatwg.org/#map-exists); otherwise null.

7.   If extends is not null:

    1.   If [this](https://webidl.spec.whatwg.org/#this)'s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is true, then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

    2.   If extends is a [valid custom element name](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name), then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

    3.   If the [element interface](https://dom.spec.whatwg.org/#concept-element-interface) for extends and the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace) is `HTMLUnknownElement` (e.g., if extends does not indicate an element definition in this specification), then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

    4.   Set localName to extends.

8.   If [this](https://webidl.spec.whatwg.org/#this)'s [element definition is running](https://html.spec.whatwg.org/multipage/custom-elements.html#element-definition-is-running) is true, then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

9.   Set [this](https://webidl.spec.whatwg.org/#this)'s [element definition is running](https://html.spec.whatwg.org/multipage/custom-elements.html#element-definition-is-running) to true.

10.   Let formAssociated be false.

11.   Let disableInternals be false.

12.   Let disableShadow be false.

13.   Let observedAttributes be an empty `sequence<DOMString>`.

14.   Run the following steps while catching any exceptions:

    1.   Let prototype be ? [Get](https://tc39.es/ecma262/#sec-get-o-p)(constructor, "prototype").

    2.   If prototype[is not an Object](https://tc39.es/ecma262/#sec-object-type), then throw a `TypeError` exception.

    3.   Let lifecycleCallbacks be the [ordered map](https://infra.spec.whatwg.org/#ordered-map) «[ "`connectedCallback`" → null, "`disconnectedCallback`" → null, "`adoptedCallback`" → null, "`connectedMoveCallback`" → null, "`attributeChangedCallback`" → null ]».

    4.   For each callbackName of [the keys](https://infra.spec.whatwg.org/#map-getting-the-keys) of lifecycleCallbacks:

        1.   Let callbackValue be ? [Get](https://tc39.es/ecma262/#sec-get-o-p)(prototype, callbackName).

        2.   If callbackValue is not undefined, then [set](https://infra.spec.whatwg.org/#map-set)lifecycleCallbacks[callbackName] to the result of [converting](https://webidl.spec.whatwg.org/#es-type-mapping)callbackValue to the Web IDL `Function` callback type.

    5.   If lifecycleCallbacks["`attributeChangedCallback`"] is not null:

        1.   Let observedAttributesIterable be ? [Get](https://tc39.es/ecma262/#sec-get-o-p)(constructor, "observedAttributes").

        2.   If observedAttributesIterable is not undefined, then set observedAttributes to the result of [converting](https://webidl.spec.whatwg.org/#es-type-mapping)observedAttributesIterable to a `sequence<DOMString>`. Rethrow any exceptions from the conversion.

    6.   Let disabledFeatures be an empty `sequence<DOMString>`.

    7.   Let disabledFeaturesIterable be ? [Get](https://tc39.es/ecma262/#sec-get-o-p)(constructor, "disabledFeatures").

    8.   If disabledFeaturesIterable is not undefined, then set disabledFeatures to the result of [converting](https://webidl.spec.whatwg.org/#es-type-mapping)disabledFeaturesIterable to a `sequence<DOMString>`. Rethrow any exceptions from the conversion.

    9.   If disabledFeatures[contains](https://infra.spec.whatwg.org/#list-contain) "`internals`", then set disableInternals to true.

    10.   If disabledFeatures[contains](https://infra.spec.whatwg.org/#list-contain) "`shadow`", then set disableShadow to true.

    11.   Let formAssociatedValue be ? [Get](https://tc39.es/ecma262/#sec-get-o-p)( constructor, "formAssociated").

    12.   Set formAssociated to the result of [converting](https://webidl.spec.whatwg.org/#es-type-mapping)formAssociatedValue to a `boolean`.

    13.   If formAssociated is true, then for each callbackName of « "`formAssociatedCallback`", "`formResetCallback`", "`formDisabledCallback`", "`formStateRestoreCallback`" »:

        1.   Let callbackValue be ? [Get](https://tc39.es/ecma262/#sec-get-o-p)(prototype, callbackName).

        2.   If callbackValue is not undefined, then [set](https://infra.spec.whatwg.org/#map-set)lifecycleCallbacks[callbackName] to the result of [converting](https://webidl.spec.whatwg.org/#es-type-mapping)callbackValue to the Web IDL `Function` callback type.

Then, regardless of whether the above steps threw an exception or not: set [this](https://webidl.spec.whatwg.org/#this)'s [element definition is running](https://html.spec.whatwg.org/multipage/custom-elements.html#element-definition-is-running) to false.

Finally, if the steps threw an exception, rethrow that exception.

15.   Let definition be a new [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition) with [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name)name, [local name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-local-name)localName, [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor)constructor, [observed attributes](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-observed-attributes)observedAttributes, [lifecycle callbacks](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-lifecycle-callbacks)lifecycleCallbacks, [form-associated](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-form-associated)formAssociated, [disable internals](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-disable-internals)disableInternals, and [disable shadow](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-disable-shadow)disableShadow.

16.   [Append](https://infra.spec.whatwg.org/#set-append)definition to [this](https://webidl.spec.whatwg.org/#this)'s [custom element definition set](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition-set).

17.   If [this](https://webidl.spec.whatwg.org/#this)'s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is true, then for each document of [this](https://webidl.spec.whatwg.org/#this)'s [scoped document set](https://html.spec.whatwg.org/multipage/custom-elements.html#scoped-document-set): [upgrade particular elements within a document](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrade-particular-elements-within-a-document) given [this](https://webidl.spec.whatwg.org/#this), document, definition, and localName.

18.   Otherwise, [upgrade particular elements within a document](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrade-particular-elements-within-a-document) given [this](https://webidl.spec.whatwg.org/#this), [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window), definition, localName, and name.

19.   If [this](https://webidl.spec.whatwg.org/#this)'s [when-defined promise map](https://html.spec.whatwg.org/multipage/custom-elements.html#when-defined-promise-map)[name] [exists](https://infra.spec.whatwg.org/#map-exists):

    1.   Resolve [this](https://webidl.spec.whatwg.org/#this)'s [when-defined promise map](https://html.spec.whatwg.org/multipage/custom-elements.html#when-defined-promise-map)[name] with constructor.

    2.   [Remove](https://infra.spec.whatwg.org/#map-remove)[this](https://webidl.spec.whatwg.org/#this)'s [when-defined promise map](https://html.spec.whatwg.org/multipage/custom-elements.html#when-defined-promise-map)[name].

To upgrade particular elements within a document given a `CustomElementRegistry` object registry, a `Document` object document, a [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition)definition, a string localName, and optionally a string name (default localName):

1.   Let upgradeCandidates be all elements that are [shadow-including descendants](https://dom.spec.whatwg.org/#concept-shadow-including-descendant) of document, whose [custom element registry](https://dom.spec.whatwg.org/#element-custom-element-registry) is registry, whose namespace is the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), and whose local name is localName, in [shadow-including tree order](https://dom.spec.whatwg.org/#concept-shadow-including-tree-order). Additionally, if name is not localName, only include elements whose [`is` value](https://dom.spec.whatwg.org/#concept-element-is-value) is equal to name.

2.   For each element element of upgradeCandidates: [enqueue a custom element upgrade reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-upgrade-reaction) given element and definition.

The `get(name)` method steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this)'s [custom element definition set](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition-set)[contains](https://infra.spec.whatwg.org/#list-contain) an item with [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name)name, then return that item's [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor).

2.   Return undefined.

[CustomElementRegistry/getName](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry/getName "The getName() method of the CustomElementRegistry interface returns the name for a previously-defined custom element.")

Firefox 116+Safari🔰 preview+Chrome 117+

* * *

Opera?Edge 117+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `getName(constructor)` method steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this)'s [custom element definition set](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition-set)[contains](https://infra.spec.whatwg.org/#list-contain) an item with [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor)constructor, then return that item's [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name).

2.   Return null.

The `whenDefined(name)` method steps are:

1.   If name is not a [valid custom element name](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name), then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a ["`SyntaxError`"](https://webidl.spec.whatwg.org/#syntaxerror)`DOMException`.

2.   If [this](https://webidl.spec.whatwg.org/#this)'s [custom element definition set](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition-set)[contains](https://infra.spec.whatwg.org/#list-contain) an item with [name](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-name)name, then return [a promise resolved with](https://webidl.spec.whatwg.org/#a-promise-resolved-with) that item's [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor).

3.   If [this](https://webidl.spec.whatwg.org/#this)'s [when-defined promise map](https://html.spec.whatwg.org/multipage/custom-elements.html#when-defined-promise-map)[name] does not [exist](https://infra.spec.whatwg.org/#map-exists), then [set](https://infra.spec.whatwg.org/#map-set)[this](https://webidl.spec.whatwg.org/#this)'s [when-defined promise map](https://html.spec.whatwg.org/multipage/custom-elements.html#when-defined-promise-map)[name] to a new promise.

4.   Return [this](https://webidl.spec.whatwg.org/#this)'s [when-defined promise map](https://html.spec.whatwg.org/multipage/custom-elements.html#when-defined-promise-map)[name].

The `whenDefined()` method can be used to avoid performing an action until all appropriate [custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) are [defined](https://dom.spec.whatwg.org/#concept-element-defined). In this example, we combine it with the `:defined` pseudo-class to hide a dynamically-loaded article's contents until we're sure that all of the [autonomous custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element) it uses are defined.

```
articleContainer.hidden = true;

fetch(articleURL)
  .then(response => response.text())
  .then(text => {
    articleContainer.innerHTML = text;

    return Promise.all(
      [...articleContainer.querySelectorAll(":not(:defined)")]
        .map(el => customElements.whenDefined(el.localName))
    );
  })
  .then(() => {
    articleContainer.hidden = false;
  });
```

The `upgrade(root)` method steps are:

1.   For each [shadow-including inclusive descendant](https://dom.spec.whatwg.org/#concept-shadow-including-inclusive-descendant)candidate of root, in [shadow-including tree order](https://dom.spec.whatwg.org/#concept-shadow-including-tree-order):

    1.   If candidate is not an `Element` node, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    2.   If candidate's [custom element registry](https://dom.spec.whatwg.org/#element-custom-element-registry) is not [this](https://webidl.spec.whatwg.org/#this), then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    3.   [Try to upgrade](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-try-upgrade)candidate.

The `upgrade()` method allows upgrading of elements at will. Normally elements are automatically upgraded when they become [connected](https://dom.spec.whatwg.org/#connected), but this method can be used if you need to upgrade before you're ready to connect the element.

```
const el = document.createElement("spider-man");

class SpiderMan extends HTMLElement {}
customElements.define("spider-man", SpiderMan);

console.assert(!(el instanceof SpiderMan)); // not yet upgraded

customElements.upgrade(el);
console.assert(el instanceof SpiderMan);    // upgraded!
```

The `initialize(root)` method steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this)'s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is false and either root is a `Document` node or root's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [custom element registry](https://dom.spec.whatwg.org/#document-custom-element-registry) is not [this](https://webidl.spec.whatwg.org/#this), then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

2.   If root is a `Document` node whose [custom element registry](https://dom.spec.whatwg.org/#document-custom-element-registry) is null, then set root's [custom element registry](https://dom.spec.whatwg.org/#document-custom-element-registry) to [this](https://webidl.spec.whatwg.org/#this).

3.   Otherwise, if root is a `ShadowRoot` node whose [custom element registry](https://dom.spec.whatwg.org/#shadowroot-custom-element-registry) is null, then set root's [custom element registry](https://dom.spec.whatwg.org/#shadowroot-custom-element-registry) to [this](https://webidl.spec.whatwg.org/#this).

4.   For each [inclusive descendant](https://dom.spec.whatwg.org/#concept-tree-inclusive-descendant)inclusiveDescendant of root, in [tree order](https://dom.spec.whatwg.org/#concept-tree-order):

    1.   If inclusiveDescendant is not an `Element` node, then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    2.   If inclusiveDescendant's [custom element registry](https://dom.spec.whatwg.org/#element-custom-element-registry) is null:

        1.   Set inclusiveDescendant's [custom element registry](https://dom.spec.whatwg.org/#element-custom-element-registry) to [this](https://webidl.spec.whatwg.org/#this).

        2.   If [this](https://webidl.spec.whatwg.org/#this)'s [is scoped](https://html.spec.whatwg.org/multipage/custom-elements.html#is-scoped) is true, then [append](https://infra.spec.whatwg.org/#set-append)inclusiveDescendant's [node document](https://dom.spec.whatwg.org/#concept-node-document) to [this](https://webidl.spec.whatwg.org/#this)'s [scoped document set](https://html.spec.whatwg.org/multipage/custom-elements.html#scoped-document-set).

    3.   If inclusiveDescendant's [custom element registry](https://dom.spec.whatwg.org/#element-custom-element-registry) is not [this](https://webidl.spec.whatwg.org/#this), then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    4.   [Try to upgrade](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-try-upgrade)inclusiveDescendant.

Once the custom element registry of a node is initialized to a `CustomElementRegistry` object, it intentionally cannot be changed any further. This simplifies reasoning about code and allows implementations to optimize.

#### 4.13.5 Upgrades[](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrades)

To upgrade an element, given as input a [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition)definition and an element element, run the following steps:

1.   If element's [custom element state](https://dom.spec.whatwg.org/#concept-element-custom-element-state) is not "`undefined`" or "`uncustomized`", then return.

One scenario where this can occur due to reentrant invocation of this algorithm, as in the following example:

```
<!DOCTYPE html>
<x-foo id="a"></x-foo>
<x-foo id="b"></x-foo>

<script>
// Defining enqueues upgrade reactions for both "a" and "b"
customElements.define("x-foo", class extends HTMLElement {
  constructor() {
    super();

    const b = document.querySelector("#b");
    b.remove();

    // While this constructor is running for "a", "b" is still
    // undefined, and so inserting it into the document will enqueue a
    // second upgrade reaction for "b" in addition to the one enqueued
    // by defining x-foo.
    document.body.appendChild(b);
  }
})
</script>
```

This step will thus bail out the algorithm early when [upgrade an element](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-upgrade-an-element) is invoked with "`b`" a second time. 
2.   Set element's [custom element definition](https://dom.spec.whatwg.org/#concept-element-custom-element-definition) to definition.

3.   Set element's [custom element state](https://dom.spec.whatwg.org/#concept-element-custom-element-state) to "`failed`".

It will be set to "`custom`" [after the upgrade succeeds](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-upgrade-an-element-set-state-to-custom). For now, we set it to "`failed`" so that any reentrant invocations will hit [the above early-exit step](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-upgrade-an-element-early-exit).

4.   For each attribute in element's [attribute list](https://dom.spec.whatwg.org/#concept-element-attribute), in order, [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with element, callback name "`attributeChangedCallback`", and « attribute's local name, null, attribute's value, attribute's namespace ».

5.   If element is [connected](https://dom.spec.whatwg.org/#connected), then [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with element, callback name "`connectedCallback`", and « ».

6.   Add element to the end of definition's [construction stack](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-construction-stack).

7.   Let C be definition's [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor).

8.   [Set](https://infra.spec.whatwg.org/#map-set) the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)'s [active custom element constructor map](https://html.spec.whatwg.org/multipage/custom-elements.html#active-custom-element-constructor-map)[C] to element's [custom element registry](https://dom.spec.whatwg.org/#element-custom-element-registry).

9.   Run the following steps while catching any exceptions:

    1.   If definition's [disable shadow](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-disable-shadow) is true and element's [shadow root](https://dom.spec.whatwg.org/#concept-element-shadow-root) is non-null, then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

This is needed as `attachShadow()` does not use [look up a custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#look-up-a-custom-element-definition) while `attachInternals()` does.

    2.   Set element's [custom element state](https://dom.spec.whatwg.org/#concept-element-custom-element-state) to "`precustomized`".

    3.   Let constructResult be the result of [constructing](https://webidl.spec.whatwg.org/#construct-a-callback-function)C, with no arguments.

If C[non-conformantly](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-conformance) uses an API decorated with the `[CEReactions]` extended attribute, then the reactions enqueued at the beginning of this algorithm will execute during this step, before C finishes and control returns to this algorithm. Otherwise, they will execute after C and the rest of the upgrade process finishes.

    4.   If [SameValue](https://tc39.es/ecma262/#sec-samevalue)(constructResult, element) is false, then throw a `TypeError`.

This can occur if C constructs another instance of the same custom element before calling `super()`, or if C uses JavaScript's `return`-override feature to return an arbitrary `HTMLElement` object from the constructor.

Then, perform the following steps, regardless of whether the above steps threw an exception or not:

    1.   [Remove](https://infra.spec.whatwg.org/#map-remove) the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)'s [active custom element constructor map](https://html.spec.whatwg.org/multipage/custom-elements.html#active-custom-element-constructor-map)[C].

This is a no-op if C immediately calls `super()` as it ought to do.

    2.   Remove the last entry from the end of definition's [construction stack](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-construction-stack).

Assuming C calls `super()` (as it will if it is [conformant](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-conformance)), and that the call succeeds, this will be the [_already constructed_ marker](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-already-constructed-marker) that replaced the element we pushed at the beginning of this algorithm. (The [HTML element constructor](https://html.spec.whatwg.org/multipage/dom.html#html-element-constructors) carries out this replacement.)

If C does not call `super()` (i.e. it is not [conformant](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-conformance)), or if any step in the [HTML element constructor](https://html.spec.whatwg.org/multipage/dom.html#html-element-constructors) throws, then this entry will still be element. 

Finally, if the above steps threw an exception, then:

    1.   Set element's [custom element definition](https://dom.spec.whatwg.org/#concept-element-custom-element-definition) to null.

    2.   Empty element's [custom element reaction queue](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reaction-queue).

    3.   Rethrow the exception (thus terminating this algorithm).

If the above steps threw an exception, then element's [custom element state](https://dom.spec.whatwg.org/#concept-element-custom-element-state) will remain "`failed`" or "`precustomized`".

10.   If element is a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element), then:

    1.   [Reset the form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#reset-the-form-owner) of element. If element is associated with a `form` element, then [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with element, callback name "`formAssociatedCallback`", and « the associated `form` ».

    2.   If element is [disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-disabled), then [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with element, callback name "`formDisabledCallback`", and « true ».

11.   Set element's [custom element state](https://dom.spec.whatwg.org/#concept-element-custom-element-state) to "`custom`".

#### 4.13.6 Custom element reactions[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reactions)

A [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) possesses the ability to respond to certain occurrences by running author code:

*   When [upgraded](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrades), its [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-constructor) is run, with no arguments.

*   When it [becomes connected](https://html.spec.whatwg.org/multipage/infrastructure.html#becomes-connected), its `connectedCallback` is called, with no arguments.

*   When it [becomes disconnected](https://html.spec.whatwg.org/multipage/infrastructure.html#becomes-disconnected), its `disconnectedCallback` is called, with no arguments.

*   When it is [moved](https://dom.spec.whatwg.org/#concept-node-move-ext), its `connectedMoveCallback` is called, with no arguments.

*   When it is [adopted](https://dom.spec.whatwg.org/#concept-node-adopt) into a new document, its `adoptedCallback` is called, given the old document and new document as arguments.

*   When any of its attributes are [changed](https://dom.spec.whatwg.org/#concept-element-attributes-change), [appended](https://dom.spec.whatwg.org/#concept-element-attributes-append), [removed](https://dom.spec.whatwg.org/#concept-element-attributes-remove), or [replaced](https://dom.spec.whatwg.org/#concept-element-attributes-replace), its `attributeChangedCallback` is called, given the attribute's local name, old value, new value, and namespace as arguments. (An attribute's old or new value is considered to be null when the attribute is added or removed, respectively.)

*   When the user agent [resets the form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#reset-the-form-owner) of a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) and doing so changes the form owner, its `formAssociatedCallback` is called, given the new form owner (or null if no owner) as an argument.

*   When the form owner of a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) is [reset](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-reset), its `formResetCallback` is called.

*   When the [disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-disabled) state of a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) is changed, its `formDisabledCallback` is called, given the new state as an argument.

*   When the user agent updates a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element)'s value on behalf of a user or [as part of navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restore-persisted-state), its `formStateRestoreCallback` is called, given the new state and a string indicating a reason, "`autocomplete`" or "`restore`", as arguments.

We call these reactions collectively custom element reactions.

The way in which [custom element reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-reaction) are invoked is done with special care, to avoid running author code during the middle of delicate operations. Effectively, they are delayed until "just before returning to user script". This means that for most purposes they appear to execute synchronously, but in the case of complicated composite operations (like [cloning](https://dom.spec.whatwg.org/#concept-node-clone), or [range](https://dom.spec.whatwg.org/#concept-range) manipulation), they will instead be delayed until after all the relevant user agent processing steps have completed, and then run together as a batch.

Additionally, the precise ordering of these reactions is managed via a somewhat-complicated stack-of-queues system, described below. The intention behind this system is to guarantee that [custom element reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-reaction) always are invoked in the same order as their triggering actions, at least within the local context of a single [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element). (Because [custom element reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-reaction) code can perform its own mutations, it is not possible to give a global ordering guarantee across multiple elements.)

* * *

Each [similar-origin window agent](https://html.spec.whatwg.org/multipage/webappapis.html#similar-origin-window-agent) has a custom element reactions stack, which is initially empty. A [similar-origin window agent](https://html.spec.whatwg.org/multipage/webappapis.html#similar-origin-window-agent)'s current element queue is the [element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#element-queue) at the top of its [custom element reactions stack](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reactions-stack). Each item in the stack is an element queue, which is initially empty as well. Each item in an [element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#element-queue) is an element. (The elements are not necessarily [custom](https://dom.spec.whatwg.org/#concept-element-custom) yet, since this queue is used for [upgrades](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrades) as well.)

Each [custom element reactions stack](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reactions-stack) has an associated backup element queue, which is an initially-empty [element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#element-queue). Elements are pushed onto the [backup element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#backup-element-queue) during operations that affect the DOM without going through an API decorated with `[CEReactions]`, or through the parser's [create an element for the token](https://html.spec.whatwg.org/multipage/parsing.html#create-an-element-for-the-token) algorithm. An example of this is a user-initiated editing operation which modifies the descendants or attributes of an [editable](https://w3c.github.io/editing/docs/execCommand/#editable) element. To prevent reentrancy when processing the [backup element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#backup-element-queue), each [custom element reactions stack](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reactions-stack) also has a processing the backup element queue flag, initially unset.

All elements have an associated custom element reaction queue, initially empty. Each item in the [custom element reaction queue](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reaction-queue) is of one of two types:

*   An upgrade reaction, which will [upgrade](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrades) the custom element and contains a [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition); or

*   A callback reaction, which will call a lifecycle callback, and contains a callback function as well as a list of arguments.

This is all summarized in the following schematic diagram:

![Image 2: A custom element reactions stack consists of a stack of element queues. Zooming in on a particular queue, we see that it contains a number of elements (in our example, <x-a>, then <x-b>, then <x-c>). Any particular element in the queue then has a custom element reaction queue. Zooming in on the custom element reaction queue, we see that it contains a variety of queued-up reactions (in our example, upgrade, then attribute changed, then another attribute changed, then connected).](https://html.spec.whatwg.org/images/custom-element-reactions.svg)

To enqueue an element on the appropriate element queue, given an element element, run the following steps:

1.   Let reactionsStack be element's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [custom element reactions stack](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reactions-stack).

2.   If reactionsStack is empty, then:

    1.   Add element to reactionsStack's [backup element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#backup-element-queue).

    2.   If reactionsStack's [processing the backup element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#processing-the-backup-element-queue) flag is set, then return.

    3.   Set reactionsStack's [processing the backup element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#processing-the-backup-element-queue) flag.

    4.   [Queue a microtask](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-microtask) to perform the following steps:

        1.   [Invoke custom element reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#invoke-custom-element-reactions) in reactionsStack's [backup element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#backup-element-queue).

        2.   Unset reactionsStack's [processing the backup element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#processing-the-backup-element-queue) flag.

3.   Otherwise, add element to element's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [current element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#current-element-queue).

To enqueue a custom element callback reaction, given a [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element)element, a callback name callbackName, and a list of arguments args, run the following steps:

1.   Let definition be element's [custom element definition](https://dom.spec.whatwg.org/#concept-element-custom-element-definition).

2.   Let callback be the value of the entry in definition's [lifecycle callbacks](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-lifecycle-callbacks) with key callbackName.

3.   If callbackName is "`connectedMoveCallback`" and callback is null:

    1.   Let disconnectedCallback be the value of the entry in definition's [lifecycle callbacks](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-lifecycle-callbacks) with key "`disconnectedCallback`".

    2.   Let connectedCallback be the value of the entry in definition's [lifecycle callbacks](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-lifecycle-callbacks) with key "`connectedCallback`".

    3.   If connectedCallback and disconnectedCallback are null, then return.

    4.   Set callback to the following steps:

        1.   If disconnectedCallback is not null, then call disconnectedCallback with no arguments.

        2.   If connectedCallback is not null, then call connectedCallback with no arguments.

4.   If callback is null, then return.

5.   If callbackName is "`attributeChangedCallback`":

    1.   Let attributeName be the first element of args.

    2.   If definition's [observed attributes](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-observed-attributes) does not contain attributeName, then return.

6.   Add a new [callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#callback-reaction) to element's [custom element reaction queue](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reaction-queue), with callback function callback and arguments args.

7.   [Enqueue an element on the appropriate element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-an-element-on-the-appropriate-element-queue) given element.

To enqueue a custom element upgrade reaction, given an element element and [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition)definition, run the following steps:

1.   Add a new [upgrade reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrade-reaction) to element's [custom element reaction queue](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reaction-queue), with [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition)definition.

2.   [Enqueue an element on the appropriate element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-an-element-on-the-appropriate-element-queue) given element.

To invoke custom element reactions in an [element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#element-queue)queue, run the following steps:

1.   While queue is not [empty](https://infra.spec.whatwg.org/#list-is-empty):

    1.   Let element be the result of [dequeuing](https://infra.spec.whatwg.org/#queue-dequeue) from queue.

    2.   Let reactions be element's [custom element reaction queue](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reaction-queue).

    3.   Repeat until reactions is empty:

        1.   Remove the first element of reactions, and let reaction be that element. Switch on reaction's type:

[upgrade reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#upgrade-reaction)
[Upgrade](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-upgrade-an-element)element using reaction's [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition).

If this throws an exception, catch it, and [report](https://html.spec.whatwg.org/multipage/webappapis.html#report-an-exception) it for reaction's [custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-definition)'s [constructor](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-constructor)'s corresponding JavaScript object's [associated realm](https://webidl.spec.whatwg.org/#dfn-associated-realm)'s [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-realm-global).

[callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#callback-reaction)
[Invoke](https://webidl.spec.whatwg.org/#invoke-a-callback-function)reaction's callback function with reaction's arguments and "`report`", and _[callback this value](https://webidl.spec.whatwg.org/#dfn-callback-this-value)_ set to element.

* * *

To ensure [custom element reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-reaction) are triggered appropriately, we introduce the `[CEReactions]` IDL [extended attribute](https://webidl.spec.whatwg.org/#dfn-extended-attribute). It indicates that the relevant algorithm is to be supplemented with additional steps in order to appropriately track and invoke [custom element reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-reaction).

The `[CEReactions]` extended attribute must take no arguments, and must not appear on anything other than an operation, attribute, setter, or deleter. Additionally, it must not appear on readonly attributes.

Operations, attributes, setters, or deleters annotated with the `[CEReactions]` extended attribute must run the following steps in place of the ones specified in their description:

1.   [Push](https://infra.spec.whatwg.org/#stack-push) a new [element queue](https://html.spec.whatwg.org/multipage/custom-elements.html#element-queue) onto this object's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [custom element reactions stack](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reactions-stack).

2.   Run the originally-specified steps for this construct, catching any exceptions. If the steps return a value, let value be the returned value. If they throw an exception, let exception be the thrown exception.

3.   Let queue be the result of [popping](https://infra.spec.whatwg.org/#stack-pop) from this object's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [custom element reactions stack](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element-reactions-stack).

4.   [Invoke custom element reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#invoke-custom-element-reactions) in queue.

5.   If an exception exception was thrown by the original steps, rethrow exception.

6.   If a value value was returned from the original steps, return value.

The intent behind this extended attribute is somewhat subtle. One way of accomplishing its goals would be to say that every operation, attribute, setter, and deleter on the platform must have these steps inserted, and to allow implementers to optimize away unnecessary cases (where no DOM mutation is possible that could cause [custom element reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-reaction) to occur).

However, in practice this imprecision could lead to non-interoperable implementations of [custom element reactions](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-reaction), as some implementations might forget to invoke these steps in some cases. Instead, we settled on the approach of explicitly annotating all relevant IDL constructs, as a way of ensuring interoperable behavior and helping implementations easily pinpoint all cases where these steps are necessary.

Any nonstandard APIs introduced by the user agent that could modify the DOM in such a way as to cause [enqueuing a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) or [enqueuing a custom element upgrade reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-upgrade-reaction), for example by modifying any attributes or child elements, must also be decorated with the `[CEReactions]` attribute.

As of the time of this writing, the following nonstandard or not-yet-standardized APIs are known to fall into this category:

*   `HTMLInputElement`'s `webkitdirectory` and `incremental` IDL attributes

*   `HTMLLinkElement`'s `scope` IDL attribute

#### 4.13.7 Element internals[](https://html.spec.whatwg.org/multipage/custom-elements.html#element-internals)

Certain capabilities are meant to be available to a custom element author, but not to a custom element consumer. These are provided by the `element.attachInternals()` method, which returns an instance of `ElementInternals`. The properties and methods of `ElementInternals` allow control over internal features which the user agent provides to all elements.

`element.attachInternals()`
Returns an `ElementInternals` object targeting the [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element)element. Throws an exception if element is not a [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element), if the "`internals`" feature was disabled as part of the element definition, or if it is called twice on the same element.

Each `HTMLElement` has an attached internals (null or an `ElementInternals` object), initially null.

[HTMLElement/attachInternals](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/attachInternals "The HTMLElement.attachInternals() method returns an ElementInternals object. This method allows a custom element to participate in HTML forms. The ElementInternals interface provides utilities for working with these elements in the same way you would work with any standard HTML form element, and also exposes the Accessibility Object Model to the element.")

Support in all current engines.

Firefox 93+Safari 16.4+Chrome 77+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `attachInternals()` method steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this)'s [`is` value](https://dom.spec.whatwg.org/#concept-element-is-value) is not null, then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

2.   Let definition be the result of [looking up a custom element definition](https://html.spec.whatwg.org/multipage/custom-elements.html#look-up-a-custom-element-definition) given [this](https://webidl.spec.whatwg.org/#this)'s [custom element registry](https://dom.spec.whatwg.org/#element-custom-element-registry), [this](https://webidl.spec.whatwg.org/#this)'s [namespace](https://dom.spec.whatwg.org/#concept-element-namespace), [this](https://webidl.spec.whatwg.org/#this)'s [local name](https://dom.spec.whatwg.org/#concept-element-local-name), and null.

3.   If definition is null, then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

4.   If definition's [disable internals](https://html.spec.whatwg.org/multipage/custom-elements.html#concept-custom-element-definition-disable-internals) is true, then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

5.   If [this](https://webidl.spec.whatwg.org/#this)'s [attached internals](https://html.spec.whatwg.org/multipage/custom-elements.html#attached-internals) is non-null, then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

6.   If [this](https://webidl.spec.whatwg.org/#this)'s [custom element state](https://dom.spec.whatwg.org/#concept-element-custom-element-state) is not "`precustomized`" or "`custom`", then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

7.   Set [this](https://webidl.spec.whatwg.org/#this)'s [attached internals](https://html.spec.whatwg.org/multipage/custom-elements.html#attached-internals) to a new `ElementInternals` instance whose [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) is [this](https://webidl.spec.whatwg.org/#this).

8.   Return [this](https://webidl.spec.whatwg.org/#this)'s [attached internals](https://html.spec.whatwg.org/multipage/custom-elements.html#attached-internals).

##### 4.13.7.1 The `ElementInternals` interface[](https://html.spec.whatwg.org/multipage/custom-elements.html#the-elementinternals-interface)

[ElementInternals](https://developer.mozilla.org/en-US/docs/Web/API/ElementInternals "The ElementInternals interface of the Document Object Model gives web developers a way to allow custom elements to fully participate in HTML forms. It provides utilities for working with these elements in the same way you would work with any standard HTML form element, and also exposes the Accessibility Object Model to the element.")

Support in all current engines.

Firefox 93+Safari 16.4+Chrome 77+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The IDL for the `ElementInternals` interface is as follows, with the various operations and attributes defined in the following sections:

```
[Exposed=Window]
interface ElementInternals {
  // Shadow root access
  readonly attribute ShadowRoot? shadowRoot;

  // Form-associated custom elements
  undefined setFormValue((File or USVString or FormData)? value,
                         optional (File or USVString or FormData)? state);

  readonly attribute HTMLFormElement? form;

  undefined setValidity(optional ValidityStateFlags flags = {},
                        optional DOMString message,
                        optional HTMLElement anchor);
  readonly attribute boolean willValidate;
  readonly attribute ValidityState validity;
  readonly attribute DOMString validationMessage;
  boolean checkValidity();
  boolean reportValidity();

  readonly attribute NodeList labels;

  // Custom state pseudo-class
  [SameObject] readonly attribute CustomStateSet states;
};

// Accessibility semantics
ElementInternals includes ARIAMixin;

dictionary ValidityStateFlags {
  boolean valueMissing = false;
  boolean typeMismatch = false;
  boolean patternMismatch = false;
  boolean tooLong = false;
  boolean tooShort = false;
  boolean rangeUnderflow = false;
  boolean rangeOverflow = false;
  boolean stepMismatch = false;
  boolean badInput = false;
  boolean customError = false;
};
```

Each `ElementInternals` has a target element, which is a [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element).

##### 4.13.7.2 Shadow root access[](https://html.spec.whatwg.org/multipage/custom-elements.html#shadow-root-access)

`internals.shadowRoot`
Returns the `ShadowRoot` for internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target), if the [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) is a [shadow host](https://dom.spec.whatwg.org/#element-shadow-host), or null otherwise.

[ElementInternals/shadowRoot](https://developer.mozilla.org/en-US/docs/Web/API/ElementInternals/shadowRoot "The shadowRoot read-only property of the ElementInternals interface returns the ShadowRoot for this element.")

Support in all current engines.

Firefox 93+Safari 16.4+Chrome 88+

* * *

Opera?Edge 88+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

##### 4.13.7.3 Form-associated custom elements[](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-elements)

`internals.setFormValue(value)`
Sets both the [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state) and [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) of internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) to value.

If value is null, the element won't participate in form submission.

```
internals.setFormValue(value,
   state)
```

Sets the [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) of internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) to value, and its [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state) to state.

If value is null, the element won't participate in form submission.

`internals.form`
Returns the [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) of internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target).

```
internals.setValidity(flags,
   message [, anchor ])
```

Marks internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) as suffering from the constraints indicated by the flags argument, and sets the element's validation message to message. If anchor is specified, the user agent might use it to indicate problems with the constraints of internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) when the [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) is validated interactively or `reportValidity()` is called.

`internals.setValidity({})`
Marks internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) as [satisfying its constraints](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fv-valid).

`internals.willValidate`
Returns true if internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) will be validated when the form is submitted; false otherwise.

`internals.validity`
Returns the `ValidityState` object for internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target).

`internals.validationMessage`
Returns the error message that would be shown to the user if internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) was to be checked for validity.

`valid = internals.checkValidity()`
Returns true if internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) has no validity problems; false otherwise. Fires an `invalid` event at the element in the latter case.

`valid = internals.reportValidity()`
Returns true if internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) has no validity problems; otherwise, returns false, fires an `invalid` event at the element, and (if the event isn't canceled) reports the problem to the user.

`internals.labels`
Returns a `NodeList` of all the `label` elements that internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target) is associated with.

Each [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) has submission value. It is used to provide one or more [entries](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-entry) on form submission. The initial value of [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) is null, and [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) can be null, a string, a `File`, or a [list](https://infra.spec.whatwg.org/#list) of [entries](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-entry).

Each [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) has state. It is information with which the user agent can restore a user's input for the element. The initial value of [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state) is null, and [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state) can be null, a string, a `File`, or a [list](https://infra.spec.whatwg.org/#list) of [entries](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-entry).

The `setFormValue()` method is used by the custom element author to set the element's [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) and [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state), thus communicating these to the user agent.

When the user agent believes it is a good idea to restore a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element)'s [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state), for example [after navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#restore-persisted-state) or restarting the user agent, they may [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with that element, callback name "`formStateRestoreCallback`", and « the state to be restored, "`restore`" ».

If the user agent has a form-filling assist feature, then when the feature is invoked, it may [enqueue a custom element callback reaction](https://html.spec.whatwg.org/multipage/custom-elements.html#enqueue-a-custom-element-callback-reaction) with a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element), callback name "`formStateRestoreCallback`", and « the state value determined by history of state value and some heuristics, "`autocomplete`" ».

In general, the [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state) is information specified by a user, and the [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) is a value after canonicalization or sanitization, suitable for submission to the server. The following examples makes this concrete:

Suppose that we have a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) which asks a user to specify a date. The user specifies "3/15/2019", but the control wishes to submit `"2019-03-15"` to the server. "3/15/2019" would be a [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state) of the element, and `"2019-03-15"` would be a [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value).

Suppose you develop a custom element emulating a the behavior of the existing [checkbox](https://html.spec.whatwg.org/multipage/input.html#checkbox-state-(type=checkbox))`input` type. Its [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) would be the value of its `value` content attribute, or the string `"on"`. Its [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state) would be one of `"checked"`, `"unchecked"`, `"checked/indeterminate"`, or `"unchecked/indeterminate"`.

[ElementInternals/setFormValue](https://developer.mozilla.org/en-US/docs/Web/API/ElementInternals/setFormValue "The setFormValue() method of the ElementInternals interface sets the element's submission value and state, communicating these to the user agent.")

Support in all current engines.

Firefox 98+Safari 16.4+Chrome 77+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The 
```
setFormValue(value,
  state)
```
 method steps are:

1.   Let element be [this](https://webidl.spec.whatwg.org/#this)'s [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target).

2.   If element is not a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element), then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

3.   Set element's [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) to value if value is not a `FormData` object, or to a [clone](https://infra.spec.whatwg.org/#list-clone) of value's [entry list](https://xhr.spec.whatwg.org/#concept-formdata-entry-list) otherwise.

4.   If the state argument of the function is omitted, set element's [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state) to its [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value).

5.   Otherwise, if state is a `FormData` object, set element's [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state) to a [clone](https://infra.spec.whatwg.org/#list-clone) of state's [entry list](https://xhr.spec.whatwg.org/#concept-formdata-entry-list).

6.   Otherwise, set element's [state](https://html.spec.whatwg.org/multipage/custom-elements.html#face-state) to state.

* * *

Each [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) has validity flags named `valueMissing`, `typeMismatch`, `patternMismatch`, `tooLong`, `tooShort`, `rangeUnderflow`, `rangeOverflow`, `stepMismatch`, and `customError`. They are false initially.

Each [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) has a validation message string. It is the empty string initially.

Each [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) has a validation anchor element. It is null initially.

[ElementInternals/setValidity](https://developer.mozilla.org/en-US/docs/Web/API/ElementInternals/setValidity "The setValidity() method of the ElementInternals interface sets the validity of the element.")

Support in all current engines.

Firefox 98+Safari 16.4+Chrome 77+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The 
```
setValidity(flags, message,
  anchor)
```
 method steps are:

1.   Let element be [this](https://webidl.spec.whatwg.org/#this)'s [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target).

2.   If element is not a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element), then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

3.   If flags contains one or more true values and message is not given or is the empty string, then throw a `TypeError`.

4.   For each entry flag → value of flags, set element's validity flag with the name flag to value.

5.   Set element's [validation message](https://html.spec.whatwg.org/multipage/custom-elements.html#face-validation-message) to the empty string if message is not given or all of element's validity flags are false, or to message otherwise.

6.   If element's `customError` validity flag is true, then set element's [custom validity error message](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#custom-validity-error-message) to element's [validation message](https://html.spec.whatwg.org/multipage/custom-elements.html#face-validation-message). Otherwise, set element's [custom validity error message](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#custom-validity-error-message) to the empty string.

7.   If anchor is not given, then set it to element.

8.   Otherwise, if anchor is not a [shadow-including inclusive descendant](https://dom.spec.whatwg.org/#concept-shadow-including-inclusive-descendant) of element, then throw a ["`NotFoundError`"](https://webidl.spec.whatwg.org/#notfounderror)`DOMException`.

9.   Set element's [validation anchor](https://html.spec.whatwg.org/multipage/custom-elements.html#face-validation-anchor) to anchor.

[ElementInternals/validationMessage](https://developer.mozilla.org/en-US/docs/Web/API/ElementInternals/validationMessage "The validationMessage read-only property of the ElementInternals interface returns the validation message for the element.")

Support in all current engines.

Firefox 98+Safari 16.4+Chrome 77+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The entry construction algorithm for a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element), given an element element and an [entry list](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#entry-list)entry list, consists of the following steps:

1.   If element's [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) is a [list](https://infra.spec.whatwg.org/#list) of [entries](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-entry), then [append](https://infra.spec.whatwg.org/#list-append) each item of element's [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) to entry list, and return.

In this case, user agent does not refer to the `name` content attribute value. An implementation of [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) is responsible to decide names of [entries](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-entry). They can be the `name` content attribute value, they can be strings based on the `name` content attribute value, or they can be unrelated to the `name` content attribute.

2.   If the element does not have a `name` attribute specified, or its `name` attribute's value is the empty string, then return.

3.   If the element's [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value) is not null, [create an entry](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#create-an-entry) with the `name` attribute value and the [submission value](https://html.spec.whatwg.org/multipage/custom-elements.html#face-submission-value), and [append](https://infra.spec.whatwg.org/#list-append) it to entry list.

##### 4.13.7.4 Accessibility semantics[](https://html.spec.whatwg.org/multipage/custom-elements.html#accessibility-semantics)

`internals.role [ = value ]`
Sets or retrieves the default ARIA role for internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target), which will be used unless the page author overrides it using the `role` attribute.

`internals.aria* [ = value ]`
Sets or retrieves various default ARIA states or property values for internals's [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target), which will be used unless the page author overrides them using the `aria-*` attributes.

Each [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) has an internal content attribute map, which is a [map](https://infra.spec.whatwg.org/#ordered-map), initially empty. See the [Requirements related to ARIA and to platform accessibility APIs](https://html.spec.whatwg.org/multipage/dom.html#wai-aria) section for information on how this impacts platform accessibility APIs.

##### 4.13.7.5 Custom state pseudo-class[](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-state-pseudo-class)

`internals.states.add(value)`
Adds the string value to the element's [states set](https://html.spec.whatwg.org/multipage/custom-elements.html#states-set) to be exposed as a pseudo-class.

`internals.states.has(value)`
Returns true if value is in the element's [states set](https://html.spec.whatwg.org/multipage/custom-elements.html#states-set), otherwise false.

`internals.states.delete(value)`
If the element's [states set](https://html.spec.whatwg.org/multipage/custom-elements.html#states-set) has value, then it will be removed and true will be returned. Otherwise, false will be returned.

`internals.states.clear()`
Removes all values from the element's [states set](https://html.spec.whatwg.org/multipage/custom-elements.html#states-set).

`for (const stateName of internals.states)``for (const stateName of internals.states.entries())``for (const stateName of internals.states.keys())``for (const stateName of internals.states.values())`
Iterates over all values in the element's [states set](https://html.spec.whatwg.org/multipage/custom-elements.html#states-set).

`internals.states.forEach(callback)`
Iterates over all values in the element's [states set](https://html.spec.whatwg.org/multipage/custom-elements.html#states-set) by calling callback once for each value.

`internals.states.size`
Returns the number of values in the element's [states set](https://html.spec.whatwg.org/multipage/custom-elements.html#states-set).

Each [custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) has a states set, which is a `CustomStateSet`, initially empty.

```
[Exposed=Window]
interface CustomStateSet {
  setlike<DOMString>;
};
```

The `states` getter steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [target element](https://html.spec.whatwg.org/multipage/custom-elements.html#internals-target)'s [states set](https://html.spec.whatwg.org/multipage/custom-elements.html#states-set).

The [states set](https://html.spec.whatwg.org/multipage/custom-elements.html#states-set) can expose boolean states represented by existence/non-existence of string values. If an author wants to expose a state which can have three values, it can be converted to three exclusive boolean states. For example, a state called `readyState` with `"loading"`, `"interactive"`, and `"complete"` values can be mapped to three exclusive boolean states, `"loading"`, `"interactive"`, and `"complete"`:

```
// Change the readyState from anything to "complete".
this._readyState = "complete";
this._internals.states.delete("loading");
this._internals.states.delete("interactive");
this._internals.states.add("complete");
```

[← 4.12.5 The canvas element](https://html.spec.whatwg.org/multipage/canvas.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.14 Common idioms without dedicated elements →](https://html.spec.whatwg.org/multipage/semantics-other.html)
