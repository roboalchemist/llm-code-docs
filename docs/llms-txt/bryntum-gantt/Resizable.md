# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/mixin/Resizable.md

# [Resizable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Resizable)

Mixin making popups resizable via the [resizable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Resizable#config-resizable) config.

Example usage:

```
// Resizable with default handles (all edges/corners)
const myPopup = new Popup({
  resizable : true
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[resizable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Resizable#config-resizable)
Configure this property to allow the widget/component to be resized. Pressing Shift while resizing will constrain the aspect ratio.

* **`false`** (the default) disables resizing entirely.
* **`true`** enables resizing on all edges and corners.
* An **Object** allows fine-grained control, for example specifying which edges or corners have handles.

Example usage:

```
// Resizable with default handles (all edges/corners)
new SomePopup({
  resizable : true
});

// Resizable with only start and bottom edges active
new SomePopup({
  resizable : {
    handles : {
      top    : false,
      end    : false,
      bottom : true,
      start  : true,
      // corners also available: topStart, topEnd, bottomStart, bottomEnd
      // all omitted properties default to `true` if unspecified
    }
  }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResizable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Resizable#property-isResizable)
Identifies an object as an instance of [Resizable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Resizable) class, or subclass thereof.

[isResizable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Resizable#property-isResizable-static)
Identifies an object as an instance of [Resizable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Resizable) class, or subclass thereof.

[resizable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Resizable#property-resizable)
Configure this property to allow the widget/component to be resized. Pressing Shift while resizing will constrain the aspect ratio.

* **`false`** (the default) disables resizing entirely.
* **`true`** enables resizing on all edges and corners.
* An **Object** allows fine-grained control, for example specifying which edges or corners have handles.

Example usage:

```
// Resizable with default handles (all edges/corners)
new SomePopup({
  resizable : true
});

// Resizable with only start and bottom edges active
new SomePopup({
  resizable : {
    handles : {
      top    : false,
      end    : false,
      bottom : true,
      start  : true,
      // corners also available: topStart, topEnd, bottomStart, bottomEnd
      // all omitted properties default to `true` if unspecified
    }
  }
});
```
