# Source: https://vueflow.dev/guide/theming.md

---
url: /guide/theming.md
---

# Theming

Let's take a tour around the library styles, customization opportunities, and other features that Vue Flow offers out of
the box.

## Library Styles

Vue Flow values flexibility and allows you to take the lead when it comes to styling.
It showcases some obligatory stylings that must be imported, while leaving optional features, such as the default theme,
up to your preference.

To import the necessary and optional styles:

```css
/* these are necessary styles for vue flow */
@import '@vue-flow/core/dist/style.css';

/* this contains the default theme, these are optional styles */
@import '@vue-flow/core/dist/theme-default.css';
```

## Adjusting the Default Theme

The Vue Flow default theme functions as your baseline, which you can customize and decorate as per your liking using CSS
rules, style and class properties, and CSS variables.

### Styling with CSS Classes

Here's how you can use CSS classes to add a pop of color or alter the font style for the theme:

```css
/* Use a purple theme for our custom node */
.vue-flow__node-custom {
    background: purple;
    color: white;
    border: 1px solid purple;
    border-radius: 4px;
    box-shadow: 0 0 0 1px purple;
    padding: 8px;
}
```

### Using CSS Properties

You can also directly pass a style or class attribute to Vue Flow components and nodes/edges.

Below are a couple of examples on how you can do this:

Directly styling the Vue Flow component:

```vue{4-5}
<VueFlow
  :nodes="nodes"
  :edges="edges"
  class="my-diagram-class"  
  :style="{ background: 'red' }"
/>
```

Styling nodes/edges with a style or class attribute:

::: code-group

```js{8-12} [<LogosJavascript />]
/* Customizing node by assigning class and style properties */
const nodes = ref([
  { 
    id: '1', 
    position: { x: 250, y: 5 },
    data: { label: 'Node 1' },
    
    // Add a class name to the node
    class: 'my-custom-node-class',
    
    // You can pass an object containing CSSProperties or CSS variables
    style: { backgroundColor: 'green', width: '200px', height: '100px' },
  },
])
```

:::

### [Redefining Styles with CSS variables](/typedocs/type-aliases/CSSVars)

Some of the defined theme styles can be overwritten using CSS variables.
These alterations can be implemented either on a global scale or to individual elements.

::: code-group

```css
/* Global default CSS variable values */
:root {
    --vf-node-bg: #fff;
    --vf-node-text: #222;
    --vf-connection-path: #b1b1b7;
    --vf-handle: #555;
}
```

```js{6-7} [<LogosJavascript />]
const nodes = ref([
  { 
    id: '1', 
    position: { x: 100, y: 100 }, 
    data: { label: 'Node 1' },
    /* Overriding the `--vf-node-color` variable to change node border, box-shadow and handle color */
    style: { '--vf-node-color': 'blue' } 
  },
])
```

:::

## CSS Variables

Here's a concise list of CSS variables you can consider, along with their effects:

| Variable             | Effect                                             |
|----------------------|----------------------------------------------------|
| --vf-node-color      | Defines node border, box-shadow, and handle colors |
| --vf-box-shadow      | Defines color of node box-shadow                   |
| --vf-node-bg         | Defines node background color                      |
| --vf-node-text       | Defines node text color                            |
| --vf-handle          | Defines node handle color                          |
| --vf-connection-path | Defines connection line color                      |

## CSS Class Names

Here you'll find a handy reference guide of class names and their respective elements:

#### Containers

| Name                  | Container                                 |
| --------------------- | ----------------------------------------- |
| .vue-flow             | The outer container                       |
| .vue-flow\_\_container  | Wrapper for container elements            |
| .vue-flow\_\_viewport   | The inner container                       |
| .vue-flow\_\_background | Background component                      |
| .vue-flow\_\_minimap    | MiniMap component                         |
| .vue-flow\_\_controls   | Controls component                        |

#### Edges

| Name                      | Description                                       |
| ------------------------- | ------------------------------------------------- |
| .vue-flow\_\_edges          | Wrapper rendering edges                           |
| .vue-flow\_\_edge           | Wrapper around each edge element                  |
| .vue-flow\_\_selectionpane  | Pane for handling user selection                  |
| .vue-flow\_\_selection      | Defines current user selection box                |
| .vue-flow\_\_edge-{type}  | Edge type (either custom or default)              |
| .vue-flow\_\_edge.selected  | Defines the currently selected edge(s)            |
| .vue-flow\_\_edge.animated  | Defines an animated edge                          |
| .vue-flow\_\_edge-path      | SVG path for edge elements                        |
| .vue-flow\_\_edge-text      | Wrapper around edge label                         |
| .vue-flow\_\_edge-textbg    | Background wrapper around edge label              |
| .vue-flow\_\_connectionline | Container for the connection line elements        |
| .vue-flow\_\_connection     | Individual connection line element                |
| .vue-flow\_\_connection-path| SVG path for connection line                      |

#### Nodes

| Name                  | Description                               |
| --------------------- | ----------------------------------------- |
| .vue-flow\_\_nodes      | Rendering wrapper around nodes            |
| .vue-flow\_\_node       | Wrapper around each node element          |
| .vue-flow\_\_node.selected | Defines the currently selected node(s)  |
| .vue-flow\_\_node-{type}   | Node type (either custom or default)     |
| .vue-flow\_\_nodesselection | Defines selection rectangle for nodes   |

#### Node Handles

| Name                      | Description                               |
| ------------------------- | ----------------------------------------- |
| .vue-flow\_\_handle         | Wrapper around node handle elements       |
| .vue-flow\_\_handle-bottom  | Defines a handle at bottom                |
| .vue-flow\_\_handle-top     | Defines a handle at top                   |
| .vue-flow\_\_handle-left    | Defines a handle at left                  |
| .vue-flow\_\_handle-right   | Defines a handle at right                 |
| .vue-flow\_\_handle-connecting | Connection line is over the handle      |
| .vue-flow\_\_handle-valid      | Connection line over handle with valid connection |
