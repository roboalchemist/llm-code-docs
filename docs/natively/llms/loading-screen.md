# Source: https://docs.buildnatively.com/guides/integration/loading-screen.md

# Loading Screen

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

### 🧋 Bubble.io Plugin

#### \[Action] Natively - Show Loading Screen

* Auto Hide - Automatically hides screen after page loaded. \
  !!! Use this carefully since the user can stack on the Loading screen.

#### \[Action] Natively - Hide Loading Screen

### 🛠 JavaScript SDK

#### Show Loading Screen

{% code overflow="wrap" lineNumbers="true" %}

```javascript
// Automatically hides screen after page loaded. 
// !!! Use this carefully since the user can stack on the Loading screen.
const autoHide = true; 
window.natively.showLoadingScreen(autoHide);
```

{% endcode %}

#### Hide Loading Screen

```javascript
window.natively.hideLoadingScreen();
```
