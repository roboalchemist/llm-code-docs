# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/StickyCells.md

# [StickyCells](https://bryntum.com/docs/gantt/api/Grid/feature/StickyCells)

A feature which pins configurable content from a grid row to the top of the grid while the row scrolls off the top but is still visible.

As soon as the row becomes too small to contain the content, it is unpinned, and scrolls out naturally, and the following row's configured content becomes pinned.

For example:

```
    new Grid({
        features : {
            stickyCells : {
                // Identifies elements to clone and pin to the grid top.
                contentSelector : '.myClassName'
            }
        }
    });
```

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[contentSelector](https://bryntum.com/docs/gantt/api/Grid/feature/StickyCells#config-contentSelector)
A CSS selector which must identify the content within your grid row which you require to be pinned to the grid while the row if the topmost row, and remains visible.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStickyCells](https://bryntum.com/docs/gantt/api/Grid/feature/StickyCells#property-isStickyCells)
Identifies an object as an instance of [StickyCells](https://bryntum.com/docs/gantt/api/#Grid/feature/StickyCells) class, or subclass thereof.

[isStickyCells](https://bryntum.com/docs/gantt/api/Grid/feature/StickyCells#property-isStickyCells-static)
Identifies an object as an instance of [StickyCells](https://bryntum.com/docs/gantt/api/#Grid/feature/StickyCells) class, or subclass thereof.
