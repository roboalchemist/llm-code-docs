# Source: https://docs.buildnatively.com/guides/integration/app-storage.md

# App Storage

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

### 🧋 Bubble.io Plugin

#### \[Element] Natively - Storage

#### Events:

* **Storage value received** - Get called when a new value received

#### States:

* **Latest requested storage value** - The latest received value by key
* **Latest requested storage key** - The latest requested key

#### Actions:

* **Store value to device storage**
  * key
  * value
* **Get value from device storage**
  * key
* **Reset device storage**
* **Remove value from device storage**
  * key

### 🛠 JavaScript SDK

#### Storage

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const storage = new NativelyStorage()
const get_storage_value_callback = function (resp) {
    console.log(resp.key);
    console.log(resp.value);
};
storage.setStorageValue(key, value);
storage.getStorageValue(key, get_storage_value_callback);
storage.removeStorageValue(key);
storage.resetStorage();
```

{% endcode %}
