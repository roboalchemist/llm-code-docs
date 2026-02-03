# Source: https://mui.com/x/react-tree-view/rich-tree-view/items.md

# Source: https://mui.com/x/react-tree-view/simple-tree-view/items.md

---
productId: x-tree-view
title: Simple Tree View - Items
components: SimpleTreeView, TreeItem
packageName: '@mui/x-tree-view'
githubLabel: 'scope: tree view'
waiAria: https://www.w3.org/WAI/ARIA/apg/patterns/treeview/
---

# Simple Tree View - Items

Learn how to add simple data to the Tree View component.

## Basics

```jsx
import { SimpleTreeView } from '@mui/x-tree-view/SimpleTreeView';
import { TreeItem } from '@mui/x-tree-view/TreeItem';
```

`SimpleTreeView` receives its items directly as JSX children.

```tsx
import Box from '@mui/material/Box';
import { SimpleTreeView } from '@mui/x-tree-view/SimpleTreeView';
import { TreeItem } from '@mui/x-tree-view/TreeItem';

export default function BasicSimpleTreeView() {
  return (
    <Box sx={{ minHeight: 352, minWidth: 250 }}>
      <SimpleTreeView>
        <TreeItem itemId="grid" label="Data Grid">
          <TreeItem itemId="grid-community" label="@mui/x-data-grid" />
          <TreeItem itemId="grid-pro" label="@mui/x-data-grid-pro" />
          <TreeItem itemId="grid-premium" label="@mui/x-data-grid-premium" />
        </TreeItem>
        <TreeItem itemId="pickers" label="Date and Time Pickers">
          <TreeItem itemId="pickers-community" label="@mui/x-date-pickers" />
          <TreeItem itemId="pickers-pro" label="@mui/x-date-pickers-pro" />
        </TreeItem>
        <TreeItem itemId="charts" label="Charts">
          <TreeItem itemId="charts-community" label="@mui/x-charts" />
        </TreeItem>
        <TreeItem itemId="tree-view" label="Tree View">
          <TreeItem itemId="tree-view-community" label="@mui/x-tree-view" />
        </TreeItem>
      </SimpleTreeView>
    </Box>
  );
}

```

### Item identifier

Each `TreeItem` must have a unique `itemId`.
This is used internally to identify the item in various models and to track it across updates.

```tsx
<SimpleTreeView>
  <TreeItem itemId="item-unique-id" {...otherItemProps} />
</SimpleTreeView>
```

### Item label

You must pass a `label` prop to each `TreeItem`, as shown below:

```tsx
<SimpleTreeView>
  <TreeItem label="Item label" {...otherItemProps} />
</SimpleTreeView>
```

### Disabled items

Use the `disabled` prop on `TreeItem` to disable interaction and focus:

```tsx
import Box from '@mui/material/Box';
import { SimpleTreeView } from '@mui/x-tree-view/SimpleTreeView';
import { TreeItem } from '@mui/x-tree-view/TreeItem';

export default function DisabledJSXItem() {
  return (
    <Box sx={{ minHeight: 320, minWidth: 250 }}>
      <SimpleTreeView>
        <TreeItem itemId="grid" label="Data Grid">
          <TreeItem itemId="grid-community" label="@mui/x-data-grid" />
          <TreeItem itemId="grid-pro" label="@mui/x-data-grid-pro" />
          <TreeItem itemId="grid-premium" label="@mui/x-data-grid-premium" />
        </TreeItem>
        <TreeItem itemId="pickers" label="Date and Time Pickers">
          <TreeItem itemId="pickers-community" label="@mui/x-date-pickers" />
          <TreeItem itemId="pickers-pro" label="@mui/x-date-pickers-pro" />
        </TreeItem>
        <TreeItem itemId="charts" label="Charts">
          <TreeItem itemId="charts-community" label="@mui/x-charts" disabled />
        </TreeItem>
        <TreeItem itemId="tree-view" label="Tree View" disabled>
          <TreeItem itemId="tree-view-community" label="@mui/x-tree-view" />
        </TreeItem>
      </SimpleTreeView>
    </Box>
  );
}

```

#### Focusable disabled items

The demo below includes a switch that toggles the `disabledItemsFocusable` prop, which controls whether or not a disabled `TreeItem` can be focused.

When this prop is set to false:

- Disabled items will not receive focus when navigating with keyboard arrow keys—they next non-disabled item is focused instead.
- Typing the first character of a disabled item's label will not move the focus to it.
- Mouse or keyboard interactions will not expand or collapse disabled items.
- Mouse or keyboard interactions will not select disabled items.
- <kbd class="key">Shift</kbd> + arrow keys will skip disabled items, and the next non-disabled item will be selected instead.
- Programmatic focus will not focus disabled items.

When it's set to true:

- Disabled items will receive focus when navigating with keyboard arrow keys.
- Typing the first character of a disabled item's label will move focus to it.
- Mouse or keyboard interactions will not expand or collapse disabled items.
- Mouse or keyboard interactions will not select disabled items.
- <kbd class="key">Shift</kbd> + arrow keys will not skip disabled items, but the disabled item will not be selected.
- Programmatic focus will focus disabled items.

```tsx
import * as React from 'react';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Switch from '@mui/material/Switch';
import FormControlLabel from '@mui/material/FormControlLabel';
import { SimpleTreeView } from '@mui/x-tree-view/SimpleTreeView';
import { TreeItem } from '@mui/x-tree-view/TreeItem';

export default function DisabledItemsFocusable() {
  const [disabledItemsFocusable, setDisabledItemsFocusable] = React.useState(false);
  const handleToggle = (event: React.ChangeEvent<HTMLInputElement>) => {
    setDisabledItemsFocusable(event.target.checked);
  };

  return (
    <Stack spacing={2}>
      <FormControlLabel
        control={
          <Switch
            checked={disabledItemsFocusable}
            onChange={handleToggle}
            name="disabledItemsFocusable"
          />
        }
        label="Allow focusing disabled items"
      />
      <Box sx={{ minHeight: 352, minWidth: 250 }}>
        <SimpleTreeView disabledItemsFocusable={disabledItemsFocusable}>
          <TreeItem itemId="grid" label="Data Grid">
            <TreeItem itemId="grid-community" label="@mui/x-data-grid" />
            <TreeItem itemId="grid-pro" label="@mui/x-data-grid-pro" />
            <TreeItem itemId="grid-premium" label="@mui/x-data-grid-premium" />
          </TreeItem>
          <TreeItem itemId="pickers" label="Date and Time Pickers">
            <TreeItem itemId="pickers-community" label="@mui/x-date-pickers" />
            <TreeItem itemId="pickers-pro" label="@mui/x-date-pickers-pro" />
          </TreeItem>
          <TreeItem itemId="charts" label="Charts">
            <TreeItem itemId="charts-community" label="@mui/x-charts" disabled />
          </TreeItem>
          <TreeItem itemId="tree-view" label="Tree View" disabled>
            <TreeItem itemId="tree-view-community" label="@mui/x-tree-view" />
          </TreeItem>
        </SimpleTreeView>
      </Box>
    </Stack>
  );
}

```

## Track item clicks

Use the `onItemClick` prop to track the clicked item:

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import { SimpleTreeView } from '@mui/x-tree-view/SimpleTreeView';
import { TreeItem } from '@mui/x-tree-view/TreeItem';

export default function OnItemClick() {
  const [lastClickedItem, setLastClickedItem] = React.useState<string | null>(null);

  return (
    <Stack spacing={2}>
      <Typography>
        {lastClickedItem == null
          ? 'No item click recorded'
          : `Last clicked item: ${lastClickedItem}`}
      </Typography>
      <Box sx={{ minHeight: 352, minWidth: 300 }}>
        <SimpleTreeView onItemClick={(event, itemId) => setLastClickedItem(itemId)}>
          <TreeItem itemId="grid" label="Data Grid">
            <TreeItem itemId="grid-community" label="@mui/x-data-grid" />
            <TreeItem itemId="grid-pro" label="@mui/x-data-grid-pro" />
            <TreeItem itemId="grid-premium" label="@mui/x-data-grid-premium" />
          </TreeItem>
          <TreeItem itemId="pickers" label="Date and Time Pickers">
            <TreeItem itemId="pickers-community" label="@mui/x-date-pickers" />
            <TreeItem itemId="pickers-pro" label="@mui/x-date-pickers-pro" />
          </TreeItem>
          <TreeItem itemId="charts" label="Charts">
            <TreeItem itemId="charts-community" label="@mui/x-charts" />
          </TreeItem>
          <TreeItem itemId="tree-view" label="Tree View">
            <TreeItem itemId="tree-view-community" label="@mui/x-tree-view" />
          </TreeItem>
        </SimpleTreeView>
      </Box>
    </Stack>
  );
}

```

## Imperative API

To use the `apiRef` object, you need to initialize it using the `useSimpleTreeViewApiRef()` hook as follows:

```tsx
const apiRef = useSimpleTreeViewApiRef();

return <SimpleTreeView apiRef={apiRef} items={ITEMS} />;
```

When your component first renders, `apiRef.current` is `undefined`.
After the initial render, `apiRef` holds methods to interact imperatively with the Tree View.

### Get an item's DOM element by ID

Use the `getItemDOMElement()` API method to get an item's DOM element by its ID.

```ts
const itemElement = apiRef.current.getItemDOMElement(
  // The id of the item to get the DOM element of
  itemId,
);
```

```tsx
import * as React from 'react';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import { SimpleTreeView } from '@mui/x-tree-view/SimpleTreeView';
import { TreeItem } from '@mui/x-tree-view/TreeItem';
import { useSimpleTreeViewApiRef } from '@mui/x-tree-view/hooks';

export default function ApiMethodGetItemDOMElement() {
  const apiRef = useSimpleTreeViewApiRef();
  const handleScrollToChartsCommunity = (event: React.SyntheticEvent) => {
    apiRef.current!.focusItem(event, 'charts-community');
    apiRef
      .current!.getItemDOMElement('charts-community')
      ?.scrollIntoView({ block: 'nearest' });
  };

  return (
    <Stack spacing={2}>
      <div>
        <Button onClick={handleScrollToChartsCommunity}>
          Focus and scroll to charts community item
        </Button>
      </div>
      <Box sx={{ height: 200, minWidth: 250, overflowY: 'scroll' }}>
        <SimpleTreeView
          apiRef={apiRef}
          defaultExpandedItems={['grid', 'pickers', 'charts', 'tree-view']}
        >
          <TreeItem itemId="grid" label="Data Grid">
            <TreeItem itemId="grid-community" label="@mui/x-data-grid" />
            <TreeItem itemId="grid-pro" label="@mui/x-data-grid-pro" />
            <TreeItem itemId="grid-premium" label="@mui/x-data-grid-premium" />
          </TreeItem>
          <TreeItem itemId="pickers" label="Date and Time Pickers">
            <TreeItem itemId="pickers-community" label="@mui/x-date-pickers" />
            <TreeItem itemId="pickers-pro" label="@mui/x-date-pickers-pro" />
          </TreeItem>
          <TreeItem itemId="charts" label="Charts">
            <TreeItem itemId="charts-community" label="@mui/x-charts" />
          </TreeItem>
          <TreeItem itemId="tree-view" label="Tree View">
            <TreeItem itemId="tree-view-community" label="@mui/x-tree-view" />
          </TreeItem>
        </SimpleTreeView>
      </Box>
    </Stack>
  );
}

```
