# Source: https://docs.buildnatively.com/guides/integration/toast-banner.md

# Toast/Banner

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

### 🧋 Bubble.io Plugin

#### \[Action] Natively - Show Toast

* Text
* Type - DEFAULT, DARK, ERROR, SUCCESS, WARNING, or MATRIX

#### \[Action] Natively - Show Banner

* Title
* Description
* Type - SUCCESS, ERROR, or INFO

### 🛠 JavaScript SDK

#### Show App Toast

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const type = "DEFAULT"; // DEFAULT, DARK, ERROR, SUCCESS, WARNING, or MATRIX
const text = "Test text";
window.natively.showAppToast(type, text);
```

{% endcode %}

#### Show App Banner

```javascript
const type = "SUCCESS"; // SUCCESS, ERROR, or INFO
const title = "Test Title";
const description = "Test Description";
window.natively.showAppBanner(type, title, description);
```
