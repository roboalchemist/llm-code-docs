# Source: https://opensource.adobe.com/spectrum-web-components/tools/grid/

Title: Grid: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/tools/grid/

Markdown Content:
An `<sp-grid>` element displays a virtualized grid of elements built from its `items`, a normalized array of JavaScript objects, applied to a supplied `renderItem`, a `TemplateResult` returning method. The `<sp-grid>` is a class extension of `lit-virtualizer` and as such surfaces all of its underlying methods and events.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/grid?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/grid?style=for-the-badge)

yarn add @spectrum-web-components/grid
Import the side effectful registration of `<sp-grid>` via:

import '@spectrum-web-components/grid/sp-grid.js';
When looking to leverage the `Grid` base class as a type and/or for extension purposes, do so via:

import { Grid } from '@spectrum-web-components/grid';
The grid consists of several key parts:

*   A virtualized container that efficiently renders only visible items
*   Individual grid items rendered via the `renderItem` method
*   A roving tabindex system for keyboard navigation
*   Configurable layout properties for item sizing and spacing

<sp-grid id="basic-grid"></sp-grid>
<script type="module"> const grid = document.querySelector('#basic-grid'); grid.items = [{ name: 'Item 1' }, { name: 'Item 2' }, { name: 'Item 3' }]; grid.renderItem = (item) => { const div = document.createElement('div'); div.textContent = item.name; return div; };</script>
The grid supports several properties for configuration:

The `items` property accepts a normalized array of JavaScript objects that will be rendered in the grid:

const grid = document.querySelector('sp-grid');
grid.items = [
  { name: 'Card 1', date: '10/15/18' },
  { name: 'Card 2', date: '10/16/18' },
  { name: 'Card 3', date: '10/17/18' },
];
The `renderItem` property is a function that receives an item, index, and selected state, and returns a DOM element to be rendered:

grid.renderItem = (item, index, selected) => {
  const card = document.createElement('sp-card');
  card.heading = item.name;
  card.selected = selected;
  return card;
};
Control the dimensions of each grid item using the `itemSize` property, which accepts an object with `width` and `height` properties:

grid.itemSize = {
  width: 200,
  height: 300,
};
Customize the space between grid items via the `gap` property, which accepts a value of `0` or `${number}px`:

grid.gap = '10px';
Specify which element within the rendered item can receive focus by providing a CSS selector to the `focusableSelector` property:

grid.focusableSelector = 'sp-card';
This informs the `<sp-grid>` element what part of the DOM created by the `renderItem` method can be focused via keyboard navigation.

The `<sp-grid>` uses virtualization to efficiently render large lists of items. Only the items visible in the viewport (plus a small buffer) are rendered to the DOM, which significantly improves performance for large datasets. As you scroll, the grid dynamically updates which items are rendered.

Elements displayed in the grid can be focused via the roving tabindex pattern. This allows the grid to be entered via the Tab key and then subsequent elements to be focused via the arrow keys.

Focus will always enter the element list at index 0 of all available elements, not just those currently realized to the page.

The grid supports selection of items. You can maintain a `selectedItems` array and update it based on user interactions:

grid.selectedItems = [];

grid.renderItem = (item, index, selected) => {
  const card = document.createElement('sp-card');
  card.selected = grid.selectedItems.includes(card.value);
  card.addEventListener('change', () => {
    if (grid.selectedItems.includes(card.value)) {
      grid.selectedItems = grid.selectedItems.filter(
        (item) => item !== card.value
      );
    } else {
      grid.selectedItems.push(card.value);
    }
  });
  return card;
};
The `<sp-grid>` is designed with accessibility in mind and follows ARIA best practices for grid patterns.

The grid supports keyboard navigation through the roving tabindex pattern:

*   Tab: Enter the grid (focus moves to first item)
*   Arrow Keys: Navigate between grid items
*   Focus always starts at index 0 of all available elements

When implementing a grid, ensure you provide appropriate ARIA attributes for screen reader support:

grid.role = 'grid';
grid.ariaLabel = 'Select images';
grid.ariaMultiSelectable = 'true';
grid.ariaRowCount = `${grid.items.length}`;
grid.ariaColCount = 1;
Additionally, each rendered item should have appropriate ARIA attributes:

card.role = 'row';
card.label = `Card Heading ${index}`;
card.ariaSelected = grid.selectedItems.includes(card.value);
card.ariaRowIndex = `${index + 1}`;
Use the `focusableSelector` property to specify which elements within each grid item should receive focus. This ensures that keyboard users can navigate to interactive elements within the grid.

To interact with a fully accessible grid example, reference our Grid Storybook documentation.

<sp-grid id="grid-demo" style=" margin: calc(-1 * var(--spectrum-spacing-500)) calc(-1 * var(--spectrum-spacing-600)) "></sp-grid>
<script type="module"> const initItems = (count) => { const total = count; const items = []; while (count) { count--; items.push({ name: String(total - count), date: count, }); } return items; }; const initGrid = () => { const grid = document.querySelector('#grid-demo'); grid.items = initItems(100); grid.focusableSelector = 'sp-card'; grid.gap = '10px'; grid.itemSize = { width: 200, height: 300, }; grid.role = 'grid'; grid.ariaLabel = 'Select images'; grid.ariaMultiSelectable = 'true'; grid.ariaRowCount = `${grid.items.length}`; grid.ariaColCount = 1; grid.selectedItems = []; grid.renderItem = ( item, index, selected ) => { const card = document.createElement('sp-card'); const img = document.createElement('img'); const description = document.createElement('div'); const footer = document.createElement('div'); card.toggles = true; card.variant = 'quiet'; card.heading = `Card Heading ${index}` card.subheading = 'JPG Photo' card.style = 'contain: strict; padding: 1px;' card.value = `card-${index}` card.selected = grid.selectedItems.includes(card.value); card.key = index; card.role = 'row'; card.label = `Card Heading ${index}`; card.ariaSelected = grid.selectedItems.includes(card.value); card.ariaRowIndex = `${index + 1}`; card.addEventListener('change', () => { if(grid.selectedItems.includes(card.value)) { grid.selectedItems = grid.selectedItems.filter(item => item !== card.value); } else { grid.selectedItems.push(card.value); } }); img.alt = ''; img.slot = 'preview'; img.src = `https://picsum.photos/id/${index}/200/300`; img.decoding = 'async'; description.slot = 'description'; description.textContent = '10/15/18'; footer.slot = 'footer'; footer.textContent = 'Footer'; card.append(img, description, footer); return card; } }; customElements.whenDefined('sp-grid').then(() => { initGrid(); });</script>

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`b95e254`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   #5171`eae4332` Thanks @majornista! - Enhanced the Card component's checkbox functionality with improved screen reader support and keyboard navigation.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

*   add an optional chromatic vrt action (7d2f840)

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

*   **reactive-controllers:** update focusable element's tab-index to 0 on accepting focus (#4630) (d359e84)

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

*   **overlay:** calculate more transforms (6538a45)
*   **overlay:** place longpress helper content in a more accessible, less layout affecting location (dd12c23)

*   **grid:** plug a mememory leak from the render process (4414bd9)

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

*   **grid:** added lit dependency (#3489) (fb5f166)

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

*   add Grid pattern (341f493)
*   add support for "padding" attribute (e43078f)
*   avoid registering lit-virtualizer globally (281071f)
*   import LitVirtualizer from @lit-labs/virtualizer@0.7.0-pre.3 (9886ce4)
*   prevent Grid clicks from throwing focus unexpectedly (872e9fd)

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

*   add support for "padding" attribute (e43078f)

*   prevent Grid clicks from throwing focus unexpectedly (872e9fd)

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

**Note:** Version bump only for package @spectrum-web-components/grid

*   avoid registering lit-virtualizer globally (281071f)
*   import LitVirtualizer from @lit-labs/virtualizer@0.7.0-pre.3 (9886ce4)

**Note:** Version bump only for package @spectrum-web-components/grid

*   add Grid pattern (341f493)

Property  Attribute  Type  Default  Description `focusableSelector``focusableSelector``string``gap``gap```${'0' | `${number}px`}```'0'``itemSize``itemSize``{ width: number; height: number; }``{ width: 200, height: 200, }``items``items``Record<string, unknown>[]``[]``padding``padding```${'0' | `${number}px`}` | undefined``selected``selected``Record<string, unknown>[]``[]`

Name  Type  Description `change``Event``Announces that the value of `selected` has changed`
