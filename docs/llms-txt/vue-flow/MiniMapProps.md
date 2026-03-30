# Source: https://vueflow.dev/typedocs/interfaces/MiniMapProps.md

---
url: /typedocs/interfaces/MiniMapProps.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: MiniMapProps

## Properties

### ariaLabel?

> `optional` **ariaLabel**: `null` | `string`

***

### height?

> `optional` **height**: `number`

***

### inversePan?

> `optional` **inversePan**: `boolean`

Enable inverse panning, i.e. drag minimap to move viewport in opposite direction

***

### maskBorderRadius?

> `optional` **maskBorderRadius**: `number`

Mask border radius

***

### maskColor?

> `optional` **maskColor**: `string`

Background color of minimap mask

***

### maskStrokeColor?

> `optional` **maskStrokeColor**: `string`

Border color of minimap mask

***

### maskStrokeWidth?

> `optional` **maskStrokeWidth**: `number`

Border width of minimap mask

***

### nodeBorderRadius?

> `optional` **nodeBorderRadius**: `number`

Node border radius

***

### nodeClassName?

> `optional` **nodeClassName**: `string` | [`MiniMapNodeFunc`](../type-aliases/MiniMapNodeFunc.md)

Additional node class name, can be either a string or a string func that receives the current node

***

### nodeColor?

> `optional` **nodeColor**: `string` | [`MiniMapNodeFunc`](../type-aliases/MiniMapNodeFunc.md)

Node color, can be either a string or a string func that receives the current node

***

### nodeStrokeColor?

> `optional` **nodeStrokeColor**: `string` | [`MiniMapNodeFunc`](../type-aliases/MiniMapNodeFunc.md)

Node stroke color, can be either a string or a string func that receives the current node

***

### nodeStrokeWidth?

> `optional` **nodeStrokeWidth**: `number`

Node stroke width

***

### offsetScale?

> `optional` **offsetScale**: `number`

Specify minimap scale

***

### pannable?

> `optional` **pannable**: `boolean`

Enable drag minimap to drag viewport

***

### position?

> `optional` **position**: `PanelPositionType` | `PanelPosition`

Position of the minimap [PanelPosition](../enumerations/PanelPosition.md)

***

### width?

> `optional` **width**: `number`

***

### zoomable?

> `optional` **zoomable**: `boolean`

Enable zoom minimap to zoom viewport

***

### zoomStep?

> `optional` **zoomStep**: `number`

Specify zoom step
