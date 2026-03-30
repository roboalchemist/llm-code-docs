# Source: https://docs.buildnatively.com/guides/integration/control-style-and-colors.md

# Control Style & Colors

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

### 🧋 Bubble.io Plugin

#### \[Action] Natively - Background Color

Updating the [App background-color](https://docs.buildnatively.com/guides/integration/broken-reference)

#### \[Action] Natively - Progress Color

Updating a [progress bar color](https://docs.buildnatively.com/guides/integration/broken-reference)

#### \[Action] Natively - Swipe Navigation

Enable or disable [Swipe Navigation](https://docs.buildnatively.com/guides/integration/broken-reference)

#### \[Action] Natively - Status Bar Style

Updating the [Status Bar Style](https://docs.buildnatively.com/guides/integration/broken-reference)

#### \[Action] Natively - Pull to refresh

Enable or disable [Pull to refresh](https://docs.buildnatively.com/guides/integration/broken-reference)

#### \[Action] Natively - Orientation

Change and lock device orientation in the app

#### \[Action] Natively - Show Progress

Hide / show progress in the app

#### \[Action] Natively - Close App

Closes (kill) the app

#### \[Action] Natively - Enable Wake Lock

Keeps the screen unlocked

#### \[Action] Natively - DIsable Wake Lock

Allows screen to auto lock

### 🛠 JavaScript SDK

#### Updating the [App background-color](https://docs.buildnatively.com/guides/integration/broken-reference)

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const color = "#000000";
window.natively.setAppBackgroundColor(color);
```

{% endcode %}

#### Updating a [progress bar color](https://docs.buildnatively.com/guides/integration/broken-reference)

{% code lineNumbers="true" %}

```javascript
const color = "#000000";
window.natively.setAppProgressColor(color);
```

{% endcode %}

#### Enable or disable [Swipe Navigation](https://docs.buildnatively.com/guides/integration/broken-reference)

{% code lineNumbers="true" %}

```javascript
const toggle = true;
window.natively.setAppSwipeNavigationIOS(toggle);
```

{% endcode %}

#### Updating the [Status Bar Style](https://docs.buildnatively.com/guides/integration/broken-reference)

{% code lineNumbers="true" %}

```javascript
const style = "NONE"; // DARK, LIGHT or NONE
window.natively.setAppStatusBarStyleIOS(toggle);
```

{% endcode %}

#### Enable or disable [Pull to refresh](https://docs.buildnatively.com/guides/integration/broken-reference)

{% code lineNumbers="true" %}

```javascript
const toggle = true;
window.natively.setAppPullToRefresh(toggle);
```

{% endcode %}

#### Change and lock device orientation in the app

{% code lineNumbers="true" %}

```javascript
const orientation = "PORTRAIT"; // DEFAULT, PORTRAIT or LANDSCAPE
window.natively.setAppOrientation(orientation);
```

{% endcode %}

#### Show/Hide Progress in the app

{% code lineNumbers="true" %}

```javascript
const toggle = false;
window.natively.showProgress(toggle);
```

{% endcode %}

#### Close the app

{% code lineNumbers="true" %}

```javascript
window.natively.closeApp()
```

{% endcode %}

#### Wake Lock

```javascript
window.natively.enableWakelock(); // Keeps the screen unlocked
and window.natively.disableWakelock(); // Allows screen to auto lock
```
