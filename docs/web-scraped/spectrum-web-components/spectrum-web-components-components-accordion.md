# Source: https://opensource.adobe.com/spectrum-web-components/components/accordion/

Title: Accordion: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/accordion/

Markdown Content:
The `<sp-accordion>` element contains a list of items that can be expanded or collapsed to reveal additional content or information associated with each item. There can be zero expanded items, exactly one expanded item, or more than one item expanded at a time, depending on the configuration. This list of items is defined by child `<sp-accordion-item>` elements that are targeted to the default slot of their `<sp-accordion>` parent.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/accordion?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/accordion?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/accordion
Import the side effectful registration of `<sp-accordion>` and `<sp-accordion-item>` via:

import '@spectrum-web-components/accordion/sp-accordion.js';
import '@spectrum-web-components/accordion/sp-accordion-item.js';
When looking to leverage the `Accordion` and `AccordionItem` base class as a type and/or for extension purposes, do so via:

import { Accordion, AccordionItem } from '@spectrum-web-components/accordion';
The accordion consists of several key parts:

*   A container element that manages the accordion behavior
*   Individual accordion items that can be expanded or collapsed
*   Each item has a header with a label and chevron icon
*   Content that is revealed when an item is expanded

<sp-accordion>
  <sp-accordion-item label="Bellows">
    <div>
      The bellows is the expandable section in the middle of the accordion.
    </div>
  </sp-accordion-item>
  <sp-accordion-item disabled label="Treble">
    <div>
      The treble section of the accordion is the right-hand section for playing
      melodies.
    </div>
  </sp-accordion-item>
  <sp-accordion-item label="Bass">
    <div>
      The bass section of the accordion is the left-hand section for playing
      accompaniment.
    </div>
  </sp-accordion-item>
</sp-accordion>Small<sp-accordion size="s">
  <sp-accordion-item label="Key Accordion">
    <div>
      A key accordion, or a chromatic piano accordion, includes a keyboard for
      the right hand.
    </div>
  </sp-accordion-item>
  <sp-accordion-item disabled label="Button Accordion">
    <div>
      A button accoridon, or a chromatic accordion, has buttons instead of keys.
    </div>
  </sp-accordion-item>
  <sp-accordion-item label="Diatonic Accordion">
    <div>
      Produces two different tones or notes depending on whether the bellows is
      pulled or pushed.
    </div>
  </sp-accordion-item>
  <sp-accordion-item label="Concertina">
    <div>
      A concertina has buttons on both sides and each button makes two different
      notes or tones depending on whether the bellows is pulled or pushed.
    </div>
  </sp-accordion-item>
</sp-accordion>Medium<sp-accordion size="m">
  <sp-accordion-item label="Key Accordion">
    <div>
      A key accordion, or a chromatic piano accordion, includes a keyboard for
      the right hand.
    </div>
  </sp-accordion-item>
  <sp-accordion-item disabled label="Button Accordion">
    <div>
      A button accoridon, or a chromatic accordion, has buttons instead of keys.
    </div>
  </sp-accordion-item>
  <sp-accordion-item label="Diatonic Accordion">
    <div>
      Produces two different tones or notes depending on whether the bellows is
      pulled or pushed.
    </div>
  </sp-accordion-item>
  <sp-accordion-item label="Concertina">
    <div>
      A concertina has buttons on both sides and each button makes two different
      notes or tones depending on whether the bellows is pulled or pushed.
    </div>
  </sp-accordion-item>
</sp-accordion>Large<sp-accordion size="l">
  <sp-accordion-item label="Key Accordion">
    <div>
      A key accordion, or a chromatic piano accordion, includes a keyboard for
      the right hand.
    </div>
  </sp-accordion-item>
  <sp-accordion-item disabled label="Button Accordion">
    <div>
      A button accoridon, or a chromatic accordion, has buttons instead of keys.
    </div>
  </sp-accordion-item>
  <sp-accordion-item label="Diatonic Accordion">
    <div>
      Produces two different tones or notes depending on whether the bellows is
      pulled or pushed.
    </div>
  </sp-accordion-item>
  <sp-accordion-item label="Concertina">
    <div>
      A concertina has buttons on both sides and each button makes two different
      notes or tones depending on whether the bellows is pulled or pushed.
    </div>
  </sp-accordion-item>
</sp-accordion>Extra Large<sp-accordion size="xl">
  <sp-accordion-item label="Key Accordion">
    <div>
      A key accordion, or a chromatic piano accordion, includes a keyboard for
      the right hand.
    </div>
  </sp-accordion-item>
  <sp-accordion-item disabled label="Button Accordion">
    <div>
      A button accoridon, or a chromatic accordion, has buttons instead of keys.
    </div>
  </sp-accordion-item>
  <sp-accordion-item label="Diatonic Accordion">
    <div>
      Produces two different tones or notes depending on whether the bellows is
      pulled or pushed.
    </div>
  </sp-accordion-item>
  <sp-accordion-item label="Concertina">
    <div>
      A concertina has buttons on both sides and each button makes two different
      notes or tones depending on whether the bellows is pulled or pushed.
    </div>
  </sp-accordion-item>
</sp-accordion>
The `density` property, when applied, accepts the values of `compact` or `spacious`.

Compact<div style=" display: grid; grid-gap: 20px; grid-template-columns: 1fr 1fr">
  <sp-accordion density="compact" size="s">
    <sp-accordion-item label="Compact Density">
      <div>This accordion is compact.</div>
    </sp-accordion-item>
    <sp-accordion-item label="Small Size">
      <div>This accordion is also small.</div>
    </sp-accordion-item>
  </sp-accordion>
  <sp-accordion density="compact" size="m">
    <sp-accordion-item label="Compact Density">
      <div>This accordion is compact.</div>
    </sp-accordion-item>
    <sp-accordion-item label="Medium Size">
      <div>This accordion is also medium.</div>
    </sp-accordion-item>
  </sp-accordion>
  <sp-accordion density="compact" size="l">
    <sp-accordion-item label="Compact Density">
      <div>This accordion is compact.</div>
    </sp-accordion-item>
    <sp-accordion-item label="Large Size">
      <div>This accordion is also large.</div>
    </sp-accordion-item>
  </sp-accordion>
  <sp-accordion density="compact" size="xl">
    <sp-accordion-item label="Compact Density">
      <div>This accordion is compact.</div>
    </sp-accordion-item>
    <sp-accordion-item label="Extra Large Size">
      <div>This accordion is also extra large.</div>
    </sp-accordion-item>
  </sp-accordion>
</div>Spacious<div style=" display: grid; grid-gap: 20px; grid-template-columns: 1fr 1fr">
  <sp-accordion density="spacious" size="s">
    <sp-accordion-item label="Spacious Density">
      <div>This accordion is spacious.</div>
    </sp-accordion-item>
    <sp-accordion-item label="Small Size">
      <div>This accordion is also small.</div>
    </sp-accordion-item>
  </sp-accordion>
  <sp-accordion density="spacious" size="m">
    <sp-accordion-item label="Spacious Density">
      <div>This accordion is spacious.</div>
    </sp-accordion-item>
    <sp-accordion-item label="Medium Size">
      <div>This accordion is also medium.</div>
    </sp-accordion-item>
  </sp-accordion>
  <sp-accordion density="spacious" size="l">
    <sp-accordion-item label="Spacious Density">
      <div>This accordion is spacious.</div>
    </sp-accordion-item>
    <sp-accordion-item label="Large Size">
      <div>This accordion is also large.</div>
    </sp-accordion-item>
  </sp-accordion>
  <sp-accordion density="spacious" size="xl">
    <sp-accordion-item label="Spacious Density">
      <div>This accordion is spacious.</div>
    </sp-accordion-item>
    <sp-accordion-item label="Extra Large Size">
      <div>This accordion is also extra large.</div>
    </sp-accordion-item>
  </sp-accordion>
</div>
The `level` attribute controls the semantic heading level (2-6) used for all accordion item titles. This helps maintain proper document structure and accessibility. The range is restricted to 2-6 as there should only be one `h1` per page. Defaults to 3.

All items within an accordion will use the same heading level, ensuring items of equal importance have consistent semantic meaning.

<h1>Main Page Title</h1>

<sp-accordion level="2">
  <sp-accordion-item label="First Section">
    <div>Content for the first main section.</div>
  </sp-accordion-item>
  <sp-accordion-item label="Second Section">
    <div>Content for the second main section.</div>
  </sp-accordion-item>
  <sp-accordion-item label="Third Section">
    <div>Content for the third main section.</div>
  </sp-accordion-item>
</sp-accordion>

<h2>Subsection Title</h2>

<sp-accordion level="3">
  <sp-accordion-item label="Subsection A">
    <div>Content for subsection A.</div>
  </sp-accordion-item>
  <sp-accordion-item label="Subsection B">
    <div>Content for subsection B.</div>
  </sp-accordion-item>
</sp-accordion>
By default, only one accordion item can be expanded at a time. Use the `allow-multiple` attribute to allow multiple items to be expanded simultaneously.

<sp-accordion allow-multiple>
  <sp-accordion-item label="Kermit">
    <div>Kermit is a frog.</div>
  </sp-accordion-item>
  <sp-accordion-item label="Fozzie">
    <div>Fozzie is a bear.</div>
  </sp-accordion-item>
  <sp-accordion-item label="Miss Piggy">
    <div>Miss Piggy is a pig.</div>
  </sp-accordion-item>
</sp-accordion>
Individual accordion items can be disabled using the `disabled` attribute. Disabled items cannot be expanded or collapsed.

<sp-accordion>
  <sp-accordion-item label="Apples">
    <div>
      We have some of the most popular varieties include Red Delicious, Gala,
      Granny Smith, Honeycrisp, and Fuji.
    </div>
  </sp-accordion-item>
  <sp-accordion-item disabled label="Bananas">
    <div>We have the Gros Michel.</div>
  </sp-accordion-item>
  <sp-accordion-item label="Oranges">
    <div>We have Mandarins, Seville Oranges, and Clementines.</div>
  </sp-accordion-item>
</sp-accordion>
The accordion component provides proper ARIA attributes and keyboard navigation:

*   Each accordion item header has `aria-expanded` to indicate its current state
*   The header button has `aria-controls` pointing to the content region
*   The content region has `role="region"` and `aria-labelledby` pointing to the header
*   Disabled items have `aria-disabled="true"` applied
*   The accordion supports keyboard navigation with arrow keys and Enter/Space for activation

Each accordion item should have a clear, descriptive label that indicates what content will be revealed when expanded.

Accordion content should be related to the header label and provide additional information or functionality that users can access when needed.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   **accordion:** core token migration (#3300) (9650b71)

**Note:** Version bump only for package @spectrum-web-components/accordion

*   removed usage of id in accordion (c26c81f)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   **accordion:** ensure item toggle events can be prevented from the outside (30dbfc8)
*   **accordion:** update a11y tree to not double label (cc91a6b)
*   add missing dependency (9f74e7d)
*   contain activation to header content (10183ce)
*   correct @element jsDoc listing across library (c97a632)
*   correctly apply tab order to Accordion Items (fd7a7f9)
*   ensure item exists when attempting to acquire next item to focus (fb52cea)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   prevent infinite loops when all children are [disabled] (2deac3d)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update consumption of Spectrum CSS for latest version (ed2305b)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

*   **accordion:** add accordion pattern (97529d8)
*   **accordion:** allow accordion items to close (3c715ab)
*   **accordion:** update spectrum css input (d94e059)
*   **action-button:** add action button pattern (03ac00a)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/accordion

*   add missing dependency (9f74e7d)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   update consumption of Spectrum CSS for latest version (ed2305b)

*   contain activation to header content (10183ce)
*   correctly apply tab order to Accordion Items (fd7a7f9)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/accordion

*   **accordion:** ensure item toggle events can be prevented from the outside (30dbfc8)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   ensure item exists when attempting to acquire next item to focus (fb52cea)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   **accordion:** update a11y tree to not double label (cc91a6b)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   include the "types" entry in package.json files (b432f59)
*   prevent infinite loops when all children are [disabled] (2deac3d)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

*   **accordion:** allow accordion items to close (3c715ab)
*   **accordion:** update spectrum css input (d94e059)
*   **action-button:** add action button pattern (03ac00a)

*   include the "types" entry in package.json files (b432f59)
*   prevent infinite loops when all children are disabled
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **accordion:** allow accordion items to close (3c715ab)
*   **accordion:** update spectrum css input (d94e059)
*   **action-button:** add action button pattern (03ac00a)

**Note:** Version bump only for package @spectrum-web-components/accordion

*   include default export in the "exports" fields (f32407d)

**Note:** Version bump only for package @spectrum-web-components/accordion

**Note:** Version bump only for package @spectrum-web-components/accordion

*   **accordion:** add accordion pattern (97529d8)

Property  Attribute  Type  Default  Description `allowMultiple``allow-multiple``boolean``false` Allows multiple accordion items to be opened at the same time `density``density``'compact' | 'spacious' | undefined` Sets the spacing between the content to borders of an accordion item `level``level``number``3` The heading level (2-6) to use for all accordion item titles. Defaults to 3.

Name  Description `default slot` The sp-accordion-item children to display.
