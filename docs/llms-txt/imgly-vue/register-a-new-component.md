# Register a New Component

Register custom UI components using CE.SDK’s builder system and place them in different areas of the editor interface like the navigation bar, inspector bar, dock, and canvas menu.

![Register New Component](/docs/cesdk/_astro/browser.hero.B9VmwL_R_ZfhEap.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-ui-extensions-register-new-component-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-ui-extensions-register-new-component-browser)

The builder system provides a declarative API for creating UI components that integrate with CE.SDK. Components registered via `cesdk.ui.registerComponent()` receive a render function that is automatically re-invoked when relevant engine state changes, enabling reactive UIs without manual subscription management. You can create buttons, dropdowns, inputs, and other UI elements that react to engine state changes.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';
const registerNewComponentPlugin: EditorPlugin = {  name: 'ly.img.registerNewComponentPlugin',  version: '1.0.0',
  async initialize({ cesdk, engine }: EditorPluginContext) {    if (cesdk == null) return;
    // Load a scene so the editor has content to display    await engine.scene.loadFromURL(      'https://cdn.img.ly/assets/demo/v3/ly.img.template/templates/cesdk_postcard_1.scene'    );
    // Register a custom button component that shows the selected block's type.    // The render function is automatically re-invoked when engine state changes.    cesdk.ui.registerComponent(      'com.example.blockTypeButton',      ({ builder, engine: eng, cesdk: cesdkInstance }) => {        // Engine API calls are tracked. When the selection changes,        // the component re-renders automatically.        const selectedBlocks = eng.block.findAllSelected();        const selectedBlock =          selectedBlocks.length > 0 ? selectedBlocks[0] : null;        const blockType = selectedBlock          ? eng.block.getType(selectedBlock)          : null;        const label = blockType ? formatBlockType(blockType) : 'No Selection';
        builder.Button('block-type-display', {          label,          icon: '@imgly/icons/Info',          isDisabled: !selectedBlock,          onClick: () => {            const message = selectedBlock              ? `Selected block type: ${blockType}`              : 'No block selected';            cesdkInstance.ui.showNotification({ message, type: 'info' });          }        });      }    );
    // Register a component with a dropdown menu containing buttons.    // Dropdowns in the navigation bar support Button and Separator elements.    cesdk.ui.registerComponent(      'com.example.actionsDropdown',      ({ builder, engine: eng, cesdk: cesdkInstance }) => {        const selectedBlocks = eng.block.findAllSelected();        const selectedBlock =          selectedBlocks.length > 0 ? selectedBlocks[0] : null;
        builder.Dropdown('actions-dropdown', {          label: 'Actions',          icon: '@imgly/icons/Adjustments',          children: () => {            builder.Button('action-duplicate', {              label: 'Duplicate',              icon: '@imgly/icons/Duplicate',              variant: 'plain',              isDisabled: !selectedBlock,              onClick: () => {                if (selectedBlock) {                  eng.block.duplicate(selectedBlock);                  cesdkInstance.ui.showNotification({                    message: 'Block duplicated',                    type: 'info'                  });                }              }            });
            builder.Button('action-delete', {              label: 'Delete',              icon: '@imgly/icons/Trash',              variant: 'plain',              color: 'danger',              isDisabled: !selectedBlock,              onClick: () => {                if (selectedBlock) {                  eng.block.destroy(selectedBlock);                  cesdkInstance.ui.showNotification({                    message: 'Block deleted',                    type: 'info'                  });                }              }            });
            builder.Separator('action-separator');
            builder.Button('action-select-all', {              label: 'Select All',              icon: '@imgly/icons/SelectAll',              variant: 'plain',              onClick: () => {                const page = eng.scene.getCurrentPage();                if (page) {                  const children = eng.block.getChildren(page);                  children.forEach((child) =>                    eng.block.setSelected(child, true)                  );                }              }            });          }        });      }    );
    // Place the custom components in the navigation bar.    // Use setNavigationBarOrder to define the order of components.    cesdk.ui.setNavigationBarOrder([      'ly.img.save',      'com.example.blockTypeButton',      'com.example.actionsDropdown',      'ly.img.spacer',      'ly.img.undo',      'ly.img.redo',      'ly.img.zoom.navigationBar'    ]);  }};
// Helper function to format block type for displayfunction formatBlockType(blockType: string): string {  // Extract the last part of the block type (e.g., '//ly.img.ubq/graphic' -> 'Graphic')  const parts = blockType.split('/');  const typeName = parts[parts.length - 1];  return typeName.charAt(0).toUpperCase() + typeName.slice(1);}
export default registerNewComponentPlugin;
```

This guide demonstrates registering custom components including a button, dropdown menu, checkbox, and select control, then placing them in the navigation bar and inspector bar.

## Registering a Component[#](#registering-a-component)

Use `cesdk.ui.registerComponent()` to register a component with a unique ID and a render function. The render function receives `builder`, `engine`, `cesdk`, `state`, and `payload` parameters.

```
// Register a custom button component that shows the selected block's type.// The render function is automatically re-invoked when engine state changes.cesdk.ui.registerComponent(  'com.example.blockTypeButton',  ({ builder, engine: eng, cesdk: cesdkInstance }) => {    // Engine API calls are tracked. When the selection changes,    // the component re-renders automatically.    const selectedBlocks = eng.block.findAllSelected();    const selectedBlock =      selectedBlocks.length > 0 ? selectedBlocks[0] : null;    const blockType = selectedBlock      ? eng.block.getType(selectedBlock)      : null;    const label = blockType ? formatBlockType(blockType) : 'No Selection';
    builder.Button('block-type-display', {      label,      icon: '@imgly/icons/Info',      isDisabled: !selectedBlock,      onClick: () => {        const message = selectedBlock          ? `Selected block type: ${blockType}`          : 'No block selected';        cesdkInstance.ui.showNotification({ message, type: 'info' });      }    });  });
```

### Component ID Naming[#](#component-id-naming)

Use reverse domain notation for component IDs (e.g., `'com.example.myButton'`). This ensures uniqueness and avoids conflicts with built-in components.

### Render Function Signature[#](#render-function-signature)

The render function receives these parameters:

*   **builder**: Object providing methods to create UI elements
*   **engine**: The engine instance for accessing block and scene state
*   **cesdk**: The editor instance for UI operations like notifications
*   **state**: Function for managing local component state
*   **payload**: Optional data passed when adding the component to an order

## Engine Reactivity[#](#engine-reactivity)

Components automatically re-render when engine APIs called within the render function detect state changes. Engine method calls like `engine.block.findAllSelected()` are tracked, and only components that use changed engine state re-render.

In the example above, calling `eng.block.findAllSelected()` and `eng.block.getType()` inside the render function creates automatic subscriptions. When the selection changes, the component re-renders with updated values.

This reactive approach eliminates manual subscription management. The builder system handles all subscriptions internally.

## Using Builder Elements[#](#using-builder-elements)

The builder object provides methods to create UI elements within your component.

### Button[#](#button)

The `builder.Button()` method creates an interactive button. It accepts a unique ID and configuration options including `label`, `icon`, `onClick`, and state flags like `isDisabled`.

### Dropdown with Nested Content[#](#dropdown-with-nested-content)

Use `builder.Dropdown()` to create a dropdown menu with nested content. The `children` callback function lets you add buttons and separators inside the dropdown.

```
// Register a component with a dropdown menu containing buttons.// Dropdowns in the navigation bar support Button and Separator elements.cesdk.ui.registerComponent(  'com.example.actionsDropdown',  ({ builder, engine: eng, cesdk: cesdkInstance }) => {    const selectedBlocks = eng.block.findAllSelected();    const selectedBlock =      selectedBlocks.length > 0 ? selectedBlocks[0] : null;
    builder.Dropdown('actions-dropdown', {      label: 'Actions',      icon: '@imgly/icons/Adjustments',      children: () => {        builder.Button('action-duplicate', {          label: 'Duplicate',          icon: '@imgly/icons/Duplicate',          variant: 'plain',          isDisabled: !selectedBlock,          onClick: () => {            if (selectedBlock) {              eng.block.duplicate(selectedBlock);              cesdkInstance.ui.showNotification({                message: 'Block duplicated',                type: 'info'              });            }          }        });
        builder.Button('action-delete', {          label: 'Delete',          icon: '@imgly/icons/Trash',          variant: 'plain',          color: 'danger',          isDisabled: !selectedBlock,          onClick: () => {            if (selectedBlock) {              eng.block.destroy(selectedBlock);              cesdkInstance.ui.showNotification({                message: 'Block deleted',                type: 'info'              });            }          }        });
        builder.Separator('action-separator');
        builder.Button('action-select-all', {          label: 'Select All',          icon: '@imgly/icons/SelectAll',          variant: 'plain',          onClick: () => {            const page = eng.scene.getCurrentPage();            if (page) {              const children = eng.block.getChildren(page);              children.forEach((child) =>                eng.block.setSelected(child, true)              );            }          }        });      }    });  });
```

The dropdown receives the same configuration as buttons, but uses `children` instead of `onClick` to define the dropdown content.

### Available Builder Components[#](#available-builder-components)

Not every location supports every builder component yet. The following table shows the available builder components and their properties.

| Builder Component | Description | Properties |
| --- | --- | --- |
| `builder.Button` | A simple button to react on a user click. | **label**: The button label (supports i18n keys).  
**onClick**: Click handler.  
**variant**: `regular` (default) or `plain`.  
**color**: `accent` or `danger`.  
**icon**: The button icon.  
**trailingIcon**: Trailing icon.  
**isActive**: Active state indicator.  
**isSelected**: Selected state indicator.  
**isDisabled**: Disabled state.  
**isLoading**: Loading state.  
**loadingProgress**: Progress value 0-1.  
**tooltip**: Hover tooltip (supports i18n keys). |
| `builder.ButtonGroup` | Grouping of multiple buttons in a segmented control. | **children**: Function to render grouped buttons (only Button and Dropdown allowed). |
| `builder.Dropdown` | A button that opens a dropdown with content. | Same as Button, but with **children** instead of onClick for dropdown content. |
| `builder.Heading` | Renders text as a heading. | **content**: The heading text. |
| `builder.Separator` | Adds visual separation between entries. | No properties. Follows special layout rules for consecutive separators. |
| `builder.Component` | Renders another registered component. | **componentId**: The registered component ID.  
**payload**: Optional data passed to the component. |
| `builder.Checkbox` | Toggle checkbox control. | **value**: Current value.  
**setValue**: Change handler.  
**inputLabel**: Checkbox label. |
| `builder.Select` | Dropdown select with options. | **value**: Current selection object.  
**setValue**: Change handler.  
**values**: Array of option objects with `id`, `label`, and optional `icon`. |
| `builder.TextInput` | Text input field. | **value**: Current value.  
**setValue**: Change handler.  
**placeholder**: Placeholder text. |
| `builder.NumberInput` | Numeric input field. | **value**: Current value.  
**setValue**: Change handler.  
**min/max**: Range limits. |
| `builder.Slider` | Numeric range slider. | **value**: Current value.  
**setValue**: Change handler.  
**min/max/step**: Range configuration. |
| `builder.Section` | Container for grouping related controls. | **children**: Function to render section contents. |

## Managing Component State[#](#managing-component-state)

The `state` function provides local state management within components, similar to React’s `useState`.

```
const { value, setValue } = state('unique-id', defaultValue);
```

State persists across re-renders with the same ID. Calling `setValue()` triggers a component re-render. Since the returned object matches input component expectations, you can spread it directly into components.

```
cesdk.ui.registerComponent('counter', ({ builder, state }) => {  const { value, setValue } = state('counter', 0);
  builder.Button('counter-button', {    label: `${value} clicks`,    onClick: () => {      setValue(value + 1);    }  });});
```

## Placing Components in the Navigation Bar[#](#placing-components-in-the-navigation-bar)

Add components to the navigation bar using `cesdk.ui.setNavigationBarOrder()`. The navigation bar appears at the top of the editor.

```
// Place the custom components in the navigation bar.// Use setNavigationBarOrder to define the order of components.cesdk.ui.setNavigationBarOrder([  'ly.img.save',  'com.example.blockTypeButton',  'com.example.actionsDropdown',  'ly.img.spacer',  'ly.img.undo',  'ly.img.redo',  'ly.img.zoom.navigationBar']);
```

Use `cesdk.ui.insertNavigationBarOrderComponent()` to position components relative to existing ones without replacing the entire order.

## Placing Components in the Inspector Bar[#](#placing-components-in-the-inspector-bar)

The inspector bar appears at the bottom when a block is selected. Add components using `cesdk.ui.setInspectorBarOrder()` or position relative to existing components with `cesdk.ui.insertInspectorBarOrderComponent()`.

```
cesdk.ui.setInspectorBarOrder([  'com.example.myInspectorButton',  'ly.img.fill',  'ly.img.stroke']);
```

## Placing Components in the Dock[#](#placing-components-in-the-dock)

The dock is the vertical sidebar for asset libraries and tools. Add components using `cesdk.ui.setDockOrder()` or `cesdk.ui.insertDockOrderComponent()`.

```
cesdk.ui.insertDockOrderComponent(  { id: 'ly.img.assetLibrary.dock' },  'com.example.myDockButton',  'after');
```

## Placing Components in the Canvas Menu[#](#placing-components-in-the-canvas-menu)

The canvas menu appears as a floating menu near selected blocks. Add components using `cesdk.ui.setCanvasMenuOrder()` or `cesdk.ui.insertCanvasMenuOrderComponent()`.

```
cesdk.ui.setCanvasMenuOrder([  'ly.img.delete',  'com.example.myCanvasMenuAction',  'ly.img.duplicate']);
```

## Placing Components in the Canvas Bar[#](#placing-components-in-the-canvas-bar)

Canvas bars appear above or below the canvas area. Specify `'top'` or `'bottom'` position using `cesdk.ui.setCanvasBarOrder()` or `cesdk.ui.insertCanvasBarOrderComponent()`.

```
cesdk.ui.setCanvasBarOrder(['com.example.myCanvasBarButton'], 'top');
```

## Passing Payload Data[#](#passing-payload-data)

Components can receive contextual data through the `payload` parameter. Pass data when adding a component to an order using an object with `id` and additional properties.

```
cesdk.ui.registerComponent(  'myDockEntry.dock',  ({ builder: { Button }, payload }) => {    const { label } = payload;    Button('entry-button', { label });  });
cesdk.ui.setDockOrder([  {    id: 'myDockEntry.dock',    label: 'Custom Label'  }]);
```

Use TypeScript generics with `registerComponent<PayloadType>()` to type the payload parameter.

## Troubleshooting[#](#troubleshooting)

### Component Not Rendering[#](#component-not-rendering)

Verify the component ID matches between registration and placement in order arrays. Check that the registration happens before setting the order. Component IDs are case-sensitive.

### State Not Persisting[#](#state-not-persisting)

Ensure unique state IDs within the component. Duplicate IDs cause conflicts and unexpected behavior. Each `state()` call should use a distinct identifier.

### Component Not Updating[#](#component-not-updating)

Confirm engine API calls are made inside the render function, not outside. The reactor only tracks calls made during the render function execution. Moving engine calls outside breaks reactivity.

### Order Changes Not Applying[#](#order-changes-not-applying)

Check that the order method matches the UI location. Use `setDockOrder()` for the dock, `setNavigationBarOrder()` for navigation, and so on. Mismatched methods silently fail.

## API Reference[#](#api-reference)

| Method | Category | Purpose |
| --- | --- | --- |
| `cesdk.ui.registerComponent()` | Component Registration | Register a custom component with a unique ID and render function |
| `cesdk.ui.setNavigationBarOrder()` | UI Layout | Set the order of components in the navigation bar |
| `cesdk.ui.getNavigationBarOrder()` | UI Layout | Get the current navigation bar component order |
| `cesdk.ui.insertNavigationBarOrderComponent()` | UI Layout | Insert a component relative to an existing navigation bar component |
| `cesdk.ui.setInspectorBarOrder()` | UI Layout | Set the order of components in the inspector bar |
| `cesdk.ui.getInspectorBarOrder()` | UI Layout | Get the current inspector bar component order |
| `cesdk.ui.insertInspectorBarOrderComponent()` | UI Layout | Insert a component relative to an existing inspector bar component |
| `cesdk.ui.setDockOrder()` | UI Layout | Set the order of components in the dock |
| `cesdk.ui.getDockOrder()` | UI Layout | Get the current dock component order |
| `cesdk.ui.insertDockOrderComponent()` | UI Layout | Insert a component relative to an existing dock component |
| `cesdk.ui.setCanvasMenuOrder()` | UI Layout | Set the order of components in the canvas menu |
| `cesdk.ui.getCanvasMenuOrder()` | UI Layout | Get the current canvas menu component order |
| `cesdk.ui.insertCanvasMenuOrderComponent()` | UI Layout | Insert a component relative to an existing canvas menu component |
| `cesdk.ui.setCanvasBarOrder()` | UI Layout | Set the order of components in the canvas bar (top or bottom) |
| `cesdk.ui.getCanvasBarOrder()` | UI Layout | Get the current canvas bar component order |
| `cesdk.ui.insertCanvasBarOrderComponent()` | UI Layout | Insert a component relative to an existing canvas bar component |
| `builder.Button()` | Builder | Create an interactive button element |
| `builder.Dropdown()` | Builder | Create a dropdown menu with nested children |
| `builder.ButtonGroup()` | Builder | Create a group of related buttons |
| `builder.Checkbox()` | Builder | Create a toggle checkbox control |
| `builder.Select()` | Builder | Create a select dropdown with predefined options |
| `builder.TextInput()` | Builder | Create a text input field |
| `builder.NumberInput()` | Builder | Create a numeric input field |
| `builder.Slider()` | Builder | Create a numeric slider control |
| `builder.Section()` | Builder | Create a container for grouping controls |
| `builder.Separator()` | Builder | Create a visual divider |
| `builder.Heading()` | Builder | Create a heading text element |
| `builder.Component()` | Builder | Render another registered component with optional payload |
| `state()` | Component State | Access local state with get/set capabilities |

---



[Source](https:/img.ly/docs/cesdk/vue/user-interface/ui-extensions/quick-actions-1e478d)