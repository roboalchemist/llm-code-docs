# Source: https://docs-containers.back4app.com/docs/android/working-with-users/android-twitter-login.md

---
title: Sign in with Twitter
slug: docs/android/working-with-users/android-twitter-login
description: In this guide you learn how to implement twitter login on your Android project
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-14T12:48:45.017Z
updatedAt: 2025-01-16T20:45:08.279Z
---

# How to add twitter login to your Android App

## Introduction

This section explains how you can create an app with user registration using Twitter Login and [**Parse Server core features**](https://www.back4app.com/product/parse-server) through Back4App.

It will look like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/3Fmyms7qN4uXug_8PjCkl_twitter-login.gif" signedSrc size="50" width="274" height="477" position="center" caption}

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our [**GitHub repository**](https://github.com/back4app/android-geopoints-tutorial).
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, we need:**

- [**Android Studio**](https://developer.android.com/studio/index.html)
- An app created on Back4App.
  - **Note:&#x20;**&#x46;ollow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- An android app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK tutoria**](https://www.back4app.com/docs/android/parse-android-sdk)l to create an Android Studio Project connected to Back4App.
- A device (or[**&#x20;virtual device**](https://developer.android.com/studio/run/managing-avds.html)) running Android 4.1 (Jelly Bean) or newer.
:::

## 1 - Twitter Set up

To start using Twitter functions, you need to:

1. Go to [**Twitter Application Management Website**](https://apps.twitter.com/), sign in with a Twitter account and click on Create New App.
2. Fill in the Application Details. When asked to specify Callback URLs, please insert twittersdk://. This is **mandatory** in order to enable authentication through Twitter.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/4KreLh6xuEZyCgXIVo4ge_image.png)

&#x20;    3\. Click on the Developer Agreement and then on Create your Twitter application.

&#x20;    4\. Open your Android Studio Project, find your build.gradle (Module: app) and in the dependencies\{} section add the following code to install the Parse Twitter Utils SDK for Android.

:::BlockQuote
*1  // Don't forget to change the line below with the latest version of Parse Twitter Utils SDK for Android*
2  implementation 'com.github.parse-community\:ParseTwitterUtils-Android\:latest.version.here'
:::

:::hint{type="info"}
Remember to update the version of Parse Facebook Utils SDK for Android to the latest one. You can find out which is the latest version at the [**JitPack website**](https://jitpack.io/), following these steps:

1. At JitPack website paste parse-community/ParseTwitterUtils-Androidin the Git repo urlbox.
2. After doing that, click on the Look upbutton. Then you should see the available versions of Parse Twitter Utils SDK for Android, as shown in the following image.&#x20;

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/i9JXLBBrNNsgQarX_tI8u_image.png)
:::

## 2 - Link your Twitter App with Back4App

1. In your Android Studio Project, in the Java file called App that extends Application that you created to initialize the Parse SDK, on its onCreatemethod, right after Parse.initialize()call, use the following code to initialize Parse Twitter Utils SDK.

```java
1   ParseTwitterUtils.initialize(getString(R.string.twitter_consumer_key),  getString(R.string.twitter_consumer_secret));
```

:::hint{type="danger"}
**If you don’t have an&#x20;**&#x41;pp.jav&#x61;**&#x20;file as described in this step, access the&#x20;**[**Install Parse SDK for Android**](https://www.back4app.com/docs/android/parse-android-sdk)**&#x20;documentation and make sure that you have followed all the steps required to install Parse SDK correctly. If you do not install Parse SDK properly your facebook login with Parse will not work.**
:::

&#x20;    2\. Go to app > res > values > strings.xml file.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/NwZ3K7fEHhCwOPW3tu19G_image.png)

1. In the strings.xml file add the following code:

:::BlockQuote
*\<!-- Change the following strings as required -->&#xA;*\<stringname="twitter\_consumer\_key">PASTE\_YOUR\_TWITTER\_CONSUMER\_KEY\</string>\<string name="twitter\_consumer\_secret">PASTE\_YOUR\_TWITTER\_CONSUMER\_SECRET\</string>
:::

&#x20;    2\. Leave the string.xml opened and go to Back4App Website, log in and click on My Apps. Find your app and then click on SERVER SETTINGS.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/DelZzb12DpiSGO6982KlB_image.png)

1. Find the “Twitter Login” block and click on Settings. The “Twitter Login” block looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SVtBq40Gp_rC_p1fs-9t9_image.png)

&#x20;    2\. Leave the *Back4App Twitter Login&#x20;*&#x70;age you visited opened and go to [**Twitter Application Management Website**](https://apps.twitter.com/) find your app and click on its name.

&#x20;    3\. Click on Keys and Access Tokens, copy the Consumer Key (API Key) and the Consumer Secret (API Secret) and paste it in the Back4App Twitter Login page, filling in the respective fields. To finish just click on SAVE. The Consumer Key (API Key) and the Consumer Secret (API Secret) looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wfT0e_pyIJNl7ipTqcUR4_image.png)

&#x20;    4\. Also, copy the Consumer Key (API Key) and the Consumer Secret (API Secret) and paste it in the strings.xml file of your Android Studio Project.

## 4 - Log In

1. Import to your LoginActivity:

:::BlockQuote
1   import android.app.AlertDialo&#x67;**;**
2   import android.app.ProgressDialo&#x67;**;**
3   import android.content.DialogInterfac&#x65;**;**
4   import android.content.Inten&#x74;**;**
5   import android.support.v7.app.AppCompatActivit&#x79;**;**
6   import android.os.Bundl&#x65;**;**
7   import android.view\.Vie&#x77;**;**
8   import android.util.Lo&#x67;**;**
9   import android.widget.Butto&#x6E;**;**
10  import android.widget.Toas&#x74;**;**
11
12  import com.parse.LogInCallbac&#x6B;**;**
13  import com.parse.ParseExceptio&#x6E;**;**
14  import com.parse.twitter.ParseTwitterUtil&#x73;**;**
15  import com.parse.ParseUse&#x72;**;**
16  import com.parse.SaveCallbac&#x6B;**;**
:::

&#x20;    2\. To implement Twitter Login, simply use below code:

```java
1   ParseTwitterUtils.logIn(LoginActivity.this, new LogInCallback() {
2
3        @Override
4        public void done(final ParseUser user, ParseException err) {
5            if (err != null) {
6                dlg.dismiss();
7                ParseUser.logOut();
8                Log.e("err", "err", err);
9            }
10           if (user == null) {
11               dlg.dismiss();
12               ParseUser.logOut();
13               Toast.makeText(LoginActivity.this, "The user cancelled the Twitter login.", Toast.LENGTH_LONG).show();
14               Log.d("MyApp", "Uh oh. The user cancelled the Twitter login.");
15           } else if (user.isNew()) {
16               dlg.dismiss();
17               Toast.makeText(LoginActivity.this, "User signed up and logged in through Twitter.", Toast.LENGTH_LONG).show();
18               Log.d("MyApp", "User signed up and logged in through Twitter!");
19               user.setUsername(ParseTwitterUtils.getTwitter().getScreenName());
20               user.saveInBackground(new SaveCallback() {
21                   @Override
22                   public void done(ParseException e) {
23                       if (null == e) {
24                           alertDisplayer("First tome login!", "Welcome!");
25                       } else {
26                           ParseUser.logOut();
27                           Toast.makeText(LoginActivity.this, "It was not possible to save your username.", Toast.LENGTH_LONG).show();
28                       }
29                   }
30               });
31           } else {
32               dlg.dismiss();
33               Toast.makeText(LoginActivity.this, "User logged in through Twitter.", Toast.LENGTH_LONG).show();
34               Log.d("MyApp", "User logged in through Twitter!");
35               alertDisplayer("Oh, you!","Welcome back!");
36           }
37       }
38   });
```

:::hint{type="info"}
In the example project, this code is placed inside aLOGIN VIA TWITTERbutton callback.
:::

&#x20;    3\. It’s interesting to add some method to display Alert Dialogs and make the process look more professional. The method below does this:

```java
1   private void alertDisplayer(String title,String message){
2           AlertDialog.Builder builder = new AlertDialog.Builder(LoginActivity.this)
3                   .setTitle(title)
4                   .setMessage(message)
5                   .setPositiveButton("OK", new DialogInterface.OnClickListener() {
6                       @Override
7                       public void onClick(DialogInterface dialog, int which) {
8                           dialog.cancel();
9                           // don't forget to change the line below with the names of your Activities
10                          Intent intent = new Intent(LoginActivity.this, LogoutActivity.class);
11                          intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK | Intent.FLAG_ACTIVITY_NEW_TASK);
12                          startActivity(intent);
13                      }
14                   });
15          AlertDialog ok = builder.create();
16          ok.show();
17  }
```

## 5 - Log out

1. Import to your LoginActivity:

:::BlockQuote
1   import android.app.AlertDialo&#x67;**;**
2   import android.app.ProgressDialo&#x67;**;**
3   import android.content.DialogInterfac&#x65;**;**
4   import android.content.Inten&#x74;**;**
5   import android.support.v7.app.AppCompatActivit&#x79;**;**
6   import android.os.Bundl&#x65;**;**
7   import android.view\.Vie&#x77;**;**
8   import android.widget.Butto&#x6E;**;**
9
10  import com.parse.ParseUse&#x72;**;**
:::

&#x20;    2\. To implement Twitter Logout, simply use the code below:

:::BlockQuote
&#x31;**&#x20;  ParseUser.**&#x6C;ogOu&#x74;**();**
2   alertDisplaye&#x72;**(**"So, you're going..."**,** "Ok...Bye-bye then"**);**
:::

:::hint{type="info"}
In the example project, this code is placed inside aLOGOUT VIA TWITTERbutton callback.
:::

:::hint{type="info"}
The method alertDisplayer is the same that you added in the LoginActivity, just remember to change the Intent arguments. in the strings.xml file of your Android Studio Project.
:::

## It’s done!

At this stage, you can log in, register and log out of your app with Twitter using Parse Server core features through Back4App!
