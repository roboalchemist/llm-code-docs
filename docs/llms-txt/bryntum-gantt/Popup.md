# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Popup.md

# [Popup](https://bryntum.com/docs/gantt/api/Core/widget/Popup)

A floating Popup widget, which can contain child [widgets](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items) or plain html. Serves as the base class for Menu / Tooltip.

When it contains focus, the `Escape` key [closes](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-closeAction) the picker. When it hides, focus is reverted to the element from which it entered the Popup, or, if that is no longer focusable, a close relative of that element.

```
const popup = new Popup({
  forElement : document.querySelector('button'),
  items      : {
    text : { type : 'text', placeholder: 'Text' },
    button : { type: 'button', text: 'Okay', style: 'width: 100%', color: 'b-orange'}
  }
});
```

Dragging & Resizing
-------------------

Popups can be resized and dragged around the screen. To enable resizing, set the [resizable](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-resizable) config to `true` or an object with specific options. To enable dragging, set the [draggable](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-draggable) config to `true`.

For example:

```
const popup = new Popup({
   draggable : true,
   resizable : {
      handles : {
         top  : false,
         minWidth : 100
      }
   }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoShow](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-autoShow)
Auto show flag for Popup. If truthy then Popup is shown automatically upon hover.

[autoClose](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-autoClose)
By default, a Popup is transient, and will [close](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#function-close) when the user clicks or taps outside its owned widgets and when focus moves outside its owned widgets.

**Note**: [Modal](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-modal) popups won't [close](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#function-close) when focus moves outside even if autoClose is `true`.

Configure as `false` to make a Popup non-transient.

[showOnClick](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-showOnClick)
Show popup when user clicks the element that it is anchored to. Cannot be combined with showOnHover. Can also be provided as the button number (0: main button, 2: right button).

[forElement](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-forElement)
DOM element to attach popup.

[draggable](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-draggable)
Set to `false` to prevent dragging the popup element.

[closeAction](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-closeAction)
The action to take when calling the [close](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#function-close) method. By default, the popup is hidden.

This may be set to `'destroy'` to destroy the popup upon close.

[trapFocus](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-trapFocus)
By default, tabbing within a Popup is circular - that is it does not exit. Configure this as `false` to allow tabbing out of the Popup.

[focusOnToFront](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-focusOnToFront)
By default a Popup is focused when it is shown. Configure this as `false` to prevent automatic focus on show.

[closable](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-closable)
Show a tool in the header to close this Popup. The tool is available in the [tools](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Toolable#property-tools) object under the name `close`. It uses the CSS class `b-popup-close` to apply a default close icon. This may be customized with your own CSS rules.

[maximizable](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-maximizable)
Show a tool in the header to maximize this popup

[modal](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-modal)
Optionally show an opaque mask below this Popup when shown. Configure this as `true` to show the mask.

When a Popup is modal, it defaults to being [centered](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-centered). Also, it won't [close](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#function-close) when focus moves outside even if [autoClose](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-autoClose) is `true`.

The default action is to focus the popup.

Usage:

```
new Popup({
    title  : 'I am modal',
    modal  : {
        closeOnMaskTap : true
    },
    height : 100,
    width  : 200
});
```

[maximized](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-maximized)
Set to `true` to make this widget take all available space in the visible viewport.

[closeOnEscape](https://bryntum.com/docs/gantt/api/Core/widget/Popup#config-closeOnEscape)
Close popup when `ESC` key is pressed.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPopup](https://bryntum.com/docs/gantt/api/Core/widget/Popup#property-isPopup)
Identifies an object as an instance of [Popup](https://bryntum.com/docs/gantt/api/#Core/widget/Popup) class, or subclass thereof.

[isPopup](https://bryntum.com/docs/gantt/api/Core/widget/Popup#property-isPopup-static)
Identifies an object as an instance of [Popup](https://bryntum.com/docs/gantt/api/#Core/widget/Popup) class, or subclass thereof.

[maximized](https://bryntum.com/docs/gantt/api/Core/widget/Popup#property-maximized)
Set to `true` to make this widget take all available space in the visible viewport.

[modalMask](https://bryntum.com/docs/gantt/api/Core/widget/Popup#property-modalMask)
Returns the modal mask element for this Popup correctly positioned just below this Popup.

[modalMask](https://bryntum.com/docs/gantt/api/Core/widget/Popup#property-modalMask-static)
Returns the modal mask element. It does NOT guarantee its placement in the DOM relative to any Popup. To get the modal mask for a particular Popup, use the instance property.

## Functions

Functions are methods available for calling on the class

[close](https://bryntum.com/docs/gantt/api/Core/widget/Popup#function-close)
Performs the configured [closeAction](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-closeAction) upon this popup. By default, the popup hides. The [closeAction](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#config-closeAction) may be configured as `'destroy'`.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeClose](https://bryntum.com/docs/gantt/api/Core/widget/Popup#event-beforeClose)
Fired when the [close](https://bryntum.com/docs/gantt/api/#Core/widget/Popup#function-close) method is called and the popup is not hidden. May be vetoed by returning `false` from a handler.
