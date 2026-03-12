# Source: https://documentation.onesignal.com/docs/en/example-target-certain-android-manufacturers-and-devices.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Target certain Android manufacturers and devices

> Identify and target Android devices from manufacturers known to block push notifications when apps are swiped away, and use in-app messages to educate users on enabling proper settings.

Certain Android devices have a known issue where they do not get push notifications when the app is swiped away. More details on this [here](./notifications-show-successful-but-are-not-being-shown#the-app-is-force-stopped). This issue affects all push providers, but fortunately OneSignal provides a way to reach out to users of these devices to help educate them on how to enable push for your app if they swipe it away.

Using the Native Android SDK, you can easily check the `deviceModel` and `deviceManufacturer`. Then, based on this data, trigger the in-app message to ask those users to enable the proper settings on the device for your app.

Some example code looks like this:

<CodeGroup>
  ```java java theme={null}
  //Gets the device model
  String deviceModel = android.os.Build.MODEL;
  //Gets the device manufacturer
  String deviceManufacturer = android.os.Build.MANUFACTURER;
  HashSet<String> manufWithIssues = new HashSet<>(Arrays.asList("samsung","huawei","xiaomi","oppo","vivo","lenovo","sony","asus"));
  if (manufWithIssues.contains(deviceManufacturer.toLowerCase()){
    //Based on the device manufacturer you can trigger the IAM to show
    OneSignal.addTrigger("device_manuf", "issue_manuf");  //"issue_manuf" == deviceManufacturer
  }
  ```
</CodeGroup>

In this example, if the current device's manufacturer matches a manufacturer in the HashSet with known issues, it will be passed to the OneSignal `addTrigger` method which you can use to trigger the in-app message setup in your OneSignal Dashboard.

<Frame caption="Choose In-app message trigger">
    <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f18b86e-iam-target-devices-add-trigger.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=6e0131c435a16b3a010207c8c3b9f24b" alt="" width="1279" height="356" data-path="images/docs/f18b86e-iam-target-devices-add-trigger.png" />
</Frame>

An example message might say:

Your device may not be getting our notifications! 😱 Please check your device settings have our important alerts turned on:

Settings ➝ Device Management ➝ Battery ➝ Unmonitored apps ➝ Add this app 👍

Settings ➝ Apps ➝ this app ➝ App Settings ➝ Notifications ➝ Set as Priority 👍

<Frame caption="Image showing in-app editor with preview of in-app warning user they may only be getting certain notifications">
    <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/79a09e7-iam-target-certain-android-devices.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=23713a3d356dd3f1893d5d51e913f6cc" alt="" width="1922" height="1661" data-path="images/docs/79a09e7-iam-target-certain-android-devices.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
