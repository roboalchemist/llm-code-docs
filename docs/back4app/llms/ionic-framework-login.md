# Source: https://docs-containers.back4app.com/docs/js-framework/ionic/ionic-framework-login.md

---
title: Facebook Login
slug: docs/js-framework/ionic/ionic-framework-login
description: In this guide you learn how to add facebook login to your Ionic Android app.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-08T13:59:15.188Z
updatedAt: 2025-01-17T01:07:47.689Z
---

# How to add facebook login to your Ionic App

## Introduction

This section explains how you can create an app with user registration using Facebook Login and [**Parse Server core features**](https://www.back4app.com/product/parse-server) through Back4App.

After following this tutorial, you will be able to do this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/PrNRMaA0rfyc0wtY3KPiY_image.png" signedSrc size="50" width="360" height="640" position="center" caption}

:::hint{type="success"}
At any time, you can access the complete Ionic Project built with this tutorial at our [**GItHub repository**](https://github.com/back4app/ionic-email-verification).
:::

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Visual Studio Code&#x20;**](https://code.visualstudio.com/download)(or any web IDE you like).
- [**Ionic Framework&#x20;**](https://ionicframework.com/getting-started/)
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
- A [**Facebook**](https://www.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2F) account for creating the app.
:::

## 1 - Facebook Set up

To start using Facebook functions, you need to:

1. Go to the [**Facebook Developer**](https://developers.facebook.com/) Website and create an account and log in.
2. Go to [**My Apps**](https://www.facebook.com/login.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Fapps%2F) and click on Add a New App:
3. At the left panel, click on Settings > Basic. In this page:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xsVB-JyllSoKNbm2bJLrm_image.png)

- Take note of your App ID
- Add a Privacy Police URL
- Select a Category
- Scroll down and hit Save changes

4\. At the top of the same page, click on the Off button and **Confirm** to make your app live.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SSBOjQ0Rl5I0638Yp0xUJ_image.png" signedSrc size="50" width="391" height="160" position="center" caption}



&#x20;   5\. Scroll down at the same page and click on Add platform.

- For this tutorial, let’s choose **Android**.
- Add your Google Play Package Name which in our case is com.back4app.myapp
- Add the Key Hashes of your machine (run keytool -exportcert -alias androiddebugkey -keystore \~/.android/debug.keystore | openssl sha1 -binary | openssl base64 to find out yours)
- Save changes

&#x20;   6\. At the left panel, to back to Dashboard, scroll down and click on Facebook Login.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/6YRZiQ5uSVljKxiN8oF5y_image.png" signedSrc size="80" width="548" height="299" position="center" caption}

## 2 - Link your Facebook App with Back4App

1. Go to your App dashboard at [**Back4App Website**](https://www.back4app.com/) and click on Server Settings.
2. Find the “Facebook Login” block and click on Settings. The “Facebook Login” block looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/WIYx7akL5P5bxjmbBPmIo_image.png)

&#x20;    3\. Add the Facebook App ID taken note in the previous step.

## 3 - Set up

In this tutorial, we will be starting from where we left off in the previous [**User registration with email verification**](https://www.back4app.com/docs/ionic/user-registration-email-verification) one.

## 4 - Facebook Login

Let’s first install Facebook cordova plugins:

:::BlockQuote
$ ionic cordova plugin add cordova-plugin-facebook4 --variable APP\_ID="XXXXXXXX" --variable APP\_NAME="XXXXXXXX"
$ npm install --save @ionic-native/facebook
:::

Now, let’s implement the facebookLogin() method:

:::CodeblockTabs
login.ts

```typescript
1     async facebookLogin() {
2       try {
3         // Log in to Facebook and request user data
4         let facebookResponse = await this.facebook.login(['public_profile', 'email']);
5         let facebookAuthData = {
6           id: facebookResponse.authResponse.userID,
7           access_token: facebookResponse.authResponse.accessToken,
8         };
9
10        // Request the user from parse
11        let toLinkUser = new Parse.User();
12        let user = await toLinkUser._linkWith('facebook', {authData: facebookAuthData});
13
14        // If user did not exist, updates its data
15        if (!user.existed()) {
16          let userData = await this.facebook.api('me?fields=id,name,email,first_name,picture.width(720).height(720).as(picture)', []);
17          user.set('username', userData.name);
18          user.set('name', userData.name);
19          user.set('email', userData.email);
20          await user.save();
21        }
22
23        this.navCtrl.setRoot('HomePage');
24      } catch (err) {
25        console.log('Error logging in', err);
26
27        this.toastCtrl.create({
28          message: err.message,
29          duration: 2000
30        }).present();
31      }
32    }
```
:::

Finally, let’s add a button to our Login page and make it call the method we just created:

:::CodeblockTabs
login.html

```html
1   <div text-center>
2         <button ion-button color="facebook" (click)="facebookLogin()">
3           LOG IN WITH FACEBOOK
4         </button>
5       </div>
```
:::

## 5 - Test your app

1. Since Facebook log in does’t work on a browser, test your app by running ionic cordova run android.
2. Login at [**Back4App Website**](https://www.back4app.com/).
3. Find your app and click on Dashboard > Core > Browser > User to see the user that you’ve created!

## It’s done!

At this stage, you can log in, register and log out of your app with Facebook using Parse Server core features through Back4App!
