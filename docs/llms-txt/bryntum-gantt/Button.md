# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Button.md

# [Button](https://bryntum.com/docs/gantt/api/Core/widget/Button)

Button widget, wraps and styles a regular `<button>` element. Can display text and icon and also allows specifying button [color](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-color). Supports different appearances, by setting [rendition](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-rendition) to one of:

* 'text' - Flat appearance with text only, no background or border
* 'outlined' - Transparent button with border
* 'tonal' - Flat appearance with "soft" background color
* 'filled' - Flat appearance with stronger background color
* 'elevated' - Raised appearance

```
// Green button with text and icon
const button = new Button({
    appendTo : document.body,
    icon    : 'fa-plus-circle',
    text    : 'Add',
    color   : 'b-green',
    onClick : () => {}
});
```

Button with menu
----------------

Buttons can also have a menu that is shown on click, or on click or hover of only the menu icon part of the button (if [split](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-split) is set):

```
const button = new Button({
    appendTo : document.body,
    icon    : 'fa-chart',
    menu    : {
        items : [
            {
                text : 'Click me',
                onItem : () => console.log('I was clicked')
            }
        ]
    }
});
```

Click handling in a complex widget
----------------------------------

In the case of a button which is part of a complex UI within a larger Bryntum widget, use of the string form for handlers is advised. A handler which starts with `'up.'` will be resolved by looking in owning widgets of the Button. For example a Calendar may have handlers for its buttons configured in:

```
new Calendar({
    appendTo : document.body,
    project  : myProjectConfig,
    sidebar  : {
        items : {
            addNew : {
                weight  : 0,
                text    : 'New',

                // The Button's ownership will be traversed to find this function name.
                // It will be called on the outermost Calendar widget.
                onClick : 'up.onAddNewClick'
            }
        }
    },

    // Button handler found here
    onAddNewClick() {
        // Use Calendar API which creates event in the currently active date
        this.createEvent();
    }
});
```

This class may be operated by the keyboard. `Space` presses the button and invokes any click handler, and `ArrowDown` activates any configured [menu](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-menu).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[icon](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-icon)
Button icon class, a developer-defined CSS class string which results in the desired icon.

Note that demos use [Font Awesome](https://bryntum.com/docs/gantt/api/https://fontawesome.com/cheatsheet) icons, but no icons are actually built in.

This may also be configured as the URL of an image (Detected by searching for a `/` in the string).

[menuIcon](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-menuIcon)
The menu icon class to show when the button has a menu. Set to `null` to not show a menu icon.

Note that demos use [Font Awesome](https://bryntum.com/docs/gantt/api/https://fontawesome.com/cheatsheet) icons, but no icons are actually built in.

[pressedIcon](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-pressedIcon)
Icon class for the buttons pressed state, a developer-defined CSS class string which results in the desired icon. Only applies to toggle buttons

Note that demos use [Font Awesome](https://bryntum.com/docs/gantt/api/https://fontawesome.com/cheatsheet) icons, but no icons are actually built in.

```
new Button({
   // Icon for unpressed button
   icon        : 'fa-wine-glass',

   // Icon for pressed button
   pressedIcon : 'fa-wine-glass-alt',

   // Only applies to toggle buttons
   toggleable  : true
});
```

[pressedCls](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-pressedCls)
A CSS class to add to the pressed state of the button. A `b-pressed` CSS class is always added, when a button is pressed.

[iconAlign](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-iconAlign)
Button icon alignment. May be `'start'` or `'end'`. Defaults to `'start'`

[behaviorType](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-behaviorType)
The button behavioral type, will be applied as a `type` attribute to this button's element.

[text](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-text)
The button's text. You can also supply a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) or an array of DomConfigs for complex button content.

[toggleable](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-toggleable)
Enabled toggling of the button (stays pressed when pressed).

[pressed](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-pressed)
Initially pressed or not. Only applies with `toggleable = true`.

```
const toggleButton = new Button({
   toggleable : true,
   text : 'Enable cool action'
});
```

[toggleGroup](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-toggleGroup)
Indicates that this button is part of a group where only one button can be pressed. Assigning a value also sets `toggleable` to `true`.

When part of a [ButtonGroup](https://bryntum.com/docs/gantt/api/#Core/widget/ButtonGroup), you can set [toggleGroup](https://bryntum.com/docs/gantt/api/#Core/widget/ButtonGroup#config-toggleGroup) on it as an alternative to on each button. This config can then be used to override that value if needed.

```
const yesButton = new Button({
   toggleGroup : 'yesno',
   text        : 'Yes'
});

const noButton = new Button({
   toggleGroup : 'yesno',
   text        : 'No'
});
```

[supportsPressedClick](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-supportsPressedClick)
Set to `true` to perform action on clicking the button if it's already pressed and belongs to a [toggleGroup](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-toggleGroup).

[menu](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-menu)
A submenu configuration object, or an array of MenuItem configuration objects from which to create a submenu which is shown when this button is pressed.

Note that this does not have to be a Menu. The `type` config can be used to specify any widget as the submenu.

May also be specified as a fully instantiated [floating Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-floating) such as a [Popup](https://bryntum.com/docs/gantt/api/#Core/widget/Popup).

[href](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-href)
If provided, turns the button into a link.

Not compatible with the [adopt](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-adopt) config.

[target](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-target)
The `target` attribute for the [href](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-href) config

[tabIndex](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-tabIndex)
The tab index of the button, or `null` for natural tab order (recommended). Setting to `0` is equivalent to natural tab order, but is unnecessary for buttons since they are naturally tabbable (i.e., accessible via the TAB key). Setting to `-1` disables tabbability but allows for focus to be set to the element programmatically.

From [MDN documentation](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex):

**Warning**: You are recommended to only use `0` and `-1` as tabindex values. Avoid using tabindex values greater than 0 and CSS properties that can change the order of focusable HTML elements ([Ordering flex items](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Ordering_flex_items)). Doing so makes it difficult for people who rely on using keyboard for navigation or assistive technology to navigate and operate page content. Instead, write the document with the elements in a logical sequence.

[split](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-split)
Set to `true` to create a split button. A split button has a main action and a dropdown arrow to show a menu.

The menu only shows when the arrow is clicked, not when the main button is clicked.

Set to `'mouseover'` to show the menu when _hovering_ the arrow part of the button as well as when toggling by clicking it.

Set to `'hover'` to show the menu only when _hovering_ the arrow part of the button - the menu will hide when the mouse leaves the icon to outside of the icon or menu.

The button will only toggle its [pressed](https://bryntum.com/docs/gantt/api/#Core/widget/Button#property-pressed) state and action its `click` handler when the main part of the button is clicked.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/Button#config-rendition)
Predefined style to use for the button. Possible values are:

* `'elevated'` - Raised button with box-shadow
* `'filled'` - Filled with the primary color
* `'tonal'` - Filled with a faded shade of the primary color
* `'outlined'` - Outlined with borders and pale or transparent fill
* `'text'` - Transparent text-only button

The supplied value will be part of the button's class list, as `b-button-{rendition}`.

If no value is provided, a default rendition will be determined based on the theme.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isButton](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-isButton)
Identifies an object as an instance of [Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button) class, or subclass thereof.

[isButton](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-isButton-static)
Identifies an object as an instance of [Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button) class, or subclass thereof.

[icon](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-icon)
Button icon class, a developer-defined CSS class string which results in the desired icon.

Note that demos use [Font Awesome](https://bryntum.com/docs/gantt/api/https://fontawesome.com/cheatsheet) icons, but no icons are actually built in.

This may also be configured as the URL of an image (Detected by searching for a `/` in the string).

[menuIcon](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-menuIcon)
The menu icon class to show when the button has a menu. Set to `null` to not show a menu icon.

Note that demos use [Font Awesome](https://bryntum.com/docs/gantt/api/https://fontawesome.com/cheatsheet) icons, but no icons are actually built in.

[pressedIcon](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-pressedIcon)
Icon class for the buttons pressed state, a developer-defined CSS class string which results in the desired icon. Only applies to toggle buttons

Note that demos use [Font Awesome](https://bryntum.com/docs/gantt/api/https://fontawesome.com/cheatsheet) icons, but no icons are actually built in.

```
new Button({
   // Icon for unpressed button
   icon        : 'fa-wine-glass',

   // Icon for pressed button
   pressedIcon : 'fa-wine-glass-alt',

   // Only applies to toggle buttons
   toggleable  : true
});
```

[pressedCls](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-pressedCls)
A CSS class to add to the pressed state of the button. A `b-pressed` CSS class is always added, when a button is pressed.

[iconAlign](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-iconAlign)
Button icon alignment. May be `'start'` or `'end'`. Defaults to `'start'`

[behaviorType](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-behaviorType)
The button behavioral type, will be applied as a `type` attribute to this button's element.

[text](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-text)
The button's text. You can also supply a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) or an array of DomConfigs for complex button content.

[toggleable](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-toggleable)
Enabled toggling of the button (stays pressed when pressed).

[pressed](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-pressed)
Initially pressed or not. Only applies with `toggleable = true`.

```
const toggleButton = new Button({
   toggleable : true,
   text : 'Enable cool action'
});
```

[toggleGroup](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-toggleGroup)
Indicates that this button is part of a group where only one button can be pressed. Assigning a value also sets `toggleable` to `true`.

When part of a [ButtonGroup](https://bryntum.com/docs/gantt/api/#Core/widget/ButtonGroup), you can set [toggleGroup](https://bryntum.com/docs/gantt/api/#Core/widget/ButtonGroup#config-toggleGroup) on it as an alternative to on each button. This config can then be used to override that value if needed.

```
const yesButton = new Button({
   toggleGroup : 'yesno',
   text        : 'Yes'
});

const noButton = new Button({
   toggleGroup : 'yesno',
   text        : 'No'
});
```

[menu](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-menu)
Returns the instantiated menu widget as configured by [menu](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-menu).

[href](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-href)
If provided, turns the button into a link.

Not compatible with the [adopt](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-adopt) config.

[target](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-target)
The `target` attribute for the [href](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-href) config

[tabIndex](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-tabIndex)
The tab index of the button, or `null` for natural tab order (recommended). Setting to `0` is equivalent to natural tab order, but is unnecessary for buttons since they are naturally tabbable (i.e., accessible via the TAB key). Setting to `-1` disables tabbability but allows for focus to be set to the element programmatically.

From [MDN documentation](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex):

**Warning**: You are recommended to only use `0` and `-1` as tabindex values. Avoid using tabindex values greater than 0 and CSS properties that can change the order of focusable HTML elements ([Ordering flex items](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Ordering_flex_items)). Doing so makes it difficult for people who rely on using keyboard for navigation or assistive technology to navigate and operate page content. Instead, write the document with the elements in a logical sequence.

[split](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-split)
Set to `true` to create a split button. A split button has a main action and a dropdown arrow to show a menu.

The menu only shows when the arrow is clicked, not when the main button is clicked.

Set to `'mouseover'` to show the menu when _hovering_ the arrow part of the button as well as when toggling by clicking it.

Set to `'hover'` to show the menu only when _hovering_ the arrow part of the button - the menu will hide when the mouse leaves the icon to outside of the icon or menu.

The button will only toggle its [pressed](https://bryntum.com/docs/gantt/api/#Core/widget/Button#property-pressed) state and action its `click` handler when the main part of the button is clicked.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/Button#property-rendition)
Predefined style to use for the button. Possible values are:

* `'elevated'` - Raised button with box-shadow
* `'filled'` - Filled with the primary color
* `'tonal'` - Filled with a faded shade of the primary color
* `'outlined'` - Outlined with borders and pale or transparent fill
* `'text'` - Transparent text-only button

The supplied value will be part of the button's class list, as `b-button-{rendition}`.

If no value is provided, a default rendition will be determined based on the theme.

## Functions

Functions are methods available for calling on the class

[eachWidget](https://bryntum.com/docs/gantt/api/Core/widget/Button#function-eachWidget)
Iterate over all widgets owned by this widget and any descendants.

_Note_: Due to this method aborting when the function returns `false`, beware of using short form arrow functions. If the expression executed evaluates to `false`, iteration will terminate.

_Due to the [menu](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-menu) config being a lazy config and only being converted to be a `Menu` instance just before it's shown, the menu will not be part of the iteration before it has been shown once_.

[onInternalClick](https://bryntum.com/docs/gantt/api/Core/widget/Button#function-onInternalClick)
Triggers events when user clicks button

[toggle](https://bryntum.com/docs/gantt/api/Core/widget/Button#function-toggle)
Toggle button state (only use with toggleable = true)

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeShowMenu](https://bryntum.com/docs/gantt/api/Core/widget/Button#event-beforeShowMenu)
This event is triggered when the button's menu is about to be shown.

[toggle](https://bryntum.com/docs/gantt/api/Core/widget/Button#event-toggle)
Fires when the button is toggled via a UI interaction (the [pressed](https://bryntum.com/docs/gantt/api/#Core/widget/Button#property-pressed) state is changed). If the button is part of a [toggleGroup](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-toggleGroup) and you need to process the pressed button only, consider using [click](https://bryntum.com/docs/gantt/api/#Core/widget/Button#event-click) event or [action](https://bryntum.com/docs/gantt/api/#Core/widget/Button#event-action) event.

[click](https://bryntum.com/docs/gantt/api/Core/widget/Button#event-click)
Fires when the button is clicked

[action](https://bryntum.com/docs/gantt/api/Core/widget/Button#event-action)
Fires when the default action is performed (the button is clicked)

[beforeToggle](https://bryntum.com/docs/gantt/api/Core/widget/Button#event-beforeToggle)
Fires before the button is toggled (the [pressed](https://bryntum.com/docs/gantt/api/#Core/widget/Button#property-pressed) state is changed). If the button is part of a [toggleGroup](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-toggleGroup) and you need to process the pressed button only, consider using [click](https://bryntum.com/docs/gantt/api/#Core/widget/Button#event-click) event or [action](https://bryntum.com/docs/gantt/api/#Core/widget/Button#event-action) event. Return `false` to prevent the toggle to the new pressed state.
