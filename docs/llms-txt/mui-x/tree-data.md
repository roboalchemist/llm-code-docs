# Source: https://mui.com/x/react-data-grid/server-side-data/tree-data.md

# Source: https://mui.com/x/react-data-grid/tree-data.md

# Source: https://mui.com/x/react-data-grid/server-side-data/tree-data.md

# Source: https://mui.com/x/react-data-grid/tree-data.md

---
title: Data Grid - Tree data
---

# Data Grid - Tree data [<span class="plan-pro"></span>](/x/introduction/licensing/#pro-plan 'Pro plan')

Use tree data to render rows with parent-child relationships in the Data Grid.

Trees are hierarchical data structures that organize data into parent-child relationships.
The Data Grid Pro can use tree data to render rows that conform to this pattern.
The demo below illustrates this feature with a large and complex hierarchical dataset:

```tsx
import { DataGridPro, useGridApiRef } from '@mui/x-data-grid-pro';
import { useDemoData } from '@mui/x-data-grid-generator';
import Button from '@mui/material/Button';

export default function TreeDataFullExample() {
  const apiRef = useGridApiRef();
  const { data, loading } = useDemoData({
    dataSet: 'Employee',
    rowLength: 1000,
    treeData: { maxDepth: 2, groupingField: 'name', averageChildren: 200 },
  });

  return (
    <div style={{ width: '100%' }}>
      <Button onClick={() => apiRef.current?.expandAllRows()}>Expand all</Button>
      <Button onClick={() => apiRef.current?.collapseAllRows()}>Collapse all</Button>
      <div style={{ height: 400 }}>
        <DataGridPro loading={loading} {...data} apiRef={apiRef} />
      </div>
    </div>
  );
}

```

:::info
This document covers client-side data.
For tree data on the server side, see [Server-side data—Tree data](/x/react-data-grid/server-side-data/tree-data/).
:::

## Rendering tree data

To work with tree data, pass the `treeData` and `getTreeDataPath` props to the `<DataGridPro />` component.
The `getTreeDataPath` function returns an array of strings representing the path to a given row.

```tsx
<DataGridPro treeData getTreeDataPath={getTreeDataPath} />
```

Both examples that follow will render a tree that looks like this:

```tsx
// - Sarah
//     - Thomas
//         - Robert
//         - Karen
```

**1. Without transformation:**

```tsx
const columns: GridColDef[] = [{ field: 'jobTitle', width: 250 }];

const rows: GridRowsProp = [
  { path: ['Sarah'], jobTitle: 'CEO', id: 0 },
  { path: ['Sarah', 'Thomas'], jobTitle: 'Head of Sales', id: 1 },
  { path: ['Sarah', 'Thomas', 'Robert'], jobTitle: 'Sales Person', id: 2 },
  { path: ['Sarah', 'Thomas', 'Karen'], jobTitle: 'Sales Person', id: 3 },
];

const getTreeDataPath: DataGridProProps['getTreeDataPath'] = (row) => row.path;

<DataGridPro
  treeData
  getTreeDataPath={getTreeDataPath}
  rows={rows}
  columns={columns}
/>;
```

**2. With transformation:**

```tsx
const columns: GridColDef[] = [{ field: 'jobTitle', width: 250 }];

const rows: GridRowsProp = [
  { path: 'Sarah', jobTitle: 'CEO', id: 0 },
  { path: 'Sarah/Thomas', jobTitle: 'Head of Sales', id: 1 },
  { path: 'Sarah/Thomas/Robert', jobTitle: 'Sales Person', id: 2 },
  { path: 'Sarah/Thomas/Karen', jobTitle: 'Sales Person', id: 3 },
];

const getTreeDataPath: DataGridProProps['getTreeDataPath'] = (row) =>
  row.path.split('/');

<DataGridPro
  treeData
  getTreeDataPath={getTreeDataPath}
  rows={rows}
  columns={columns}
/>;
```

:::warning
The `getTreeDataPath` prop should keep the same reference between two renders.
If it changes, the Data Grid assumes that the data itself has changed and recomputes the tree, causing all rows to collapse.
:::

## Customizing grouping columns with tree data

For complete details on customizing grouping columns, see [Row grouping—Grouping columns](/x/react-data-grid/row-grouping/#grouping-columns).
The implementation and behavior are the same when working with tree data, but note that the `leafField` and `mainGroupingCriteria` props are not applicable.

The demo below customizes the **Hierarchy** grouping column:

```tsx
import {
  DataGridPro,
  GridRenderCellParams,
  useGridApiContext,
  GridColDef,
  GridRowsProp,
  DataGridProProps,
  useGridSelector,
  gridFilteredDescendantCountLookupSelector,
} from '@mui/x-data-grid-pro';
import Box from '@mui/material/Box';
import Button, { ButtonProps } from '@mui/material/Button';

export const isNavigationKey = (key: string) =>
  key === 'Home' ||
  key === 'End' ||
  key.indexOf('Arrow') === 0 ||
  key.indexOf('Page') === 0 ||
  key === ' ';

function CustomGridTreeDataGroupingCell(props: GridRenderCellParams) {
  const { id, field, rowNode } = props;
  const apiRef = useGridApiContext();
  const filteredDescendantCountLookup = useGridSelector(
    apiRef,
    gridFilteredDescendantCountLookupSelector,
  );
  const filteredDescendantCount = filteredDescendantCountLookup[rowNode.id] ?? 0;

  const handleClick: ButtonProps['onClick'] = (event) => {
    if (rowNode.type !== 'group') {
      return;
    }

    apiRef.current.setRowChildrenExpansion(id, !rowNode.childrenExpanded);
    apiRef.current.setCellFocus(id, field);
    event.stopPropagation();
  };

  return (
    <Box sx={{ ml: rowNode.depth * 4 }}>
      <div>
        {filteredDescendantCount > 0 ? (
          <Button onClick={handleClick} tabIndex={-1} size="small">
            See {filteredDescendantCount} employees
          </Button>
        ) : (
          <span />
        )}
      </div>
    </Box>
  );
}

interface Row {
  hierarchy: string[];
  jobTitle: string;
  recruitmentDate: Date;
  id: number;
}

const rows: GridRowsProp<Row> = [
  {
    hierarchy: ['Sarah'],
    jobTitle: 'Head of Human Resources',
    recruitmentDate: new Date(2020, 8, 12),
    id: 0,
  },
  {
    hierarchy: ['Thomas'],
    jobTitle: 'Head of Sales',
    recruitmentDate: new Date(2017, 3, 4),
    id: 1,
  },
  {
    hierarchy: ['Thomas', 'Robert'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 11, 20),
    id: 2,
  },
  {
    hierarchy: ['Thomas', 'Karen'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 10, 14),
    id: 3,
  },
  {
    hierarchy: ['Thomas', 'Nancy'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2017, 10, 29),
    id: 4,
  },
  {
    hierarchy: ['Thomas', 'Daniel'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 7, 21),
    id: 5,
  },
  {
    hierarchy: ['Thomas', 'Christopher'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 7, 20),
    id: 6,
  },
  {
    hierarchy: ['Thomas', 'Donald'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2019, 6, 28),
    id: 7,
  },
  {
    hierarchy: ['Mary'],
    jobTitle: 'Head of Engineering',
    recruitmentDate: new Date(2016, 3, 14),
    id: 8,
  },
  {
    hierarchy: ['Mary', 'Jennifer'],
    jobTitle: 'Tech lead front',
    recruitmentDate: new Date(2016, 5, 17),
    id: 9,
  },
  {
    hierarchy: ['Mary', 'Jennifer', 'Anna'],
    jobTitle: 'Front-end developer',
    recruitmentDate: new Date(2019, 11, 7),
    id: 10,
  },
  {
    hierarchy: ['Mary', 'Michael'],
    jobTitle: 'Tech lead devops',
    recruitmentDate: new Date(2021, 7, 1),
    id: 11,
  },
  {
    hierarchy: ['Mary', 'Linda'],
    jobTitle: 'Tech lead back',
    recruitmentDate: new Date(2017, 0, 12),
    id: 12,
  },
  {
    hierarchy: ['Mary', 'Linda', 'Elizabeth'],
    jobTitle: 'Back-end developer',
    recruitmentDate: new Date(2019, 2, 22),
    id: 13,
  },
  {
    hierarchy: ['Mary', 'Linda', 'William'],
    jobTitle: 'Back-end developer',
    recruitmentDate: new Date(2018, 4, 19),
    id: 14,
  },
];

const columns: GridColDef<Row>[] = [
  {
    field: 'name',
    headerName: 'Name',
    valueGetter: (value, row) => {
      const hierarchy = row.hierarchy;
      return hierarchy[hierarchy.length - 1];
    },
  },
  { field: 'jobTitle', headerName: 'Job Title', width: 200 },
  {
    field: 'recruitmentDate',
    headerName: 'Recruitment Date',
    type: 'date',
    width: 150,
  },
];

const getTreeDataPath: DataGridProProps['getTreeDataPath'] = (row) => row.hierarchy;

const groupingColDef: DataGridProProps['groupingColDef'] = {
  headerName: 'Hierarchy',
  renderCell: (params) => <CustomGridTreeDataGroupingCell {...params} />,
};

export default function TreeDataCustomGroupingColumn() {
  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGridPro
        treeData
        rows={rows}
        columns={columns}
        getTreeDataPath={getTreeDataPath}
        groupingColDef={groupingColDef}
      />
    </div>
  );
}

```

### Accessing the grouping column field

To access the grouping column field—for example, to use it with [column pinning](/x/react-data-grid/column-pinning/)—the Grid provides the `GRID_TREE_DATA_GROUPING_FIELD` constant:

```tsx
<DataGridPro
  treeData
  initialState={{
    pinnedColumns: {
      left: [GRID_TREE_DATA_GROUPING_FIELD],
    },
  }}
  {...otherProps}
/>
```

## Group expansion with tree data

For complete details on customizing the group expansion experience, see [Row grouping—Group expansion](/x/react-data-grid/row-grouping/#group-expansion).
The implementation and behavior are the same when working with tree data.

## Automatic parent and child selection with tree data

For complete details on automatic parent and child selection, see [Row grouping—Automatic parent and child selection](/x/react-data-grid/row-grouping/#automatic-parent-and-child-selection).
The implementation and behavior are the same when working with tree data.

## Gaps in the tree

If the tree data provided is missing levels in the hierarchy, the Data Grid Pro will automatically create the rows needed to fill the gaps.
Consider a simple dataset with two rows:

```js
[{ path: ['A'] }, { path: ['A', 'B', 'C'] }];
```

This tree data implies a `{ path: ["A", "B"] }` row that's not present.
To address this, the Grid generates an internal row so it can render without issues.

In the demo below, rows with no gaps are denoted with **✕** in the **Gap** column—you can see that the rows for Thomas, Mary, and Linda have been autogenerated since they're not present in the dataset.

```tsx
import { DataGridPro, GridColDef, DataGridProProps } from '@mui/x-data-grid-pro';

const rows = [
  {
    hierarchy: ['Sarah'],
    jobTitle: 'Head of Human Resources',
    recruitmentDate: new Date(2020, 8, 12),
    id: 0,
  },
  {
    hierarchy: ['Thomas', 'Robert'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 11, 20),
    id: 2,
  },
  {
    hierarchy: ['Thomas', 'Karen'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 10, 14),
    id: 3,
  },
  {
    hierarchy: ['Thomas', 'Nancy'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2017, 10, 29),
    id: 4,
  },
  {
    hierarchy: ['Thomas', 'Daniel'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 7, 21),
    id: 5,
  },
  {
    hierarchy: ['Thomas', 'Christopher'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 7, 20),
    id: 6,
  },
  {
    hierarchy: ['Thomas', 'Donald'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2019, 6, 28),
    id: 7,
  },
  {
    hierarchy: ['Mary', 'Jennifer'],
    jobTitle: 'Tech lead front',
    recruitmentDate: new Date(2016, 5, 17),
    id: 9,
  },
  {
    hierarchy: ['Mary', 'Jennifer', 'Anna'],
    jobTitle: 'Front-end developer',
    recruitmentDate: new Date(2019, 11, 7),
    id: 10,
  },
  {
    hierarchy: ['Mary', 'Michael'],
    jobTitle: 'Tech lead devops',
    recruitmentDate: new Date(2021, 7, 1),
    id: 11,
  },
  {
    hierarchy: ['Mary', 'Linda', 'Elizabeth'],
    jobTitle: 'Back-end developer',
    recruitmentDate: new Date(2019, 2, 22),
    id: 13,
  },
  {
    hierarchy: ['Mary', 'Linda', 'William'],
    jobTitle: 'Back-end developer',
    recruitmentDate: new Date(2018, 4, 19),
    id: 14,
  },
];

const columns: GridColDef<(typeof rows)[number]>[] = [
  { field: 'jobTitle', headerName: 'Job Title', width: 200 },
  {
    field: 'recruitmentDate',
    headerName: 'Recruitment Date',
    type: 'date',
    width: 150,
  },
  {
    field: 'isAutoGenerated',
    headerName: 'Gap',
    type: 'boolean',
    valueGetter: (value, row, column, apiRef) => {
      const rowId = apiRef.current.getRowId(row);
      const rowNode = apiRef.current.getRowNode(rowId);
      if (rowNode?.type !== 'group') {
        return undefined;
      }

      return rowNode.isAutoGenerated;
    },
  },
];

const getTreeDataPath: DataGridProProps['getTreeDataPath'] = (row) => row.hierarchy;

export default function TreeDataWithGap() {
  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGridPro
        treeData
        rows={rows}
        columns={columns}
        getTreeDataPath={getTreeDataPath}
      />
    </div>
  );
}

```

## Filtering tree data

When a filter is applied, a node is included if it _or_ any of its descendents passes.

By default, filtering is applied at every level of the tree.
You can limit it to top-level rows with the `disableChildrenFiltering` prop.

```tsx
import * as React from 'react';
import {
  DataGridPro,
  GridColDef,
  GridFilterModel,
  GridLogicOperator,
  GridRowsProp,
  DataGridProProps,
} from '@mui/x-data-grid-pro';
import Box from '@mui/material/Box';
import Checkbox from '@mui/material/Checkbox';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Typography from '@mui/material/Typography';

const rows: GridRowsProp = [
  {
    hierarchy: ['Sarah'],
    jobTitle: 'Head of Human Resources',
    recruitmentDate: new Date(2020, 8, 12),
    id: 0,
  },
  {
    hierarchy: ['Thomas'],
    jobTitle: 'Head of Sales',
    recruitmentDate: new Date(2017, 3, 4),
    id: 1,
  },
  {
    hierarchy: ['Thomas', 'Robert'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 11, 20),
    id: 2,
  },
  {
    hierarchy: ['Thomas', 'Karen'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 10, 14),
    id: 3,
  },
  {
    hierarchy: ['Thomas', 'Nancy'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2017, 10, 29),
    id: 4,
  },
  {
    hierarchy: ['Thomas', 'Daniel'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 7, 21),
    id: 5,
  },
  {
    hierarchy: ['Thomas', 'Christopher'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 7, 20),
    id: 6,
  },
  {
    hierarchy: ['Thomas', 'Donald'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2019, 6, 28),
    id: 7,
  },
  {
    hierarchy: ['Mary'],
    jobTitle: 'Head of Engineering',
    recruitmentDate: new Date(2016, 3, 14),
    id: 8,
  },
  {
    hierarchy: ['Mary', 'Jennifer'],
    jobTitle: 'Tech lead front',
    recruitmentDate: new Date(2016, 5, 17),
    id: 9,
  },
  {
    hierarchy: ['Mary', 'Jennifer', 'Anna'],
    jobTitle: 'Front-end developer',
    recruitmentDate: new Date(2019, 11, 7),
    id: 10,
  },
  {
    hierarchy: ['Mary', 'Michael'],
    jobTitle: 'Tech lead devops',
    recruitmentDate: new Date(2021, 7, 1),
    id: 11,
  },
  {
    hierarchy: ['Mary', 'Linda'],
    jobTitle: 'Tech lead back',
    recruitmentDate: new Date(2017, 0, 12),
    id: 12,
  },
  {
    hierarchy: ['Mary', 'Linda', 'Elizabeth'],
    jobTitle: 'Back-end developer',
    recruitmentDate: new Date(2019, 2, 22),
    id: 13,
  },
  {
    hierarchy: ['Mary', 'Linda', 'William'],
    jobTitle: 'Back-end developer',
    recruitmentDate: new Date(2018, 4, 19),
    id: 14,
  },
];

const columns: GridColDef[] = [
  { field: 'jobTitle', headerName: 'Job Title', width: 200 },
  {
    field: 'recruitmentDate',
    headerName: 'Recruitment Date',
    type: 'date',
    width: 150,
  },
];

const getTreeDataPath: DataGridProProps['getTreeDataPath'] = (row) => row.hierarchy;

export default function TreeDataDisableChildrenFiltering() {
  const [disableChildrenFiltering, setDisableChildrenFiltering] =
    React.useState(true);
  const [filterModel, setFilterModel] = React.useState<GridFilterModel>({
    logicOperator: GridLogicOperator.Or,
    items: [
      {
        id: 0,
        field: 'recruitmentDate',
        operator: 'before',
        value: '2018-01-01',
      },
    ],
  });

  return (
    <Box sx={{ width: '100%' }}>
      <FormGroup>
        <FormControlLabel
          control={
            <Checkbox
              checked={disableChildrenFiltering}
              onChange={(event) => setDisableChildrenFiltering(event.target.checked)}
            />
          }
          label={
            <Typography component="span">
              Apply <code>disableChildrenFiltering</code>
            </Typography>
          }
        />
      </FormGroup>
      <Box sx={{ height: 400, pt: 1 }}>
        <DataGridPro
          treeData
          rows={rows}
          columns={columns}
          disableChildrenFiltering={disableChildrenFiltering}
          getTreeDataPath={getTreeDataPath}
          filterModel={filterModel}
          onFilterModelChange={setFilterModel}
          defaultGroupingExpansionDepth={1}
        />
      </Box>
    </Box>
  );
}

```

## Sorting tree data

By default, sorting is applied at every level of the tree.
You can limit it to top-level rows with the `disableChildrenSorting` prop.

```tsx
import * as React from 'react';
import {
  DataGridPro,
  GridColDef,
  GridRowsProp,
  GridSortModel,
  DataGridProProps,
} from '@mui/x-data-grid-pro';
import Box from '@mui/material/Box';
import Checkbox from '@mui/material/Checkbox';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Typography from '@mui/material/Typography';

const rows: GridRowsProp = [
  {
    hierarchy: ['Sarah'],
    jobTitle: 'Head of Human Resources',
    recruitmentDate: new Date(2020, 8, 12),
    id: 0,
  },
  {
    hierarchy: ['Thomas'],
    jobTitle: 'Head of Sales',
    recruitmentDate: new Date(2017, 3, 4),
    id: 1,
  },
  {
    hierarchy: ['Thomas', 'Robert'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 11, 20),
    id: 2,
  },
  {
    hierarchy: ['Thomas', 'Karen'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 10, 14),
    id: 3,
  },
  {
    hierarchy: ['Thomas', 'Nancy'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2017, 10, 29),
    id: 4,
  },
  {
    hierarchy: ['Thomas', 'Daniel'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 7, 21),
    id: 5,
  },
  {
    hierarchy: ['Thomas', 'Christopher'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2020, 7, 20),
    id: 6,
  },
  {
    hierarchy: ['Thomas', 'Donald'],
    jobTitle: 'Sales Person',
    recruitmentDate: new Date(2019, 6, 28),
    id: 7,
  },
  {
    hierarchy: ['Mary'],
    jobTitle: 'Head of Engineering',
    recruitmentDate: new Date(2016, 3, 14),
    id: 8,
  },
  {
    hierarchy: ['Mary', 'Jennifer'],
    jobTitle: 'Tech lead front',
    recruitmentDate: new Date(2016, 5, 17),
    id: 9,
  },
  {
    hierarchy: ['Mary', 'Jennifer', 'Anna'],
    jobTitle: 'Front-end developer',
    recruitmentDate: new Date(2019, 11, 7),
    id: 10,
  },
  {
    hierarchy: ['Mary', 'Michael'],
    jobTitle: 'Tech lead devops',
    recruitmentDate: new Date(2021, 7, 1),
    id: 11,
  },
  {
    hierarchy: ['Mary', 'Linda'],
    jobTitle: 'Tech lead back',
    recruitmentDate: new Date(2017, 0, 12),
    id: 12,
  },
  {
    hierarchy: ['Mary', 'Linda', 'Elizabeth'],
    jobTitle: 'Back-end developer',
    recruitmentDate: new Date(2019, 2, 22),
    id: 13,
  },
  {
    hierarchy: ['Mary', 'Linda', 'William'],
    jobTitle: 'Back-end developer',
    recruitmentDate: new Date(2018, 4, 19),
    id: 14,
  },
];

const columns: GridColDef[] = [
  { field: 'jobTitle', headerName: 'Job Title', width: 200 },
  {
    field: 'recruitmentDate',
    headerName: 'Recruitment Date',
    type: 'date',
    width: 150,
  },
];

const getTreeDataPath: DataGridProProps['getTreeDataPath'] = (row) => row.hierarchy;

export default function TreeDataDisableChildrenSorting() {
  const [disableChildrenSorting, setDisableChildrenSorting] = React.useState(true);
  const [sortModel, setSortModel] = React.useState<GridSortModel>([
    { field: 'recruitmentDate', sort: 'asc' },
  ]);

  return (
    <Box sx={{ width: '100%' }}>
      <FormGroup>
        <FormControlLabel
          control={
            <Checkbox
              checked={disableChildrenSorting}
              onChange={(event) => setDisableChildrenSorting(event.target.checked)}
            />
          }
          label={
            <Typography component="span">
              Apply <code>disableChildrenSorting</code>
            </Typography>
          }
        />
      </FormGroup>
      <Box sx={{ height: 400, mt: 1 }}>
        <DataGridPro
          treeData
          rows={rows}
          columns={columns}
          disableChildrenSorting={disableChildrenSorting}
          getTreeDataPath={getTreeDataPath}
          sortModel={sortModel}
          onSortModelChange={setSortModel}
          defaultGroupingExpansionDepth={-1}
        />
      </Box>
    </Box>
  );
}

```

:::warning
When using `sortingMode="server"`, a child must always immediately follow its parent:

```ts
// ✅ Row A.A immediately follows its parent
const validRows = [{ path: ['A'] }, { path: ['A', 'A'] }, { path: ['B'] }];

// ❌ Row X.X does not immediately follow its parent
const invalidRows = [{ path: ['X'] }, { path: ['Y'] }, { path: ['X', 'X'] }];
```

:::

## Drag-and-drop tree data reordering

With row reordering, users can reorder tree data or move rows from one group to another.

To enable this feature with tree data, pass the `rowReordering` prop to the Data Grid component.
You also need to pass the `setTreeDataPath()` prop to revert the operation done by [`getTreeDataPath()`](/x/api/data-grid/data-grid-pro/#data-grid-pro-prop-getTreeDataPath) while building the tree, because row reordering can change the path of the row.

```tsx
<DataGridPro
  columns={columns}
  rows={rows}
  treeData
  getTreeDataPath={getTreeDataPath}
  setTreeDataPath={setTreeDataPath}
  rowReordering
/>
```

```tsx
import * as React from 'react';
import { DataGridPro, type DataGridProProps } from '@mui/x-data-grid-pro';
import { useDemoData } from '@mui/x-data-grid-generator';

const getTreeDataPath: DataGridProProps['getTreeDataPath'] = (row) => {
  return row.path;
};

const setTreeDataPath: DataGridProProps['setTreeDataPath'] = (path, row) => {
  return {
    ...row,
    path,
  };
};

export default function TreeDataReordering() {
  const { data, loading } = useDemoData({
    dataSet: 'Employee',
    rowLength: 100,
    treeData: { maxDepth: 3, groupingField: 'name', averageChildren: 2 },
  });

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGridPro
        {...data}
        loading={loading}
        rowReordering
        disableRowSelectionOnClick
        getTreeDataPath={getTreeDataPath}
        setTreeDataPath={setTreeDataPath}
      />
    </div>
  );
}

```

### Reordering persistance

To sync the updated row order with an external store, depending on how you manage the order of rows in the external store, you can use either [`processRowUpdate()`](/x/api/data-grid/data-grid-pro/#data-grid-pro-prop-processRowUpdate) or the [`onRowOrderChange()`](/x/api/data-grid/data-grid-pro/#data-grid-pro-prop-onRowOrderChange) callback, or both.

The `processRowUpdate()` callback is triggered whenever a row is updated either by row editing or when the `path` value is updated during a cross parent reorder operation.

After the reorder operation is successfully completed, the `onRowOrderChange()` callback is triggered, which contains information about the new row reordering of the format [`GridRowOrderChangeParams`](/x/api/data-grid/grid-row-order-change-params/).

```tsx
<DataGridPro
  // Fired when:
  // - A row is edited (e.g. when the user changes the value of a cell)
  // - The `path` value is updated during a cross parent reorder operation
  processRowUpdate={processRowUpdate}
  // Fired after a reorder operation is completed
  onRowOrderChange={handleRowOrderChange}
/>
```

The demo below uses a custom data store bound using `useSyncExternalStore()` to persist the row data in local storage.

It maintains a row tree structure which is used to recompute path values after a reorder operation is performed, these props are used to sync the updated row order with the external store:

- **`processRowUpdate()`**: Used to update the row data when a row is edited (`path` value change isn't needed due to dynamic path computation. For static paths, you might need to also sync the `path` values).
- **`onRowOrderChange()`**: Used to capture the new row order after a reorder operation is performed, and update the external store with the new row order.

You can test out the demo by reordering the rows and then refreshing the page to see that the order persists.

```tsx
import * as React from 'react';
import {
  DataGridPro,
  useGridApiRef,
  type DataGridProProps,
} from '@mui/x-data-grid-pro';
import Button from '@mui/material/Button';
import { TreeDataSyncRowDataGroupingCell } from './utils/TreeDataSyncRowDataGroupingCell';
import { DataStore } from './utils/DataStore';

export default function TreeDataSyncRowData() {
  const apiRef = useGridApiRef();

  const dataStore = React.useMemo(() => new DataStore(), []);

  const { rows, loading } = React.useSyncExternalStore(
    dataStore.subscribe,
    dataStore.getSnapshot,
    dataStore.getSnapshot,
  );

  return (
    <div
      style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: 10 }}
    >
      <Button variant="outlined" onClick={() => dataStore.reset()}>
        Reset Local Storage Data
      </Button>
      <div style={{ height: 400 }}>
        <DataGridPro
          apiRef={apiRef}
          loading={loading}
          rows={rows}
          columns={columns}
          treeData
          rowReordering
          isValidRowReorder={isValidRowReorder}
          disableRowSelectionOnClick
          onRowOrderChange={dataStore.handleRowOrderChange}
          processRowUpdate={dataStore.processRowUpdate}
          getTreeDataPath={getTreeDataPath}
          setTreeDataPath={setTreeDataPath}
          groupingColDef={groupingColDef}
        />
      </div>
    </div>
  );
}

const columns: DataGridProProps['columns'] = [
  {
    field: 'type',
    headerName: 'Type',
    width: 120,
    editable: true,
    valueGetter: (value) => {
      const typeMap: Record<string, string> = {
        folder: 'Folder',
        tsx: 'TypeScript',
        ts: 'TypeScript',
        json: 'JSON',
        md: 'Markdown',
        css: 'CSS',
        svg: 'SVG Image',
        png: 'PNG Image',
        jpg: 'JPEG Image',
        txt: 'Text',
      };
      return typeMap[value] || value;
    },
  },
  {
    field: 'modified',
    headerName: 'Modified',
    editable: true,
    width: 140,
    type: 'date',
    valueFormatter: (value) => {
      if (!value) {
        return '';
      }
      const date = new Date(value);
      return date.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      });
    },
  },
  { field: 'size', headerName: 'Size', width: 100, editable: true },
];

const isValidRowReorder: DataGridProProps['isValidRowReorder'] = (context) => {
  const targetRow = context.apiRef.current.getRow(context.targetNode.id);
  if (
    !targetRow ||
    (targetRow.type.toLowerCase() !== 'folder' && context.dropPosition === 'inside')
  ) {
    return false;
  }
  return true;
};

const getTreeDataPath: DataGridProProps['getTreeDataPath'] = (row) => {
  return row.path;
};

const setTreeDataPath: DataGridProProps['setTreeDataPath'] = (path, row) => {
  return {
    ...row,
    path,
  };
};

const groupingColDef: DataGridProProps['groupingColDef'] = {
  headerName: 'Name',
  renderCell: TreeDataSyncRowDataGroupingCell as any,
};

```

:::info
The demo above uses the `isValidRowReorder()` prop to disallow converting files (or leaf rows) into parents.

Check the [Row ordering—Disable specific reorder operations](/x/react-data-grid/row-ordering/#disable-specific-reorder-operations) documentation section for more details.
:::

## Lazy-loading tree data children

See [Server-side data—Tree data](/x/react-data-grid/server-side-data/tree-data/) for details on lazy-loading tree data children.

## API

- [DataGrid](/x/api/data-grid/data-grid/)
- [DataGridPro](/x/api/data-grid/data-grid-pro/)
- [DataGridPremium](/x/api/data-grid/data-grid-premium/)
- [GridRowOrderChangeParams](/x/api/data-grid/grid-row-order-change-params/)
