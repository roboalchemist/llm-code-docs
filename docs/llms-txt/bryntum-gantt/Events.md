# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Events.md

# [Events](https://bryntum.com/docs/gantt/api/Core/mixin/Events)

Mix this into another class to enable event handling.

Basic usage
-----------

Listeners can be added either through config:

```
let button = new Button({
  listeners: {
    click: () => {},
    press: () => {},
    ...
  }
});
```

_NOTE_: Do not reuse listeners config object, use new every time:

```
// wrong
let config = { click : () => {} }
new Button({
    listeners : config
})
new Button({
    listeners : config
})
// right
new Button({
    listeners : { click : () => {} }
})
new Button({
    listeners : { click : () => {} }
})
```

Or by calling on()/addListener():

```
let button = new Button();

button.addListener('press', () => {});
// on is an alias for addListener
button.on('click', () => {});
```

This style also accepts multiple listeners in same way as when using config:

```
button.on({
  click: () => {},
  press: () => {},
  ...
});
```

### Handlers as function name

Event handlers may be specified as a function **name**. If a string is specified, it is the name of the function in the `thisObj` object.

If the string begins with `up.`, the owning object's ownership hierarchy (if present) is scanned for an object which implements that function name:

```
new Popup({
    tbar : {
        items : {
            myCombo : {
                type      : 'combo',
                editable  : false,
                label     : 'Type',
                listeners : {
                    // Look in owner chain for this function name
                    change : 'up.onFilterChange'
                },
                items     : [
                    'Event',
                    'Task',
                    'Appointment'
                ]
            }
        }
    },
    items : {
        ...
    },
    onFilterChange({ value }) {
        // Handle event type selection here
    }
});
```

Listener options
----------------

### Once

Listeners can be configured to automatically deregister after first trigger by specifying config option `once`:

```
button.on({
  click: () => {},
  once: true
});
```

### Priority

Specifying priority affects the order in which listeners are called when triggering an event. Higher priorities will be called before lower. Default value is 0.

```
button.on({
  click: this.onClick,
  prio: 1
});
```

### This reference

If desired, you can specify thisObj when configuring listeners. There is no need if you are using arrow functions as listeners, but might be handy in other cases. Of course, you can also use bind to set `this` reference.

```
button.on({
  click: this.onClick,
  thisObj: this
});

// or

button.on({
  click: this.onClick.bind(this)
});
```

### Buffering

By specifying a `buffer` events that fire frequently can be grouped together and delayed. A handler for the event will be called once only, when no new event has been fired during the specified buffer time:

```
button.on({
  click  : this.onClick,
  buffer : 200 // in milliseconds
});
```

In this example, if a user clicked the button 6 times very fast (<200ms between each click), the `this.onClick` handler would be called only once 200 milliseconds after the last click.

### Throttling

Create a "debounced" function which will call on the "leading edge" of a timer period. When first invoked will call immediately, but invocations after that inside its buffer period will be rejected, and _one_ invocation will be made after the buffer period has expired.

This is useful for responding immediately to a first mousemove, but from then on, only calling the action function on a regular timer while the mouse continues to move.

```
button.on({
  click    : this.onClick,
  throttle : 200 // in milliseconds
});
```

In this example, if a user clicked the button 6 times very fast, the `this.onClick` handler would be called once immediately on the first click and a second time 200 milliseconds after the **first** click. So in reality the `click` event handler will be called every 200ms independent of amount of click in a middle, if the event was triggered at least once during the `throttle` timeout.

### Detacher

A convenient way of unregistering events is to use a detacher, a function returned when adding listeners that you call later to deregister them. As of version 1.0, detachable defaults to true.

```
let detacher = button.on({
  click: () => {},
  press: () => {},
  detachable: true
});

// when you want to detach, for example in destroy()
detacher();
```

### Named listeners

Named listeners allow you to define event handlers with a specific `name` linked to the passed `thisObj`. This can be used to easily remove them later.

```
// The name is registered with the thisObj
button.on({
  name    : 'myButtonListeners',
  click   : 'myClickHandler',
  thisObj : this
});
```

And later you can remove them like this:

```
this.detachListeners('myButtonListeners');
```

Note that all listeners registered on that `thisObj` with the specified name on this object will be removed.

### Auto detaching

When listeners are bound to a class instance using `thisObj`, the `thisObj`'s `doDestroy` method is overridden to remove the listeners before calling the overridden doDestroy.

```
class MyClass extends Base {
  construct() {
    let button = new Button({
      listeners: {
        click: () => {},
        thisObj: this
      }
    });
  }

  doDestroy() {
    // clean up stuff
  }
}

let myObj = new MyClass();
// clean up, also removes listeners
myObj.destroy();
```

### On-functions

When mixing Events into another class it can be configured to call on-functions when events are triggered. On-functions are functions named 'onEventName', for example 'onClick', 'onPress' declared on the class triggering the event.

```
// mix Events in with on-functions activated
let button = new Button({
  callOnFunctions: true,

  onClick: () => {}
});

// or add a getter in class declaration
```

Returning `false` from an on-function will prevent triggering listeners for the event.

### Catching all events

By specifying a listener for [catchAll](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#event-catchAll) a function can be notified when any event is triggered:

```
const button = new Button({
   listeners : {
       catchAll(event) {
           // All events on the button will pass through here
       }
   }
});
```

Preventable events
------------------

By returning `false` from a listener for an event documented as `preventable` the action that would otherwise be executed after the event is prevented. These events are usually named `beforeXX`, for example `beforeRemove`, `beforeDragStart` etc.

Note that Angular does not support return values from listeners. Instead, assign to `event.returnValue` as shown in the Angular snippet below

```
taskBoard.on({
    beforeColumnDrag({ columnRecord }) {
        if (columnRecord.locked) {
            return false;
        }
    }
});
```

```
const App = props => {
    function onBeforeColumnDrag({ columnRecord }) {
        if (columnRecord.locked) {
            return false;
        }
    }

    return (
        <>
            <BryntumTaskBoard onBeforeColumnDrag={onBeforeColumnDrag} />
        </>
    )
}
```

```
<bryntum-task-board @beforeColumnDrag="onBeforeColumnDrag" />
```

```
export default {
    methods : {
        onBeforeColumnDrag({ columnRecord }) {
            if (columnRecord.locked) {
                return false;
            }
        }
   }
}
```

```
<bryntum-task-board (onBeforeColumnDrag)="onBeforeColumnDrag({event : $event})"></bryntum-task-board>
```

```
export class AppComponent {
    onBeforeColumnDrag({ event }: { event: any }): void {
        event.returnValue = !event.columnRecord.locked;
    }
 }
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[callOnFunctions](https://bryntum.com/docs/gantt/api/Core/mixin/Events#config-callOnFunctions)
Set to `true` to call onXXX method names (e.g. `onShow`, `onClick`), as an easy way to listen for events.

```
const container = new Container({
    callOnFunctions : true

    onHide() {
         // Do something when the 'hide' event is fired
    }
});
```

[listeners](https://bryntum.com/docs/gantt/api/Core/mixin/Events#config-listeners)
The listener set for this object.

An object whose property names are the names of events to handle, or options which modifiy **how** the handlers are called.

See [addListener](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#function-addListener) for details about the options.

Listeners can be specified in target class config and they will be merged with any listeners specified in the instantiation config. Class listeners will be fired first:

```
class MyStore extends Store({
    static configurable = {
        listeners : {
            myCustomEvent() {
            },
            load : {
                prio : 10000,
                fn() { // this load listener handles things first }
            }
        }
    };
});

let store = new MyStore({
  listeners: {
    load: () => { // This load listener runs after the class's },
    ...
  }
});
```

### Handlers as function name

Object event handlers may be specified as a function **name**. If a string is specified, it is the name of the function in the `thisObj` object.

If the string begins with `up.`, this object's ownership hierarchy (if present) is scanned for an object which implements that function name:

```
new Popup({
    tbar : {
        items : {
            myCombo : {
                type      : 'combo',
                editable  : false,
                label     : 'Type',
                listeners : {
                    // Look in owner chain for this function name
                    change : 'up.onFilterChange'
                },
                items     : [
                    'Event',
                    'Task',
                    'Appointment'
                ]
            }
        }
    },
    items : {
        ...
    },
    onFilterChange({ value }) {
        // Handle event type selection here
    }
});
```

[internalListeners](https://bryntum.com/docs/gantt/api/Core/mixin/Events#config-internalListeners)
Internal listeners, that cannot be removed by the user.

[bubbleEvents](https://bryntum.com/docs/gantt/api/Core/mixin/Events#config-bubbleEvents)
An object where property names with a truthy value indicate which events should bubble up the ownership hierarchy when triggered.

```
const container = new Container({
    items : [
       { type : 'text', bubbleEvents : { change : true }}
    ],

    listeners : {
        change() {
            // Will catch change event from the text field
        }
    }
});
```

[catchEventHandlerExceptions](https://bryntum.com/docs/gantt/api/Core/mixin/Events#config-catchEventHandlerExceptions)
By default, if an event handler throws an exception, the error propagates up the stack and the application state is undefined. Code which follows the event handler will _not_ be executed.

Set this to `true` to catch exceptions thrown by this object's event handlers and continue processing the event. The exception will be rethrown on a zero millisecond timeout, so it will not destroy the stack.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEvents](https://bryntum.com/docs/gantt/api/Core/mixin/Events#property-isEvents)
Identifies an object as an instance of [Events](https://bryntum.com/docs/gantt/api/#Core/mixin/Events) class, or subclass thereof.

[isEvents](https://bryntum.com/docs/gantt/api/Core/mixin/Events#property-isEvents-static)
Identifies an object as an instance of [Events](https://bryntum.com/docs/gantt/api/#Core/mixin/Events) class, or subclass thereof.

[deprecatedEvents](https://bryntum.com/docs/gantt/api/Core/mixin/Events#property-deprecatedEvents-static)
The list of deprecated events as an object, where `key` is an event name which is deprecated and `value` is an object which contains values for [VersionHelper](https://bryntum.com/docs/gantt/api/#Core/helper/VersionHelper#function-deprecate-static):

* product {String} The name of the product;
* invalidAsOfVersion {String} The version where the offending code is invalid (when any compatibility layer is actually removed);
* message {String} Warning message to show to the developer using a deprecated API;

For example:

```
return {
    click : {
        product            : 'Grid',
        invalidAsOfVersion : '1.0.0',
        message            : 'click is deprecated!'
    }
}
```

[callOnFunctions](https://bryntum.com/docs/gantt/api/Core/mixin/Events#property-callOnFunctions)
Set to `true` to call onXXX method names (e.g. `onShow`, `onClick`), as an easy way to listen for events.

```
const container = new Container({
    callOnFunctions : true

    onHide() {
         // Do something when the 'hide' event is fired
    }
});
```

[catchEventHandlerExceptions](https://bryntum.com/docs/gantt/api/Core/mixin/Events#property-catchEventHandlerExceptions)
By default, if an event handler throws an exception, the error propagates up the stack and the application state is undefined. Code which follows the event handler will _not_ be executed.

Set this to `true` to catch exceptions thrown by this object's event handlers and continue processing the event. The exception will be rethrown on a zero millisecond timeout, so it will not destroy the stack.

## Functions

Functions are methods available for calling on the class

[doDestroy](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-doDestroy)
Auto detaches listeners registered from start, if set as detachable

[addListener](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-addListener)
Adds an event listener. This method accepts parameters in the following format:

```
 myObject.addListener({
     thisObj    : this,          // The this reference for the handlers
     eventname2 : 'functionName' // Resolved at invocation time using the thisObj,
     otherevent : {
         fn      : 'handlerFnName',
         once    : true          // Just this handler is auto-removed on fire
     },
     yetanother  : {
         fn      : 'yetAnotherHandler',
         args    : [ currentState1, currentState2 ] // Capture info to be passed to handler
     },
     prio        : 100           // Higher prio listeners are called before lower
 });
```

When listeners have a `thisObj` option, they are linked to the lifecycle of that object. When it is destroyed, those listeners are removed.

The `config` parameter allows supplying options for the listener(s), for available options see [BryntumListenerConfig](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#typedef-BryntumListenerConfig).

A simpler signature may be used when only adding a listener for one event and no extra options (such as `once` or `delay`) are required:

```
myObject.addListener('click', myController.handleClicks, myController);
```

The args in this simple case are `eventName`, `handler` and `thisObj`

By default, if an event handler throws an exception, the error propagates up the stack and the application state is undefined. Code which follows the event handler will _not_ be executed. Set the [catchEventHandlerExceptions](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#config-catchEventHandlerExceptions) config to `true` to catch exceptions thrown by this object's event handlers and allow the event to continue processing. The exception will be rethrown on a zero millisecond timeout,

[on](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-on)
Alias for [addListener](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#function-addListener). Adds an event listener. This method accepts parameters in the following format:

```
 myObject.on({
     thisObj    : this,          // The this reference for the handlers
     eventname2 : 'functionName' // Resolved at invocation time using the thisObj,
     otherevent : {
         fn      : 'handlerFnName',
         once    : true          // Just this handler is auto-removed on fire
     },
     yetanother  : {
         fn      : 'yetAnotherHandler',
         args    : [ currentState1, currentState2 ] // Capture info to be passed to handler
     },
     prio        : 100           // Higher prio listeners are called before lower
 });
```

When listeners have a `thisObj` option, they are linked to the lifecycle of that object. When it is destroyed, those listeners are removed.

The `config` parameter allows supplying options for the listener(s), for available options see [BryntumListenerConfig](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#typedef-BryntumListenerConfig).

A simpler signature may be used when only adding a listener for one event and no extra options (such as `once` or `delay`) are required:

```
myObject.on('click', myController.handleClicks, myController);
```

The args in this simple case are `eventName`, `handler` and `thisObj`

[ion](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-ion)
Internal convenience method for adding an internal listener, that cannot be removed by the user.

Alias for `on({ $internal : true, ... })`. Only supports single argument form.

[un](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-un)
Shorthand for [removeListener](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#function-removeListener)

[removeListener](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-removeListener)
Removes an event listener. Same API signature as [addListener](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#function-addListener)

[findListener](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-findListener)
Finds the index of a particular listener to the named event. Returns `-1` if the passed function/thisObj listener is not present.

[hasListener](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-hasListener)
Returns `true` if any listener is registered for the specified `eventName`, or if `null`, for any event.

[numListeners](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-numListeners)
Returns the number of attached listener for the specified `eventName`, or if `null`, for any event.

[relayAll](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-relayAll)
Relays all events through another object that also implements Events mixin. Adds a prefix to the event name before relaying, for example add -> storeAdd

```
// Relay all events from store through grid, will make it possible to listen for store events prefixed on grid:
'storeLoad', 'storeChange', 'storeRemoveAll' etc.
store.relayAll(grid, 'store');

grid.on('storeLoad', () => console.log('Store loaded');
```

[removeAllListeners](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-removeAllListeners)
Removes all listeners registered to this object by the application.

[onListen](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-onListen)
This method is called when the first listener for an event is added.

[onUnlisten](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-onUnlisten)
This method is called when the last listener for an event is removed.

[attachAutoDetacher](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-attachAutoDetacher)
Internal function used to hook destroy() calls when using thisObj

[detachAutoDetacher](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-detachAutoDetacher)
Internal function used restore hooked destroy() calls when using thisObj

[once](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-once)
Internal function used to run a callback function after an event is triggered

[await](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-await)

[trigger](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-trigger)
Triggers an event, calling all registered listeners with the supplied arguments. Returning false from any listener makes function return false.

By default, if an event handler throws an exception, the error propagates up the stack and the application state is undefined. Code which follows the event handler will _not_ be executed. Set the [catchEventHandlerExceptions](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#config-catchEventHandlerExceptions) config to `true` to catch exceptions thrown by this object's event handlers and allow the event to continue processing. The exception will be rethrown on a zero millisecond timeout,

[suspendEvents](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-suspendEvents)
Prevents events from being triggered until [resumeEvents()](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#function-resumeEvents) is called. Optionally queues events that are triggered while suspended. Multiple calls stack to require matching calls to `resumeEvents()` before actually resuming.

[resumeEvents](https://bryntum.com/docs/gantt/api/Core/mixin/Events#function-resumeEvents)
Resume event triggering after a call to [suspendEvents()](https://bryntum.com/docs/gantt/api/#Core/mixin/Events#function-suspendEvents). If any triggered events were queued they will be triggered.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeDestroy](https://bryntum.com/docs/gantt/api/Core/mixin/Events#event-beforeDestroy)
Fires before an object is destroyed.

[destroy](https://bryntum.com/docs/gantt/api/Core/mixin/Events#event-destroy)
Fires when an object is destroyed.

[catchAll](https://bryntum.com/docs/gantt/api/Core/mixin/Events#event-catchAll)
Fires when any other event is fired from the object.

**Note**: `catchAll` is fired for both public and private events. Please rely on the public events only.

## Typedefs

Typedefs are type definitions for the class

[BryntumListenerConfig](https://bryntum.com/docs/gantt/api/Core/mixin/Events#typedef-BryntumListenerConfig)
