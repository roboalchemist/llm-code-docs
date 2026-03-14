# Source: https://icflorescu.github.io/mantine-datatable/type-definitions/

Title: Type definitions | Mantine DataTable

URL Source: https://icflorescu.github.io/mantine-datatable/type-definitions/

Published Time: Tue, 20 Jan 2026 11:41:51 GMT

Markdown Content:
Type definitions | Mantine DataTable
===============

[Mantine DataTable =================](https://icflorescu.github.io/mantine-datatable/)

8.3.13

Search

[Source code](https://github.com/icflorescu/mantine-datatable)[287.6k/mo nth](https://www.npmjs.com/package/mantine-datatable)[Sponsor](https://github.com/sponsors/icflorescu)

[Home](https://icflorescu.github.io/mantine-datatable/)[Getting started](https://icflorescu.github.io/mantine-datatable/getting-started/)[Styling](https://icflorescu.github.io/mantine-datatable/styling/)

Examples

[Basic usage](https://icflorescu.github.io/mantine-datatable/examples/basic-usage/)[Basic table properties](https://icflorescu.github.io/mantine-datatable/examples/basic-table-properties/)[Overriding the default styles](https://icflorescu.github.io/mantine-datatable/examples/overriding-the-default-styles/)[Column properties and styling](https://icflorescu.github.io/mantine-datatable/examples/column-properties-and-styling/)[Column grouping](https://icflorescu.github.io/mantine-datatable/examples/column-grouping/)[Default column properties](https://icflorescu.github.io/mantine-datatable/examples/default-column-properties/)[Default column render](https://icflorescu.github.io/mantine-datatable/examples/default-column-render/)[Row styling](https://icflorescu.github.io/mantine-datatable/examples/row-styling/)[Non-standard record IDs](https://icflorescu.github.io/mantine-datatable/examples/non-standard-record-ids/)[Scrollable vs. auto-height](https://icflorescu.github.io/mantine-datatable/examples/scrollable-vs-auto-height/)[Scrolling a row into view](https://icflorescu.github.io/mantine-datatable/examples/scrolling-a-row-into-view/)[Empty state](https://icflorescu.github.io/mantine-datatable/examples/empty-state/)[Pagination](https://icflorescu.github.io/mantine-datatable/examples/pagination/)[Sorting](https://icflorescu.github.io/mantine-datatable/examples/sorting/)[Column dragging and toggling](https://icflorescu.github.io/mantine-datatable/examples/column-dragging-and-toggling/)[Row dragging](https://icflorescu.github.io/mantine-datatable/examples/row-dragging/)[Column resizing](https://icflorescu.github.io/mantine-datatable/examples/column-resizing/)[Infinite scrolling](https://icflorescu.github.io/mantine-datatable/examples/infinite-scrolling/)[Searching and filtering](https://icflorescu.github.io/mantine-datatable/examples/searching-and-filtering/)[Records selection](https://icflorescu.github.io/mantine-datatable/examples/records-selection/)[Handling row clicks](https://icflorescu.github.io/mantine-datatable/examples/handling-row-clicks/)[Handling cell clicks](https://icflorescu.github.io/mantine-datatable/examples/handling-cell-clicks/)[Using with Mantine ContextMenu](https://icflorescu.github.io/mantine-datatable/examples/using-with-mantine-contextmenu/)[Expanding rows](https://icflorescu.github.io/mantine-datatable/examples/expanding-rows/)[Nested tables](https://icflorescu.github.io/mantine-datatable/examples/nested-tables/)[Nested tables with async data loading](https://icflorescu.github.io/mantine-datatable/examples/nested-tables-with-async-data-loading/)[Nested tables with async data loading and sorting](https://icflorescu.github.io/mantine-datatable/examples/nested-tables-with-async-data-loading-and-sorting/)[Row actions cell](https://icflorescu.github.io/mantine-datatable/examples/row-actions-cell/)[Pinning the last column](https://icflorescu.github.io/mantine-datatable/examples/pinning-the-last-column/)[Pinning the first column](https://icflorescu.github.io/mantine-datatable/examples/pinning-the-first-column/)[RTL support](https://icflorescu.github.io/mantine-datatable/examples/rtl-support/)[Links or buttons inside clickable rows or cells](https://icflorescu.github.io/mantine-datatable/examples/links-or-buttons-inside-clickable-rows-or-cells/)[Disabling text selection](https://icflorescu.github.io/mantine-datatable/examples/disabling-text-selection/)[Asynchronous data loading](https://icflorescu.github.io/mantine-datatable/examples/asynchronous-data-loading/)[Custom row or cell attributes](https://icflorescu.github.io/mantine-datatable/examples/custom-row-or-cell-attributes/)[Using bodyRef with AutoAnimate](https://icflorescu.github.io/mantine-datatable/examples/using-with-auto-animate/)[Complex usage scenario](https://icflorescu.github.io/mantine-datatable/examples/complex-usage-scenario/)

[Type definitions](https://icflorescu.github.io/mantine-datatable/type-definitions/)[Mantine V6 support](https://icflorescu.github.io/mantine-datatable/mantine-v6-support/)[Contribute and support](https://icflorescu.github.io/mantine-datatable/contribute-and-support/)[Hire the author](https://icflorescu.github.io/mantine-datatable/hire-the-author/)[Changelog](https://github.com/icflorescu/mantine-datatable/blob/main/CHANGELOG.md)

[View source code](https://github.com/icflorescu/mantine-datatable)[Go to the npm package (287.6k/mo)](https://www.npmjs.com/package/mantine-datatable)[Sponsor the author](https://github.com/sponsors/icflorescu)

Type definitions
----------------

Mantine DataTable is written in TypeScript and the component properties are well documented with additional JSDoc annotations, so you can harness the full power of your IDE to build type safe applications with confidence.

Here are the Mantine DataTable type files:

DataTableCellClickHandler.ts

```
import type { DataTableColumn } from './DataTableColumn';

export type DataTableCellClickHandler<T = Record<string, unknown>> = (params: {
  /**
   * Click event.
   */
  event: React.MouseEvent;

  /**
   * Clicked record.
   */
  record: T;
  /**
   * Clicked record index.
   */
  index: number;
  /**
   * Clicked column information.
   */
  column: DataTableColumn<T>;
  /**
   * Clicked column index.
   */
  columnIndex: number;
}) => void;
```

Expand code

DataTableColorProps.ts

```
import type { MantineColor } from '@mantine/core';

export type DataTableColorProps<T> = {
  /**
   * Data table text color.
   * Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string),
   * or an object with `light` and `dark` keys and `MantineColor` values.
   */
  c?: MantineColor | { light: MantineColor; dark: MantineColor };

  /**
   * Data table background color.
   * Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string),
   * or an object with `light` and `dark` keys and `MantineColor` values.
   */
  backgroundColor?: MantineColor | { light: MantineColor; dark: MantineColor };

  /**
   * Color of table borders, applied to all borders except row borders.
   * Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string),
   * or an object with `light` and `dark` keys and `MantineColor` values.
   */
  borderColor?: MantineColor | { light: MantineColor; dark: MantineColor };

  /**
   * Color of row borders.
   * Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string),
   * or an object with `light` and `dark` keys and `MantineColor` values.
   */
  rowBorderColor?: MantineColor | { light: MantineColor; dark: MantineColor };

  /**
   * Background color of striped rows.
   * Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string),
   * or an object with `light` and `dark` keys and `MantineColor` values.
   */
  stripedColor?: MantineColor | { light: MantineColor; dark: MantineColor };

  /**
   * Background color of hover-highlighted row.
   * Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string),
   * or an object with `light` and `dark` keys and `MantineColor` values.
   */
  highlightOnHoverColor?: MantineColor | { light: MantineColor; dark: MantineColor };

  /**
   * Data table row text color.
   * A function that accepts row data and returns color.
   * The returned color can be a `MantineColor` (key of `theme.colors` or any valid CSS color string),
   * or an object with `light` and `dark` keys and `MantineColor` values.
   */
  rowColor?: (record: T, index: number) => MantineColor | undefined | { light: MantineColor; dark: MantineColor };

  /**
   * Data table row background color.
   * A function that accepts row data and returns background color color.
   * Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string),
   * or an object with `light` and `dark` keys and `MantineColor` values.
   */
  rowBackgroundColor?: (
    record: T,
    index: number
  ) => MantineColor | undefined | { light: MantineColor; dark: MantineColor };
};
```

Expand code

DataTableColumn.ts

```
import type { MantineStyleProp, MantineTheme, PopoverProps } from '@mantine/core';
import type { DataTableColumnTextAlign } from './DataTableColumnTextAlign';

export type DataTableColumn<T = Record<string, unknown>> = {
  /**
   * Column accessor.
   * You can use dot-notation for nested objects property drilling.
   * (i.e. `department.name` or `department.company.name`)
   */
  accessor: keyof T | (string & NonNullable<unknown>);

  /**
   * Optional column header title.
   * If not present, one will be generated by "humanizing" the provided column accessor.
   * (i.e. `firstName` -> `First name`; `user.firstName` -> `User first name`)
   */
  title?: React.ReactNode;

  /**
   * Custom cell data render function.
   * Accepts the current record and its index in `records` as arguments and returns a React node
   * (remember that a string is a valid React node too).
   */
  render?: (record: T, index: number) => React.ReactNode;

  /**
   * Column text alignment.
   * @default `left`
   */
  textAlign?: DataTableColumnTextAlign;

  /**
   * If true, column will be sortable.
   */
  sortable?: boolean;
  sortKey?: string;

  /**
   * If set to true, the column can be dragged.
   */
  draggable?: boolean;

  /**
   * If set to true, the column can be toggled.
   */
  toggleable?: boolean;

  /**
   * If set to true, the column can be resized.
   */
  resizable?: boolean;

  /**
   * If set to true, the column will be toggled by default.
   */
  defaultToggle?: boolean;

  /**
   * Optional node providing the user with filtering options.
   * If present, a filter button will be added to the column's header. Upon clicking that button,
   * a pop-over showing the provided node will be opened.
   *
   * Alternatively, a function returning a node can be provided. The function receives props with a `close`
   * method which allows programmatically closing the pop-over.
   *
   * ```tsx
   * // …
   * columns={[
   *   {
   *     accessor: 'name',
   *     filter: ({ close }) => {
   *       return <Stack>
   *         <Button onClick={() => { setFilter(undefined); close(); }}>Reset</Button>
   *       </Stack>
   *     },
   *   }
   * ]}
   * // …
   * ```
   *
   * Note: this property only takes care of rendering the node which provides the filtering options.
   * It is assumed that the actual filtering is performed somewhere in user code.
   */
  filter?: React.ReactNode | ((params: { close: () => void }) => React.ReactNode);

  /**
   * Filter popover props; override if necessary.
   */
  filterPopoverProps?: PopoverProps;

  /**
   * Disables the use of the Mantine useClickOutside hook inside the filter popover
   */
  filterPopoverDisableClickOutside?: boolean;

  /**
   * If true, filter icon will be styled differently to indicate the filter is in effect.
   */
  filtering?: boolean;

  /**
   * Desired column width.
   */
  width?: string | number;

  /**
   * If true, column will not be visible.
   */
  hidden?: boolean;

  /**
   * If true, tbody cells will not be visible.
   */
  hiddenContent?: boolean;

  /**
   * If set, the column will only be visible according to the specified media query.
   * Can be a string, or a function receiving the current theme and returning a string.
   */
  visibleMediaQuery?: string | ((theme: MantineTheme) => string);

  /**
   * Optional class name passed to the column title
   */
  titleClassName?: string;

  /**
   * Optional style passed to the column title.
   * Either a style object, or a function receiving the current theme and returning a style object.
   */
  titleStyle?: MantineStyleProp;

  /**
   * Optional class name passed to each data cell in the column.
   * Can be a string, or a function receiving the current record and its index
   * as arguments and returning a string.
   */
  cellsClassName?: string | ((record: T, index: number) => string | undefined);

  /**
   * Optional style passed to each data cell in the column.
   * A function that receives the current record and its index as arguments and returns either
   * a style object, or a function that accepts theme and returns a style object.
   */
  cellsStyle?: (record: T, index: number) => MantineStyleProp | undefined;

  /**
   * Optional function returning an object of custom attributes to be applied to each cell in the column.
   * Receives the current record and its index as arguments.
   * Useful for adding data attributes, handling middle-clicks, etc.
   */
  customCellAttributes?: (record: T, index: number) => Record<string, unknown>;

  /**
   * Optional column footer content.
   * If at least one column has a footer, the table will display a footer row.
   */
  footer?: React.ReactNode;

  /**
   * Optional class name passed to the column footer.
   */
  footerClassName?: string;

  /**
   * Optional style passed to the column footer.
   */
  footerStyle?: MantineStyleProp;
} & (
  | {
      /**
       * If true, cell content in this column will be truncated with ellipsis as needed and will not wrap
       * to multiple lines (i.e. `overflow: hidden; text-overflow: ellipsis`; `white-space: nowrap`).
       * On a column, you can either set this property or `noWrap`, but not both.
       */
      ellipsis?: boolean;

      noWrap?: never;
    }
  | {
      ellipsis?: never;

      /**
       * If true, cell content in this column will not wrap to multiple lines (i.e. `white-space: nowrap`).
       * This is useful for columns containing long strings.
       * On a column, you can either set this property or `ellipsis`, but not both.
       */
      noWrap?: boolean;
    }
);
```

Expand code

DataTableColumnGroup.ts

```
import type { MantineStyleProp } from '@mantine/core';
import type { DataTableColumn } from './DataTableColumn';
import type { DataTableColumnTextAlign } from './DataTableColumnTextAlign';

export type DataTableColumnGroup<T = Record<string, unknown>> = {
  /**
   * Used as the `key` prop for the created `<th />`.
   */
  id: string;

  /**
   * Component to render inside the column group header.
   */
  title?: React.ReactNode;

  /**
   * Text alignment of the column group header.
   * @default `left`
   */
  textAlign?: DataTableColumnTextAlign;

  /**
   * Columns which are part of the group.
   * Optional when groups are provided for multilevel grouping.
   */
  columns?: DataTableColumn<T>[];

  /**
   * Nested column groups for multilevel grouping.
   * When provided, columns should be omitted.
   */
  groups?: DataTableColumnGroup<T>[];

  /**
   * Optional className to apply to the column group header.
   */
  className?: string;

  /**
   * Optional style to apply to the column group header.
   * Can be a style object or a function which receives the current theme and
   * returns a style object.
   */
  style?: MantineStyleProp;
};
```

Expand code

DataTableColumnProps.ts

```
import type { DataTableColumn } from './DataTableColumn';
import type { DataTableColumnGroup } from './DataTableColumnGroup';

export type DataTableColumnProps<T = Record<string, unknown>> =
  | {
      /**
       * Grouped columns.
       */
      groups: DataTableColumnGroup<T>[];

      columns?: never;
    }
  | {
      groups?: never;

      /**
       * Visible columns.
       */
      columns: DataTableColumn<T>[];
    };
```

Expand code

DataTableColumnTextAlign.ts

`export type DataTableColumnTextAlign = 'left' | 'center' | 'right';`

Expand code

DataTableDefaultColumnProps.ts

```
import type { DataTableColumn } from './DataTableColumn';

export type DataTableDefaultColumnProps<T = Record<string, unknown>> = Omit<
  DataTableColumn<T>,
  'accessor' | 'hidden' | 'visibleMediaQuery' | 'render'
>;
```

Expand code

DataTableDraggableRowProps.ts

```
import type { TableTrProps } from '@mantine/core';

export type DataTableDraggableRowProps = {
  /**
   * Optional class name.
   */
  className?: string;

  /**
   * Current dragging status.
   */
  isDragging?: boolean;
} & TableTrProps;
```

Expand code

DataTableEmptyStateProps.ts

```
export type DataTableEmptyStateProps =
  | {
      /**
       * Content to show when no records are available.
       * The provided content will be overlaid and centered automatically.
       * You can either provide this property or `noRecordsIcon`, but not both.
       */
      emptyState?: React.ReactNode;

      noRecordsIcon?: never;
    }
  | {
      emptyState?: never;

      /**
       * Icon to show when no records are available.
       * The provided icon will be overlaid and centered automatically.
       * You can either provide this property or `emptyState`, but not both.
       */
      noRecordsIcon?: React.ReactNode;
    };
```

Expand code

DataTableLoaderProps.ts

```
import type { MantineColor, MantineLoader, MantineSize } from '@mantine/core';

export type DataTableLoaderProps = {
  /**
   * Loader background blur (in pixels).
   */
  loaderBackgroundBlur?: number;
} & (
  | {
      loaderSize?: never;
      loaderType?: never;
      loaderColor?: never;

      /**
       * Custom loader component to use instead of default one.
       */
      customLoader?: React.ReactNode;
    }
  | {
      /**
       * Loader size.
       * @default `lg`.
       */
      loaderSize?: MantineSize | (string & NonNullable<unknown>) | number;

      /**
       * Loader type.
       */
      loaderType?: MantineLoader;

      /**
       * Loader color.
       */
      loaderColor?: MantineColor;

      customLoader?: never;
    }
);
```

Expand code

DataTableOuterBorderProps.ts

```
import type { MantineSize } from '@mantine/core';

export type DataTableOuterBorderProps =
  | {
      withTableBorder?: never;
      borderRadius?: never;
    }
  | {
      /**
       * If true, table will have border.
       */
      withTableBorder: boolean;

      /**
       * Table border radius.
       */
      borderRadius?: MantineSize | (string & NonNullable<unknown>) | number;
    };
```

Expand code

DataTablePageSizeSelectorProps.ts

```
export type DataTablePageSizeSelectorProps =
  | {
      onRecordsPerPageChange?: never;
      recordsPerPageOptions?: never;
      recordsPerPageLabel?: never;
    }
  | {
      /**
       * Callback fired a new page size is selected.
       * Receives new page size as argument.
       */
      onRecordsPerPageChange: (recordsPerPage: number) => void;

      /**
       * Array of page sizes (numbers) to show in records per page selector.
       */
      recordsPerPageOptions: number[];

      /**
       * Label for records per page selector.
       */
      recordsPerPageLabel?: string;
    };
```

Expand code

DataTablePaginationProps.ts

```
import type { MantineColor, MantineSize } from '@mantine/core';
import type { DataTablePageSizeSelectorProps } from './DataTablePageSizeSelectorProps';
import type { PaginationRenderContext } from './PaginationRenderContext';

export type DataTablePaginationProps = (
  | {
      paginationWithEdges?: never;
      paginationWithControls?: never;
      page?: never;
      onPageChange?: never;
      totalRecords?: never;
      recordsPerPage?: never;
      paginationActiveTextColor?: never;
      paginationActiveBackgroundColor?: never;
      paginationSize?: never;
      loadingText?: never;
      paginationText?: never;
      paginationWrapBreakpoint?: never;
      getPaginationControlProps?: never;
      getPaginationItemProps?: never;
      renderPagination?: never;
    }
  | {
      /**
       * Whether to show first and last page navigation buttons.
       */
      paginationWithEdges?: boolean;

      /**
       * Whether to show next and previous page navigation buttons.
       */
      paginationWithControls?: boolean;

      /**
       * Current page number (1-based).
       * If provided, a pagination component is shown.
       */
      page: number;

      /**
       * Callback fired after page change.
       * Receives the new page number as argument.
       */
      onPageChange: (page: number) => void;

      /**
       * Total number of records in the dataset.
       */
      totalRecords: number | undefined;

      /**
       * Number of records per page.
       */
      recordsPerPage: number;

      /**
       * Pagination component size.
       * @default `sm`
       */
      paginationSize?: MantineSize;

      /**
       * Color applied to active page button text.
       * Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string),
       * or an object with `light` and `dark` keys and `MantineColor` values.
       * Defaults to white.
       */
      paginationActiveTextColor?: MantineColor | { light: MantineColor; dark: MantineColor };

      /**
       * Color applied to active page button background.
       * Can be a `MantineColor` (key of `theme.colors` or any valid CSS color string),
       * or an object with `light` and `dark` keys and `MantineColor` values.
       * Defaults to primary theme color.
       */
      paginationActiveBackgroundColor?: MantineColor | { light: MantineColor; dark: MantineColor };

      /**
       * Text to show while records are loading.
       */
      loadingText?: string;

      /**
       * Pagination text. Defaults to ```({ from, to, totalRecords }) => `${from}-${to}/${totalRecords}`
       * ```
       */
      paginationText?: (params: { from: number; to: number; totalRecords: number }) => React.ReactNode;

      /**
       * Pagination wrap breakpoints.
       * Below this breakpoint the content will be displayed on multiple lines,
       * above it the content will be displayed on a single line.
       * @default `sm`
       */
      paginationWrapBreakpoint?: MantineSize | (string & NonNullable<unknown>) | number;

      /**
       * Function that returns props object for pagination control.
       * Useful for improving accessibility.
       */
      getPaginationControlProps?: (control: 'first' | 'last' | 'previous' | 'next') => Record<string, unknown>;

      /**
       * Function that returns props object for pagination item (page number button).
       */
      getPaginationItemProps?: (page: number) => Record<string, unknown>;

      /**
       * Optional render function to replace the entire pagination component.
       */
      renderPagination?: (ctx: PaginationRenderContext) => React.ReactNode;
    }
) &
  DataTablePageSizeSelectorProps;
```

Expand code

DataTableProps.ts

```
import type {
  MantineShadow,
  MantineStyleProp,
  ScrollAreaProps,
  StylesRecord,
  TableProps,
  TableTrProps,
} from '@mantine/core';
import type { DataTableCellClickHandler } from './DataTableCellClickHandler';
import type { DataTableColorProps } from './DataTableColorProps';
import type { DataTableColumnProps } from './DataTableColumnProps';
import type { DataTableDefaultColumnProps } from './DataTableDefaultColumnProps';
import type { DataTableEmptyStateProps } from './DataTableEmptyStateProps';
import type { DataTableLoaderProps } from './DataTableLoaderProps';
import type { DataTableOuterBorderProps } from './DataTableOuterBorderProps';
import type { DataTablePaginationProps } from './DataTablePaginationProps';
import type { DataTableRowClickHandler } from './DataTableRowClickHandler';
import type { DataTableRowExpansionProps } from './DataTableRowExpansionProps';
import type { DataTableScrollProps } from './DataTableScrollProps';
import type { DataTableSelectionProps } from './DataTableSelectionProps';
import type { DataTableSortProps } from './DataTableSortProps';
import type { DataTableVerticalAlign } from './DataTableVerticalAlign';

export type DataTableProps<T = Record<string, unknown>> = {
  /**
   * Data table container class name.
   */
  className?: string;

  /**
   * Data table container style.
   * Either a style object or a function that accepts current theme and returns a style object.
   */
  style?: MantineStyleProp;

  /**
   * Data table elements class names.
   * An object with `root`, `table`, `header`, `footer` and `pagination` keys and class names
   * as values.
   */
  classNames?: Partial<Record<'root' | 'table' | 'header' | 'footer' | 'pagination', string>>;

  /**
   * Data table elements styles.
   * An object with `root`, `table`, `header`, `footer` and `pagination` keys and
   * either style objects, or functions that accept current theme and return style objects, as values.
   */
  styles?: StylesRecord<'root' | 'table' | 'header' | 'footer' | 'pagination', MantineStyleProp>;

  /**
   * Table height.
   * @default '100%'
   */
  height?: string | number;

  /**
   * Minimum table height.
   */
  minHeight?: string | number;

  /**
   * Maximum table height.
   */
  maxHeight?: string | number;

  /**
   * DataTable component shadow.
   */
  shadow?: MantineShadow;

  /**
   * If true, the user will not be able to select text.
   */
  textSelectionDisabled?: boolean;

  /**
   * Vertical alignment for row cells.
   * @default `center`
   */
  verticalAlign?: DataTableVerticalAlign;

  /**
   * If true, will show a loader with semi-transparent background, centered over the table.
   */
  fetching?: boolean;

  /**
   * If true, the first column will be pinned to the left side of the table.
   */
  pinFirstColumn?: boolean;

  /**
   * If true, the last column will be pinned to the right side of the table.
   */
  pinLastColumn?: boolean;

  /**
   * Default column props; will be merged with column props provided to each column
   */
  defaultColumnProps?: DataTableDefaultColumnProps<T>;

  /**
   * If you want to use drag and drop as well as toggle to reorder and toggle columns
   * provide a unique key which will be used to store the column order in localStorage.
   */
  storeColumnsKey?: string | undefined;

  /**
   * A default render function for all columns.
   * Accepts the current record, its index in `records` and the column `accessor` as
   * arguments and returns a React node (remember that a string is a valid React node too).
   */
  defaultColumnRender?: (
    record: T,
    index: number,
    accessor: keyof T | (string & NonNullable<unknown>)
  ) => React.ReactNode;

  /**
   * Accessor to use as unique record key.
   * Can be a string representing a property name or a function receiving the current record
   * and returning a unique value.
   * If you're providing a string, you can use dot-notation for nested objects property drilling
   * (i.e. `department.name` or `department.company.name`).
   * @default `id`
   */
  idAccessor?: (keyof T | (string & NonNullable<unknown>)) | ((record: T) => React.Key);

  /**
   * Visible records.
   * The component will try to infer its row type from here.
   */
  records?: T[];

  /**
   * Text to show on empty state and pagination footer when no records are available.
   */
  noRecordsText?: string;

  /**
   * If true, the table will not show the header with column titles.
   */
  noHeader?: boolean;

  /**
   * Function to call when a row cell is clicked.
   * Receives an object with the current record, its index in `records`, the current column,
   * its index in `columns` and the click event as properties.
   */
  onCellClick?: DataTableCellClickHandler<T>;

  /**
   * Function to call when a row cell is double-clicked.
   * Receives an object with the current record, its index in `records`, the current column,
   * its index in `columns` and the click event as properties.
   */
  onCellDoubleClick?: DataTableCellClickHandler<T>;

  /**
   * Function to call when the user right-clicks on a row cell.
   * Receives an object with the current record, its index in `records`, the current column,
   * its index in `columns` and the click event as properties.
   */
  onCellContextMenu?: DataTableCellClickHandler<T>;

  /**
   * Function to call when a row is clicked.
   * Receives an object with the current record, its index in `records` and the click event
   * as properties.
   */
  onRowClick?: DataTableRowClickHandler<T>;

  /**
   * Function to call when a row is double-clicked.
   * Receives an object with the current record, its index in `records` and the click event
   * as properties.
   */
  onRowDoubleClick?: DataTableRowClickHandler<T>;

  /**
   * Function to call when the user right-clicks on a row.
   * Receives an object with the current record, its index in `records` and the click event
   * as properties.
   */
  onRowContextMenu?: DataTableRowClickHandler<T>;

  /**
   * Defines the row expansion behavior.
   */
  rowExpansion?: DataTableRowExpansionProps<T>;

  /**
   * Optional class name passed to each row.
   * Can be a string or a function receiving the current record and its index as arguments and returning a string.
   */
  rowClassName?: string | ((record: T, index: number) => string | undefined);

  /**
   * Optional style passed to each row.
   * A function receiving the current record and its index as arguments and returning either
   * a style object, or a function that accepts theme and returns a style object.
   */
  rowStyle?: (record: T, index: number) => MantineStyleProp | undefined;

  /**
   * Optional style passed to each row.
   * a function that receives the current record, its index, default row props and expanded element as arguments
   * and returns a React node representing the row.
   */
  rowFactory?: (props: {
    record: T;
    index: number;
    children: React.ReactNode;
    rowProps: TableTrProps;
    expandedElement?: React.ReactNode;
  }) => React.ReactNode;

  /**
   * Optional function returning a React node representing the table wrapper.
   * If not provided, no wrapper will be used.
   *
   * examplle: This function can be used with rowFactory if using drag and drop to pass context
   */
  tableWrapper?: ({ children }: { children: React.ReactNode }) => React.ReactNode;

  /**
   * Optional function returning an object of custom attributes to be applied to each row in the table.
   * Receives the current record and its index as arguments.
   * Useful for adding data attributes, handling middle-clicks, etc.
   */
  customRowAttributes?: (record: T, index: number) => Record<string, unknown>;

  /**
   * Ref pointing to the scrollable viewport element.
   * Useful for imperative scrolling.
   */
  scrollViewportRef?: React.RefObject<HTMLDivElement | null>;

  /**
   * Additional props passed to the underlying `ScrollArea` element.
   */
  scrollAreaProps?: Omit<ScrollAreaProps, 'classNames' | 'styles' | 'onScrollPositionChange'>;

  /**
   * Ref pointing to the table element.
   */
  tableRef?: ((instance: HTMLTableElement | null) => void) | React.RefObject<HTMLTableElement>;

  /**
   * Ref pointing to the table body element.
   */
  bodyRef?: ((instance: HTMLTableSectionElement | null) => void) | React.RefObject<HTMLTableSectionElement>;
} & Omit<
  TableProps,
  | 'onScroll'
  | 'className'
  | 'classNames'
  | 'style'
  | 'styles'
  | 'p'
  | 'px'
  | 'py'
  | 'pt'
  | 'pb'
  | 'layout'
  | 'captionSide'
  | 'c'
  | 'color'
  | 'borderColor'
  | 'stripedColor'
  | 'highlightOnHoverColor'
  | 'stickyHeader'
  | 'stickyHeaderOffset'
  | 'onDragEnd'
> &
  DataTableColorProps<T> &
  DataTableColumnProps<T> &
  DataTableOuterBorderProps &
  DataTableLoaderProps &
  DataTableEmptyStateProps &
  DataTablePaginationProps &
  DataTableSortProps<T> &
  DataTableScrollProps &
  DataTableSelectionProps<T>;
```

Expand code

DataTableRowClickHandler.ts

```
export type DataTableRowClickHandler<T = Record<string, unknown>> = (params: {
  /**
   * Click event.
   */
  event: React.MouseEvent;

  /**
   * Clicked record.
   */
  record: T;

  /**
   * Clicked record index.
   */
  index: number;
}) => void;
```

Expand code

DataTableRowExpansionCollapseProps.ts

```
import type { CollapseProps } from '@mantine/core';

export type DataTableRowExpansionCollapseProps = Pick<
  CollapseProps,
  'animateOpacity' | 'transitionDuration' | 'transitionTimingFunction'
>;
```

Expand code

DataTableRowExpansionProps.ts

```
import type { DataTableRowExpansionCollapseProps } from './DataTableRowExpansionCollapseProps';

export type DataTableRowExpansionProps<T = Record<string, unknown>> = {
  /**
   * Function defining which records can be expanded.
   * Accepts an object with `record` and `index` properties and returns a boolean specifying
   * whether the row should be expandable.
   */
  expandable?: (params: { record: T; index: number }) => boolean;

  /**
   * Defines when rows should expand.
   * @default `click`
   */
  trigger?: 'click' | 'always' | 'never';

  /**
   * If true, multiple rows can be expanded at the same time.
   */
  allowMultiple?: boolean;

  /**
   * Function defining which records will be initially expanded.
   * Accepts an object with `record` and `index` properties and returns a boolean specifying
   * whether the row should be expanded initially.
   * Does nothing if `trigger === 'always'`.
   */
  initiallyExpanded?: (options: { record: T; index: number }) => boolean;

  /**
   * Additional properties passed to the Mantine Collapse component wrapping the custom content.
   */
  collapseProps?: DataTableRowExpansionCollapseProps;

  /**
   * An object defining the row expansion behavior in controlled mode.
   */
  expanded?: {
    /**
     * Currently expanded record IDs.
     */
    recordIds: unknown[];

    /**
     * Callback fired when expanded records change.
     * Receives an array containing the newly expanded record IDs.
     */
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    onRecordIdsChange?: React.Dispatch<React.SetStateAction<any[]>> | ((recordIds: unknown[]) => void);
  };

  /**
   * Function returning the custom content to be lazily rendered for an expanded row.
   * Accepts an object with properties containing the current record, its index,
   * and a `collapse()` callback that can be used to collapse the expanded row.
   * Must return a React node.
   */
  content: (params: { record: T; index: number; collapse: () => void }) => React.ReactNode;
};
```

Expand code

DataTableScrollProps.ts

```
export type DataTableScrollProps = {
  /**
   * Function to call when the DataTable is scrolled.
   */
  onScroll?: (position: { x: number; y: number }) => void;

  /**
   * Function to call when the DataTable is scrolled to top.
   */
  onScrollToTop?: () => void;

  /**
   * Function to call when the DataTable is scrolled to bottom.
   */
  onScrollToBottom?: () => void;

  /**
   * Function to call when the DataTable is scrolled to left.
   */
  onScrollToLeft?: () => void;

  /**
   * Function to call when the DataTable is scrolled to right.
   */
  onScrollToRight?: () => void;
};
```

Expand code

DataTableSelectionProps.ts

```
import type { CheckboxProps, MantineStyleProp } from '@mantine/core';
import type { DataTableSelectionTrigger } from './DataTableSelectionTrigger';

export type DataTableSelectionProps<T = Record<string, unknown>> =
  | {
      selectionTrigger?: never;
      selectedRecords?: never;
      onSelectedRecordsChange?: never;
      isRecordSelectable?: never;
      selectionCheckboxProps?: never;
      getRecordSelectionCheckboxProps?: never;
      allRecordsSelectionCheckboxProps?: never;
      selectionColumnClassName?: never;
      selectionColumnStyle?: never;
    }
  | {
      /**
       * Defines how selection is triggered.
       * @default 'checkbox'
       */
      selectionTrigger?: DataTableSelectionTrigger;

      /**
       * Currently-selected records.
       */
      selectedRecords?: T[];

      /**
       * Callback fired when selected records change.
       * Receives and array of selected records as argument.
       */
      onSelectedRecordsChange?: (selectedRecords: T[]) => void;

      /**
       * Optional class name applied to selection column.
       */
      selectionColumnClassName?: string;

      /**
       * Optional style applied to selection column.
       */
      selectionColumnStyle?: MantineStyleProp;

      /**
       * A function used to determine whether a certain record is selectable.
       * if the function returns false, the row selection checkbox is disabled.
       * Accepts the current recors and index as arguments and returns a boolean.
       */
      isRecordSelectable?: (record: T, index: number) => boolean;

      /**
       * Props for the selection checkboxes, applied to header and all rows.
       */
      selectionCheckboxProps?: CheckboxProps;

      /**
       * A function used to determine additional props of the row selection checkboxes.
       * Accepts the current record and its index as arguments and returns an object.
       */
      getRecordSelectionCheckboxProps?: (record: T, index: number) => CheckboxProps;

      /**
       * Additional props for the header checkbox that toggles selection of all records.
       */
      allRecordsSelectionCheckboxProps?: CheckboxProps;
    };
```

Expand code

DataTableSelectionTrigger.ts

`export type DataTableSelectionTrigger = 'cell' | 'checkbox';`

Expand code

DataTableSortProps.ts

```
import type { DataTableSortStatus } from './DataTableSortStatus';

export type DataTableSortProps<T = Record<string, unknown>> = (
  | {
      sortStatus?: never;
      onSortStatusChange?: never;
    }
  | {
      /**
       * Current sort status (sort column accessor & direction).
       */
      sortStatus: DataTableSortStatus<T>;

      /**
       * Callback fired after change of sort status.
       * Receives the new sort status as argument.
       */
      onSortStatusChange?: (sortStatus: DataTableSortStatus<T>) => void;
    }
) & {
  /**
   * Custom sort icons.
   */
  sortIcons?: {
    /**
     * Icon to display when column is sorted ascending.
     * Will be rotated 180deg for descending sort
     */
    sorted: React.ReactNode;
    /**
     * Icon to display when column is not sorted.
     */
    unsorted: React.ReactNode;
  };
};
```

Expand code

DataTableSortStatus.ts

```
export type DataTableSortStatus<T = Record<string, unknown>> = {
  /**
   * Sort column key for nested values.
   * @type {string}
   */
  sortKey?: string;
  /**
   * Sort column accessor.
   * You can use dot-notation for nested objects property drilling
   * (i.e. `department.name` or `department.company.name`).
   */
  columnAccessor: keyof T | (string & NonNullable<unknown>);

  /**
   * Sort direction - `asc` for ascending, `desc` for descending.
   */
  direction: 'asc' | 'desc';
};
```

Expand code

DataTableVerticalAlign.ts

`export type DataTableVerticalAlign = 'top' | 'center' | 'bottom';`

Expand code

PaginationRenderContext.tsx

```
import type { MantineSize, PaginationProps, TextProps } from '@mantine/core';
import type { JSX } from 'react';
import type { DataTablePageSizeSelectorProps } from './DataTablePageSizeSelectorProps';

export type PaginationRenderContext = {
  state: {
    paginationSize: MantineSize;
    page: number;
    totalPages: number;
    totalRecords: number | undefined;
    recordsPerPage: number | undefined;
    recordsLength: number | undefined;
    fetching: boolean | undefined;
    from?: number;
    to?: number;
    isWrapped: boolean;
  };
  actions: {
    setPage: (page: number) => void;
    setRecordsPerPage?: (n: number) => void;
  };
  Controls: {
    Text: (props?: Partial<TextProps>) => JSX.Element;
    PageSizeSelector: (props?: Partial<DataTablePageSizeSelectorProps>) => JSX.Element;
    Pagination: (props?: Partial<PaginationProps>) => JSX.Element;
  };
};
```

Expand code

utils.ts

```
export type WithOptionalProperty<T, K extends keyof T> = Pick<Partial<T>, K> & Omit<T, K>;

export type WithRequiredProperty<Type, Key extends keyof Type> = Type & {
  [Property in Key]-?: Type[Property];
};
```

Expand code

[Go back Examples › Complex usage scenario](https://icflorescu.github.io/mantine-datatable/examples/complex-usage-scenario/)[Up next Mantine V6 support](https://icflorescu.github.io/mantine-datatable/mantine-v6-support/)

Mantine DataTable is used and trusted by
----------------------------------------

[![Image 1: Microsoft is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/microsoft.svg)](https://www.microsoft.com/ "Microsoft is using Mantine DataTable")[![Image 2: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-light.svg)![Image 3: Namecheap is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/namecheap-dark.svg)](https://www.namecheap.com/ "Namecheap is using Mantine DataTable")[![Image 4: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-light.svg)![Image 5: EasyWP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/easywp-dark.svg)](https://www.easywp.com/ "EasyWP is using Mantine DataTable")[![Image 6: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-light.png)![Image 7: LeasingSH.ro is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/leasingsh-ro-dark.png)](https://leasingsh.ro/ "LeasingSH.ro is using Mantine DataTable")[![Image 8: CodeParrot.AI is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/codeparrot.svg) CodeParrot.AI](https://codeparrot.ai/ "CodeParrot.AI is using Mantine DataTable")[![Image 9: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-light.svg)![Image 10: OmicsStudio is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/omicsstudio-dark.svg)](https://omicsstudio.com/ "OmicsStudio is using Mantine DataTable")[![Image 11: SegmentX is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/segmentx.png) SegmentX](https://segmentx.ai/ "SegmentX is using Mantine DataTable")[![Image 12: Aquarino is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/aquarino.svg)](http://aquarino.com.br/ "Aquarino is using Mantine DataTable")[![Image 13: Dera is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/dera.webp) Dera](https://getdera.com/ "Dera is using Mantine DataTable")[![Image 14: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-light.png)![Image 15: kappa.ai is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/kapa-dark.png)](https://kapa.ai/ "kappa.ai is using Mantine DataTable")[![Image 16: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-light.svg)![Image 17: exdatis is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/exdatis-dark.svg)](https://exdatis.ai/ "exdatis is using Mantine DataTable")[![Image 18: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-light.svg)![Image 19: teachfloor is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/teachfloor-dark.svg)](https://www.teachfloor.com/ "teachfloor is using Mantine DataTable")[![Image 20: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-light.png)![Image 21: MARKUP is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/markup-dark.png)](https://www.getmarkup.com/ "MARKUP is using Mantine DataTable")[![Image 22: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-light.png)![Image 23: InvenTree is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/inventree-dark.png)](https://inventree.org/ "InvenTree is using Mantine DataTable")[![Image 24: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-light.svg)![Image 25: BookieBase is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/bookiebase-dark.svg)](https://bookiebase.ie/ "BookieBase is using Mantine DataTable")[![Image 26: Zipline is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/zipline.png)](https://zipline.diced.sh/ "Zipline is using Mantine DataTable")[![Image 27: Pachtop is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pachtop.png) Pachtop](https://pachtop.com/ "Pachtop is using Mantine DataTable")[![Image 28: Ganymede is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ganymede.png) Ganymede](https://github.com/Zibbp/ganymede "Ganymede is using Mantine DataTable")[![Image 29: Pipedash is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/pipedash.png) Pipedash](https://github.com/hcavarsan/pipedash "Pipedash is using Mantine DataTable")[![Image 30: COH3 Stats is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/coh3-stats.png) COH3 Stats](https://coh3stats.com/ "COH3 Stats is using Mantine DataTable")[![Image 31: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-light.svg)![Image 32: ccrentals.org is using Mantine DataTable](https://icflorescu.github.io/mantine-datatable/users/ccrentals-dark.svg) ccrentals.org](https://www.ccrentals.org/ "ccrentals.org is using Mantine DataTable")

[![Image 33: MIT License](https://img.shields.io/npm/l/mantine-datatable.svg?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable/blob/main/LICENSE)[![Image 34: Sponsor the author](https://img.shields.io/static/v1?label=github&message=sponsor&color=1c7ed6)](https://github.com/sponsors/icflorescu)

Built by [Ionut-Cristian Florescu](https://github.com/icflorescu) and[these awesome people](https://github.com/icflorescu/mantine-datatable/graphs/contributors).

Please [sponsor my work](https://github.com/sponsors/icflorescu) if you find it useful.

[![Image 35: GitHub Stars](https://img.shields.io/github/stars/icflorescu/mantine-datatable?style=flat&color=1c7ed6)](https://github.com/icflorescu/mantine-datatable)[![Image 36: NPM Downloads](https://img.shields.io/npm/dm/mantine-datatable.svg?style=flat&color=1c7ed6)](https://www.npmjs.com/package/mantine-datatable)
