# Source: https://docs-containers.back4app.com/docs/get-started/welcome.md

---
title: Quickstart
slug: docs/get-started/welcome
description: Release your App faster, reducing drastically your development effort by providing a flexible, scalable and easy-to-use backend platform.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-16T19:22:06.326Z
updatedAt: 2025-08-07T18:29:53.382Z
---

Back4app is a low-code backend platform that simplifies building modern applications. This guide will help you quickly set up Back4app and start saving data.

## Back4app Main Features

- Database (real-time capability)
- Cloud Code Functions
- APIs (GraphQL and REST)
- File Storage
- Authentication
- Web Deployment
- Push Notifications

## 5-minutes quick start

After creating your Back4app account and first app, go to your App Dashboard and get your App Keys under App Settings -> Security & Keys(check the image below). Note that you will always need two keys to connect with Back4app, the Application ID, and another key according to the SDK you will use.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/pGTX6D2rGm8Ohe9w99cin_app-settings.png)

### 1. Install and Configure the Parse SDK

To integrate the Parse SDK, follow these general steps:

**Install the Parse SDK:**

- **JavaScript / Node.js**: `npm install parse --save`
- **React Native**: `npm install parse @react-native-async-storage/async-storage --save`, then run `cd ios && pod install`
- **Flutter**: Add `parse_server_sdk_flutter` to `pubspec.yaml`
- **Android (Java):** Add your app's `build.gradle` inside `dependencies{}`:&#x20;

:::CodeblockTabs
build.gradle

```java
implementation "com.github.parse-community.Parse-SDK-Android:parse:latest_version"
```
:::

- **iOS (Swift)**: Install CocoaPods `(sudo gem install cocoapods)` and add Parse to your `Podfile`

**Initialize the Parse SDK** with your Application ID and the appropriate key:

```javascript
Parse.initialize('YOUR_APPLICATION_ID', 'YOUR_JAVASCRIPT_KEY');
Parse.serverURL = 'https://parseapi.back4app.com/';
```

*The example above is for JavaScript/Node.js. Adjust accordingly for your platform.*

### 2. Save Data on Back4app

Create and save a sample object to confirm that the SDK is properly set up. Use the example below and adapt it to your programming language:

```javascript
async function saveNewPlayer() {
    const player = new Parse.Object('Player');
    player.set('name', 'Alex');
    player.set('yearOfBirth', 1997);
    player.set('emailContact', 'alex@email.com');
    player.set('attributes', ['fast', 'good endurance']);
    
    try {
        const result = await player.save();
        console.log('New object created with ID:', result.id);
    } catch (error) {
        console.error('Failed to save object:', error.message);
    }
}
```

After saving, you can verify the data in the **App Dashboard** on Back4app.

### 3. Platform-Specific Setup

**JavaScript - React / Angular**

- **Install** the SDK: `npm install parse --save`
- **Initialize** with your App Keys and Back4app server URL.

**Flutter**

1. Add `parse_server_sdk_flutter` in your `pubspec.yaml:`

:::CodeblockTabs
pubspec.yaml

```yaml
dependencies:
  parse_server_sdk_flutter: ^latest_version
```
:::

&#x20;   2\.  **Initialize** Parse in `main.dart:`

```dart
await Parse().initialize('YOUR_APPLICATION_ID', 'https://parseapi.back4app.com', clientKey: 'YOUR_CLIENT_KEY');
```

**Android (Kotlin/Java)**

- **Include** the SDK in `build.gradle` and configure network permissions in `AndroidManifest.xml`
- **Initialize** in `App.kt:`

```kotlin
Parse.initialize(new Parse.Configuration.Builder(this)
    .applicationId(getString(R.string.back4app_app_id))
    .clientKey(getString(R.string.back4app_client_key))
    .server(getString(R.string.back4app_server_url))
    .build()
);
```

**iOS (Swift)**

1. Add `ParseSwift` to your project using CocoaPods.
2. Initialize Parse in `AppDelegate.swift:`

:::CodeblockTabs
AppDelegate.swift

```swift
let configuration = ParseClientConfiguration {
    $0.applicationId = "YOUR_APPLICATION_ID"
    $0.clientKey = "YOUR_CLIENT_KEY"
    $0.server = "https://parseapi.back4app.com"
}
Parse.initialize(with: configuration)
```
:::

**PHP**

1. **Install the SDK** with Composer by creating a composer.json with:

:::CodeblockTabs
composer.json

```json
{
    "require": {
        "parse/php-sdk" : "1.6.*"
    }
}
```
:::

Then, run `composer.install`.

&#x20;   2\. **Initialize** Parse in your PHP script:

```php
require 'vendor/autoload.php';
ParseClient::initialize('YOUR_APP_ID', 'YOUR_REST_KEY', 'YOUR_MASTER_KEY');
ParseClient::setServerURL('https://parseapi.back4app.com', '/');
```

&#x20;   3\. **Save Data** in PHP:

:::CodeblockTabs
composer.json

```php
$player = new ParseObject("Player");
$player->set("name", "Alex");
$player->set("yearOfBirth", 1997);
$player->set("emailContact", "alex@email.com");
$player->setArray("attributes", ["fast", "good endurance"]);
$player->save();
```
:::

**.NET (C#)**

1. **Install** Parse SDK through NuGet Package Manager in Visual Studio.
2. **Initialize** Parse in your application:

```csharp
ParseClient.Initialize(new ParseClient.Configuration {
    ApplicationId = "YOUR_APP_ID",
    Server = "https://parseapi.back4app.com",
    ClientKey = "YOUR_CLIENT_KEY"
});
```

&#x20;   3\. **Save Data** in C#:

```csharp
var player = new ParseObject("Player")
{
    ["name"] = "Alex",
    ["yearOfBirth"] = 1997,
    ["emailContact"] = "alex@email.com",
    ["attributes"] = new List<object> { "fast", "good endurance" }
};
await player.SaveAsync();
```

**REST API**

1. **Save Data** via REST by sending a POST request:

```bash
curl -X POST \
-H "X-Parse-Application-Id: YOUR_APP_ID" \
-H "X-Parse-REST-API-Key: YOUR_REST_KEY" \
-H "Content-Type: application/json" \
-d '{"name":"Alex", "yearOfBirth":1997, "emailContact":"alex@email.com", "attributes":["fast", "good endurance"]}' \
https://parseapi.back4app.com/classes/Player
```

### 4. Additional Resources and Examples

There are many example apps and starter projects to get going

- [**ReactJS Slack Clone**](https://github.com/templates-back4app/react-js-slack-clone) - A React template using real-time, relational queries and authentication.
- [**Flutter User Login/SignUp**](https://github.com/templates-back4app/flutter-user-signup) - A user sign-up/login flutter template using Parse.User class.
- [**React Native Associations**](https://github.com/templates-back4app/react-native-js-associations)  - A template on React Native digging deeper into associations and relational queries using Pointers andRelations.
- [**Flutter File Storage**](https://www.back4app.com/docs/flutter/parse-sdk/flutter-save-file)  - Saving files from a Flutter app.
- [**GeoPointers on Kotlin-Android**](https://github.com/templates-back4app/AndroidGeoLocationKotlin)  - Exploring GeoPointers in Android.
- [**ToDo List example is Swift-iOS**](https://github.com/templates-back4app/ios-template-todo-list)  - A ToDo List example in Swift.

Find more examples in [**Back4app Templates.**](https://github.com/templates-back4app)

## &#x20;What to do Next?

After completing the quick start, we encourage you to explore Back4app's key features through the guides below. You'll learn how to store and query relational data, implement cloud functions for backend logic, use real-time subscriptions to keep users updated, manage file storage, send push notifications, and set up authentication. Select the technology that best fits your project and enjoy the journey!

::::LinkArray
:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/pEkmfq5PdkxC3lmfRzYsE_1.png"}
&#x20;       [**React Native**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/tPONkoW1aPPhiAdTvbvrx_sem-nome-rectangle-sticker-landscape.png"}
[**Flutter**](https://www.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vqJJw7ljIhPJ1Yfz7mD9n_3.png"}
[**Android&#x20;**](https://www.back4app.com/docs/android/android-project-with-source-code-download)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/rzkB1YU-Feimt_SWfZUuC_4.png"}
[**iOS**](https://www.back4app.com/docs/ios/ios-app-template)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/GsQE6ru-jj2rRbUt7P3Tr_5.png"}
****[**Javascript**](https://www.back4app.com/docs/javascript/parse-javascript-sdk)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/35IqTes9QhdmijlReYBYZ_6.png"}
[**GraphQL**](https://www.back4app.com/docs/parse-graphql/graphql-getting-started)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/D4RecbrtvjfbKUfb4yRbP_7.png"}
[**Ionic**](https://www.back4app.com/docs/js-framework/ionic/ionic-template)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/yOia2J8LzE-r1WSHQ7ZSQ_8.png"}
[**Xamarin**](https://www.back4app.com/docs/xamarin/xamarin-templates)
:::
::::

