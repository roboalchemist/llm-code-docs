# Source: https://mui.com/x/react-data-grid/filtering-recipes.md

---
title: Data Grid - Filtering customization recipes
---

# Data Grid - Filtering customization recipes

Advanced filtering customization recipes.

## Persisting filters in local storage

You can persist the filters in the local storage to keep the filters applied after the page is reloaded.

In the demo below, the [`React.useSyncExternalStore` hook](https://react.dev/reference/react/useSyncExternalStore) is used to synchronize the filters with the local storage.

```tsx
import * as React from 'react';
import { DataGrid, DataGridProps, GridFilterModel } from '@mui/x-data-grid';
import { useDemoData } from '@mui/x-data-grid-generator';

const VISIBLE_FIELDS = ['name', 'rating', 'country', 'dateCreated', 'isAdmin'];

const createFilterModelStore = () => {
  let listeners: Array<() => void> = [];
  const lsKey = 'gridFilterModel';
  const emptyModel = 'null';

  return {
    subscribe: (callback: () => void) => {
      listeners.push(callback);
      return () => {
        listeners = listeners.filter((listener) => listener !== callback);
      };
    },
    getSnapshot: () => {
      try {
        return localStorage.getItem(lsKey) || emptyModel;
      } catch (error) {
        return emptyModel;
      }
    },

    getServerSnapshot: () => {
      return emptyModel;
    },

    update: (filterModel: GridFilterModel) => {
      localStorage.setItem(lsKey, JSON.stringify(filterModel));
      listeners.forEach((listener) => listener());
    },
  };
};

const usePersistedFilterModel = () => {
  const [filterModelStore] = React.useState(createFilterModelStore);

  const filterModelString = React.useSyncExternalStore(
    filterModelStore.subscribe,
    filterModelStore.getSnapshot,
    filterModelStore.getServerSnapshot,
  );

  const filterModel = React.useMemo(() => {
    try {
      return (JSON.parse(filterModelString) as GridFilterModel) || undefined;
    } catch (error) {
      return undefined;
    }
  }, [filterModelString]);

  return React.useMemo(
    () => [filterModel, filterModelStore.update] as const,
    [filterModel, filterModelStore.update],
  );
};

export default function FilteringLocalStorage() {
  const { data, loading } = useDemoData({
    dataSet: 'Employee',
    visibleFields: VISIBLE_FIELDS,
    rowLength: 100,
  });

  const [filterModel, setFilterModel] = usePersistedFilterModel();

  const onFilterModelChange = React.useCallback<
    NonNullable<DataGridProps['onFilterModelChange']>
  >(
    (newFilterModel) => {
      setFilterModel(newFilterModel);
    },
    [setFilterModel],
  );

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        {...data}
        loading={loading}
        showToolbar
        filterModel={filterModel}
        onFilterModelChange={onFilterModelChange}
      />
    </div>
  );
}

```

## Save and manage filters from the panel

Create a custom filter panel by wrapping the `GridFilterPanel` component and pass it to the `slots.filterPanel` prop.

In the demo below, the custom component lets users to save and manage filters, which are stored in local storage.
For a more scalable approach, you can replace local storage with a server-side database.

```tsx
import * as React from 'react';
import {
  DataGridPro,
  GridFilterModel,
  gridFilterModelSelector,
  GridFilterPanel,
  useGridApiContext,
  useGridSelector,
} from '@mui/x-data-grid-pro';
import { useDemoData } from '@mui/x-data-grid-generator';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import DialogActions from '@mui/material/DialogActions';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import Typography from '@mui/material/Typography';
import Alert from '@mui/material/Alert';
import Stack from '@mui/material/Stack';
import Tooltip from '@mui/material/Tooltip';
import Divider from '@mui/material/Divider';
import SaveIcon from '@mui/icons-material/Save';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';

interface FilterPreset {
  id: string;
  name: string;
  filterModel: GridFilterModel;
  createdAt: string;
}

interface FilterPresetStore {
  presets: FilterPreset[];
  activePresetId: string | null;
}

const STORAGE_KEY = 'dataGridFilterPresets';
const EMPTY_STORE: FilterPresetStore = { presets: [], activePresetId: null };

const createPresetsStore = () => {
  let listeners: Array<() => void> = [];

  return {
    subscribe: (callback: () => void) => {
      listeners.push(callback);
      return () => {
        listeners = listeners.filter((listener) => listener !== callback);
      };
    },
    getSnapshot: () => {
      try {
        const saved = localStorage.getItem(STORAGE_KEY);
        return saved || JSON.stringify(EMPTY_STORE);
      } catch {
        return JSON.stringify(EMPTY_STORE);
      }
    },
    getServerSnapshot: () => {
      return JSON.stringify(EMPTY_STORE);
    },
    update: (store: FilterPresetStore) => {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(store));
      } catch {
        // Silently fail if localStorage is not available
      }
      listeners.forEach((listener) => listener());
    },
  };
};

const usePersistedPresets = () => {
  const [presetsStore] = React.useState(createPresetsStore);

  const storeString = React.useSyncExternalStore(
    presetsStore.subscribe,
    presetsStore.getSnapshot,
    presetsStore.getServerSnapshot,
  );

  const store = React.useMemo(() => {
    try {
      return JSON.parse(storeString) as FilterPresetStore;
    } catch {
      return EMPTY_STORE;
    }
  }, [storeString]);

  return React.useMemo(
    () => [store, presetsStore.update] as const,
    [store, presetsStore.update],
  );
};

type GridFilterPanelProps = React.ComponentProps<typeof GridFilterPanel>;

function CustomFilterPanel(props: GridFilterPanelProps) {
  const apiRef = useGridApiContext();
  const [store, setStore] = usePersistedPresets();
  const [createFilterDialogOpen, setCreateFilterDialogOpen] = React.useState(false);
  const [createFilterName, setCreateFilterName] = React.useState('');

  const filterModel = useGridSelector(apiRef, gridFilterModelSelector);
  const hasActiveFilters = filterModel.items.length > 0;

  const handleSavePreset = () => {
    setStore({
      ...store,
      presets: store.presets.map((p) =>
        p.id === store.activePresetId
          ? {
              ...p,
              filterModel,
            }
          : p,
      ),
    });
  };

  const handleCreateFilter = () => {
    if (!createFilterName.trim()) {
      return;
    }

    const newPreset: FilterPreset = {
      id: `preset_${Date.now()}`,
      name: createFilterName.trim(),
      filterModel,
      createdAt: new Date().toISOString(),
    };

    setStore({
      ...store,
      presets: [...store.presets, newPreset],
      activePresetId: newPreset.id,
    });

    setCreateFilterDialogOpen(false);
    setCreateFilterName('');
  };

  const handleLoadPreset = (presetId: string) => {
    const preset = store.presets.find((p) => p.id === presetId);
    if (preset) {
      apiRef.current.setFilterModel(preset.filterModel);

      setStore({
        ...store,
        activePresetId: presetId,
      });
    }
  };

  const handleDeletePreset = (presetId: string) => {
    setStore({
      ...store,
      presets: store.presets.filter((p) => p.id !== presetId),
      activePresetId:
        store.activePresetId === presetId ? null : store.activePresetId,
    });
  };

  return (
    <React.Fragment>
      <Box
        sx={{
          minWidth: 256,
          display: 'flex',
          flexDirection: 'column',
          'div:has(&)': { flexWrap: 'wrap' },
        }}
      >
        <Box
          sx={{
            p: 2,
            pb: 1,
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}
        >
          <Typography variant="subtitle2" sx={{ fontWeight: 'bold' }}>
            Saved Filter Presets
          </Typography>
          <Stack direction="row" spacing={0.5}>
            <Tooltip title="Create new filter">
              <IconButton
                onClick={() => setCreateFilterDialogOpen(true)}
                size="small"
                color="primary"
              >
                <AddIcon fontSize="small" />
              </IconButton>
            </Tooltip>
            <Tooltip title="Update selected filter">
              <span>
                <IconButton
                  onClick={handleSavePreset}
                  disabled={!store.activePresetId}
                  size="small"
                  color="primary"
                >
                  <SaveIcon fontSize="small" />
                </IconButton>
              </span>
            </Tooltip>
          </Stack>
        </Box>

        {store.presets.length === 0 ? (
          <Box sx={{ p: 2, pt: 0, flexGrow: 1, display: 'flex' }}>
            <Box
              sx={(theme) => ({
                flex: 1,
                border: '1px solid',
                borderColor: 'divider',
                borderRadius: 1,
                bgcolor: 'grey.100',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                p: 2,
                color: 'text.secondary',
                ...theme.applyStyles('dark', {
                  bgcolor: 'grey.900',
                }),
              })}
            >
              <Typography variant="body2" align="center">
                No saved filters yet
              </Typography>
            </Box>
          </Box>
        ) : (
          <List dense sx={{ pt: 0 }}>
            {store.presets.map((preset) => (
              <ListItem
                key={preset.id}
                disablePadding
                secondaryAction={
                  <IconButton
                    edge="end"
                    size="small"
                    onClick={(event) => {
                      event.stopPropagation();
                      handleDeletePreset(preset.id);
                    }}
                  >
                    <DeleteIcon fontSize="small" />
                  </IconButton>
                }
              >
                <ListItemButton
                  selected={preset.id === store.activePresetId}
                  onClick={() => handleLoadPreset(preset.id)}
                  sx={{
                    '&.Mui-selected': {
                      bgcolor: 'action.selected',
                      position: 'relative',
                      '&::after': {
                        content: '""',
                        position: 'absolute',
                        right: 0,
                        top: '50%',
                        transform: 'translateY(-50%)',
                        width: 3,
                        height: '60%',
                        bgcolor: 'primary.main',
                        borderRadius: '3px 0 0 3px',
                      },
                    },
                  }}
                >
                  <ListItemText
                    primary={preset.name}
                    secondary={
                      <Typography variant="caption" color="text.secondary">
                        {preset.filterModel.items.length} filter
                        {preset.filterModel.items.length > 1 ? 's' : ''}
                      </Typography>
                    }
                  />
                </ListItemButton>
              </ListItem>
            ))}
          </List>
        )}
      </Box>

      <Divider orientation="vertical" sx={{ height: 'auto' }} />

      <GridFilterPanel {...props} />

      <Dialog
        open={createFilterDialogOpen}
        onClose={() => setCreateFilterDialogOpen(false)}
        maxWidth="sm"
      >
        <DialogTitle>Create new filter</DialogTitle>
        <DialogContent>
          <Stack spacing={2} sx={{ mt: 1 }}>
            <TextField
              autoFocus
              label="Filter Name"
              value={createFilterName}
              onChange={(event) => setCreateFilterName(event.target.value)}
              fullWidth
              required
            />
            <Alert severity="info">
              {hasActiveFilters
                ? `This will save the current ${filterModel.items.length} active filter${filterModel.items.length !== 1 ? 's' : ''} as a new preset.`
                : 'This will create an empty filter preset that you can configure later.'}
            </Alert>
          </Stack>
        </DialogContent>
        <DialogActions>
          <Button
            variant="outlined"
            onClick={() => setCreateFilterDialogOpen(false)}
          >
            Cancel
          </Button>
          <Button
            onClick={handleCreateFilter}
            variant="contained"
            disabled={!createFilterName.trim()}
            startIcon={<AddIcon />}
          >
            Create Filter
          </Button>
        </DialogActions>
      </Dialog>
    </React.Fragment>
  );
}

export default function FilterPresetsPanel() {
  const { data, loading } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 100,
    maxColumns: 10,
  });

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <DataGridPro
        {...data}
        loading={loading}
        slots={{
          filterPanel: CustomFilterPanel,
        }}
        showToolbar
      />
    </Box>
  );
}

```

## Quick filter outside of the grid

The [Quick Filter](/x/react-data-grid/filtering/quick-filter/) component is typically used in the Data Grid's Toolbar component slot.

Some use cases may call for placing components like the Quick Filter outside of the Grid.
This requires certain considerations due to the Grid's context structure.
The following example shows how to accomplish this:

```tsx
import * as React from 'react';
import Portal from '@mui/material/Portal';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import {
  DataGrid,
  GridPortalWrapper,
  QuickFilter,
  QuickFilterClear,
  QuickFilterControl,
  ToolbarButton,
  ColumnsPanelTrigger,
  FilterPanelTrigger,
  Toolbar,
} from '@mui/x-data-grid';
import { useDemoData } from '@mui/x-data-grid-generator';
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';
import SearchIcon from '@mui/icons-material/Search';
import CancelIcon from '@mui/icons-material/Cancel';
import Tooltip from '@mui/material/Tooltip';
import Badge from '@mui/material/Badge';
import FilterListIcon from '@mui/icons-material/FilterList';
import ViewColumnIcon from '@mui/icons-material/ViewColumn';

function MyCustomToolbar() {
  return (
    <React.Fragment>
      <Portal container={() => document.getElementById('filter-panel')!}>
        <GridPortalWrapper>
          <QuickFilter expanded>
            <QuickFilterControl
              render={({ ref, ...other }) => (
                <TextField
                  {...other}
                  sx={{ width: 260 }}
                  inputRef={ref}
                  aria-label="Search"
                  placeholder="Search..."
                  size="small"
                  slotProps={{
                    input: {
                      startAdornment: (
                        <InputAdornment position="start">
                          <SearchIcon fontSize="small" />
                        </InputAdornment>
                      ),
                      endAdornment: other.value ? (
                        <InputAdornment position="end">
                          <QuickFilterClear
                            edge="end"
                            size="small"
                            aria-label="Clear search"
                            material={{ sx: { marginRight: -0.75 } }}
                          >
                            <CancelIcon fontSize="small" />
                          </QuickFilterClear>
                        </InputAdornment>
                      ) : null,
                    },
                  }}
                />
              )}
            />
          </QuickFilter>
        </GridPortalWrapper>
      </Portal>

      <Toolbar>
        <Tooltip title="Columns">
          <ColumnsPanelTrigger render={<ToolbarButton />}>
            <ViewColumnIcon fontSize="small" />
          </ColumnsPanelTrigger>
        </Tooltip>

        <Tooltip title="Filters">
          <FilterPanelTrigger
            render={(triggerProps, state) => (
              <ToolbarButton {...triggerProps} color="default">
                <Badge
                  badgeContent={state.filterCount}
                  color="primary"
                  variant="dot"
                >
                  <FilterListIcon fontSize="small" />
                </Badge>
              </ToolbarButton>
            )}
          />
        </Tooltip>
      </Toolbar>
    </React.Fragment>
  );
}

const VISIBLE_FIELDS = ['name', 'rating', 'country', 'dateCreated', 'isAdmin'];

export default function QuickFilterOutsideOfGrid() {
  const { data, loading } = useDemoData({
    dataSet: 'Employee',
    rowLength: 1000,
  });

  // Otherwise filter will be applied on fields such as the hidden column id
  const columns = React.useMemo(
    () => data.columns.filter((column) => VISIBLE_FIELDS.includes(column.field)),
    [data.columns],
  );

  return (
    <Grid container spacing={2}>
      <Grid>
        <Box id="filter-panel" />
      </Grid>
      <Grid style={{ height: 400, width: '100%' }}>
        <DataGrid
          {...data}
          loading={loading}
          columns={columns}
          slots={{
            toolbar: MyCustomToolbar,
          }}
          slotProps={{
            toolbar: {
              showQuickFilter: false,
            },
          }}
          showToolbar
          initialState={{
            filter: {
              filterModel: {
                items: [],
                quickFilterExcludeHiddenColumns: true,
              },
            },
          }}
        />
      </Grid>
    </Grid>
  );
}

```

## Calculating filtered rows in advance

The [Grid API](/x/react-data-grid/api-object/#how-to-use-the-api-object) provides the [`getFilterState`](/x/api/data-grid/grid-api/#grid-api-prop-getFilterState) method, which lets you display the row count for predefined filters upfront without applying filters to the Data Grid:

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGridPro, useGridApiRef, GridFilterModel } from '@mui/x-data-grid-pro';
import { useDemoData } from '@mui/x-data-grid-generator';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

const predefinedFilters: { label: string; filterModel: GridFilterModel }[] = [
  {
    label: 'All',
    filterModel: { items: [] },
  },
  {
    label: 'Filled',
    filterModel: { items: [{ field: 'status', operator: 'is', value: 'Filled' }] },
  },
  {
    label: 'Open',
    filterModel: { items: [{ field: 'status', operator: 'is', value: 'Open' }] },
  },
  {
    label: 'Rejected',
    filterModel: { items: [{ field: 'status', operator: 'is', value: 'Rejected' }] },
  },
  {
    label: 'Partially Filled',
    filterModel: {
      items: [{ field: 'status', operator: 'is', value: 'PartiallyFilled' }],
    },
  },
];

export default function FilteredRowCount() {
  const { data, loading } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 1000,
    maxColumns: 10,
  });

  const apiRef = useGridApiRef();

  const [predefinedFiltersRowCount, setPredefinedFiltersRowCount] = React.useState<
    number[]
  >([]);

  const getFilteredRowsCount = React.useCallback(
    (filterModel: GridFilterModel) => {
      const rowIds = apiRef.current?.getAllRowIds();
      const filterState = apiRef.current?.getFilterState(filterModel);
      if (!rowIds || !filterState) {
        return 0;
      }

      const { filteredRowsLookup } = filterState;
      return rowIds.filter((rowId) => filteredRowsLookup[rowId] !== false).length;
    },
    [apiRef],
  );

  React.useEffect(() => {
    // Calculate the row count for predefined filters
    if (data.rows.length === 0) {
      return;
    }

    setPredefinedFiltersRowCount(
      predefinedFilters.map(({ filterModel }) => getFilteredRowsCount(filterModel)),
    );
  }, [apiRef, data.rows, getFilteredRowsCount]);

  return (
    <div style={{ overflow: 'hidden' }}>
      <Stack direction="row" gap={1} mb={1} flexWrap="wrap">
        {predefinedFilters.map(({ label, filterModel }, index) => {
          const count = predefinedFiltersRowCount[index];
          return (
            <Button
              key={label}
              onClick={() => apiRef.current?.setFilterModel(filterModel)}
              variant="outlined"
            >
              {label} {count !== undefined ? `(${count})` : ''}
            </Button>
          );
        })}
      </Stack>
      <Box sx={{ height: 520, width: '100%' }}>
        <DataGridPro {...data} loading={loading} apiRef={apiRef} />
      </Box>
    </div>
  );
}

```
