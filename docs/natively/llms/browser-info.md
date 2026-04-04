# Source: https://docs.buildnatively.com/guides/integration/browser-info.md

# Browser Info

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

## 🧋 Bubble.io Plugin

### \[Element] Natively - Browser

#### Events:

* Device went offline
* Device back online

#### States:

* **isAndroidApp** - Yes / No
* **isIOSApp** - Yes / No
* **isNativeApp** - Yes / No
* **Connectivity** - Yes / No (Device is online or offline)

## 🛠 JavaScript SDK

### Device App Info

{% code overflow="wrap" lineNumbers="true" %}

```javascript
// Check if native app
const browserInfo = info.browserInfo();
console.log(browserInfo.isAndroidApp);
console.log(browserInfo.isIOSApp);
console.log(browserInfo.isNativeApp);

// Check connectivity (internet connection);
window.ononline = (e) => { console.log("online") };
window.onoffline = (e) => { console.log("offline") };
```

{% endcode %}
