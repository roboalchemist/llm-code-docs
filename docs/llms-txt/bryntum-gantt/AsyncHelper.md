# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/AsyncHelper.md

# [AsyncHelper](https://bryntum.com/docs/gantt/api/Core/helper/AsyncHelper)

A helper class to make asynchronous tasks `await` friendly.

## Functions

Functions are methods available for calling on the class

[animationFrame](https://bryntum.com/docs/gantt/api/Core/helper/AsyncHelper#function-animationFrame-static)
Returns a promise that resolves on next animation frame.

```
 async method() {
     // do work
     await AsyncHelper.animationFrame();
     // do more work
 }
```

[sleep](https://bryntum.com/docs/gantt/api/Core/helper/AsyncHelper#function-sleep-static)
Returns a promise that resolves after a specified number of milliseconds.

```
 async method() {
     await AsyncHelper.sleep(10);
     // ...
 }
```

[waitFor](https://bryntum.com/docs/gantt/api/Core/helper/AsyncHelper#function-waitFor-static)
Returns a Promise which resolves when the passed function returns a truthy value.

```
 async method() {
      / Wait for a maximum of ten seconds for the eventList to be empty
     await AsyncHelper.waitFor(this.eventList.length === 0, 10000);
     // ...
 }
```

[yield](https://bryntum.com/docs/gantt/api/Core/helper/AsyncHelper#function-yield-static)
Returns a promise that resolves as soon as possible, allowing the browser to minimally process other messages. This is the shortest possible delay the browser offers, so be aware that it does not necessarily allow the browser to paint or reflow if used in a long loop. It does, however, allow other async methods to execute.

```
 async method() {
     await AsyncHelper.yield();
     // ...
 }
```

[waitForAnimations](https://bryntum.com/docs/gantt/api/Core/helper/AsyncHelper#function-waitForAnimations-static)
Returns a promise that resolves when all finite animations on the element have finished.
