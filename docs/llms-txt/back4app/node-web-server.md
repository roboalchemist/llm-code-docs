# Source: https://docs-containers.back4app.com/docs/js-framework/node-web-server.md

---
title: Express.js
slug: docs/js-framework/node-web-server
description: In this guide you learn how to download a Node JS App.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-07T13:31:50.743Z
updatedAt: 2025-01-17T01:07:25.834Z
---

# Hosting your Node.JS web application on Back4App servers

## Introduction

This tutorial explains how you can set up a subdomain and easily host static pages. After completing this step-by-step guide, you will be able to use a Node JS App to Register and Login Users.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- If you want to test this App locally, you need to install Node JS in your local environment. You can follow the
- An app created with Back4App.
  - Check out
- Back4App Command Line Configured with the project.
  - Go through the
:::

## First off, let’s talk about our new simple application!

We’ll describe an example about the usage of Web hosting with Node JS!

Let’s imagine that we need to build a simple Log in, Register and request password from Users included in your Back4App Dashboard. We will be able to use Bootstrap, Static files (CSS and Images) and usign Express in the Project.

See the live app here: [**nodeapplication.back4app.io**](https://nodeapplication.back4app.io/).

:::hint{type="info"}
You can clone this complete application in the App code templates on the Back4App Platform [**here**](https://www.back4app.com/database/back4app/node-app-template).
:::

Firstly, complete the set up using the Command Line Interface ([**see prerequisites**](https://www.back4app.com/docs/js-framework/node-web-server#content-prerequisites)), to understand how it will work with the final structure from the files:

:::BlockQuote
├── NodeJSWebApp/
│  ├── cloud/
│  │   ├── app.js
│  │   ├── routes.js
│  │   ├── package.json
│  │   ├── views/
│  │   │   ├── head.ejs
│  │   │   ├── index.ejs
│  │   │   ├── reset\_password.ejs
│  ├── public/
│  │   ├── images/
│  │   ├── css/
│  │   │   ├── style.css
:::

## 1 - Enable your subdomain name on Back4app

Enable your Web Hosting feature, please follow the steps available in the guide below:

&#x20;                                  [**Activating your Web Hosting and Live Query**](https://www.back4app.com/docs/platform/parse-web-hosting)

## 2 - Create and upload files

Before getting started with this step, we recommend you using Command Line Tool ([**see prereqs**](https://www.back4app.com/docs/js-framework/node-web-server#content-prerequisites)) to upload your files easily!

First off, create the files called as app.js and package.json inside the cloud directory!

::::ExpandableHeading
**Install modules in Back4App**

Inside the cloud folder (in your terminal), you need to write:

:::BlockQuote
$ touch package.json
:::

Now, insert the npm module ‘body-parser’ inside the file package.json:

```json
1   {
2     "dependencies": {
3       "body-parser": "*"
4     }
5   }
```

:::hint{type="danger"}
**Troubleshooting:&#x20;**&#x49;t is not necessary to run npm install inside the cloud folder because the Back4App server will install it automatically
:::
::::

:::ExpandableHeading
**app.js**

```javascript
1   // Require the module
2   var bodyParser = require("body-parser");
3
4   // Set up the views directory
5   app.set('views', __dirname + '/views');
6   app.set('view engine', 'ejs');
7
8   // Set up the Body Parser to your App
9   app.use(bodyParser.json());
10  app.use(bodyParser.urlencoded({extended: true})); 
11
12  //Require the routes.js file
13
14  require('./routes');
```
:::

## 3 - Create the views to your App

We’ll provide template EJS files to make the template App, you can change it anytime at your end. :)

**Returning to the terminal**

Inside the Cloud directory, it is necessary to create the views folder and the following EJS files:

- head.ejs- We will use it to add content to head of HTML structure.
- index.ejs- We will use it to Register and Log in users.
- reset\_password.ejs- We will use it for the user request the Password Reset.

:::hint{type="warning"}
**Hint:&#x20;**&#x57;e will construct the views using Bootstrap, [**click here**](https://getbootstrap.com/) to read more about it.
:::

You can add content to your respective views. You can use the below templates without any hassle:

:::CodeblockTabs
head.ejs

```nodejs
1   <title>Back4App - Node JS Application</title>
2     <meta charset="utf-8">
3     <meta name="viewport" content="width=device-width, initial-scale=1">
4     <link rel="shortcut icon" type="image/png" href="/favicon.png"/>
5     <!-- Bootstrap CSS--> 
6     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
7
8     <!-- jQuery--> 
9     <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
10
11    <!-- Bootstrap JS--> 
12    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
13
14    <!-- Stylesheet Pages -->
15    <link rel="stylesheet" type="text/css" href="/css/style.css">
```

index.ejs

```nodejs
1   <!DOCTYPE html>
2     <html>
3     <head>
4       <% include head.ejs %>
5     </head>
6     <body>
7       <section id="header">
8         <div class="container">
9           <div class="row">
10            <div class="col-sm-6">
11              <div class="box-settings box-register">
12                <div class="wrap-login100">
13                  <form class="validate-form" method="POST" action="/users/register">
14                    <h2 class="title-screen">
15                      Register a new account
16                    </h2>
17                    <div class="form-group">
18                      <input type="text" name="usernameRegister" placeholder="Username" class="form-control" value="<%= infoUser.usernameRegister %>">
19                    </div>
20                    <div class="form-group">
21                      <input type="text" name="emailRegister" placeholder="Email" class="form-control" value="<%= infoUser.emailRegister %>">
22                    </div>
23                    <div class="form-group">
24                      <input type="password" name="passwordRegister" placeholder="Password" class="form-control" value="<%= infoUser.passwordRegister %>">
25                    </div>
26                    <% if (RegisterMessage != 'undefined' ? RegisterMessage  : '' ) { %>
27                      <div class="alert alert-<%= typeStatus %>" role="alert">
28                        <p><%= RegisterMessage %></p>
29                      </div>
30                    <% } %>
31                    <div class="form-group">
32                      <button class="btn-login btn">
33                        Register
34                      </button>
35                    </div>
36                  </form>
37                </div>            
38              </div>
39            </div>
40            <div class="col-sm-6">
41              <div class="box-settings box-login">
42                <div class="wrap-login100">
43                  <form class="validate-form" method="POST" action="/users/login">
44                    <h2 class="title-screen">
45                      Access your account
46                    </h2>
47                    <div class="form-group">
48                      <input type="text" name="usernameLogin" placeholder="Username" class="form-control" value="<%= infoUser.usernameLogin %>">
49                    </div>
50  
51                    <div class="form-group">
52                      <input type="password" name="passwordLogin" placeholder="Password" class="form-control" value="<%= infoUser.passwordLogin %>">
53                    </div>
54                    <% if (loginMessage != 'undefined' ? loginMessage  : '' ) { %>
55                      <div class="alert alert-<%= typeStatus %>" role="alert">
56                        <p><%= loginMessage %></p>
57                      </div>
58                    <% } %>
59                    <div class="form-group">
60                      <button class="btn-login btn">
61                        Login
62                      </button>
63                    </div>
64  
65                    <div class="text-forgot">
66                      <a href="/users/forgot-password">
67                        Forgot Password? Click here to retrive your access!
68                      </a>
69                    </div>
70                  </form>
71                </div>            
72               </div>
73            </div>
74          </div>
75        </div>
76      </section>
77    </body>
78    </html>
```

reset\_password.ejs

```nodejs
1   <!DOCTYPE html>
2     <html>
3     <head>
4       <% include head.ejs %>
5     </head>
6     <body>
7       <section id="header">
8         <div class="container">
9           <div class="row">
10            <div class="col-sm-offset-3 col-sm-6" align="center">
11              <div class="box-settings box-password">
12                <div class="wrap-login100">
13                  <form class="validate-form" method="POST" action="/users/forgot-password">
14                    <h2 class="title-screen">
15                      Retrieve your access
16                    </h2>
17                    <p>Insert your email address</p>
18                    <div class="form-group">
19                      <input type="text" name="email" placeholder="Email" class="form-control" value="<%= infoUser.email %>">
20                    </div>
21                    <% if (resetPass != 'undefined' ? resetPass  : '' ) { %>
22                      <div class="alert alert-<%= typeStatus %>" role="alert">
23                        <p><%= resetPass %></p>
24                      </div>
25                    <% } %>
26                    <div class="form-group">
27                      <button class="btn-login btn">
28                        Reset Password
29                      </button>
30                    </div>
31                  </form>
32                </div>            
33              </div>
34            </div>
35          </div>
36        </div>
37      </section>
38    </body>
39    </html>
```
:::

## 4 - Create the routes to render the views

Now, we need to configure the Routes to render the views that were created previously. The routes will be built using [**Express**](https://expressjs.com/).

```nodejs
1   // Index
2   app.get('/', (req, res) => {
3     res.render('index', {loginMessage: '', RegisterMessage: '', typeStatus: '',  infoUser: ''});
4   });
5   // Request Password
6   app.get('/users/forgot-password', (req, res) => {
7     res.render('reset_password', { resetPass: '', typeStatus: '', infoUser: ''});
8   });
```

:::hint{type="warning"}
**Hint:&#x20;**&#x41;s you can see, we are configuring variable as parameters, which will be used to display alerts on the page.
:::

## 5 - Create the routes to save the informations to your database

We will use the [**Parse Server Javascript Guide**](https://docs.parseplatform.org/js/guide/) as a reference for developing our functions for Register, Login and Request the Password.

```javascript
1   // Request the Log in passing the email and password
2   app.post('/users/login', async(req, res) => {
3     let infoUser = req.body;
4  
5     try{
6       let user = await Parse.User.logIn(infoUser.usernameLogin, infoUser.passwordLogin)
7       res.render('index', { loginMessage: "User logged!", RegisterMessage: '', typeStatus: "success",  infoUser: infoUser });
8     } catch (error){
9       res.render('index', { loginMessage: error.message, RegisterMessage: '', typeStatus: "danger",  infoUser: infoUser});
10    }
11  });
12
13  // Register the user passing the username, password and email
14  app.post('/users/register', async(req, res) => {
15    let infoUser = req.body;    
16    let user = new Parse.User();
17  
18    user.set("username", infoUser.usernameRegister);
19    user.set("password", infoUser.passwordRegister);
20    user.set("email", infoUser.emailRegister);
21
22    try{
23      await user.signUp();
24      res.render('index', { loginMessage : '', RegisterMessage: "User created!", typeStatus: "success",  infoUser: infoUser});
25    } catch (error) {
26      res.render('index', { loginMessage : '', RegisterMessage: error.message, typeStatus: "danger",  infoUser: infoUser});
27    }
28  });
29
30  // Request the Password reset passing the email
31  app.post('/users/forgot-password', function(req, res) {
32    let infoUser = req.body;
33    try{  
34      await Parse.User.requestPasswordReset(infoUser.email);
35      res.render('reset_password', { resetPass: "Check your email!", typeStatus: "success", infoUser: infoUser});
36    } catch (e){
37      res.render('reset_password', { resetPass: error.message, typeStatus: "danger", infoUser: infoUser});
38    }
39  });
```

## 6 - Almost there! Static files in public folder

It’s not over yet! In the public folder, you can insert static files such as CSS and images to require this on the views :)

When you add files to CSS and images, you are able to provide different stylesheets to your Website created!

## 7 - It’s done!

Up to this point, you have splendidly learned how to create a Node JS Application using Cloud code.

:::hint{type="info"}
Click on [**this link**](https://nodeapplication.back4app.io/) to access the complete Project in Back4App at anytime.
:::

With the steps described above, you’ll be able to work with the Web Hosting when using a Node JS application!
