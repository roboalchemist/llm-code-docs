# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Delayable.md

# [Delayable](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable)

Tracks `setTimeout`, `setInterval` and `requestAnimationFrame` calls and clears them on destroy.

```
someClass.setTimeout(() => console.log('hi'), 200);
someClass.setInterval(() => console.log('annoy'), 100);
// can also use named timeouts for easier tracking
someClass.setTimeout(() => console.log('named'), 300, 'named');
someClass.clearTimeout('named');
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDelayable](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#property-isDelayable)
Identifies an object as an instance of [Delayable](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable) class, or subclass thereof.

[isDelayable](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#property-isDelayable-static)
Identifies an object as an instance of [Delayable](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable) class, or subclass thereof.

[delayable](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#property-delayable-static)
This class property returns an object that specifies methods to wrap with configurable timer behaviors.

It is used like so:

```
 class Foo extends Base.mixin(Delayable) {
     static get delayable() {
         return {
             expensiveMethod : 500
         };
     }

     expensiveMethod() {
         this.things();
         this.moreThings();
         this.evenMoreThings();
     }
 }
```

With the above in place, consider:

```
 let instance = new Foo();

 instance.expensiveMethod();
```

Instead of the above code immediately calling the `expensiveMethod()`, it will start a timer that will invoke the method 500ms later. Because `expensiveMethod()` is an instance method, each instance of `Foo` will have its own timer.

NOTE: Only instance methods are currently supported (i.e., only non-`static` methods).

#### Options

The value of each key configures how the method will be scheduled. If the value is a number, it is promoted to a config object of `type='buffer'` as in the following:

```
 class Foo extends Base.mixin(Delayable) {
     static get delayable() {
         return {
             expensiveMethod : {
                 type  : 'buffer',
                 delay : 500
             }
         };
     }
 }
```

The `type` property of the config object must be one of three values. Other options can be provided depending on the `type`:

* `buffer`  
    Other options:
  * `delay` (Number) : The number of milliseconds to wait before calling the underlying method. A value of 0 is equivalent to setting `immediate: true`.
  * `immediate` (Boolean) : Set to `true` to call immediately (effectively disabling the buffer).
* `raf` (short for "request animation frame")  

* `idle` (short for "request idle callback") **Not available on Safari**  
    Other options:
  * `cancelOutstanding` (Boolean) : Set to `true` to cancel any pending animation frame requests and schedule a new one on each call.
  * `immediate` (Boolean) : Set to `true` to call immediately.
* `throttle`  
    Other options:
  * `delay` (Number) : The number of milliseconds to wait after each execution before another execution takes place. A value of 0 is equivalent to setting `immediate: true`.
  * `immediate` (Boolean) : Set to `true` to call immediately (effectively disabling the throttle).

While `immediate: true` can be specified at the class level, it is more typical to set it on the instance's method as described below.

#### Delayable Method API

Delayable methods have a consistent API to manage their scheduling. This API is added to the methods themselves.

For example:

```
 let instance = new Foo();

 instance.expensiveMethod();         // schedule a call in 500ms
 instance.expensiveMethod.isPending; // true
 instance.expensiveMethod.cancel();
 instance.expensiveMethod.flush();
 instance.expensiveMethod.now();

 instance.expensiveMethod.delay = 10;
 instance.expensiveMethod();         // schedule a call in 10ms
```

##### `isPending` (Boolean, readonly)

This boolean property will be `true` if a call has been scheduled, and false otherwise.

##### `cancel()`

Cancels a pending call if one has been scheduled. Otherwise this method does nothing.

##### `flush()`

Cancels the timer and causes the pending call to execute immediately. If there is no pending call, this method does nothing.

##### `now()`

Cancels the timer (if one is pending) and executes the method immediately. If there is no pending call, this method will still call the underlying method.

## Functions

Functions are methods available for calling on the class

[makeInvoker](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-makeInvoker)
Creates and returns a function that will call the user-supplied `fn`.

[decorateWrapFn](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-decorateWrapFn)
Decorates the supported `wrapFn` with additional methods and an `isPending` readonly property. These decorations are available to user code to help manage the scheduling behavior of the buffered function.

[hasTimeout](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-hasTimeout)
Check if a named timeout is active

[asap](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-asap)
Returns a function that when called will schedule a call to `fn` via [queueMicrotask](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable#function-queueMicrotask).

[queueMicrotask](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-queueMicrotask)
Equivalent to the native [`queueMicrotask`](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/queueMicrotask), but will be cancelled automatically on `destroy`. When `queueMicrotask` is not available, the provided `fn` is called using `Promise.resolve().then(fn)`, which behaves similarly.

Returns a function that when called will cancel the impending call. This function can also be viewed as a timer id that can be passed to [cancelMicrotask](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable#function-cancelMicrotask)

[cancelMicrotask](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-cancelMicrotask)
Given the return value from a call to [queueMicrotask](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable#function-queueMicrotask), cancels the pending call. This method is provided for symmetry with other timer functions, such as [setTimeout](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable#function-setTimeout).

[setTimeout](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-setTimeout)
Same as native setTimeout, but will be cleared automatically on destroy. If a propertyName is supplied it will be used to store the timeout id.

[clearTimeout](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-clearTimeout)
clearTimeout wrapper, either call with timeout id as normal clearTimeout or with timeout name (if you specified a name to setTimeout()) property to null.

[clearInterval](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-clearInterval)
clearInterval wrapper

[setInterval](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-setInterval)
Same as native setInterval, but will be cleared automatically on destroy

[requestAnimationFrame](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-requestAnimationFrame)
Relays to native requestAnimationFrame and adds to tracking to have call automatically canceled on destroy.

[requestIdleCallback](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-requestIdleCallback)
Relays to native requestIdleCallback and adds to tracking to have call automatically canceled on destroy.

[createOnFrame](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-createOnFrame)
Creates a function which will execute once, on the next animation frame. However many time it is called in one event run, it will only be scheduled to run once.

[cancelAnimationFrame](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-cancelAnimationFrame)
Relays to native cancelAnimationFrame and removes from tracking.

[cancelIdleCallback](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-cancelIdleCallback)
Relays to native cancelIdleCallback and removes from tracking.

[buffer](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-buffer)
Wraps a function with another function that delays it specified amount of time, repeated calls to the wrapper resets delay.

[raf](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-raf)
Returns a function that when called will schedule a call to `fn` on the next animation frame.

[throttle](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-throttle)
Create a "debounced" function which will call on the "leading edge" of a timer period. When first invoked will call immediately, but invocations after that inside its buffer period will be rejected, and _one_ invocation will be made after the buffer period has expired.

This is useful for responding immediately to a first mousemove, but from then on, only calling the action function on a regular timer while the mouse continues to move.

[setupDelayableMethods](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#function-setupDelayableMethods-static)
This method initializes the `delayable` methods on this class.

## Typedefs

Typedefs are type definitions for the class

[DelayableConfig](https://bryntum.com/docs/gantt/api/Core/mixin/Delayable#typedef-DelayableConfig)
Configuration options available when defining a delayable function.
