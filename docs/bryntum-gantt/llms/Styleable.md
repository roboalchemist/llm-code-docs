# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/mixin/Styleable.md

# [Styleable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Styleable)

Mixin for widgets that allows manipulating CSS variables. Works by setting style properties of the target widgets element.

As part of configuration:

```
const taskBoard = new TaskBoard({
   css : {
       cardBorderTop    : '5px solid currentColor',
       columnBackground : '#ddd'
   }
});
```

And/or at runtime:

```
taskBoard.css.cardBackground = '#333';
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[cssVarPrefix](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Styleable#config-cssVarPrefix)
CSS variable prefix, appended to the keys used in [css](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Styleable#config-css).

For example:

```
{
   cssVarPrefix : 'taskboard',

   css : {
       cardBackground : '#333'
   }
}
```

Results in the css var `--taskboard-card-background` being set to `#333`.

Bryntum widgets defaults to using `-b-{type}` as prefix: `--b-button-font-size` etc.

[css](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Styleable#config-css)
Initial CSS variables to set.

Each key will be applied as a CSS variable to the target elements style. Key names are hyphenated and prefixed with [cssVarPrefix](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Styleable#config-cssVarPrefix) in the process. For example:

```
{
   cssVarPrefix : 'taskboard',

   css : {
       cardBackground : '#333'
   }
}
```

Results in the css var `--taskboard-card-background` being set to `#333`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStyleable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Styleable#property-isStyleable)
Identifies an object as an instance of [Styleable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Styleable) class, or subclass thereof.

[isStyleable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Styleable#property-isStyleable-static)
Identifies an object as an instance of [Styleable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Styleable) class, or subclass thereof.

[css](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Styleable#property-css)
Allows runtime manipulating of CSS variables.

See [css](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Styleable#config-css) for more information.

```
taskBoard.css.columnBackground = '#ccc';

// Will set "--taskboard-column-background : #ccc"
```
