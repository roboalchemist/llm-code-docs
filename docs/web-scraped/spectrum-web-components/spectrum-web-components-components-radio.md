# Source: https://opensource.adobe.com/spectrum-web-components/components/radio/

Title: Radio: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/radio/

Markdown Content:
`<sp-radio>` and `<sp-radio-group>` allow users to select a single option from a list of mutually exclusive options. All possible options are exposed up front for users to compare.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/radio?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/radio?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/radio
Import the side effectful registration of `<sp-radio>` or `<sp-radio-group>` via:

import '@spectrum-web-components/radio/sp-radio.js';
import '@spectrum-web-components/radio/sp-radio-group.js';
When looking to leverage the `Radio` or `RadioGroup` base classes as a type and/or for extension purposes, do so via:

import { Radio, RadioGroup } from '@spectrum-web-components/radio';
`<sp-radio-group>` holds a list of `<sp-radio>` elements, and is responsible for deselecting radio buttons when a new one is selected, which in turn makes it responsible for keeping track of which one is selected. `<sp-radio>` is responsible for handling user interactions and for visually reflecting if it is the one that is checked or not.

<sp-radio-group label="Choose an option" name="anatomy">
  <sp-radio value="first">Option 1</sp-radio>
  <sp-radio value="second">Option 2</sp-radio>
  <sp-radio value="third">Option 3</sp-radio>
  <sp-radio value="fourth">Option 4</sp-radio>
</sp-radio-group>
The `<sp-radio>` elements are labelled with text in their default slot.

<sp-radio-group label="Choose an option" name="anatomy">
  <sp-radio value="first">Option 1</sp-radio>
  <sp-radio value="second">Option 2</sp-radio>
  <sp-radio value="third">Option 3</sp-radio>
  <sp-radio value="fourth">Option 4</sp-radio>
</sp-radio-group>Small<sp-radio-group label="Small" selected="first" name="small">
  <sp-radio value="first" size="s">Option 1</sp-radio>
  <sp-radio value="second" size="s">Option 2</sp-radio>
  <sp-radio value="third" size="s">Option 3</sp-radio>
  <sp-radio value="fourth" size="s">Option 4</sp-radio>
</sp-radio-group>Medium<sp-radio-group label="Medium" selected="first" name="medium">
  <sp-radio value="first" size="m">Option 1</sp-radio>
  <sp-radio value="second" size="m">Option 2</sp-radio>
  <sp-radio value="third" size="m">Option 3</sp-radio>
  <sp-radio value="fourth" size="m">Option 4</sp-radio>
</sp-radio-group>Large<sp-radio-group label="Large" selected="first" name="large">
  <sp-radio value="first" size="l">Option 1</sp-radio>
  <sp-radio value="second" size="l">Option 2</sp-radio>
  <sp-radio value="third" size="l">Option 3</sp-radio>
  <sp-radio value="fourth" size="l">Option 4</sp-radio>
</sp-radio-group>Extra Large<sp-radio-group label="Extra large" selected="first" name="extra-large">
  <sp-radio value="first" size="xl">Option 1</sp-radio>
  <sp-radio value="second" size="xl">Option 2</sp-radio>
  <sp-radio value="third" size="xl">Option 3</sp-radio>
  <sp-radio value="fourth" size="xl">Option 4</sp-radio>
</sp-radio-group>
Standard radio buttons are the default style for radio buttons. They are optimal for application panels where all visual elements are monochrome in order to direct focus to the content.

**Emphasized** radio buttons are a secondary style for radio buttons. The blue color provides a visual prominence that is optimal for forms, settings, etc. where the radio buttons need to be noticed.

Standard<div style="display: flex; justify-content: space-between;">
    <div style="display: flex; flex-direction: column;">
        <sp-field-label for="example-1" size="l">
            <h4 class="spectrum-Heading--subtitle1">Default</h4>
        </sp-field-label>
        <sp-radio-group id="example-1" name="example" vertical>
            <sp-radio value="kittens">Kittens</sp-radio>
            <sp-radio value="puppies" checked>Puppies</sp-radio>
        </sp-radio-group>
    </div>

    <div style="display: flex; flex-direction: column;">
        <sp-field-label for="example-2" size="l">
            <h4 class="spectrum-Heading--subtitle1">Invalid</h4>
        </sp-field-label>
        <sp-radio-group invalid id="example-2" name="example" vertical>
            <sp-radio invalid value="kittens">Kittens</sp-radio>
            <sp-radio invalid value="puppies" checked>Puppies</sp-radio>
             <sp-help-text slot="negative-help-text" icon>
                This selection is invalid.
            </sp-help-text>
        </sp-radio-group>
    </div>

    <div style="display: flex; flex-direction: column;">
        <sp-field-label for="example-3" size="l">
            <h4 class="spectrum-Heading--subtitle1">Disabled</h4>
        </sp-fieldlabel>
        <sp-radio-group id="example-3" name="example" vertical>
            <sp-radio disabled value="kittens">Kittens</sp-radio>
            <sp-radio disabled value="puppies" checked>Puppies</sp-radio>
        </sp-radio-group>
    </div>
</div>Emphasized<div style="display: flex; justify-content: space-between;">
    <div style="display: flex; flex-direction: column;">
        <sp-field-label for="example-a" size="l">
            <h4 class="spectrum-Heading--subtitle1">Default</h4>
        </sp-field-label>
        <sp-radio-group id="example-a" name="example" vertical>
            <sp-radio emphasized value="kittens">Kittens</sp-radio>
            <sp-radio emphasized value="puppies" checked>Puppies</sp-radio>
        </sp-radio-group>
    </div>

    <div style="display: flex; flex-direction: column;">
        <sp-field-label for="example-b" size="l">
            <h4 class="spectrum-Heading--subtitle1">Invalid</h4>
        </sp-field-label>
        <sp-radio-group invalid id="example-b" name="example" vertical>
            <sp-radio emphasized invalid value="kittens">Kittens</sp-radio>
            <sp-radio emphasized invalid value="puppies" checked>Puppies</sp-radio>
            <sp-help-text slot="negative-help-text" icon>
                This selection is invalid.
            </sp-help-text>
        </sp-radio-group>
    </div>

    <div style="display: flex; flex-direction: column;">
        <sp-field-label for="example-c" size="l">
            <h4 class="spectrum-Heading--subtitle1">Disabled</h4>
        </sp-fieldlabel>
        <sp-radio-group id="example-c" name="example" vertical>
            <sp-radio emphasized disabled value="kittens">Kittens</sp-radio>
            <sp-radio emphasized disabled value="puppies" checked>Puppies</sp-radio>
        </sp-radio-group>
    </div>
</div>
Event handlers for clicks and other user actions can be registered on an `<sp-radio>` similar to a standard `<input type="radio">` element.

<sp-radio id="radio-example" onclick="spAlert(this, '<sp-radio> clicked!')">
  Web component
</sp-radio>
Tabbing into a group of radio buttons places the focus on the first radio button selected. If none of the radio buttons are selected, the focus is set on the first one in the group. Space selects the radio button in focus (if not already selected). Using the arrow keys moves focus and selection to the previous or next radio button in the group (last becomes first, and first becomes last). The new radio button in focus gets selected even if the previous one was not.

Radio groups and radio items should always have labels.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/field-group@1.11.2
    *   @spectrum-web-components/help-text@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/help-text@1.11.1
    *   @spectrum-web-components/field-group@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`7af5e8f`, `b95e254`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/help-text@1.11.0
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/field-group@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/field-group@1.10.0
    *   @spectrum-web-components/help-text@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/field-group@1.9.1
    *   @spectrum-web-components/help-text@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`, `72d807c`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/help-text@1.9.0
    *   @spectrum-web-components/field-group@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/field-group@1.8.0
    *   @spectrum-web-components/help-text@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/field-group@1.7.0
    *   @spectrum-web-components/help-text@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.6.0
    *   @spectrum-web-components/field-group@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`165a904`]: 
    *   @spectrum-web-components/help-text@1.5.0
    *   @spectrum-web-components/field-group@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/field-group@1.4.0
    *   @spectrum-web-components/help-text@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/field-group@1.3.0
    *   @spectrum-web-components/help-text@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   **button:** adds pending button, fixes #3162 (#3163) (71254ec)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   **radio-group:** onChange event not triggering on keyboard navigation (#3592) (8501239)

**Note:** Version bump only for package @spectrum-web-components/radio

*   **radio:** aria-disabled misspelling (b3fbd25), closes adobe/spectrum-web-components#3526

**Note:** Version bump only for package @spectrum-web-components/radio

*   **radio:** fix radio documentation usage of sp-field-label[for] and sp-radio-group[id] (60f54fb)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   add support for "readonly" attribute (4bce3b7)
*   apply "HelpTextMixin" to form elements (a952447)
*   apply Focuable styles in class extensions (38f7afd)
*   complete deprecation of "quiet" attribute in checkbox and radio (29d8452)
*   correct @element jsDoc listing across library (c97a632)
*   correct a11y representation of a radio group (24ed0b8)
*   ensure [disabled] styling (4c067eb)
*   implement "emphasized" styles (750bbe7)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   lint away debugger statements (34a498e)
*   manage updated node types (0517fc1)
*   move hover/focus hoisting into conditioning (15ac2f7)
*   normalize "event" and "error" argument names (8d382cd)
*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)
*   **radio:** ensure radio-group first selected value is followed (074bff8)
*   **radio:** process :focus and :focus-visible (77bc0e9)
*   **radio:** select in response to arrow keys not focus (b6acb59)
*   **slider:** use standard "change" and "input" events (59cf786)
*   stop merging selectors in a way that alters the cascade (369388f)
*   stop propagation of sp-radio "change" events at sp-radio-group boundary (f618460)
*   support matching keydown to [dir] (70b40a9)
*   update file path access (8898bf7)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   add t-shirt sizing to the Radio pattern (fc49343)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **field-group:** add field-group pattern (f8d265c)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   **overlay:** manage focus throwing and tab trapping (27a0b53)
*   **radio:** update spectrum css input (4fef340)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update lit-* dependencies, wip (377f3c8)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/radio

*   **radio:** process :focus and :focus-visible (77bc0e9)

*   move hover/focus hoisting into conditioning (15ac2f7)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   manage updated node types (0517fc1)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   add t-shirt sizing to the Radio pattern (fc49343)

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   stop propagation of sp-radio "change" events at sp-radio-group boundary (f618460)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   apply "HelpTextMixin" to form elements (a952447)

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/radio

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/radio

*   correct a11y representation of a radio group (24ed0b8)

**Note:** Version bump only for package @spectrum-web-components/radio

*   lint away debugger statements (34a498e)

*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)

*   **radio:** ensure radio-group first selected value is followed (074bff8)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   add support for "readonly" attribute (4bce3b7)

**Note:** Version bump only for package @spectrum-web-components/radio

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   complete deprecation of "quiet" attribute in checkbox and radio (29d8452)
*   ensure [disabled] styling (4c067eb)
*   implement "emphasized" styles (750bbe7)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update file path access (8898bf7)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **field-group:** add field-group pattern (f8d265c)
*   **radio:** update spectrum css input (4fef340)

*   implement "emphasized" styles (750bbe7)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update file path access (8898bf7)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **field-group:** add field-group pattern (f8d265c)
*   **radio:** update spectrum css input (4fef340)

**Note:** Version bump only for package @spectrum-web-components/radio

*   **radio:** select in response to arrow keys not focus (b6acb59)
*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/radio

*   support matching keydown to dir

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   **overlay:** manage focus throwing and tab trapping (27a0b53)
*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/radio

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

**Note:** Version bump only for package @spectrum-web-components/radio

*   apply Focuable styles in class extensions (38f7afd)

*   normalize "event" and "error" argument names (8d382cd)

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

*   **slider:** use standard "change" and "input" events (59cf786)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/radio

Property  Attribute  Type  Default  Description `checked``checked``boolean``false` Represents when the input is checked `disabled``disabled``boolean``false` Uses the disabled style `emphasized``emphasized``boolean``false``invalid``invalid``boolean``false` Uses the invalid style `readonly``readonly``boolean``false``value``value``string``''` Identifies this radio button within its radio group

Name  Description `default slot` text label of the Radio button

Name  Type  Description `change``Event``When the input is interacted with and its state is changed`
