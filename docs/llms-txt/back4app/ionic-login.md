# Source: https://docs-containers.back4app.com/docs/js-framework/ionic/ionic-login.md

---
title: Email Verification
slug: docs/js-framework/ionic/ionic-login
description: In this guide you learn how to use implement ionic user registration with email verification
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-08T13:45:08.560Z
updatedAt: 2025-01-17T01:07:43.797Z
---

## User registration with email verification

### Introduction

This section explains how you can create an app with user registration and email verification using [**Parse Server core features**](https://www.back4app.com/product/parse-server) through Back4App.

This is how it will look like:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/c7_HTGlsLsEc0AcyZJ-Jk_image.png)

:::hint{type="success"}
At any time, you can access the complete Ionic Project built with this tutorial at our [**GItHub repository**](https://github.com/back4app/ionic-email-verification).
:::

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- [**Visual Studio Code&#x20;**](https://code.visualstudio.com/download)(or any web IDE you like).
- [**Ionic Framework&#x20;**](https://ionicframework.com/getting-started/)
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
- Followed the [**User Registration**](https://www.back4app.com/docs/js-framework/ionic/ionic-framework-login) tutorial to learn how to implement sign up, login and log out with back4app.
:::

## 1 - Set up

In this tutorial, we will be starting from where we left off in the previous [**User Registration**](https://www.back4app.com/docs/ionic/ionic-framework-login-screen) one.

## 2 - Enable Email Verification

1. Go to your App at [**Back4App Website&#x20;**](https://www.back4app.com/)and click on Server Settings.
2. Find the “Verification emails” block and click on Settings. The “Verification emails” block looks like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/3bu-2FLDQV0u_HLu1DlBq_image.png)

&#x20;     3\. Click on Verify User Email. It is right here:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/AAm7YFMWHE0vI1U5gIl6P_image.png)



&#x20;   4\. Fill in the empty fields and modify the ones that have already been filled based on your preferences.

&#x20;   5\. Click on the SAVE button.

## 3 - Sign Up

The two fundamental attributes of ParseUser class are **username** and **password**. There’s a third special attribute that you should also set, i.e. the **email**.
To implement Sign Up with Email Verification, you will use the same method as the basic user registration. But this time, instead of sending the user to the Home page, you will ask him/her to verify his/her email to login.

Once the user creation is completed, it is automatically added to Parse Dashboard and its **emailVerified** Boolean attribute is set as **false**. At this point, the user should not be allowed to log into your platform. Once he/she verifies his/her e-mail, by clicking on the link sent to his/her mailbox, the **emailVerified** boolean will be automatically set to **true**, enabling him/her to access your platform entirely.

To make SignUpActivity work, follow these steps:

Add the isSigningup and email variables to login.ts to toggle and hold the e-mail input:

:::CodeblockTabs
login.ts

```typescript
1   // Parse Dependencies
2     email: string;
3     isSigningup: boolean;
```
:::

Make the signUp() method send the e-mail address to the parse User.signUp() function:

:::CodeblockTabs
login.ts

```typescript
1   signUp() {
2       Parse.User.signUp(this.username, this.password, {email: this.email}).then((resp) => {
3           console.log('Signed up successfully', resp);
4
5           // Clears up the form
6           this.username = '';
7           this.password = '';
8           this.email = '';
9
10          this.toastCtrl.create({
11          message: 'Account created successfully',
12          duration: 2000
13          }).present();
14
15          this.isSigningup = false;
16      }, err => {
17          console.log('Error signing in', err);
18
19          this.toastCtrl.create({
20          message: err.message,
21          duration: 2000
22          }).present();
23      });
24  }
```
:::

Now, let’s reflect those changes to the view login.html by adding \*ngIf to show/hide html elements whenever the user is signing up (**isSigningup** is equal to **true**) or signing in (**isSigningup** is equal to **false**).

:::CodeblockTabs
login.html

```html
1     <ion-item *ngIf="isSigningup">
2       <ion-label stacked>E-mail</ion-label>
3       <ion-input type="email" [(ngModel)]="email"></ion-input>
4     </ion-item>
5
6     <div text-center margin-top *ngIf="!isSigningup">
7       <button ion-button margin-right (click)="isSigningup = true">
8         SIGN UP
9       </button>
10
11      <button ion-button color="secondary" (click)="signIn()">
12        SIGN IN
13      </button>
14    </div>
15
16    <div text-center margin-top *ngIf="isSigningup">
17      <button ion-button (click)="signUp()">
18        SIGN UP
19      </button>
20    </div>
```
:::

## 4 - Log in

Now, let’s add the **emailVerified** boolean verification before sending the user to the Home page.

:::hint{type="info"}
**Note**: Although the user logs in when the function Parse.User.logIn() is called, he/she can’t access the app until the e-mail verification is done.
Also, because of a Session object is created in the database when calling logIn(), it’s important to call Parse.User.logout() every time a user who hasn’t verified his/her e-mail tries to access the application in order to not leave Sessions opened.
:::

Now, let’s implement the **emailVerified&#x20;**&#x76;erification to decide whether the user logs in or get an alert saying e-mail must be verified:

:::CodeblockTabs
login.ts

```typescript
1   // Parse Dependencies
2   signIn() {
3       Parse.User.logIn(this.username, this.password).then((user) => {
4           console.log('Logged in successfully', user);
5
6           if(user.get('emailVerified')) {
7               // If you app has Tabs, set root to TabsPage
8               this.navCtrl.setRoot('HomePage')
9           } else {
10              Parse.User.logOut().then((resp) => {
11                  console.log('Logged out successfully', resp);
12              }, err => {
13                  console.log('Error logging out', err);
14              });
15
16              this.alertCtrl.create({
17                  title: 'E-mail verification needed',
18                  message: 'Your e-mail address must be verified before logging in.',
19                  buttons: ['Ok']
20              }).present();
21          }
22      }, err => {
23          console.log('Error logging in', err);
24
25          this.toastCtrl.create({
26          message: err.message,
27          duration: 2000
28          }).present();
29      });
30  }
```
:::

## 5 - Test your app

1. Test your app by running ionic serve and creating a couple of users, also try logging in after registering without verifying the email to see if the error is actually displayed.
2. Login at [**Back4App Website.**](https://www.back4app.com/)&#x20;
3. Find your app and click on Dashboard > Core > Browser > User to see the users that you’ve created!

## It’s done!

At this stage, you can login, register or logout of your app using email verification with Parse Server core features through Back4App!
