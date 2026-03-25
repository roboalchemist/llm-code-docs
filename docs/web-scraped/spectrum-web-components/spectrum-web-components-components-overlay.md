# Source: https://opensource.adobe.com/spectrum-web-components/components/overlay/

Title: Overlay: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/overlay/

Markdown Content:
An `<sp-overlay>` element is used to decorate content that you would like to present to your visitors as "overlaid" on the rest of the application. This includes dialogs (modal and not), pickers, tooltips, context menus, et al.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/overlay?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/overlay?style=for-the-badge)

yarn add @spectrum-web-components/overlay
Import the side effectful registration of `<sp-overlay>` as follows:

import '@spectrum-web-components/overlay/sp-overlay.js';
When looking to leverage the `Overlay` base class as a type and/or for extension purposes, do so via:

import { Overlay } from '@spectrum-web-components/overlay';
By leveraging the `trigger` attribute to pass an ID reference to another element within the same DOM tree, your overlay will be positioned in relation to this element. When the ID reference is followed by an `@` symbol and interaction type, like `click`, `hover`, or `longpress`, the overlay will bind itself to the referenced element via the DOM events associated with that interaction.

<sp-button id="trigger">Overlay Trigger</sp-button>

<sp-overlay trigger="trigger@click" placement="bottom">
  <sp-popover>
    <sp-dialog>
      <h2 slot="heading">Clicking opens this popover...</h2>
      <p>But, it really could be anything. Really.</p>
    </sp-dialog>
  </sp-popover>
</sp-overlay>

<sp-overlay trigger="trigger@hover" placement="bottom">
  <sp-tooltip>
    I'm a tooltip and I'm triggered by hovering over the button!
  </sp-tooltip>
</sp-overlay>
When a `<sp-overlay>` element is opened, it will pass that state to its direct children elements as the property `open`, which it will set to `true`. Elements should react to this by initiating any transition between closed and open that they see fit. Similarly, `open` will be set to `false` when the `<sp-overlay>` element is closed.

delayed
An Overlay that is `delayed` will wait until a warm-up period of 1000ms has completed before opening. Once the warmup period has completed, all subsequent Overlays will open immediately. When no Overlays are opened, a cool down period of 1000ms will begin. Once the cool down has completed, the next Overlay to be opened will be subject to the warm-up period if provided that option.

<sp-button id="trigger">Overlay Trigger</sp-button>

<sp-overlay trigger="trigger@hover" placement="bottom" delayed>
  <sp-tooltip>I'm a tooltip and I'm delayed!</sp-tooltip>
</sp-overlay>notImmediatelyCloseable
When an Overlay is `notImmediatelyCloseable` that means that the first interaction that would lead to the closure of the Overlay in question will be ignored. This is useful when working with non-"click" mouse interactions, like `contextmenu`, where the trigger event (e.g. `contextmenu`) occurs _before_ an event that would close said overlay (e.g. `pointerup`).

<style> #root { position: relative; width: 100%; height: 20vh; background-color: var(--spectrum-gray-100); border: 1px solid var(--spectrum-gray-400); }</style>

<p>Right click anywhere in bounded rectangle to open the menu</p>
<div id="root">
    <sp-overlay offset="0" type="auto" placement="right-start" >
        <sp-popover style="width:300px;">
            <sp-menu>
                <sp-menu-group>
                    <span slot="header">Menu</span>
                    <sp-menu-item>Deselect</sp-menu-item>
                    <sp-menu-item>Select inverse</sp-menu-item>
                    <sp-menu-item>Feather...</sp-menu-item>
                    <sp-menu-item>Select and mask...</sp-menu-item>
                    <sp-menu-divider></sp-menu-divider>
                    <sp-menu-item>Save selection</sp-menu-item>
                    <sp-menu-item disabled>Make work path</sp-menu-item>
                </sp-menu-group>
            </sp-menu>
        </sp-popover>
    </sp-overlay>
</div>

<script type="module"> import { VirtualTrigger } from '@spectrum-web-components/overlay'; const init = () => { const overlay = document.querySelector('sp-overlay'); const popover = overlay.querySelector('sp-popover'); overlay.triggerElement = new VirtualTrigger(0, 0); popover.addEventListener('change', (event) => { event.target.dispatchEvent(new Event('close', { bubbles: true })); }); const handleContextmenu = async (event) => { event.preventDefault(); event.stopPropagation(); if (overlay.triggerElement instanceof VirtualTrigger) { overlay.triggerElement.updateBoundingClientRect( event.clientX, event.clientY ); } overlay.willPreventClose = true; overlay.open = true; }; const root = document.getElementById('root'); root.addEventListener('contextmenu', handleContextmenu, { capture: true }); } customElements.whenDefined('code-example').then(() => { Promise.all([...document.querySelectorAll('code-example')].map(example => example.updateComplete)).then(() => { init(); }); });</script>offset
The `offset` property accepts either a single number, to define the offset of the Overlay along the main axis from the trigger, or 2-tuple, to define the offset along the main axis and the cross axis. This option has no effect when there is no trigger element.

<sp-button id="trigger">Overlay Trigger</sp-button>

<sp-overlay trigger="trigger@click" placement="bottom" offset="50">
  <sp-popover>
    <sp-dialog>
      <h2 slot="heading">Clicking opens this popover...</h2>
      <p>An offset of 50px is applied to the overlay.</p>
    </sp-dialog>
  </sp-popover>
</sp-overlay>placement
A `placement` of `"auto-start" | "auto-end" | "top" | "bottom" | "right" | "left" | "top-start" | "top-end" | "bottom-start" | "bottom-end" | "right-start" | "right-end" | "left-start" | "left-end"` will instruct the Overlay where to place itself in relationship to the trigger element.

<sp-button id="trigger">Overlay Trigger</sp-button>

<sp-overlay trigger="trigger@click" placement="right-start">
  <sp-popover>
    <sp-dialog>
      <h2 slot="heading">Clicking opens this popover...</h2>
      <p>The overlay is placed to the right of the trigger.</p>
    </sp-dialog>
  </sp-popover>
</sp-overlay>receivesFocus
Some Overlays will always be passed focus (e.g. modal or page Overlays). When this is not true, the `receivesFocus` option will inform the API whether to attempt to pass focus into the Overlay once it is open. `'true'` will pass focus, `'false'` will not (when possible), and `"auto"` (the default), will make a decision based on the `type` of the Overlay.

<sp-button id="trigger">Overlay Trigger</sp-button>

<sp-overlay trigger="trigger@click" placement="bottom" receives-focus="false">
  <sp-popover>
    <sp-dialog>
      <h2 slot="heading">
        Clicking opens this popover but does not receive focus
      </h2>
      <sp-field-label>Enter your email</sp-field-label>
      <sp-textfield placeholder="test@gmail.com"></sp-textfield>
      <sp-action-button onClick=" this.dispatchEvent( new Event('close', { bubbles: true, composed: true, }) ); " >
        Sign in
      </sp-action-button>
    </sp-dialog>
  </sp-popover>
</sp-overlay>
The `trigger` attribute accepts a string ID reference for the trigger element combined with the interaction type.

The format is `"elementId@interaction"`, where:

*   `elementId` is the ID of the HTML element to use as the trigger
*   `interaction` is required and can be `click`, `hover`, or `longpress`

Examples:

<sp-button id="my-button">Open Overlay</sp-button>

<sp-overlay trigger="my-button@click" placement="top-start">
  <sp-popover>Click popover</sp-popover>
</sp-overlay>

<sp-overlay trigger="my-button@hover" placement="right-start">
  <sp-popover>Hover popover</sp-popover>
</sp-overlay>

<sp-overlay trigger="my-button@longpress" placement="bottom-start">
  <sp-popover>Longpress popover</sp-popover>
</sp-overlay>
The `triggerElement` property accepts an `HTMLElement` or a `VirtualTrigger` from which to position the Overlay.

*   You can import the `VirtualTrigger` class from the overlay package to create a virtual trigger that can be used to position an Overlay. This is useful when you want to position an Overlay relative to a point on the screen that is not an element in the DOM, like the mouse cursor.

The `type` of an Overlay outlines a number of things about the interaction model within which it works:

Modal
`'modal'` Overlays create a modal context that traps focus within the content and prevents interaction with the rest of the page. The overlay manages focus trapping and accessibility features like `aria-modal="true"` to ensure proper screen reader behavior.

They should be used when you need to ensure that the user has interacted with the content of the Overlay before continuing with their work. This is commonly used for dialogs that require a user to confirm or cancel an action before continuing.

<sp-button id="trigger">open modal</sp-button>
<sp-overlay trigger="trigger@click" type="modal">
  <sp-dialog-wrapper headline="Signin form" dismissable underlay>
    <p>I am a modal type overlay.</p>
    <sp-field-label>Enter your email</sp-field-label>
    <sp-textfield placeholder="test@gmail.com"></sp-textfield>
    <sp-action-button onClick=" this.dispatchEvent( new Event('close', { bubbles: true, composed: true, }) ); " >
      Sign in
    </sp-action-button>
  </sp-dialog-wrapper>
</sp-overlay>Page
`'page'` Overlays behave similarly to `'modal'` Overlays by creating a modal context and trapping focus, but they will not be allowed to close via the "light dismiss" algorithm (e.g. the Escape key).

A page overlay could be used for a full-screen menu on a mobile website. When the user clicks on the menu button, the entire screen is covered with the menu options.

<sp-button id="trigger">open page</sp-button>
<sp-overlay trigger="trigger@click" type="page">
  <sp-dialog-wrapper headline="Full screen menu" mode="fullscreenTakeover" cancel-label="Close" >
    <p>I am a page type overlay.</p>
  </sp-dialog-wrapper>
</sp-overlay>Hint
`'hint'` Overlays are much like tooltips so they are not just ephemeral, but they are delivered primarily as a visual helper and exist outside of the tab order. In this way, be sure _not_ to place interactive content within this type of Overlay.

This overlay type does not accept focus and does not interfere with the user's interaction with the rest of the page.

<sp-button id="trigger">open hint</sp-button>
<sp-overlay trigger="trigger@hover" type="hint">
  <sp-tooltip>
    I am a hint type overlay. I am not interactive and will close when the user
    interacts with the page.
  </sp-tooltip>
</sp-overlay>Auto
`'auto'` Overlays provide a place for content that is ephemeral _and_ interactive. These Overlays can accept focus and remain open while interacting with their content. They will close when focus moves outside the overlay or when clicking elsewhere on the page.

<sp-button id="trigger">Open Overlay</sp-button>
<sp-overlay trigger="trigger@click" type="auto" placement="bottom">
  <sp-popover dialog>
    <p>
      My slider in overlay element:
      <sp-slider label="Slider Label - Editable" editable></sp-slider>
    </p>
  </sp-popover>
</sp-overlay>Manual
`'manual'` Overlays act much like `'auto'` Overlays, but do not close when losing focus or interacting with other parts of the page.

Note: When a `'manual'` Overlay is at the top of the "overlay stack", it will still respond to the Escape key and close.

<style> .chat-container { position: fixed; bottom: 1em; left: 1em; }</style>
<sp-button id="trigger">open manual</sp-button>
<sp-overlay trigger="trigger@click" type="manual">
  <sp-popover class="chat-container">
    <sp-dialog dismissable>
      <span slot="heading">Chat Window</span>
      <sp-textfield placeholder="Enter your message"></sp-textfield>
      <sp-action-button>Send</sp-action-button>
    </sp-dialog>
  </sp-popover>
</sp-overlay>
When fully open the `<sp-overlay>` element will dispatch the `sp-opened` event, and when fully closed the `sp-closed` event will be dispatched. Both of these events are of type:

type OverlayStateEvent = Event & {
  overlay: Overlay;
};
The `overlay` value in this case will hold a reference to the actual `<sp-overlay>` that is opening or closing to trigger this event. Remember that some `<sp-overlay>` element (like those creates via the imperative API) can be transiently available in the DOM, so if you choose to build a cache of Overlay elements to some end, be sure to leverage a weak reference so that the `<sp-overlay>` can be garbage collected as desired by the browser.

"Fully" in this context means that all CSS transitions that have dispatched `transitionrun` events on the direct children of the `<sp-overlay>` element have successfully dispatched their `transitionend` or `transitioncancel` event. Keep in mind the following:

*   `transition*` events bubble; this means that while transition events on light DOM content of those direct children will be heard, those events will not be taken into account
*   `transition*` events are not composed; this means that transition events on shadow DOM content of the direct children will not propagate to a level in the DOM where they can be heard

This means that in both cases, if the transition is meant to be a part of the opening or closing of the overlay in question you will need to re-dispatch the `transitionrun`, `transitionend`, and `transitioncancel` events from that transition from the closest direct child of the `<sp-overlay>`.

<style> .overlay-demo-popover sp-action-group { padding: var(--spectrum-actiongroup-vertical-spacing-regular); } #overlay-demo { position: static; } #overlay-demo:not(:defined), #overlay-demo *:not(:defined) { display: none; }</style>
<sp-popover id="overlay-demo" class="overlay-demo-popover" open>
  <sp-action-group vertical quiet emphasized selects="single">
    <sp-action-button id="trigger-1" hold-affordance>
      <sp-icon-anchor-select slot="icon"></sp-icon-anchor-select>
    </sp-action-button>
    <sp-action-button id="trigger-2" hold-affordance>
      <sp-icon-polygon-select slot="icon"></sp-icon-polygon-select>
    </sp-action-button>
    <sp-action-button id="trigger-3" hold-affordance>
      <sp-icon-rect-select slot="icon"></sp-icon-rect-select>
    </sp-action-button>
  </sp-action-group>
  <sp-overlay trigger="trigger-1@hover" type="hint">
    <sp-tooltip>Hover</sp-tooltip>
  </sp-overlay>
  <sp-overlay trigger="trigger-1@longpress" type="auto" placement="right-start">
    <sp-popover class="overlay-demo-popover" tip>
      <sp-action-group vertical quiet>
        <sp-action-button>
          <sp-icon-anchor-select slot="icon"></sp-icon-anchor-select>
        </sp-action-button>
        <sp-action-button>
          <sp-icon-polygon-select slot="icon"></sp-icon-polygon-select>
        </sp-action-button>
        <sp-action-button>
          <sp-icon-rect-select slot="icon"></sp-icon-rect-select>
        </sp-action-button>
      </sp-action-group>
    </sp-popover>
  </sp-overlay>
  <sp-overlay trigger="trigger-2@hover" type="hint">
    <sp-tooltip>Hover</sp-tooltip>
  </sp-overlay>
  <sp-overlay trigger="trigger-2@longpress" type="auto" placement="right-start">
    <sp-popover class="overlay-demo-popover" tip>
      <sp-action-group vertical quiet>
        <sp-action-button>
          <sp-icon-anchor-select slot="icon"></sp-icon-anchor-select>
        </sp-action-button>
        <sp-action-button>
          <sp-icon-polygon-select slot="icon"></sp-icon-polygon-select>
        </sp-action-button>
        <sp-action-button>
          <sp-icon-rect-select slot="icon"></sp-icon-rect-select>
        </sp-action-button>
      </sp-action-group>
    </sp-popover>
  </sp-overlay>
  <sp-overlay trigger="trigger-3@hover" type="hint">
    <sp-tooltip>Hover</sp-tooltip>
  </sp-overlay>
  <sp-overlay trigger="trigger-3@longpress" type="auto" placement="right-start">
    <sp-popover class="overlay-demo-popover" tip>
      <sp-action-group vertical quiet>
        <sp-action-button>
          <sp-icon-anchor-select slot="icon"></sp-icon-anchor-select>
        </sp-action-button>
        <sp-action-button>
          <sp-icon-polygon-select slot="icon"></sp-icon-polygon-select>
        </sp-action-button>
        <sp-action-button>
          <sp-icon-rect-select slot="icon"></sp-icon-rect-select>
        </sp-action-button>
      </sp-action-group>
    </sp-popover>
  </sp-overlay>
</sp-popover><sp-overlay
    ?open=${boolean}
    ?delayed=${boolean}
    offset=${Number | [Number, Number]}
    placement=${Placement}
    receives-focus=${'true' | 'false' | 'auto' (default)
    trigger=${string | ${string}@${string}}
    .triggerElement=${HTMLElement | VirtualTrigger}
    .triggerInteraction=${'click' | 'longpress' | 'hover'}
    type=${'auto' | 'hint' | 'manual' | 'modal' | 'page'}
    ?allow-outside-click=${boolean}
></sp-overlay>
When a `triggerElement` is present (via `trigger` attribute or direct property setting), the following configurations apply:

Configuration Required Properties Behavior Basic Placement`placement` + `triggerElement`Content positions next to trigger Placement + Offset`placement` + `offset` + `triggerElement`Content positions with extra spacing Invalid Placement`placement` without `triggerElement`No positioning occurs No Placement No `placement` specified Content positioning handled by: • Content itself • Application 
Common in `modal`/`page` overlays for full-screen content

> **⚠️ Deprecation Notice**: The `allow-outside-click` property is deprecated and will be removed in a future version.

The `allow-outside-click` property allows clicks outside the overlay to close it. **We do not recommend using this property for accessibility reasons** as it can cause unexpected behavior and accessibility issues. When set to `true`, it configures the focus trap to allow outside clicks, which may interfere with proper focus management and user expectations.

<sp-overlay trigger="trigger@click" allow-outside-click="true">
  <sp-popover>
    <p>This overlay can be closed by clicking outside</p>
  </sp-popover>
</sp-overlay>
**Alternative approaches**: Instead of using `allow-outside-click`, consider implementing explicit close buttons or using the `type="modal"` or `type="page"` overlay types which provide better accessibility and user experience.

`<sp-overlay>` element will use the `<dialog>` element or `popover` attribute to project your content onto the top-layer of the browser, without being moved in the DOM tree. That means that you can style your overlay content with whatever techniques you are already leveraging to style the content that doesn't get overlaid. This means standard CSS selectors, CSS Custom Properties, and CSS Parts applied in your parent context will always apply to your overlaid content.

There are some complex CSS values that have not yet been covered by the positioning API that the `<sp-overlay>` element leverages to associate overlaid content with their trigger elements. In specific, properties like `filter`, when applied to a trigger element within which lives the related content to be overlaid, are not currently supported by the relationship created herein. If support for this is something that you and the work you are addressing would require, we'd love to hear from you in an issue. We'd be particularly interested in speaking with you if you were interested in contributing support/testing to ensure this capability for all consumers of the library.

While the `<dialog>` element is widely supported by browsers, the `popover` attribute is still quite new. When leveraged in browsers that do not yet support the `popover` attribute, there may be additional intervention required to ensure your content is delivered to your visitors as expected.

When an overlay is placed within a page with complex layering, the content therein can fall behind other content in the `z-index` stack. The following example is somewhat contrived but, imagine a toolbar next to a properties panel. If the toolbar has a lower `z-index` than the properties panel, any overlaid content (tooltips, etc.) within that toolbar will display underneath any content in the properties panel with which it may share pixels.

<div class="complex-layered-demo">
  <div class="complex-layered-holder">
    <sp-action-button id="complex-layered">Trigger</sp-action-button>
    <sp-overlay trigger="complex-layered@hover" type="hint" placement="bottom-start" >
      <sp-tooltip>
        I can be partially blocked when [popover] is not available
      </sp-tooltip>
    </sp-overlay>
  </div>
  <div class="complex-layered-blocker"></div>
</div>
<style> .complex-layered-demo { position: relative; } .complex-layered-holder { z-index: 1; position: relative; } .complex-layered-blocker { position: relative; z-index: 10; background: white; width: 100%; height: 40px; }</style>
Properly managed `z-index` values will support working around this issue while browsers work to adopt the `popover` attribute. In this demo, you can achieve the same output by sharing one `z-index` between the various pieces of content, removing `z-index` values altogether, or raising the `.complex-layered-holder` element to a higher `z-index` than the `.complex-layered-blocker` element.

CSS Containment gives a developer direct control over how the internals of one element affect the paint and layout of the internals of other elements on the same page. While leveraging some of its values can offer performance gains, they can interrupt the delivery of your overlaid content.

<div class="contained-demo">
  <sp-action-button id="contained">Trigger</sp-action-button>
  <sp-overlay trigger="contained@hover" type="hint" placement="bottom-start">
    <sp-tooltip>I can be blocked when [popover] is not available</sp-tooltip>
  </sp-overlay>
</div>
<style> .contained-demo { contain: content; }</style>
You could just _remove_ the `contain` rule. But, if you are not OK with simply removing the `contain` value, you still have options. If you would like to continue to leverage `contain`, you can place your "contained" content separately from your overlaid content, like so:

<div class="contained-demo">
  <sp-action-button id="contained-working">Trigger</sp-action-button>
</div>
<sp-overlay trigger="contained-working@hover" type="hint" placement="bottom-start">
  <sp-tooltip>I can be blocked when [popover] is not available</sp-tooltip>
</sp-overlay>
<style> .contained-demo { contain: content; }</style>
`<sp-overlay>` accepts an ID reference via the `trigger` attribute to relate it to interactions and positioning in the DOM. To fulfill this reference the two elements need to be in the same DOM tree. However, `<sp-overlay>` alternatively accepts a `triggerElement`_property_ that opens even more flexibility in addressing this situation.

`clip-path` can also restrict how content in an element is surfaced at paint time. When overlaid content should display outside of the `clip-path`, without the `popover` attribute, that content could be _clipped_.

<div class="clip-pathed-demo">
  <sp-action-button id="clip-pathed">Trigger</sp-action-button>
  <sp-overlay trigger="clip-pathed@hover" type="hint" placement="bottom-start">
    <sp-tooltip>I can be blocked when [popover] is not available</sp-tooltip>
  </sp-overlay>
</div>
<style> .clip-pathed-demo { clip-path: inset(0 0); }</style>
Here, again, working with your content needs (whether or not you want to leverage `clip-path`) or DOM structure (not colocating clipped and non-clipped content) will allow you to avoid this issue:

<div class="clip-pathed-demo">
  <sp-action-button id="clip-pathed-working">Trigger</sp-action-button>
</div>
<sp-overlay trigger="clip-pathed-working@hover" type="hint" placement="bottom-start">
  <sp-tooltip>I can be blocked when [popover] is not available</sp-tooltip>
</sp-overlay>
<style> .clip-pathed-demo { clip-path: inset(0 0); }</style>
Under very specific conditions, WebKit will incorrectly clip fixed-position content. WebKit clips `position: fixed` elements within containers that have all of:

1.   `position: relative`
2.   `overflow: clip` or `overflow: hidden`
3.   `z-index` greater than zero

If you notice overlay clipping _only_ in Safari, this is likely the culprit. The solution is to break up the conditions into separate elements to avoid triggering WebKit's bug. For example, leaving relative positioning and z-index on the outermost container while creating an inner container that enforces the overflow rules.

When nesting multiple overlays, it is important to ensure that the nested overlays are actually nested in the HTML as well, otherwise it will not be accessible.

<div style="padding: 20px;">
  <sp-button id="outerTrigger" variant="primary" aria-haspopup="dialog">
    Open Outer Modal
  </sp-button>
  <sp-overlay id="outerOverlay" type="auto" trigger="outerTrigger@click">
    <sp-popover>
      <sp-dialog>
        <h2 slot="heading" id="outer-dialog-heading">Outer Dialog</h2>
        <p>This is the outer modal content. Press ESC to close it.</p>
        <sp-button id="innerTrigger" variant="primary" aria-haspopup="dialog">
          Open Inner Modal
        </sp-button>
        <sp-overlay id="innerOverlay" type="auto" trigger="innerTrigger@click">
          <sp-popover>
            <sp-dialog>
              <h2 slot="heading" id="inner-dialog-heading">Inner Dialog</h2>
              <p>
                This is the inner modal content. Press ESC to close this first,
                then the outer modal.
              </p>
            </sp-dialog>
          </sp-popover>
        </sp-overlay>
      </sp-dialog>
    </sp-popover>
  </sp-overlay>
</div>
The overlay manages focus based on its type:

*   For `modal` and `page` types, focus is always trapped within the overlay
*   For `auto` and `manual` types, focus behavior is controlled by the `receives-focus` attribute
*   For `hint` type, focus remains on the trigger element

Example of proper focus management:

<sp-button id="modal-trigger" aria-haspopup="dialog" aria-expanded="false">
  Open Settings
</sp-button>
<sp-overlay trigger="modal-trigger@click" type="modal">
  <sp-dialog-wrapper headline="Settings" dismissable underlay aria-labelledby="settings-heading" >
    <h2 id="settings-heading" slot="heading">Settings</h2>
    <sp-field-label for="setting1">Email Notifications</sp-field-label>
    <sp-switch id="setting1">Enable notifications</sp-switch>

    <div slot="footer">
      <sp-button variant="secondary" onclick="this.dispatchEvent(new Event('close', { bubbles: true }))" >
        Cancel
      </sp-button>
      <sp-button variant="accent" onclick="this.dispatchEvent(new Event('close', { bubbles: true }))" >
        Save
      </sp-button>
    </div>
  </sp-dialog-wrapper>
</sp-overlay>Key Action ESC Closes overlays in reverse order of opening TAB/Shift+TAB Navigates through focusable elements within modal/page overlays Arrow keys Navigate through menu items in menu overlays ENTER/SPACE Activates buttons and controls
*   Use `aria-haspopup` on trigger elements to indicate the type of overlay
*   Provide descriptive labels using `aria-label` or `aria-labelledby`
*   Use proper heading structure within overlays
*   Ensure error messages are announced using `aria-live`

Example of a tooltip with proper screen reader support:

<sp-button id="help-trigger" aria-describedby="help-tooltip" label="Help">
  <sp-icon-help slot="icon"></sp-icon-help>
</sp-button>
<sp-overlay trigger="help-trigger@hover" type="hint">
  <sp-tooltip id="help-tooltip">
    Click for more information about this feature
  </sp-tooltip>
</sp-overlay>

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/theme@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/action-button@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/theme@1.11.1
    *   @spectrum-web-components/action-button@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   #5873`02b2d7d` Thanks @TarunAdobe! - Fixes overlay trigger directive behavior when used with Lit's `cache()` directive. When the trigger element is disconnected and reconnected (as happens with `cache()`), the directive now properly cleans up and recreates the overlay state. On disconnect, the overlay is closed, removed from the DOM, and its reference is cleared from the strategy. This ensures that when the trigger reconnects, a fresh overlay will be created on the next open, preventing stale state and console errors.

*   #5868`f07344f` Thanks @Rajdeepc! - **Fixed** issue where picker menus inside overlays could not scroll to the bottom after selecting an item and reopening. The problem was caused by the overlay's placement calculation happening before the menu fully rendered, resulting in incorrect height measurements.

This fix ensures picker menus maintain proper scrollable height when reopened, regardless of the selected item's position.

*   #5893`1d76b70` Thanks @majornista! - hover overlays should close with the Esc key when trigger is not focused

*   #5907`cadc39e` Thanks @Rajdeepc! - **Fixed**: Modal overlays now properly close when clicking the backdrop, while page overlays correctly remain blocking.

The `modal-backdrop` click handler now correctly distinguishes between overlay types:

    *   Modal overlays close on backdrop click (light dismiss behavior)
    *   Page overlays remain blocking and do not close on backdrop click

*   #5964`4cb0b7b` Thanks @rubencarvalho! - **Fixed**: Third-level submenus now open correctly on Safari. Simplified the WebKit layout timing fix in `computePlacement()` to ensure consistent overlay positioning for deeply nested menus.

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]:

    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/theme@1.11.0
    *   @spectrum-web-components/action-button@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/action-button@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/theme@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   #5806`a19cbe3` Thanks @rubencarvalho! - - **Fixed**: Expanded `<overlay-trigger>``type` property to accept all overlay types ('auto', 'hint', 'manual', 'modal', 'page') instead of the incorrect, previous restricted subset.

*   Updated dependencies []:

    *   @spectrum-web-components/action-button@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1
    *   @spectrum-web-components/theme@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/action-button@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0
    *   @spectrum-web-components/theme@1.9.0

*   #5670`14486d6` Thanks @Rajdeepc! - Added `allow-outside-click` property to `<sp-overlay>` with deprecation notice. This property allows clicks outside the overlay to close it, but is not recommended for accessibility reasons and will be removed in a future version.

This property is being added as deprecated to support the fallback for `showModal()` which was removed as part of performance optimization. We will no longer support outside clicks for modal overlays as they violate accessibility guidelines.

The property defaults to `false` and shows deprecation warnings when used. Consider using explicit close buttons or modal/page overlay types instead for better accessibility.

*   #5710`ee1bae6` Thanks @Rajdeepc! - **Fixed** : Added body scroll prevention for modal and page overlays. Overlay automatically blocks body scroll when modal or page overlays are open and restores the original scroll state when they are closed, improving user experience and accessibility for modal dialogs.

*   #5670`14486d6` Thanks @Rajdeepc! - **Fixed** : external click registration behavior in the `sp-overlay` component. Programmatic clicks on elements outside of modal overlays now properly register and close the overlay, while user-initiated clicks are prevented from doing so.

*   Updated dependencies []: 
    *   @spectrum-web-components/theme@1.8.0
    *   @spectrum-web-components/action-button@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   #5477`a646ae8` Thanks @Rajdeepc! - **Fixed** : Overlays (like pickers and action menus) were incorrectly closing when scrolling occurred within components. The fix ensures the `handleScroll` method in `OverlayStack` only responds to document/body scrolling events and ignores component-level scrolling events, which was the original intention.

*   Updated dependencies [`c1669d2`]: 
    *   @spectrum-web-components/action-button@1.7.0
    *   @spectrum-web-components/theme@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   #5392`53f3769` Thanks @TarunAdobe! - Fixed layout issues in Safari when an `sp-tray` is nested inside a dialog-type `sp-overlay`.

*   Updated dependencies []:

    *   @spectrum-web-components/action-button@1.6.0
    *   @spectrum-web-components/theme@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5308`8f8735c` Thanks @Rajdeepc! - prevent overlay close on document scroll

*   Updated dependencies [`6c58f50`]: 
    *   @spectrum-web-components/action-button@1.5.0
    *   @spectrum-web-components/theme@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   #5223`46cd782` Thanks @Rajdeepc! - Removed pointer-events:none from the slot-trigger under overlay-trigger to disable the overlay content and not the trigger element.

*   #5248`70f5f6f` Thanks @Rajdeepc! - overlay type auto stays open when interacting with elements inside

*   Updated dependencies [`72dbe62`]: 
    *   @spectrum-web-components/action-button@1.4.0
    *   @spectrum-web-components/theme@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   #5176`468314f` Thanks @TarunAdobe! - 1. chore(checkbox): updated to latest css v10.1.1 for s2 fast follow 2. chore(dialog): The error property was not properly deprecated with a full migration plan in place. This has caused confusion and false sense of urgency for consumers to migrate. We are removing it to eliminate those pain points for consumers while we take a deep look at our dialogs and patterns. 3. chore(menu): updated to latest css v9.1.1 for s2 fast follow 4. fix(overlay): sp-overlay with type="manual" should close on pressing ESC key. When the last item is on overlay stack we are triggering the close method on esc key event.

*   Updated dependencies [`ea38ef0`]:

    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/action-button@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0
    *   @spectrum-web-components/theme@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **action menu:** keyboard accessibility omnibus (#5031) (ea38ef0), closes #4623

*   **overlay:** add triggeredBy property to overlay-trigger for performance optimization (#5046) (fd504aa)

*   **picker:** stop the click events from reaching the elements below picker-tray (#5060) (7e4fdbf)

*   **overlay:** make :focus-visible consistent when using overlay type modal (#4912) (7a5f786), closes #5021

*   **overlay:** make :focus-visible consistent when using overlay type modal (#4912) (7a5f786), closes #5021

*   add an optional chromatic vrt action (7d2f840)
*   **picker:** add forcePopover property (#5041) (3651e57)

*   **overlay:** overlay scroll in safari and firefox (#4969) (05d24ff)

*   **overlay:** ensure smooth animation when opening modal overlays (#4879) (cd8dad7)
*   **overlay:** overlay closing another overlay (#4880) (30434fa)
*   **overlay:** remove flex display for dialog (#4902) (48448ea)

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **breadcrumbs:** add Breadcrumbs component (#4578) (acd4b5e)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay** replace at() polyfill (#4628) (8cef2c6) **Note:** Version bump only for package @spectrum-web-components/overlay

*   **coachmark,overlay:** adjust imports of overlay and coachmark (#4455) (39706da)
*   **overlay:** ensure hint Overlays within shadow roots open as expected (#4443) (7dd64b9)
*   **overlay:** ensure that passing "open" to the directive manages a single strategy (#4474) (15d6ac7)
*   **overlay:** persist "host" in directive rendered Overlay content (#4475) (5d189c2)

*   **action-menu:** allow menu groups to handle their own selections (#4397) (5a19051)
*   **base:** move lit imports to base (#4416) (b7cb07e)
*   **overlay:** prevent "receivesFocus=false" overlays from returning focus (607819f)
*   **slider,overlay:** ensure that pointer events in Slider are handled as expected in Overlay (#4438) (db193e8)
*   **styles,theme:** add S2 tokens and theme (#4241) (a29e4a2), closes #4232#4228
*   **theme:** deprecate `theme` property for `system` (#4230) (ac26168)

*   **overlay:** prevent "receivesFocus=false" overlays from returning focus (607819f)
*   **theme:** deprecate `theme` property for `system` (#4230) (ac26168)

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** prevent focus based hover interaction without :focus-visible (79337ff)
*   **overlay:** prioritize non-"hint" Overlays on the same trigger (b9833f3)
*   **picker:** add loading state to the picker (#3110) (d91e2c9)
*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)

*   **overlay:** ensure "manual" Overlays ignore "light dismiss" when [popover] is not supported (#4121) (eb5e1ad)
*   **overlay:** leverage "transition-behavior" to persist top-layer content while closing (#4050) (e3dea14)
*   **slider:** double click on slider handle to reset slider position (#3991) (64c594a)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   support generating random IDs outside of secure contexts (485a67c)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** clean position data on close (edac590)

*   **overlay:** automatically reposition overlay when the contents resize (83be807)
*   **overlay:** move closed overlays to "display: none" (fc0278b)
*   **overlay:** normalize popover toggling between native and synthetic [popover] usage (26fa692)
*   **overlay:** support positioning overlays within parents leveraging container-type rules (21044b3)
*   **overlay:** surface "overlay" property to "sp-opened" and "sp-closed" events (957f8e9)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** ensure events are only bound once (abe57ce)

*   **overlay:** ensure manual overlays persist through interactions outside of their subtree (#3788) (ef5617f)

*   **overlay:** add delay resolution from overlaid content (#3748) (5c4f1f6)
*   **overlay:** calculate more transforms (6538a45)
*   **overlay:** place longpress helper content in a more accessible, less layout affecting location (dd12c23)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** allow overlay to persist on hover (#3706) (7707040)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** allow "receives-focus" to target the root of an overlay (#3658) (0db1025)
*   **overlay:** ensure position when closing overlays over the top-layer (55fab0d)
*   **overlay:** reduce circular dependencies (25eeb71)

*   **action-menu:** added static attribute support (#3573) (25889a8)
*   **overlay:** position for transformed and contained parents (ca8fd8a)

*   address margin effected positioning (38c8cf2)
*   ensure submenus stay open when root it clicked again (83ced1c)
*   handle longpress and over filter overlays (483e52d)

*   **overlay:** ship Overlay API v2 (67b5d1b)

*   make lots of things lazy (b8fa3ad)
*   open/close timing update (d4ebcd3)

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** ensure CSS calcs resolve to the expected measurement value (51a3feb)

*   **popover:** use core tokens (68328cc)

*   **overlay:** address review comments (dd8b985)
*   **overlay:** removes use of px units in overlay stack (122f96c)
*   **overlay:** stop the tab trapping if shadow root is not found (4f0ec46)

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)
*   add content flow fallbacks to the position manager (c008957)
*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)
*   allow contextmenu event passing to pierce shadow roots (05b69e9)
*   allow detached elements to be used as content for an overlay (3ad8383)
*   allow Picker to be reparented (39e7309)
*   centralize updated first focusable selector (300e84c)
*   close modal overlays with contextmenu events and pass those to the underlying page (9e83f3c)
*   constrain overlay to available window size (9729b55)
*   correct @element jsDoc listing across library (c97a632)
*   correct add/remove timing of overlay events (474ec6e)
*   correct overlay closure order or operations for manual override (0b7a8c4)
*   correct the relationship between overlayWillCloseCallback and phased animations (c63db8d)
*   delete the used cleanup method (942ef0f)
*   describe longpress button to screen readers (acdcaf4)
*   **dialog:** updates for delivering dialog content accessibly (f0ed33c)
*   **dropdown:** correct conditional check (a3a790f)
*   ensure browser understandable extensions (f4e59f7)
*   ensure focus is managed when tabbing out of a menu (9bfa81d)
*   ensure Overlay.update bypasses the auto close mechanism (8f2aa2e)
*   ensure that an overlay can be released even if it does not complete its fade in animation (4cbb36f)
*   ensure that entering an ancestor Menu Item without a submen closes related submenus (efe5fa1)
*   expand sync offering for elements with overlay content (0195843)
*   include default export in the "exports" fields (f32407d)
*   include sync builds in publication configuration (e731673)
*   include the "types" entry in package.json files (b432f59)
*   keep parent overlays open when not closing child hover overlays (643fcff)
*   leverage "dvh" rather than measured screen height (84b9df0)
*   manage "lang" via context provided by "sp-theme" (b1e3457)
*   **menu:** add support for submenu interactions (68399af)
*   **overlay:** add overlay lifecycle methods to stack management (9361527)
*   **overlay:** allow [type="modal"] hover overlays to be closed (5a6802b)
*   **overlay:** allow external style access to "sp-theme" elements in overlays as a CSS part (a107f66)
*   **overlay:** allow overlay-trigger to declaratively open overlay content (194a44e)
*   **overlay:** close when overlay-trigger becomes [disabled] (6f27e25)
*   **overlay:** correct overlay content sizing (d9bcd6f)
*   **overlay:** do not focus the trigger when closing an overlay, unless expected (21d7dfe)
*   **overlay:** enforce the full frame (63628e9)
*   **overlay:** ensure overlay addition occurs after closing previous (7d2b102)
*   **overlay:** ensure undefined data is not passed into theme (3e2e1ca)
*   **overlay:** export OverlayTriggerInteractions type (4caec7f)
*   **overlay:** extend state machine to manage disposal process (f0f26af)
*   **overlay:** focus closure action on ancestor scroll, not participant resize (925af0a)
*   **overlay:** handle hover/longpress more directly via the "open" attribute (7b2b64b)
*   **overlay:** init tab trapping on OverlayStack construction (a3121e3)
*   **overlay:** measure initial overlay data offscreen (fecda5a)
*   **overlay:** move "escape" listener to "keydown" (813b341)
*   **overlay:** new popper version tracks scroll through assigned slots (ea2bac4)
*   **overlay:** only "tab trap" when you mean to (74e1bd2)
*   **overlay:** override SpectrumCSS tip rules and process usage in popper (aad3dec)
*   **overlay:** persist hover overlay when there is not click content (27111a9)
*   **overlay:** place return focus element on demand (d262237)
*   **overlay:** reduce DOM and use of "display: contents" for simplicity and accessibility (2e02075)
*   **overlay:** reduce the control active-overlay places on its content (9d12571)
*   **overlay:** remove trapped content from a11y tree, manage focus, open projected content (6c496c0)
*   **overlay:** remove unused dependency (a3f3a72)
*   **overlay:** reset cached values and applied CSS before "updating" overlays (b871e52)
*   **overlay:** resolve async races with closeOverlays and manageOpen (ff3738e)
*   **overlay:** track "modalRoots" for expanded overlay management (dceccb1)
*   **overlay:** traverse up through shadow roots when determining parent overlay (27f232c)
*   **overlay:** use esm build from popper and point through to types (078ca0f)
*   **overlay:** use isolatedModules in tsconfig (48d6069)
*   **overlay:** use tabindex=-1 but always remove it on open (6047003)
*   **overlay:** vend a VirtualTrigger for overlays with no element trigger (a359c60)
*   **picker:** use "modal" as the menu overlay interaction (c8fbbe2)
*   prevent "hover" overlays from receiving focus (7bd5ac2)
*   prevent "hover" overlays from returning focus to the root of a parent modal (ceb8fa7)
*   prevent leaving multiple submenus open at a time (d2bfbb2)
*   prevent longpress when interacting with context menu (f8b0732)
*   prevent touch scolling on non-modal content (e471feb)
*   special case the possibility of leaving an overlay trigger by entering its overlay content (c32a075)
*   **theme:** track default theme values dynamically (a0c306c)
*   **tooltip:** correct arrow orientation, remove popper-arrow-rotate (fcd6ea2)
*   update "reparentChildren" types for flexibility (2d358be)
*   update presence confirmation so popper is available on update (24f8380)
*   update screen reader interface with menu items list (16756b5)
*   update when events are added to manage overlays (60cddac)
*   use "fixed" strategy to prevent unexpected overlay placement (e39e108)
*   use height: 100% to avoid layout breaks (1498129)
*   use latest @spectrum-css/* versions (c35eb86)
*   use less restrictive overlay sizing (f6917aa)
*   use typescript@^4.5 for "native" document.fonts typings (a3e4aea)
*   wait for fonts ready before positioning overlays (cb8026a)

*   add open/close events for some menus and overlays (17f0a58)
*   add support for Spectrum Express (12bfe99)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   allow activation of longpress content (55e71fd)
*   delivery dev mode messages in various packages (62370a1)
*   **dropdown:** open menu UI with overlay system (9811eeb)
*   **field-group:** add field-group pattern (f8d265c)
*   include all Dev Mode files in side effects (f70817c)
*   join overlay-root and overlay-trigger as overlay (dcde42c)
*   leverage "exports" field in package.json (321abd7)
*   leverage latest Spectrum button API (9caf2f6)
*   **overlay:** manage focus throwing and tab trapping (27a0b53)
*   **overlay:** move entire package behind dynamic import by default (9b0a74d)
*   **picker:** process field-label content for more accurate a11y tree (dc9df54)
*   **picker:** support responsive delivery of menu (20031d1)
*   **progress-bar:** use core tokens (540552e)
*   reparentChildren - refactored arguments - breaking change (dea2bc5)
*   rework overlays to use popper (e17d1bb)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **sidenav:** add keyboard accessibility (6ff622b)
*   **split-button:** add split-button pattern (4833a59)
*   **story-decorator:** add story decorator to replace knobs for theme application (7c0c6be)
*   update lit-* dependencies, wip (377f3c8)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **progress-bar:** use core tokens (540552e)

*   **overlay:** reset cached values and applied CSS before "updating" overlays (b871e52)

*   use "fixed" strategy to prevent unexpected overlay placement (e39e108)

*   ensure Overlay.update bypasses the auto close mechanism (8f2aa2e)
*   leverage "dvh" rather than measured screen height (84b9df0)

*   ensure that an overlay can be released even if it does not complete its fade in animation (4cbb36f)
*   **overlay:** focus closure action on ancestor scroll, not participant resize (925af0a)

*   keep parent overlays open when not closing child hover overlays (643fcff)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   correct the relationship between overlayWillCloseCallback and phased animations (c63db8d)
*   **overlay:** init tab trapping on OverlayStack construction (a3121e3)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   special case the possibility of leaving an overlay trigger by entering its overlay content (c32a075)

*   **overlay:** move "escape" listener to "keydown" (813b341)

*   prevent "hover" overlays from returning focus to the root of a parent modal (ceb8fa7)
*   prevent longpress when interacting with context menu (f8b0732)

*   include all Dev Mode files in side effects (f70817c)

*   **overlay:** export OverlayTriggerInteractions type (4caec7f)

*   delivery dev mode messages in various packages (62370a1)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   ensure that entering an ancestor Menu Item without a submen closes related submenus (efe5fa1)

*   prevent leaving multiple submenus open at a time (d2bfbb2)

*   add content flow fallbacks to the position manager (c008957)
*   prevent "hover" overlays from receiving focus (7bd5ac2)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   allow Picker to be reparented (39e7309)
*   use less restrictive overlay sizing (f6917aa)

*   add support for Spectrum Express (12bfe99)
*   reparentChildren - refactored arguments - breaking change (dea2bc5)

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **menu:** add support for submenu interactions (68399af)

*   leverage latest Spectrum button API (9caf2f6)

*   **dialog:** updates for delivering dialog content accessibly (f0ed33c)
*   **overlay:** measure initial overlay data offscreen (fecda5a)

*   **picker:** support responsive delivery of menu (20031d1)

*   **overlay:** remove unused dependency (a3f3a72)

*   describe longpress button to screen readers (acdcaf4)

*   **overlay:** reduce DOM and use of "display: contents" for simplicity and accessibility (2e02075)

*   use typescript@^4.5 for "native" document.fonts typings (a3e4aea)

*   update lit-* dependencies, wip (377f3c8)

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)
*   prevent touch scolling on non-modal content (e471feb)

*   centralize updated first focusable selector (300e84c)
*   update screen reader interface with menu items list (16756b5)
*   **picker:** use "modal" as the menu overlay interaction (c8fbbe2)

*   adopt DNA@7 base Spectrum CSS (e08cafd)

*   **overlay:** allow [type="modal"] hover overlays to be closed (5a6802b)
*   **overlay:** resolve async races with closeOverlays and manageOpen (ff3738e)
*   **overlay:** traverse up through shadow roots when determining parent overlay (27f232c)

*   allow contextmenu event passing to pierce shadow roots (05b69e9)
*   correct add/remove timing of overlay events (474ec6e)

*   close modal overlays with contextmenu events and pass those to the underlying page (9e83f3c)

*   correct @element jsDoc listing across library (c97a632)

*   update when events are added to manage overlays (60cddac)

*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)
*   expand sync offering for elements with overlay content (0195843)

*   **overlay:** allow external style access to "sp-theme" elements in overlays as a CSS part (a107f66)
*   delete the used cleanup method (942ef0f)

*   allow detached elements to be used as content for an overlay (3ad8383)
*   manage "lang" via context provided by "sp-theme" (b1e3457)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   ensure focus is managed when tabbing out of a menu (9bfa81d)
*   **overlay:** vend a VirtualTrigger for overlays with no element trigger (a359c60)

*   **overlay:** add overlay lifecycle methods to stack management (9361527)
*   **overlay:** use tabindex=-1 but always remove it on open (6047003)

*   **overlay:** reduce the control active-overlay places on its content (9d12571)
*   update "reparentChildren" types for flexibility (2d358be)
*   update presence confirmation so popper is available on update (24f8380)

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** handle hover/longpress more directly via the "open" attribute (7b2b64b)

*   **overlay:** allow overlay-trigger to declaratively open overlay content (194a44e)
*   **overlay:** persist hover overlay when there is not click content (27111a9)

*   **picker:** process field-label content for more accurate a11y tree (dc9df54)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** correct overlay content sizing (d9bcd6f)
*   **overlay:** track "modalRoots" for expanded overlay management (dceccb1)
*   wait for fonts ready before positioning overlays (cb8026a)

*   use latest exports specification (a7ecf4b)

*   **overlay:** place return focus element on demand (d262237)

*   allow activation of longpress content (55e71fd)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** remove trapped content from a11y tree, manage focus, open projected content (6c496c0)
*   **tooltip:** correct arrow orientation, remove popper-arrow-rotate (fcd6ea2)

*   **overlay:** do not focus the trigger when closing an overlay, unless expected (21d7dfe)
*   include the "types" entry in package.json files (b432f59)
*   **overlay:** use esm build from popper and point through to types (078ca0f)
*   **overlay:** use isolatedModules in tsconfig (48d6069)
*   use latest @spectrum-css/* versions (c35eb86)

*   add open/close events for some menus and overlays (17f0a58)
*   **field-group:** add field-group pattern (f8d265c)
*   **story-decorator:** add story decorator to replace knobs for theme application (7c0c6be)

*   **overlay:** do not focus the trigger when closing an overlay, unless expected (21d7dfe)
*   include the "types" entry in package.json files (b432f59)
*   **overlay:** use esm build from popper and point through to types (078ca0f)
*   **overlay:** use isolatedModules in tsconfig (48d6069)
*   use latest @spectrum-css/* versions (c35eb86)

*   add open/close events for some menus and overlays (17f0a58)
*   **field-group:** add field-group pattern (f8d265c)
*   **story-decorator:** add story decorator to replace knobs for theme application (7c0c6be)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** close when overlay-trigger becomes disabled
*   include default export in the "exports" fields (f32407d)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** only "tab trap" when you mean to (74e1bd2)

*   correct overlay closure order or operations for manual override (0b7a8c4)

*   **split-button:** add split-button pattern (4833a59)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   include sync builds in publication configuration (e731673)

*   **overlay:** enforce the full frame (63628e9)
*   **overlay:** ensure overlay addition occurs after closing previous (7d2b102)

*   **overlay:** move entire package behind dynamic import by default (9b0a74d)

*   use height: 100% to avoid layout breaks (1498129)

*   ensure browser understandable extensions (f4e59f7)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **overlay:** manage focus throwing and tab trapping (27a0b53)
*   leverage "exports" field in package.json (321abd7)

*   **overlay:** ensure undefined data is not passed into theme (3e2e1ca)

*   **dropdown:** correct conditional check (a3a790f)

*   constrain overlay to available window size (9729b55)

*   use "sideEffects" listing in package.json (7271614)

*   **overlay:** new popper version tracks scroll through assigned slots (ea2bac4)

**Note:** Version bump only for package @spectrum-web-components/overlay

*   **theme:** track default theme values dynamically (a0c306c)

*   **overlay:** extend state machine to manage disposal process (f0f26af)

*   **dropdown:** open menu UI with overlay system (9811eeb)

*   **overlay:** override SpectrumCSS tip rules and process usage in popper (aad3dec)

*   rework overlays to use popper (e17d1bb)

*   join overlay-root and overlay-trigger as overlay (dcde42c)
*   **sidenav:** add keyboard accessibility (6ff622b)

 Property  Attribute  Type  Default  Description `allowOutsideClick``allow-outside-click``boolean``false` DEPRECATED: Whether clicks outside the overlay should close it (not recommended for accessibility) `delayed``delayed``boolean``false` An Overlay that is `delayed` will wait until a warm-up period of 1000ms has completed before opening. Once the warm-up period has completed, all subsequent Overlays will open immediately. When no Overlays are opened, a cool-down period of 1000ms will begin. Once the cool-down has completed, the next Overlay to be opened will be subject to the warm-up period if provided that option. 
This behavior helps to manage the performance and user experience by preventing multiple overlays from opening simultaneously and ensuring a smooth transition between opening and closing overlays.

`disabled``disabled``boolean``false` Indicates whether the overlay is currently functional or not. 
When set to `true`, the overlay is disabled, and any active strategy is aborted. The overlay will also close if it is currently open. When set to `false`, the overlay will re-bind events and re-open if it was previously open.

`offset``offset``number | [number, number]``0` The `offset` property accepts either a single number to define the offset of the Overlay along the main axis from the trigger, or a 2-tuple to define the offset along both the main axis and the cross axis. This option has no effect when there is no trigger element. `open``open``boolean``false` Indicates whether the Overlay is projected onto the "top layer" or not. 
When set to `true`, the overlay is open and visible. When set to `false`, the overlay is closed and hidden.

`placement``placement``"top" | "top-start" | "top-end" | "right" | "right-start" | "right-end" | "bottom" | "bottom-start" | "bottom-end" | "left" | "left-start" | "left-end"` Instruct the Overlay where to place itself in relationship to the trigger element. `receivesFocus``receives-focus``'true' | 'false' | 'auto'``'auto'` Whether to pass focus to the overlay once opened, or to the appropriate value based on the "type" of the overlay when set to `"auto"`. `tipPadding``tip-padding``number` The padding around the tip of the overlay. This property defines the padding around the tip of the overlay, which can be used to adjust its positioning. `trigger``trigger``string` An optional ID reference for the trigger element combined with the optional interaction (click | hover | longpress) by which the overlay should open. The format is `trigger@interaction`, e.g., `trigger@click` opens the overlay when an element with the ID "trigger" is clicked. `type``type``"auto" | "hint" | "manual" | "modal" | "page"``'auto'` Configures the open/close heuristics of the Overlay. 

Name  Description `default` The content that will be displayed in the overlay

Name  Type  Description `slottable-request``Event``requests to add or remove slottable content``sp-closed``Event``announce that an overlay has completed any exit animations``sp-opened``Event``announces that an overlay has completed any entry animations`
