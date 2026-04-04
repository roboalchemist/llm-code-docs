# Source: https://docs-containers.back4app.com/docs/android/working-with-users/android-app-facebook-login-tutorial.md

---
title: Sign in with Facebook
slug: docs/android/working-with-users/android-app-facebook-login-tutorial
description: In this guide you learn how to add facebook login to your app.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-14T11:13:10.770Z
updatedAt: 2025-01-16T20:45:05.503Z
---

# How to add Facebook login to your Android App

## Introduction

In this guide, you will learn how to login using Facebook Login and Parse User class through Back4App. This tutorial uses a basic app created in Android Studio 4.1.1 with buildToolsVersion=30.0.3 , Compile SDK Version = 30 and targetSdkVersion 30

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our Github repositories

- [**Kotlin Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Kotlin)
- [**Java Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Java)
:::

## Goal

Create a Login with Facebook feature to your Android App using Parse and Back4App.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/TGg2Jd2Zr3RMJsaHj8Eqk_facebook-login-v2.gif" signedSrc size="50" width="405" height="880" position="center" caption}

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

## 1 - Facebook Set up

To start using Facebook functions, you need to:

1. Go to the [**Facebook Developer Website&#x20;**](https://developers.facebook.com/)and create an account and an app.
2. Follow Facebook’s Quickstart Guide by [**clicking here&#x20;**](https://developers.facebook.com/docs/facebook-login/android)and pay attention to the following recommendations:

::::hint{type="info"}
**Here are the steps included in Facebook’s Quickstart Guide, which you need to follow carefully, as you are not going to follow them precisely as Facebook suggests:**

- In Step 3 instead of adding

:::BlockQuote
implementation 'com.facebook.android\:facebook-login:\[8.1)'
:::

in the dependencies\{} section at build.gradle (Module\:app), add the following code in the dependencies\{} section at build.gradle (Module\:app)

:::BlockQuote
*1    // update the versions to the latest ones*
2    implementation "com.github.parse-community\:ParseFacebookUtils-Android\:latest.version.here"
3    implementation 'com.facebook.android\:facebook-android-sdk\:latest.version.here'
:::

- Remember to update the version of Parse Facebook Utils SDK for Android to the latest one. You can find out which is the latest version at the [**JitPack website**](https://jitpack.io/), following these steps:

1. At JitPack website paste parse-community\:ParseFacebookUtils-Android in the Git repo URL box.
2. After doing that, click on the Look up button. Then you should see the available versions of Parse SDK for Android, as shown in the following image.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/jpJmidWu5uQY7-GKoeSS6_image.png)

- In Step 4, you’ll be asked to add internet permission at the application element in /app/manifest/AndroidManifest.xml file, but you have already added it while following [**Install Parse SDK**](https://www.back4app.com/docs/android/parse-android-sdk) Tutorial so you don’t need to do this.
- In Step 6, you’ll need to provide key hashes, so you must have [**Open SSL**](https://www.openssl.org/) installed. Facebook’s Guide doesn’t provide command lines to generate key hashes in Linux, but doing that is simple, as all it requires from you is to open a terminal window and run the following command:

:::BlockQuote
keytool -exportcert -alias androiddebugkey -keystore \~/.android/debug.keystore | openssl sha1 -binary | openssl base64
:::

- Don’t follow the steps of Facebook’s Quickstart Guide right after **Step 6**.
::::

:::hint{type="info"}
&#x20; [**Whats is SHA-1**](https://en.wikipedia.org/wiki/SHA-1) (Secure Hashing Algorithm)  &#x20;

SHA-1, called the Secure Hashing Algorithm, is the most common encryption algorithm. SHA-1, designed by United States National Security Agency. SHA-1 fingerprint is a unique key generated for your PC that can be used for signing. Its mainly used for submitting for using the some APIs (Like the Facebook api we will use in this guide.). If you want to learn more details, you can visit the SHA-1 Wikipedia page.
:::

:::hint{type="danger"}
You should follow the other steps described on Facebook’s Quickstart Guide and not mentioned here.
:::

## 2 - Link your Facebook App with Back4App

1. Go to your App dashboard at [**Back4App Website&#x20;**](https://www.back4app.com/)and click on Server Settings.
2. Find the “Facebook Login” block and click on Settings. The “Facebook Login” block looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wzY4k1lITNJdcCZ-hY9ou_image.png)

&#x20;    3\. We need to add our facebook\_id, which we got from Facebook Guide to string.xml(You should have followed the Facebook Guide and did this before). Go to your Android Studio Project, open your strings file: .../app/src/main/res/values/strings.xml, copy your facebook\_app\_id and paste it in the Facebook appId field of the last page of Back4App that you opened. Lastly, press the + button.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Enivtee1WosjYCAgG3T5L_image.png)

## 3 - Add provider element in the Manifest file

Go back to your Android Studio Project and inside the application element in /app/manifest/AndroidManifest.xml file, right after the meta data element, add the following code.

```java
1  <provider
2      android:name="com.facebook.FacebookContentProvider"
3      <!--don't forget to put your Facebook App ID in the following link-->
4      android:authorities="com.facebook.app.FacebookContentProviderYOUR_FACEBOOK_APP_ID"
5      android:exported="true" />
```

:::hint{type="danger"}
**Don’t forget to put your Facebook App ID in the code above.**
:::

## 4 - Initialize Parse Facebook Util SDKs

In your Android Studio Project, in the Java file called App that extends Application that you created to initialize the Parse SDK, on its onCreate method, right after Parse.initialize() call, use the following code to initialize Parse Facebook Utils SDK.

:::BlockQuote
**1   ParseFacebookUtils.**&#x69;nitializ&#x65;**(this);**
:::

:::hint{type="danger"}
If you don’t have an App.java file as described in this step, access the [**Install Parse SDK for Android**](https://www.back4app.com/docs/android/parse-android-sdk) documentation and make sure that you have followed all the steps required to install Parse SDK correctly. If you do not install Parse SDK properly your facebook login with Parse will not work.
:::

## 5 - Set up

At the beginning of each Parse activity, import the following:

:::BlockQuote
1   import androidx.appcompat.app.AppCompatActivit&#x79;**;**
2   import android.app.AlertDialo&#x67;**;**
3   import android.app.ProgressDialo&#x67;**;**
4   import android.content.Inten&#x74;**;**
5   import android.os.Bundl&#x65;**;**
6   import android.widget.Butto&#x6E;**;**
7   import com.facebook.login.LoginManage&#x72;**;**
8   import com.parse.ParseUse&#x72;**;**
:::

## 6 - Log In

To implement your Login Activity, do the following:

1. Import into your LoginActivity, in addition to the dependencies imported in **Step 4**:

:::BlockQuote
1    import android.app.AlertDialo&#x67;**;**
2    import android.app.ProgressDialo&#x67;**;**
3    import android.content.Inten&#x74;**;**
4    import android.os.Bundl&#x65;**;**
5    import android.util.Lo&#x67;**;**
6    import android.widget.Butto&#x6E;**;**
7    import android.widget.Toas&#x74;**;**
8    import com.facebook.AccessToke&#x6E;**;**
9    import com.facebook.GraphReques&#x74;**;**
10   import com.parse.ParseUse&#x72;**;**
11   import com.parse.facebook.ParseFacebookUtil&#x73;**;**
12   import org.json.JSONExceptio&#x6E;**;**
13   import java.util.Array&#x73;**;**
14   import java.util.Collectio&#x6E;**;**
:::

&#x20;    2\. To implement Facebook Login, simply use the following code:

:::CodeblockTabs
```java
1    final ProgressDialog dialog = new ProgressDialog(this);
2    dialog.setTitle("Please, wait a moment.");
3    dialog.setMessage("Logging in...");
4    dialog.show();
5    Collection<String> permissions = Arrays.asList("public_profile", "email");
6    ParseFacebookUtils.logInWithReadPermissionsInBackground(this, permissions, (user, err) -> {
7        dialog.dismiss();
8        if (err != null) {
9            Log.e("FacebookLoginExample", "done: ", err);
10           Toast.makeText(this, err.getMessage(), Toast.LENGTH_LONG).show();
11       } else if (user == null) {
12           Toast.makeText(this, "The user cancelled the Facebook login.", Toast.LENGTH_LONG).show();
13           Log.d("FacebookLoginExample", "Uh oh. The user cancelled the Facebook login.");
14       } else if (user.isNew()) {
15           Toast.makeText(this, "User signed up and logged in through Facebook.", Toast.LENGTH_LONG).show();
16           Log.d("FacebookLoginExample", "User signed up and logged in through Facebook!");
17           getUserDetailFromFB();
18       } else {
19           Toast.makeText(this, "User logged in through Facebook.", Toast.LENGTH_LONG).show();
20           Log.d("FacebookLoginExample", "User logged in through Facebook!");
21           showAlert("Oh, you!", "Welcome back!");
22       }
23   });
```

```kotlin
1        val dlg = ProgressDialog(this)
2        dlg.setTitle("Please, wait a moment.")
3        dlg.setMessage("Logging in...")
4        dlg.show()
5        val permissions: Collection<String> = listOf("public_profile", "email")
6        ParseFacebookUtils.logInWithReadPermissionsInBackground(this, permissions) { user: ParseUser?, err: ParseException? ->
7             dlg.dismiss()
8             when {
9                err != null -> {
10                   Log.e("FacebookLoginExample", "done: ", err)
11                   Toast.makeText(this, err.message, Toast.LENGTH_LONG).show()
12               }
13               user == null -> {
14                   Toast.makeText(this, "The user cancelled the Facebook login.", Toast.LENGTH_LONG).show()
15                   Log.d("FacebookLoginExample", "Uh oh. The user cancelled the Facebook login.")
16               }
17               user.isNew -> {
18                   Toast.makeText(this, "User signed up and logged in through Facebook.", Toast.LENGTH_LONG).show()
19                   Log.d("FacebookLoginExample", "User signed up and logged in through Facebook!")
20                   getUserDetailFromFB()
21               }
22               else -> {
23                   Toast.makeText(this, "User logged in through Facebook.", Toast.LENGTH_LONG).show()
24                   Log.d("FacebookLoginExample", "User logged in through Facebook!")
25                   showAlert("Oh, you!", "Welcome back!")
26               }
27            }
28       }
```
:::

:::hint{type="info"}
In the example project, this code is placed inside a LOGIN VIA FACEBOOK button callback.
:::

&#x20;    3\. After a successful login through Facebook to our App, we can now get some basic logged user information.. As you can see, there are many more methods included in the code above. The getUserDetailFromFB method is responsible for fetching user details. Here’s the code for this method:

:::CodeblockTabs
```java
1    private void getUserDetailFromFB() {
2        GraphRequest request = GraphRequest.newMeRequest(AccessToken.getCurrentAccessToken(), (object, response) -> {
3            ParseUser user = ParseUser.getCurrentUser();
4            try {
5                if (object.has("name"))
6                    user.setUsername(object.getString("name"));
7                if (object.has("email"))
8                    user.setEmail(object.getString("email"));
9            } catch (JSONException e) {
10               e.printStackTrace();
11           }
12           user.saveInBackground(e -> {
13             if (e == null) {
14                 showAlert("First Time Login!", "Welcome!");
15             } else
16                 showAlert("Error", e.getMessage());
17         });
18     });
19
20     Bundle parameters = new Bundle();
21     parameters.putString("fields", "name,email");
22     request.setParameters(parameters);
23     request.executeAsync();
24  }
```

```kotlin
1    private fun getUserDetailFromFB() {
2        val request =
3            GraphRequest.newMeRequest(AccessToken.getCurrentAccessToken()) { `object`: JSONObject, _: GraphResponse? ->
4                val user = ParseUser.getCurrentUser()
5                try {
6                    user.username = `object`.getString("name")
7                } catch (e: JSONException) {
8                    e.printStackTrace()
9                }
10               try {
11                   user.email = `object`.getString("email")
12               } catch (e: JSONException) {
13                   e.printStackTrace()
14               }
15               user.saveInBackground {
16                   if (it == null)
17                       showAlert("First Time Login!", "Welcome!")
18                   else
19                       showAlert("Error", it.message)
20               }
21           }
22       val parameters = Bundle()
23       parameters.putString("fields", "name,email")
24       request.parameters = parameters
25       request.executeAsync()
26   }
```
:::

&#x20;    4\. It’s interesting to add a method to display Alert Dialogs and make the process look more professional. In this function, we also get a user parameter. When going to the MainAtivity page, we send this user parameter in the intent, and in the MainActivity, we pull the information in this user and print it on the screen. The method below does this:

:::CodeblockTabs
```java
1    private void showAlert(String title, String message) {
2        AlertDialog.Builder builder = new AlertDialog.Builder(this)
3                .setTitle(title)
4                .setMessage(message)
5                .setPositiveButton("OK", (dialog, which) -> {
6                    dialog.cancel();
7                    Intent intent = new Intent(this, MainActivity.class);
8                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK | Intent.FLAG_ACTIVITY_NEW_TASK);
9                    startActivity(intent);
10               });
11       AlertDialog ok = builder.create();
12       ok.show();
13   }
```

```kotlin
1    private fun showAlert(title: String, message: String?) {
2        val builder = AlertDialog.Builder(this)
3            .setTitle(title)
4            .setMessage(message)
5            .setPositiveButton("OK") { dialog: DialogInterface, which: Int ->
6                dialog.cancel()
7                val intent = Intent(this@LoginActivity, MainActivity::class.java)
8                intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK or Intent.FLAG_ACTIVITY_NEW_TASK)
9                startActivity(intent)
10           }
11       val ok = builder.create()
12       ok.show()
13   }
```
:::

&#x20;    5\. If you want to associate an existing ParseUser to a Facebook account, you can link it like so:

:::CodeblockTabs
```java
1    Collection<String> permissions = Arrays.asList("public_profile", "email");
2    if (!ParseFacebookUtils.isLinked(ParseUser.getCurrentUser())) {
3        ParseFacebookUtils.linkWithReadPermissionsInBackground(ParseUser.getCurrentUser(), this, permissions, ex -> {
4            if (ParseFacebookUtils.isLinked(ParseUser.getCurrentUser())) {
5                Toast.makeText(this, "Woohoo, user logged in with Facebook.", Toast.LENGTH_LONG).show();
6                Log.d("FacebookLoginExample", "Woohoo, user logged in with Facebook!");
7            }
8        });
9    } else {
10       Toast.makeText(this, "You have already linked your account with Facebook.", Toast.LENGTH_LONG).show();
11   }
```

```kotlin
1    val permissions= listOf("public_profile","email")
2        if (!ParseFacebookUtils.isLinked(ParseUser.getCurrentUser())){
3            ParseFacebookUtils.linkWithReadPermissionsInBackground(ParseUser.getCurrentUser(),this,permissions) {
4                if (ParseFacebookUtils.isLinked(ParseUser.getCurrentUser())){
5                    Toast.makeText(this, "Woohoo, user logged in with Facebook.", Toast.LENGTH_LONG).show()
6                    Log.d("FacebookLoginExample", "Woohoo, user logged in with Facebook!")
7                }
8            }
9        } else {
10           Toast.makeText(this, "You have already linked your account with Facebook.", Toast.LENGTH_LONG).show()
11       }
12   }
```
:::

:::hint{type="info"}
In the example project, this code is placed inside a LINK YOUR ACCOUNT TO FACEBOOK button callback.
:::

&#x20;    6\. If you want to unlink Facebook from a user, simply do this:

:::CodeblockTabs
```java
1    ParseFacebookUtils.unlinkInBackground(ParseUser.getCurrentUser(), ex -> {
2        if (ex == null) {
3            Toast.makeText(this, "The user is no longer associated with their Facebook account.", Toast.LENGTH_LONG).show();
4            Log.d("MyApp", "The user is no longer associated with their Facebook account.");
5        } else {
6            Toast.makeText(this, ex.getMessage(), Toast.LENGTH_LONG).show();
7        }
8    });
```

```kotlin
1    ParseFacebookUtils.unlinkInBackground(ParseUser.getCurrentUser()) {
2        if (it == null) {
3            Toast.makeText(this,"The user is no longer associated with their Facebook account.",Toast.LENGTH_LONG).show()
4            Log.d("MyApp", "The user is no longer associated with their Facebook account.")
5        } else {
6            Toast.makeText(this, it.message, Toast.LENGTH_LONG).show()
7        }
8    }
```
:::

:::hint{type="info"}
In the example project, this code is placed inside a UNLINK YOUR ACCOUNT FROM FACEBOOK button callback.
:::

&#x20;    7\. It’s **very important** to use the following as a method outside the onCreate() method of your LoginActivity to pass login results to the LoginManager via callbackManager and avoid errors.

:::CodeblockTabs
```java
1   @Override
2   protected void onActivityResult(int requestCode, int resultCode, Intent data) {
3       super.onActivityResult(requestCode, resultCode, data);
4       ParseFacebookUtils.onActivityResult(requestCode, resultCode, data);
5   }
```

```kotlin
1    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
2        super.onActivityResult(requestCode, resultCode, data)
3        ParseFacebookUtils.onActivityResult(requestCode, resultCode, data)
4    }
```
:::

## 7 - Log out

To implement Facebook Logout, simply use the code mentioned below:

:::CodeblockTabs
```java
1     final ProgressDialog dialog = new ProgressDialog(this);
2     dialog.setTitle("Please, wait a moment.");
3     dialog.setMessage("Logging out...");
4     dialog.show();
5     LoginManager.getInstance().logOut();
6     ParseUser.logOutInBackground(e -> {
7         if (e == null)
8             showAlert("So, you're going...", "Ok...Bye-bye then", true);
9         else
10            showAlert("Error...", e.getMessage(), false);
11    });
```

```kotlin
1    val dlg = ProgressDialog(this)
2     dlg.setTitle("Please, wait a moment.")
3     dlg.setMessage("Logging out...")
4     dlg.show()
5     LoginManager.getInstance().logOut()
6     ParseUser.logOutInBackground { e->
7         if (e == null)
8             showAlert("So, you're going...", "Ok...Bye-bye then", true)
9         else
10            showAlert("Error...", e.message, false)
11    }
```
:::

:::hint{type="info"}
In the example project, this code is placed inside a LOG OUT button callback.
:::

:::hint{type="info"}
The method alertDisplayer is the same that you added in theLoginActivity, don’t forget to change its Intent arguments though.
:::

## It’s done!

At this stage, you can log in, register and log out of your app with Facebook using Parse Server core features through Back4App!


