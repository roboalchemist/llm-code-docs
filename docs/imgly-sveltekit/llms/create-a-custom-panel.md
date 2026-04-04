# Create a Custom Panel

Create custom sidebar panels that integrate with CE.SDK’s user interface using the builder system and built-in components.

![Create Custom Panel](/docs/cesdk/_astro/browser.hero.BcYkmxGO_Z21ssvN.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-ui-extensions-create-custom-panel-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-ui-extensions-create-custom-panel-browser)

Custom panels extend CE.SDK by adding sidebar interfaces that match the editor’s design language. The builder system provides pre-built components for forms, buttons, and media display, allowing you to create rich editing experiences without building UI from scratch.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';
export default class CreateCustomPanelExample implements EditorPlugin {  name = 'CreateCustomPanelExample';  version = '1.0.0';
  async initialize(context: EditorPluginContext) {    const { cesdk } = context;    if (!cesdk) return;
    await cesdk.createDesignScene();
    cesdk.i18n.setTranslations({      en: { 'panel.my-settings': 'My Settings Panel' }    });
    cesdk.ui.registerPanel('my-settings', ({ builder, engine, state }) => {
      const textState = state('text', 'Hello CE.SDK');      const opacityState = state('opacity', 100);
      builder.Section('settings', {        title: 'Settings',        children: () => {
          builder.TextInput('name', {            inputLabel: 'Name',            ...textState          });
          builder.Slider('opacity', {            inputLabel: 'Opacity',            min: 0,            max: 100,            ...opacityState          });
          builder.Checkbox('enabled', {            inputLabel: 'Enable feature',            value: true,            setValue: () => {}          });
          builder.Button('apply', {            label: 'Apply',            onClick: () => {
              const page = engine.block.findByType('page')[0];              engine.block.setOpacity(page, opacityState.value / 100);            }          });
          const selected = engine.block.findAllSelected();          if (selected.length > 0) {            builder.Text('info', { content: `${selected.length} selected` });          }        }      });    });
    cesdk.ui.registerComponent('settings-btn', ({ builder }) => {      builder.Button('toggle', {        label: 'Settings',        icon: '@imgly/Settings',        isActive: cesdk.ui.isPanelOpen('my-settings'),        onClick: () => cesdk.ui.openPanel('my-settings')      });    });
    cesdk.ui.setDockOrder([...cesdk.ui.getDockOrder(), 'settings-btn']);
    cesdk.ui.openPanel('my-settings');  }}
```

This guide covers how to register panels, use builder components, manage local state, respond to engine changes, set panel titles, and integrate panels with the dock.

## Registering a Custom Panel[#](#registering-a-custom-panel)

Register a panel using `cesdk.ui.registerPanel()` with a unique ID and a render function. The render function receives `builder`, `engine`, and `state` as arguments.

```
cesdk.ui.registerPanel('my-settings', ({ builder, engine, state }) => {
```

The panel renders whenever the function is called. CE.SDK tracks engine method calls within the render function and re-invokes it when relevant state changes.

## Managing Local State[#](#managing-local-state)

Use the `state` function to create panel-local state that persists across re-renders. Call `state('key', defaultValue)` to get `value` and `setValue` properties.

```
const textState = state('text', 'Hello CE.SDK');const opacityState = state('opacity', 100);
```

State objects integrate directly with input components by spreading the object into the component props.

## Structuring with Sections[#](#structuring-with-sections)

Group related components using `builder.Section()`. Sections accept a title and a children function containing nested components.

```
builder.Section('settings', {  title: 'Settings',  children: () => {
```

Sections provide visual organization and collapsible areas within your panel.

## Using Input Components[#](#using-input-components)

### Text Input[#](#text-input)

Capture text with `builder.TextInput()`. Bind to state using the value and setValue properties.

```
builder.TextInput('name', {  inputLabel: 'Name',  ...textState});
```

### Slider[#](#slider)

Handle numeric ranges with `builder.Slider()`. Configure min, max, and step values.

```
builder.Slider('opacity', {  inputLabel: 'Opacity',  min: 0,  max: 100,  ...opacityState});
```

### Checkbox[#](#checkbox)

Toggle boolean values with `builder.Checkbox()`.

```
builder.Checkbox('enabled', {  inputLabel: 'Enable feature',  value: true,  setValue: () => {}});
```

## Adding Buttons[#](#adding-buttons)

Add interactive buttons with `builder.Button()`. Configure the label, icon, and onClick handler.

```
builder.Button('apply', {  label: 'Apply',  onClick: () => {
```

## Accessing Engine State[#](#accessing-engine-state)

Access engine state within the render function to create reactive panels. The panel re-renders when tracked engine state changes.

```
const selected = engine.block.findAllSelected();if (selected.length > 0) {  builder.Text('info', { content: `${selected.length} selected` });}
```

## Modifying Engine State[#](#modifying-engine-state)

Use engine APIs within event handlers to modify the scene based on panel input.

```
const page = engine.block.findByType('page')[0];engine.block.setOpacity(page, opacityState.value / 100);
```

## Setting the Panel Title[#](#setting-the-panel-title)

Set panel titles through i18n translations. The translation key follows the pattern `panel.[panelId]`.

```
cesdk.i18n.setTranslations({  en: { 'panel.my-settings': 'My Settings Panel' }});
```

## Adding a Dock Button[#](#adding-a-dock-button)

Register a component that renders a button to toggle your panel. Use `cesdk.ui.isPanelOpen()` to track state.

```
cesdk.ui.registerComponent('settings-btn', ({ builder }) => {  builder.Button('toggle', {    label: 'Settings',    icon: '@imgly/Settings',    isActive: cesdk.ui.isPanelOpen('my-settings'),    onClick: () => cesdk.ui.openPanel('my-settings')  });});
```

Add the component to the dock order.

```
cesdk.ui.setDockOrder([...cesdk.ui.getDockOrder(), 'settings-btn']);
```

## Opening the Panel[#](#opening-the-panel)

Open your custom panel programmatically using `cesdk.ui.openPanel()`.

```
cesdk.ui.openPanel('my-settings');
```

To learn how to manage panel lifecycle and positioning, see [Panel](sveltekit/user-interface/customization/panel-7ce1ee/) .

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `cesdk.ui.registerPanel(id, renderFn)` | Registers a panel with a unique ID and render function. The render function receives `builder`, `engine`, and `state`. |
| `cesdk.ui.openPanel(id)` | Opens a registered panel by ID. |
| `cesdk.ui.isPanelOpen(id)` | Returns `true` if the panel is currently open. |
| `state(key, defaultValue)` | Creates panel-local state. Returns `{ value, setValue }` for use with input components. |
| `cesdk.i18n.setTranslations(translations)` | Sets translation strings. Use key `panel.[panelId]` for panel titles. |

## Next Steps[#](#next-steps)

[Register New Component](sveltekit/user-interface/ui-extensions/register-new-component-b04a04/) — Create reusable custom components for use across panels.

[Customize UI Behavior](sveltekit/user-interface/ui-extensions/customize-behaviour-c09cb2/) — Control UI programmatically with events and notifications.

[Add New Button](sveltekit/user-interface/ui-extensions/add-new-button-74884d/) — Add buttons to dock, inspector bar, and other UI areas.

[Dock](sveltekit/user-interface/customization/dock-cb916c/) — Configure the editor dock area and component ordering.

---



[Source](https:/img.ly/docs/cesdk/sveltekit/user-interface/ui-extensions/asset-library-f2c082)