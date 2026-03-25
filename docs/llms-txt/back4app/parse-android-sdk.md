# Source: https://docs-containers.back4app.com/docs/android/parse-android-sdk.md

---
title: Install Parse SDK
slug: docs/android/parse-android-sdk
description: Learn how to install Parse Android SDK into your Android Studio project
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T20:07:56.176Z
updatedAt: 2025-01-17T19:28:15.041Z
---

# Install Parse SDK on your Android Studio Project

## Introduction

In this section you learn how to install Parse Android SDK into your Android Studio project.

This tutorial uses a basic app created in Android Studio Arctic Fox 2020.3.1 Patch 1 with compileSdk 30 , minSdk 21 and targetSdk 30

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our Github repositories

- [**Kotlin Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Kotlin)
- [**Java Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Java)
:::

## Goal

Learn how to install Parse-SDK on your Android project.

## Prerequisites

:::hint{type="info"}
**To complete this section, you will need:**

- An app created at Back4App.
  - **Note:&#x20;**&#x49;f you don’t have an app now please follow the [**New Parse App tutorial&#x20;**](https://www.back4app.com/docs/get-started/new-parse-app)to learn how to create a Parse app at Back4App.
- [**Android Studio**](https://developer.android.com/studio/index.html)
- Basic android app.
  - **Note:&#x20;**&#x49;f you don’t have a basic app created you can follow the [**Create a Project tutorial**](https://developer.android.com/studio/projects/create-project.html) from Android Studio official website.
:::

:::hint{type="danger"}
Note: Parse Android SDK works with compileSdk 27 and targetSdk 27 or higher.
:::

## 1 - Install SDK

We need to implement Parse SDK to our Android project for this we will use [**Gradle**](https://www.gradle.org/), an open-source build automation tool that is designed to be flexible enough to build almost any type of software. Android Studio uses Gradle for build process and import external libraries like Parse SDK.

1 - In your Android Studio project, open your settings.gradle file.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/5d_tVQHxlUjkVgdXG420s_image.png)

Now we will add [**Jitpack**](https://jitpack.io/) to our Project. Jitpack is a package repository for JVM and Android projects.

2 - Now we need to add `maven {url 'https://jitpack.io'}` line to `repositories{}` tag in the settings.gradle file:

```java
1   repositories {
2      ...
3      ...
4     maven { url 'https://jitpack.io' }
5   }
```

3 - It’s also necessary to look in the `android{}` tag if your compileSdk is **27** or higher and also if your targetSdk is **27** or higher. If they aren’t, you **must change** these versions to **27** or higher, otherwise your Parse SDK for Android may not work properly. After checking this, your build.gradle (Module\:app) should look like the one in the image below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/XvKscevOVe8mNMeFFKS93_image.png)

4 - If all previous steps are set now we are able to add Parse Android SDK to our project.

:::BlockQuote
implementation "com.github.parse-community.Parse-SDK-Android\:parse"
:::

In `dependencies{}` tag change the latest-version-here value with version of your choice. It will look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/PEnrdlXhjwCx2EMPe8_-s_image.png)

:::hint{type="info"}
You can see current version of SDK in here [**SDK Versions.**](https://jitpack.io/#parse-community/Parse-SDK-Android)
:::

5 - Now we need to sync our build.gradle to last changes to effect our project.

:::hint{type="success"}
To learn more about adding support libraries to your Android Studio Project, see the [**Android Studio’s Support Library Setup page.**](https://developer.android.com/topic/libraries/support-library/setup.html)
:::

## 2 - Connect to Back4App

Now it is time to use Android Parse SDK in action. We need internet access and server credentials to connect to Back4App.

To use Parse SDK, our application need to have access to the internet network. To allow our app to have it, we need to grant permissions in the AndroidManifest.xml file. Also, we have to set up the app’s credentials to connect our app to Back4App. For achiving this we need to follow the steps below.

1 - Go to app > manifests > AndroidManifest.xml in your Android Studio Project.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/af4mtPasGyAzepVI6ETba_image.png)

2 - Now, before the application tag in the AndroidManifest.xml file, copy the following code snippet:

```java
1   <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
2   <uses-permission android:name="android.permission.INTERNET"/>
```

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/jub_rXBXhlLxrcPUn3VJ-_image.png)

3 - Inside the application section of the AndroidManifest.xml file, add the following code:

```java
1      <meta-data
2          android:name="com.parse.SERVER_URL"
3          android:value="@string/back4app_server_url" />
4     <meta-data
5          android:name="com.parse.APPLICATION_ID"
6          android:value="@string/back4app_app_id" />
7     <meta-data
8          android:name="com.parse.CLIENT_KEY"
9          android:value="@string/back4app_client_key" />
```

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7OZujVFUP87UrL-MzQRP6_image.png)

4 - Go to app > res > values > strings.xml file.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/RHmeXgu8hTiyJ00z8JYYz_image.png)

5 - In the strings.xml file, add the following code:

```xml
1       <string name="back4app_server_url">https://parseapi.back4app.com/</string>
2
3       <!-- Paste BOTH strings as required -->
4       <string name="back4app_app_id">PASTE_YOUR_APPLICATION_ID_HERE</string>
5       <string name="back4app_client_key">PASTE_YOUR_CLIENT_KEY_HERE</string>
```

6 - Leave the string.xml opened and go to [**Back4App Website**](https://www.back4app.com/).
Now you will find your keys to replace in the code. Go your Dashboard and then click on App Settings > Security & Keys.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ctca44UgoK4mWJxsTFtKs_image.png)

## 3 - Initialize Parse SDK in Our App

In this step we will complete the Parse Initialization using App Id and Client key which we have obtained at the end of Step 2.

We recommend you to write the installation codes in the App.java or App.kt files which you will create. The reason for this, to ensure that our Parse SDK initialize codes will work before any other Activity or Context, Application Context is the first that creates and last destroy.
So, create the App.javain the same folder as your MainAcitivty, and then follow the steps below:

1 - Import parse library to your App file:

```java
1  import com.parse.Parse;
```

2 - Inside App file call the following code:

:::CodeblockTabs
App.java

```java
1    public class App extends Application {
2       @Override
3       public void onCreate() {
4          super.onCreate();
5          Parse.initialize(new Parse.Configuration.Builder(this)
6                   .applicationId(getString(R.string.back4app_app_id))
7                   .clientKey(getString(R.string.back4app_client_key))
8                   .server(getString(R.string.back4app_server_url))
9                   .build());
10         }
11      }
```

App.kt

```kotlin
1    class App : Application() {
2       override fun onCreate() {
3          super.onCreate()
4          Parse.initialize(
5                Parse.Configuration.Builder(this)
6                      .applicationId(getString(R.string.back4app_app_id))
7                      .clientKey(getString(R.string.back4app_client_key))
8                      .server(getString(R.string.back4app_server_url))
9                      .build());
10      }
11   }
```
:::

Please check the image below as an example using Java:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/H1xURGFgeMWMMiNgaleqd_image.png)

We put our code to onCreate() method because we want to connect to our server first before taking any other action.

Don’t forget to define this file in the AndroidManifest.xml. For doing this, go to the AndroidManifest.xml file and add the following line of code inside the applicationtag:

:::BlockQuote
android=".App"
:::

At the end, your AndroidManifest.xml should look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/y6HicUiYpm96rJzns3Mvg_image.png)

:::hint{type="info"}
If the name of the java file that extends Application that you created on the previous step isn’t “App”, don’t forget that the code above should have the correct name of the file (android\:name=".name\_of\_the\_file").
:::

## 4 - Test your connection

To test your connection with Parse SDK, let’s save an object in the MainActivity of your Android Studio Project.

1 - Go to your Android Studio Project and add the following code to your onCreate() method in order to save your first Parse Object of the application into your Dashboard.

:::CodeblockTabs
App.java

```java
1    public class MainActivity extends AppCompatActivity {
2       @Override
3       protected void onCreate(Bundle savedInstanceState) {
4          super.onCreate(savedInstanceState);
5          setContentView(R.layout.activity_main);
6          ParseObject firstObject = new  ParseObject("FirstClass");
7          firstObject.put("message","Hey ! First message from android. Parse is now connected");
8          firstObject.saveInBackground(e -> {
9             if (e != null){
10               Log.e("MainActivity", e.getLocalizedMessage());
11               }else{
12                  Log.d("MainActivity","Object saved.");
13               }
14            });
15         }
16      }
```

App.kt

```kotlin
1    class MainActivity : AppCompatActivity() {
2     override fun onCreate(savedInstanceState: Bundle?) {
3         super.onCreate(savedInstanceState)
4         setContentView(R.layout.activity_main)
5         val firstObject = ParseObject("FirstClass")
6         firstObject.put("message","Hey ! First message from android. Parse is now connected")
7         firstObject.saveInBackground {
8             if (it != null){
9                 it.localizedMessage?.let { message -> Log.e("MainActivity", message) }
10            }else{
11                Log.d("MainActivity","Object saved.")
12            }
13        }
14    }
15   }
```
:::

2 - Launch your app and go to [**Back4App Website**](https://www.back4app.com/). Find your app and go to its Dashboard.

3 - Now click on Database > Browser > First Class. You should see the First Class with an object, as shown in the image below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/HKOfg3OLg365GYhm6phIW_image.png)

## It’s done!

We completed the section! Now you have learned how to install the Parse SDK in your application.

:::hint{type="success"}
Learn more by walking around our [**Android Tutorials.**](https://www.back4app.com/docs/android/android-project-with-source-code-download)
:::

