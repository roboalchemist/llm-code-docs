# Source: https://mui.com/x/react-data-grid/undo-redo.md

---
title: Data Grid - Undo and redo
---

# Data Grid - Undo and redo [<span class="plan-premium"></span>](/x/introduction/licensing/#premium-plan 'Premium plan')

Let users undo and reapply changes made to the Data Grid.

The undo/redo feature lets users reverse and reapply their actions in the Data Grid.
It tracks registered events, listens for keyboard events and adds toolbar buttons.

## Basic usage

The undo/redo feature is enabled when at least one history event handler is registered and `historyStackSize` is greater than 0 (default is 30).
The toolbar automatically displays undo and redo buttons when the feature is active.

Users can:

- Undo an action using <kbd><kbd class="key">Ctrl</kbd>+<kbd class="key">Z</kbd></kbd> (<kbd><kbd class="key">⌘ Command</kbd>+<kbd class="key">Z</kbd></kbd> on macOS)
- Redo an action using <kbd><kbd class="key">Ctrl</kbd>+<kbd class="key">Shift</kbd>+<kbd class="key">Z</kbd></kbd> and <kbd><kbd class="key">Ctrl</kbd>+<kbd class="key">Y</kbd></kbd> (<kbd><kbd class="key">⌘ Command</kbd>+<kbd class="key">Shift</kbd>+<kbd class="key">Z</kbd></kbd> and <kbd><kbd class="key">⌘ Command</kbd>+<kbd class="key">Y</kbd></kbd> on macOS)

In the following demo, undo-redo is available for the "edit" and "paste" operations.

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGridPremium } from '@mui/x-data-grid-premium';
import { useDemoData } from '@mui/x-data-grid-generator';

export default function BasicUndoRedo() {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 200,
    editable: true,
  });

  return (
    <Box sx={{ height: 450, width: '100%' }}>
      <DataGridPremium
        {...data}
        pagination
        showToolbar
        disableRowSelectionOnClick
        cellSelection
        disablePivoting
      />
    </Box>
  );
}

```

### Disabling the undo and redo

To disable the undo/redo feature, set `historyStackSize` to `0`:

```tsx
<DataGridPremium historyStackSize={0} />
```

This removes existing history, prevents any further history from being tracked, and hides the undo/redo buttons from the toolbar.

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';
import { DataGridPremium } from '@mui/x-data-grid-premium';
import { useDemoData } from '@mui/x-data-grid-generator';

export default function ToggleUndoRedo() {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 200,
    editable: true,
  });

  const [stackSize, setStackSize] = React.useState(0);

  return (
    <Box style={{ width: '100%' }}>
      <FormControlLabel
        control={
          <Checkbox
            checked={stackSize > 0}
            onChange={(event) => setStackSize(event.target.checked ? 10 : 0)}
          />
        }
        label="Enable undo/redo"
      />
      <Box style={{ height: 450, position: 'relative' }}>
        <DataGridPremium
          {...data}
          pagination
          showToolbar
          disableRowSelectionOnClick
          cellSelection
          disablePivoting
          historyStackSize={stackSize}
        />
      </Box>
    </Box>
  );
}

```

### Removing the toolbar buttons

To remove the toolbar buttons for undo and redo while keeping the keyboard controls active, set the `showHistoryControls` flag to `false` in the Toolbar's slot props.

```tsx
<DataGridPremium
  slotProps={{
    toolbar: {
      showHistoryControls: false,
      // ... other toolbar slotProps
    },
    // ... other slotProps
  }}
/>
```

## History event handlers

The Data Grid tracks changes and stores the data that can be used to revert those changes based on the provided history event handlers. Each handler must correspond to one of the [Data Grid events](/x/react-data-grid/events/#catalog-of-events).

A history event handler is an object that defines how to `store()`, `undo()`, `redo()`, and `validate()` the ability to undo or redo an action.

```tsx
interface GridHistoryEventHandler<T = any> {
  // Store the data when the event occurs.
  // Return `null` to skip adding the current change to the stack (to control undo step granularity)
  store: (...params: any[]) => T | null;

  // Undo the action
  undo: (data: T) => void | Promise<void>;

  // Redo the action
  redo: (data: T) => void | Promise<void>;

  // Validate whether the operation can be performed
  // Can be omitted if validation is not needed for the current history event handler
  validate?: (data: T, operation: 'undo' | 'redo') => boolean;
}
```

### Default handlers

The list of events that are handled by default depends on the props passed to Data Grid.

If none of the columns are [editable](/x/react-data-grid/editing/#making-a-column-editable), and [`isCellEditable()`](/x/react-data-grid/editing/#disable-editing-of-specific-cells-within-a-row) is not provided, then the feature is disabled because there are no default event handlers.

If there are editable cells, then the list of the default handlers depends on the way the data is provided to Data Grid.

When not using a [Data Source](/x/react-data-grid/server-side-data/), the following events are tracked out of the box:

- `rowEditStop` - Tracks changes made to entire rows in row edit mode
- `cellEditStop` - Tracks changes made to individual cells in cell edit mode
- `clipboardPasteEnd` - Tracks paste operations that can modify multiple cells

When using a Data Source, `clipboardPasteEnd` is not tracked and the other two events are only tracked if your Data Source is set up to support [editing](/x/react-data-grid/server-side-data/#updating-server-side-data) (by providing the `updateRow` method).

If you use a Data Source that doesn't have an `updateRow` method, then the history event handler list is empty and the feature is disabled.

:::warning
Default handlers invalidate the stack if the data is not visible to the user anymore due to filtering, grouping, page change, etc.

Check the customization sections to learn how to change the default behavior.
:::

The following demo shows the undo/redo feature working with a Data Source that supports row editing.
Remove the `updateRow` method to see the toolbar adjustment.

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGridPremium, GridDataSource } from '@mui/x-data-grid-premium';
import { useMockServer } from '@mui/x-data-grid-generator';

export default function DataSourceUndoRedo() {
  const {
    columns,
    initialState: initState,
    fetchRows,
    editRow,
  } = useMockServer({ editable: true }, { useCursorPagination: false });

  const dataSource: GridDataSource = React.useMemo(
    () => ({
      getRows: async (params) => {
        const urlParams = new URLSearchParams({
          paginationModel: JSON.stringify(params.paginationModel),
          filterModel: JSON.stringify(params.filterModel),
          sortModel: JSON.stringify(params.sortModel),
        });
        const getRowsResponse = await fetchRows(
          `https://mui.com/x/api/data-grid?${urlParams.toString()}`,
        );
        return {
          rows: getRowsResponse.rows,
          rowCount: getRowsResponse.rowCount,
        };
      },
      updateRow: (params) => editRow(params.rowId, params.updatedRow),
    }),
    [fetchRows, editRow],
  );

  const initialState = React.useMemo(
    () => ({
      ...initState,
      pagination: {
        paginationModel: { pageSize: 10, page: 0 },
        rowCount: 0,
      },
    }),
    [initState],
  );

  return (
    <Box sx={{ height: 450, width: '100%' }}>
      <DataGridPremium
        columns={columns}
        dataSource={dataSource}
        pagination
        initialState={initialState}
        pageSizeOptions={[10, 20, 50]}
        showToolbar
        disableRowSelectionOnClick
        cellSelection
        disablePivoting
        disableRowGrouping
        disableColumnPinning
      />
    </Box>
  );
}

```

## Custom history event handlers

Provide your own map of the history event handlers via the `historyEventHandlers` prop to change the default handlers or to track more events and add them to the undo/redo stack.
Use default handler exports (like `createCellEditHistoryHandler()`) to create a map that can combine:

- default handlers
- your own handlers replacing default handlers
- handlers for other events not covered by the default handlers

### Customizing default handlers

The following demo shows how to customize the cell edit and clipboard paste handlers to:

- Keep undo/redo operations valid even when the cell is on a different page
- Automatically navigate to the correct page when undoing/redoing

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import {
  DataGridPremium,
  useGridApiRef,
  GridHistoryEventHandler,
  GridEvents,
  GridApiPremium,
} from '@mui/x-data-grid-premium';
import { useDemoData } from '@mui/x-data-grid-generator';
import {
  createCustomCellEditHandler,
  createCustomClipboardPasteHistoryHandler,
} from './customHistoryEventHandlers';

export default function CustomHandlers() {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 200,
    editable: true,
  });

  const apiRef = useGridApiRef() as React.RefObject<GridApiPremium>;

  const historyEventHandlers = React.useMemo(() => {
    if (!apiRef.current) {
      return {};
    }

    return {
      cellEditStop: createCustomCellEditHandler(apiRef),
      clipboardPasteEnd: createCustomClipboardPasteHistoryHandler(apiRef),
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [apiRef.current]) as Record<GridEvents, GridHistoryEventHandler<any>>;

  return (
    <Box sx={{ height: 500, width: '100%' }}>
      <DataGridPremium
        {...data}
        apiRef={apiRef}
        pagination
        pageSizeOptions={[50, 100]}
        showToolbar
        disableRowSelectionOnClick
        cellSelection
        disablePivoting
        disableRowGrouping
        disableColumnPinning
        historyEventHandlers={historyEventHandlers}
        initialState={{
          ...data.initialState,
          pagination: { paginationModel: { pageSize: 50 } },
        }}
      />
    </Box>
  );
}

```

### Creating a new handler

Track and let users undo of any Data Grid interaction by providing custom history event handlers.

The following demo keeps all the default handlers, and adds a custom history handler that tracks filter model changes.
This lets users to undo and redo filter operations.

To reduce the number of undo steps, changes on the filter model items that do not have a value are ignored.

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import {
  DataGridPremium,
  useGridApiRef,
  GridHistoryEventHandler,
  GridEvents,
  GridFilterModel,
  GridApiPremium,
  createClipboardPasteHistoryHandler,
  createRowEditHistoryHandler,
  createCellEditHistoryHandler,
} from '@mui/x-data-grid-premium';
import { useDemoData } from '@mui/x-data-grid-generator';
import { isDeepEqual } from './utils';

interface FilterHistoryData {
  oldFilterModel: GridFilterModel;
  newFilterModel: GridFilterModel;
}

function createFilterHistoryHandler(
  apiRef: React.RefObject<GridApiPremium>,
): GridHistoryEventHandler<FilterHistoryData> {
  let previousFilterModel: GridFilterModel | undefined;

  return {
    store: (newFilterModel: GridFilterModel) => {
      const oldFilterModel = previousFilterModel;
      previousFilterModel = { ...newFilterModel };

      // Ignore changes made to the operator for the empty values
      const oldFilterItemsWithValues = oldFilterModel?.items.filter(
        (item) => item.value !== undefined,
      );
      const newFilterItemsWithValues = newFilterModel.items.filter(
        (item) => item.value !== undefined,
      );

      if (
        !oldFilterModel &&
        newFilterItemsWithValues.length === 0 &&
        newFilterModel.quickFilterValues?.length === 0
      ) {
        return null;
      }

      if (
        oldFilterModel &&
        isDeepEqual(oldFilterItemsWithValues, newFilterItemsWithValues) &&
        isDeepEqual(
          oldFilterModel.quickFilterValues,
          newFilterModel.quickFilterValues,
        ) &&
        oldFilterModel.logicOperator === newFilterModel.logicOperator &&
        oldFilterModel.quickFilterLogicOperator ===
          newFilterModel.quickFilterLogicOperator
      ) {
        return null;
      }

      return {
        oldFilterModel: oldFilterModel || { items: [] },
        newFilterModel,
      };
    },

    undo: async (data: FilterHistoryData) => {
      const { oldFilterModel } = data;
      apiRef.current.setFilterModel(oldFilterModel);
    },

    redo: async (data: FilterHistoryData) => {
      const { newFilterModel } = data;
      apiRef.current.setFilterModel(newFilterModel);
    },
  };
}

export default function AddFilterHandler() {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 200,
    editable: true,
  });

  const apiRef = useGridApiRef() as React.RefObject<GridApiPremium>;

  const historyEventHandlers = React.useMemo(() => {
    if (!apiRef.current) {
      return {};
    }

    return {
      cellEditStop: createCellEditHistoryHandler(apiRef),
      rowEditStop: createRowEditHistoryHandler(apiRef),
      clipboardPasteEnd: createClipboardPasteHistoryHandler(apiRef),
      filterModelChange: createFilterHistoryHandler(apiRef),
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [apiRef.current]) as Record<GridEvents, GridHistoryEventHandler<any>>;

  return (
    <Box sx={{ height: 500, width: '100%' }}>
      <DataGridPremium
        {...data}
        apiRef={apiRef}
        historyEventHandlers={historyEventHandlers}
        showToolbar
        disableRowSelectionOnClick
        cellSelection
        disablePivoting
        disableRowGrouping
        disableColumnPinning
      />
    </Box>
  );
}

```

## Validation events

The undo/redo state is automatically revalidated when certain grid events occur.
By default, validation happens on `paginationModelChange`, `columnsChange`, `sortedRowsSet`, `filteredRowsSet` and `rowsSet` events.

During revalidation, the `validate()` method of the current item in the stack is called for the `undo` operation and the `validate()` method of the next item in the stack is called for the `redo` operation.
If validation fails for the `undo` operation, all items in the stack before the current item and the current item itself are removed from the stack.
If validation fails for the `redo` operation, all items after the current item in the stack are removed from the stack.

### Customizing validation events

You can customize which events trigger revalidation using the `historyValidationEvents` prop.

```tsx
<DataGridPremium historyValidationEvents={['stateChange']} />
```

This is useful when you create a handler that tracks changes that don't affect rows or columns, or if you remove the default handlers and you don't need the validation on the default events anymore.

:::warning
List the events in the `historyValidationEvents` prop that are sufficient for validation to occur at the right time.
Be aware that adding `'stateChange'` to the list does have an impact on the performance of Data Grid.
:::

## API

- [DataGrid](/x/api/data-grid/data-grid/)
- [DataGridPro](/x/api/data-grid/data-grid-pro/)
- [DataGridPremium](/x/api/data-grid/data-grid-premium/)
