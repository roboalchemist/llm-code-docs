# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Widget.md

# [Widget](https://bryntum.com/docs/gantt/api/Core/widget/Widget)

The base class for all other widgets in the Bryntum libraries. The Widget base class encapsulates a native DOM element, and can optionally contain [html](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-html). See also [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container) which lets you build a component tree where widgets can contain other widgets. Simple widget example (inspect with the DOM inspector to see it's really just a simple DIV):

Rendering
---------

Subclasses should override the [compose](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-compose) method to return their encapsulating element and internal DOM structure. The `compose()` method returns a [createElement](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#function-createElement-static) config object that is\* used to create the DOM structure, based on its [configurable](https://bryntum.com/docs/gantt/api/#Core/Base#property-configurable-static) properties:

```
 class Button extends Widget {
     static configurable = {
         cls  : null,
         text : null
     };

     compose() {
         const { cls, text } = this;  // collect all relevant configs properties (for auto-detection)

         return {
             tag   : 'button',
             class : cls,
             text
         };
     }
 }
```

The config properties used by the `compose()` method are auto-detected when the method is first called for a class. All relevant properties must be read, even if they end up not being used so that future changes to these properties will mark the rendering as dirty.

When a config property used by `compose()` is modified, the [recompose](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-recompose) method is called. Since `recompose()` is a [delayable](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable#property-delayable-static) method, calling it schedules a delayed call to `compose()` and a DOM update. Accessing the Widget's primary `element` or any reference element property will force the DOM update to occur immediately.

### Lifecycle events

The lifecycle events provide hooks into the various stages of a widget's existence, allowing for custom behavior at key points.

These events include

* [elementCreated](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#event-elementCreated) - Fired once, after the widget's main element has been created but before it is added to the DOM. At this stage it will have its [style](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-style) and [cls](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-cls) applied. But since the element is not yet in the DOM, it will not be visible, nor will styles from CSS be applied.

    If you need to measure the element (for example to set its size based on its content), you should add a listener for the [paint](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#event-paint) event and perform your measurements there.

* [paint](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#event-paint) - Fired whenever the widget becomes visible and eligible for layout. This event may be fired multiple times during the lifetime of a widget, whenever it becomes visible after being hidden, or when an ancestor widget is shown after being hidden.

    Note that to only react the first time a widget is painted, you can use the `once` option when adding a listener early in the widget's lifecycle or check the `firstPaint` property of the event object.

* [beforeDestroy](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#event-beforeDestroy) - Fired when the widget is being destroyed. At this stage the widget is still fully functional and can be interacted with if certain actions need to be called.

* [destroy](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#event-destroy) - Fired after the widget has been destroyed. At this stage the widget's DOM elements have been removed from the DOM and all event listeners have been detached. The widget is _completely inert_ and has no properties or methods.

### Child Elements

Unlike typical [DOM config](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#function-createElement-static) objects, the object returned by `compose()` can use an object to simplify naming:

```
 class Button extends Widget {
     ...

     compose() {
         const { cls, iconCls, text } = this;  // collect all relevant configs properties (for auto-detection)

         return {
             tag   : 'button',
             class : cls,

             children : {
                 iconElement : iconCls && {
                     class : {
                         'button-icon' : 1,
                         [iconCls]     : 1
                     }
                 },

                 textElement : {
                     text
                 }
             }
         };
     }
 }
```

The keys of the `children` are [iterated](https://bryntum.com/docs/gantt/api/https://2ality.com/2015/10/property-traversal-order-es6.html) to convert the values into the array required by [createElement](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#function-createElement-static). The names of the properties becomes the `reference` of the element.

For example, the above is equivalent to the following:

```
 class Button extends Widget {
     ...

     compose() {
         const { cls, iconCls, text } = this;  // collect all relevant configs properties (for auto-detection)

         return {
             tag   : 'button',
             class : cls,

             children : [iconCls && {
                 reference : 'iconElement',
                 class : {
                     'button-icon' : 1,
                     [iconCls]     : 1
                 }
             }, {
                 reference : 'textElement',
                 text
             }]
         };
     }
 }
```

In other places inside your class, you can then access those elements as `this.iconElement` and `this.textElement`, no need to use `querySelector` etc.

The object form of `children` is preferred for clarity but also because it facilitates inheritance.

### Inheritance

When a derived class implements `compose()`, the object it returns is automatically merged with the object returned by the base class.

For example, the following class adds a new child element:

```
 class MenuButton extends Button {
     ...

     compose() {
         const { menuCls } = this;  // collect all relevant configs properties (for auto-detection)

         return {
             children : {
                 menuElement : {
                     class : {
                         'button-menu' : 1,
                         [menuCls]     : 1
                     }
                 }
             }
         };
     }
 }
```

### Listeners

Reference elements may also define event `listeners` in the `compose()` method:

```
 class Button extends Widget {
     compose() {
         const { cls, text } = this;

         return {
             tag   : 'button',
             class : cls,
             text,

             listeners : {
                 click : 'onClick'
             }
         };
     }

     onClick(event) {
         // handle click event
     }
 }
```

Resolving properties
--------------------

Values for a Widgets properties can be resolved from the ownership hierarchy. For example a text field in a toolbar can get its initial value from a property on the container owning the toolbar. This is achieved by prefixing the desired property name with 'up.':

```
 const grid = new Grid((
     tbar : [{
         type  : 'numberfield',
         // Fields value will be retrieved from the grids rowHeight property
         value : 'up.rowHeight'
     }]
 });
```

NOTE: this is for now a one way one time binding, the value will only be read initially and not kept up to date on later changes.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[color](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-color)
Applies the specified color to the widget, by setting the `--b-primary` CSS variable in the widgets `style` block.

If the supplied color starts with `b-`, a named color from the current theme will be used (red -> b-color-red etc.). Applied as `<tag style="--b-primary: var(--b-color-<color>)">`, for example:

```
<tag style="--b-primary: var(--b-color-red)">
```

When the supplied color does not start with `b-`, it is assumed to be a valid CSS color specification and is used as is. Applied as `<tag style="--b-primary: <color>">`, for example:

```
<tag style="--b-primary: red">
```

[element](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-element)
A [createElement](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#function-createElement-static) config object or HTML string from which to create the Widget's element.

[callOnFunctions](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-callOnFunctions)
Set to `false` to not call onXXX method names (e.g. `onShow`, `onClick`), as an easy way to listen for events.

```
const container = new Container({
    callOnFunctions : true

    onHide() {
         // Do something when the 'hide' event is fired
    }
});
```

[hideMode](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-hideMode)
Determines how a widget will prevent itself from being seen when [hidden](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-hidden) is set to `true` or the [hide](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-hide) method is called.

The allowed values are as follows:

* `'display'` (the default) to hide the widget using `display: none` style
* `'clip'` to hide the widget using CSS `clip` style (only valid if `position: absolute`)
* `'opacity'` to hide the widget using `opacity : 0` style (and `pointer-events : none`)

[id](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-id)
Widget id, if not specified one will be generated. Also used for lookups through Widget.getById

[html](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-html)
The HTML to display initially or a function returning the markup (called at widget construction time).

This may be specified as the name of a function which can be resolved in the component ownership hierarchy, such as 'up.getHTML' which will be found on an ancestor Widget.

[content](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-content)
The HTML content that coexists with sibling elements which may have been added to the [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement) by plugins and features. When specifying html, this widget's element will also have the [htmlCls](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-htmlCls) class added to its classList, to allow targeted styling.

[cls](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-cls)
Custom CSS classes to add to element. May be specified as a space separated string, or as an object in which property names with truthy values are used as the class names:

```
 cls : {
     'b-my-class'     : 1,
     [this.extraCls]  : 1,
     [this.activeCls] : this.isActive
 }
```

[ui](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-ui)
Custom CSS class name suffixes to apply to the elements rendered by this widget. This may be specified as a space separated string, an array of strings, or as an object in which property names with truthy values are used as the class names.

For example, consider a `Panel` with a `ui` config like so:

```
 new Panel({
     text : 'OK',
     ui   : 'light'
 });
```

This will apply the CSS class `'b-panel-ui-light'` to the main element of the panel as well as its many child elements. This allows simpler CSS selectors to match the child elements of this particular panel UI:

```
 .b-panel-content.b-panel-ui-light {
     background-color : #eee;
 }
```

Using the [cls config](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-cls) would make matching the content element more complex, and in the presence of [docked items](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-strips) and nested panels, impossible to target accurately.

[collapsify](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-collapsify)
Determines how a [collapsed](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-collapsed) panel will treat this widget if it resides within the panel's header (for example, as one of its [strips](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-strips) or [tools](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-tools)).

Valid options are:

* `null` : The widget will be moved to the overlay header when the panel is collapsed (the default).
* `false` : The widget will be unaffected when the panel is collapsed and will remain in the primary panel header at all times.
* `'hide'` : The widget will be hidden when the panel is collapsed.
* `'overlay'` : The widget will only appear in the collapsed panel's overlay header. See [collapsible type='overlay'](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapserOverlay).

[contentElementCls](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-contentElementCls)
Custom CSS classes to add to the [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement). May be specified as a space separated string, or as an object in which property names with truthy values are used as the class names:

```
 cls : {
     'b-my-class'     : 1,
     [this.extraCls]  : 1,
     [this.activeCls] : this.isActive
 }
```

[defaultCls](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-defaultCls)
Custom CSS classes to add to this widget's `element`. This property is typically used internally to assign default CSS classes while allowing `cls` to alter these defaults. It is not recommended that client code set this config but instead should set `cls`.

For example, to remove a class defined by `defaultCls` using `cls`, declare the class name as a key with a falsy value:

```
 cls : {
     'default-class' : false
 }
```

[dock](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-dock)
Controls the placement of this widget when it is added to a [panel's](https://bryntum.com/docs/gantt/api/#Core/widget/Panel) [strips collection](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-strips). Typical values for this config are `'top'`, `'bottom'`, `'left'`, or `'right'`, which cause the widget to be placed on that side of the panel's body. Such widgets are called "edge strips".

Also accepts direction neutral horizontal values `'start'` and `'end'`.

If this config is set to `'header'`, the widget is placed in the panel's header, following the title. If this config is set to `'pre-header'`, the widget is placed before the title. Such widgets are called "header strips".

[tab](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-tab)
A configuration for the [tab](https://bryntum.com/docs/gantt/api/#Core/widget/Tab) created for this widget when it is placed in a [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel). For example, this config can be used to control the icon of the `tab` for this widget:

```
 items : {
     panel : {
         type : 'panel',
         // other configs...

         tab : {
             icon : 'fa-wrench'
         }
     },
     ...
 }
```

Another use for this config is to set the tab's [rotate](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Rotatable#config-rotate) value differently than the default managed by the `TabPanel`:

```
 items : {
     panel : {
         type : 'panel',
         // other configs...

         tab : {
             rotate : false   // don't rotate even if tabBar is docked left or right
         }
     },
     ...
 }
```

Set this to `false` to prevent the creation of a `tab` for this widget. In this case, this widget must be [shown](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-show) explicitly. The [activeTab](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel#config-activeTab) for the tab panel will be -1 in this situation.

```
 items : {
     panel : {
         type : 'panel',
         tab  : false,    // no tab for this item

         // other configs...
     },
     ...
 ]
```

[elementAttributes](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-elementAttributes)
An object specifying attributes to assign to the root element of this widget. Set `null` value to attribute to remove it.

```
new Label({
    elementAttributes : {
       'data-role': 'primary', // Add data-role attribute with `"primary"` value
       inert : '',             // Add inert with no value
       title : null            // This will remove the title attribute from the element
    }
});
```

[htmlCls](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-htmlCls)
The CSS class(es) to add when HTML content is being applied to this widget.

[style](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-style)
Custom style spec to add to element

[disabled](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-disabled)
Disable or enable the widget. It is similar to [readOnly](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-readOnly) except a disabled widget cannot be focused, uses a different rendition (usually greyish) and does not allow selecting its value.

Set to `'inert'` to also set the `inert` DOM attribute.

[readOnly](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-readOnly)
Whether this widget is read-only. This is only valid if the widget is an input field, **or contains input fields at any depth**.

All descendant input fields follow the widget's setting. If a descendant widget has a readOnly config, that is set.

[ignoreParentReadOnly](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-ignoreParentReadOnly)
Determines if the widgets read-only state should be controlled by its parent.

When set to `true`, setting a parent container to read-only will not affect the widget. When set to `false`, it will affect the widget.

[adopt](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-adopt)
Element (or element id) to adopt as this Widget's encapsulating element. The widget's content will be placed inside this element.

If this widget has not been configured with an id, it will adopt the id of the element in order to preserve CSS rules which may apply to the id.

[appendTo](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-appendTo)
Element (or the id of an element) to append this widget's element to. Can be configured, or set once at runtime. To access the element of a rendered widget, see [element](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-element).

[insertBefore](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-insertBefore)
Element (or element id) to insert this widget before. If provided, [appendTo](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-appendTo) config is ignored.

[insertFirst](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-insertFirst)
Element (or element id) to append this widget element to, as a first child. If provided, [appendTo](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-appendTo) config is ignored.

[dataset](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-dataset)
Object to apply to elements dataset (each key will be used as a data-attribute on the element)

[tooltip](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-tooltip)
Tooltip for the widget, either as a string or as a Tooltip config object.

By default, the Widget will use a single, shared instance to display its tooltip as configured, reconfiguring it to the specification before showing it. Therefore, it may not be permanently mutated by doing things such as adding fixed event listeners.

To have this Widget _own_ its own `Tooltip` instance, add the property `newInstance : true` to the configuration. In this case, the tooltip's [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-owner) will be this Widget.

**Note that in the absence of a configured [ariaDescription](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ariaDescription), the tooltip's value will be used to populate an `aria-describedBy` element within this Widget.**

[showTooltipWhenDisabled](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-showTooltipWhenDisabled)
Set to `false` to not show the tooltip when this widget is [disabled](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-disabled)

[preventTooltipOnTouch](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-preventTooltipOnTouch)
Prevent tooltip from being displayed on touch devices. Useful for example for buttons that display a menu on click etc, since the tooltip would be displayed at the same time.

[monitorResize](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-monitorResize)
When this is configured as `true` a [ResizeObserver](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver) is used to monitor this element for size changes caused by either style manipulation, or by CSS layout.

By default, notifications are queued up for delivery in the next microtask.

To receive notifications immediately, set the `immediate` option to `true`.

Size changes are announced using the [resize](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#event-resize) event.

[masked](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-masked)
Set to `true` to apply the default mask to the widget. Alternatively, this can be the mask message or a [Mask](https://bryntum.com/docs/gantt/api/#Core/widget/Mask) config object.

[maskDefaults](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-maskDefaults)
This config object contains the defaults for the [Mask](https://bryntum.com/docs/gantt/api/#Core/widget/Mask) created for the [masked](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-masked) config. Any properties specified in the `masked` config will override these values.

[floating](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-floating)
Set to `true` to move the widget out of the document flow and position it absolutely in browser viewport space.

[positionable](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-positionable)
This config is used to absolutely position this widget in its parent [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container). When enabled, this widget will be rendered into the parent widget's primary [element](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-element). In containers where the [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement) is not the same as the `element` (for example, [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel)), the value of this config indicates if this widget should be rendered `'before'` or `'after'` the `contentElement`.

Because `positionable` widgets are `position: absolute` and may even be rendered outside of the owning container's `contentElement`, these widgets do not participate in the standard layout of their container.

It is not necessary to set this config explicitly when using the position configs [top](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-top), [right](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-right), [bottom](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-bottom), or [left](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-left), unless it needs to be set to `'after'`.

[positioned](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-positioned)
Set to `true` when a widget is rendered into another widget's [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement), but must not participate in the standard layout of that widget, and must be positioned relatively to that widget's [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement).

[Editor](https://bryntum.com/docs/gantt/api/#Core/widget/Editor)s are positioned widgets.

[draggable](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-draggable)
_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating)._ Set to `true` to be able to drag a widget freely on the page. Or set to an object with a ´handleSelector´ property which controls when a drag should start.

```
draggable : {
    handleSelector : ':not(button)'
}
```

[align](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-align)
_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating)._

How to align this element with its target when [showBy](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-showBy) is called passing a simple element as an align target.

Either a full alignment config object, or for simple cases, the edge alignment string to use.

When using a simple string, the format is `'[trblc]n-[trblc]n'` and it specifies our edge and the target edge plus optional offsets from 0 to 100 along the edges to align to. Also supports direction independent edges horizontally, `s` for start and `e` for end (maps to `l` and `r` for LTR, `r` and `l` for RTL).

See the [showBy](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-showBy) function for more details about using the object form.

Once set, this is stored internally in object form.

[centered](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-centered)
_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating)._ Set to `true` to centre the Widget in browser viewport space.

[constrainTo](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-constrainTo)
_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) or [positioned](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-positioned)._ Element, Widget or Rectangle to which this Widget is constrained.

[anchor](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-anchor)
_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) and being shown through [showBy](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-showBy)._ `true` to show a connector arrow pointing to the align target.

[owner](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-owner)
The owning Widget of this Widget. If this Widget is directly contained (that is, it is one of the [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-items) of a Container), this config will be ignored. In this case the owner is **always** the encapsulating Container.

If this Widget is floating, this config should be specified by the developer.

Registering with an `owner` creates a lifecycle relationship with that owning Widget. When the `owner` is destroyed this widget will also be destroyed.

This also allows focus to be tracked in the ownership tree. If a widget `owns` another widget, then even if that other widget is in a different element, focusing that owned widget will _not_ cause a [focusOut](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#event-focusOut) event, and the [containsFocus](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-containsFocus) property remains set.

A widget can unregister from its `owner` and break this relationship at any time by setting the property to `null`. It is then the developer's responsibility to ensure that this Widget is destroyed.

[scrollAction](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-scrollAction)
Defines what to do if document is scrolled while Widget is visible (only relevant when floating is set to `true`). Valid values: ´null´: do nothing, ´hide´: hide the widget or ´realign´: realign to the target if possible.

[hideAnimation](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-hideAnimation)
_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating)._

An object which defined which CSS style property should be animated upon hide, and how it should be animated eg:

```
{
   opacity: {
       to : 0,
       duration: '10s',
       delay: '0s'
   }
}
```

Set to `'false'` to disable animation.

[showAnimation](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-showAnimation)
_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating)._

An object which defined which CSS style property should be animated upon show, and how it should be animated eg:

```
{
   opacity: {
       to : 1,
       duration: '10s',
       delay: '0s'
   }
}
```

Set to `'false'` to disable animation.

[top](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-top)
The `top` CSS absolute position for this widget. If specified, the widget is implicitly configured as [positionable](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-positionable).

[right](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-right)
The `inset-inline-end` CSS absolute position for this widget. If specified, the widget is implicitly configured as [positionable](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-positionable).

[bottom](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-bottom)
The `bottom` CSS absolute position for this widget. If specified, the widget is implicitly configured as [positionable](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-positionable).

[left](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-left)
The `inset-inline-start` CSS absolute position for this widget. If specified, the widget is implicitly configured as [positionable](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-positionable).

[x](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-x)
The x position for the widget.

_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) and not aligned or anchored to an element._

[y](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-y)
The y position for the widget.

_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) and not aligned or anchored to an element._

[scrollable](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-scrollable)
Specifies whether (and optionally in which axes) a Widget may scroll. `true` means this widget may scroll in both axes. May be an object containing boolean `overflowX` and `overflowY` properties which are applied to CSS style properties `overflowX` and `overflowY`. If they are boolean, they are translated to CSS overflow properties thus:

* `true` -> `'auto'`
* `false` -> `'hidden'`

After initialization, this property yields a [Scroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller) which may be used to both set and read scroll information.

A Widget uses its [overflowElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-overflowElement) property to select which element is to be scrollable. By default, in the base `Widget` class, this is the Widget's encapsulating element. Subclasses may implement `get overflowElement` to scroll inner elements.

[scrollerClass](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-scrollerClass)
The class to instantiate to use as the [scrollable](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-scrollable). Defaults to [Scroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller).

[defaultBindProperty](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-defaultBindProperty)
The name of the property to set when a single value is to be applied to this Widget. Such as when used in a grid WidgetColumn, this is the property to which the column's `field` is applied.

[defaultAction](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-defaultAction)
Event that should be considered the default action of the widget. When that event is triggered the widget is also expected to trigger an `action` event. Purpose is to allow reacting to most widgets in a coherent way.

[overflowable](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-overflowable)
When set to `true`, this widget is considered as a whole when processing [Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar) overflow. When `false`, this widget's child items are considered instead.

When set to the string `'none'`, this widget is ignored by overflow processing. This option should be used with caution as it prevents the overflow algorithm from moving such widgets into the overflow popup which may result in not clearing enough space to avoid overflowing the toolbar.

[width](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-width)
Widget's width, used to set element `style.width`. Either specify a valid width string or a number, which will get 'px' appended. We recommend using CSS as the primary way to control width, but in some cases this config is convenient.

[height](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-height)
Widget's height, used to set element `style.height`. Either specify a valid height string or a number, which will get 'px' appended. We recommend using CSS as the primary way to control height, but in some cases this config is convenient.

[maxHeight](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-maxHeight)
The element's maxHeight. Can be either a String or a Number (which will have 'px' appended). Note that like [height](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-height), _reading_ the value will return the numeric value in pixels.

[maxWidth](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-maxWidth)
The elements maxWidth. Can be either a String or a Number (which will have 'px' appended). Note that like [width](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-width), _reading_ the value will return the numeric value in pixels.

[minWidth](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-minWidth)
The elements minWidth. Can be either a String or a Number (which will have 'px' appended). Note that like [width](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-width), _reading_ the value will return the numeric value in pixels.

[minHeight](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-minHeight)
The element's minHeight. Can be either a String or a Number (which will have 'px' appended). Note that like [height](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-height), _reading_ the value will return the numeric value in pixels.

[margin](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-margin)
Widget's margin. This may be configured as a single number or a `TRBL` format string. numeric-only values are interpreted as pixels.

[flex](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-flex)
When this widget is a child of a [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container), it will by default be participating in a flexbox layout. This config allows you to set this widget's [flex](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex) style. This may be configured as a single number or a `<flex-grow> <flex-shrink> <flex-basis>` format string. numeric-only values are interpreted as the `flex-grow` value.

[weight](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-weight)
A widgets weight determines its position among siblings when added to a [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container). Higher weights go further down.

[alignSelf](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-alignSelf)
When this widget is a child of a [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container), it will by default be participating in a flexbox layout. This config allows you to set this widget's [align-self](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/align-self) style.

[ripple](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-ripple)
Configure as `true` to have the component display a translucent ripple when its [focusElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-focusElement), or [element](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-element) is tapped _if the current theme supports ripples_. Out of the box, only the Material theme supports ripples.

This may also be a config object containing the properties listed below.

E.g.

```
   columns  : [{}...],
   ripple   : {
       color : 'red',
       clip  : '.b-grid-row'
   },
   ...
```

[title](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-title)
A title to display for the widget. Only in effect when inside a container that uses it (such as TabPanel)

[ref](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-ref)
An identifier by which this widget will be registered in the [widgetMap](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-widgetMap) of all ancestor containers.

If omitted, this widget will be registered using its [id](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-id). In most cases `ref` is preferable over `id` since `id` is required to be globally unique while `ref` is not.

The `ref` value is also added to the elements dataset, to allow targeting it using CSS etc.

[hidden](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-hidden)
Configure with true to make widget initially hidden.

[textAlign](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-textAlign)
Text alignment: 'left', 'center' or 'right'. Also accepts direction neutral 'start' and 'end'.

Applied by adding a `b-text-align-xx` class to the widgets element. Blank by default, which does not add any alignment class.

To be compliant with RTL, 'left' yields same result as 'start' and 'right' as 'end'.

[tag](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-tag)
The tag name of this Widget's root element

[recomposeAsync](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-recomposeAsync)
Set this config to `false` to disable batching DOM updates on animation frames for this widget. This has the effect of synchronously updating the DOM when configs affecting the rendered DOM are modified. Depending on the situation, this could simplify code while increasing time spent updating the DOM.

[rootElement](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-rootElement)
If you are rendering this widget to a shadow root inside a web component, set this config to the shadowRoot. If not inside a web component, set it to `document.body`

[ariaLabel](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-ariaLabel)
A localizable string (May contain `'L{}'` tokens which resolve in the locale file) to inject as the `aria-label` attribute.

This widget is passed as the `templateData` so that functions in the locale file can interrogate the widget's state.

[ariaDescription](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-ariaDescription)
A localizable string (May contain `'L{}'` tokens which resolve in the locale file) to inject into an element which will be linked using the `aria-describedby` attribute.

This widget is passed as the `templateData` so that functions in the locale file can interrogate the widget's state.

[maximizeOnMobile](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-maximizeOnMobile)
_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating)._

When configured as `true`, this widget uses [isMobile](https://bryntum.com/docs/gantt/api/#Core/helper/BrowserHelper#property-isMobile-static) to maximize itself on mobile devices.

[twinForwardEvents](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-twinForwardEvents)
The events to forward from an overflow twin to its origin widget.

May be specified as a space separated string, or as an object in which property names with truthy values are used as the event names:

```
 twinForwardEvents : {
     change : true,
     input  : 1
 }
```

NOTE: This config cannot be dynamically changed after the `overflowTwin` has been created (see [ensureOverflowTwin](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-ensureOverflowTwin).

[twinSyncConfigs](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-twinSyncConfigs)
A mapping object describing config properties to sync with the `overflowTwin`. This is pass to [bindConfigs](https://bryntum.com/docs/gantt/api/#Core/Base#function-bindConfigs).

For example:

```
 twinSyncConfigs : {
     disabled : true,
     value    : 'checked'   // sync twin's checked config to this object's value config
 }
```

NOTE: This config cannot be dynamically changed after the `overflowTwin` has been created (see [ensureOverflowTwin](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-ensureOverflowTwin).

[span](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-span)
Programmatic control over how many columns to span when used in a grid layout.

[column](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-column)
Programmatic control over which column to start in when used in a grid layout.

[detectCSSCompatibilityIssues](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-detectCSSCompatibilityIssues)
Check for CSS compatibility issues when upgrading to v7. Performs the following checks:

* Detects usage of `.b-fa` class for icons. FontAwesome is no longer built-in, the standard `.fa` class should be used instead.
* Detects missing FontAwesome font. With FontAwesome no longer built-in, this must be included separately by the app.
* Checks for presence of a Bryntum theme. Theme and structural CSS has been separated, both structural CSS and a theme must be included.

Defaults to `true` in Grid, Scheduler, Scheduler Pro, Gantt, Calendar and TaskBoard.

[dataField](https://bryntum.com/docs/gantt/api/Core/widget/Widget#config-dataField)
When this Widget configuration is used in the Grid's RowExpander feature's `widget` config, provide the field on the expanded record to use for populating this widget's store (if applicable)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isWidget](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-isWidget)
Identifies an object as an instance of [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) class, or subclass thereof.

[isWidget](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-isWidget-static)
Identifies an object as an instance of [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) class, or subclass thereof.

[$name](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-$name-static)
Class name getter. Used when original ES6 class name is minified or mangled during production build. Should be overridden in each class which extends Widget or it descendants.

```
class MyNewClass extends Widget {
    static $name = 'MyNewClass';
}
```

[type](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-type-static)
Widget name alias which you can use in the `items` of a Container widget.

```
class MyWidget extends Widget {
    static get type() {
       return 'mywidget';
    }
}
```

```
const panel = new Panel({
   title : 'Cool widgets',
   items : {
      customWidget : { type : 'mywidget', html : 'Lorem ipsum dolor sit amet...' }
   }
});
```

[convertPinchToMousewheel](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-convertPinchToMousewheel-static)
By default, on touch devices, a two finger pinch gesture where both touch points are within a Bryntum widget is converted to a `CTRL/wheel` event injected at the mid-point between the two initial touches.

This is so that Scheduler and Calendar views which are configured to `zoomOnMouseWheel` will zoom on pinch on touch devices.

That disables the platform's native pinch-zooming. Set this static flag to `false` to disable the conversion:

```
    Widget.convertPinchToMousewheel = false;
```

[element](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-element)
Get this widget's encapsulating HTMLElement, which is created along with the widget but added to DOM at render time.

[hideMode](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-hideMode)
Determines how a widget will prevent itself from being seen when [hidden](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-hidden) is set to `true` or the [hide](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-hide) method is called.

The allowed values are as follows:

* `'display'` (the default) to hide the widget using `display: none` style
* `'clip'` to hide the widget using CSS `clip` style (only valid if `position: absolute`)
* `'opacity'` to hide the widget using `opacity : 0` style (and `pointer-events : none`)

[id](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-id)
Get/set widgets id

[html](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-html)
The HTML to display initially or a function returning the markup (called at widget construction time).

This may be specified as the name of a function which can be resolved in the component ownership hierarchy, such as 'up.getHTML' which will be found on an ancestor Widget.

[content](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-content)
Set HTML content safely, without disturbing sibling elements which may have been added to the [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement) by plugins and features. When specifying html, this widget's element will also have the [htmlCls](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-htmlCls) added to its classList, to allow targeted styling.

[cls](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-cls)
Custom CSS classes to add to element. May be specified as a space separated string, or as an object in which property names with truthy values are used as the class names:

```
 cls : {
     'b-my-class'     : 1,
     [this.extraCls]  : 1,
     [this.activeCls] : this.isActive
 }
```

[tab](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-tab)
The [tab](https://bryntum.com/docs/gantt/api/#Core/widget/Tab) created for this widget when it is placed in a [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel).

[disabled](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-disabled)
Get/set element's disabled state. Set to `'inert'` to also set the `inert` DOM attribute.

[readOnly](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-readOnly)
Get/set element's readOnly state. This is only valid if the widget is an input field, **or contains input fields at any depth**. Updating this property will trigger a [readOnly](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#event-readOnly) event.

All descendant input fields follow the widget's setting. If a descendant widget has a readOnly config, that is set.

[appendTo](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-appendTo)
Element (or the id of an element) to append this widget's element to. Can be configured, or set once at runtime. To access the element of a rendered widget, see [element](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-element).

[insertBefore](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-insertBefore)
Element (or element id) to insert this widget before. If provided, [appendTo](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-appendTo) config is ignored.

[insertFirst](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-insertFirst)
Element (or element id) to append this widget element to, as a first child. If provided, [appendTo](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-appendTo) config is ignored.

[scrollable](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-scrollable)
Accessor to the [Scroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller) which can be used to both set and read scroll information.

[margin](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-margin)
Get element's margin property. This may be configured as a single number or a `TRBL` format string. numeric-only values are interpreted as pixels.

[flex](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-flex)
Get element's flex property. This may be configured as a single number or a format string:

```
 <flex-grow> <flex-shrink> <flex-basis>
```

Numeric-only values are interpreted as the `flex-grow` value.

[alignSelf](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-alignSelf)
Get/set this widget's `align-self` flexbox setting. This may be set to modify how this widget is aligned within the cross axis of a flexbox layout container.

[ref](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-ref)
An identifier by which this widget will be registered in the [widgetMap](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-widgetMap) of all ancestor containers.

If omitted, this widget will be registered using its [id](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-id). In most cases `ref` is preferable over `id` since `id` is required to be globally unique while `ref` is not.

The `ref` value is also added to the elements dataset, to allow targeting it using CSS etc.

[hidden](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-hidden)
Get/set the widget hidden state.

Note: `hidden : false` does _not_ mean that this widget is definitely visible. To ascertain visibility, use the [isVisible](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-isVisible) property.

[maximizeOnMobile](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-maximizeOnMobile)
_Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating)._

When configured as `true`, this widget uses [isMobile](https://bryntum.com/docs/gantt/api/#Core/helper/BrowserHelper#property-isMobile-static) to maximize itself on mobile devices.

[span](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-span)
Programmatic control over how many columns to span when used in a grid layout.

[column](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-column)
Programmatic control over which column to start in when used in a grid layout.

[hasGeneratedId](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-hasGeneratedId)
true if no id was set, will use generated id instead (widget1, ...). Toggle automatically on creation

[hasPainted](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-hasPainted)
This property is set to `true` after processing the initial paint for the widget. It remains `false` during the initial paint. The intended use for this flag is to avoid processing that will be handled by the first paint (similar to not firing events during the widget's initial configuration). If this field is `true`, the initial paint has already taken place, otherwise, it has yet to run. This field differs from `isPainted` which checks that the widget's element is attached to the DOM.

[innerItem](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-innerItem)
This readonly property is `true` for normal widgets in the [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items) of a container. It is `false` for special widgets such as a [tbar](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-tbar).

[renderConfigs](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-renderConfigs-static)
This property declares the set of config properties that affect a Widget's rendering, i.e., the configs used by the [compose](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-compose) method.

For example:

```
 class Button extends Widget {
     static renderConfigs = [ 'cls', 'iconCls', 'text' ];
 }
```

Alternatively this can be an object:

```
 class Button extends Widget {
     static renderConfigs = {
         cls     : true,
         iconCls : true,
         text    : true
     };
 }
```

[cellInfo](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-cellInfo)
An object providing the `record` and `column` for a widget embedded inside a [WidgetColumn](https://bryntum.com/docs/gantt/api/#Grid/column/WidgetColumn)

```
columns : [
   {
       type   : 'widget',
       widgets: [{
           type     : 'button',
           icon     : 'fa fa-trash',
           onAction : ({ source : btn }) => btn.cellInfo.record.remove()
       }]
   }
]
```

[all](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-all-static)
Returns an array containing all existing Widgets. The returned array is generated by this call and is not an internal structure.

[recomposeAsync](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-recomposeAsync-static)
Get/set the [recomposeAsync](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-recomposeAsync) config for all widgets. Setting this value will set the config for all existing widgets and will be the default value for newly created widgets. Set this value to `null` to disable the default setting for new widgets while leaving existing widgets unaffected.

[overflowTwin](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-overflowTwin)
This widget's twin that is placed in an overflow menu when this widget has been hidden by its owner, typically a [Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar) due to [overflow](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar#config-overflow). The `overflowTwin` is created lazily by [ensureOverflowTwin](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-ensureOverflowTwin).

[isComposable](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-isComposable)
Returns `true` if this class uses `compose()` to render itself.

[dataset](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-dataset)
Get widgets elements dataset or assign to it

[contentElement](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-contentElement)
The child element into which content should be placed. This means where [html](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-html) should be put, or, for [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container)s, where child items should be rendered.

[style](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-style)
Get/set widgets elements style. The setter accepts a cssText string or a style config object, the getter always returns a CSSStyleDeclaration

[overflowElement](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-overflowElement)
The child element which scrolls if any. This means the element used by the [scrollable](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-scrollable).

[anchorSize](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-anchorSize)
Returns an `[x, y]` array containing the width and height of the anchor arrow used when aligning this Widget to another Widget or element.

The height is the height of the arrow when pointing upwards, the width is the width of the baseline.

[x](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-x)
Moves this Widget to the desired x position.

Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) and not aligned or anchored to an element.

[y](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-y)
Moves this Widget to the desired y position.

Only valid if this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) and not aligned or anchored to an element.

[width](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-width)
Get elements offsetWidth or sets its style.width, or specified width if element not created yet.

[maxWidth](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-maxWidth)
Get/set elements maxWidth. Getter returns max-width from elements style, which is always a string. Setter accepts either a String or a Number (which will have 'px' appended). Note that like [width](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-width), _reading_ the value will return the numeric value in pixels.

[minWidth](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-minWidth)
Get/set elements minWidth. Getter returns min-width from elements style, which is always a string. Setter accepts either a String or a Number (which will have 'px' appended). Note that like [width](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-width), _reading_ the value will return the numeric value in pixels.

[height](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-height)
Get element's offsetHeight or sets its style.height, or specified height if element no created yet.

[maxHeight](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-maxHeight)
Get/set element's maxHeight. Getter returns max-height from elements style, which is always a string. Setter accepts either a String or a Number (which will have 'px' appended). Note that like [height](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-height), _reading_ the value will return the numeric value in pixels.

[minHeight](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-minHeight)
Get/set element's minHeight. Getter returns min-height from elements style, which is always a string. Setter accepts either a String or a Number (which will have 'px' appended). Note that like [height](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-height), _reading_ the value will return the numeric value in pixels.

[tooltip](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-tooltip)
Get/set a tooltip on the widget. Accepts a string or tooltip config (specify true (or 'true') to use placeholder as tooltip). When using a string it will configure the tooltip with `textContent: true` which enforces a default max width.

By default, this uses a singleton Tooltip instance which may be accessed from the `[Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget)` class under the name `Widget.tooltip`. This is configured according to the config object on pointer over.

To request a separate instance be created just for this widget, add `newInstance : true` to the configuration.

[tooltip](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-tooltip-static)
The shared [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip) instance which handles [tooltips](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-tooltip) which are **not** configured with `newInstance : true`.

[isVisible](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-isVisible)
Determines visibility by checking if the Widget is hidden, or any ancestor is hidden and that it has an element which is visible in the DOM

[focusability](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-focusability)
Returns an object describing the focus and keyboard navigation aspects of this widget's [focusElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-focusElement).

[focusableElement](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-focusableElement)
Returns this widget's [focusElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-focusElement) if that element can currently be given focus (e.g., this widget is not disabled, or hidden).

[focusElement](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-focusElement)
Get this widget's primary focus holding element if this widget is itself focusable, or contains focusable widgets.

[assignedId](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-assignedId)
Get id assigned by user (not generated id)

[parent](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-parent)
Get this Widget's parent when used as a child in a [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container),

[owner](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-owner)
The owning Widget of this Widget. If this Widget is directly contained (i.e. it is one of the [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-items) of a Container), **this property will be read-only, and will refer to the containing Widget**.

If this property has not been set and this is a `Popup` with a [forElement](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-forElement), this config will refer to that element's encapsulating Widget.

If this Widget is floating, this property should be set by the developer.

Registering with an `owner` creates a lifecycle relationship with that owning Widget. When the `owner` is destroyed this widget will also be destroyed.

A widget can unregister from its `owner` and break this relationship at any time by setting the property to `null`. It is then the developer's responsibility to ensure that this Widget is destroyed.

[previousSibling](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-previousSibling)
Get this Widget's previous sibling in the parent [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container), or, if not in a Container, the previous sibling widget in the same _parentElement_.

[nextSibling](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-nextSibling)
Get this Widget's next sibling in the parent [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container), or, if not in a Container, the next sibling widget in the same _parentElement_.

[containsFocus](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-containsFocus)
This property is set to `true` when focus is within the ownership tree of this Widget.

This means that either the DOM of this widget contains focus, **or, any widget DOM who's [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-owner) axis leads to this widget contains focus**.

For example a [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField) with its [DatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker) open and being interacted with will still have `containsFocus` set.

[staticClassList](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-staticClassList)
Returns the `DomClassList` for this widget's class. This object should not be mutated.

[uiClasses](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-uiClasses)
Returns the cross-product of the classes `staticClassList` with each `ui` as an array of strings.

For example, a Combo with a `ui: 'foo bar'` would produce:

```
 [
     'b-widget-foo', 'b-field-foo', 'b-text-field-foo', 'b-picker-field-foo', 'b-combo-foo',
     'b-widget-bar', 'b-field-bar', 'b-text-field-bar', 'b-picker-field-bar', 'b-combo-bar'
 ]
```

[uiClassList](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-uiClassList)
Returns the cross-product of the classes `staticClassList` with each `ui` as a `DomClassList` instance.

For example, a Combo with a `ui: 'foo bar'` would produce:

```
     new DomClassList({
         'b-field-ui-foo'       : 1,
         'b-text-field-ui-foo'   : 1,
         'b-picker-field-ui-foo' : 1,
         'b-combo-ui-foo'       : 1,

         'b-field-ui-bar'       : 1,
         'b-text-field-ui-bar'   : 1,
         'b-picker-field-ui-bar' : 1,
         'b-combo-ui-bar'       : 1
     });
```

A Panel with a `ui: 'foo bar'` would produce:

```
     new DomClassList({
         'b-panel-ui-foo' : 1,
         'b-panel-ui-bar' : 1
     });
```

[widgetClassList](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-widgetClassList)
Used by the Widget class internally to create CSS classes based on this Widget's inheritance chain to allow styling from each level to apply.

For example Combo would yield `"["b-widget", "b-field", "b-text-field", "b-picker-field", "b-combo"]"`

May be implemented in subclasses to add or remove classes from the super.widgetClassList

[focusVisible](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-focusVisible)
This property yields `true` if the currently focused element has been reached through other means than mouse click. If the `activeElement` matches `:focus-visible`.

[focusVisible](https://bryntum.com/docs/gantt/api/Core/widget/Widget#property-focusVisible-static)
This property yields `true` if the currently focused element has been reached through other means than mouse click. If the `activeElement` matches `:focus-visible`.

## Functions

Functions are methods available for calling on the class

[initClass](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-initClass-static)
Call once per class for custom widgets to have them register with the `Widget` class, allowing them to be created by type.

For example:

```
class MyWidget extends Widget {
  static get type() {
    return 'mywidget';
  }
}
MyWidget.initClass();
```

[create](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-create-static)
Creates a new widget instance based on the passed config object. The config object is require to have a `type` property which determines what kind of widget to create.

[finalizeInit](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-finalizeInit)
Called by the Base constructor after all configs have been applied.

[configureOverflowTwin](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-configureOverflowTwin)
This method returns the config object to use for creating this widget's [overflowTwin](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-overflowTwin).

[createOverflowTwin](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-createOverflowTwin)
This method creates the [overflowTwin](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-overflowTwin) for this widget. It is called by [ensureOverflowTwin](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-ensureOverflowTwin) if the `overflowTwin` does not yet exist.

The config for the [overflowTwin](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-overflowTwin) is produced by [configureOverflowTwin](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-configureOverflowTwin).

[ensureOverflowTwin](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-ensureOverflowTwin)
This method returns the existing [overflowTwin](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-overflowTwin) or creates it, if it has not yet been created (see [createOverflowTwin](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-createOverflowTwin)).

[addRefAccessor](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-addRefAccessor)
Defines an element reference accessor on the class prototype. This accessor is used to flush any pending DOM changes prior to accessing such elements.

[attachRef](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-attachRef)
This method is called by `DomHelper.createElement` and `DomSync.sync` as new reference elements are created.

[detachRef](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-detachRef)
This method is called by `DomSync.sync` as reference elements are removed from the DOM.

[afterRecompose](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-afterRecompose)
This method is called following an update to the widget's rendered DOM.

[compose](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-compose)
Returns a [createElement](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#function-createElement-static) config object that defines this widget's DOM structure. This object should be determined using [configurable](https://bryntum.com/docs/gantt/api/#Core/Base#property-configurable-static) properties to ensure this method is called again if these properties are modified.

For more information see [class documentation](https://bryntum.com/docs/gantt/api/#Core/widget/Widget).

[doCompose](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-doCompose)
This method iterates the class hierarchy from Widget down to the class of this instance and calls any `compose` methods implemented by derived classes.

[domSyncCallback](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-domSyncCallback)
Template method called during DOM updates. See [DomSync.sync()](https://bryntum.com/docs/gantt/api/#Core/helper/DomSync#function-sync-static).

[isCollapsified](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-isCollapsified)
This method determines if this widget (typically a [Tool](https://bryntum.com/docs/gantt/api/#Core/widget/Tool)) should be placed in the header of the calling [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel).

[recompose](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-recompose)
Calling this [delayable](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable#property-delayable-static) method marks this widget as dirty. The DOM will be updated on the next animation frame:

```
 widget.recompose();

 console.log(widget.recompose.isPending);
 > true
```

A pending update can be flushed by calling `flush()` (this does nothing if no update is pending):

```
 widget.recompose.flush();
```

This can be combined in one call to force a DOM update without first scheduling one:

```
 widget.recompose.now();
```

[getRenderContext](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-getRenderContext)
Interprets the [appendTo](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-appendTo), [insertBefore](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-insertBefore) and [insertFirst](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-insertFirst) configs to return an array containing `[parentElement, insertBefore]`

[template](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-template)
A function which, when passed an instance of this Widget, produces a valid HTML string which is compiled to create the encapsulating element for this Widget, and its own internal DOM structure.

Note that this just creates the DOM structure that _this_ Widget owns. If it contains child widgets (Such as for example a grid), this is not included. The template creates own structure.

Certain elements within the generated element can be identified as special elements with a `reference="name"` property. These will be extracted from the element upon creation and injected as the named property into the Widget. For example, a [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField) will have an `input` property which is its `<input>` element.

[fixRefOwnerId](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-fixRefOwnerId)
This method fixes the element's `$refOwnerId` when this instance's `id` is changing.

[alignTo](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-alignTo)
If this Widget is [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) or [positioned](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-positioned), and visible, aligns the widget according to the passed specification. To stop aligning, call this method without arguments.

[onAlignTargetOutOfView](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-onAlignTargetOutOfView)
This method is called when the [alignTo](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-alignTo) target element loses intersection with the visible viewport. That means it has been scrolled out of view, or becomes zero size, or hidden or is removed from the DOM.

The base class implementation hides by default.

[realign](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-realign)
Called when an element which affects the position of this Widget's [align target](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-alignTo) scrolls so that this can realign.

If the target has scrolled out of view, then this Widget is hidden.

[rectangle](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-rectangle)
Returns the specified bounding rectangle of this widget.

[rectangleOf](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-rectangleOf)
Returns the specified bounding rectangle of the specified child `element` of this widget.

[toFront](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-toFront)
Only valid for [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) Widgets. Moves to the front of the visual stacking order.

[validateDragStartEvent](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-validateDragStartEvent)
Validates a `dragstart` event with respect to the target element. Dragging is not normally initiated when the target is interactive such as an input field or its label, or a button. This may be overridden to provide custom drag start validation.

[setXY](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-setXY)
Moves this Widget to the x,y position. Both arguments can be omitted to just set one value.

_For [floating](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) Widgets, this is a position in the browser viewport._ _For [positioned](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-positioned) Widgets, this is a position in the element it was rendered into._

[onDisabled](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-onDisabled)
Called when disabled state is changed. Override in subclass that needs special handling when being disabled.

[disable](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-disable)
Disable the widget

[enable](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-enable)
Enable the widget

[requestFullscreen](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-requestFullscreen)
Requests fullscreen display for this widget

[exitFullscreen](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-exitFullscreen)
Exits fullscreen mode

[focus](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-focus)
Focuses this widget if it has a focusable element.

[show](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-show)
Shows this widget

[showBy](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-showBy)
Show aligned to another target element or [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) or [Rectangle](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle)

[suspendVisibility](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-suspendVisibility)
Temporarily changes the [isVisible](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-isVisible) to yield `false` regardless of this Widget's true visibility state. This can be useful for suspending operations which rely on the [isVisible](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-isVisible) property.

This increments a counter which [resumeVisibility](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-resumeVisibility) decrements.

[resumeVisibility](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-resumeVisibility)
Resumes visibility. If the suspension counter is returned to zero by this, then the [paint](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#event-paint) event is triggered, causing a cascade of `paint` events on all descendants. This can be prevented by passing `false` as the only parameter.

[hide](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-hide)
Hide widget

[up](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-up)
Looks up the [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-owner) axis to find an ancestor which matches the passed selector. The selector may be a widget type identifier, such as `'grid'`, or a function which will return `true` when passed the desired ancestor.

[closest](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-closest)
Starts with this Widget, then Looks up the [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-owner) axis to find an ancestor which matches the passed selector. The selector may be a widget type identifier, such as `'grid'`, or a function which will return `true` when passed the desired ancestor.

[owns](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-owns)
Returns `true` if this Widget owns the passed Element, Event or Widget. This is based on the widget hierarchy, not DOM containment. So an element in a `Combo`'s dropdown list will be owned by the `Combo`.

[eachAncestor](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-eachAncestor)
Iterate over all ancestors of this widget.

_Note_: Due to this method aborting when the function returns `false`, beware of using short form arrow functions. If the expression executed evaluates to `false`, iteration will terminate.

[eachWidget](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-eachWidget)
Iterate over all widgets owned by this widget and any descendants.

_Note_: Due to this method aborting when the function returns `false`, beware of using short form arrow functions. If the expression executed evaluates to `false`, iteration will terminate.

[queryAll](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-queryAll)
Returns an array of all descendant widgets which the passed filter function returns `true` for.

[query](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-query)
Returns the first descendant widgets which the passed filter function returns `true` for.

[getWidgetByRef](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-getWidgetByRef)
Get a widget by ref, starts on self and traverses up the owner hierarchy checking `widgetMap` at each level. Not checking the top level widgetMap right away to have some acceptance for duplicate refs.

[captureFocus](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-captureFocus)
Returns a function that will set the focus (`document.activeElement`) to the most consistent element possible based on the focus state at the time this method was called. Derived classes can implement `captureFocusItem()` to refine this process to include logical items (e.g., a grid cell) that would be more stable than DOM element references.

If this widget does not contain the focus, the returned function will do nothing.

[captureFocusItem](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-captureFocusItem)
This method is called by `captureFocus()` when this widget contains the focus and it returns a function that restores the focus to the correct internal element. The returned function is only called if the current `document.activeElement` is different from the passed `activeElement`.

This method can be replaced by derived classes to capture stable identifiers for the currently focused, logical item (for example, a cell of a grid).

[contains](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-contains)
Returns `true` if this widget is or contains the specified element or widget.

[revertFocus](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-revertFocus)
If this Widget contains focus, focus is reverted to the source from which it entered if possible, or to a close relative if not.

[getFocusRevertTarget](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-getFocusRevertTarget)
This method finds a close sibling (or parent, or parent's sibling etc. recursively) to which focus can be directed in the case of revertFocus not having a focusable element from our focusInEvent.

This can happen when the "from" component is destroyed or hidden. We should endeavour to prevent focus escaping to `document.body` for accessibility and ease of use, and keep focus close.

[getStaticWidgetClasses](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-getStaticWidgetClasses)
Returns a `DomClassList` computed from the `topMostBase` (e.g., `Widget` or `Panel`) with the given `suffix` appended to each `widgetClass`.

[fromCache](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-fromCache)
Gets dom elements in the view. Caches the results for faster future calls.

[emptyCache](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-emptyCache)
Clear caches, forces all calls to fromCache to requery dom. Called on render/rerender.

[mask](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-mask)
Mask the widget, showing the specified message

[unmask](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-unmask)
Unmask the widget

[executeAndAwaitAnimations](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-executeAndAwaitAnimations)
Executes a function which initiates animations, and waits for any animations within the passed element to complete.

Takes a snapshot of animations running before and after the function executes and waits for any animations started due to that function to finish.

[animationsFinished](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-animationsFinished)
Returns a Promise which resolves when all finite animations on _or within_ the element are finished.

Pass `subtree` as `false` to only consider animations directly on the element.

[query](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-query-static)
Analogous to `document.querySelector`, finds the first Bryntum widget matching the passed selector. Supported selector formats:

* Widget type (lowercased class name): `'grid'`, `'scheduler'`, `'gantt'`
* ID selector: `'#myWidgetId'`
* Attribute selector: `'[ref=myRef]'`, `'[customProp=value]'`
* Filter function returning `true` for matching widgets

```
Widget.query('grid').destroy();
Widget.query('#myScheduler');
Widget.query('[ref=timeline]');
Widget.query(widget => widget.isCool);
```

This is aliased on the global `bryntum` object as `bryntum.query`.

[queryAll](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-queryAll-static)
Analogous to `document.querySelectorAll`, finds all Bryntum widgets matching the passed selector. Supported selector formats:

* Widget type (lowercased class name): `'grid'`, `'scheduler'`, `'gantt'`
* ID selector: `'#myWidgetId'`
* Attribute selector: `'[ref=myRef]'`, `'[customProp=value]'`
* Filter function returning `true` for matching widgets

```
Widget.queryAll('field', true);
Widget.queryAll('[customProp=someValue]');
```

This is aliased on the global `bryntum` object as `bryntum.queryAll`.

[fromElement](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-fromElement-static)
Returns the Widget which owns the passed element (or event).

This is aliased on the global `bryntum` object as `bryntum.fromElement`.

[getById](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-getById-static)
Returns the widget with the specified id.

[fromSelector](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-fromSelector-static)
Returns the Widget which owns the passed CSS selector.

```
const button = Widget.fromSelector('#my-button');
```

[triggerFieldChange](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-triggerFieldChange)
Triggers a 'change' event with the supplied params. After triggering it also calls `onFieldChange()` on each ancestor the implements that function, supplying the same set of params.

[isolateFieldChange](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-isolateFieldChange)
Returns `true` if the given `field`'s value change should be isolated (kept hidden by this widget). By default, this method returns the value of [isolateFields](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-isolateFields) for all fields.

[attachTooltip](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-attachTooltip-static)
Attached a tooltip to the specified element.

```
Widget.attachTooltip(element, {
  text: 'Useful information goes here'
});
```

[announceAriaLive](https://bryntum.com/docs/gantt/api/Core/widget/Widget#function-announceAriaLive)
Announces a text message that can be parsed by assistive technologies using an `aria-live` element.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[elementCreated](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-elementCreated)
Triggered when a widget's [element](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-element) is available.

[recompose](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-recompose)
This event is fired after a widget's elements have been synchronized due to a direct or indirect call to [recompose](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-recompose), if this results in some change to the widget's rendered DOM elements.

[beforeShow](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-beforeShow)
Triggered before a widget is shown. Return `false` to prevent the action.

[paint](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-paint)
Triggered when a widget which had been in a non-visible state for any reason achieves visibility.

A non-visible state _might_ mean the widget is hidden and has just been shown.

But this event will also fire on widgets when a non-visible (unrendered, or hidden) ancestor achieves visibility, for example a [Popup](https://bryntum.com/docs/gantt/api/#Core/widget/Popup) being shown.

TLDR: **This event can fire multiple times**

[beforeHide](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-beforeHide)
Triggered before a widget is hidden. Return `false` to prevent the action.

[show](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-show)
Triggered after a widget is shown.

[hide](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-hide)
Triggered after a widget was hidden

[readOnly](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-readOnly)
Fired when a Widget's read only state is toggled

[focusIn](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-focusIn)
Fired when focus enters this Widget.

[focusOut](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-focusOut)
Fired when focus exits this Widget's ownership tree. This is different from a `blur` event. focus moving from within this Widget's ownership tree, even if there are floating widgets will not trigger this event. This is when focus exits this widget completely.

[resize](https://bryntum.com/docs/gantt/api/Core/widget/Widget#event-resize)
Fired when the encapsulating element of a Widget resizes _only when [monitorResize](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-monitorResize) is `true`_.

## Typedefs

Typedefs are type definitions for the class

[Color](https://bryntum.com/docs/gantt/api/Core/widget/Widget#typedef-Color)
Predefined named colors (actual color might vary by theme):

red

pink

magenta

purple

violet

deep-purple

indigo

blue

light-blue

cyan

teal

green

light-green

lime

yellow

orange

amber

deep-orange

light-gray

gray

black

[AlignSpec](https://bryntum.com/docs/gantt/api/Core/widget/Widget#typedef-AlignSpec)
Specification for how to align a Widget to another Widget, Element or Rectangle.

[CellWidgetContext](https://bryntum.com/docs/gantt/api/Core/widget/Widget#typedef-CellWidgetContext)
A context object injected into all cell widgets owned by grid widget columns. It allows event handlers for the widget to ascertain the context in which they are operating.
