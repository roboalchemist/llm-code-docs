# Source: https://docs.flux.ai/reference/pcb-object-types.md

# PCB Object Types

The PCB layout editor workspace is organized as a tree and each object in that tree is of a specific type that defines its function.

> These object types can be used as part of the selector in [Selector-Based Layout Rules](https://docs.flux.ai/flux/reference/pcb-layout-rule-selectors).

## Object Types

### Top level

| **Syntax** | **Meaning** | **What it selects** | 
| ---- | ---- | ---- | 
| `root` | The topmost level of the tree | The root object | 
| `layout` | Defines a PCB board | Any layout object | 
| `element` | Defines a component and is linked to its equivalent in the Schematic | Any sub-layouts that have a corresponding schematic element. Please note that there is one special case: `pad` could also be an `element` because it could be associated with a _Terminal_ | 


### Containers

Essentially folders which contain other object types. Either created and managed by the system or by the user.

| **Syntax** | **Meaning** | **What it selects** | 
| ---- | ---- | ---- | 
| `container` | A system-specific object type that helps organize the tree in the app. It cannot be altered by the user | Any system object, such as the "Components" or "Nets" containers | 
| `group` | Similar to the `container` type but is instead user defined | Any group object | 
| `footprint` | Defines the actual footprint of a component | Any footprint object | 
| `model` | Used to represent 2D or 3D models | Any 2D/3D models | 
| `net` | A system-specific object type similar to `container` which organizes related `trace` objects into one place. | Any Net object. Since a `net` object is also a system object, it also will be selected by the `container` selector. | 


### Copper

Bundled objects which typically contain copper and/or drill holes.

| **Syntax** | **Meaning** | **What it selects** | 
| ---- | ---- | ---- | 
| `pad` | Defines a PCB pad | Any pad object | 
| `via` | Defines a PCB via | Any via object | 
| `trace` | Defines a PCB trace | Any trace object | 
| `fill` | Defines a PCB fill | Any fill object | 


### Silk

Objects in this category get assigned to the Top or Bottom Silk layers.

| **Syntax** | **Meaning** | **What it selects** | 
| ---- | ---- | ---- | 
| `text` | Defines a PCB silk text | Any text object | 
| `line` | Defines a PCB silk line | Any line object | 
| `circle` | Defines a PCB silk circle | Any circle object | 
| `rectangle` | Defines a PCB silk rectangle | Any rectangle object | 


### Utility

Objects in this category provide additional utilities.

| **Syntax** | **Meaning** | **What it selects** | 
| ---- | ---- | ---- | 
| `zone` | Defines copper keep out zone | Any zone object | 
