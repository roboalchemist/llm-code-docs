# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/customElements/WidgetTag.md

# [WidgetTag](https://bryntum.com/docs/gantt/api/Core/customElements/WidgetTag)

A base class for a custom web component element wrapping one [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[theme](https://bryntum.com/docs/gantt/api/Core/customElements/WidgetTag#config-theme)
Path to theme to use within the web component.

```
<bryntum-grid stylesheet="resources/svalbard-light.css">
</bryntum-grid>
```

[stylesheet](https://bryntum.com/docs/gantt/api/Core/customElements/WidgetTag#config-stylesheet)
Path to the Bryntum components structural CSS, to use within the web component.

```
<bryntum-grid stylesheet="resources/grid.css">
</bryntum-grid>
```

[faPath](https://bryntum.com/docs/gantt/api/Core/customElements/WidgetTag#config-faPath)
Path to folder containing Font Awesome 6 Free.

```
<bryntum-grid fa-path="resources/fontawesome/webfonts">
</bryntum-grid>
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[widget](https://bryntum.com/docs/gantt/api/Core/customElements/WidgetTag#property-widget)
The widget instance rendered in the shadow root

[ready](https://bryntum.com/docs/gantt/api/Core/customElements/WidgetTag#property-ready)
A Promise which is resolved when this component's [stylesheet](https://bryntum.com/docs/gantt/api/#Core/customElements/WidgetTag#config-stylesheet) and [font](https://bryntum.com/docs/gantt/api/#Core/customElements/WidgetTag#config-faPath) dependencies are fully ready.

## Functions

Functions are methods available for calling on the class

[destroy](https://bryntum.com/docs/gantt/api/Core/customElements/WidgetTag#function-destroy)
Destroys the inner widget instance and cleans up
