# Source: https://docs-containers.back4app.com/docs/get-started/parse-sdk.md

---
title: Connect to Back4app
slug: docs/get-started/parse-sdk
description: In this guide you'll learn how to install and connect the Parse SDK to your project and get ready to use Parse
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-18T15:18:12.638Z
updatedAt: 2025-01-27T19:41:38.269Z
---

Now that you've created your application on Back4app, you’re just a few steps away from using its backend features. This guide will walk you through connecting your app to Back4app's servers using the Parse SDK or REST APIs.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- **Create an Application**: [**Create a new app on Back4app**](https://www.back4app.com/docs/get-started/new-parse-app) if you haven't already.
- **Access Application Keys**: Go to **Server Settings > Core Settings > App ID and Keys** to find your keys. You will use these to authenticate with Back4app.
:::

## 1 - Install the Parse SDK

Based on the platform you’re working with, follow one of the installation methods below:

### JavaScript (Web or Node.js)

:::BlockQuote
\# Install the Parse SDK
$ npm install parse --save
:::

### React Native

:::BlockQuote
\# Install Parse and AsyncStorage for React Native
$ npm install parse @react-native-async-storage/async-storage --save

\# Run pod install for iOS
cd ios && pod install
:::

### Flutter

Add Parse SDK to `pubspec.yaml`

:::BlockQuote
dependencies:
&#x20; parse\_server\_sdk\_flutter: ^latest\_version
:::

:::hint{type="info"}
To check the latest version, you can check [**here.**](https://pub.dev/packages/parse_server_sdk_flutter)
:::

### Android

Open your `build.gradle` file (Module: app) and add the following dependencies:

:::BlockQuote
repositories \{
&#x20;   mavenCentral()
&#x20;   jcenter()
&#x20;   maven \{ url 'https\://jitpack.io' }
}
dependencies \{
&#x20;   implementation 'com.github.parse-community.Parse-SDK-Android\:parse\:latest\_version'
}
:::

:::hint{type="info"}
To check the latest version, you can check [**here.**](https://github.com/parse-community/Parse-SDK-Android)
:::

### iOS

1. Install CocoaPods

:::BlockQuote
sudo gem install cocoapods
:::

&#x20;   2\.  Add Parse SDK to your Podfile:

:::BlockQuote
pod 'ParseSwift
:::

:::hint{type="info"}
You can also use the Swift Package Manager (SPM) or Carthage to install ParseSwift. Click [**here**](https://github.com/parse-community/Parse-Swift?tab=readme-ov-file#installation) to know more.
:::

### PHP

1. Create a `composer.json` file in your project root with the following content:

:::BlockQuote
\{
&#x20; "require": \{
&#x20;   "parse/php-sdk": "latest\_version\_here"
&#x20; }
}
:::

Then run:

:::BlockQuote
composer install
:::

&#x20;   2\.  Or clone from GitHub: &#x20;

:::BlockQuote
git clone https\://github.com/parse-community/parse-php-sdk.git
:::

:::hint{type="info"}
For more details, see [**this guide**](https://docs.parseplatform.org/php/guide/#installation).
:::

### .NET

1. Add Parse SDK from NuGet Packages: Open Visual Studio, go to Solution Explorer, right-click your project, and select `Manage NuGet Packages...`
2. Search for Parse and install it.

:::hint{type="info"}
For more details, see [**this guide**](https://github.com/parse-community/Parse-SDK-dotNET).
:::

## 2 - Initialize the Parse SDK&#x20;

Once the SDK is installed, initialize it in your app. Below are examples for each platform:

:::CodeblockTabs
```javascript
// Import Parse SDK
const Parse = require('parse/node');

// Initialize with your Back4app keys
Parse.initialize("YOUR_APP_ID", "YOUR_JS_KEY");  // Replace with your App ID and JS Key
Parse.serverURL = 'https://parseapi.back4app.com';
```

RN

```javascript
import Parse from 'parse/react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Set AsyncStorage
Parse.setAsyncStorage(AsyncStorage);

// Initialize Parse
Parse.initialize("YOUR_APP_ID", "YOUR_JS_KEY");  // Replace with your App ID and JS Key
Parse.serverURL = 'https://parseapi.back4app.com';
```

Flutter

```dart
import 'package:parse_server_sdk_flutter/parse_server_sdk_flutter.dart';

void main() async {
  await Parse().initialize(
    'YOUR_APP_ID',    // Replace with your App ID
    'https://parseapi.back4app.com',
    clientKey: 'YOUR_CLIENT_KEY',  // Replace with your Client Key
  );
}
```

Android

```java
Parse.initialize(new Parse.Configuration.Builder(context)
    .applicationId("YOUR_APP_ID")  // Replace with your App ID
    .clientKey("YOUR_CLIENT_KEY")  // Replace with your Client Key
    .server("https://parseapi.back4app.com")
    .build()
);
```

iOS

```swift
import ParseSwift

ParseSwift.initialize(applicationId: "YOUR_APP_ID", 
                     clientKey: "YOUR_CLIENT_KEY", 
                     serverURL: URL(string: "https://parseapi.back4app.com")!)
```

```php
require 'vendor/autoload.php';

ParseClient::initialize('YOUR_APP_ID', 'YOUR_REST_KEY', 'YOUR_MASTER_KEY');
ParseClient::setServerURL('https://parseapi.back4app.com', '/');
```

.NET

```csharp
ParseClient.Initialize(new ParseClient.Configuration {
    ApplicationId = "YOUR_APP_ID", // Replace with your App ID
    Key = "YOUR_MASTER_KEY"
    ServerURI = "https://parseapi.back4app.com/"
});
```
:::

## 3 - Save and Read your first Data Object

To ensure your connection is set up correctly, save and retrieve a test object in your Back4app app. Here’s an example:

:::CodeblockTabs
```javascript
// Create and save a test object
const Person = new Parse.Object("Person");
Person.set("name", "Jon Snow");
Person.set("age", 30);

Person.save()
  .then(() => console.log("Successfully connected to Back4app!"))
  .catch((error) => console.error("Connection error:", error.message));
```

RN

```javascript
// Create and save a test object
const testConnection = async () => {
  const Person = new Parse.Object("Person");
  Person.set("name", "Jon Snow");
  Person.set("age", 30);

  try {
    await Person.save();
    console.log("Successfully connected to Back4app!");
  } catch (error) {
    console.error("Connection error:", error.message);
  }
};

testConnection();
```

Flutter

```dart
import 'package:parse_server_sdk_flutter/parse_server_sdk_flutter.dart';

// Test connection by saving an object
void testConnection() async {
  var person = ParseObject('Person')
    ..set('name', 'Jon Snow')
    ..set('age', 30);

  var response = await person.save();

  if (response.success) {
    print("Successfully connected to Back4app!");
  } else {
    print("Connection error: ${response.error?.message}");
  }
}

testConnection();
```

Android

```java
import com.parse.ParseObject;
import com.parse.SaveCallback;
import com.parse.ParseException;

// Test connection by saving an object
ParseObject person = new ParseObject("Person");
person.put("name", "Jon Snow");
person.put("age", 30);

person.saveInBackground(new SaveCallback() {
    @Override
    public void done(ParseException e) {
        if (e == null) {
            Log.i("ParseConnection", "Successfully connected to Back4app!");
        } else {
            Log.e("ParseConnection", "Connection error: " + e.getMessage());
        }
    }
});
```

iOS

```swift
import ParseSwift

// Test connection by saving an object
struct Person: ParseObject {
    var objectId: String?
    var name: String?
    var age: Int?

    // Required ParseObject properties
    var createdAt: Date?
    var updatedAt: Date?
    var ACL: ParseACL?

    init() {
        // Default empty initializer
    }
}

func testConnection() {
    var person = Person()
    person.name = "Jon Snow"
    person.age = 30

    person.save { result in
        switch result {
        case .success:
            print("Successfully connected to Back4app!")
        case .failure(let error):
            print("Connection error: \(error.localizedDescription)")
        }
    }
}

testConnection()
```

```php
require 'vendor/autoload.php';

// Create and save a test object
$person = new ParseObject("Person");
$person->set("name", "Jon Snow");
$person->set("age", 30);

try {
    $person->save();
    echo "Successfully connected to Back4app!";
} catch (ParseException $error) {
    echo "Connection error: " . $error->getMessage();
}
```

.NET

```csharp
using Parse;

// Create and save a test object
var person = new ParseObject("Person");
person["name"] = "Jon Snow";
person["age"] = 30;

await person.SaveAsync().ContinueWith(t => {
    if (t.IsCompletedSuccessfully) {
        Console.WriteLine("Successfully connected to Back4app!");
    } else {
        Console.WriteLine("Connection error: " + t.Exception?.Message);
    }
});
```

REST API

```curl
//Saving your First Data Object on Back4App

curl -X POST \
-H "X-Parse-Application-Id: APPLICATION_ID" \
-H "X-Parse-REST-API-Key: REST_API_KEY" \
-H "Content-Type: application/json" \
-d '{"name":"John Snow","age":27}' \
https://parseapi.back4app.com/classes/Person

//Reading your First Data Object from Back4app

curl -X GET \
-H "X-Parse-Application-Id: APPLICATION_ID" \
-H "X-Parse-REST-API-Key: REST_API_KEY" \
https://parseapi.back4app.com/classes/Person/OBJECT-ID-HERE
```
:::

:::hint{type="info"}
After running these code snippets, check your Back4app Dashboard to verify that the object was saved successfully. This confirms that your connection to Back4app is working.
:::

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/3z1v07mHc4n6l-sslZStt_screenshot-2024-11-08-at-115652.png)

## What to do Next?

After a quick start, we recommend keeping exploring the Back4app main features by checking out the guides below.

::::LinkArray
:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/pEkmfq5PdkxC3lmfRzYsE_1.png"}
&#x20;     &#x20;**&#x20;  &#x20;**[**React Native**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/tPONkoW1aPPhiAdTvbvrx_sem-nome-rectangle-sticker-landscape.png"}
&#x20;               [**Flutter**](https://www.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vqJJw7ljIhPJ1Yfz7mD9n_3.png"}
&#x20;            [**Android&#x20;**](https://www.back4app.com/docs/android/android-project-with-source-code-download)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/rzkB1YU-Feimt_SWfZUuC_4.png"}
&#x20;                  [**iOS**](https://www.back4app.com/docs/ios/ios-app-template)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/GsQE6ru-jj2rRbUt7P3Tr_5.png"}
&#x20;          [**Javascript**](https://www.back4app.com/docs/javascript/parse-javascript-sdk)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/35IqTes9QhdmijlReYBYZ_6.png"}
&#x20;              [**GraphQL**](https://www.back4app.com/docs/parse-graphql/graphql-getting-started)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/D4RecbrtvjfbKUfb4yRbP_7.png"}
&#x20;                [**Ionic**](https://www.back4app.com/docs/js-framework/ionic/ionic-template)
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/yOia2J8LzE-r1WSHQ7ZSQ_8.png"}
&#x20;             [**Xamarin**](https://www.back4app.com/docs/xamarin/xamarin-templates)
:::
::::

&#x20;
