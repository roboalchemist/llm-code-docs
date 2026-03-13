# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Panel.md

# [Panel](https://bryntum.com/docs/gantt/api/Core/widget/Panel)

Panel widget is a general purpose container which may be used to contain child [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items) or [html](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-html).

A Panel may also dock a [header](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-header) and [footer](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-footer) either at top/bottom or left/right:

```
const panel = new Panel({
  items : {
      customerName : { type : 'text', placeholder: 'Text' },
  },
  header : {
      title : 'Customer Details'
  }
});
```

Toolbars with buttons and other widgets
---------------------------------------

The Panel has two built-in toolbars, [tbar](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-tbar) and [bbar](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-bbar), which are toolbars docked to the top and bottom of the panel. You can easily add any widgets to them using the code below:

```
const panel = new Panel({
  title : 'A Test Panel',
  items : {
    customerName : {
        type : 'text', placeholder: 'Text'
    },
  },
  bbar : {
    items : {
      proceedButton : {
        text : 'Proceed',
        onClick : () => {
          alert('Proceeding!');
        }
      }
    }
});
```

Panel with a form
-----------------

You can use a Panel to create forms containing any Bryntum widgets. The Panel can load data into its field from a record since it subclasses the [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container) which has a [record](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-record) config.

Collapsible Panel
-----------------

Panels can also be [collapsible](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-collapsible). The collapsible panel can be collapsed and expanded by clicking the icon on the far-right end of the header.

Panel as a drawer
-----------------

Panels can be used as drawers which slide out from the side of the viewport, by using the [drawer](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-drawer) config:

Panel with strips
-----------------

Panels can have [strips](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-strips) docked to the top, right, bottom, or left. Strips are widgets that are docked to the panel's sides. The higher the `weight` assigned to a widget, the closer that widget will be to the panel body.

This is useful for adding slide-out containers to the panel. For example, a settings panel shown on the right as seen below (click the hamburger icon to show the settings panel).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[ui](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-ui)
Custom CSS class name suffixes to apply to the elements rendered by this widget. This may be specified as a space separated string, an array of strings, or as an object in which property names with truthy values are used as the class names.

The panel supports a few special UIs, such as `plain` rendition where toolbars and header have no background/borders, and `toolbar`.

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

Using the [cls config](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-cls) would make matching the content element more complex, and in the presence of [docked items](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-strips) and nested panels, impossible to target accurately.

[collapsed](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-collapsed)
Controls whether the panel is collapsed (the body of the panel is hidden while only the header is visible). Only valid if the panel is [collapsible](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-collapsible).

[collapsible](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-collapsible)
This config enables collapsibility for the panel. See [collapsed](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-collapsed).

For example:

```
     {
         type        : 'panel',
         collapsible : true
     }
```

This is managed by an instance of [PanelCollapser](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapser) which can be configured if an object is passed for this config property:

```
     {
         type        : 'panel',
         collapsible : {
             direction : 'left'
         }
     }
```

The config object form can contain a `type` property to specify the type of collapse the panel will use. This property can be one of the following:

* `'inline'` (see [PanelCollapser](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapser))
* `'overlay'` (see [PanelCollapserOverlay](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapserOverlay))

The default `direction` property is inferred from the position of the Panel in a flexbox layout.

If the Panel is the last child of a flexbox container, the `direction` is `'right'` for a horizontal flexbox layout and `'down'` for a vertical layout.

All other Panels in a flexbox container have the `direction` set to `'left'` for a horizontal layout and `'up'` for a vertical layout.

[bodyCls](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-bodyCls)
Custom CSS classes to add to the panel's body element.

May be specified as a space separated string, or as an object in which property names with truthy values are used as the class names:

```
 bodyCls : {
     'b-my-class'     : 1,
     [this.extraCls]  : 1,
     [this.activeCls] : this.isActive
 }
```

[trapFocus](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-trapFocus)
By default, tabbing within a Panel is not contained, ie you can TAB out of the Panel forwards or backwards. Configure this as `true` to disallow tabbing out of the Panel, and make tabbing circular within this Panel.

[title](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-title)
A title to display in the header or owning TabPanel. Causes creation and docking of a header to the top if no header is configured.

If a header has been disabled by configuring the [header](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-header)as `false`, setting it will have no effect.

The title is not HTML-encoded

The title is not HTML-encoded

[icon](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-icon)
An icon to show before the [title](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-title). Either pass a CSS class as a string, or pass a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object describing an element to represent the icon.

[header](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-header)
A config [object](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#typedef-PanelHeader) for the panel's header or a string in place of a `title`.

Configuring this as `false` explicitly removes the header bar, overriding any [tools](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-tools) or [title](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-title) configs.

[stripDefaults](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-stripDefaults)
An object containing config defaults for corresponding [strips](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-strips) objects with a matching name.

By default, this object contains the keys `'bbar'` and `'tbar'` to provide default config values for the [bbar](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-bbar) and [tbar](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-tbar) configs.

This object also contains a key named `'*'` with default config properties to apply to all strips. This object provides the default `type` (`'toolbar') and [dock](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-dock) (`'top'\`) property for strips.

[strips](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-strips)
An object containing widgets keyed by name. By default (when no `type` is given), strips are [toolbars](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar). If you want to pass an array, you can use the toolbar's [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items).

The [bbar](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-bbar) and [tbar](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-tbar) configs are shortcuts for adding toolbars to the panel's `strips`.

Strips are arranged based on their [dock](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-dock) and [weight](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-weight) configs.

For widgets using a `dock` of `'top'`, `'bottom'`, `'left'`, `'right'`, `'start'` or `'end'`(an "edge strip"), the higher the `weight` assigned to a widget, the closer that widget will be to the panel body.

For widgets with `'header'` or `'pre-header'` for `dock` (a "header strip"), higher `weight` values cause the widget to be placed closer to the panel's title.

```
 new Panel({
     title : 'Test',
     html  : 'Panel strip test',
     strips : {
         left : {
             dock  : 'left'
             items : {
                 go : {
                     text : 'Go'
                 }
             }
         }
     }
 });

// Pass an array to tbar
strips : {
    tbar : {
        items: {
            addButton : {
                type : 'button',
                text : 'Add column',
                icon : 'fa-plus',
                onAction : ({ source }) => addColumn(source.element)
            },
            // consider 'getCurrentDate()` a custom function
            today : `Today is ${getCurrentDate()}`
        }
    }
}
```

[footer](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-footer)
Config object of a footer. May contain a `dock`, `html` and a `cls` property. A footer is not a widget, but rather plain HTML that follows the last element of the panel's body and [strips](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-strips).

The `dock` property may be `top`, `right`, `bottom`, `left`, `start` or `end`

[revealed](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-revealed)
This config is used with [PanelCollapserOverlay](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapserOverlay) to programmatically control the visibility of the panel's body. In this mode of collapse, the body of a collapsed panel is a floating overlay. Setting this config to `true` will show this element, while `false` will hide it.

[tools](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-tools)
The [tools](https://bryntum.com/docs/gantt/api/#Core/widget/Tool) to add either before or after the `title` in the Panel header. Each property name is the reference by which an instantiated tool may be retrieved from the live `[tools](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Toolable#property-tools)` property.

```
new Panel({
    ...
    tools : {
        add : {
            cls : 'fa fa-plus',
            handler() {
                // Clicked the tool
            }
        }
    }
});
```

[tbar](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-tbar)
A Config object representing the configuration of a [Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar), or array of config objects representing the child items of a Toolbar. This creates a toolbar docked to the top of the panel immediately below the header.

To add toolbars not docked to the top, see [bbar](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-bbar) and [strips](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-strips).

```
// Text only
tbar : ['Project Timeline Overview', '->', 'Key Milestones & Deadlines'],

// Buttons
tbar : [
   {
      type     : 'button',
      ref      : 'addButton',
      text     : 'Add column',
      icon     : 'fa-plus',
      tooltip  : 'Add new column',
      onAction : ({ source }) => addColumn(source.element) // add new column
  },
  {
      type     : 'button',
      ref      : 'removeButton',
      text     : 'Remove last',
      icon     : 'fa-minus',
      tooltip  : 'Remove last column',
      onAction : () => grid.columns.count > 1 && grid.columns.last.remove() // remove last column
  }
]

// ToolbarConfig
tbar : {
    height : '4em',
    items  : {
        button1 : { text : 'A button', icon : 'fa fa-plus' },
        button2 : { text : 'Right button 1', icon : 'fa fa-trash', style : 'margin-inline-start:auto' },
        button3 : { icon : 'fa fa-gear' }
    }
}
```

[bbar](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-bbar)
A Config object representing the configuration of a [Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar), or array of config objects representing the child items of a Toolbar. Another way to add a bbar is to use [strips](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-strips).

```
// Text only
bbar : [`Total number of students: ${totalStds}`, '->', `Passed Students: ${passedStds}`],

// Buttons
bbar : [
   {
      type     : 'button',
      ref      : 'addButton',
      text     : 'Add column',
      icon     : 'fa-plus',
      tooltip  : 'Add new column',
      onAction : ({ source }) => addColumn(source.element) // add new column
  },
  {
      type     : 'button',
      ref      : 'removeButton',
      text     : 'Remove last',
      icon     : 'fa-minus',
      tooltip  : 'Remove last column',
      onAction : () => grid.columns.count > 1 && grid.columns.last.remove() // remove last column
  }
]

// ToolbarConfig
bbar : {
    height : '4em',
    items  : {
        button1 : { text : 'A button', icon : 'fa fa-plus' },
        button2 : { text : 'Right button 1', icon : 'fa fa-trash', style : 'margin-inline-start:auto' },
        button3 : { icon : 'fa fa-gear' }
    }
}
```

This creates a toolbar docked to the bottom of the panel immediately above the footer.

[drawer](https://bryntum.com/docs/gantt/api/Core/widget/Panel#config-drawer)
Make this Panel a docked drawer which slides out from one side of the browser viewport by default.

If this Panel is a child of another widget, the drawer will slide out from the side of the parent widget.

By default, it floats above the content of its host. If you want the drawer to be inline within the host, consuming content space in the host, set the `drawer` `inline` property to `true`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPanel](https://bryntum.com/docs/gantt/api/Core/widget/Panel#property-isPanel)
Identifies an object as an instance of [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel) class, or subclass thereof.

[isPanel](https://bryntum.com/docs/gantt/api/Core/widget/Panel#property-isPanel-static)
Identifies an object as an instance of [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel) class, or subclass thereof.

[collapsed](https://bryntum.com/docs/gantt/api/Core/widget/Panel#property-collapsed)
Controls whether the panel is collapsed (the body of the panel is hidden while only the header is visible). Only valid if the panel is [collapsible](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-collapsible).

[title](https://bryntum.com/docs/gantt/api/Core/widget/Panel#property-title)
A title to display in the header or owning TabPanel. Causes creation and docking of a header to the top if no header is configured.

If a header has been disabled by configuring the [header](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-header)as `false`, setting it will have no effect.

The title is not HTML-encoded

The title is not HTML-encoded

[tools](https://bryntum.com/docs/gantt/api/Core/widget/Panel#property-tools)
The tool Widgets as specified by the [tools](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-tools) configuration (and the [closable](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-closable) configuration in the Popup subclass). Each is a [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) instance which may be hidden, shown and observed and styled just like any other widget.

```
panel.tools.add = {
    cls : 'fa fa-plus',
    handler() {
        // Clicked the tool
    }
}
```

[tbar](https://bryntum.com/docs/gantt/api/Core/widget/Panel#property-tbar)
Get toolbar [Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar) docked to the top of the panel

[bbar](https://bryntum.com/docs/gantt/api/Core/widget/Panel#property-bbar)
Get toolbar [Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar) docked to the bottom of the panel

[collapsing](https://bryntum.com/docs/gantt/api/Core/widget/Panel#property-collapsing)
This property is `true` if the panel is currently collapsing.

[collapsingExpanding](https://bryntum.com/docs/gantt/api/Core/widget/Panel#property-collapsingExpanding)
This property is `true` if the panel is currently either collapsing or expanding.

[expanding](https://bryntum.com/docs/gantt/api/Core/widget/Panel#property-expanding)
This property is `true` if the panel is currently expanding.

## Functions

Functions are methods available for calling on the class

[collapsePanel](https://bryntum.com/docs/gantt/api/Core/widget/Panel#function-collapsePanel)
Collapse the panel.

[expandPanel](https://bryntum.com/docs/gantt/api/Core/widget/Panel#function-expandPanel)
Expand the panel.

[toggleCollapsed](https://bryntum.com/docs/gantt/api/Core/widget/Panel#function-toggleCollapsed)
Toggles collapsed state of the panel.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[toolClick](https://bryntum.com/docs/gantt/api/Core/widget/Panel#event-toolClick)
A header [tool](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-tools) has been clicked.

[collapse](https://bryntum.com/docs/gantt/api/Core/widget/Panel#event-collapse)
Fires when a Panel is collapsed using the [collapsible](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-collapsible) setting.

[expand](https://bryntum.com/docs/gantt/api/Core/widget/Panel#event-expand)
Fires when a Panel is expanded using the [collapsible](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-collapsible) setting.

## Typedefs

Typedefs are type definitions for the class

[PanelHeader](https://bryntum.com/docs/gantt/api/Core/widget/Panel#typedef-PanelHeader)
An object that describes a Panel's header.
