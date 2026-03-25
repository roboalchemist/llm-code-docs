# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/Pointers.md

# [Pointers](https://bryntum.com/docs/gantt/api/Core/helper/util/Pointers)

This class tracks active [pointers](https://bryntum.com/docs/gantt/api/#Core/helper/util/Pointers#typedef-Pointer) involved in the [Pointer Events](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events) API.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[active](https://bryntum.com/docs/gantt/api/Core/helper/util/Pointers#property-active)
An array of [Pointer](https://bryntum.com/docs/gantt/api/#Core/helper/util/Pointers#typedef-Pointer) objects, in order of first-started to last-started.

[current](https://bryntum.com/docs/gantt/api/Core/helper/util/Pointers#property-current)
The most recently active [Pointer](https://bryntum.com/docs/gantt/api/#Core/helper/util/Pointers#typedef-Pointer) object.

[primary](https://bryntum.com/docs/gantt/api/Core/helper/util/Pointers#property-primary)
The primary [Pointer](https://bryntum.com/docs/gantt/api/#Core/helper/util/Pointers#typedef-Pointer).

[secondary](https://bryntum.com/docs/gantt/api/Core/helper/util/Pointers#property-secondary)
The secondary [Pointer](https://bryntum.com/docs/gantt/api/#Core/helper/util/Pointers#typedef-Pointer).

## Typedefs

Typedefs are type definitions for the class

[Pointer](https://bryntum.com/docs/gantt/api/Core/helper/util/Pointers#typedef-Pointer)
Readonly object describing an active pointer's current state.
