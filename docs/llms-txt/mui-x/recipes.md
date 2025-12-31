# Source: https://mui.com/x/react-data-grid/server-side-data/recipes.md

# Data Grid - Server-side data recipes

Recipes for advanced data source use-cases.

## Cursor-based pagination

Cursor-based pagination requires the cursor from the previous page's response to fetch the next page. Unlike offset pagination where you can jump to any page independently, each page request depends on the cursor returned from the earlier response.

There are two approaches to implement:

1. **Blocking approach**: Users can only navigate to the next page after the current response arrives with its cursor
2. **Non-blocking approach**: Allow users to click next immediately, but queue the request until the previous cursor becomes available

### Blocking approach

The following example demonstrates the blocking approach by controlling the `paginationModel` state.
It is only updated when the previous page's response arrives, ensuring that the cursor is always available for the next request.

```tsx
import * as React from 'react';
import {
  DataGrid,
  GridDataSource,
  GridPaginationModel,
  GridRowId,
} from '@mui/x-data-grid';
import { useMockServer } from '@mui/x-data-grid-generator';

export default function ServerSideCursorBlocking() {
  const { columns, initialState, fetchRows } = useMockServer(
    {},
    { useCursorPagination: true, minDelay: 1000, maxDelay: 2000 },
  );
  const [paginationModel, setPaginationModel] = React.useState({
    page: 0,
    pageSize: 10,
  });
  const paginationModelRef = React.useRef(paginationModel);
  paginationModelRef.current = paginationModel;

  const mapPageToNextCursor = React.useRef<{
    [page: number]: GridRowId | undefined;
  }>({});

  const handlePaginationModelChange = (newPaginationModel: GridPaginationModel) => {
    if (
      newPaginationModel.page === 0 ||
      mapPageToNextCursor.current[newPaginationModel.page - 1]
    ) {
      setPaginationModel(newPaginationModel);
    }
  };

  const dataSource: GridDataSource = React.useMemo(
    () => ({
      getRows: async (params) => {
        const cursor =
          mapPageToNextCursor.current[paginationModelRef.current.page - 1];
        const urlParams = new URLSearchParams({
          paginationModel: JSON.stringify(params.paginationModel),
          filterModel: JSON.stringify(params.filterModel),
          sortModel: JSON.stringify(params.sortModel),
          cursor: String(cursor ?? ''),
        });
        const getRowsResponse = await fetchRows(
          `https://mui.com/x/api/data-grid?${urlParams.toString()}`,
        );
        mapPageToNextCursor.current[params.paginationModel?.page || 0] =
          getRowsResponse.pageInfo?.nextCursor;
        return {
          rows: getRowsResponse.rows,
          rowCount: getRowsResponse.rowCount,
        };
      },
    }),
    [fetchRows],
  );

  return (
    <div style={{ width: '100%', height: 400 }}>
      <DataGrid
        columns={columns}
        dataSource={dataSource}
        pagination
        initialState={{
          ...initialState,
          pagination: { rowCount: 0 },
        }}
        paginationModel={paginationModel}
        onPaginationModelChange={handlePaginationModelChange}
        pageSizeOptions={[10, 20, 50]}
      />
    </div>
  );
}

```

### Non-blocking approach

The following example demonstrates the non-blocking approach using a custom cache with two key methods:

- **`pushKey()`**: Tracks request order before responses arrive, allowing immediate pagination
- **`getLast()`**: Waits for the previous page's cursor to resolve before making the actual request

The cache is cleared whenever the filter or sort model changes to ensure data consistency.

For error handling, the example simulates a server error when requesting page 8.
When an error occurs, the cache entry for that request is deleted, and the `paginationModel` is reverted to the previous page to maintain a consistent state.

```tsx
import * as React from 'react';
import {
  DataGrid,
  GridDataSource,
  GridGetRowsParams,
  GridGetRowsResponse,
  useGridApiRef,
} from '@mui/x-data-grid';
import Snackbar from '@mui/material/Snackbar';
import Alert, { AlertProps } from '@mui/material/Alert';
import { useMockServer } from '@mui/x-data-grid-generator';

function getKeyDefault(params: GridGetRowsParams) {
  return JSON.stringify([
    params.filterModel,
    params.sortModel,
    params.start,
    params.end,
  ]);
}

class Cache {
  private cache: Record<string, { value: GridGetRowsResponse }>;

  private cacheKeys: Set<string>;

  private getKey: (params: GridGetRowsParams) => string;

  constructor() {
    this.cache = {};
    this.cacheKeys = new Set();
    this.getKey = getKeyDefault;
  }

  set(key: GridGetRowsParams, value: GridGetRowsResponse) {
    const keyString = this.getKey(key);
    this.cache[keyString] = { value };
  }

  get(key: GridGetRowsParams): GridGetRowsResponse | undefined {
    const keyString = this.getKey(key);
    const entry = this.cache[keyString];
    if (!entry) {
      return undefined;
    }

    return entry.value;
  }

  pushKey(key: GridGetRowsParams) {
    const keyString = this.getKey(key);
    this.cacheKeys.add(keyString);
  }

  deleteKey(key: GridGetRowsParams) {
    const keyString = this.getKey(key);
    delete this.cache[keyString];
    this.cacheKeys.delete(keyString);
  }

  async getLast(key: GridGetRowsParams): Promise<GridGetRowsResponse | undefined> {
    const cacheKeys = Array.from(this.cacheKeys);
    const prevKey = cacheKeys[cacheKeys.indexOf(this.getKey(key)) - 1];
    if (!prevKey) {
      return undefined;
    }
    if (this.cache[prevKey]) {
      return this.cache[prevKey].value;
    }
    return new Promise((resolve) => {
      const intervalId = setInterval(() => {
        if (this.cache[prevKey]) {
          clearInterval(intervalId);
          resolve(this.cache[prevKey].value);
        }
      }, 100);
    });
  }

  clear() {
    this.cache = {};
    this.cacheKeys.clear();
  }
}

export default function ServerSideCursorNonBlocking() {
  const apiRef = useGridApiRef();
  const [snackbar, setSnackbar] = React.useState<AlertProps | null>(null);
  const { columns, initialState, fetchRows } = useMockServer(
    {},
    { useCursorPagination: true, minDelay: 200, maxDelay: 500 },
  );
  const cache = React.useMemo(() => new Cache(), []);

  const dataSource: GridDataSource = React.useMemo(
    () => ({
      getRows: async (params) => {
        cache.pushKey(params);
        const latestResponse = await cache.getLast(params);
        const urlParams = new URLSearchParams({
          paginationModel: JSON.stringify(params.paginationModel),
          filterModel: JSON.stringify(params.filterModel),
          sortModel: JSON.stringify(params.sortModel),
          cursor: String(latestResponse?.pageInfo?.nextCursor ?? ''),
        });
        try {
          if (params.paginationModel?.page === 7) {
            throw new Error('Simulate server error on page 8');
          }
          const getRowsResponse = await fetchRows(
            `https://mui.com/x/api/data-grid?${urlParams.toString()}`,
          );
          return {
            rows: getRowsResponse.rows,
            rowCount: getRowsResponse.rowCount,
            pageInfo: { nextCursor: getRowsResponse.pageInfo?.nextCursor },
          };
        } catch (error) {
          cache.deleteKey(params);
          apiRef.current?.setPaginationModel({
            page: params.paginationModel!.page - 1,
            pageSize: params.paginationModel!.pageSize,
          });
          setSnackbar({ children: (error as Error).message, severity: 'error' });
          throw error;
        }
      },
    }),
    [fetchRows, cache, apiRef],
  );

  const handleCloseSnackbar = () => {
    setSnackbar(null);
  };

  return (
    <div style={{ width: '100%', height: 400 }}>
      <DataGrid
        apiRef={apiRef}
        columns={columns}
        dataSource={dataSource}
        dataSourceCache={cache}
        pagination
        initialState={{
          ...initialState,
          pagination: {
            paginationModel: {
              page: 0,
              pageSize: 10,
            },
            rowCount: 0,
          },
        }}
        pageSizeOptions={[10, 20, 50]}
        onFilterModelChange={() => cache.clear()}
        onSortModelChange={() => cache.clear()}
      />
      {!!snackbar && (
        <Snackbar
          open
          anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
          onClose={handleCloseSnackbar}
          autoHideDuration={6000}
        >
          <Alert {...snackbar} onClose={handleCloseSnackbar} />
        </Snackbar>
      )}
    </div>
  );
}

```

## Tree data nested pagination

By default, the pagination works only on the first level of the tree.
You can create the nested pagination with [row pinning](/x/react-data-grid/row-pinning/) feature as shown in the following demo.

:::warning

This demo implements nested lazy loading using row pinning, which means that certain features such as caching, row selection, and copy & paste functionality may not work as expected.

Check the [Server-side data—Nested lazy loading](/x/react-data-grid/server-side-data/lazy-loading/#nested-lazy-loading) section for updates on an internal implementation.

:::

```tsx
import * as React from 'react';
import {
  DataGridPro,
  useGridApiRef,
  type GridDataSource,
} from '@mui/x-data-grid-pro';
import { useMockServer } from '@mui/x-data-grid-generator';
import useNestedPagination from './useNestedPagination';

const pageSizeOptions = [5, 10, 50];
const dataSetOptions = {
  dataSet: 'Employee' as const,
  rowLength: 1000,
  treeData: { maxDepth: 3, groupingField: 'name', averageChildren: 20 },
};
const serverOptions = {};

const initialPaginationModel = {
  pageSize: 5,
  page: 0,
};

export default function ServerSideTreeDataNestedPagination() {
  const apiRef = useGridApiRef();

  const { groupKeys, ...props } = useNestedPagination(initialPaginationModel);
  const { fetchRows, columns, initialState } = useMockServer(
    dataSetOptions,
    serverOptions,
    false,
    true,
  );

  const dataSource: GridDataSource = React.useMemo(
    () => ({
      getRows: async (params) => {
        const urlParams = new URLSearchParams({
          paginationModel: JSON.stringify(params.paginationModel),
          filterModel: JSON.stringify(params.filterModel),
          sortModel: JSON.stringify(params.sortModel),
          groupKeys: JSON.stringify(groupKeys),
        });
        const getRowsResponse = await fetchRows(
          `https://mui.com/x/api/data-grid?${urlParams.toString()}`,
        );
        return {
          rows: getRowsResponse.rows,
          rowCount: getRowsResponse.rowCount,
        };
      },
      getGroupKey: (row) => row[dataSetOptions.treeData.groupingField],
      getChildrenCount: (row) => row.descendantCount,
    }),
    [fetchRows, groupKeys],
  );

  return (
    <div style={{ width: '100%', height: 500 }}>
      <DataGridPro
        {...props}
        columns={columns}
        dataSource={dataSource}
        dataSourceCache={null}
        treeData
        apiRef={apiRef}
        pagination
        pageSizeOptions={pageSizeOptions}
        initialState={initialState}
        showToolbar
      />
    </div>
  );
}

```
