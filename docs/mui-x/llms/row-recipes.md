# Source: https://mui.com/x/react-data-grid/row-recipes.md

---
title: Data Grid - Row customization recipes
---

# Data Grid - Row customization recipes

Advanced row customization recipes.

## One expanded detail panel at a time

By default, the [Master-detail row panel <span class="plan-pro" />](/x/react-data-grid/master-detail/) feature supports multiple expanded detail panels simultaneously.

However, you can [control the expanded detail panels](/x/react-data-grid/master-detail/#controlling-expanded-detail-panels) to have only one detail panel expanded at a time.

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import {
  DataGridPro,
  DataGridProProps,
  GridRowsProp,
  GridRowId,
  GridColDef,
} from '@mui/x-data-grid-pro';
import {
  randomCreatedDate,
  randomCurrency,
  randomEmail,
  randomPrice,
} from '@mui/x-data-grid-generator';

const getDetailPanelContent: DataGridProProps['getDetailPanelContent'] = ({
  row,
}) => <Box sx={{ p: 2 }}>{`Order #${row.id}`}</Box>;
const getDetailPanelHeight: DataGridProProps['getDetailPanelHeight'] = () => 50;

export default function DetailPanelOneExpandedRow() {
  const [detailPanelExpandedRowIds, setDetailPanelExpandedRowIds] = React.useState(
    () => new Set<GridRowId>(),
  );

  const handleDetailPanelExpandedRowIdsChange = React.useCallback<
    NonNullable<DataGridProProps['onDetailPanelExpandedRowIdsChange']>
  >((newIds) => {
    if (newIds.size > 1) {
      const newSet = new Set<GridRowId>();
      const newIdsArray = Array.from(newIds);
      newSet.add(newIdsArray[newIdsArray.length - 1]);
      setDetailPanelExpandedRowIds(newSet);
    } else {
      setDetailPanelExpandedRowIds(newIds);
    }
  }, []);

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <DataGridPro
        rows={rows}
        columns={columns}
        getDetailPanelContent={getDetailPanelContent}
        getDetailPanelHeight={getDetailPanelHeight}
        detailPanelExpandedRowIds={detailPanelExpandedRowIds}
        onDetailPanelExpandedRowIdsChange={handleDetailPanelExpandedRowIdsChange}
      />
    </Box>
  );
}

const columns: GridColDef[] = [
  { field: 'id', headerName: 'Order ID' },
  { field: 'customer', headerName: 'Customer', width: 200 },
  { field: 'date', type: 'date', headerName: 'Placed at' },
  { field: 'currency', headerName: 'Currency' },
  { field: 'total', type: 'number', headerName: 'Total' },
];

const rows: GridRowsProp = [
  {
    id: 1,
    customer: 'Matheus',
    email: randomEmail(),
    date: randomCreatedDate(),
    currency: randomCurrency(),
    total: randomPrice(1, 1000),
  },
  {
    id: 2,
    customer: 'Olivier',
    email: randomEmail(),
    date: randomCreatedDate(),
    currency: randomCurrency(),
    total: randomPrice(1, 1000),
  },
  {
    id: 3,
    customer: 'Flavien',
    email: randomEmail(),
    date: randomCreatedDate(),
    currency: randomCurrency(),
    total: randomPrice(1, 1000),
  },
  {
    id: 4,
    customer: 'Danail',
    email: randomEmail(),
    date: randomCreatedDate(),
    currency: randomCurrency(),
    total: randomPrice(1, 1000),
  },
  {
    id: 5,
    customer: 'Alexandre',
    email: randomEmail(),
    date: randomCreatedDate(),
    currency: randomCurrency(),
    total: randomPrice(1, 1000),
  },
];

```

## Expand or collapse all detail panels

The following demo shows how to create a custom header element that expands or collapses all detail panels at once.

Here's how it works:

The custom header uses `gridRowsLookupSelector` to find all rows with a detail panel.
It checks the status of open panels using the [`useGridSelector` hook](/x/react-data-grid/state/#with-usegridselector) to access the grid's state.
When clicked, it uses [`setExpandedDetailPanels`](/x/api/data-grid/grid-api/#grid-api-prop-setExpandedDetailPanels) from the [Grid API](/x/react-data-grid/api-object/#how-to-use-the-api-object) to expand or collapse all detail panels.

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import IconButton from '@mui/material/IconButton';
import UnfoldLessIcon from '@mui/icons-material/UnfoldLess';
import UnfoldMoreIcon from '@mui/icons-material/UnfoldMore';
import {
  DataGridPro,
  GridColDef,
  GridRowsProp,
  GridRowParams,
  useGridApiContext,
  useGridSelector,
  gridRowsLookupSelector,
  gridDetailPanelExpandedRowIdsSelector,
  gridDetailPanelExpandedRowsContentCacheSelector,
  GRID_DETAIL_PANEL_TOGGLE_COL_DEF,
  GridRowId,
} from '@mui/x-data-grid-pro';
import {
  randomCreatedDate,
  randomCurrency,
  randomEmail,
  randomPrice,
} from '@mui/x-data-grid-generator';

export default function DetailPanelExpandCollapseAll() {
  const getDetailPanelContent = React.useCallback(
    ({ row }: GridRowParams) => <Box sx={{ p: 2 }}>{`Order #${row.id}`}</Box>,
    [],
  );

  const getDetailPanelHeight = React.useCallback(() => 50, []);

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGridPro
        rows={rows}
        columns={columns}
        getDetailPanelContent={getDetailPanelContent}
        getDetailPanelHeight={getDetailPanelHeight}
      />
    </div>
  );
}

function CustomDetailPanelHeader() {
  const apiRef = useGridApiContext();

  const expandedRowIds = useGridSelector(
    apiRef,
    gridDetailPanelExpandedRowIdsSelector,
  );
  const rowsWithDetailPanels = useGridSelector(
    apiRef,
    gridDetailPanelExpandedRowsContentCacheSelector,
  );

  const noDetailPanelsOpen = expandedRowIds.size === 0;

  const expandOrCollapseAll = () => {
    if (noDetailPanelsOpen) {
      const dataRowIdToModelLookup = gridRowsLookupSelector(apiRef);
      const allRowIdsWithDetailPanels = new Set<GridRowId>();
      for (const key in rowsWithDetailPanels) {
        if (rowsWithDetailPanels.hasOwnProperty(key)) {
          allRowIdsWithDetailPanels.add(
            apiRef.current.getRowId(dataRowIdToModelLookup[key]),
          );
        }
      }
      apiRef.current.setExpandedDetailPanels(allRowIdsWithDetailPanels);
    } else {
      apiRef.current.setExpandedDetailPanels(new Set());
    }
  };

  const Icon = noDetailPanelsOpen ? UnfoldMoreIcon : UnfoldLessIcon;

  return (
    <IconButton
      size="small"
      tabIndex={-1}
      onClick={expandOrCollapseAll}
      aria-label={noDetailPanelsOpen ? 'Expand All' : 'Collapse All'}
    >
      <Icon fontSize="inherit" />
    </IconButton>
  );
}

const columns: GridColDef[] = [
  {
    ...GRID_DETAIL_PANEL_TOGGLE_COL_DEF,
    renderHeader: () => <CustomDetailPanelHeader />,
  },
  { field: 'id', headerName: 'Order ID' },
  { field: 'customer', headerName: 'Customer', width: 200 },
  { field: 'date', type: 'date', headerName: 'Placed at' },
  { field: 'currency', headerName: 'Currency' },
  { field: 'total', type: 'number', headerName: 'Total' },
];

const rows: GridRowsProp = [
  {
    id: 1,
    customer: 'Matheus',
    email: randomEmail(),
    date: randomCreatedDate(),
    currency: randomCurrency(),
    total: randomPrice(1, 1000),
  },
  {
    id: 2,
    customer: 'Olivier',
    email: randomEmail(),
    date: randomCreatedDate(),
    currency: randomCurrency(),
    total: randomPrice(1, 1000),
  },
  {
    id: 3,
    customer: 'Flavien',
    email: randomEmail(),
    date: randomCreatedDate(),
    currency: randomCurrency(),
    total: randomPrice(1, 1000),
  },
  {
    id: 4,
    customer: 'Danail',
    email: randomEmail(),
    date: randomCreatedDate(),
    currency: randomCurrency(),
    total: randomPrice(1, 1000),
  },
  {
    id: 5,
    customer: 'Alexandre',
    email: randomEmail(),
    date: randomCreatedDate(),
    currency: randomCurrency(),
    total: randomPrice(1, 1000),
  },
];

```

## Toggling detail panels on row click

In the demo below, you can toggle the detail panel by clicking anywhere on the row:

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import {
  DataGridPro,
  DataGridProProps,
  GridColDef,
  GridEventListener,
  useGridApiRef,
} from '@mui/x-data-grid-pro';
import {
  randomCreatedDate,
  randomPrice,
  randomCurrency,
  randomCountry,
  randomCity,
  randomEmail,
  randomInt,
  randomAddress,
  randomCommodity,
} from '@mui/x-data-grid-generator';

function DetailPanelContent({ row: rowProp }: { row: Customer }) {
  return (
    <Stack
      sx={{ py: 2, height: '100%', boxSizing: 'border-box' }}
      direction="column"
    >
      <Paper sx={{ flex: 1, mx: 'auto', width: '90%', p: 1 }}>
        <Stack direction="column" spacing={1} sx={{ height: 1 }}>
          <Typography variant="h6">{`Order #${rowProp.id}`}</Typography>
          <Grid container>
            <Grid size={{ md: 6 }}>
              <Typography variant="body2" color="textSecondary">
                Customer information
              </Typography>
              <Typography variant="body1">{rowProp.customer}</Typography>
              <Typography variant="body1">{rowProp.email}</Typography>
            </Grid>
            <Grid size={{ md: 6 }}>
              <Typography variant="body2" align="right" color="textSecondary">
                Shipping address
              </Typography>
              <Typography variant="body1" align="right">
                {rowProp.address}
              </Typography>
              <Typography
                variant="body1"
                align="right"
              >{`${rowProp.city}, ${rowProp.country.label}`}</Typography>
            </Grid>
          </Grid>
          <DataGridPro
            density="compact"
            columns={[
              { field: 'name', headerName: 'Product', flex: 1 },
              {
                field: 'quantity',
                headerName: 'Quantity',
                align: 'center',
                type: 'number',
              },
              { field: 'unitPrice', headerName: 'Unit Price', type: 'number' },
              {
                field: 'total',
                headerName: 'Total',
                type: 'number',
                valueGetter: (value, row) => row.quantity * row.unitPrice,
              },
            ]}
            rows={rowProp.products}
            sx={{ flex: 1 }}
            hideFooter
          />
        </Stack>
      </Paper>
    </Stack>
  );
}

const columns: GridColDef<(typeof rows)[number]>[] = [
  { field: 'id', headerName: 'Order ID' },
  { field: 'customer', headerName: 'Customer', width: 200 },
  { field: 'date', type: 'date', headerName: 'Placed at' },
  { field: 'currency', headerName: 'Currency' },
  {
    field: 'total',
    type: 'number',
    headerName: 'Total',
    valueGetter: (value, row) => {
      const subtotal = row.products.reduce(
        (acc: number, product: any) => product.unitPrice * product.quantity,
        0,
      );
      const taxes = subtotal * 0.05;
      return subtotal + taxes;
    },
  },
];

function generateProducts() {
  const quantity = randomInt(1, 5);
  return [...Array(quantity)].map((_, index) => ({
    id: index,
    name: randomCommodity(),
    quantity: randomInt(1, 5),
    unitPrice: randomPrice(1, 1000),
  }));
}

const rows = [
  {
    id: 1,
    customer: 'Matheus',
    email: randomEmail(),
    date: randomCreatedDate(),
    address: randomAddress(),
    country: randomCountry(),
    city: randomCity(),
    currency: randomCurrency(),
    products: generateProducts(),
  },
  {
    id: 2,
    customer: 'Olivier',
    email: randomEmail(),
    date: randomCreatedDate(),
    address: randomAddress(),
    country: randomCountry(),
    city: randomCity(),
    currency: randomCurrency(),
    products: generateProducts(),
  },
  {
    id: 3,
    customer: 'Flavien',
    email: randomEmail(),
    date: randomCreatedDate(),
    address: randomAddress(),
    country: randomCountry(),
    city: randomCity(),
    currency: randomCurrency(),
    products: generateProducts(),
  },
  {
    id: 4,
    customer: 'Danail',
    email: randomEmail(),
    date: randomCreatedDate(),
    address: randomAddress(),
    country: randomCountry(),
    city: randomCity(),
    currency: randomCurrency(),
    products: generateProducts(),
  },
  {
    id: 5,
    customer: 'Alexandre',
    email: randomEmail(),
    date: randomCreatedDate(),
    address: randomAddress(),
    country: randomCountry(),
    city: randomCity(),
    currency: randomCurrency(),
    products: generateProducts(),
  },
];

type Customer = (typeof rows)[number];

export default function DetailPanelExpandOnRowClick() {
  const getDetailPanelContent = React.useCallback<
    NonNullable<DataGridProProps['getDetailPanelContent']>
  >(({ row }) => <DetailPanelContent row={row} />, []);

  const getDetailPanelHeight = React.useCallback(() => 400, []);

  const apiRef = useGridApiRef();

  const onRowClick = React.useCallback<GridEventListener<'rowClick'>>(
    (params) => {
      apiRef.current?.toggleDetailPanel(params.id);
    },
    [apiRef],
  );

  return (
    <Box sx={{ width: '100%', height: 400 }}>
      <DataGridPro
        apiRef={apiRef}
        columns={columns}
        onRowClick={onRowClick}
        rows={rows}
        getDetailPanelHeight={getDetailPanelHeight}
        getDetailPanelContent={getDetailPanelContent}
      />
    </Box>
  );
}

```

## Lazy loading detail panels with auto height

In the demo below, detail panels have a height based on content (auto height) and are lazy loaded.
To prevent scrolling issues, panel heights are cached once they are loaded and the cached height is returned from the `getDetailPanelHeight()` callback.

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import {
  randomEmail,
  randomInt,
  randomCommodity,
  randomPrice,
  randomTraderName,
  randomId,
} from '@mui/x-data-grid-generator';
import {
  DataGridPro,
  DataGridProProps,
  GridColDef,
  GridRowId,
  GridRowParams,
} from '@mui/x-data-grid-pro';
import { DetailPanelWrapper, useDetailPanelCache } from './detailPanelCache';

type Products = Awaited<ReturnType<typeof getProducts>>;

const DetailPanelDataCache = React.createContext(new Map<GridRowId, Products>());

async function getProducts(orderId: Customer['id']) {
  await new Promise((resolve) => {
    setTimeout(resolve, 1000);
  });

  const quantity = randomInt(30, 50);
  return [...Array(quantity)].map((_, index) => ({
    id: index,
    orderId,
    name: randomCommodity(),
    quantity: randomInt(1, 5),
    unitPrice: randomPrice(1, 1000),
  }));
}

const detailPanelColumns: GridColDef[] = [
  { field: 'name', headerName: 'Product', flex: 1 },
  {
    field: 'quantity',
    headerName: 'Quantity',
    align: 'center',
    type: 'number',
  },
  { field: 'unitPrice', headerName: 'Unit Price', type: 'number' },
  {
    field: 'total',
    headerName: 'Total',
    type: 'number',
    valueGetter: (value, row) => row.quantity * row.unitPrice,
  },
];

function DetailPanelContent({
  row: rowProp,
  onLoaded,
}: {
  row: Customer;
  onLoaded?: () => void;
}) {
  const [isLoading, setLoading] = React.useState(true);
  const [products, setProducts] = React.useState<
    Awaited<ReturnType<typeof getProducts>>
  >([]);

  const detailPanelDataCache = React.useContext(DetailPanelDataCache) as Map<
    GridRowId,
    Products
  >;

  React.useEffect(() => {
    let isMounted = true;
    (async () => {
      if (!detailPanelDataCache.has(rowProp.id)) {
        console.log('fetching detail panel content for row', rowProp.id);
        const response = await getProducts(rowProp.id);
        // Store the data in cache so that when detail panel unmounts due to virtualization, the data is not lost
        detailPanelDataCache.set(rowProp.id, response);
      }

      const result = detailPanelDataCache.get(rowProp.id)!;

      if (!isMounted) {
        return;
      }

      setProducts(result);
      setLoading(false);
      onLoaded?.();
    })();

    return () => {
      isMounted = false;
    };
  }, [rowProp.id, detailPanelDataCache, onLoaded]);

  return (
    <Stack
      sx={{ py: 2, height: '100%', boxSizing: 'border-box' }}
      direction="column"
    >
      <Paper sx={{ flex: 1, mx: 'auto', width: '90%', p: 1 }}>
        <Stack direction="column" spacing={1} sx={{ height: 1 }}>
          <Typography variant="h6">{`Order #${rowProp.id}`}</Typography>
          <DataGridPro
            density="compact"
            loading={isLoading}
            columns={detailPanelColumns}
            rows={products}
            sx={{ flex: 1 }}
            hideFooter
          />
        </Stack>
      </Paper>
    </Stack>
  );
}

const columns: GridColDef[] = [
  { field: 'customer', headerName: 'Customer', width: 200 },
  { field: 'email', headerName: 'Email', width: 200 },
];

function getRow() {
  return {
    id: randomId(),
    customer: randomTraderName(),
    email: randomEmail(),
  };
}

const rows: ReturnType<typeof getRow>[] = [];
for (let i = 0; i < 30; i += 1) {
  rows.push(getRow());
}

type Customer = (typeof rows)[number];

export default function LazyLoadingAutoHeightDetailPanel() {
  const {
    detailPanelDataCache,
    detailPanelHeights,
    handleDetailPanelHeightChange,
    handleDetailPanelExpansionChange,
  } = useDetailPanelCache<Products>();

  const getDetailPanelHeight = React.useCallback(
    (params: { row: Customer }) => {
      const cachedHeight = detailPanelHeights.get(params.row.id);
      return cachedHeight ?? ('auto' as const);
    },
    [detailPanelHeights],
  );

  const getDetailPanelContent: DataGridProProps['getDetailPanelContent'] =
    React.useCallback(
      (params: GridRowParams<Customer>) => (
        <DetailPanelWrapper
          rowId={params.row.id}
          onHeightChange={handleDetailPanelHeightChange}
        >
          <DetailPanelContent row={params.row} />
        </DetailPanelWrapper>
      ),
      [handleDetailPanelHeightChange],
    );

  return (
    <Box sx={{ width: '100%', height: 400 }}>
      <DetailPanelDataCache.Provider value={detailPanelDataCache}>
        <DataGridPro
          columns={columns}
          rows={rows}
          getDetailPanelHeight={getDetailPanelHeight}
          getDetailPanelContent={getDetailPanelContent}
          onDetailPanelExpandedRowIdsChange={handleDetailPanelExpansionChange}
        />
      </DetailPanelDataCache.Provider>
    </Box>
  );
}

```

## Access Data Grid internal loading state

The following demo shows how to disable a button on the toolbar when the Data Grid is in loading state using the [`useGridSelector()`](https://mui.com/x/react-data-grid/state/#with-usegridselector) hook with the `gridRowsLoadingSelector()`.

```tsx
import Button from '@mui/material/Button';
import {
  DataGrid,
  Toolbar,
  useGridApiContext,
  gridRowsLoadingSelector,
  useGridSelector,
} from '@mui/x-data-grid';

function CustomToolbar() {
  const apiRef = useGridApiContext();
  const isLoading = useGridSelector(apiRef, gridRowsLoadingSelector);
  return (
    <Toolbar>
      <Button
        variant="outlined"
        loading={isLoading}
        onClick={() => apiRef.current?.setLoading(true)}
      >
        Set Loading
      </Button>
      {isLoading && (
        <Button onClick={() => apiRef.current?.setLoading(false)}>Cancel</Button>
      )}
    </Toolbar>
  );
}

const rows = [
  { id: 1, name: 'React' },
  { id: 2, name: 'MUI' },
];

const columns = [{ field: 'name' }];

export default function AccessingLoadingState() {
  return (
    <div style={{ height: 300, width: '100%' }}>
      <DataGrid
        columns={columns}
        rows={rows}
        slots={{ toolbar: CustomToolbar }}
        showToolbar
      />
    </div>
  );
}

```

:::info
The `useGridSelector()` is based on a React Context, so the component must be a child of the Data Grid in the React tree to access the internal state.

You could use a [React portal](https://react.dev/reference/react-dom/createPortal) to achieve the same while rendering the component outside the Data Grid DOM tree.
:::
