# Source: https://docs-containers.back4app.com/docs/javascript/javascript-facebook-login.md

---
title: Facebook Login
slug: docs/javascript/javascript-facebook-login
description: In this guide you learn how to add facebook login to your javascript app
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-05T13:48:15.845Z
updatedAt: 2024-03-28T22:16:20.329Z
---

# Add facebook login to your javascript App

## Introduction

This section guides you on how to use the Facebook API for JavaScript in a [**Parse**](http://parseplatform.org/) environment through Back4App.

In this tutorial, you will learn how to link the Facebook SDK to your Parse dashboard and how to implement Facebook login, signup, logout, link and unlink functions.

By following the below-mentioned steps, you will be capable of building a system like this: [**Back4App JavaScript Example Facebook Login App**](http://js-fb-login.back4app.io/).

:::hint{type="info"}
**At any time, you can access the complete Android Project built with this tutorial at our&#x20;**[**GitHub repository**](https://github.com/back4app/javascript-facebook-login)**.**
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- Basic JavaScript App connected with Back4App.
  - **Note:&#x20;**&#x59;ou can use the app created in our [**JavaScript Install Parse SDK tutorial**](https://www.back4app.com/docs/javascript/parse-javascript-sdk) or any app connected to Back4App.
- A domain for your app.
  - **Note:&#x20;**&#x49;t’s necessary to have a domain to start using the Facebook Login API. To know more about web hosting take a look at [**Back4App WebHosting tutorial**](https://help.back4app.com/hc/en-us/articles/360002120991-How-can-I-use-Back4App-webhosting).
- A Parse Server at version 2.6.5 or higher.
  - **Note:&#x20;**&#x54;he Parse Facebook SDK only works on Parse Server version higher than 2.6.5, which this tutorial will be using. So, if you’re using a lower version of Parse, consider upgrading it.
:::

## 1 - Facebook Set up

To start using the Facebook SDK for JavaScript, you need to follow these steps:

1. Go to the [**Facebook Developer Website**](https://developers.facebook.com/), create an account and an App.
2. Set up your Facebook App.
3. Activate the Facebook Login by clicking on Facebook login > Quickstart, which is present on the left menu, then follow the [**Facebook Quickstart Documentation**](https://developers.facebook.com/docs/facebook-login/web) carry out the activation.
4. To link Back4app with your Facebook App, log in to your [**Back4App&#x20;**](https://www.back4app.com/)account, click on Server Settings of your App and click on Settings of the ''Facebook Login'' block. It should look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ixUc4J1oLUcmumlAis20W_image.png)

&#x20;   5\. Then, add your Facebook App ID, which can be found on the [**Dashboard**](https://www.facebook.com/login.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Fapps) of your Facebook App.
&#x20;   6\. Follow [**these instructions**](https://developers.facebook.com/docs/javascript/quickstart/) for loading the Facebook JavaScript SDK into your application.
&#x20;   7\. Replace your call to FB.init() with a call to Parse.FacebookUtils.init(). For example,
&#x20;if you load the Facebook JavaScript SDK asynchronously, your fbAsyncInit function will look like this:

:::CodeblockTabs
init.js

```javascript
1   // Initialize Parse
2   Parse.initialize("Your Parse App Id Here", "Your JavaScript Key Here"); // don't forget to change these keys
3   Parse.serverURL = "https://parseapi.back4app.com/";
4
5   // Load the Facebook API asynchronous when the window starts loading
6   window.fbAsyncInit = function() {
7       Parse.FacebookUtils.init({ // this line replaces FB.init({
8           appId      : '{facebook-app-id}', // Facebook App ID
9           cookie     : true,  // enable cookies to allow Parse to access the session
10          xfbml      : true,  // initialize Facebook social plugins on the page
11          version    : 'v2.3' // point to the latest Facebook Graph API version, found in FB's App dashboard.
12      });
13
14      // Put here code to run after the Facebook SDK is loaded.
15  };
16
17  // Include the Facebook SDK
18  (function(d, s, id){
19      var js, fjs = d.getElementsByTagName(s)[0];
20      if (d.getElementById(id)) {return;}
21      js = d.createElement(s); js.id = id;
22      js.src = "//connect.facebook.net/en_US/sdk.js";
23      fjs.parentNode.insertBefore(js, fjs);
24  }(document, 'script', 'facebook-jssdk'));
```
:::

## 2 - Log in

Start by making a *log in with Facebook* function that saves the user to the Parse
database.

Unfortunately, it’s not possible to use the login button provided by Facebook, as logging in
with it would not save the new user to the Parse Dashboard. However, when you use the [**Parse SDK for Facebook**](http://docs.parseplatform.org/js/guide/#facebook-users), it solves the problem on the server side.

:::hint{type="info"}
For an easy design of the Facebook Login button, using HTML and CSS, look at this implementation: [**Facebook Login Button**](https://codepen.io/davidelrizzo/pen/vEYvyv).
:::

To start the Login Implementation, assign an onClick event that calls the following logIn function to your Facebook Login button. To build this function, follow the steps mentioned below:

1. Use the Parse.FacebookUtils.logIn to perform the Facebook log in together with Parse, this function receives Facebook’s permissions as arguments. In this example, these permissions correspond to the public profile and email.

:::hint{type="info"}
Note: See [**Facebook Login Permission Reference**](https://developers.facebook.com/docs/permissions) for more details.
:::

&#x20;     2\. Check if the user is already in the database. If he is, just redirect him to another page.
&#x20;     3\. Make a call to FB.api to get information about the new user. In this example, it’s possible to access the ID, name, email and permissions of users.

:::hint{type="info"}
**Note**: To know more about this function click [**here**](https://developers.facebook.com/docs/javascript/reference/FB.api).
:::

&#x20;    4\. Set the properties, username and email of the user and save it to the database.
&#x20;    5\. Redirect the page.

The *logIn()&#x20;*&#x63;ode is the following:

:::CodeblockTabs
login.js

```javascript
1   function logIn() {
2       Parse.FacebookUtils.logIn("public_profile,email", {
3           success: function(user) {
4               if (!user.existed()) {
5                   FB.api('/me?fields=id,name,email,permissions', function (response) {
6                       user.set('username', response.name);
7                       user.set('email', response.email);
8
9                       user.save(null, {
10                          success: function(user) {
11                              alert('User logged in and sign up through Facebook, with username: ' + user.get('username') + ' and email: ' + user.get('email'));
12  
13                              // You should redirect the user to another page after a successful login.
14                              window.location.replace('http://js-fb-login.back4app.io/logout.html');
15                          },
16                          error: function(user, error) {
17                              alert('Failed to save user to database with error: ' + error.message);
18                          }
19                      });
20                  });
21              } else {
22                  alert("User logged in through Facebook!");
23                  // You should redirect the user to another page after a successful login.
24                  window.location.replace('http://js-fb-login.back4app.io/logout.html');
25              }
26          },
27          error: function(user, error) {
28              console.log("User cancelled the Facebook login or did not fully authorize.");
29          }
30      });
31  }
```
:::

## 3 - Log out

The log out function is way simpler than the log in one. This time, you will be able to use the button provided by Facebook. However, it will be used just for log out purposes, because it’s necessary to use the Parse’s function to log in. Thus, you should only use this button when the user is already logged in to Facebook and want to log out.

:::hint{type="info"}
To see the official Facebook reference to the Facebook button click [**here**](https://developers.facebook.com/docs/facebook-login/web/login-button).
:::

Here’s how you can implement this button using the Facebook SDK:

:::CodeblockTabs
logout.html

```html
1   <div class="fb-login-button" data-max-rows="1" data-size="large" data-button-type="login_with"
2        data-show-faces="false" data-auto-logout-link="true" data-use-continue-as="false"
3        onlogin="logOutWithFacebook()"></div>
```
:::

:::hint{type="info"}
**Note**: this element has a callback onlogin, which calls our function logOutWithFacebook when the user logs out. Yeah, that’s right: the onlogin event is fired on log out.
:::

The logOutWithFacebook function will simply log out the user from his current Parse session and redirect him to another page, as shown below:

:::CodeblockTabs
logout.js

```javascript
1   function logOutWithFacebook() { // The callback function
2       Parse.User.logOut(); // Delete the current session for the user
3       alert('User logged out of Facebook!');
4       window.location.replace('http://js-fb-login.back4app.io'); // Redirects the user to another webpage
5   }
```
:::

## 4 - Link and Unlink

The last features available for Parse Facebook are link and unlink functions.

While **Linking** is the act of associating an existing Parse.User to his Facebook account and **Unlinking&#x20;**&#x72;efers to removing this association. This association can be seen in your Parse Dashboard, in the authData column, right here:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uZ1mtNyTrWfLZTcBs0mon_image.png)

You can use the data in the column to validate your link and unlink functions.

### **Step 4.1 - Link**

The link function checks if the current user is linked before trying to link him again. It is quite
&#x20;simple and uses the Parse.FacebookUtils SDK, as shown below:

:::CodeblockTabs
link.js

```javascript
1   function link() {
2       var user = Parse.User.current();
3       if (!Parse.FacebookUtils.isLinked(user)) {
4           Parse.FacebookUtils.link(user, null, {
5               success: function(user) {
6                   alert("Woohoo, user logged in with Facebook!");
7               },
8               error: function(user, error) {
9                   alert("User cancelled the Facebook login or did not fully authorize.");
10              }
11          });
12      }
13      else {
14          alert("Can't link user to facebook because he is already linked");
15      }
16  }
```
:::

### **Step 4.2 - Unlink**

For the unlink function, simply call Parse.FacebookUtils.unlink on the current Parse User, as you can see:

:::CodeblockTabs
unlink.js

```javascript
1   function unlink() {
2       var user = Parse.User.current();
3       Parse.FacebookUtils.unlink(user, {
4           success: function(user) {
5               alert("The user is no longer associated with their Facebook account.");
6           }
7       });
8   }
```
:::

:::hint{type="info"}
Go to the authData column in your Parse Dashboard to confirm that it is empty after the function call.
:::

## It’s done!

At this point, you have learned not only how to configure and use the Facebook login and logout functions with your app, but also how to use them with Back4App and Parse.

You now master the use of the Parse Facebook SDK and can start using it at will.

:::hint{type="success"}
See more about Parse SDK at J[**avaScript SDK API Reference**](https://parseplatform.org/Parse-SDK-JS/api/4.3.1/) and [**Parse open source documentation for Javascript SDK**](https://docs.parseplatform.org/js/guide/#facebook-users).
:::

