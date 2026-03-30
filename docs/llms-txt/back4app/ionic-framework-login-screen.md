# Source: https://docs-containers.back4app.com/docs/js-framework/ionic/ionic-framework-login-screen.md

---
title: User Registration
slug: docs/js-framework/ionic/ionic-framework-login-screen
description: Learn how to build a login screen on your Ionic framework project using Back4App
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-08T13:12:47.635Z
updatedAt: 2025-01-17T01:07:40.077Z
---

# How to add a login screen to your Ionic framework project

## Introduction

In this section you learn how to create a page, implement sign up, sign in and sign out to your Ionic app.

This is how it will look like:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/PC-d303k9wdHVghTjEwg0_image.png)

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Visual Studio Code&#x20;**](https://code.visualstudio.com/download)(or any web IDE you like).
- [**Ionic Framework&#x20;**](https://ionicframework.com/getting-started/)
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
:::

:::hint{type="success"}
At any time, you can access the complete Ionic Project built with this tutorial at our [**GItHub repository**](https://github.com/back4app/ionic-email-verification).
:::

## 1 - Install parse SDK

Considering you have an existing Ionic project, the first thing you need to do is to install parse SDK. You can do it by running:

:::BlockQuote
$ npm install parse
:::

## 2 - Set up app’s credentials

1. Open your app.component.ts, import parse and initialize its connection to Back4App Parse server.

:::CodeblockTabs
app.component.html

```html
1   Parse.initialize("YOUR-APP-ID", "YOUR-JS-KEY");
2   Parse.serverURL = 'https://parseapi.back4app.com/';
```
:::

:::hint{type="info"}
If you don’t know how to find your keys, check out the first Ionic tutorial [**Start From Template**](https://www.back4app.com/docs/js-framework/ionic/ionic-template#setup).
:::

## 3 - Create the LogIn Page

Now, let’s create our LogIn page. Luckly, Ionic does everything to us. All we need to do is to run the following command:

:::BlockQuote
$ ionic generate page Login
:::

In this page view, we need to add inputs for username and password and two buttons, one for signing up and another one for signing in.

:::CodeblockTabs
login.html

```html
1     <h4 text-center margin-top>Insert your credentials</h4>
2
3     <ion-item>
4       <ion-label stacked>Username</ion-label>
5       <ion-input [(ngModel)]="username"></ion-input>
6     </ion-item>
7
8     <ion-item>
9       <ion-label stacked>Password</ion-label>
10      <ion-input type="password" [(ngModel)]="password"></ion-input>
11    </ion-item>
12
13    <div text-center margin-top>
14      <button ion-button margin-right (click)="signUp()">
15        SIGN UP
16      </button>
17
18      <button ion-button color="secondary" (click)="signIn()">
19        SIGN IN
20      </button>
21    </div>
```
:::

Let’s implement now the methods signIn() and signUp() referred in our Login view.

:::CodeblockTabs
login.ts

```typescript
1     signUp() {
2       Parse.User.signUp(this.username, this.password).then((resp) => {
3         console.log('Logged in successfully', resp);
4
5         // Clears up the form
6         this.username = '';
7         this.password = '';
8
9         this.toastCtrl.create({
10          message: 'Account created successfully',
11          duration: 2000
12        }).present();
13      }, err => {
14        console.log('Error signing in', err);
15
16        this.toastCtrl.create({
17          message: err.message,
18          duration: 2000
19        }).present();
20      });
21    }
```
:::

:::hint{type="info"}
Learn more about signUp() at [**Parse Documentation**](https://parseplatform.org/Parse-SDK-JS/api/v1.11.1/Parse.User.html#.signUp).
:::

:::CodeblockTabs
login.ts

```typescript
1     signIn() {
2       Parse.User.logIn(this.username, this.password).then((resp) => {
3         console.log('Logged in successfully', resp);
4
5         // If you app has Tabs, set root to TabsPage
6         this.navCtrl.setRoot('HomePage')
7       }, err => {
8         console.log('Error logging in', err);
9
10        this.toastCtrl.create({
11          message: err.message,
12          duration: 2000
13        }).present();
14      });
15    }
```
:::

:::hint{type="info"}
Learn more about Parse.User.logIn() at [**Parse Documentation**](https://parseplatform.org/Parse-SDK-JS/api/v1.11.1/Parse.User.html#.signUp).
:::

This is how it should look like.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/efmW3s-Z-wu4kLeQlhUL__image.png" signedSrc size="50" width="413" height="731" position="center" caption}

## 4 - Implement Log out

Let’s move to our HomePage (or the page the user will be directed after logging in) and implement the sign out.

First, go ahead, open home.html and add a button for doing so.

:::CodeblockTabs
login.html

```html
1     <h2 text-center>You are logged in!</h2>
2
3     <div margin-top text-center>
4       <button ion-button (click)="logOut()">
5         Log out
6       </button>
7     </div>
```
:::

Now, let’s implement the logOut() method and also add a Toast component if the request fails.

:::CodeblockTabs
home.ts

```typescript
1     logOut() {
2       Parse.User.logOut().then((resp) => {
3         console.log('Logged out successfully', resp);
4
5         this.navCtrl.setRoot('LoginPage');
6       }, err => {
7         console.log('Error logging out', err);
8
9         this.toastCtrl.create({
10          message: 'Error logging out',
11          duration: 2000
12        }).present();
13      })
14    }
```
:::

:::hint{type="info"}
Learn more about Parse.User.logOut() at [**Parse Documentation**](https://parseplatform.org/Parse-SDK-JS/api/v1.11.1/Parse.User.html#.signUp).
:::

It should look like this.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/HB337gxfN6oOM-D7B-dCl_image.png" signedSrc size="50" width="417" height="737" position="center" caption}

## 5 - Set root page

An important feature of parse is that it remembers if a user is logged or not in a device. It means that even if the user closes the app, you can still restore his session when the app is open.

With that, we can determine if the app initial page will be our LoginPage or HomePage.

To do so, we just need to call currentAsync(). It will return the user logged in or null.

:::CodeblockTabs
app.component.ts

```typescript
1     Parse.User.currentAsync().then(user => {
2       console.log('Logged user', user);
3
4       this.rootPage = user ? 'HomePage' : 'LoginPage';
5     }, err => {
6       console.log('Error getting logged user');
7
8       this.rootPage = 'LoginPage';
9     })
```
:::

:::hint{type="info"}
Learn more about Parse.User.currentAsync() at [**Parse Documentation**](https://parseplatform.org/Parse-SDK-JS/api/v1.11.1/Parse.User.html#.signUp).
:::

## Finally, it’s all set up!

At this point, just run ionic serve and you will have a sign in, sign up and sign out features working that also remembers the logged user until he/she logs out.
