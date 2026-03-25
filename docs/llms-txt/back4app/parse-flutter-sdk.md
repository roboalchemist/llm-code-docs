# Source: https://docs-containers.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk.md

---
title: Install Parse SDK
slug: docs/flutter/parse-sdk/parse-flutter-sdk
description: In this guide you learn how to install and connect the Parse Server SDK to your Flutter project
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-15T13:06:02.190Z
updatedAt: 2025-01-16T20:36:18.119Z
---

## Introduction



In this guide, you will learn how to get started with Back4App for your Flutter project using the **Flutter plugin for Parse Server**.

## Prerequisites

:::hint{type="info"}
To complete this tutorial, you will need:

- An app [**created**](https://www.back4app.com/docs/get-started/new-parse-app) on Back4App:
- [**Flutter version 3.3.x or later**](https://flutter.dev/docs/get-started/install)
- [**Android Studio&#x20;**](https://developer.android.com/studio)or [**VS Code installed**](https://code.visualstudio.com/) (with [**Plugins**](https://docs.flutter.dev/get-started/editor) Dart and Flutter)
:::

## 1. Install Parse SDK

Open your computer's cmd or terminal (depending on your operating system) and **go** into your Flutter projects directory. Run this command to create a new Flutter app.

:::BlockQuote
flutter create flutter\_parse
:::

Launch your Flutter app by running this command:

:::BlockQuote
cd flutter\_parse
flutter run
:::

Add the [**Parse SDK**](https://pub.dev/packages/parse_server_sdk_flutter) to your project dependencies running:

:::BlockQuote
flutter pub add parse\_server\_sdk\_flutter
:::

This command will `flutter get` and add the Parse SDK to your pubspec.yaml file.

## 2. Set up Parse SDK

The next step is to import the Parse SDK inside your project's main.dart file.

Inside main.dart, you can use:

```dart
import 'package:parse_server_sdk_flutter/parse_server_sdk_flutter.dart';
```

### **Initialize your Parse app**

Go to main.dart, and initialize Parse in your Flutter app:

```dart
1   void main() async {
2     const keyApplicationId = 'YOUR_APP_ID_HERE';
3     const keyClientKey = 'YOUR_CLIENT_KEY_HERE';
4     const keyParseServerUrl = 'https://parseapi.back4app.com';
5
6     await Parse().initialize(keyApplicationId, keyParseServerUrl,
7       clientKey: keyClientKey, debug: true);
8   }
```

:::hint{type="info"}
**Note:&#x20;**&#x54;he debug parameter in function Parse().initialize is set to true,  to allow displaying Parse API calls on the console. This configuration can assist in debugging the code. It is advisable to disable debug in the release version.
:::

To successfully connect your app to the Back4App servers, you must provide Parse SDK with your backend application credentials.

Update the string values with your Application Id and Client key.

Locate your Application ID and Client Key credentials by navigating to your app Dashboard > App Settings > Security & Keys.

![Image of the backend app ID ](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/IYCmXJi-0nsTFw-agj-HK_testapp-credentials.png "Flutter app backend")

Copy these credentials and replace in main.dart.

- `keyApplicationId = App Id`
- `keyClientKey = Client Key`


3\. Test your Parse connection
------------------------------

You should test the SDK to verify that Parse and your backend is working with your Flutter application.

It will create an object on your project called `First Class.`

Let’s add the test code to main.dart as follows:

```dart
1 void main() async {
2   final keyApplicationId = 'YOUR_APP_ID_HERE';
3   final keyClientKey = 'YOUR_CLIENT_KEY_HERE';
4   final keyParseServerUrl = 'https://parseapi.back4app.com';
5
6   await Parse().initialize(keyApplicationId, keyParseServerUrl,
7        clientKey: keyClientKey, autoSendSessionId: true);
8
9  var firstObject = ParseObject('FirstClass')
10    ..set(
11        'message', 'Hey, Parse is now connected!🙂');
12  await firstObject.save();
13  
14  print('done');
15 }
```

Launch your app and go to the [**Back4App Website**](https://www.back4app.com/). Find your app and navigate to the Dashboard.

Now go to `Database` > `Browser` > `First Class`. You should see the First Class with an object, as shown in the image below.

![Image of a new class object created in the backend](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/PLtrsfttnteqJfjxCrU8N_firstclass.png "First Class")

## You're done!

Now you know exactly how to get started using Back4app. You learned how to install the Parse SDK in your Flutter Application and connect to your Back4App backend.
