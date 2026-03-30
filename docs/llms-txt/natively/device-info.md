# Source: https://docs.buildnatively.com/guides/integration/device-info.md

# Device Info

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

## 🧋 Bubble.io Plugin

### \[Element] Natively - Device

**Initialize:**

* **Refresh App Info** action will be called on element load, so you can access it asap.

{% hint style="info" %}
Make sure to not add a lot of 'Natively - Device' elements because it will send a request to a device each time on load.
{% endhint %}

**Events:**

* App Info received
* App went foreground - User opened the app - **available starting from v2.12.2**
* App went background - User minimized the app (closed without exiting) - **available starting from v2.12.2**
* Keyboard is visible - User taps an input and keyboard appears - **available starting from v. 2.17.0**
* Keyboard is hidden - User closes the keyboard - **available starting from v. 2.17.0**
* Error occurred - Fires automatically when an HTTP request fails and the **Set Error Handler** action has been previously called on the current page. **- available starting from v. 2.26.0**

**States:**

* **Device** - Device model (iOS can be decoded with this [list](https://github.com/pbakondy/ios-device-list/blob/master/devices.json))
* **OS Version** - Android/iOS version
* **App Version**
* **Build Number**
* **Natively SDK Version**
* **OS Name** - "Android" / "iOS"
* **isDarkMode** - Yes / No
* **Orientation** - "PORTRAIT" / "LANDSCAPE"
* **Error Code:** The HTTP status code of the failed request (e.g., 404, 500)
* **Error Description:** A text description of the error provided by the requester endpoint
* **Error Response Data:** The raw response body (JSON/Text) returned by the server for the failed HTTP request (if available)

#### Actions:

* **Refresh App Info**
* **Set Error Handler** - Enables the custom error handling mode for the current page session. When Active, the app will not automatically display the native Error Screen when an HTTP request fails. Instead, it will trigger the **Error occurred** event.

#### How to use the Error Handler

To ensure consistent error handling across your app, we recommend placing the logic in a Reusable Element (like your Header or a dedicated technical Reusable) that exists on every page.

1. Place the **Natively - Device** element inside your Reusable Element
2. When Natively - Device's Device state is not empty (this ensures the element is fully initialized) > call **Set Error Handler** action\
   ![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FCWvYWUW4A2iGksgO2peU%2Ferror_handfler_bubble_action.png?alt=media\&token=7cc4de52-db99-4530-b7b5-a646cd3f2fea)
3. Create a workflow to handle the error when it happens (the event **Error occurred** is fired)\
   ![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FedcYmsQkAxUB0a1XigDp%2Ferror_handfler_bubble_event.png?alt=media\&token=9d4d443f-0c51-437f-92cd-b394fe39d929)
4. The error's details can also be visible in the Debug console<br>

## 🛠 JavaScript SDK

### Device App Info

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const info = new NativelyInfo()
const app_info_callback = function (resp) {
        console.log(resp.device); // iPhone14,2
        console.log(resp.osVersion); // 15.6
        console.log(resp.osName); // iOS / Android
        console.log(resp.buildVersion); // 1.0.0
        console.log(resp.buildNumber); // 1
        console.log(resp.sdkVersion); // 3
        console.log(resp.isDarkMode); // true/false
};
info.getAppInfo(app_info_callback);
// available starting from v2.12.2
const app_state_callback = function (resp) {
        if (resp.state) {
                // User opened the app (iOS "active", android "resume")
                console.log("App went foreground")
        } else {
                // User minimized the app (closed without exiting)
                // (iOS "inactive", android "pause")
                console.log("App went background")
        }
};
info.app_state(app_state_callback);
// available starting from v2.15.4
const keyboard_visibility_callback = function (resp) {
        if (resp.visible) {
                // Keyboard is visible
                console.log("Keyboard is visible")
        } else {
                // Keyboard is hidden
                console.log("Keyboard is hidden")
        }
};
// Error Handler. Available from v. 2.20.0
const error_handler_callback = function (resp) {
    console.log(resp.code); // 404, 500, 0
    console.log(resp.description); // "Network Request Failed", "Not Found"
    console.log(resp.url); // "https://api.example.com/v1/...
    console.log(resp.type); // "NETWORK_ERROR", "HTTP_ERROR"
    // response_data is usually an Object, so we stringify it to read it
    console.log(JSON.stringify(resp.response_data));
};
window.natively.setErrorHandler(error_handler_callback);
```

{% endcode %}

{% hint style="info" %}
**resp.device** value for iOS can be decoded with this [list](https://github.com/pbakondy/ios-device-list/blob/master/devices.json)
{% endhint %}

{% hint style="info" %}
Need to recognize the app and the web users? Check this out: [Browser Info](https://docs.buildnatively.com/guides/integration/browser-info)
{% endhint %}
