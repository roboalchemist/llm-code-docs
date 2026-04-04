# Source: https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 8.4 Dynamic markup insertion](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [8.9 System state and capabilities →](https://html.spec.whatwg.org/multipage/system-state.html)
1.       1.   [8.6 Timers](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timers)
    2.   [8.7 Microtask queuing](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#microtask-queuing)
    3.   [8.8 User prompts](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#user-prompts)
        1.   [8.8.1 Simple dialogs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#simple-dialogs)
        2.   [8.8.2 Printing](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#printing)

### 8.6 Timers[](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timers)

The `setTimeout()` and `setInterval()` methods allow authors to schedule timer-based callbacks.

`id = self.setTimeout(handler [, timeout [, ...arguments ] ])`

[setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout "The global setTimeout() method sets a timer which executes a function or specified piece of code once the timer expires.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 4+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Schedules a timeout to run handler after timeout milliseconds. Any arguments are passed straight through to the handler.

`id = self.setTimeout(code [, timeout ])`
Schedules a timeout to compile and run code after timeout milliseconds.

`self.clearTimeout(id)`

[clearTimeout](https://developer.mozilla.org/en-US/docs/Web/API/clearTimeout "The global clearTimeout() method cancels a timeout previously established by calling setTimeout().")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera 4+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android 37+Samsung Internet?Opera Android 10.1+

Cancels the timeout set with `setTimeout()` or `setInterval()` identified by id.

`id = self.setInterval(handler [, timeout [, ...arguments ] ])`

[setInterval](https://developer.mozilla.org/en-US/docs/Web/API/setInterval "The setInterval() method, offered on the Window and Worker interfaces, repeatedly calls a function or executes a code snippet, with a fixed time delay between each call.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 4+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Schedules a timeout to run handler every timeout milliseconds. Any arguments are passed straight through to the handler.

`id = self.setInterval(code [, timeout ])`
Schedules a timeout to compile and run code every timeout milliseconds.

`self.clearInterval(id)`

[clearInterval](https://developer.mozilla.org/en-US/docs/Web/API/clearInterval "The global clearInterval() method cancels a timed, repeating action which was previously established by a call to setInterval(). If the parameter provided does not identify a previously established action, this method does nothing.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 4+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 10.1+

Cancels the timeout set with `setInterval()` or `setTimeout()` identified by id.

Timers can be nested; after five such nested timers, however, the interval is forced to be at least four milliseconds.

This API does not guarantee that timers will run exactly on schedule. Delays due to CPU load, other tasks, etc, are to be expected.

Objects that implement the `WindowOrWorkerGlobalScope` mixin have a map of setTimeout and setInterval IDs, which is an [ordered map](https://infra.spec.whatwg.org/#ordered-map), initially empty. Each [key](https://infra.spec.whatwg.org/#map-key) in this map is a positive integer, corresponding to the return value of a `setTimeout()` or `setInterval()` call. Each [value](https://infra.spec.whatwg.org/#map-value) is a [unique internal value](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#unique-internal-value), corresponding to a key in the object's [map of active timers](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-active-timers).

* * *

The 
```
setTimeout(handler, timeout,
  ...arguments)
```
 method steps are to return the result of running the [timer initialization steps](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timer-initialisation-steps) given [this](https://webidl.spec.whatwg.org/#this), handler, timeout, arguments, and false.

The 
```
setInterval(handler, timeout,
  ...arguments)
```
 method steps are to return the result of running the [timer initialization steps](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timer-initialisation-steps) given [this](https://webidl.spec.whatwg.org/#this), handler, timeout, arguments, and true.

The `clearTimeout(id)` and `clearInterval(id)` method steps are to [remove](https://infra.spec.whatwg.org/#map-remove)[this](https://webidl.spec.whatwg.org/#this)'s [map of setTimeout and setInterval IDs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-settimeout-and-setinterval-ids)[id].

Because `clearTimeout()` and `clearInterval()` clear entries from the same map, either method can be used to clear timers created by `setTimeout()` or `setInterval()`.

* * *

To perform the timer initialization steps, given a `WindowOrWorkerGlobalScope`global, a string or `Function` or `TrustedScript`handler, a number timeout, a list arguments, a boolean repeat, and optionally (and only if repeat is true) a number previousId, perform the following steps. They return a number.

1.   Let thisArg be global if that is a `WorkerGlobalScope` object; otherwise let thisArg be the `WindowProxy` that corresponds to global.

2.   If previousId was given, let id be previousId; otherwise, let id be an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) integer that is greater than zero and does not already [exist](https://infra.spec.whatwg.org/#map-exists) in global's [map of setTimeout and setInterval IDs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-settimeout-and-setinterval-ids).

3.   If the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop)'s [currently running task](https://html.spec.whatwg.org/multipage/webappapis.html#currently-running-task) is a task that was created by this algorithm, then let nesting level be the [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task)'s [timer nesting level](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timer-nesting-level). Otherwise, let nesting level be 0.

The task's [timer nesting level](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timer-nesting-level) is used both for nested calls to `setTimeout()`, and for the repeating timers created by `setInterval()`. (Or, indeed, for any combination of the two.) In other words, it represents nested invocations of this algorithm, not of a particular method.

4.   If timeout is less than 0, then set timeout to 0.

5.   If nesting level is greater than 5, and timeout is less than 4, then set timeout to 4.

6.   Let realm be global's [relevant realm](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-realm).

7.   Let initiating script be the [active script](https://html.spec.whatwg.org/multipage/webappapis.html#active-script).

8.   Let uniqueHandle be null.

9.   Let task be a [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that runs the following substeps:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): uniqueHandle is a [unique internal value](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#unique-internal-value), not null.

    2.   If id does not [exist](https://infra.spec.whatwg.org/#map-exists) in global's [map of setTimeout and setInterval IDs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-settimeout-and-setinterval-ids), then abort these steps.

    3.   If global's [map of setTimeout and setInterval IDs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-settimeout-and-setinterval-ids)[id] does not equal uniqueHandle, then abort these steps.

This accommodates for the ID having been cleared by a `clearTimeout()` or `clearInterval()` call, and being reused by a subsequent `setTimeout()` or `setInterval()` call.

    4.   Let settings object be global's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

    5.   If [scripting is disabled](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-noscript) for settings object, then abort these steps.

    6.   [Record timing info for timer handler](https://w3c.github.io/long-animation-frames/#record-timing-info-for-timer-handler) given handler, settings object, and repeat.

    7.   If handler is a `Function`, then [invoke](https://webidl.spec.whatwg.org/#invoke-a-callback-function)handler given arguments and "`report`", and with _[callback this value](https://webidl.spec.whatwg.org/#dfn-callback-this-value)_ set to thisArg.

    8.   Otherwise:

        1.   If previousId was not given:

            1.   Let globalName be "`Window`" if global is a `Window` object; "`WorkerGlobalScope`" otherwise.

            2.   Let methodName be "`setInterval`" if repeat is true; "`setTimeout`" otherwise.

            3.   Let sink be a concatenation of globalName, U+0020 SPACE, and methodName.

            4.   Set handler to the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedScript`, global, handler, sink, and "`script`".

        2.   [Assert](https://infra.spec.whatwg.org/#assert): handler is a string.

        3.   Perform [EnsureCSPDoesNotBlockStringCompilation](https://w3c.github.io/webappsec-csp/#can-compile-strings)(realm, « », handler, handler, timer, « », handler). If this throws an exception, catch it, [report](https://html.spec.whatwg.org/multipage/webappapis.html#report-an-exception) it for global, and abort these steps.

        4.   Let fetch options be the [default script fetch options](https://html.spec.whatwg.org/multipage/webappapis.html#default-script-fetch-options).

        5.   Let base URL be settings object's [API base URL](https://html.spec.whatwg.org/multipage/webappapis.html#api-base-url).

        6.   If initiating script is not null, then:

            1.   Set fetch options to a [script fetch options](https://html.spec.whatwg.org/multipage/webappapis.html#script-fetch-options) whose [cryptographic nonce](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-fetch-options-nonce) is initiating script's [fetch options](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-script-fetch-options)'s [cryptographic nonce](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-fetch-options-nonce), [integrity metadata](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-fetch-options-integrity) is the empty string, [parser metadata](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-fetch-options-parser) is "`not-parser-inserted`", [credentials mode](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-fetch-options-credentials) is initiating script's [fetch options](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-script-fetch-options)'s [credentials mode](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-fetch-options-credentials), [referrer policy](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-fetch-options-referrer-policy) is initiating script's [fetch options](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-script-fetch-options)'s [referrer policy](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-fetch-options-referrer-policy), and [fetch priority](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-fetch-options-fetch-priority) is "`auto`".

            2.   Set base URL to initiating script's [base URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-script-base-url).

The effect of these steps ensures that the string compilation done by `setTimeout()` and `setInterval()` behaves equivalently to that done by `eval()`. That is, [module script](https://html.spec.whatwg.org/multipage/webappapis.html#module-script) fetches via `import()` will behave the same in both contexts.

        7.   Let script be the result of [creating a classic script](https://html.spec.whatwg.org/multipage/webappapis.html#creating-a-classic-script) given handler, settings object, base URL, and fetch options.

        8.   [Run the classic script](https://html.spec.whatwg.org/multipage/webappapis.html#run-a-classic-script)script.

    9.   If id does not [exist](https://infra.spec.whatwg.org/#map-exists) in global's [map of setTimeout and setInterval IDs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-settimeout-and-setinterval-ids), then abort these steps.

    10.   If global's [map of setTimeout and setInterval IDs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-settimeout-and-setinterval-ids)[id] does not equal uniqueHandle, then abort these steps.

The ID might have been removed via the author code in handler calling `clearTimeout()` or `clearInterval()`. Checking that uniqueHandle isn't different accounts for the possibility of the ID, after having been cleared, being reused by a subsequent `setTimeout()` or `setInterval()` call.

    11.   If repeat is true, then perform the [timer initialization steps](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timer-initialisation-steps) again, given global, handler, timeout, arguments, true, and id.

    12.   Otherwise, [remove](https://infra.spec.whatwg.org/#map-remove)global's [map of setTimeout and setInterval IDs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-settimeout-and-setinterval-ids)[id].

10.   Increment nesting level by one.

11.   Set task's timer nesting level to nesting level.

12.   Let completionStep be an algorithm step which [queues a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the timer task source given global to run task.

13.   Set uniqueHandle to the result of [running steps after a timeout](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#run-steps-after-a-timeout) given global, "`setTimeout/setInterval`", timeout, and completionStep.

14.   [Set](https://infra.spec.whatwg.org/#map-set)global's [map of setTimeout and setInterval IDs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-settimeout-and-setinterval-ids)[id] to uniqueHandle.

15.   Return id.

Argument conversion as defined by Web IDL (for example, invoking `toString()` methods on objects passed as the first argument) happens in the algorithms defined in Web IDL, before this algorithm is invoked.

So for example, the following rather silly code will result in the log containing "`ONE TWO`":

```
var log = '';
function logger(s) { log += s + ' '; }

setTimeout({ toString: function () {
  setTimeout("logger('ONE')", 100);
  return "logger('TWO')";
} }, 100);
```

To run tasks of several milliseconds back to back without any delay, while still yielding back to the browser to avoid starving the user interface (and to avoid the browser killing the script for hogging the CPU), simply queue the next timer before performing work:

```
function doExpensiveWork() {
  var done = false;
  // ...
  // this part of the function takes up to five milliseconds
  // set done to true if we're done
  // ...
  return done;
}

function rescheduleWork() {
  var id = setTimeout(rescheduleWork, 0); // preschedule next iteration
  if (doExpensiveWork())
    clearTimeout(id); // clear the timeout if we don't need it
}

function scheduleWork() {
  setTimeout(rescheduleWork, 0);
}

scheduleWork(); // queues a task to do lots of work
```

Objects that implement the `WindowOrWorkerGlobalScope` mixin have a map of active timers, which is an [ordered map](https://infra.spec.whatwg.org/#ordered-map), initially empty. Each [key](https://infra.spec.whatwg.org/#map-key) in this map is a [unique internal value](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#unique-internal-value) that represents a timer, and each [value](https://infra.spec.whatwg.org/#map-value) is a `DOMHighResTimeStamp`, representing the expiry time for that timer.

To run steps after a timeout, given a `WindowOrWorkerGlobalScope`global, a string orderingIdentifier, a number milliseconds, and a set of steps completionSteps, perform the following steps. They return a [unique internal value](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#unique-internal-value).

1.   Let timerKey be a new [unique internal value](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#unique-internal-value).

2.   Let startTime be the [current high resolution time](https://w3c.github.io/hr-time/#dfn-current-high-resolution-time) given global.

3.   [Set](https://infra.spec.whatwg.org/#map-set)global's [map of active timers](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-active-timers)[timerKey] to startTime plus milliseconds.

4.   Run the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

    1.   If global is a `Window` object, wait until global's [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window) has been [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active) for a further milliseconds milliseconds (not necessarily consecutively).

Otherwise, global is a `WorkerGlobalScope` object; wait until milliseconds milliseconds have passed with the worker not suspended (not necessarily consecutively).

    2.   Wait until any invocations of this algorithm that had the same global and orderingIdentifier, that started before this one, and whose milliseconds is less than or equal to this one's, have completed.

    3.   Optionally, wait a further [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) length of time.

This is intended to allow user agents to pad timeouts as needed to optimize the power usage of the device. For example, some processors have a low-power mode where the granularity of timers is reduced; on such platforms, user agents can slow timers down to fit this schedule instead of requiring the processor to use the more accurate mode with its associated higher power usage.

    4.   Perform completionSteps.

    5.   [Remove](https://infra.spec.whatwg.org/#map-remove)global's [map of active timers](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-active-timers)[timerKey].

5.   Return timerKey.

[Run steps after a timeout](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#run-steps-after-a-timeout) is meant to be used by other specifications that want to execute developer-supplied code after a developer-supplied timeout, in a similar manner to `setTimeout()`. (Note, however, it does not have the nesting and clamping behavior of `setTimeout()`.) Such specifications can choose an orderingIdentifier to ensure ordering within their specification's timeouts, while not constraining ordering with respect to other specification's timeouts.

### 8.7 Microtask queuing[](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#microtask-queuing)

[queueMicrotask](https://developer.mozilla.org/en-US/docs/Web/API/queueMicrotask "The queueMicrotask() method, which is exposed on the Window or Worker interface, queues a microtask to be executed at a safe time prior to control returning to the browser's event loop.")

Support in all current engines.

Firefox 69+Safari 12.1+Chrome 71+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

`self.queueMicrotask(callback)`
[Queues](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-microtask) a [microtask](https://html.spec.whatwg.org/multipage/webappapis.html#microtask) to run the given callback.

The `queueMicrotask(callback)` method must [queue a microtask](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-microtask) to [invoke](https://webidl.spec.whatwg.org/#invoke-a-callback-function)callback with « » and "`report`".

The `queueMicrotask()` method allows authors to schedule a callback on the [microtask queue](https://html.spec.whatwg.org/multipage/webappapis.html#microtask-queue). This allows their code to run once the [JavaScript execution context stack](https://tc39.es/ecma262/#execution-context-stack) is next empty, which happens once all currently executing synchronous JavaScript has run to completion. This doesn't yield control back to the [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop), as would be the case when using, for example, `setTimeout(f, 0)`.

Authors ought to be aware that scheduling a lot of microtasks has the same performance downsides as running a lot of synchronous code. Both will prevent the browser from doing its own work, such as rendering. In many cases, `requestAnimationFrame()` or `requestIdleCallback()` is a better choice. In particular, if the goal is to run code before the next rendering cycle, that is the purpose of `requestAnimationFrame()`.

As can be seen from the following examples, the best way of thinking about `queueMicrotask()` is as a mechanism for rearranging synchronous code, effectively placing the queued code immediately after the currently executing synchronous JavaScript has run to completion.

The most common reason for using `queueMicrotask()` is to create consistent ordering, even in the cases where information is available synchronously, without introducing undue delay.

For example, consider a custom element firing a `load` event, that also maintains an internal cache of previously-loaded data. A naïve implementation might look like:

```
MyElement.prototype.loadData = function (url) {
  if (this._cache[url]) {
    this._setData(this._cache[url]);
    this.dispatchEvent(new Event("load"));
  } else {
    fetch(url).then(res => res.arrayBuffer()).then(data => {
      this._cache[url] = data;
      this._setData(data);
      this.dispatchEvent(new Event("load"));
    });
  }
};
```

This naïve implementation is problematic, however, in that it causes its users to experience inconsistent behavior. For example, code such as

```
element.addEventListener("load", () => console.log("loaded"));
console.log("1");
element.loadData();
console.log("2");
```

will sometimes log "1, 2, loaded" (if the data needs to be fetched), and sometimes log "1, loaded, 2" (if the data is already cached). Similarly, after the call to `loadData()`, it will be inconsistent whether or not the data is set on the element.

To get a consistent ordering, `queueMicrotask()` can be used:

```
MyElement.prototype.loadData = function (url) {
  if (this._cache[url]) {
    queueMicrotask(() => {
      this._setData(this._cache[url]);
      this.dispatchEvent(new Event("load"));
    });
  } else {
    fetch(url).then(res => res.arrayBuffer()).then(data => {
      this._cache[url] = data;
      this._setData(data);
      this.dispatchEvent(new Event("load"));
    });
  }
};
```

By essentially rearranging the queued code to be after the [JavaScript execution context stack](https://tc39.es/ecma262/#execution-context-stack) empties, this ensures a consistent ordering and update of the element's state.

Another interesting use of `queueMicrotask()` is to allow uncoordinated "batching" of work by multiple callers. For example, consider a library function that wants to send data somewhere as soon as possible, but doesn't want to make multiple network requests if doing so is easily avoidable. One way to balance this would be like so:

```
const queuedToSend = [];

function sendData(data) {
  queuedToSend.push(data);

  if (queuedToSend.length === 1) {
    queueMicrotask(() => {
      const stringToSend = JSON.stringify(queuedToSend);
      queuedToSend.length = 0;

      fetch("/endpoint", stringToSend);
    });
  }
}
```

With this architecture, multiple subsequent calls to `sendData()` within the currently executing synchronous JavaScript will be batched together into one `fetch()` call, but with no intervening event loop tasks preempting the fetch (as would have happened with similar code that instead used `setTimeout()`).

### 8.8 User prompts[](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#user-prompts)

#### 8.8.1 Simple dialogs[](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#simple-dialogs)

`window.alert(message)`

[Window/alert](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert "window.alert() instructs the browser to display a dialog with an optional message, and to wait until the user dismisses the dialog.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 3+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Displays a modal alert with the given message, and waits for the user to dismiss it.

`result = window.confirm(message)`

[Window/confirm](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm "window.confirm() instructs the browser to display a dialog with an optional message, and to wait until the user either confirms or cancels the dialog.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 3+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 1+Samsung Internet?Opera Android 10.1+

Displays a modal OK/Cancel prompt with the given message, waits for the user to dismiss it, and returns true if the user clicks OK and false if the user clicks Cancel.

`result = window.prompt(message [, default])`

[Window/prompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt "window.prompt() instructs the browser to display a dialog with an optional message prompting the user to input some text, and to wait until the user either submits the text or cancels the dialog.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 3+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 4+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Displays a modal text control prompt with the given message, waits for the user to dismiss it, and returns the value that the user entered. If the user cancels the prompt, then returns null instead. If the second argument is present, then the given value is used as a default.

Logic that depends on [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) or [microtasks](https://html.spec.whatwg.org/multipage/webappapis.html#microtask), such as [media elements](https://html.spec.whatwg.org/multipage/media.html#media-element) loading their [media data](https://html.spec.whatwg.org/multipage/media.html#media-data), are stalled when these methods are invoked.

The `alert()` and `alert(message)` method steps are:

1.   If we [cannot show simple dialogs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#cannot-show-simple-dialogs) for [this](https://webidl.spec.whatwg.org/#this), then return.

2.   If the method was invoked with no arguments, then let message be the empty string; otherwise, let message be the method's first argument.

3.   Set message to the result of [normalizing newlines](https://infra.spec.whatwg.org/#normalize-newlines) given message.

4.   Set message to the result of [optionally truncating](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#optionally-truncate-a-simple-dialog-string)message.

5.   Let userPromptHandler be [WebDriver BiDi user prompt opened](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-user-prompt-opened) with [this](https://webidl.spec.whatwg.org/#this), "`alert`", and message.

6.   If userPromptHandler is "`none`", then:

    1.   Show message to the user, treating U+000A LF as a line break.

    2.   Optionally, [pause](https://html.spec.whatwg.org/multipage/webappapis.html#pause) while waiting for the user to acknowledge the message.

7.   Invoke [WebDriver BiDi user prompt closed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-user-prompt-closed) with [this](https://webidl.spec.whatwg.org/#this), "`alert`", and true.

This method is defined using two overloads, instead of using an optional argument, for historical reasons. The practical impact of this is that `alert(undefined)` is treated as `alert("undefined")`, but `alert()` is treated as `alert("")`.

The `confirm(message)` method steps are:

1.   If we [cannot show simple dialogs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#cannot-show-simple-dialogs) for [this](https://webidl.spec.whatwg.org/#this), then return false.

2.   Set message to the result of [normalizing newlines](https://infra.spec.whatwg.org/#normalize-newlines) given message.

3.   Set message to the result of [optionally truncating](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#optionally-truncate-a-simple-dialog-string)message.

4.   Show message to the user, treating U+000A LF as a line break, and ask the user to respond with a positive or negative response.

5.   Let userPromptHandler be [WebDriver BiDi user prompt opened](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-user-prompt-opened) with [this](https://webidl.spec.whatwg.org/#this), "`confirm`", and message.

6.   Let accepted be false.

7.   If userPromptHandler is "`none`", then:

    1.   [Pause](https://html.spec.whatwg.org/multipage/webappapis.html#pause) until the user responds either positively or negatively.

    2.   If the user responded positively, then set accepted to true.

8.   If userPromptHandler is "`accept`", then set accepted to true.

9.   Invoke [WebDriver BiDi user prompt closed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-user-prompt-closed) with [this](https://webidl.spec.whatwg.org/#this), "`confirm`", and accepted.

10.   Return accepted.

The 
```
prompt(message,
  default)
```
 method steps are:

1.   If we [cannot show simple dialogs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#cannot-show-simple-dialogs) for [this](https://webidl.spec.whatwg.org/#this), then return null.

2.   Set message to the result of [normalizing newlines](https://infra.spec.whatwg.org/#normalize-newlines) given message.

3.   Set message to the result of [optionally truncating](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#optionally-truncate-a-simple-dialog-string)message.

4.   Set default to the result of [optionally truncating](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#optionally-truncate-a-simple-dialog-string)default.

5.   Show message to the user, treating U+000A LF as a line break, and ask the user to either respond with a string value or abort. The response must be defaulted to the value given by default.

6.   Let userPromptHandler be [WebDriver BiDi user prompt opened](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-user-prompt-opened) with [this](https://webidl.spec.whatwg.org/#this), "`prompt`", and message.

7.   Let result be null.

8.   If userPromptHandler is "`none`", then:

    1.   [Pause](https://html.spec.whatwg.org/multipage/webappapis.html#pause) while waiting for the user's response.

    2.   If the user did not abort, then set result to the string that the user responded with.

9.   Otherwise, if userPromptHandler is "`accept`", then set result to the empty string.

10.   Invoke [WebDriver BiDi user prompt closed](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-user-prompt-closed) with [this](https://webidl.spec.whatwg.org/#this), "`prompt`", false if result is null or true otherwise, and result.

11.   Return result.

To optionally truncate a simple dialog string s, return either s itself or some string derived from s that is shorter. User agents should not provide UI for displaying the elided portion of s, as this makes it too easy for abusers to create dialogs of the form "Important security alert! Click 'Show More' for full details!".

For example, a user agent might want to only display the first 100 characters of a message. Or, a user agent might replace the middle of the string with "…". These types of modifications can be useful in limiting the abuse potential of unnaturally large, trustworthy-looking system dialogs.

#### 8.8.2 Printing[](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#printing)

[Window/print](https://developer.mozilla.org/en-US/docs/Web/API/Window/print "Opens the print dialog to print the current document.")

Support in all current engines.

Firefox 1+Safari 1.1+Chrome 1+

* * *

Opera 6+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5+

* * *

Firefox Android 114+Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

`window.print()`
Prompts the user to print the page.

The `print()` method steps are:

1.   Let document be [this](https://webidl.spec.whatwg.org/#this)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window).

2.   If document is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then return.

3.   If document's [unload counter](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-counter) is greater than 0, then return.

4.   If document is [ready for post-load tasks](https://html.spec.whatwg.org/multipage/parsing.html#ready-for-post-load-tasks), then run the [printing steps](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#printing-steps) for document.

5.   Otherwise, set document's print when loaded flag.

User agents should also run the [printing steps](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#printing-steps) whenever the user asks for the opportunity to [obtain a physical form](https://html.spec.whatwg.org/multipage/rendering.html#obtain-a-physical-form) (e.g. printed copy), or the representation of a physical form (e.g. PDF copy), of a document.

The printing steps for a `Document`document are:

1.   The user agent may display a message to the user or return (or both).

For instance, a kiosk browser could silently ignore any invocations of the `print()` method.

For instance, a browser on a mobile device could detect that there are no printers in the vicinity and display a message saying so before continuing to offer a "save to PDF" option.

2.   If the [active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set) of document has the [sandboxed modals flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-modals-flag) set, then return.

If the printing dialog is blocked by a `Document`'s sandbox, then neither the `beforeprint` nor `afterprint` events will be fired.

3.   The user agent must [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `beforeprint` at the [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) of document, as well as any [child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) in it.

Firing in children only doesn't seem right here, and some tasks likely need to be queued. See [issue #5096](https://github.com/whatwg/html/issues/5096).

The `beforeprint` event can be used to annotate the printed copy, for instance adding the time at which the document was printed.

4.   The user agent should offer the user the opportunity to [obtain a physical form](https://html.spec.whatwg.org/multipage/rendering.html#obtain-a-physical-form) (or the representation of a physical form) of document. The user agent may wait for the user to either accept or decline before returning; if so, the user agent must [pause](https://html.spec.whatwg.org/multipage/webappapis.html#pause) while the method is waiting. Even if the user agent doesn't wait at this point, the user agent must use the state of the relevant documents as they are at this point in the algorithm if and when it eventually creates the alternate form.

5.   The user agent must [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `afterprint` at the [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) of document, as well as any [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable) in it.

Firing in children only doesn't seem right here, and some tasks likely need to be queued. See [issue #5096](https://github.com/whatwg/html/issues/5096).

The `afterprint` event can be used to revert annotations added in the earlier event, as well as showing post-printing UI. For instance, if a page is walking the user through the steps of applying for a home loan, the script could automatically advance to the next step after having printed a form or other.

[← 8.4 Dynamic markup insertion](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [8.9 System state and capabilities →](https://html.spec.whatwg.org/multipage/system-state.html)
