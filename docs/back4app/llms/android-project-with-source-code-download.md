# Source: https://docs-containers.back4app.com/docs/android/android-project-with-source-code-download.md

---
title: Start from template
slug: docs/android/android-project-with-source-code-download
description: In this guide you learn how to download and start using a complete (frontend and backend) android studio app template.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T20:45:23.355Z
updatedAt: 2025-01-17T14:21:29.744Z
---

# Download an Android project with source code and start using Back4App

## Introduction

In this guide, you will learn how to get started with an Android application written in Java or Kotlin and connect it to Back4App.

If you want a detailed Quickstart guide or connect Back4App to an existing project, go to our [**Install Parse SDK tutorial**](https://www.back4app.com/docs/android/parse-android-sdk)

## Goal

Download an Android Template and connect it to Back4App

## Prerequisites

:::hint{type="info"}
- [**Android Studio version 4.1 or newer**](https://developer.android.com/studio/index.html)
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
:::

## 1 - Download the template

There are 2 Android templates, one written in Java and the other on Kotlin:

- [**Kotlin Example Repository**](https://github.com/templates-back4app/android-kotlin-starter-template)
- [**Java Example Repository**](https://github.com/templates-back4app/android-java-starter-template)

Choose the template that suits you, and proceed to download or import your project on Android Studio. Android Studio.

### **1.1 - Download Directly from GitHub**

Use the following commands to download and unzip your project template:

::::ExpandableHeading
**MacOS and Linux**

:::CodeblockTabs
```java
$ curl -LOk https://github.com/templates-back4app/android-java-starter-template/archive/master.zip && unzip master.zip
```

```kotlin
$ curl -LOk https://github.com/templates-back4app/android-kotlin-starter-template/archive/master.zip && unzip master.zip
```
:::
::::

:::ExpandableHeading
**Windows**

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/rwKky1GhnCrMeLd1Fqv_h_image.png)


:::

### **1.2 - Open the project on Android Studio**

After downloading the files, unzip them. Let’s open Android Studio

In the welcoming screen of Android Studio, choose **‘Open an Existing Project’** and select the project’s folder.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/YTGfM9yPvulBzq16XurNv_image.png)

Choose your downloaded and unzipped folder’s location and open it.

Please wait until the finish of the Gradle Run process. Now you can see Gradle console bottom tabs in Android Studio.

### **1.3 - Import from GitHub(Optional Path)**

You can import the repository link directly to Android Studio. On Android Studio welcoming screen, choose **‘Get from Version Control’**

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/9-PUyUTdaJPyxMaQ8YhKD_image.png)

Android Studio will ask you for the Git repository link and the desired project path. You can find repository links at the start of this section.

You can find repository links in the start of this section

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Hzljs-WMmNnIWQQjAsofd_image.png)

After filling the URL and Directory fields, click on the **Clone** button. Then Android Studio will copy and open the project for you. Please wait until the finish of the Gradle Run process. Now you can see Gradle console bottom tabs in Android Studio

Android Studio will copy and open project for you

Please wait until gradle run is finished.You can see gradle console bottom tabs in Android Studio

## 2 - Get your App Keys

In this guide we will use following files in project :

AndroidManifest.xml - We will set our Back4App credentials as \<meta-data> and app permissions
App.java (App.kt for kotlin) - We will modify our initialization code in here
MainActivity.java (MainActivity.kt for kotlin) - Will contain our very first code for creating a Parse Object
strings.xml - We will store and read Back4App setup credentails from here
build.gradle - We will set our Parse Android SDK version in here

In order to connect your App project to Back4App’s server, you’ll need three primary information the server URL, the Application ID, and the Client Key.
In an Android project, strings.xml is a perfect place to set this information. It is where Parse Android SDK reads Application key values to make a connection with your Back4App App.
The server URL is already on the project. You’‘ll need now go to Back4App, copy your App keys, and update your strings.xml with those values:

1. Open your strings file: .../app/src/main/res/values/strings.xml

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/KJ-smC7t6unznvL7h0gsv_image.png)

&#x20;    2\. Go to your App Dashboard at [**Back4App Website.**](https://www.back4app.com/)

&#x20;    3\. Find you keys on: App Settings > Security & Keys.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/5mOgO_acno_d2_SrvkCQH_image.png)

&#x20;    4\. Return to your strings.xml file and paste your applicationId and clientKey.

```xml
1  <resources>
2      <string name="app_name">Back4AppExample</string>
3      <string name="back4app_server_url" translatable="false">https://parseapi.back4app.com/</string>
4        
5      <!-- Paste BOTH keys here  -->
6      <string name="back4app_app_id" translatable="false">PASTE_YOUR_APPLICATION_ID_HERE</string>
7      <string name="back4app_client_key" translatable="false">PASTE_YOUR_CLIENT_KEY_HERE</string>
8  </resources>
```

&#x20;    5\. Open your build.gradle (Module\:Back4AppExample.app) file in Gradle Scripts from Project Explorer

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/nMxeKFNVGzA9mivKlP4wU_image.png)

In dependencies section change the Parse-SDK-Android value with version of your choice.

```java
 implementation "com.github.parse-community.Parse-SDK-Android:parse:latest-version-here"
```

After saving build.gradle run ‘Sync Now’

:::hint{type="info"}
You can see current version of SDK in here [**SDK Versions**](https://jitpack.io/#parse-community/Parse-SDK-Android).

:::

## 3 - Connect to Back4App

After setting up your App credentials, you are ready to connect with your Parse Server instance on Back4App.

This is the initialization code you’re going to use:

You can reach initialization code in project in App.java (App.kt for kotlin)

We are using App.java for our initialization because we need to establish connection before app takes any other action. App.java is the first Context to be created before any other Activity and Service and last to be destroyed.

Below initilization code gets App Keys from strings.xml and try to establish a connection with our Back4App server. We put our code onCreate() method because we want to connect to our server first before taking any other action.

:::CodeblockTabs
App.java

```java
1   public class App extends Application {
2       @Override
3       public void onCreate() {
4           super.onCreate();
5           Parse.initialize(new Parse.Configuration.Builder(this)
6                   .applicationId(getString(R.string.back4app_app_id))
7                   .clientKey(getString(R.string.back4app_client_key))
8                   .server(getString(R.string.back4app_server_url))
9                   .build());
10      }
11  }
```

App.kt

```kotlin
1   class App : Application() {
2       override fun onCreate() {
3           super.onCreate()
4           Parse.initialize(
5               Parse.Configuration.Builder(this)
6                       .applicationId(getString(R.string.back4app_app_id))
7                       .clientKey(getString(R.string.back4app_client_key))
8                       .server(getString(R.string.back4app_server_url))
9                       .build());
10      }
11  }
```
:::

Now it is time to add some codes for interacting with the server. Let’s open our MainActivity file.

Activity files are great for interacting with user. They are main purpose providing a User Interface.

You can choose which activity to show in launch in AndroidManifest.xml

```xml
1    <activity android:name=".MainActivity">
2        <intent-filter>
3            <action android:name="android.intent.action.MAIN" />
4            <category android:name="android.intent.category.LAUNCHER" />
5        </intent-filter>
6    </activity>
```

In our project MainActivity is set to open on launch.

In this code sample we have a Parse SDK code for saving a Parse Object to server and showing objectId of saved Parse Object to user with a TextView

:::CodeblockTabs
MainActivity.java

```java
1   public class MainActivity extends AppCompatActivity {
2       @Override
3       protected void onCreate(Bundle savedInstanceState) {
4           super.onCreate(savedInstanceState);
5           setContentView(R.layout.activity_main);
6           TextView textView = findViewById(R.id.textView);
7           ParseObject firstObject = new  ParseObject("FirstClass");
8           firstObject.put("message","Hey ! First message from android. Parse is now connected");
9           firstObject.saveInBackground(e -> {
10              if (e != null){
11                  Log.e("MainActivity", e.getLocalizedMessage());
12              }else{
13                  Log.d("MainActivity","Object saved.");
14                  textView.setText(String.format("Object saved. %s", firstObject.getObjectId()));
15              }
16          });
17      }
18  }
```

MainActivity.kt

```kotlin
1   class MainActivity : AppCompatActivity() {
2       override fun onCreate(savedInstanceState: Bundle?) {
3           super.onCreate(savedInstanceState)
4           setContentView(R.layout.activity_main)
5           val textView = findViewById<TextView>(R.id.textView)
6           val firstObject = ParseObject("FirstClass")
7           firstObject.put("message","Hey ! First message from android. Parse is now connected")
8           firstObject.saveInBackground {
9               if (it != null){
10                  it.localizedMessage?.let { message -> Log.e("MainActivity", message) }
11              }else{
12                  Log.d("MainActivity","Object saved.")
13                  textView.text = String.format("Object saved. %s", firstObject.objectId)
14              }
15          }
16      }
17  }
```
:::

## 4 - Test the connection

1. Build your app in a device or virtual device (Shift+F10).

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/PWVvmanCmRcSYI9Ui3GO0_image.png)

:::hint{type="info"}
If you don’t have any virtual device to run app. You can create a new one from AVD Manager in Android Studio
:::

1. Wait until the Hello Word! screen appears. After Hello Word! you will see `Object saved`. Message this message will include saved object’s id.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/oGS_6wcZQJ-oLzJpxj54v_image.png" signedSrc size="50" width="340" height="726" position="center" caption}

&#x20;    2\. Login at [**Back4App Website**](https://www.back4app.com/).&#x20;

&#x20;    3\. Find your app and click on Dashboard > Database > Browser.

If everything works properly, you should find a class named FirstClass as follows:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/QYDpDyCwN9GNk-7HxLQFG_image.png)

## It’s done!

You can see objectId in dashboard and your app’s screen is matches !

At this point, you have learned how to get started with Android apps.

:::hint{type="success"}
Learn more by walking around our [**Android Tutorials&#x20;**](https://www.back4app.com/docs/android/android-project-with-source-code-download)or check [**Parse open source documentation for Android SDK.**](http://docs.parseplatform.org/android/guide/)
:::

