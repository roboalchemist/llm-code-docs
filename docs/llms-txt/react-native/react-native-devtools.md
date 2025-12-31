# Source: https://reactnative.dev/docs/react-native-devtools.md

# React Native DevTools

React Native DevTools is our modern debugging experience for React Native. Purpose-built from the ground up, it aims to be fundamentally more integrated, correct, and reliable than previous debugging methods.

![React Native DevTools opened to the \&quot;Welcome\&quot; pane](/assets/images/debugging-rndt-welcome-083-9f56f0124de2d2607022330b0ce41d85.jpg)

React Native DevTools is designed for debugging React app concerns, and not to replace native tools. If you want to inspect React Native’s underlying platform layers (for example, while developing a Native Module), please use the debugging tools available in Android Studio and Xcode (see [Debugging Native Code](/docs/debugging-native-code.md)).

**💡 Compatibility** — released in 0.76

React Native DevTools supports all React Native apps running Hermes. It replaces the previous Flipper, Experimental Debugger, and Hermes debugger (Chrome) frontends.

It is not possible to set up React Native DevTools with any older versions of React Native.

* **Chrome Browser DevTools — unsupported**
  * Connecting to React Native via `chrome://inspect` is no longer supported. Features may not work correctly, as the latest versions of Chrome DevTools (which are built to match the latest browser capabilities and APIs) have not been tested, and this frontend lacks our customisations. Instead, we ship a supported version with React Native DevTools.
* **Visual Studio Code — unsupported** (pre-existing)
  <!-- -->
  * Third party extensions such as [Expo Tools](https://github.com/expo/vscode-expo) and [Radon IDE](https://ide.swmansion.com/) may have improved compatibility, but are not directly supported by the React team.

**💡 Feedback & FAQs**

We want the tooling you use to debug React across all platforms to be reliable, familiar, simple, and cohesive. All the features described on this page are built with these principles in mind, and we also want to offer more capabilities in future.

We are actively iterating on the future of React Native DevTools, and have created a centralized [GitHub discussion](https://github.com/react-native-community/discussions-and-proposals/discussions/819) to keep track of issues, frequently asked questions, and feedback.

## Core features[​](#core-features "Direct link to Core features")

React Native DevTools is based on the Chrome DevTools frontend. If you have a web development background, its features should be familiar. As a starting point, we recommend browsing the [Chrome DevTools docs](https://developer.chrome.com/docs/devtools) which contain full guides as well as video resources.

### Console[​](#console "Direct link to Console")

![A series of logs React Native DevTools Sources view, alongside a device](/assets/images/debugging-rndt-console-536fe8a6f470b09b93ace9b4f67b4612.jpg)

The Console panel allows you to view and filter messages, evaluate JavaScript, inspect object properties, and more.

[Console features reference | Chrome DevTools](https://developer.chrome.com/docs/devtools/console/reference)

#### Useful tips[​](#useful-tips "Direct link to Useful tips")

* If your app has a lot of logs, use the filter box or change the log levels that are shown.
* Watch values over time with [Live Expressions](https://developer.chrome.com/docs/devtools/console/live-expressions).
* Persist messages across reloads with [Preserve Logs](https://developer.chrome.com/docs/devtools/console/reference#persist).
* Use `Ctrl` + `L` to clear the console view.

### Sources & breakpoints[​](#sources--breakpoints "Direct link to Sources & breakpoints")

![A paused breakpoint in the React Native DevTools Sources view, alongside a device](/assets/images/debugging-rndt-sources-paused-with-device-c7585ed4a3ab596e32c2109efd9c22a0.jpg)

The Sources panel allows you to view the source files in your app and register breakpoints. Use a breakpoint to define a line of code where your app should pause — allowing you to inspect the live state of the program and incrementally step through code.

[Pause your code with breakpoints | Chrome DevTools](https://developer.chrome.com/docs/devtools/javascript/breakpoints)

tip

#### Mini-guide[​](#mini-guide "Direct link to Mini-guide")

Breakpoints are a fundamental tool in your debugging toolkit!

1. Navigate to a source file using the sidebar or `Cmd ⌘`+`P` / `Ctrl`+`P`.
2. Click in the line number column next to a line of code to add a breakpoint.
3. Use the navigation controls at the top right to [step through code](https://developer.chrome.com/docs/devtools/javascript/reference#stepping) when paused.

#### Useful tips[​](#useful-tips-1 "Direct link to Useful tips")

* A "Paused in Debugger" overlay appears when your app is paused. Tap it to resume.
* Pay attention to the right-hand panels when on a breakpoint, which allow you to inspect the current scope and call stack, and set watch expressions.
* Use a `debugger;` statement to quickly set a breakpoint from your text editor. This will reach the device immediately via Fast Refresh.
* There are multiple kinds of breakpoints! For example, [Conditional Breakpoints and Logpoints](https://developer.chrome.com/docs/devtools/javascript/breakpoints#overview).

### NetworkSince 0.83[​](#network-since-083 "Direct link to network-since-083")

![A network request in the React Native DevTools Network panel](/assets/images/debugging-rndt-network-462cd5e39a5525592501627bb0087747.jpg)

The Network panel allows you to view and inspect the network requests made by your app. Logged requests provide detailed metadata such as timings and headers sent/received, as well as response previews.

Network requests are recorded automatically when DevTools is open. We support most features from Chrome, with some exceptions. See more below.

**💡 Network event coverage, Expo support**

**Which network events are captured?**

Today, we record all network calls through `fetch()`, `XMLHttpRequest`, and `<Image>` — with support for custom networking libraries, such as Expo Fetch, coming later.

**Expo Network differences**

Because of this, apps using Expo will continue to see the "Expo Network" panel — a separate implementation by the Expo framework which will log these additional request sources but has slightly reduced features.

* Coverage for Expo-specific network events.
* No request initiator support.
* No Performance panel integration.

We're working with Expo to integrate Expo Fetch and third party networking libraries with our new Network inspection pipeline in future releases.

**Unimplemented features**

At launch, these are the features we don't yet support in React Native:

* WebSocket events
* Network response mocking
* Simulated network throttling

**💡 Response previews buffer size**

If you are inspecting a large volume of response data, please note that response previews are cached in an on-device buffer with a maximum size of 100MB. This means we may evict response previews (but not metadata) if the cache becomes too large, oldest request first.

#### Useful tips[​](#useful-tips-2 "Direct link to Useful tips")

* Use the Initiator tab to see the call stack of where a network request was initiated in your app.
* Network events will also be shown in the Network track in the Performance panel.

### PerformanceSince 0.83[​](#performance-since-083 "Direct link to performance-since-083")

![A performance trace in the React Native DevTools Performance panel](/assets/images/debugging-rndt-performance-084166527768b90dbb936b240707bdcb.jpg)

Performance tracing allows you to record a performance session within your app to understand how your JavaScript code is running and what operations took the most time. In React Native, we show JavaScript execution, React Performance tracks, Network events, and custom [User Timings](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/User_timing), rendered in a single performance timeline.

#### Useful tips[​](#useful-tips-3 "Direct link to Useful tips")

* Use [Annotations](https://developer.chrome.com/docs/devtools/performance/annotations) to label and mark up a performance trace — useful before [downloading and sharing](https://developer.chrome.com/docs/devtools/performance/save-trace) with a teammate.
* Use the [`PerformanceObserver` API](/docs/global-PerformanceObserver.md) in your app to observe performance events at runtime — useful if you want to capture performance telemetry.

#### Learn more[​](#learn-more "Direct link to Learn more")

* [React Performance tracks](https://react.dev/reference/dev-tools/react-performance-tracks)
* [Performance APIs > User Timings | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/User_timing)
* ["Debug Like a Senior — React Native Performance Panel" | Software Mansion](https://blog.swmansion.com/react-native-debugging-new-performance-panel-in-react-native-0-83-21ca90871f6d)

### Memory[​](#memory "Direct link to Memory")

![Inspecting a heap snapshot in the Memory panel](/assets/images/debugging-rndt-memory-741d3be5a43f872d0d4485d9f71456c8.jpg)

The Memory panel allows you to take a heap snapshot and view the memory usage of your JavaScript code over time.

[Record heap snapshots | Chrome DevTools](https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots)

#### Useful tips[​](#useful-tips-4 "Direct link to Useful tips")

* Use `Cmd ⌘`+`F` / `Ctrl`+`F` to filter for specific objects in the heap.
* Taking an [allocation timeline report](https://developer.chrome.com/docs/devtools/memory-problems/allocation-profiler) can be useful to see memory usage over time as a graph, to identify possible memory leaks.

## React DevTools features[​](#react-devtools-features "Direct link to React DevTools features")

In the integrated Components and Profiler panels, you'll find all the features of the [React DevTools](https://react.dev/learn/react-developer-tools) browser extension. These work seamlessly in React Native DevTools.

### React Components[​](#react-components "Direct link to React Components")

![Selecting and locating elements using the React Components panel](/assets/images/debugging-rndt-react-components-628d33c662dc37b0a7c3c21d840fc63c.gif)

The React Components panel allows you to inspect and update the rendered React component tree.

* Hover or select an element in DevTools to highlight it on the device.
* To locate an element in DevTools, click the top-left "Select element" button, then tap any element in the app.

#### Useful tips[​](#useful-tips-5 "Direct link to Useful tips")

* Props and state on a component can be viewed and modified at runtime using the right hand panel.
* Components optimized with [React Compiler](https://react.dev/learn/react-compiler) will be annotated with a "Memo ✨" badge.

tip

#### Protip: Highlight re-renders[​](#protip-highlight-re-renders "Direct link to Protip: Highlight re-renders")

Re-renders can be a significant contributor to performance issues in React apps. DevTools can highlight component re-renders as they happen.

* To enable, click the View Settings (`⚙︎`) icon and check "Highlight updates when components render".

![Location of the \&quot;highlight updates\&quot; setting, next to a recording of the live render overlay](/assets/images/debugging-rndt-highlight-renders-bc20258bbc79dba4fe1866c227943e37.gif)

### React Profiler[​](#react-profiler "Direct link to React Profiler")

![A profile rendered as a flame graph](/assets/images/debugging-rndt-react-profiler-df4337af110cbdc1da74837b2beacec2.jpg)

The React Profiler panel allows you to record performance profiles to understand the timing of component renders and React commits.

For more info, see the [original 2018 guide](https://legacy.reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html#reading-performance-data) (note that parts of this may be outdated).

## Reconnecting DevTools[​](#reconnecting-devtools "Direct link to Reconnecting DevTools")

Occasionally, DevTools might disconnect from the target device. This can happen if:

* The app is closed.
* The app is rebuilt (a new native build is installed).
* The app crashes on the native side.
* The dev server (Metro) is quit.
* A physical device is disconnected.

On disconnect, a dialog will be shown with the message "Debugging connection was closed".

![A reconnect dialog shown when a device is disconnected](/assets/images/debugging-reconnect-menu-fc38b7d074e730cc41346286561f75b8.jpg)

From here, you can either:

* **Dismiss**: Select the close (`×`) icon or click outside the dialog to return to the DevTools UI in the last state before disconnection.
* **Reconnect**: Select "Reconnect DevTools", having addressed the reason for disconnection.
