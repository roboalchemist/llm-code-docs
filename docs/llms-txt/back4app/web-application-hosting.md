# Source: https://docs-containers.back4app.com/docs/advanced-guides/web-application-hosting.md

---
title: Web Application hosting
slug: docs/advanced-guides/web-application-hosting
description: In this guide we create a frontend and a backend for an application that we launch with Back4App
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-26T13:45:06.946Z
updatedAt: 2025-01-17T14:26:35.398Z
---

# Creating and hosting a full-stack web application

## Introduction

Launching a full-stack application can be daunting. You have to worry about hosting your front end, configuring/provisioning a server, and tying everything together. You may not have known it, but Back4App provides an optimal infrastructure for all of the above.

You can easily serve your frontend HTML (including frontend frameworks like React and Vue) with Back4App’s Web Hosting. Cloud Code makes an excellent backend that launches quickly. In this guide, we’ll build a complete, albeit rudimentary, web application on Back4App.

This is a guest tutorial written by [**John Considine**](https://github.com/considine), lead developer at [**K-Optional**](https://koptional.com/).

## Goals

Launch a full-stack web application on Back4App

## Prerequisites

:::hint{type="info"}
To complete this tutorial, you need:



- To be familiar with the command-line
- [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [**NPM**](https://docs.npmjs.com/getting-started) should be installed
- Have a Back4App Account, with the CLI tool installed and configured, see [**here for help**](https://blog.back4app.com/cli-parse-server/)
- Create a brand new project on your Back4App dashboard- see [**here for help**](https://www.back4app.com/docs/get-started/new-parse-app).
- This tutorial must be set to the Parse Server Version 3.1.x. See directly below for more details
:::

:::hint{type="danger"}
This project will use the newly released version 3.1 Parse Server. This means you need to make sure your Back4App project is set to this release- it won’t work otherwise. On your project dashboard, go to Server Settings » Manage Parse Server(settings) and select 3.1.1 (it may be in Beta).
For more information on migrating to Parse Server 3.1.x, see [**this guide**](https://www.back4app.com/docs/advanced-guides/parse-server-3).
See this guide if you do not understand the syntax of the cloud code for this project.
:::

## Project Background

We will launch a rudimentary ticket exchange application. It allows users to sign up, login, and post tickets they are selling to different events- which admins can create using the Dashboard. Other users can contact them by their email or phone number, depending on what the poster chooses to display.

I have launched the app [**here**](http://ticketlister.koptional.com/), using the same code we explore in this guide. You are free to create an account, post tickets, and see what the app looks like.

The point of this tutorial is to demonstrate how to efficiently launch an app. Thus rather than dwelling on each line of code, we will start with a mostly finished codebase and focus on the ease of deployment. There is only one place where you’ll need to edit code:

- In step 1 you’ll need to add your project settings (Application ID, JavaScript Key, and server URL).

However, you’re welcome to edit and extend this application in any way you like.

## Project Structure

Before you start preparing code, it’s important to understand the file structure of this project. I’ll use this as a reference throughout this guide. Here’s what your directory will look like when everything is finished:

:::BlockQuote
1   project
2   │   .parse.local
3   │   .parse.project
4   │   .gitignore
5   │   README.md
6   └───public
7   │   │   index.html
8   │   │   login.html
9   │   │   signup.html
10  │   └───css
11  │       │   signin.css
12  │       │   bootstrap.min.css
13  │   └───js
14  │       │   main.js
15  │       │   parse.js
16  │       │   signin.js
17  │       │   signup.js
18  │
19  └───cloud
20      │   main.js
:::

The main takeaways from this setup are:

1. The frontend code lives in the **public** directory. A frontend is simply the part of an application that your end user will interact with
2. The backend code lives in the **cloud** directory. The backend does the behind-the-scenes work in an application. This includes saving things to the database and sending data.

*The frontend tells the backend what to do by sending HTTP requests. In our case, this means running cloud functions*

:::hint{type="info"}
**Please also note the simplicity of this setup. Three HTML files represent the three pages in this application. Our whole backend is a single file!**
:::

In Step 2 we will take a brief look at the frontend code- that is, the public directory. In Step 3 we move to the backend.&#x20;

## 1 - Preparing the files

**As mentioned in the&#x20;**[**prerequisites**](https://www.back4app.com/docs/advanced-guides/web-application-hosting#prerequisites)**, you should have a fresh project on Back4App created AND&#x20;**[**your CLI tool configured**](https://blog.back4app.com/2017/01/20/cli-parse-server/)

Before visiting any of the codes, you’ll have to have it downloaded and ready. In this step, we do just that. Please note that you will run several commands on your command line. I will give you each of them to copy and run. If you feel confused during this step, don’t worry; this is just the process necessary to connect a Back4App app to a project I have on Git. It is not important to know what’s going on.

In this step we:

1. Initialize a local directory with your Back4App project using the CLI
2. Pull the example project files into this directory using .git

**Initialization with Back4App**

On your command line run

:::BlockQuote
1 b4a new
:::

You should be prompted:

:::BlockQuote
1   Would you like to create a new app, or add Cloud Code to an existing app?
2   Type "(n)ew" or "(e)xisting":
:::

Go with “e” for existing. Then select the application that you created from the list.

Next, you’ll be asked to name the directory where the code will be installed. You can just hit ‘enter’ if you don’t have a preference. For the sake of this project, I will assume the directory is called “ticketlister”. Finally, when asked:

:::BlockQuote
1   Directory Name:
2   You can either set up a blank project or download the current deployed Cloud Code
3   Please type "(b)lank" if you wish to setup a blank project, otherwise press ENTER
:::

Just hit enter (do NOT hit blank). When this command returns, you can cd into the new directory. You should see two directories, one called “cloud” the other called public”.

**Your entire output should look something like this:**

:::BlockQuote
1   $ b4a new
2   Would you like to create a new app, or add Cloud Code to an existing app?
3   Type "(n)ew" or "(e)xisting": e
4   1: ticketlister
5   Select an App to add to config: 11
6   Please enter the name of the folder where we can download the latest deployed
7   Cloud Code for your app "ticketlister"
8
9   Directory Name:&#x20;
10  You can either set up a blank project or download the current deployed Cloud Code
11  Please type "(b)lank" if you wish to setup a blank project, otherwise press ENTER:&#x20;
12  Successfully configured email for current project to: "JACKCONSIDINE3\@GMAIL.COM"
13  Your Cloud Code has been created at /tmp/ticketlister.
14
15  This includes a "Hello world" cloud function, so once you deploy,
16  you can test that it works, with the printed curl command.
17
18  Next, you might want to deploy this code with:
19
20	  cd /tmp/ticketlister
21	  b4a deploy
22
23  Once deployed you can test that it works by running:
24  curl -X POST \\
25   -H "X-Parse-Application-Id: Ivy4QAJQuAjDhpqQ2D3MCR4jlrCvDcVVH6yom1kk" \\
26   -H "X-Parse-REST-API-Key: yLgPHNEnt0jnzWy9BYt6ZCWHqmsWRyvCfsmqrvuS" \\
27   -H "Content-Type: application/json" \\
28   -d "\{}" \\
29   https\://parseapi.back4app.com/functions/hello
30
31  $ cd ticketlister&#x20;
32  $ ls
33  cloud  public
:::

**Syncing the app with the project files**

In addition to the cloud and public folders, there will be two files in your directory:

- .parse.local
- .parse.project

These hold data pertaining to the Back4App project. Everything else should be overwritten with the existing project files from [**the repo**](https://github.com/back4app/back4app-ticketlister). The following is the easiest way to do this:

:::BlockQuote
1   cd ticketlister
2   git init
3   git remote add origin https\://github.com/back4app/back4app-ticketlister
4   git fetch origin
5   git checkout --force -b  master --track origin/master
:::

If everything has worked, you should now be set with the following files:

:::BlockQuote
$ ls -R
README.md         cloud             index.js          package-lock.json package.json      public

./cloud:
main.js

./public:
css         index.html  js          login.html  signup.html

./public/css:
bootstrap.min.css signin.css

./public/js:
main.js   parse.js  signin.js signup.js
:::

Don’t worry- that was the hard part! Now we can focus on the project.

## 2 - The Frontend

As a reminder, the frontend code for this app lives in the **public** directory. To keep things relatively simple, I opted not to use a front-end framework like React, Angular, or Vue. This way, there are no external dependencies or builds.

:::hint{type="info"}
The project does use HTML5 Web Components. These are supported natively in the browser. They help encapsulate the functionality of different parts of the user interface. They allow the developer to declare new HTML elements (think ‘\<p>’). Otherwise, they just use plain-old JavaScript.
:::

In th&#x65;**&#x20;public/js** directory, there are 4 JavaScript files:

:::BlockQuote
$ ls public/js
\# main.js   parse.js  signin.js signup.js
:::

1. **main.js** is the code loaded by the main page, **index.html**. This page is where users list tickets etc.
2. **signup.js** is the code loaded by the signup page, **signup.html**
3. **signin.js** is the code loaded by the sign in page, **login.html**
4. **parse.js** is a simple file that all the pages use. It creates a connection to the backend. This is the only file you will need to edit and the project will not work unless you do!

**Adding your Back4App credentials**

First, you’ll need to grab your **Application ID** and your **JavaScript Key** from your Back4App project. After logging in to Back4App, select your project. Then click **App Settings** on the left-hand side, and select **Security & Keys**.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wm1jDb3MY4-REOljU0KMQ_image.png" signedSrc size="70" width="602" height="852" position="flex-start" caption}

You should see several keys displayed. Grab the **Application ID** and **JavaScript Key** and keep them handy.

Finally, open up **public/js/parse.js** and place each of the strings in the proper place. Remember to make sure the serverURL is **https\://parseapi.back4app.com**.

```javascript
1   // PART 1: Put your APP ID, JS Key, and SERVER URL
2   Parse.initialize(
3     '', // YOUR APP ID
4     '' // YOUR Javascript  KEY
5   );
6   // YOUR SERVER URL
7   Parse.serverURL = 'https://parseapi.back4app.com';
```

The application now can communicate with the server!

&#x20;**A shallow dive into the code.**

Though all of the code in this project is outside the scope of this guide, I encourage you to browse each of the files. Nothing is to complex, and I’d like to take a quick minute to give a 1,000-foot view.

- This project uses [**HTML5 Web Components**](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) to encapsulate each logical section of the interface.
- The important markup in the HTML files resides within the HTML \<template> tags. This is how we describe the layout
- The “functionality” of the application occurs in the JavaScript files. This is where the app describes what to do when a form is submitted, or a button is clicked etc.

For example, take the login component. The markup (**public/login.html**) looks like this:

```html
1   <template id="signin-template">
2     <style>
3       @import 'css/signin.css';
4       @import 'css/bootstrap.min.css';
5     </style>
6     <div class="signin-wrapper text-center">
7       <form class="auth-form">
8         <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
9         <label for="inputEmail" class="sr-only">Email address</label>
10        <input
11          type="email"
12          id="inputEmail"
13          class="form-control"
14          placeholder="Email address"
15          required=""
16          autofocus=""
17        />
18        <label for="inputPassword" class="sr-only">Password</label>
19        <input
20          type="password"
21          id="inputPassword"
22          class="form-control"
23          placeholder="Password"
24          required=""
25        />
26        <button class="btn btn-lg btn-primary btn-block" type="submit">
27          Sign in
28        </button>
29        <div class="text-center"><a href="/signup.html"> Sign Up</a></div>
30      </form>
31    </div>
32  </template>
33  <!-- This tag below simply tells the browser to render the component we declared above -->
34  <login-form></login-form>
```

And the functionality appears in the JavaScript file (**public/signin.js**)

```javascript
1   // Code above ^
2       // When the code is ready, listen for the form to be submitted. When it is,
3       //  call the 'onSubmit' method
4       connectedCallback() {
5         const form = this.shadowRoot.querySelector('form');
6         form.addEventListener('submit', this.onSubmit.bind(this), false);
7       }
8     // Obtain the email and password from the markup inputs
9       onSubmit(e) {
10        e.preventDefault();
11        //   Get inputs
12        const email = this.shadowRoot.querySelector('#inputEmail').value;
13        const password = this.shadowRoot.querySelector('#inputPassword').value;
14        this.login(email, password);
15      }
16    // Send a request to the backend, attempting to login. If the login
17    //  is successful, go to the index.html page. Otherwise, give the user
18    // an alert explaining what went wrong
19      login(email, password) {
20        // Add login method here
21        Parse.User.logIn(email, password)
22          .then(user => {
23            window.location.href = 'index.html';
24          })
25          .catch(e => {
26            alert(e.message);
27          });
28      }
29      // More code below
30
```

The whole application takes this general structure. Keep an eye out for the times the front end talks to the backend like this: (**public/js/main.js**).

In the next step, we’ll look into how these functions are declared.

## 3 - The Backend

The entire backend will live in **cloud/main.js**, the Cloud Code functions file. It consists of a very modest amount of code, attesting to how much we can accomplish for so little with Back4App.

Part of the app (creating events that tickets can list under) will simply use the Back4App dashboard. This awesome functionality comes with our project, so no need to reinvent the wheel!

Again, examining each line of code is outside our scope. We will, however, take another broad view of how the code works.



- You declare **Cloud Functions** in the **cloud/main.js** file. These functions can be invoked from the front end (see **Step 2**). For more information on Cloud Functions, see [**the documentation**](https://docs.parseplatform.org/cloudcode/guide/#cloud-functions).
- Furthermore, these Cloud Functions are run on a Parse Server. This [**guide**](https://www.back4app.com/docs/advanced-guides/parse-server-3) discusses some of the syntax that’s used, so it may be helpful to have a look.

More specifically, the functions we define our:

1. ‘**user\:signup**’ - Code for handling user signup flow
2. ‘**tickets\:list**’ - Code for retrieving all listed tickets
3. ‘**tickets\:create**’ - Code for creating a new ticket
4. ‘**events\:list**’ - Code for listing all events

And one last code note: I added a simple method towards the top of the file:

```javascript
1   const requireAuth = user => {
2     if (!user) throw new Error('User must be authenticated!');
3   };
```

Certain Cloud Functions require a user to be logged in. By calling this function with the user property of the request, we ensure that no one can make unauthorized requests.

I highly encourage you to skim the rest of the functions to see how they work. Now that you know what they do, we can deploy!

## 4 - Deploying

We’ve buttoned up all the code, and now the app can be deployed to Back4App. The following command will upload all public and cloud files:

:::BlockQuote
b4a deploy
:::

**Local website hosting**

To obtain a public domain to view your uploaded web app, you will need to switch on Web Hosting from your Back4App dashboard.

First, open “Server Settings” on the left side of the dashboard:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/V5-yoz42if7bmLRlv-pU3_image.png" signedSrc size="70" width="500" height="715" position="flex-start" caption}

Next, click the “Settings” link under “Web Hosting and Live Query”

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/VOlHTaDxFfwg6chUQZRnT_image.png" signedSrc size="70" width="500" height="559" position="flex-start" caption}

And finally, check “Activate Back4App Hosting”. You’ll need to pick a unique subdomain; I already claimed ticketlister for this project so pick something different. Optionally, you can configure a domain you own to “point” to this back4app domain. I did this for [**http://ticketlister.koptional.com**](https://www.back4app.com/docs/advanced-guides/my%20website) and my settings look like this:&#x20;

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/YlLshpzkdaVyh9C-gVoQA_image.png" signedSrc size="70" width="500" height="484" position="flex-start" caption}

Please note the text below “Custom Domain”, if you plan to launch off your website.

If you complete this step properly, you can go to your domain and use the app. If you don’t have a custom domain, just open http\://\<YOUR\_SUBDOMAIN>.back4app.io, where YOUR\_SUBDOMAIN is the name you just selected.

## 5 - Usage and the Dashboard

To start listing tickets, you’ll have to create an event from the admin dashboard on Back4App.

Go to the data browser, and create an ‘Event’ class. Add the columns ‘name’ (a string), and ‘when’ (a date). Then you can add an event directly. Remember to fill out all columns. It should look something like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/eSQqyJ80U9z16k7RVRxGq_image.png" signedSrc size="70" width="1086" height="636" position="flex-start" caption}

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/M8tpIQJ10s21Q5x7xTWJo_image.png" signedSrc size="70" width="1082" height="636" position="flex-start" caption}

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/HyMOBwx-36Yst_44UDAG6_image.png)

Now, on your web app, you can log in and list a ticket with that event.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/7Q7WtLTkpTcsr8EXY-LaS_image.png)

This admin functionality that comes with Parse / Back4App is another shortcut that decreases your workload.

## Conclusion

Creating a web application with a backend is something that often takes weeks and months. We took advantage of Back4App’s powerful infrastructure and the Parse SDK to launch one much quicker. Using this approach for any application allows you to build amazing things without wasting time.
