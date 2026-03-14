# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/EventHelper.md

# [EventHelper](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper)

Utility methods for dealing with Events, normalizing Touch/Pointer/Mouse events.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[eventNameMap](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#property-eventNameMap)
DOM event to trigger name mapping.

[longPressTime](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#property-longPressTime-static)
The time in milliseconds for a `taphold` gesture to trigger a `contextmenu` event.

[dblClickTime](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#property-dblClickTime-static)
The time in milliseconds within which a second touch tap event triggers a `dblclick` event.

## Functions

Functions are methods available for calling on the class

[copyEvent](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-copyEvent-static)
For use when synthesizing events from native DOM events. Copies valid properties from the passed event into the destination object;

[getXY](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-getXY-static)
Returns the `[x, y]` coordinates of the event in the viewport coordinate system.

[getDistanceBetween](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-getDistanceBetween-static)
Returns the pixel distance between two mouse/touch/pointer events.

[getPagePoint](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-getPagePoint-static)
Returns a [Point](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle/Point) which encapsulates the `pageX/Y` position of the event. May be used in [Rectangle](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle) events.

[getClientPoint](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-getClientPoint-static)
Returns a [Point](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle/Point) which encapsulates the `clientX/Y` position of the event. May be used in [Rectangle](https://bryntum.com/docs/gantt/api/#Core/helper/util/Rectangle) events.

[addListener](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-addListener-static)
Add a listener or listeners to an element The `options` parameter allows supplying options for the listener(s), for available options see [ElementListenerConfig](https://bryntum.com/docs/gantt/api/#Core/helper/EventHelper#typedef-ElementListenerConfig).

[on](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-on-static)
Adds a listener or listeners to an element. all property names other than the options listed below are taken to be event names, and the values as handler specs.

A handler spec is usually a function reference or the name of a function in the `thisObj` option.

But a handler spec may also be an options object containing a `handler` property which is the function or function name, and local options, including `element` and `thisObj` which override the top level options.

The `options` parameter allows supplying options for the listener(s), for available options see [ElementListenerConfig](https://bryntum.com/docs/gantt/api/#Core/helper/EventHelper#typedef-ElementListenerConfig).

Usage example

```
construct(config) {
    super.construct(config);

    // Add auto detaching event handlers to this Widget's reference elements
    EventHelper.on({
        element : this.iconElement,
        click   : '_handleIconClick',
        thisObj : this,
        contextmenu : {
            element : document,
            handler : '_handleDocumentContextMenu'
        }
    });
}
```

The `click` handler on the `iconElement` calls `this._handleIconClick`.

The `contextmenu` handler is added to the `document` element, but the `thisObj` is defaulted in from the top `options` and calls `this._handleDocumentContextMenu`.

Note that on touch devices, `dblclick` and `contextmenu` events are synthesized. Synthesized events contain a `browserEvent` property containing the final triggering event of the gesture. For example a synthesized `dblclick` event would contain a `browserEvent` property which is the last `touchend` event. A synthetic `contextmenu` event will contain a `browserEvent` property which the longstanding `touchstart` event.

[addElementListener](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-addElementListener-static)
Used internally to add a single event handler to an element.

[removeEventListener](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-removeEventListener-static)
Used internally to remove a single event handler from an element.

[onTransitionEnd](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-onTransitionEnd-static)
Calls a callback when the described animation completes.

[waitForTransitionEnd](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-waitForTransitionEnd-static)
Waits for the described animation completes.

[createDblClickWrapper](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-createDblClickWrapper-static)
Private function to wrap the passed function. The returned wrapper function to be used as a `touchend` handler which will call the passed function passing a fabricated `dblclick` event if there is a `click` within 300ms.

[toSpecialKey](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-toSpecialKey-static)
Handles various inputs to figure out the name of the special key of the event.

```
EventHelper.toSpecialKey('ctrl') // 'ctrlKey'
EventHelper.toSpecialKey(true)   // 'ctrlKey'
EventHelper.toSpecialKey(false)  // false
EventHelper.toSpecialKey('foo')  // false
```

[specialKeyFromEventKey](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#function-specialKeyFromEventKey-static)
If keyup event is triggered when special key is pressed, we don't get special key value from properties like `ctrlKey`. Instead we need to read `event.key`. That property uses full name and we use abbreviations, so we need to convert the key.

## Typedefs

Typedefs are type definitions for the class

[ElementListenerConfig](https://bryntum.com/docs/gantt/api/Core/helper/EventHelper#typedef-ElementListenerConfig)
