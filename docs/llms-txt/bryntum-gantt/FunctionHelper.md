# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/FunctionHelper.md

# [FunctionHelper](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper)

Provides functionality for working with functions

## Functions

Functions are methods available for calling on the class

[after](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#function-after-static)
Inserts a function after the specified `method` is called on an `object`. To remove this hook, invoke the function returned by this method.

```
 class A {
     method() {
         console.log('method');
     }
 }

 let instance = new A();

 let detach = FunctionHelper.after(instance, 'method', () => { console.log('after') });

 instance.method();
 > method
 > after

 detach();
 instance.method();
 > method
```

The value returned by the original method is passed as the first argument to `fn` followed by all the arguments passed by the caller.

If `fn` returns a value (not `undefined`), that value is returned from the method call instead of the value returned by the original method.

```
 class A {
     method(x) {
         console.log('method', x);
         return x * 2
     }
 }

 let instance = new A();

 let detach = FunctionHelper.after(instance, 'method', (ret, x) => {
     console.log('after', ret, x);
     return x / 2;
 });

 console.log(instance.method(50));
 > method 50
 > after 100 50
 > 25

 detach();
 console.log(instance.method(50));
 > method 50
 > 100
```

[before](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#function-before-static)
Inserts a function before the specified `method` is called on an `object`. To remove this hook, invoke the function returned by this method.

```
 class A {
     method() {
         console.log('method');
     }
 }

 let instance = new A();

 let detach = FunctionHelper.before(instance, 'method', () => { console.log('before') });

 instance.method();
 > before
 > method

 detach();
 instance.method();
 > method
```

If `fn` returns `false`, the original method is not invoked and `false` is returned to the caller.

```
 class A {
     method(x) {
         console.log('method', x);
         return x * 2;
     }
 }

 let instance = new A();

 let detach = FunctionHelper.before(instance, 'method', x => {
     console.log('before', x);
     return false;
 });

 console.log(instance.method(50));
 > before 50
 > false

 detach();
 console.log(instance.method(50));
 > method 50
 > 100
```

[combineFilterFns](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#function-combineFilterFns-static)
Combines all the passed filtering functions into a single function which returns `false` if any of the passed functions returns `false`, otherwise it returns `true`.

If only one function is passed, it is returned without being wrapped in another function.

If no functions are passed, `undefined` is returned - this is useful for cases where a filter function is optional and we don't want to add the overhead of an extra function call when there is no filter.

[createInterceptor](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#function-createInterceptor-static)
Returns a function which calls the passed `interceptor` function first, and the passed `original` after as long as the `interceptor` does not return `false`.

[createSequence](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#function-createSequence-static)
Returns a function which calls the passed `sequence` function after calling the passed `original`.

[createThrottled](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#function-createThrottled-static)
Create a "debounced" function which will call on the "leading edge" of a timer period. When first invoked will call immediately, but invocations after that inside its buffer period will be rejected, and _one_ invocation will be made after the buffer period has expired.

This is useful for responding immediately to a first mousemove, but from then on, only calling the action function on a regular timer while the mouse continues to move.

[createBuffered](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#function-createBuffered-static)
Create a "debounced" function which will call on the "trailing edge" of a timer period. When first invoked will wait until the buffer period has expired to call the function, and more calls within that time will restart the timer.

This is useful for responding to keystrokes, but deferring action until the user pauses typing.

[noThrow](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#function-noThrow-static)
Protects the specified `method` on a given `object` such that calling it will not throw exceptions.

[animate](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#function-animate-static)
Calls the passed function on every animation frame while animating the `progress` value from 0 to 1 over the specified duration.

The function is called with the current `progress` value as the first argument. That value changes from `0` to `1` over the duration of the animation at a rate determined by the `easing` function.

The called function may change the value of any property or perform some other action based on the current `progress` value.

The function should return `false` to indicate that the animation should be stopped immediately.

```
// Increase hourHeight by 20 pixels in a visually appealing way
const
    { activeView } = this,
    { hourHeight } = activeView;

FunctionHelper.animate(
    1000,
    progress => activeView.hourHeight = hourHeight * progress * 20,
    null,
    'bounce'
);
```

[abortablePromise](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#function-abortablePromise-static)
Creates an abortable promise and returns an array containing the promise, the abort signal, and the abort controller. When AbortController is invoked, promise gets rejected.

## Typedefs

Typedefs are type definitions for the class

[AbortablePromiseMeta](https://bryntum.com/docs/gantt/api/Core/helper/FunctionHelper#typedef-AbortablePromiseMeta)
