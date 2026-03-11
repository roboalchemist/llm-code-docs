# Source: https://docs-containers.back4app.com/docs/javascript/parse-javascript-sdk.md

---
title: Install Parse SDK
slug: docs/javascript/parse-javascript-sdk
description: In this guide you will learn how to install and connect the Parse SDK to your JavaScript project and get ready to use Parse in 3 easy steps.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-04T14:11:19.651Z
updatedAt: 2025-03-21T19:00:45.760Z
---

# Install Parse SDK to your JavaScript Project

## Introduction

In this section, you learn how to install Parse JavaScript SDK into your HTML project.

:::hint{type="success"}
See more about Parse SDK at [**Parse JavaScript SDK API Reference**](https://parseplatform.org/Parse-SDK-JS/api/4.3.1/) and [**Parse open source documentation for JavaScript SDK**](https://docs.parseplatform.org/js/guide/).
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An app created at Back4App.
  - Follow the [**new Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App at Back4App.
:::

:::hint{type="danger"}
Parse JavaScript SDK supports Firefox 23+, Chrome 17+, Safari 5+, and IE 10.

**IE 9 is supported only for apps that are hosted with HTTPS.**
:::

## 1 - Install SDK

To enable the Parse JavaScript SDK in your web app, create a new index.html file or use your main HTML file and add the following script inside its \<head> tag:

:::CodeblockTabs
index.html

```html
<!-- This is the minified production version of Parse JS -->
<script type="text/javascript" src="https://unpkg.com/parse/dist/parse.min.js"></script>
```
:::

## 2 - Connect your Parse App

### **Initialize your Parse app**

Before using any Parse functionality, you need to call the Parse.Initialize method to set up the authentication token and connect your page with Back4App servers.

In your index.html file, create a \<script> tag at the bottom of it and add the following code:

:::CodeblockTabs
index.html

```html
<script>
  // Initialize Parse
  Parse.initialize("YOUR_PARSE_APP_ID", "YOUR_PARSE_JS_KEY"); //PASTE HERE YOUR Back4App APPLICATION ID AND YOUR JavaScript KEY
  Parse.serverURL = "https://parseapi.back4app.com/";
</script>
```
:::

Note that creating and importing a separate JavaScript file is strongly advised instead of using inline JS code in your HTML file, but for simplicity, we will use the latter here.

### **Find your Application ID and your Client Key**

1. Go to your App Dashboard at the Back4App website.
2. Navigate to app settings: Click on Server Settings > Core Settings block> Settings.
3. Return to your Parse.Initialize function and paste your applicationId and javaScriptKey there.

## 3 - Testing your connection

### **Create a test code**

Test your initial setup with the following code which creates a new object of the User class. Add it inside the \<script> tag, right after the Parse.initialize method:

:::CodeblockTabs
index.html

```html
// Create a new User
async function createParseUser() {
  // Creates a new Parse "User" object, which is created by default in your Parse app
  let user = new Parse.User();
  // Set the input values to the new "User" object
  user.set("username", document.getElementById("username").value);
  user.set("email", document.getElementById("email").value);
  user.set("password", document.getElementById("password").value);
  try {
    // Call the save method, which returns the saved object if successful
    user = await user.save();
    if (user !== null) {
      // Notify the success by getting the attributes from the "User" object, by using the get method (the id attribute needs to be accessed directly, though)
      alert(
        `New object created with success! ObjectId: ${
          user.id
        }, ${user.get("username")}`
      );
    }
  } catch (error) {
    alert(`Error: ${error.message}`);
  }

 // Add on click listener to call the create parse user function
 document.getElementById("createButton").addEventListener("click", async function () {
   createParseUser();
});
```
:::

You also need to create the input fields to pass data to your JavaScript function, so add these plain elements to your \<body> section of your HTML file:

:::CodeblockTabs
index.html

```html
<h1>JS SDK</h1>   
<input id="username" type="text" placeholder="Username"/>
<input id="email" type="email" placeholder="Email"/>
<input id="password" type="password" placeholder="Password" />
<button id="createButton">Create User</button>
```
:::

Go ahead and test this example app following these steps:

1. Open your HTML file in your web browser.
2. Fill the input fields with data and click;
3. An alert box will show the id of the new User object that was created.
4. Login at Back4App.
5. Find your app and click on Dashboard.
6. Click on Core.
7. Go to Browser.
8. Click on User class.
9. Check your new object there.

After these steps you should see something like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wj7qnwGleQ7IQYyQwDV1y_image.png)

Here is the full app code:

:::CodeblockTabs
index.html

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <!-- This is the minified production version of parse js -->
    <script
      type="text/javascript"
      src="https://unpkg.com/parse/dist/parse.min.js"
    ></script>
  </head>
  <body>
    <h1>JS SDK</h1>
    <input id="username" type="text" placeholder="Username" />
    <input id="email" type="email" placeholder="Email" />
    <input id="password" type="password" placeholder="Password" />
    <button id="createButton">Create User</button>
  </body>
  <script>
    // Initialize Parse
    Parse.initialize("YOUR_PARSE_APP_ID", "YOUR_PARSE_JS_KEY"); //PASTE HERE YOUR Back4App APPLICATION ID AND YOUR JavaScript KEY
    Parse.serverURL = "https://parseapi.back4app.com/";

    // Create a new User
    async function createParseUser() {
      // Creates a new Parse "User" object, which is created by default in your Parse app
      let user = new Parse.User();
      // Set the input values to the new "User" object
      user.set("username", document.getElementById("username").value);
      user.set("email", document.getElementById("email").value);
      user.set("password", document.getElementById("password").value);
      try {
        // Call the save method, which returns the saved object if successful
        user = await user.save();
        if (user !== null) {
          // Notify the success by getting the attributes from the "User" object, by using the get method (the id attribute needs to be accessed directly, though)
          alert(
            `New object created with success! ObjectId: ${
              user.id
            }, ${user.get("username")}`
          );
        }
      } catch (error) {
        alert(`Error: ${error.message}`);
      }
    }

    // Add on click listener to call the create parse user function
    document.getElementById("createButton").addEventListener("click", async function () {
      createParseUser();
    });
  </script>
</html>
```
:::

## It’s done!

At this point, you have learned how to get started with JavaScript web apps.

:::hint{type="info"}
Learn more by reading the [**Parse open source documentation for JavaScript SDK**](https://docs.parseplatform.org/js/guide/).
:::

