# Source: https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops

Title: React Data Grid API GridProps - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops

Markdown Content:
#### [adaptive?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#adaptive)```
boolean
```Providing different rendering of the popup element based on the screen dimensions.
#### [adaptiveTitle?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#adaptivetitle)```
string
```Specifies the text that is rendered as title in the adaptive popup.
#### [autoProcessData?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#autoprocessdata)```
boolean | { filter?: boolean; group?: boolean; page?: boolean; search?: boolean; sort?: boolean; }
``````
false
```Enables data-processing inside the GridComponent based on its state. Provides an easy, built-in way to handle data operations like sorting, filtering, grouping, and paging.

jsx

```
<Grid
  autoProcessData={{
    filter: true,
    search: true,
    sort: true,
    group: true,
    page: true
  }}
/>
```
#### [cells?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#cells)```
GridCellsSettings
```Defines a set of custom cell components that the Grid will render instead of the default cells.

jsx

```
import { GridCustomCellProps } from '@progress/kendo-react-grid';

const CustomCell = (props: GridCustomCellProps) => (
  <td {...props.tdProps}>
    {props.dataItem[props.field]}
  </td>
);

<Grid
  cells={{
    data: CustomCell
  }}
/>
```
#### [children?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#children)```
React.ReactNode
```Determines the children nodes.
#### [className?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#classname)```
string
```Sets a class for the Grid DOM element.

jsx

`<Grid className="custom-grid-class" />`
#### [clipboard?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#clipboard)```
boolean | ClipboardSettings
```Enables clipboard copy, cut, and paste manipulations. Accepts `ClipboardSettings` or a boolean value.

jsx

`<Grid clipboard={true}  />`
#### [columnMenu?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#columnmenu)```
"null" | ComponentType<GridColumnMenuProps>
```Specifies a React element that will be cloned and rendered inside the column menu of the Grid.

jsx

`<Grid columnMenu={() => <div>Custom Column Menu</div>} />`
#### [columnMenuIcon?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#columnmenuicon)```
SVGIcon
```Globally overrides the default (three vertical dots) column menu icon for the whole Grid. If set, the prop can be overridden on column level using the ([menuIcon](https://www.telerik.com/kendo-react-ui/components/grid/api/gridcolumnprops#menuicon)) property.
#### [columnsState?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#columnsstate)```
GridColumnState[]
```The collection of column states of the grid.

jsx

`<Grid columnsState={[{ field: 'ProductName', locked: true }]} />`
#### [columnVirtualization?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#columnvirtualization)```
boolean
```Enables virtualization of the columns. If virtualization is enabled, the columns outside the view are not rendered.

jsx

`<Grid columnVirtualization={true} />`
#### [contextMenu?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#contextmenu)```
boolean | GridContextMenuOptions | (options: GridCellBaseOptions) => boolean | GridContextMenuOptions
```Specifies the context menu settings applied to the Grid.

jsx

`<Grid contextMenu={true} />`
#### [csv?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#csv)```
boolean | GridCSVExportOptions
```Enables CSV export functionality when set to `true` or provides CSV export configuration options.

jsx

`<Grid csv={true} />`

jsx

`<Grid csv={{ delimiter: ';', includeUTF8BOM: true, preventFormulaInjection: true }} />`
#### [data?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#data)```
"null" | any[] | DataResult
```Sets the data of the Grid ([see example](https://www.telerik.com/kendo-react-ui/components/grid/paging)). If you use paging, the `data` option has to contain only the items for the current page. It takes values of type null, any or [DataResult](https://www.telerik.com/kendo-react-ui/components/datatools/api/dataresult) Accepts values of type `null`, `any[]`, or `DataResult`.

jsx

`<Grid data={data} />`
#### [dataItemKey?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#dataitemkey)```
string
```Sets the Grid row key prop to the value of this field in the dataItem. If not set, the dataItem index will be used for the row key, which might lead to rows not updating during paging or scrolling.

jsx

`<Grid dataItemKey="ID" />`
#### [dataLayoutMode?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#datalayoutmode)```
GridDataLayoutMode
``````
"columns"
```Specifies the data layout mode for the Grid.

*   `"columns"`: Traditional column-based table layout (default).
*   `"stacked"`: Card-based layout where each row displays as a vertical stack of field label/value pairs. Useful for responsive layouts and mobile devices.

The stacked mode is independent of `adaptiveMode` and can be used separately.

> Note: Row/column spanning is not supported in stacked mode.

tsx

```
// Traditional column layout (default)
<Grid dataLayoutMode="columns" data={data}>
  <GridColumn field="name" title="Name" />
  <GridColumn field="email" title="Email" />
</Grid>

// Stacked card layout
<Grid dataLayoutMode="stacked" data={data}>
  <GridColumn field="name" title="Name" />
  <GridColumn field="email" title="Email" />
</Grid>
```
#### [defaultColumnsState?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultcolumnsstate)```
GridColumnState[]
```The default columns state, used only for the initial load.

jsx

`<Grid defaultColumnsState={[{ field: 'ProductName', locked: false }]} />`
#### [defaultDetailExpand?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultdetailexpand)```
DetailExpandDescriptor
```The default `detailExpand` state applied to the Grid when using uncontrolled mode.

jsx

`<Grid defaultDetailExpand={{ ['item-data-key-id']: true }} />`
#### [defaultEdit?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultedit)```
EditDescriptor
```The default `edit` state applied to the Grid when using uncontrolled mode.

jsx

`<Grid defaultEdit={{ ['item-data-key-id']: true }} />`
#### [defaultFilter?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultfilter)```
CompositeFilterDescriptor
```The default `filter` state applied to the Grid when using uncontrolled mode.

jsx

`<Grid defaultFilter={{ logic: 'and', filters: [{ field: 'name', operator: 'contains', value: 'John' }] }} />`
#### [defaultGroup?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultgroup)```
GroupDescriptor[]
```The default `group` state applied to the Grid when using uncontrolled mode.

jsx

`<Grid defaultGroup={[{ field: 'CategoryName' }]} />`
#### [defaultGroupExpand?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultgroupexpand)```
GroupExpandDescriptor[]
```The default `groupExpand` state applied to the Grid when using uncontrolled mode.

jsx

`<Grid defaultGroupExpand={[{ field: 'CategoryName', expanded: true }]} />`
#### [defaultSearch?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultsearch)```
CompositeFilterDescriptor
```The descriptor by which the data is searched by default. Its first FilterDescriptor populates the GridSearchBox.

jsx

`<Grid defaultSearch={{ logic: 'or', filters: [{ field: 'category', operator: 'eq', value: 'electronics' }] }} />`
#### [defaultSelect?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultselect)```
SelectDescriptor
```The default `select` state applied to the Grid when using uncontrolled mode.

jsx

`<Grid defaultSelect={{ ['item-data-key-id']: true }} />`
#### [defaultSkip?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultskip)```
number
```The default `skip` state applied to the Grid when using uncontrolled mode.

jsx

`<Grid defaultSkip={10} />`
#### [defaultSort?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultsort)```
SortDescriptor[]
```The default `sort` state applied to the Grid when using uncontrolled mode. ([see example](https://www.telerik.com/kendo-react-ui/components/grid/sorting))

jsx

`<Grid defaultSort={[{ field: 'name', dir: 'asc' }]} />`
#### [defaultTake?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaulttake)```
number
```The default `take` state applied to the Grid when using uncontrolled mode.

jsx

`<Grid defaultTake={20} />`
#### [detail?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#detail)```
"null" | ComponentType<GridDetailRowProps>
```Specifies a React element that will be cloned and rendered inside the detail rows of the currently expanded items ([see example](https://www.telerik.com/kendo-react-ui/components/grid/hierarchy)).

jsx

`<Grid detail={()=>(<div>Detail Content</div>)} />`
#### [detailExpand?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#detailexpand)```
DetailExpandDescriptor
```The descriptor by which the detail row is expanded.

jsx

`<Grid detailExpand={{ ['item-data-key-id']: true }} />`
#### [detailRowHeight?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#detailrowheight)```
number
```Defines the detail row height and forces an equal height to all detail rows.

jsx

`<Grid detailRowHeight={100} />`
#### [edit?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#edit)```
EditDescriptor
```The descriptor by which the in-edit mode of an item is defined.

jsx

`<Grid edit={{ ['item-data-key-id']: true }} />`
#### [editable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#editable)```
boolean | GridEditableSettings
```The Grid editable settings.

jsx

`<Grid editable={{ enabled: true, mode: 'inline' }} />`
#### [editDialog?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#editdialog)```
(props: GridEditDialogProps) => ReactNode
```Sets a custom edit dialog component that the Grid will render instead of the built-in edit dialog.
#### [filter?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#filter)```
CompositeFilterDescriptor
```The [descriptor](https://www.telerik.com/kendo-react-ui/components/datatools/api/compositefilterdescriptor) by which the data is filtered ([more information and examples](https://www.telerik.com/kendo-react-ui/components/grid/filtering)). This affects the values and buttons in the `FilterRow` of the Grid.

jsx

`<Grid filter={{ logic: 'and', filters: [{ field: 'name', operator: 'contains', value: 'John' }] }} />`
#### [filterable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#filterable)```
boolean
```Enables filtering for the columns with their `field` option set.

jsx

`<Grid filterable={true} />`
#### [filterOperators?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#filteroperators)```
GridFilterOperators
```The filter operators for the Grid filters.

jsx

`<Grid filterOperators={{ text: [{ text: 'grid.filterContainsOperator', operator: 'contains' }] }} />`
#### [fixedScroll?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#fixedscroll)```
boolean
```Determines if the scroll position will be updated after a data change. If set to `true`, the scroll will remain in the same position.
#### [group?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#group)```
GroupDescriptor[]
```The [descriptors](https://www.telerik.com/kendo-react-ui/components/datatools/api/groupdescriptor)[] by which the data will be grouped ([more information and examples](https://www.telerik.com/kendo-react-ui/components/grid/grouping)).

jsx

`<Grid group={[{ field: 'CategoryName' }]} />`
#### [groupable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#groupable)```
boolean | GridGroupableSettings
```Determines if grouping by dragging and dropping the column headers is allowed ([more information and examples](https://www.telerik.com/kendo-react-ui/components/grid/grouping)).

jsx

`<Grid groupable={true} />`
#### [groupExpand?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#groupexpand)```
GroupExpandDescriptor[]
```The descriptor by which the group is expanded.

jsx

`<Grid groupExpand={[{ field: 'CategoryName', expanded: true }]} />`
#### [highlight?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#highlight)```
GridHighlightDescriptor
```The descriptor by which the highlight state of an item is defined. Passing a boolean value will highlight the whole row, while passing an object will highlight individual cells by their field.

jsx

```
<Grid highlight={{ ['item-data-key-id']: true }} />
<Grid highlight={{ ['item-data-key-id']: [2, 3] }} />
```
#### [id?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#id)```
string
```Sets the `id` property of the top div element of the component.

jsx

`<Grid id="custom-grid-id" />`
#### [language?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#language)```
string
```Sets the language of the Grid when used as a server component. Have not effect when the Grid is used as a client component.

jsx

`<Grid language="en" />`
#### [loader?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#loader)```
React.ReactNode
```A custom component that the Grid will render instead of the built-in loader.

jsx

`<Grid loader={<div>Custom Loader...</div>} />`
#### [locale?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#locale)```
string
```Sets the locale of the Grid when used as a server component. Have not effect when the Grid is used as a client component.

jsx

`<Grid locale="en-US" />`
#### [lockGroups?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#lockgroups)```
boolean
```Defines if the group descriptor columns are locked (frozen or sticky). Locked columns are the columns that are visible at all times while the user scrolls the component horizontally. Defaults to `false`.

jsx

`<Grid lockGroups={true} />`
#### [navigatable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#navigatable)```
boolean | NavigatableSettings
```If set to `true`, the user can use dedicated shortcuts to interact with the Grid. By default, navigation is disabled and the Grid content is accessible in the normal tab sequence.

jsx

`<Grid navigatable={true} />`
#### [onClipboard?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onclipboard)```
(event: GridClipboardEvent) => void
```Fires when clipboard support is enabled, and one of the actions (e.g., copy) is triggered. Accepts a `GridClipboardEvent` object.

jsx

```
<Grid
  clipboard={true}
  onClipboard={(event) => console.log('Clipboard action:', event.action)}
/>
```
#### [onColumnReorder?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#oncolumnreorder)```
(event: GridColumnReorderEvent) => void
```Fires when the columns are reordered.

jsx

`<Grid onColumnReorder={(event) => console.log('Column reordered:', event)} />`
#### [onColumnResize?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#oncolumnresize)```
(event: GridColumnResizeEvent) => void
```Fires when a column is resized. Only fired when the Grid is run as a client component.

jsx

`<Grid onColumnResize={(event) => console.log('Column resized:', event)} />`
#### [onColumnsStateChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#oncolumnsstatechange)```
(event: GridColumnsStateChangeEvent) => void
```Fires when the columns state of the Grid is changed.

jsx

`<Grid onColumnsStateChange={(event) => console.log('Columns state changed:', event)} />`
#### [onContextMenu?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#oncontextmenu)```
(event: GridContextMenuEvent) => void
```The event that is fired when the ContextMenu is activated. Only fired when the Grid is run as a client component.

jsx

`<Grid onContextMenu={(event) => console.log('Context menu activated:', event)} />`
#### [onContextMenuItemClick?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#oncontextmenuitemclick)```
(event: GridContextMenuItemClickEvent) => void
```The event that is fired when the ContextMenu item is clicked. Only fired when the Grid is run as a client component.

jsx

`<Grid onContextMenuItemClick={(event) => console.log('Context menu item clicked:', event)} />`
#### [onCsvExport?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#oncsvexport)```
(data: any[]) => any[]
```Fires when the user clicks the CSV export button. Allows custom data transformation before export.

jsx

```
<Grid onCsvExport={(data) => {
    return data.filter(item => item.active);
}} />
```
#### [onDataStateChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#ondatastatechange)```
(event: GridDataStateChangeEvent) => void
```Fires when the data state of the Grid is changed ([more information](https://www.telerik.com/kendo-react-ui/components/grid/data-operations/local-operations) and [example](https://www.telerik.com/kendo-react-ui/components/grid/data-operations/odata-server-operations)).

jsx

`<Grid onDataStateChange={(event) => console.log('Data state changed:', event)} />`
#### [onDetailExpandChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#ondetailexpandchange)```
(event: GridDetailExpandChangeEvent) => void
```Fires when the user expands or collapses a detail row.

jsx

`<Grid onDetailExpandChange={(event) => console.log('Detail expand changed:', event)} />`
#### [onEditChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#oneditchange)```
(event: GridEditChangeEvent) => void
```Fires when the user enters or exits an in-edit mode of a row or cell.

jsx

`<Grid onEditChange={(event) => console.log('Edit changed:', event)} />`
#### [onFilterChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onfilterchange)```
(event: GridFilterChangeEvent) => void
```Fires when the Grid filter is modified through the UI. You must handle the event and filter the data.

jsx

```
<Grid
  filterable={true}
  onFilterChange={(event) => console.log('Filter changed:', event.filter)}
/>
```
#### [onGroupChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#ongroupchange)```
(event: GridGroupChangeEvent) => void
```Fires when the grouping of the Grid is changed. You have to handle the event yourself and group the data ([more information and examples](https://www.telerik.com/kendo-react-ui/components/grid/grouping)).

jsx

`<Grid onGroupChange={(event) => console.log('Group changed:', event.group)} />`
#### [onGroupExpandChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#ongroupexpandchange)```
(event: GridGroupExpandChangeEvent) => void
```Fires when the user expands or collapses a group.

jsx

`<Grid onGroupExpandChange={(event) => console.log('Group expand changed:', event)} />`
#### [onHeaderSelectionChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onheaderselectionchange)```
(event: GridHeaderSelectionChangeEvent) => void
```Fires when the user clicks the checkbox of a column header whose type is set to `checkbox`.

jsx

`<Grid onHeaderSelectionChange={(event) => console.log('Header selection changed:', event)} />`
#### [onHighlightChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onhighlightchange)```
(event: GridHighlightChangeEvent) => void
```Fires when the Grid highlight is modified. You must handle the event and filter the data.

jsx

```
<Grid
  onHighlightChange={(event) => console.log('Highlight changed:', event.highlight)}
/>
```
#### [onItemChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onitemchange)```
(event: GridItemChangeEvent) => void
```Fires when the user changes the values of the item.

jsx

`<Grid onItemChange={(event) => console.log('Item changed:', event)} />`
#### [onKeyDown?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onkeydown)```
(event: GridKeyDownEvent) => void
```Fires when the user press keyboard key. Only fired when the Grid is run as a client component.

jsx

`<Grid onKeyDown={(event) => console.log('Key pressed:', event)} />`
#### [onNavigationAction?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onnavigationaction)```
(event: GridNavigationActionEvent) => void
```Fires when Grid keyboard navigation position is changed. Only fired when the Grid is run as a client component.

jsx

`<Grid onNavigationAction={(event) => console.log('Navigation action:', event)} />`
#### [onPageChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onpagechange)```
(event: GridPageChangeEvent) => void
```Fires when the page of the Grid is changed.

jsx

`<Grid onPageChange={(event) => console.log('Page changed:', event.page)} />`
#### [onPdfExport?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onpdfexport)```
(event: { target: HTMLDivElement; }) => Promise<void>
```Fires when the user clicks the PDF export button.

jsx

```
<Grid onPdfExport={async (event) => {
       const pdf = await import('@progress/kendo-react-pdf');
       await pdf.saveGridPDF(event.target);
 }} />
```
#### [onRowClick?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onrowclick)```
(event: GridRowClickEvent) => void
```Fires when the user clicks a row.

jsx

`<Grid onRowClick={(event) => console.log('Row clicked:', event)} />`
#### [onRowDoubleClick?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onrowdoubleclick)```
(event: GridRowDoubleClickEvent) => void
```Fires when the user double clicks a row.

jsx

`<Grid onRowDoubleClick={(event) => console.log('Row double clicked:', event)} />`
#### [onRowReorder?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onrowreorder)```
(event: GridRowReorderEvent) => void
```Fires when the user reorders a row.

jsx

`<Grid onRowReorder={(event) => console.log('Row reordered:', event)} />`
#### [onScroll?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onscroll)```
(event: GridEvent) => void
```Fires when Grid is scrolled. Only fired when the Grid is run as a client component.

jsx

`<Grid onScroll={(event) => console.log('Grid scrolled:', event)} />`
#### [onSearchChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onsearchchange)```
(event: GridSearchChangeEvent) => void
```Fires when the search value of the GridSearchBox is changed.

jsx

`<Grid onSearchChange={(event) => console.log('Search changed:', event)} />`
#### [onSelectionChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onselectionchange)```
(event: GridSelectionChangeEvent) => void
```Fires when the user tries to select or deselect a row or cell.

jsx

`<Grid onSelectionChange={(event) => console.log('Selection changed:', event)} />`
#### [onSortChange?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onsortchange)```
(event: GridSortChangeEvent) => void
```Fires when the sorting of the Grid is changed. You must handle the event and sort the data. ([see example](https://www.telerik.com/kendo-react-ui/components/grid/sorting))

jsx

```
<Grid
  sortable={true}
  onSortChange={(event) => console.log('Sort changed:', event.sort)}
/>
```
#### [pageable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pageable)```
boolean | GridPagerSettings
```Configures the pager of the Grid. Accepts `GridPagerSettings` or a boolean value.([see example](https://www.telerik.com/kendo-react-ui/components/grid/paging))

The available options are:

*   `buttonCount: Number`—Sets the maximum numeric buttons count before the buttons are collapsed.
*   `info: Boolean`—Toggles the information about the current page and the total number of records.
*   `type: PagerType`—Accepts the `numeric` (buttons with numbers) and `input` (input for typing the page number) values.
*   `pageSizes: Boolean` or `Array<number>`—Shows a menu for selecting the page size.
*   `pageSizeValue: String or Number`—Sets the selected value of the page size Dropdownlist. It is useful when the selected value could also be a string not only a number.
*   `previousNext: Boolean`—Toggles the **Previous** and **Next** buttons.
*   `navigatable: Boolean`—Defines if the pager will be navigatable.
*   `responsive: Boolean`—Defines if the pager will be responsive. If true, hides the tools that do not fit to the available space.
*   `adaptive: Boolean`—Providing different rendering of the page sizes select element based on the screen dimensions.
*   `adaptiveTitle: String`—Specifies the text that is rendered as title in the adaptive page sizes select element.

jsx

`<Grid pageable={{ pageSizes: true }} />`
#### [pager?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pager)```
"null" | ComponentType<PagerProps>
```The pager component that the Grid will render instead of the built-in pager. It takes values of type null and ComponentType<[PagerProps](https://www.telerik.com/kendo-react-ui/components/datatools/api/pagerprops)&gt

jsx

`<Grid pager={() => <div>Custom Pager</div>} />`
#### [pageSize?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pagesize)```
number
```Defines the page size used by the Grid pager. Required for paging functionality.

jsx

`<Grid pageSize={10} />`
#### [pdf?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pdf)```
boolean | GridProps
```When set to true the Grid pdf export will be enabled. If set to an object, the Grid will use the provided settings to export the PDF.

jsx

`<Grid pdf={true} />`
#### [reorderable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#reorderable)```
boolean
```If set to `true`, the user can reorder columns by dragging their header cells ([see example](https://www.telerik.com/kendo-react-ui/components/grid/columns/reordering)).

jsx

`<Grid reorderable={true} />`
#### [resizable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#resizable)```
boolean
```If set to `true`, the user can resize columns by dragging the edges (resize handles) of their header cells ([see example](https://www.telerik.com/kendo-react-ui/components/grid/columns/resizing)).

jsx

`<Grid resizable={true} />`
#### [rowHeight?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#rowheight)```
number
```Defines the row height and forces an equal height to all rows ([see example](https://www.telerik.com/kendo-react-ui/components/grid/scroll-modes)).

jsx

`<Grid rowHeight={50} />`
#### [rowReorderable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#rowreorderable)```
boolean | GridRowReorderSettings
```Defines the row reorder settings.

jsx

`<Grid rowReorderable={true} />`
#### [rows?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#rows)```
GridRowsSettings
```jsx

```
import { GridCustomRowProps } from '@progress/kendo-react-grid';

const CustomRow = (props: GridCustomRowProps) => (
  <tr {...props.trProps} style={{ backgroundColor: props.dataItem?.highlight ? 'yellow' : 'white' }}>
    {props.children}
  </tr>
);

<Grid
  rows={{
    data: CustomRow
  }}
/>
```
#### [rowSpannable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#rowspannable)```
boolean | GridRowSpannableSettings
```Enables the built-in row span feature of the Grid.

jsx

`<Grid rowSpannable={true} />`
#### [scrollable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#scrollable)```
ScrollMode
```Defines the scroll mode that is used by the Grid ([see example](https://www.telerik.com/kendo-react-ui/components/grid/scroll-modes)).

The available options are:

*   `none`—Renders no scrollbar.
*   `scrollable`—This is the default scroll mode. It requires the setting of the `height` option.
*   `virtual`—Displays no pager and renders a portion of the data (optimized rendering) while the user is scrolling the content.

jsx

`<Grid scrollable="virtual" />`
#### [search?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#search)```
CompositeFilterDescriptor
```The descriptor by which the data is searched. Its first FilterDescriptor populates the GridSearchBox.

jsx

`<Grid search={{ logic: 'and', filters: [{ field: 'name', operator: 'contains', value: 'test' }] }} />`
#### [searchFields?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#searchfields)```
string | SearchField[]
```Defines the fields of the data that are filtered by the GridSearchBox.

jsx

`<Grid searchFields={['name', 'category']} />`
#### [select?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#select)```
SelectDescriptor
```The [descriptor](https://www.telerik.com/kendo-react-ui/components/datatools/api/selectdescriptor) by which the selected state of an item is defined. Passing a boolean value will select the whole row, while passing an array of strings will select individual.

jsx

`<Grid select={{ ['item-data-key-id']: true }} />`
#### [selectable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#selectable)```
boolean | GridSelectableSettings
```The Grid selectable settings.

jsx

`<Grid selectable={{ enabled: true, mode: 'single' }} />`
#### [showLoader?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#showloader)```
boolean
```Specifies whether the loader of the Grid will be displayed.

jsx

```
<Grid
  showLoader={true}
  loader={<div>Loading...</div>}
/>
```
#### [size?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#size)```
"small" | "medium"
``````
undefined (theme-controlled)
```Configures the `size` of the Grid.

The available options are:

*   small
*   medium

jsx

`<Grid size="small" />`
#### [skip?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#skip)```
number
```Defines the number of records that will be skipped by the pager ([see example](https://www.telerik.com/kendo-react-ui/components/grid/paging)). Required by the paging functionality.

jsx

`<Grid skip={10} />`
#### [sort?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#sort)```
SortDescriptor[]
```The ([descriptors](https://www.telerik.com/kendo-react-ui/components/datatools/api/sortdescriptor)) by which the data is sorted. Applies the sorting styles and buttons to the affected columns.

jsx

`<Grid sort={[{ field: 'name', dir: 'asc' }]} />`
#### [sortable?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#sortable)```
SortSettings
```Enables sorting for the columns with their `field` option set. ([see example](https://www.telerik.com/kendo-react-ui/components/grid/sorting))

jsx

`<Grid sortable={true} />`
#### [stackedLayoutSettings?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#stackedlayoutsettings)```
GridStackedLayoutSettings
```Configuration for the stacked layout mode. Only applicable when `dataLayoutMode="stacked"`.

The `cols` property defines how stacked cells are arranged:

*   As a number: Creates that many equal-width columns
*   As an array: The length defines column count, values define widths

tsx

```
// Two-column stacked layout with equal widths
<Grid
  dataLayoutMode="stacked"
  stackedLayoutSettings={{ cols: 2 }}
  data={data}
>
  <GridColumn field="name" title="Name" />
  <GridColumn field="email" title="Email" />
</Grid>

// Three columns with custom widths using fr units
<Grid
  dataLayoutMode="stacked"
  stackedLayoutSettings={{ cols: ['1fr', '2fr', '1fr'] }}
  data={data}
>
  ...
</Grid>

// Custom widths with pixel and fraction units
<Grid
  dataLayoutMode="stacked"
  stackedLayoutSettings={{ cols: [{ width: 200 }, { width: '1fr' }] }}
  data={data}
>
  ...
</Grid>
```
#### [style?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#style)```
React.CSSProperties
```Represents the `style` HTML attribute.

jsx

`<Grid style={{ backgroundColor: 'lightblue' }} />`
#### [take?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#take)```
number
```Alias for the `pageSize` property. If `take` is set, `pageSize` will be ignored.

jsx

`<Grid take={20} />`
#### [total?](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#total)```
number
```Defines the total number of data items in all pages. Required for paging functionality.

jsx

`<Grid total={100} />`
