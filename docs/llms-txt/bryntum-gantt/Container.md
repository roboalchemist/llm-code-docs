# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Container.md

# [Container](https://bryntum.com/docs/gantt/api/Core/widget/Container)

A Widget that can contain other widgets. Uses a CSS Grid layout by default, either use CSS or see the [layout](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-layout) config to apply another layout.

```
// Create a container with two widgets
const container = new Container({
    items : {
        name  : { type : 'textfield', label : 'Name' },
        score : { type : 'numberfield', label : 'Score' }
    }
});
```

Label position & input field alignment
--------------------------------------

Fields support placing labels either before or above them. This can be set for all fields in a container at once by specifying the [labelPosition](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-labelPosition) config. It supports 3 settings:

* `'above'` - Labels are placed above the field. For text fields in the Material3 theme, this means ~ on the fields top border.
* `'before'` - Labels are placed before the field.
* `'align-before'` - Labels are placed before the field and the fields are arranged in a two column layout (used in the live demo above).

`align-before` setting cannot be used in conjunction with specifying a Container `layout`.

When using `'align-before'`, the container uses `display: grid` to lay out the fields. You can override this by specifying a different `grid-template-columns` value in your CSS. To get two equal width columns, use:

```
.b-container.b-columns {
    grid-template-columns: 1fr 1fr;
}
```

If you want input elements aligned to the right / end side of your container, enable [inputFieldAlign](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-inputFieldAlign) as seen in the demo below.

Adding and removing child widgets
---------------------------------

Containers can have child widgets added, or removed during their lifecycle to accommodate business needs. For example:

```
 // Insert a child widget before another field
 myContainer.insert(textField, someField)

 // Remove a child widget
 myContainer.remove(checkboxField);
```

If you are looking for a more powerful container that can have toolbars, a title bar, and more see [Panel](https://bryntum.com/docs/gantt/api/#Core/widget/Panel).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[items](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-items)
An object containing typed child widget config objects or Widgets. May also be specified as an array.

If configured as an Object, the property names are used as the child component's [ref](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref) name, and the value is the child component's config object.

```
 class MyContainer extends Container {
     static configurable = {
         items : {
             details : {
                 type : 'panel',
                 ....
             },
             button : {
                 type : 'button',
                 text : 'Save'
             }
         }
     }
 }

 new MyContainer({
     title    : 'Test Container',
     floating : true,
     centered : true,
     width    : 600,
     height   : 400,
     layout   : 'fit',
     items    : {
         button : {
             disabled : true
         },
         details : {
             title : 'More coolness',
             html  : 'Details content'
         }
     }
 }).show();
```

The order of the child widgets is determined by the order they are defined in `items`, but can also be affected by configuring a [weight](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-weight) on one or more widgets.

To remove existing items, set corresponding keys to `null`.

If you want to customize child items of an existing class, you can do this using the child widget 'ref' identifier (useful for reconfiguring Event Editor in Scheduler / Gantt):

```
 new MyCustomTabPanel({
     items    : {
         // Reconfigure tabs
         firstTab : {
             title : 'My custom title'
         },
         secretTab : null // hide this tab
     }
 }).show();
```

Note that conversion between array and object notation is not supported, if you want to override items in a container that uses object notation, you must use the same notation. This applies for example to when customizing items in the event editor in Scheduler and the task editor in Scheduler Pro and Gantt.

[lazyItems](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-lazyItems)
An array of [child item](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items) _config objects_ which is to be converted into instances only when this Container is rendered, rather than eagerly at construct time.

_This is mutually exclusive with the [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items) config._

[tabBarItems](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-tabBarItems)
When this container is used as a tab in a TabPanel, these items are added to the [TabBar](https://bryntum.com/docs/gantt/api/#Core/widget/TabBar) when this container is the active tab.

```
new TabPanel({
    appendTo : targetElement,
    height   : '25em',
    items: {
        firstTab : {
            title: 'First',
            items: {
                name : { type: 'textfield', label: 'Name' }
            },
            tabBarItems : [{
                type    : 'button',
                text    : 'Add tab',
                onClick : 'up.onAddTabClick'
            }]
        }
    },

    onAddTabClick({ value }) {
        this.add({
            type  : 'container',
            title : 'New tab',
            items : {
                button : {
                    type : 'button',
                    text : 'Click me',
                    onClick() {
                        Toast.show('Awesome!');
                    }
                }
            }
        });
    }
});
```

[defaults](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-defaults)
A config object containing default settings to apply to all child widgets.

[labelPosition](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-labelPosition)
Convenience setting to use same label placement on all child widgets.

Set it to 'auto' to let the theme decide on label placement.

Specifying `'align-before'` will position labels before the field and also apply a two column layout (in combination with `display: contents` on the fields) to align all labels in the first column and the fields in the second.

[inputFieldAlign](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-inputFieldAlign)
Convenience setting to align input fields of child widgets. By default, the Field input element is placed immediately following the `label`. If you prefer to have all input fields aligned to the right, set this config to `'end'`.

[layoutStyle](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-layoutStyle)
The CSS style properties to apply to the [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement).

By default, a Container's [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement) uses flexbox layout, so this config may contain the following properties:

* [flexDirection](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction) default '`row`'
* [flexWrap](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap)
* [flexFlow](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-flow)
* [justifyContent](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)
* [alignItems](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/align-items)
* [alignContent](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/align-content)
* [placeContent](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/place-content)

[itemCls](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-itemCls)
An optional CSS class to add to child items of this container.

[border](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-border)
Set `true` to add a border to this container's element.

[layout](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-layout)
The short name of a helper class which manages rendering and styling of child items.

Or a config object which includes a `type` property which specifies which type of layout to use, and how to configure that layout.

By default, the only special processing that is applied is that the Container class's [itemCls](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-itemCls) is added to child items.

Containers use CSS flexbox in its default configuration to arrange child items. You may either use the [layoutStyle](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-layoutStyle) configuration to tune how child items are layed out, or use one of the built in helper classes which include:

* `fit` A single child item is displayed fitting exactly into the [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement).
* `card` Child items are displayed one at a time, size to fit the [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement) and are slid in from the side when activated.
* `box` Child items are layed out using flexbox.

For example:

```
{
    id     : 'myContainer',
    // Our child items flow downwards and are stretched to fill our width
    layout : {
        type       : 'box',
        direction  : 'column'
        align      : 'stretch'
    }
}
```

[namedItems](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-namedItems)
An object containing default config objects which may be referenced by name in the [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items) config. For example, a specialized [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) subclass may have a `namedItems` default value defined like this:

```
 namedItems : {
     removeRow : {
         text : 'Remove row',
         onItem() {
             this.ownerGrid.remove(this.ownerGrid.selectedRecord);
         }
     }
 }
```

Then whenever that subclass is instantiated and configured with an [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items) object, the `items` may use the above defaults like this:

```
 items : {
     removeRow : true,   // The referenced namedItem will be applied to this
     otherItemRef : {
         text : 'Option 2',
         onItem() { }
     }
}
```

If a menu instance (or its class) does not include `removeRow` in its `items`, no menu item will be created. See also [defaults](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-defaults).

[overflowable](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-overflowable)
When set to `true`, this widget is considered as a whole when processing [Toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/Toolbar) overflow. When `false`, this widget's child items are considered instead.

When set to the string `'none'`, this widget is ignored by overflow processing. This option should be used with caution as it prevents the overflow algorithm from moving such widgets into the overflow popup which may result in not clearing enough space to avoid overflowing the toolbar.

[textContent](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-textContent)
Specify `true` for a container used to show text markup. It will apply the CSS class `b-text-content` which specifies a default max-width that makes long text more readable.

This CSS class is automatically removed if the container adds/defines child Widgets.

[record](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-record)
[Record](https://bryntum.com/docs/gantt/api/#Core/data/Model) whose values will be used to populate fields in the container.

Any descendant widgets of this Container with a `name` property (or a `ref` if no name is configured) will have its value set to the value of that named property of the record.

If no record is passed, the widget has its value set to `null`.

To strictly match by the `name` property, configure [strictRecordMapping](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-strictRecordMapping) as `true`.

When fields loaded from this record are changed by user input, the [hasChanges](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-hasChanges) property will be set.

[strictRecordMapping](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-strictRecordMapping)
Specify `true` to match fields by their `name` property only when assigning a [record](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-record), without falling back to `ref`.

[autoUpdateRecord](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-autoUpdateRecord)
Update assigned [record](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-record) automatically on field changes

[autoUpdateFields](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-autoUpdateFields)
Update fields if the [record](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-record) changes

[hideWhenEmpty](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-hideWhenEmpty)
Specify `true` to make this container hide when it has no visible children (Either empty or all children hidden).

Container will show itself when there are visible children, ie: hidden children are shown, or new visible children are added.

[isolateFields](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-isolateFields)
Specify `true` to isolate record changes to this container and its ancestors. Prevents record updates from propagating up from here and also prevents record updates from parent from propagating down to us.

[defaultFocus](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-defaultFocus)
A [query](https://bryntum.com/docs/gantt/api/#Core/widget/Container#function-query) selector function which can identify the descendant widget to which focus should be directed by default.

Or a CSS selector string which identifies a descendant element to focus.

By default, the first focusable descendant widget is chosen. This may direct focus to a different widget:

```
    new Popup({
        title        : 'Details',
        width        : '25em',
        centered     : true,
        modal        : true,

        // Focus goes straight to OK button in the bottom toolbar on show
        defaultFocus : w => w.ref === 'okButton',
        items        : {
            nameField : {
                type  : 'textfield',
                label : 'Name'
            },
            ageField  : {
                type  : 'numberfield',
                label : 'Name'
            }
        },
        bbar     : {
            items : {
                okButton : {
                    text    : 'OK',
                    handler : okFunction
                },
                cancelButton : {
                    text    : 'Cancel',
                    handler : cancelFunction
                }
            }
        }
    }).show();
```

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-rendition)
Either a default `rendition` to apply to all child widgets, or a map of renditions keyed by child widget `type`.

```
// Mixed types, use object form:
new Container({
  rendition : {
    text   : 'outlined',
    button : 'raised'
  },
  items : [
    { type : 'text', label : 'Name' },
    { type : 'button', text : 'Save' }
  ]
});

// Single type, can use string form:
new Container({
  rendition : 'outlined',
  items : [
    { type : 'button', text : 'Save' },
    { type : 'button', text : 'Cancel' }
  ]
});
```

[gridColumns](https://bryntum.com/docs/gantt/api/Core/widget/Container#config-gridColumns)
Number of columns to use in a grid layout. Applied as `grid-template-columns: repeat(n, auto)`. Also applies the `b-columns` CSS class to the container.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isContainer](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-isContainer)
Identifies an object as an instance of [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container) class, or subclass thereof.

[isContainer](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-isContainer-static)
Identifies an object as an instance of [Container](https://bryntum.com/docs/gantt/api/#Core/widget/Container) class, or subclass thereof.

[labelPosition](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-labelPosition)
Convenience setting to use same label placement on all child widgets.

Set it to 'auto' to let the theme decide on label placement.

Specifying `'align-before'` will position labels before the field and also apply a two column layout (in combination with `display: contents` on the fields) to align all labels in the first column and the fields in the second.

[inputFieldAlign](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-inputFieldAlign)
Convenience setting to align input fields of child widgets. By default, the Field input element is placed immediately following the `label`. If you prefer to have all input fields aligned to the right, set this config to `'end'`.

[layoutStyle](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-layoutStyle)
The CSS style properties to apply to the [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement).

By default, a Container's [contentElement](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-contentElement) uses flexbox layout, so this config may contain the following properties:

* [flexDirection](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction) default '`row`'
* [flexWrap](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap)
* [flexFlow](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/flex-flow)
* [justifyContent](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)
* [alignItems](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/align-items)
* [alignContent](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/align-content)
* [placeContent](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/place-content)

[layout](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-layout)
The [layout](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-layout) as an instance of [Layout](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Layout). This is a helper class which adds and removes child widgets to this Container's DOM and applies CSS classes based upon its requirements.

The [card](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Card) layout provides for showing one child widget at a time, and provides a switching API to change which child widget is currently active.

[record](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-record)
[Record](https://bryntum.com/docs/gantt/api/#Core/data/Model) whose values will be used to populate fields in the container.

Any descendant widgets of this Container with a `name` property (or a `ref` if no name is configured) will have its value set to the value of that named property of the record.

If no record is passed, the widget has its value set to `null`.

To strictly match by the `name` property, configure [strictRecordMapping](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-strictRecordMapping) as `true`.

When fields loaded from this record are changed by user input, the [hasChanges](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-hasChanges) property will be set.

[strictRecordMapping](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-strictRecordMapping)
Specify `true` to match fields by their `name` property only when assigning a [record](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-record), without falling back to `ref`.

[focusDescendant](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-focusDescendant)
Can be set to `true` to make a focus of a focusable encapsulating element relay focus down into a focusable child. This is normally `false` to allow mousedown to begin text selection in Popups.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-rendition)
Either a default `rendition` to apply to all child widgets, or a map of renditions keyed by child widget `type`.

```
// Mixed types, use object form:
new Container({
  rendition : {
    text   : 'outlined',
    button : 'raised'
  },
  items : [
    { type : 'text', label : 'Name' },
    { type : 'button', text : 'Save' }
  ]
});

// Single type, can use string form:
new Container({
  rendition : 'outlined',
  items : [
    { type : 'button', text : 'Save' },
    { type : 'button', text : 'Cancel' }
  ]
});
```

[gridColumns](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-gridColumns)
Number of columns to use in a grid layout. Applied as `grid-template-columns: repeat(n, auto)`. Also applies the `b-columns` CSS class to the container.

[initialItems](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-initialItems)
This property is `true` until the container's initial `items` config has been processed. This property is set to `false` by the `updateItems` method.

[firstItem](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-firstItem)
Returns the first widget in this Container.

[lastItem](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-lastItem)
Returns the last widget in this Container.

[items](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-items)
A property, which, when _read_, returns an array of the child items of this container in rendered order.

This property may also be _set_ to change the child items of the container. Just as in the [initial items configuration](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items), the new value may either be an array of Widgets/Widget configs or an object.

If specified as an Object, the property names are used as the child Widget's [ref](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref) name, and the value is the child Widget/Widget config.

When setting this, any items which are _only_ in the outgoing child items which were created by this container from raw config objects are destroyed.

Usage patterns:

```
myContainer.items = {
    name : {
        type  : 'textfield',
        label : 'User name'
    },
    age : {
        type  : 'numberfield',
        label : 'User age'
    }
};
```

or

```
myContainer.items = [{
    ref   : 'name',
    type  : 'textfield',
    label : 'User name'
},
    ref   : 'age',
    type  : 'numberfield',
    label : 'User age'
}];
```

[visibleChildCount](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-visibleChildCount)
The number of _visible_ child items shown in this Container.

[widgetMap](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-widgetMap)
An object which contains a map of descendant widgets keyed by their [ref](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref). All descendant widgets will be available in the `widgetMap`.

[hasChanges](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-hasChanges)
Returns `true` if any of the fields in this container have been changed since the container was [loaded with a record](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-record).

Note that this value does not update during typing. The field's `change` event which is triggered when the field is blurred causes this to be updated.

For example when processing a "close" button click, this value will be in its correct state.

[values](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-values)
Retrieves or sets all values from/to contained widgets.

The property set or read from a contained widget is its [defaultBindProperty](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-defaultBindProperty).

This defaults to the `value` for fields.

You may add child widgets which may accept and yield a value to/from another property, such as a `Button` having its [href](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-href) set.

Accepts and returns a map, using [name](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-name), [ref](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref) or [id](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-id) (in that order) as keys.

```
const container = new Container({
    appendTo : document.body,
    items    : {
        firstName : {
            type : 'textfield
        },
        surName : {
            type : 'textfield
        }
        saveButton : {
            type                : 'button',
            text                : 'Save',
            defaultBindProperty : 'href'
            href                : '#'
        }
    }
});

container.values = {
    firstName  : 'Clark',
    surname    : 'Kent',
    saveButton : '#save-route'
};
```

[isSettingValues](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-isSettingValues)
Returns `true` if currently setting values. Allow fields to change highlighting to distinguishing between initially setting values and later on changing values.

[isValid](https://bryntum.com/docs/gantt/api/Core/widget/Container#property-isValid)
Returns `true` if all contained fields are valid, otherwise `false`

## Functions

Functions are methods available for calling on the class

[getPositionableLocation](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-getPositionableLocation)
Returns a 2-element array of `[parentElement, insertBefore]` that specifies where in the DOM to insert a child item based on its [positionable](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-positionable) config value.

[getAt](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-getAt)
Returns the widget at the specified `index` in this Container.

[remove](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-remove)
Removes the passed child/children from this Container.

[removeAll](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-removeAll)
Removes all children from this Container.

[add](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-add)
Appends the passed widget / widgets or config(s) describing widgets to this Container.

If the widgets specify a `weight`, they are inserted at the correct index compared to the existing items weights.

[insert](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-insert)
Inserts the passed widget into this Container at the specified position.

[onFieldChange](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-onFieldChange)
A function called by descendant widgets after they trigger their 'change' event, in reaction to field changes. By default, implements the functionality for the `autoUpdateRecord` config.

[setValues](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-setValues)
Sets values into descendant fields/widgets.

Accepts either a data Model instance or a plain object whose keys map to field names/refs/ids. The second parameter is passed through to child widgets so they can customize how they resolve and assign their value (mirrors previous internal usage).

Change tracking (dirty state) is now managed here.

When called, existing dirty state is cleared and a new baseline of `initialValues` is captured.

[resetValues](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-resetValues)
Resets field values and dirty tracking.

* Calling with no arguments restores the values captured at the last clean `setValues` call (i.e. the baseline established when `setValues(...)` ran, typically via setting a [record](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-record)).
* Calling with an object applies those values and establishes a new clean baseline.

[getWidgetById](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-getWidgetById)
Returns a directly contained widget by id

[processWidgetConfig](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-processWidgetConfig)
This function is called prior to creating widgets, override it in subclasses to allow containers to modify the configuration of each widget.

When adding a widget to a container hierarchy, each parent containers' `processWidgetConfig` will be called.

Returning `false` from the function prevents the widget from being added at all.

[setupWidgetConfig](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-setupWidgetConfig)
This method combines container [defaults](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-defaults)

[createWidget](https://bryntum.com/docs/gantt/api/Core/widget/Container#function-createWidget)
This function converts a Widget config object into a Widget.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeSetRecord](https://bryntum.com/docs/gantt/api/Core/widget/Container#event-beforeSetRecord)
Fired before this container will load record values into its child fields. This is useful if you want to modify the UI before data is loaded (e.g. set some input field to be readonly)

[dirtyStateChange](https://bryntum.com/docs/gantt/api/Core/widget/Container#event-dirtyStateChange)
Fires when a field is mutated and the state of the [hasChanges](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-hasChanges) property changes
