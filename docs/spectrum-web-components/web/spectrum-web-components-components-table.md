# Source: https://opensource.adobe.com/spectrum-web-components/components/table/

Title: Table: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/table/

Markdown Content:
An `<sp-table>` is used to create a container for displaying information. It allows users to quickly scan, sort, compare, and take action on large amounts of data. Tables are essential for organizing and presenting structured information in a clear, accessible format.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/table?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/table?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/table
Import the side effectful registration of `<sp-table>`, `<sp-table-body>`, `<sp-table-cell>`, `<sp-table-checkbox-cell>`, `<sp-table-head>`, `<sp-table-head-cell>`, and `<sp-table-row>` via:

import '@spectrum-web-components/table/elements.js';
Or individually via:

import '@spectrum-web-components/table/sp-table.js';
import '@spectrum-web-components/table/sp-table-body.js';
import '@spectrum-web-components/table/sp-table-cell.js';
import '@spectrum-web-components/table/sp-table-checkbox-cell.js';
import '@spectrum-web-components/table/sp-table-head.js';
import '@spectrum-web-components/table/sp-table-head-cell.js';
import '@spectrum-web-components/table/sp-table-row.js';
When looking to leverage the `Table`, `TableBody`, `TableCell`, `TableCheckboxCell`, `TableHead`, `TableHeadCell`, or `TableRow` base classes as a type and/or for extension purposes, do so via:

import {
  Table,
  TableBody,
  TableCell,
  TableCheckboxCell,
  TableHead,
  TableHeadCell,
  TableRow,
} from '@spectrum-web-components/table';
A table consists of the following parts:

*   a table head section (`<sp-table-head>`)
*   header cells (`<sp-table-head-cell>`) within the table head section
*   a table body section, ie.`<sp-table-body>`
*   rows (`<sp-table-row>`) within the table body section
*   body cells (`<sp-table-cell>`) within the table body rows

<sp-table>
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
    <sp-table-head-cell>Size</sp-table-head-cell>
    <sp-table-head-cell>Status</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row>
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>89 KB</sp-table-cell>
      <sp-table-cell>Reviewed</sp-table-cell>
    </sp-table-row>
    <sp-table-row>
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
      <sp-table-cell>120 KB</sp-table-cell>
      <sp-table-cell>Draft</sp-table-cell>
    </sp-table-row>
    <sp-table-row>
      <sp-table-cell>Proposal</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>139 KB</sp-table-cell>
      <sp-table-cell>Published</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table>Selection
The `selects` attribute enables row selection functionality. When `selects="single"`, users can select one row at a time. When `selects="multiple"`, users can select multiple rows and a checkbox column is automatically added to the table header for select all functionality.

When using selection, checkboxes are automatically given accessible labels for screen readers:

*   **Header row checkbox**: Uses the `select-all-label` attribute (defaults to "Select All")
*   **Body row checkboxes**: Uses the text content of the first `<sp-table-cell>` in each row

You can customize the header checkbox label using the `select-all-label` attribute:

<sp-table selects="multiple" select-all-label="Select all files">
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row value="row1">
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
    </sp-table-row>
    <sp-table-row value="row2">
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table><sp-table selects="multiple" selected='["row1", "row2"]'>
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
    <sp-table-head-cell>Size</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row value="row1">
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>89 KB</sp-table-cell>
    </sp-table-row>
    <sp-table-row value="row2">
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
      <sp-table-cell>120 KB</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table>Emphasized
The `emphasized` attribute adds visual priority to the table content. This affects the appearance of selected rows and checkboxes, providing a more prominent visual treatment.

<sp-table emphasized selects="multiple" selected='["row1"]'>
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
    <sp-table-head-cell>Size</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row value="row1">
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>89 KB</sp-table-cell>
    </sp-table-row>
    <sp-table-row value="row2">
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
      <sp-table-cell>120 KB</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table>Density
The `density` attribute controls the spacing around table cell content. Available values are `compact` for tighter spacing and `spacious` for more generous spacing.

Compact<sp-table density="compact">
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
    <sp-table-head-cell>Size</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row>
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>89 KB</sp-table-cell>
    </sp-table-row>
    <sp-table-row>
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
      <sp-table-cell>120 KB</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table>Spacious<sp-table density="spacious">
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
    <sp-table-head-cell>Size</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row>
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>89 KB</sp-table-cell>
    </sp-table-row>
    <sp-table-row>
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
      <sp-table-cell>120 KB</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table>Size
The `size` attribute controls the overall size of the table. Available values are `s` (small), `m` (medium, default), `l` (large), and `xl` (extra large).

Small<sp-table size="s">
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
    <sp-table-head-cell>Size</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row>
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>89 KB</sp-table-cell>
    </sp-table-row>
    <sp-table-row>
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
      <sp-table-cell>120 KB</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table>Medium (Default)<sp-table>
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
    <sp-table-head-cell>Size</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row>
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>89 KB</sp-table-cell>
    </sp-table-row>
    <sp-table-row>
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
      <sp-table-cell>120 KB</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table>Large<sp-table size="l">
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
    <sp-table-head-cell>Size</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row>
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>89 KB</sp-table-cell>
    </sp-table-row>
    <sp-table-row>
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
      <sp-table-cell>120 KB</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table>Extra Large<sp-table size="xl">
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
    <sp-table-head-cell>Size</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row>
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>89 KB</sp-table-cell>
    </sp-table-row>
    <sp-table-row>
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
      <sp-table-cell>120 KB</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table>Quiet
The `quiet` attribute creates a more subtle table appearance with a transparent background and no side borders. This is ideal for supplementary or lightweight data display.

<sp-table quiet>
  <sp-table-head>
    <sp-table-head-cell>File name</sp-table-head-cell>
    <sp-table-head-cell>Type</sp-table-head-cell>
    <sp-table-head-cell>Size</sp-table-head-cell>
  </sp-table-head>
  <sp-table-body>
    <sp-table-row>
      <sp-table-cell>Budget</sp-table-cell>
      <sp-table-cell>PDF</sp-table-cell>
      <sp-table-cell>89 KB</sp-table-cell>
    </sp-table-row>
    <sp-table-row>
      <sp-table-cell>Onboarding</sp-table-cell>
      <sp-table-cell>XLS</sp-table-cell>
      <sp-table-cell>120 KB</sp-table-cell>
    </sp-table-row>
  </sp-table-body>
</sp-table>
For large amounts of data, the `<sp-table>` can be virtualised to easily add table rows by using properties.

<sp-table id="table-virtualized-demo" style="height: 200px" scroller="true">
    <sp-table-head>
        <sp-table-head-cell>Column Title</sp-table-head-cell>
        <sp-table-head-cell>Column Title</sp-table-head-cell>
        <sp-table-head-cell>Column Title</sp-table-head-cell>
    </sp-table-head>
</sp-table>
<script type="module"> const initItems = (count) => { const total = count; const items = []; while (count) { count--; items.push({ name: String(total - count), date: count, }); } return items; }; const initTable = () => { const table = document.querySelector('#table-virtualized-demo'); table.items = initItems(50); table.renderItem = (item, index) => { const cell1 = document.createElement('sp-table-cell'); const cell2 = document.createElement('sp-table-cell'); const cell3 = document.createElement('sp-table-cell'); cell1.textContent = `Row Item Alpha ${item.name}`; cell2.textContent = `Row Item Alpha ${index}`; cell3.textContent = `Last Thing`; return [cell1, cell2, cell3]; } }; customElements.whenDefined('sp-table').then(() => { initTable(); });</script>
The virtualised table takes `items` as either a property or a JSON-encoded string, an array of type `Record`, where the key is a `string` and the value can be whatever you'd like. `items` is then fed into the `renderItem` method, which takes an `item` and its `index` as parameters and renders the `<sp-table-row>` for each item. An example is as follows:

const renderItem = (item: Item, index: number): TemplateResult => {
    return html` <sp-table-cell>Rowsaa Item Alpha ${item.name}</sp-table-cell> <sp-table-cell>Row Item Alpha ${item.date}</sp-table-cell> <sp-table-cell>Row Item Alpha ${index}</sp-table-cell> `;
};
`renderItem` is then included as a property of `<sp-table>`, along with the `items`, to render a full `<sp-table>` without excessive manual HTML writing.

You can also render a different cell at a particular index by doing something like below:

const renderItem = (item: Item, index: number): TemplateResult => {
    if (index === 15) {
        return html` <sp-table-cell style="text-align: center">Custom Row</sp-table-cell> `;
    }
    return html` <sp-table-cell>Row Item ${item.name}</sp-table-cell> <sp-table-cell>Row Item ${item.date}</sp-table-cell> <sp-table-cell>Row Item ${index}</sp-table-cell> `;
};
Please note that there is a bug when attempting to select all virtualised elements. The items are selected programatically, it's just not reflected visually.

By default the `selected` property will surface an array of item indexes that are currently selected. However, when making a selection on a virtualized table, it can be useful to track selection as something other than indexes. To do so, set a custom method for the `itemValue` property. The `itemValue` method accepts an item and its index as arguments and should return the value you would like to track in the `selected` property.

For accessibility, each checkbox in a virtualized table needs an accessible label. By default, the label is "Select row N" where N is the row number. You can customize this using the `itemLabel` property to provide more meaningful labels based on your item data:

table.itemLabel = (item, index) => item.name || `Select row ${index + 1}`;<sp-table id="table-item-value-demo" style="height: 200px" scroller="true" selects="multiple">
    <sp-table-head>
        <sp-table-head-cell>Column Title</sp-table-head-cell>
        <sp-table-head-cell>Column Title</sp-table-head-cell>
        <sp-table-head-cell>Column Title</sp-table-head-cell>
    </sp-table-head>
</sp-table>
<div class="selection">Selected: [ ]</div>
<script type="module"> const initItems = (count) => { const total = count; const items = []; while (count) { count--; items.push({ id: crypto.randomUUID(), name: String(total - count), date: count, }); } return items; }; const initTable = () => { const table = document.querySelector('#table-item-value-demo'); table.items = initItems(50); table.renderItem = (item, index) => { const cell1 = document.createElement('sp-table-cell'); const cell2 = document.createElement('sp-table-cell'); const cell3 = document.createElement('sp-table-cell'); cell1.textContent = `Row Item Alpha ${item.name}`; cell2.textContent = `Row Item Alpha ${index}`; cell3.textContent = `Last Thing`; return [cell1, cell2, cell3]; }; table.addEventListener('change', (event) => { const selected = event.target.nextElementSibling; selected.textContent = `Selected: ${JSON.stringify(event.target.selected, null, ' ')}`; }); }; customElements.whenDefined('sp-table').then(() => { initTable(); });</script>
All values in the item array are assumed to be homogenous by default. This means all of the rendered rows are either delivered as provided, or, in the case you are leveraging `selects`, rendered with an `<sp-table-checkbox-cell>`. However, when virtualizing a table with selection, it can sometimes be useful to surface rows with additional interactions, e.g. "Load more data" links. To support that, you can optionally include the `_$rowType$` brand in your item. The values for this are outlined by the `RowType` enum and include `ITEM` (0) and `INFORMATION` (1). When `_$rowType$: RowType.INFORMATION` is provided, it instructs the `<sp-table>` not to deliver an `<sp-table-checkbox-cell>` in that row.

<sp-table id="table-row-type-demo" style="height: 200px" scroller="true" selects="single">
    <sp-table-head>
        <sp-table-head-cell>Column Title</sp-table-head-cell>
        <sp-table-head-cell>Column Title</sp-table-head-cell>
        <sp-table-head-cell>Column Title</sp-table-head-cell>
    </sp-table-head>
</sp-table>
<script type="module"> const initItems = (count) => { const total = count; const items = []; while (count) { count--; items.push({ name: String(total - count), date: count, }); } return items; }; const initTable = () => { const table = document.querySelector('#table-row-type-demo'); const items = initItems(50); items.splice(3, 0, { _$rowType$: 1, }); table.items = items; table.renderItem = (item, index) => { if (item._$rowType$ === 1) { const infoCell = document.createElement('sp-table-cell'); infoCell.textContent = 'Use this row type for non-selectable content.'; return [infoCell]; } const cell1 = document.createElement('sp-table-cell'); const cell2 = document.createElement('sp-table-cell'); const cell3 = document.createElement('sp-table-cell'); cell1.textContent = `Row Item Alpha ${item.name}`; cell2.textContent = `Row Item Alpha ${index}`; cell3.textContent = `Last Thing`; return [cell1, cell2, cell3]; }; }; customElements.whenDefined('sp-table').then(() => { initTable(); });</script>
By default, the virtualized table doesn't contain a scroll bar and will display the entire length of the table body. Use the `scroller` property and specify an inline style for the height to get a `Table` of your desired height that scrolls.

The virtualized table supports sorting its elements.

For each table column you want to sort, use the `sortable` attribute in its respective `<sp-table-head-cell>`. `sort-direction="asc"|"desc"` specifies the direction the sort goes, in either ascending or descending order, respectively. The `@sorted` event listener on `<sp-table>` can be utilised to specify a method to fire when the `<sp-table-head-cell>` dispatches the `sorted` event. To specify which aspect of an item you'd like to sort by, use the `sort-key` attribute.

<sp-table id="sorted-virtualized-table" style="height: 200px" scroller="true">
    <sp-table-head>
        <sp-table-head-cell sortable sort-direction="desc" sort-key="name">
            Sortable Column
        </sp-table-head-cell>
        <sp-table-head-cell>Non-sortable Column</sp-table-head-cell>
        <sp-table-head-cell>Non-sortable Column</sp-table-head-cell>
    </sp-table-head>
</sp-table>
<script type="module"> const initItems = (count) => { const total = count; const items = []; while (count) { count--; items.push({ name: String(total - count), date: count, }); } return items; } let items = initItems(50); const initTable = () => { const table = document.querySelector('#sorted-virtualized-table'); table.items = items; table.renderItem = (item, index) => { const cell1 = document.createElement('sp-table-cell'); const cell2 = document.createElement('sp-table-cell'); const cell3 = document.createElement('sp-table-cell'); cell1.textContent = `Row Item Alpha ${item.name}`; cell2.textContent = `Row Item Beta ${item.date}`; cell3.textContent = `Index: ${index}`; return [cell1, cell2, cell3]; } table.addEventListener('sorted', (event) => { const { sortDirection, sortKey } = event.detail; items = items.sort((a, b) => { const first = String(a[sortKey]); const second = String(b[sortKey]); return sortDirection === 'asc' ? first.localeCompare(second) : second.localeCompare(first); }); table.items = [...items]; }); }; customElements.whenDefined('sp-table').then(() => { initTable(); });</script>
The `<sp-table>` component provides accessibility support for tabular data:

The table automatically manages ARIA attributes for proper semantic structure:

*   `role="grid"` on the table element
*   `role="row"` on each table row
*   `role="columnheader"` on header cells
*   `role="gridcell"` on data cells
*   `role="rowgroup"` on table body
*   `aria-sort` on sortable column headers
*   `aria-selected` on selectable rows
*   `aria-hidden` on single selection checkboxes
*   `aria-rowindex` on virtualized table rows
*   `aria-rowcount` on virtualized tables

When using row selection:

*   `aria-selected` is applied to selectable rows
*   Selection state is announced to screen readers
*   Checkboxes in selection cells are properly labelled for screen readers

All selection checkboxes have accessible labels to comply with WCAG 4.1.2 (Name, Role, Value). The labels are applied via `aria-label` on the checkbox's internal input element.

| Checkbox location | Default label | Customization |
| --- | --- | --- |
| Header (select all) | "Select All" | Use `select-all-label` attribute |
| Body rows (non-virtualized) | First cell's text content | Automatic |
| Body rows (virtualized) | "Select row N" | Use `itemLabel` property |

Example of customizing labels:

<sp-table selects="multiple" select-all-label="Select all documents">
  ...
</sp-table>
table.itemLabel = (item, index) => `Select ${item.fileName}`;
Sortable column headers support keyboard interaction:

*   **Space** - Activates the header and sorts on keyup
*   **Enter** - Immediately sorts the column
*   **Numpad Enter** - Immediately sorts the column
*   **Tab** - Navigates to sortable headers (only sortable headers are focusable)

Selectable rows support keyboard interaction:

*   **Click** - Toggles row selection

*   **Tab** - Navigates through focusable elements

*   **Tab** - Table body automatically receives `tabindex="0"` when content is scrollable

*   **Mouse wheel** - Scrolls through table content when focused

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/checkbox@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2

*   #5976`cdf6a24` Thanks @Rajdeepc! - **Fixed**: Fixed accessibility violation (WCAG 4.1.2) where table checkbox inputs were missing accessible labels. The axe DevTools "Form elements must have labels" error is now resolved. The fix sets `aria-label` directly on the checkbox's internal input element.

*   Updated dependencies [`95e1c25`]:

    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/checkbox@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/checkbox@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/checkbox@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/checkbox@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/checkbox@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/checkbox@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/checkbox@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   #5349`a9727d2` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/checkbox@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies [`a4de4c7`]: 
    *   @spectrum-web-components/checkbox@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/checkbox@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies [`468314f`]: 
    *   @spectrum-web-components/checkbox@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

*   add keyboard handlers to sp-table-cell-head (#4473) (794263e)

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

*   **table:** Add aria-rowcount to virtualized tables (#4156) (b4136ab)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

*   **table:** update row selection aria (6c8c706)

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

*   **table:** migrate to core tokens (#3441) (b866bab)

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

*   **table:** include all dependencies, @lit-labs/observers was missing (98d0370)

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

*   add missing "elements.js" export for sp-table component (ab8e2a7)
*   prevent runaway event listeners by not rendering while disconnected (aa8e8b2)
*   **table:** add resize controller to TableBody for a11y reasons (85dd406)
*   **table:** allow "change" events from table row content (97699a0)
*   **table:** allow tablebody to be resized via flex-grow (f797202)
*   **table:** update element tag in sp table sub components (4e94d70)
*   **table:** update sp-table import in elements.js (0cfe25a)
*   update timing to support non-virtualized rows (11ff752)

*   select row when clicking row (294523c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

*   **table:** allow "change" events from table row content (97699a0)

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

*   **table:** allow tablebody to be resized via flex-grow (f797202)
*   **table:** update element tag in sp table sub components (4e94d70)
*   **table:** update sp-table import in elements.js (0cfe25a)

**Note:** Version bump only for package @spectrum-web-components/table

*   add missing "elements.js" export for sp-table component (ab8e2a7)

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

**Note:** Version bump only for package @spectrum-web-components/table

*   update timing to support non-virtualized rows (11ff752)
*   **table:** add resize controller to TableBody for a11y reasons (85dd406)
*   prevent runaway event listeners by not rendering while disconnected (aa8e8b2)

*   select row when clicking row (294523c)

Property  Attribute  Type  Default  Description `density``density``'compact' | 'spacious' | undefined` Changes the spacing around table cell content. `emphasized``emphasized``boolean``false` Deliver the Table with additional visual emphasis to selected rows. `itemLabel``itemLabel` A function to extract the accessible label for a row's checkbox from an item. By default, returns a generic label based on the row index. Override this to provide more meaningful labels for accessibility in virtualized tables. `itemValue``itemValue` The value of an item. By default, it is set to the index of the sp-table-row. `items``items``Record<string, unknown>[]``[]` The content of the rows rendered by the virtualized table. The key is the value of the sp-table-row, and the value is the sp-table-row's content (not the row itself). `quiet``quiet``boolean``false` Display with "quiet" variant styles. `role``role``string``'grid'``scroller``scroller``boolean``false` Whether or not the virtualized table has a scroll bar. If this is set to true, make sure to specify a height in the sp-table's inline styles. `selectAllLabel``select-all-label``string``'Select All'` The accessible label for the "select all" checkbox in the table header. Defaults to 'Select All'. `selected``selected``string[]``[]` An array of  values that have been selected. `selects``selects``undefined | 'single' | 'multiple'` Whether the Table allows users to select a row or rows, and thus controls whether or not the Table also renders checkboxes.

Name  Type  Description `change``Event``Announces a change in the `selected` property of a table row``undefined``RangeChangedEvent``rangeChanged``Event``Announces a change in the range of visible cells on the table body`
