# Source: https://opensource.adobe.com/spectrum-web-components/components/action-group/

Title: Action Group: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/action-group/

Markdown Content:
`sp-action-group` delivers a set of action buttons in horizontal or vertical orientation while ensuring the appropriate spacing between those buttons. The `compact` attribute merges these buttons so that they are visually joined to clarify their relationship to each other and their distance from other buttons/groups.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/action-group?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/action-group?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/action-group

Import the side effectful registration of `<sp-action-group>` via:

import '@spectrum-web-components/action-group/sp-action-group.js';

When looking to leverage the `ActionGroup` base class as a type and/or for extension purposes, do so via:

import { ActionGroup } from '@spectrum-web-components/action-group';
Extra Small<sp-action-group size="xs">
  <sp-action-button>Extra Small 1</sp-action-button>
  <sp-action-button>Extra Small 2</sp-action-button>
</sp-action-group>Small<sp-action-group size="s">
  <sp-action-button>Small 1</sp-action-button>
  <sp-action-button>Small 2</sp-action-button>
</sp-action-group>Medium<sp-action-group size="m">
  <sp-action-button>Medium 1</sp-action-button>
  <sp-action-button>Medium 2</sp-action-button>
</sp-action-group>Large<sp-action-group size="l">
  <sp-action-button>Large 1</sp-action-button>
  <sp-action-button>Large 2</sp-action-button>
</sp-action-group>Extra Large<sp-action-group size="xl">
  <sp-action-button>Extra Large 1</sp-action-button>
  <sp-action-button>Extra Large 2</sp-action-button>
</sp-action-group>
An `<sp-action-group selects="single|multiple">` will manage a `selected` property that consists on an array of the `<sp-action-button>` children that are currently selected. A `change` event is dispatched from the `<sp-action-group>` element when the value of `selected` is updated. This event can be canceled via `event.preventDefault()`, after which the value of `selected` will be returned to what it was previously.

When a selection can be made, it is a good idea to supply the group of options with accessible text that names the group of buttons. This can be done in a non-visual way via the `label` attribute of the `<sp-action-group>` element. You can also associate the `<sp-action-group>` to a second, visible DOM element via the `aria-labelledby` attribute or, when available, via the `for` attribute on the second element to make the association in the other direction.

An `<sp-action-group selects="single">` will manage its `<sp-action-button>` children as "radio buttons" allowing the user to select a _single_ one of the buttons presented. The `<sp-action-button>` children will only be able to turn their `selected` value on while maintaining a single selection after an initial selection is made.

<sp-action-group selects="single" emphasized label="Single Selection Demo Group">
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Button 1
  </sp-action-button>
  <sp-action-button selected>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Longer Button 2
  </sp-action-button>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Short 3
  </sp-action-button>
</sp-action-group>
An `<sp-action-group selects="multiple">` will manage its `<sp-action-button>` children as "checkboxes" allowing the user to select a _multiple_ of the buttons presented. The `<sp-action-button>` children will toggle their `selected` value on and off when clicked successively.

<sp-action-group selects="multiple" emphasized label="Multiple Selection Demo Group">
  <sp-action-button selected>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Button 1
  </sp-action-button>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Longer Button 2
  </sp-action-button>
  <sp-action-button selected>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Short 3
  </sp-action-button>
</sp-action-group>
The `selected` property represents the selection state within a button group. This property can be managed either by the component or by the user. Passing in an array of button values will make `<sp-action-group>` a controllable component. Though `selected` would more commonly be set via Javascript expressions (i.e. `<sp-action-group .selected=${["first"]}>`), it is also possible to set `selected` as a JSON string.

<sp-action-group selects="single" selected='["first"]'>
  <sp-action-button value="first">First</sp-action-button>
  <sp-action-button value="second">Second</sp-action-button>
</sp-action-group>
By default, an `<sp-action-group>` will select any button passed into `selected`. Afterwards, `.selects` controls how button values are added to the selection state. For example, if `.selects` is not specified when `selected` is set, any further interaction will result in no change to the selection.

<sp-action-group selected='["first", "second"]'>
  <sp-action-button value="first">First</sp-action-button>
  <sp-action-button value="second">Second</sp-action-button>
  <sp-action-button value="third">Third</sp-action-button>
</sp-action-group>
Similarly, if `selected` contains more than one button value, but `selects = "single"`, then those initial buttons will be highlighted, but further interaction will result in radio-button functionality.

<sp-action-group selects="single" selected='["first", "second"]'>
  <sp-action-button value="first">First</sp-action-button>
  <sp-action-button value="second">Second</sp-action-button>
  <sp-action-button value="third">Third</sp-action-button>
</sp-action-group>
By default, an `<sp-action-group>` will organize its child buttons horizontally and the delivery of those buttons can be modified with the `compact`, `emphasized`, or `quiet` attributes.

<sp-action-group>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Button 1
  </sp-action-button>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Longer Button 2
  </sp-action-button>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Short 3
  </sp-action-button>
</sp-action-group>
<br />
<sp-action-group compact>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Button 1
  </sp-action-button>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Longer Button 2
  </sp-action-button>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Short 3
  </sp-action-button>
</sp-action-group>
<br />
<sp-action-group quiet>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
</sp-action-group>
<br />
<sp-action-group compact emphasized>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
</sp-action-group>
The use of the `vertical` attribute instructs the `<sp-action-group>` element to organize its child buttons vertically, while accepting the same `compact`, `emphasized`, and `quiet` attributes as modifiers.

<div style="display: flex; justify-content: space-around;">
  <sp-action-group vertical>
    <sp-action-button>
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
      Button 1
    </sp-action-button>
    <sp-action-button>
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
      Longer Button 2
    </sp-action-button>
    <sp-action-button>
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
      Short 3
    </sp-action-button>
  </sp-action-group>
  <sp-action-group vertical compact>
    <sp-action-button>
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
      Button 1
    </sp-action-button>
    <sp-action-button>
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
      Longer Button 2
    </sp-action-button>
    <sp-action-button>
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
      Short 3
    </sp-action-button>
  </sp-action-group>
  <sp-action-group vertical quiet>
    <sp-action-button label="Zoom in">
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
    </sp-action-button>
    <sp-action-button label="Zoom in">
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
    </sp-action-button>
    <sp-action-button label="Zoom in">
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
    </sp-action-button>
  </sp-action-group>
  <sp-action-group compact vertical>
    <sp-action-button label="Zoom in">
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
    </sp-action-button>
    <sp-action-button label="Zoom in">
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
    </sp-action-button>
    <sp-action-button label="Zoom in">
      <sp-icon-magnify slot="icon"></sp-icon-magnify>
    </sp-action-button>
  </sp-action-group>
</div>
The `justified` attribute will cause the `<sp-action-group>` element to fill the available horizontal space and evenly distribute that space across its child button elements.

<sp-action-group justified>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Button 1
  </sp-action-button>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Longer Button 2
  </sp-action-button>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Short 3
  </sp-action-button>
</sp-action-group>
<br />
<sp-action-group justified compact>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Button 1
  </sp-action-button>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Longer Button 2
  </sp-action-button>
  <sp-action-button>
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
    Short 3
  </sp-action-button>
</sp-action-group>
<br />
<sp-action-group justified quiet>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
</sp-action-group>
<br />
<sp-action-group compact justified>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-action-button label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
</sp-action-group>
The accessibility `role` for an `<sp-action-group>` element depends on the manner in which items are selected. By default, `<sp-action-group selects="single">` will have `role="radiogroup"`, because it manages its children as a "radio group", while `<sp-action-group>` or `<sp-action-group selects="multiple">` will have `role="toolbar"`, which makes sense for a group of buttons or checkboxes between which one can navigate using the arrow keys.

When more than one `<sp-action-group>` elements are combined together with in a toolbar, the `role` attribute for `<sp-action-group>` or `<sp-action-group selects="multiple">` should be overwritten using `role="group"` or `role="presentation"`, so that toolbars are not nested, as demonstrated in the following example of a hypothetical toolbar for formatting text within a rich text editor:

<div aria-label="Text Formatting" role="toolbar" style="height: 32px; display: flex; gap: 6px">
  <sp-action-group aria-label="Text Style" selects="multiple" role="group" compact emphasized >
    <sp-action-button label="Bold" value="bold">
      <sp-icon-text-bold slot="icon"></sp-icon-text-bold>
    </sp-action-button>
    <sp-action-button label="Italic" value="italic">
      <sp-icon-text-italic slot="icon"></sp-icon-text-italic>
    </sp-action-button>
    <sp-action-button label="Underline" value="underline">
      <sp-icon-text-underline slot="icon"></sp-icon-text-underline>
    </sp-action-button>
  </sp-action-group>
  <sp-divider size="s" style="align-self: stretch; height: auto;" vertical ></sp-divider>
  <sp-action-group aria-label="Text Align" selects="single" compact emphasized>
    <sp-action-button label="Left" value="left" selected>
      <sp-icon-text-align-left slot="icon"></sp-icon-text-align-left>
    </sp-action-button>
    <sp-action-button label="Center" value="center">
      <sp-icon-text-align-center slot="icon"></sp-icon-text-align-center>
    </sp-action-button>
    <sp-action-button label="Right" value="right">
      <sp-icon-text-align-right slot="icon"></sp-icon-text-align-right>
    </sp-action-button>
    <sp-action-button label="Justify" value="justify">
      <sp-icon-text-align-justify slot="icon"></sp-icon-text-align-justify>
    </sp-action-button>
  </sp-action-group>
  <sp-divider size="s" style="align-self: stretch; height: auto;" vertical ></sp-divider>
  <sp-action-group aria-label="List Style" selects="multiple" role="group" compact emphasized >
    <sp-action-button label="Bulleted" value="bulleted" onclick=" /* makes mutually exclusive checkbox */ this.selected && requestAnimationFrame(() => this.parentElement.selected = []); this.parentElement.selected = []; " >
      <sp-icon-text-bulleted slot="icon"></sp-icon-text-bulleted>
    </sp-action-button>
    <sp-action-button label="Numbering" value="numbering" onclick=" /* makes mutually exclusive checkbox */ this.selected && requestAnimationFrame(() => this.parentElement.selected = []); this.parentElement.selected = []; " >
      <sp-icon-text-numbered slot="icon"></sp-icon-text-numbered>
    </sp-action-button>
  </sp-action-group>
  <sp-divider size="s" style="align-self: stretch; height: auto;" vertical ></sp-divider>
  <sp-action-group role="presentation" compact>
    <sp-action-button disabled label="Copy" value="copy">
      <sp-icon-copy slot="icon"></sp-icon-copy>
    </sp-action-button>
    <sp-action-button disabled label="Paste" value="paste">
      <sp-icon-paste slot="icon"></sp-icon-paste>
    </sp-action-button>
    <sp-action-button disabled label="Cut" value="cut">
      <sp-icon-cut slot="icon"></sp-icon-cut>
    </sp-action-button>
  </sp-action-group>
</div>

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/action-button@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/action-button@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`b95e254`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/action-button@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/action-button@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/action-button@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1

*   Updated dependencies [`bdf54c1`, `7d23140`]: 
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/action-button@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/action-button@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0

*   Updated dependencies [`c1669d2`]: 
    *   @spectrum-web-components/action-button@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0

*   Updated dependencies [`f6cebbd`]: 
    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/action-button@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0

*   Updated dependencies [`6c58f50`]: 
    *   @spectrum-web-components/action-button@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0

*   Updated dependencies [`72dbe62`]: 
    *   @spectrum-web-components/action-button@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/action-button@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **action menu:** keyboard accessibility omnibus (#5031) (ea38ef0), closes #4623

*   **reactive-controllers:** Migrate to Colorjs from Tinycolor (#4713) (9d740f0)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **action-group:** add null check for slotElement in manageButtons (#4924) (60db5ab)

*   remove deprecated 'static' references (#4818)

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **reactive-controllers:** update focusable element's tab-index to 0 on accepting focus (#4630) (d359e84)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **action-bar:** support for action-menus (#3780) (4aff599)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **shared:** ensure the "updateComplete" in Focusable is stable (885b4a5)

*   **action-group:** manage Action Button selection through multiple slots (4d02b46)
*   **button:** prevent pointer interaction of child/slotted content (2cd5823)
*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **action-button:** allow change events to bubble and pierce shadowdom (#3614) (3f76e04)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **picker,action-group,split-button:** leverage Overlay v2 (170a223)

*   **action-group:** separate first selection management from later selection management (783b206)

*   **action-bar:** use core tokens (4e21edf)

*   **action-group:** ensure Action Button clicks are attributed to the right element (#3292) (ddccab7)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **action-group:** update application/management of "role" on group and buttons (533873b), closes #3221#3221#3221

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **action-group:** add custom focus() method and use sendKeys for correct "Enter" key testing (638aa35)
*   **action-group:** allow direct setting aria-label on first update (84f7fdd)
*   **action-group:** allow for initial button being "disabled" (a1e3939)
*   **action-group:** allow quiet and emphasized attributes to be passed to slotted action buttons (aadfddb)
*   **action-group:** pass styles to nested children, too (12f1be3)
*   **action-group:** support ActionButtons that are not direct children (1d4efd5)
*   **action-group:** use the correct role for buttons when not selects (0aae8ed)
*   correct @element jsDoc listing across library (c97a632)
*   ensure that "selected" can be set more than once from the outside (5f1996c)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   **textfield:** respect type=text|url|tel|email|password (1b7a59a)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** add action-group pattern (d2de766)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   **action-group:** update spectrum css input (9840b19)
*   **action-group:** use core tokens (73f3b51)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **button:** use synthetic button instead of native (49e94bc)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   include all Dev Mode files in side effects (f70817c)
*   leverage latest Spectrum button API (9caf2f6)
*   modified .selected to make `<sp-action-group>` a controllable component (#2006) (4c69b25)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   support Spectrum Token consumption and update Action Button to use them (743ab16)
*   **theme:** filter css variables (1761f3a)
*   update lit-* dependencies, wip (377f3c8)
*   use latest exports specification (a7ecf4b)

*   reorganize inheritance and composition in Menu Items (d96ccb6)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **action-group:** use core tokens (73f3b51)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/action-group

*   support Spectrum Token consumption and update Action Button to use them (743ab16)

*   **theme:** filter css variables (1761f3a)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   ensure that "selected" can be set more than once from the outside (5f1996c)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   leverage latest Spectrum button API (9caf2f6)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   modified .selected to make `<sp-action-group>` a controllable component (#2006) (4c69b25)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **textfield:** respect type=text|url|tel|email|password (1b7a59a)

*   adopt DNA@7 base Spectrum CSS (e08cafd)

*   **action-group:** allow quiet and emphasized attributes to be passed to slotted action buttons (aadfddb)

*   **action-group:** add custom focus() method and use sendKeys for correct "Enter" key testing (638aa35)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   correct @element jsDoc listing across library (c97a632)

*   reorganize inheritance and composition in Menu Items (d96ccb6)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **action-group:** pass styles to nested children, too (12f1be3)

*   **action-group:** allow direct setting aria-label on first update (84f7fdd)
*   **action-group:** use the correct role for buttons when not selects (0aae8ed)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **action-group:** allow for initial button being "disabled" (a1e3939)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **action-group:** support ActionButtons that are not direct children (1d4efd5)

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/action-group

**Note:** Version bump only for package @spectrum-web-components/action-group

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   **action-group:** update spectrum css input (9840b19)
*   **button:** use synthetic button instead of native (49e94bc)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   **action-group:** update spectrum css input (9840b19)
*   **button:** use synthetic button instead of native (49e94bc)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

**Note:** Version bump only for package @spectrum-web-components/action-group

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/action-group

*   **action-group:** add action-group pattern (d2de766)

Property  Attribute  Type  Default  Description `compact``compact``boolean``false``emphasized``emphasized``boolean``false``justified``justified``boolean``false``label``label``string``''``quiet``quiet``boolean``false``selected``selected``string[]``selects``selects``undefined | 'single' | 'multiple'``staticColor``static-color``'white' | 'black' | undefined``vertical``vertical``boolean``false`

Name  Description `default slot` the sp-action-button elements that make up the group

Name  Type  Description `change``Event``Announces that selection state has been changed by user`
