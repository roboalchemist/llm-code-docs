# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/panel/PanelCollapserOverlay.md

# [PanelCollapserOverlay](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapserOverlay)

A panel collapse implementation that adds the ability to reveal the collapsed panel as a floating overlay.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoCloseDelay](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapserOverlay#config-autoCloseDelay)
The number of milliseconds to wait once the mouse leaves a [revealed](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-revealed) panel before returning to an unrevealed state. Clicking outside the revealed panel will immediately return the panel to its collapsed state.

This may be disabled by configuring [autoClose.mouseout](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapserOverlay#config-autoClose) as `false`.

If this value is negative, the panel will not automatically recollapse due to the mouse leaving, however, clicks outside the panel will still recollapse it.

If this value is `null`, the panel will not automatically recollapse for either outside clicks or if the mouse leaves the panel.

[autoClose](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapserOverlay#config-autoClose)
By default, the following three events will hide the revealed overlay:

* `mousedown` outside of the revealed overlay
* `mouseout` of the revealed overlay
* `focusout` of the revealed overlay

This can be configured per event type, for example:

```
// Don't hide on mouseout, only on click out
autoClose : {
   mousedown : true,
   mouseout  : false,
   focusout  : false
}
```

Configure as a boolean to apply the same value for all events.

If the `mousedown` property is a selector string, clicks on elements matching that selector will also close the revealed overlay:

```
// Close when clicking outside, but not when clicking grid cells - those should not close the overlay
autoClose : {
   mousedown : ':not(.b-grid-cell)',
   mouseout  : false,
   focusout  : false
}
```

Note that if creating a whitelist using `:not()`, the `:not()` expression must encapsulate your whitelist selector.

If the revealed overlay was shown using the [recollapseTool](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapserOverlay#property-recollapseTool) then moving the mouse outside of the revealed overlay hides the revealed overlay.

Configure this as `false` to disable auto hiding, making overlayed state permanent, and changeable using the [toggleReveal](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapserOverlay#function-toggleReveal) method.

[recollapseTool](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapserOverlay#config-recollapseTool)
The reveal/hide tool which slides the collapsed panel over the top of the UI.

The `type` of this instance should not be changed but the tool instance can be configured in other ways via this config property.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPanelCollapserOverlay](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapserOverlay#property-isPanelCollapserOverlay)
Identifies an object as an instance of [PanelCollapserOverlay](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapserOverlay) class, or subclass thereof.

[isPanelCollapserOverlay](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapserOverlay#property-isPanelCollapserOverlay-static)
Identifies an object as an instance of [PanelCollapserOverlay](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapserOverlay) class, or subclass thereof.

[recollapseTool](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapserOverlay#property-recollapseTool)
The reveal/hide tool which slides the collapsed panel over the top of the UI.

## Functions

Functions are methods available for calling on the class

[toggleReveal](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapserOverlay#function-toggleReveal)
Toggles the revealed state of the Panel to match the passed boolean flag.
