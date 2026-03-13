# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Tooltip.md

# [Tooltip](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip)

A simple Tooltip class that offers a flexible way to show a popover when hovering or clicking elements. The easiest way of assigning a tooltip to a widget is by setting [tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-tooltip), see example below.

```
new Button({
    text    : 'Hover me',
    tooltip : 'Click me and you won\'t believe what happens next'
});
```

By default, tooltips of widgets use a singleton Tooltip instance which may be accessed from the `[Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget)` class under the name `Widget.tooltip`. This is configured according to the config object on pointer over.

To request a separate instance be created just for this widget, add `newInstance : true` to the configuration:

```
new Button {
    text    : 'Hover me',
    tooltip : {
        html        : 'Click me and you won\'t believe what happens next',
        newInstance : true
    }
});
```

You can ask for the singleton instance to display configured tips for your own DOM structure using `data-btip` element attributes:

```
<button class="my-button" data-btip="Contextual help for my button" data-btip-scroll-action="realign">Hover me</button>
```

Showing async content
---------------------

To load remote content into a simple tooltip, just load your data in the `beforeShow` listener (but ensure that the [activeTarget](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#property-activeTarget) is the same when the data arrives)

```
new Tooltip({
    listeners : {
        beforeShow : ({ source : tip }) => {
            tip.html = AjaxHelper.get('someurl').then(response => response.text());
        }
    }
});
```

Showing a tooltip for multiple targets
--------------------------------------

If you have multiple targets that should show a tooltip when hovered over, look at [forSelector](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-forSelector) and [getHtml](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-getHtml).

```
new Tooltip({
    forSelector : 'img.avatar',
    getHtml     : ({ source : tip, activeTarget }) => {
        return activeTarget.dataset.name;
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoHide](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-autoHide)
By default, a Tooltip is transient, and will [hide](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#function-hide) when the mouse exits the target element. Configure as `false` to make a Tooltip non-transient.

[autoClose](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-autoClose)
By default, a Tooltip is transient, and will [hide](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#function-hide) when the user clicks or taps outside its widget. Configure as `false` to make a Tooltip non-transient when user clicks outside it.

If you would like the Tooltip to stay visible when mouse leaves the Tooltip target, please see {#config-autoHide}.

[mouseOffsetX](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-mouseOffsetX)
Horizontal offset from mouse when [anchorToTarget](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-anchorToTarget) is `false`.

Direction independent, the value is internally flipped (by multiplying it with -1) for RTL.

[mouseOffsetY](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-mouseOffsetY)
Vertical offset from mouse when [anchorToTarget](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-anchorToTarget) is `false`

[getHtml](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-getHtml)
A method, or the _name_ of a method called to update the tooltip's content when the cursor is moved over a target. It receives one argument containing context about the tooltip and show operation. The function should return a string, or a Promise yielding a string.

```
new Grid({
    title    : 'Client list',
    appendTo : myElement,
    store    : myStore,
    columns  : myColumns,
    tbar     : {
        items : {
            text : 'Reload,
            tooltip : {
                // Will look in ownership hierarchy for the method
                // which will be found on the grid.
                getHtml : 'up.getReloadButtonTip'
            }
        }
    },
    getReloadButtonTip() {
        return `Reload ${this.title}`;
    }
});
```

[forElement](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-forElement)
DOM element to attach tooltip to. By default, the mouse entering this element will kick off a timer (see [hoverDelay](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-hoverDelay)) to show itself.

If the [forSelector](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-forSelector) is specified, then mouse entering matching elements within the `forElement` will trigger the show timer to start.

Note that when moving from matching element to matching element within the `forElement`, the tooltip will remain visible for [hideDelay](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-hideDelay) milliseconds after exiting one element, so that rapidly entering another matching element will not cause hide+show flicker. To prevent this behaviour configure with `hideDelay: 0`.

[trackMouse](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-trackMouse)
By default, once a tooltip is shown aligned as requested, it stays put.

Setting this to `true` causes the tooltip to be aligned by the mouse, offset by `[[mouseOffsetX](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-mouseOffsetX), [mouseOffsetY](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-mouseOffsetY)]` and keeps the tooltip aligned to the mouse maintaining the configured offsets as the mouse moves within its activating element.

[updateContentOnMouseMove](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-updateContentOnMouseMove)
By default, a tooltip displays static content. In the Scheduler however, there are plenty of uses cases when the tip content is based on the current mouse position (dragging events, resizing events, schedule hover tip, drag creation of events etc). Set to `true` to update contents on mouse movement.

[forSelector](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-forSelector)
A CSS selector which targets child elements of the [forElement](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-forElement) that should produce a tooltip when hovered over.

[hideOnDelegateChange](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-hideOnDelegateChange)
By default, when moving rapidly from target to target, if, when mouseovering a new target, the tip is still visible, the tooltip does not hide, it remains visible, but updates its content however it is configured to do so.

Configure `hideOnDelegateChange : true` to have the tip hide, and then trigger a new show delay upon entry of a new target while still visible.

[anchorToTarget](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-anchorToTarget)
Set to `true` to anchor tooltip to the triggering target. If set to `false`, the tooltip will align to the mouse position. When set to `false`, it will also set `anchor: false` to hide anchor arrow.

[showOnHover](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-showOnHover)
Show on hover

[hoverDelay](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-hoverDelay)
The amount of time to hover before showing

[autoShow](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-autoShow)
Show immediately when created

[dismissDelay](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-dismissDelay)
The time (in milliseconds) that the Tooltip should stay visible for when it shows over its target. If the tooltip is anchored to its target, then moving the mouse during this time resets the timer so that the tooltip will remain visible.

Defaults to `0` which means the Tooltip will persist until the mouse leaves the target.

[hideDelay](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-hideDelay)
The time (in milliseconds) for which the Tooltip remains visible when the mouse leaves the target.

May be configured as `false` to persist visible after the mouse exits the target element. Configure it as 0 to always retrigger `hoverDelay` even when moving mouse inside `fromElement`

[loadingMsg](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-loadingMsg)
The message to show while an async tooltip is fetching its content.

[allowOver](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-allowOver)
Keep the tooltip open if user moves the mouse over it.

If this is _not_ explicitly configured as `false`, then this is automatically set when there are any visible, interactive child items added such as [tools](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-tools), or [items](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-items) which are interactive such as buttons or input fields.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#config-rendition)
Predefined style to use for the tooltip. Possible values are:

* `'plain'` - Compact rendition for simple text
* `'rich'` - Rich rendition for complex content

The supplied value will be part of the tooltip's class list, as `b-{rendition}-tooltip`.

When left out, the rendition to use will be determined by the content of the tooltip.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTooltip](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#property-isTooltip)
Identifies an object as an instance of [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip) class, or subclass thereof.

[isTooltip](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#property-isTooltip-static)
Identifies an object as an instance of [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip) class, or subclass thereof.

[hoverDelay](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#property-hoverDelay)
The amount of time to hover before showing

[activeTarget](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#property-activeTarget)
The HTML element that triggered this Tooltip to show

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#property-rendition)
Predefined style to use for the tooltip. Possible values are:

* `'plain'` - Compact rendition for simple text
* `'rich'` - Rich rendition for complex content

The supplied value will be part of the tooltip's class list, as `b-{rendition}-tooltip`.

When left out, the rendition to use will be determined by the content of the tooltip.

[html](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#property-html)
Get/set the HTML to display. When specifying HTML, this widget's element will also have `b-html` added to its classList, to allow targeted styling. To create async tooltip and show the [loadingMsg](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip#config-loadingMsg), see code below: For example:

```
new Tooltip({
    listeners : {
        beforeShow : ({ source : tip }) => {
            tip.showAsyncMessage();
            AjaxHelper.get('someurl').then(response => tip.html = 'Done!');
        }
    }
});
```

[triggeredByEvent](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#property-triggeredByEvent)
The DOM event that triggered this tooltip to show

[currentOverElement](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#property-currentOverElement-static)
Updated dynamically with the current element that the mouse is over. For use when showing a Tooltip from code which is not triggered by a pointer event so that a tooltip can be positioned.

[showOverflow](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#property-showOverflow-static)
Set this to true to have the [shared tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-tooltip-static) pop up to show the full text for elements which have overflowing text and have `text-overflow:ellipsis`.

## Functions

Functions are methods available for calling on the class

[showAsyncMessage](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#function-showAsyncMessage)
Shows a spinner and a message to indicate an async flow is ongoing

[abortDelayedHide](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#function-abortDelayedHide)
Stops both timers which may hide this tooltip, the one which counts down from mouseout and the one which counts down from mouseover show for dismissDelay ms

[onMouseMove](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#function-onMouseMove)
Mouse move event listener which updates tooltip

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeShow](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#event-beforeShow)
Triggered before tooltip widget is shown. Return `false` to prevent the action.

[pointerOver](https://bryntum.com/docs/gantt/api/Core/widget/Tooltip#event-pointerOver)
Triggered when a mouseover event is detected on a potential target element. Return false to prevent the action
