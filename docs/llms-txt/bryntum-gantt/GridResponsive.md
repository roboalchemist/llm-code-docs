# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/mixin/GridResponsive.md

# [GridResponsive](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridResponsive)

Simplifies making grid responsive. Supply levels as [responsiveLevels](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridResponsive#config-responsiveLevels) config, default levels are:

small

< 400px

medium

< 600px

large

\> 600px

Columns can define configs per level to be resized etc:

```
let grid = new Grid({
  responsiveLevels: {
    small: 300,
    medium: 400,
    large: '*' // everything above 400
  },

  columns: [
    {
      field: 'name',
      text: 'Name',
      responsiveLevels: {
        small: { hidden: true },
        '*': { hidden: false } // all other levels
      }
    },
    { field: 'xx', ... }
  ]
});
```

It is also possible to give a [Grid state](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) object instead of a level width, but in that case the object must contain a `levelWidth` property:

```
let grid = new Grid({
  responsiveLevels: {
    small: {
      // Width is required
      levelWidth : 400,
      // Other configs are optional, see GridState for available options
      rowHeight  : 30
    },
    medium : {
      levelWidth : 600,
      rowHeight  : 40
    },
    large: {
      levelWidth : '*', // everything above 300
      rowHeight  : 45
    }
  }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[responsiveLevels](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridResponsive#config-responsiveLevels)
"Break points" for which responsive config to use for columns and css.

Each level can be specified as:

* A number representing the width threshold (e.g., `400`)
* The string `'*'` to match all sizes above other thresholds
* A [ResponsiveLevelConfig](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridResponsive#typedef-ResponsiveLevelConfig) object with `levelWidth` and additional grid state properties

See the [responsive guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/responsive.md) for details and examples.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridResponsive](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridResponsive#property-isGridResponsive)
Identifies an object as an instance of [GridResponsive](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridResponsive) class, or subclass thereof.

[isGridResponsive](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridResponsive#property-isGridResponsive-static)
Identifies an object as an instance of [GridResponsive](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridResponsive) class, or subclass thereof.

[responsiveLevel](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridResponsive#property-responsiveLevel)
Get currently used responsive level (as string)

## Functions

Functions are methods available for calling on the class

[getClosestBiggerLevel](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridResponsive#function-getClosestBiggerLevel)
Find closes bigger level, aka level we want to use.

[updateResponsive](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridResponsive#function-updateResponsive)
Check if resize lead to a new responsive level and take appropriate actions

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[responsive](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridResponsive#event-responsive)
Grid resize lead to a new responsive level being applied

## Typedefs

Typedefs are type definitions for the class

[ResponsiveLevelConfig](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridResponsive#typedef-ResponsiveLevelConfig)
Configuration object for a responsive level. Contains a required `levelWidth` plus any [GridState](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) properties to apply when this level is active.
