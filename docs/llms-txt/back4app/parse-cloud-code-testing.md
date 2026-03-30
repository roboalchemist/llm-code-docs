# Source: https://docs-containers.back4app.com/docs/advanced-guides/parse-cloud-code-testing.md

---
title: Integrated Tests
slug: docs/advanced-guides/parse-cloud-code-testing
description: In this guide you learn how to integrate tests in Back4App.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-27T19:01:11.470Z
updatedAt: 2025-01-15T19:25:52.449Z
---

# How to integrate tests into your Parse Cloud Code functions

## Introduction

***This is a guide written by&#x20;***[**John Considine**](https://github.com/considine)***, our guest writer and lead developer at&#x20;***[**K-Optional**](https://koptional.com/)***. The tutorial covers how to setup automated tests for your Back4App Cloud Code.***

We will talk briefly about moving some of your client Parse code to the cloud, and then about how integrate your project with a testing ecosystem. You can also check out the [**example project**](https://github.com/back4app/template-cloud-code-unit-test) directly for a working version.

## Goals

We hope to combine the robust, scalable aspects of automated tests with the developer-friendly Parse environment. By leveraging Cloud Code, perhaps an underappreciated feature of Parse, developers can continue to rapidly iterate their code AND be confident that the software will run as expected.

[**Test Driven Development**](https://en.wikipedia.org/wiki/Test-driven_development) is an immense field; rather than talk philosophically about testing, we will run through an implementation and talk about some strategies (stubbing for instance).

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you need:**

- An app at Back4App.
- Follow the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Back4App Command Line Configured with the project
- Follow the [**Setting up Cloud Code tutorial**](https://www.back4app.com/docs) to learn how to set up cloud code for a project
- npm installed on your command line
:::

**Note: This library will use the&#x20;**[**JavaScript Promise**](https://www.promisejs.org/)**, which shouldn’t be too complicated**

## Let’s create a basic social media backend

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/RVQdoVboWH_oPulNo6y6e_image.png)

Ok! Imagine a social media application that includes a profile model to go along with the user model. For some apps, you may place profile information in the user model, although in many cases this is not efficient; you often will need to separate the concerns of authorization/authentication with user content, and thus maintain two different models.

In this tutorial, we will be implementing a feature that manages the creation of users and profiles in this way, placing minimal strain on the client. Let’s get started!

### **1. Defining Our Functions**

**This assumes you have a Back4App project created, and the command line tool installed (see prerequisites).**

**For examples of frontend code, this guide will refer to the Parse JavaScript SDK syntax for simplicity**

When someone signs up for this application, a profile should be created and coupled to the user object.

**The signup function**

On many Parse applications, you will create the user with the following syntax

```javascript
1   var user = new Parse.User();
2   user.set("username", "my name");
3   user.set("password", "my pass");
4   user.set("email", "email@example.com");
```

In our case, we would like to also initialize a Profile, and point it at the User object.

:::CodeblockTabs
Parse Server 3.X

```javascript
1   try {
2     await user.signUp(null, {useMasterKey : true});
3     let Profile = Parse.Object.extend("Profile");
4     let profile = new Profile({
5       firstname : params.firstname,
6       lastname : params.lastname,
7       user : user
8     })
9     return profile.save(null, {useMasterKey : true});
10   } catch (err){
11     return (err.message);
12   }
```

Parse Server 2.X

```javascript
1   user.signUp(null, {
2     success : function (newUser) {
3       var Profile = Parse.Object.extend("Profile");
4       var profile = new Profile();
5       profile.set("firstname", "John");
6       profile.set("lastname", "Smith");
7       profile.set("user", newUser);
8       profile.save();
9     },
10    error : function (err) {
11      // handle error
12    }
13  })
```
:::

You could shorten that syntax to be something like this:

:::CodeblockTabs
Parse Server 3.X

```javascript
1   let user = new Parse.User({
2     username : params.username,
3     password : params.password,
4     email : params.email
5   });
6
7   try {
8     await user.signUp(null, {useMasterKey : true});
9     let Profile = Parse.Object.extend("Profile");
10    let profile = new Profile({
11      firstname : params.firstname,
12      lastname : params.lastname,
13      user : user
14    })
15    return profile.save(null, {useMasterKey : true});
16  } catch (err){
17    return (err.message);
18  }
```

Parse Server 2.X

```javascript
1   var user = new Parse.User({
2     username : params.username,
3     password : params.password,
4     email : params.email
5   });
6   user.signUp(null)
7   .then((newUser) => {
8     var Profile = Parse.Object.extend("Profile");
9     var profile = new Profile({
10      "firstname" : "John",
11      "lastname" : "Smith",
12      "user" : newUser
13   });
14    return profile.save();
15  })
```
:::

Unfortunately, this still involves making two separate requests to the Parse Server which is inefficient for a frontend to do; it is wise to avoid multiple-step client-server communication flows when possible.

Also, regarding security, the above code is putting the creation process in a client's hands which is never smart. We would like to prevent our data integrity from relying on a client properly completing all steps of a flow. They could, for example, send a custom request that creates a user with no profile, corrupting the app’s persistent data.

Why not do this all in one step using cloud code? It can prevent bloating of frontend code, and ensure that the client is not doing unnecessary/insecure work!

**Here’s what we want to do instead from the client for sign up**

```javascript
1   Parse.Cloud.run('signupUser',
2   {
3     username: 'myname',
4     password : "mypass",
5     email : "email@example.com",
6     firstname : "John",
7     lastname : "Smith" }
8   ).then(function(newuser) {
9
10  });
```

*Parse also defines for&#x20;*[**beforeSave**](http://docs.parseplatform.org/cloudcode/guide/#beforesave-triggers)*&#x20;triggers, allowing the creation of the profile when the user signs up. However by using a function we may intuitively pass firstname and lastname attributes that the profile will use*&#x20;

**Cloud code signup function**

Let's get started! Move to your project directory that is synced with Back4App (see prereqs if you don’t know what this means). We will assume the following structure:

:::BlockQuote
1   ./cloud
2   ./cloud/main.js
:::

In our case, upon initialization, we chose ‘cloud’ as our Directory Name. Your directory can be called whatever you want.

:::CodeblockTabs
Parse Server 3.X main.js

```javascript
1   Parse.Cloud.define("signuserUp", async(request) => {
2     // Make sure the necessary parameters are passed first
3     let params = request.params;
4     if (!params.username || !params.email || !params.password || !params.firstname || !params.lastname)
5       throw new Error("Missing parameters: need username, email, password, firstname, & lastname");
6
7     // Execute the signup flow
8     let user = new Parse.User({
9       username : params.username,
10      password : params.password,
11      email : params.email
12    });
13
14    try {
15      await user.signUp(null, {useMasterKey : true});
16      let Profile = Parse.Object.extend("Profile");
17      let profile = new Profile({
18        firstname : params.firstname,
19        lastname : params.lastname,
20        user : user
21      })
22      return profile.save(null, {useMasterKey : true});
23    } catch (err){
24      return (err.message);
25    }
26  });
```

Parse Server 2.X main.js

```javascript
1   Parse.Cloud.define("signuserUp", function(request, response) {
2     // Make sure the necessary parameters are passed first
3     var params = request.params;
4     if (!params.username || !params.email || !params.password || !params.firstname || !params.lastname)
5       return response.error("Missing parameters: need username, email, password, firstname, & lastname");
6
7     // Execute the signup flow
8     var user = new Parse.User({
9       username : params.username,
10      password : params.password,
11      email : params.email
12    });
13    user.signUp(null, {useMasterKey : true})
14    .then((newUser) => {
15      var Profile = Parse.Object.extend("Profile");
16      var profile = new Profile({
17        firstname : params.firstname,
18        lastname : params.lastname,
19        user : newUser
20      })
21      return profile.save(null, {useMasterKey : true});
22    })
23    .then((prof) => response.success(prof))
24    .catch((e) => {
25      response.error(e.message);
26    })
27  });
```
:::

*You may notice the ‘useMasterKey’ option being passed; this allows the cloud code to supersede any Roles or ACLs that may be in place. Since the client doesn’t touch this code, there is no risk of them hijacking our server. However, please be careful with this flag!*

In case it’s not obvious why this might be preferable to placing this functionality in the client code, here are some advantages:

- Offloads computation to the server rather than the device
- Explicitly defines the functionality of a process
- Easier to create fail-safe functions
- Gives the client an intuitive interface
- This prevents the possibility that a client will ‘half-do’ a process.

### **2. Refactoring our directory structure**

Great, we’ve created two cloud functions. We could obviously test these functions by running them and checking the Parse Dashboard, but that is not scalable or efficient. We instead want to create automated tests specifically for the methods that can be run continuously. So we will separate our code a little bit.

We will move the functions we created in main.js to a new file called cloud-functions.js (in the same directory). Then we will *import* these functions into main, and bind them to the Cloud Function definitions. The idea is to *decouple* the functions from the cloud interface so we may test them without inefficiently sending HTTP requests. This will make a lot of sense as we create the test suite.

**create the functions file**

:::BlockQuote
\# remember,  the 'cloud' directory was determined
\# when we initialized the directory with our Back4App project
\# check the Prerequisites if this does not make sense
touch ./cloud/cloud-functions.js
:::

You may be aware that you can use ‘require’ in Node.js to pull in functions, objects, and variables from other files.

We will thus define functions corresponding with the Parse Cloud Function we created in Step 1.

One possibly confusing point is that the functions we are defining will be *returning functions*, which then can be hooked into the Parse Cloud definition. It may seem strange to use a function to return a function, but this will give us the power to swap out Parse Servers later on when we are writing our tests.

You may have noticed that you can use the Parse object in your Cloud Code, without ever having to define or import it. This is due to the server that runs this code adding Parse automatically. However, if we want to run tests on the functions locally, we are not afforded an instance. As a matter of fact, we would like to supply our own instance that corresponds to a test Parse server, where there is no harm in data being created or deleted.

So each function will accept
‘Parse’ as a parameter, and return the cloud functions.

:::CodeblockTabs
Parse Server 3.X cloud-functions.js

```javascript
1   // cloud-functions.js
2   module.exports.SignupUser = function(Parse) {
3     return async(request) => {
4       // Copied from main.js:
5       // Make sure the necessary parameters are passed first
6       let params = request.params;
7       if (!params.username || !params.email || !params.password || !params.firstname || !params.lastname)
8         throw new Error("Missing parameters: need username, email, password, firstname, & lastname");
9
10      // Execute the signup flow
11      let user = new Parse.User({
12        username : params.username,
13        password : params.password,
14        email : params.email
15      });
16
17      try {
18        await user.signUp(null, {useMasterKey : true});
19        let Profile = Parse.Object.extend("Profile");
20        let profile = new Profile({
21          firstname : params.firstname,
22          lastname : params.lastname,
23          user : user
24        })
25        return profile.save(null, {useMasterKey : true});
26      } catch (err){
27        return (err.message);
28      }
29    }
30  }
```

Parse Server 2.X cloud-functions.js

```javascript
1   // cloud-functions.js
2   module.exports.SignupUser = function(Parse) {
3     return function (request, response) {
4       // Copied from main.js:
5       // Make sure the necessary parameters are passed first
6       var params = request.params;
7       if (!params.username || !params.email || !params.password || !params.firstname || !params.lastname)
8           return response.error("Missing parameters: need username, email, password, firstname, & lastname");
9       // Execute the signup flow
10      var user = new Parse.User({
11        username : params.username,
12        password : params.password,
13        email : params.email
14      });
15      user.signUp(null, {useMasterKey : true})
16      .then((newUser) => {
17        var Profile = Parse.Object.extend("Profile");
18        var profile = new Profile({
19          firstname : params.firstname,
20          lastname : params.lastname,
21          user : newUser
22        })
23        return profile.save(null, {useMasterKey : true});
24      })
25      .then((prof) => response.success(prof))
26      .catch((e) => {
27        response.error(e.message);
28      })
29    }
30  }
```
:::

In main.js, remove everything from before. Import the Cloud Function, and bind the function to the Cloud Function definition like this:

```javascript
1   // main.js
2   var cloudFunctions = require("./cloud-functions");
3   // Note that we are injecting the Parse instance, which is automatically supplied in the
4   // context of Parse Cloud Code, but not on local tests
5   Parse.Cloud.define("signuserUp", cloudFunctions.SignupUser(Parse));
```

Great! We have not changed the functionality at all since step 1, but we have decoupled the function from the Cloud Code.
In the next step we will create a unit test!

### **3. Create the test suite**

For our test suite we will be using [**Jasmine**](https://jasmine.github.io/), the popular testing framework. However, our code so far is completely agnostic of our tests, so you may use whatever framework or platform that you prefer.

Let’s install Jasmine and Jasmine-node (an integration of Jasmine and our Node.js environment)

:::BlockQuote
$ npm install jasmine jasmine-node --save-dev
:::

Now let’s install two libraries our test suite will use. It will use the Parse SDK to connect to a fake Parse Server, and the events library for stubbing out the request object

:::BlockQuote
$ npm install parse events --save-dev
:::

Now, using the Jasmine utility, let’s initialize our test directory.

:::BlockQuote
$ ./node\_modules/jasmine/bin/jasmine.js init
:::

If you prefer, you may install jasmine globally with $ npm install -g jasmine, then you can initialize with this $ jasmine init

*This guide will assume you do not install Jasmine globally, though it is recommended. If you do, you may replace all instances of ‘/node\_modules/jasmine/bin/jasmine.js’ with simply ‘jasmine’*

This should create a directory called spec, which itself includes a support folder containing configuration information for Jasmine.

By default, Jasmine knows to look for files that end in the “.spec.js” extension, so we will name our tests accordingly.

Create the file for our first unit test:

:::BlockQuote
$ # in the ./spec directory
$ touch signup-user.spec.js'
:::

Add a utilities directory with two files that will help with our tests:

:::BlockQuote
$ # in the ./spec directory
$ touch utils/purge-parse-table.js
$ touch utils/response-stub.js
:::

Finally, create a constants file in the same directory. The utility for this file will be explained later

:::BlockQuote
$ # in the ./spec directory
$ touch constants.js
:::

Here’s what your directory should now look like:

:::BlockQuote
├── cloud
│   ├── cloud-functions.js
│   ├── main.js
├── node\_modules
├── spec
│   ├── support
│   │   ├── jasmine.json
│   ├── utils
│   │   ├── purge-parse-table.js
│   │   ├── response-stub.js
│   ├── signup-user.spec.js
│   ├── constants.js
:::

### **4. Swapping in a test Parse Server**

**Testing around Parse**

Since our methods involve a Parse Server, we want to be able to test that interaction. There are two ways to do this:

A. We can “stub” out the Parse SDK object, by defining an object that implements the same interface. Then simply pass that object as the parameter to our cloud methods. That might look something like this.

```javascript
1   var ParseStub = {
2     // make sure all used methods  and properties are defined
3     User : function () {
4       // Constructor function
5         this.set = function (key, val) {
6           // logic here to implement the parse object set
7         }
8     }
9   }
10  signupUser(ParseStub); // returns cloud function that we can test
```

B. Another approach is to set up a real Parse Server that will serve only for test data. This will involve the slow HTTP layer that Parse uses, but also allow us to test the data in the database. In our tests we’d need to import the Parse SDK, and configure it with a test server.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xONtQ4ACrrwyhQdmbfF-X_image.png)

*The two places that can be stubbed when testing cloud code: A.) Stub a Parse SDK that won’t make HTTP requests, or B.) Swap in a test database implementation*

Neither of these approaches is the “right” answer. It depends on what you’re trying to test. Stubbing out the interface for the Parse SDK (even just the parts we are using) is a lot of work. Additionally, we are going to test the persistence of data after saving in this example, so we will use the second approach.

Lets:

- Create a test Parse Server on Back4App
- Grab the Application ID, and Master Key and save them into our constants file
- Initialize the Parse SDK in our spec file, so our test uses the test server

You are welcome to run a local [**Parse Server**](https://github.com/parse-community/parse-server) for your tests. We will simply create another Back4App application in our dashboard.

If you need a refresher on how to provision another Back4App server, head on over to the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app). Call your application whatever you want, though it might be wise to use something like TestBackend. Then just grab the Application ID and Master Key from Dashboard > App Settings > Security & Keys.

Now save these tokens in our constants file like this:

```javascript
1   // ./spec/constants.js
2   // Paste in your app id and master key where the strings are
3   module.exports = {
4     APPLICATION_ID : "PASTE YOUR APPLICATION KEY HERE",
5     MASTER_KEY : "PASTE YOUR MASTER KEY HERE"
6   }
```

**DO NOT put the Application ID and Master Key from your Production App!!! We will be deleting data, and doing so will risk you losing data**

### **5. Testing Utilities**

Cloud functions are passed as parameters in the Express Request and Response objects.

The server automatically creates these parameters when they are run on the cloud, so for our test environments we must create doubles.

This case is easier. When a cloud function is called, data is passed; in our case, the profile and user information are passed. Every argument that is provided is accessible from the request.params property.

So if we call a cloud function like

```javascript
1   // client code, calling Parse function
2   Parse.Cloud.run('fakefunction',
3   {
4     data1: 'I am data1',
5     data2: {
6       prop : "Nested property"
7     }
8   }
9   );
```

Then the request.params property will contain the passed data:

```javascript
1   // Server code, running the Parse function
2     console.log(request.params);
3   // {
4   //   data1: 'I am data1',
5   //   data2: {
6   //     prop : "Nested property"
7   //   }
8   // }
```

Simple enough, for our tests, when calling our cloud function the first argument should be of the form

```javascript
1   {
2     params : {
3       username: 'testuser',
4       firstname: "John",
5       // the rest of the arguments
6     }
7   }
```

Thus we don’t need to create a special mock object in this case.

The response object allows the cloud code to send an HTTP response to the client representing either a success or a failure. We would like to know what is called when invoking the cloud function. Below is a [**mock object**](https://msdn.microsoft.com/en-us/library/ff650441.aspx) that will allow our test to determine whether the invocation was successful or not. If this is confusing, don’t worry, just place it in your ./spec/utils/response-stub.js file.

```javascript
1   // ./spec/utils/response-stub.js
2   const EventEmitter = require('events');
3   /**
4    * Wrapper around response stub. Simplifies testing cloud functions that
5    * employ a response parameter
6    */
7   function ResponseStub () {
8     this.responseListener = new EventEmitter();
9     this.responseStub = {};
10    /**
11     * Success method that cloud functions expect
12     */
13    this.responseStub.success = (resp) => {
14      this.responseListener.emit("success", resp);
15    }
16    /**
17     * Error method that cloud functions expect
18     */
19    this.responseStub.error = (resp) => {
20      this.responseListener.emit("error", resp);
21    }
22    /**
23     * Listens for errors and successes from stub and returns Promise that resolves or rejects accordingly
24     */
25    this.resolver = new Promise((resolve, reject) => {
26      this.responseListener.on("success", (resp) => resolve(resp));
27      this.responseListener.on("error", (err) => reject(err));
28    });
29  }
30
31  /**
32   * reeturns stub to feed to cloud function
33   */
34  ResponseStub.prototype.getStub = function () {
35    return this.responseStub;
36  }
37
38  /**
39   * returns promise that will indicate the success or failure
40   */
41  ResponseStub.prototype.onComplete = function () {
42    return this.resolver;
43  }
44
45  module.exports = ResponseStub;
```

In short, this javascript constructor function will provide a way for our test to pass in a response object which indicates by Promise resolution / rejection whether the Cloud Function would have returned a success or an error.

**Cleaning up the database**

We obviously don’t want our test Parse database to hold onto what is accumulated during a test. Let's define a utility for clearing database tables, that can be called prior to (or after) test cases.

Add the following to ‘spec/utils/purge-parse-table.js’:

```javascript
1   // spec/utils/purge-parse-table.js
2   /**
3    * Removes all rows from the Parse Database
4    * @param  {string} tablename the name of the parse table to be purged
5    * @return {Promise}  promise to destroy each item  in the table
6    */
7   module.exports = function (Parse) {
8     return (tablename) => {
9       var tableQuery;
10      if (tablename === "User")
11        tableQuery = new Parse.Query(Parse.User);
12      else tableQuery = new Parse.Query(tablename);
13      return tableQuery.find({useMasterKey : true}).then((items) => {
14        var destroyQueue = [];
15        for (var i=0; i<items.length; i++) {
16          destroyQueue.push(items[i].destroy({useMasterKey : true}));
17        }
18        return Promise.all(destroyQueue).catch((e) => {console.log("Error destroying: " + e.message)});
19      });
20    }
21  }
```

**After defining this function, it is a good time to remind you to make sure your spec/utils/constants.js is configured to your TEST Parse Application, NOT your Production Parse Application. This will delete data, so please confirm that this is the empty database you created above**

This function accepts our configured Parse SDK, and returns another function. The returned function accepts a tablename, and removes all data from the corresponding Parse table.

*Again, the idea of returning a function may seem strange, but it allows the test spec to configure the Parse endpoint, and then reference a function that will clear THAT Parse endpoint’s table*

Awesome! Now let’s write our test!

### **6. Test that the Cloud Function will send an error if the proper parameters are not passed**

The Cloud Function relies on certain parameters being included and *should* fail if, for example, the ‘firstname’ was not sent. Let’s be sure.

We will be editing our test file (finally!) spec/signup-user.spec.js.

Here’s what needs to happen before the test definitions:

- Import the Parse NodeJS SDK
- Import our constants, and configure the Parse SDK to point at our test server
- Import our Cloud Function
- Import our “Purge Table” utility
- Import the Response Mock Object we created

The following will do:

```javascript
1   // Hook into your testing server
2   var Parse = require('parse/node');
3   var constants = require("./constants");
4   // head over to your Parse dash board for your test server, and grab your keys. Swap out the strings with the place holders below
5   Parse.initialize(constants.APPLICATION_KEY, null, constants.MASTER_KEY);
6   // if you are running a localhost Parse server, set the serverUrl accordingly
7   Parse.serverURL = 'https://parseapi.back4app.com'
8   var signupUser = require("../cloud/cloud-functions").SignupUser(Parse);
9   var purgeTable = require("./utils/purge-parse-table")(Parse);
10  var ResponseStub = require("./utils/response-stub");
```

Now let's add the test cases. The [**Jasmine introduction**](https://jasmine.github.io/2.1/introduction) may help to understand the structure better, but it looks like this (taken from the intro):

:::BlockQuote
describe("A suite", () => \{
&#x20; it("contains spec with an expectation", () => \{
&#x20;   expect(true).toBe(true);
&#x20; });
});
:::

So describe blocks encapsulate test suites, and the ‘it’ blocks represent cases and expectations.

By passing a parameter to the ‘it’ blocks, you may run tests asynchronously. The test won’t complete until the parameter is invoked like this:

:::BlockQuote
it("will not finish until done is called", (done) => \{
&#x20; setTimeout(() => \{
&#x20;   done();
&#x20; }, 100); // 100 ms
&#x20; expect(x).toBe(y);
})
:::

This is helpful since one of our tests will use HTTP, thus should be run asynchronously in this manner as using HTTP is a non-blocking procedure in NodeJS.

Additionally, Jasmine allows for special blocks within suites that can run at different points in the testing lifecycle. We want to delete all tables before each test, so we will execute the purging code in the beforeEach block.

Enough talking, let's add some code! Place the code below into your spec/signup-user.spec.js, below the imports we already added:

```javascript
1   //spec/signup-user.spec.js
2   // imports above
3   describe("SignupUser", ()=> {
4     beforeEach((done) => {
5       /// purge the user and profile tables, and then proceed
6       Promise.all([purgeTable("User"), purgeTable("Profile")])
7       .catch((e) => fail(e))
8       .then(() => done());
9     });
10    it ("should reject a request to signup that does not contain all the parameters", (done) => {
11      var responseStub = new ResponseStub();
12      responseStub.onComplete()
13      .then(() => fail("Should have failed due to invalid parameters"))
14      .catch((e) => {})
15      .then(() => done());
16
17      signupUser({ params : {}}, responseStub.getStub());
18
19    });
20  });
```

Awesome, our first test is under our belts. In the beforeEach block, we purge the User and Profile tables. Then the first test case is triggered. It verifies that passing invalid parameters to the signupUser function causes the function to send an error.

It uses the response stub to make sure the function ultimately rejected. Because ‘signupUser’ will fail, the initial ‘then’ block on the stub should not be invoked. If it is, then our test fails!

Go ahead and run the test using the following:

:::BlockQuote
$ ./node\_modules/jasmine/bin/jasmine.js spec/signup-user.spec.js
:::

You should see the following output:

:::BlockQuote
Randomized with seed 24618
Started
..


1 specs, 0 failures
Finished in 1.376 seconds
Randomized with seed 24618 (jasmine --random=true --seed=24618)
:::

### **7. A Test On Data Persistence**

Hope you have one more test in you! We are going to verify that when our Cloud Function runs properly, our database will be as expected: a Profile will exist, with a reference to a User object, both with the expected attributes.

Add the following block to our existing ‘describe’ suite block:

```javascript
1   //spec/signup-user.spec.js
2   // inside describe
3   it ("should signup a User, and also create a Profile that contains a reference to the user", (done) => {
4     var responseStub = new ResponseStub();
5     var stub = responseStub.getStub();
6     signupUser({
7         params : {
8           firstname : "John",
9           lastname : "Smith",
10          email : "jsmith@example.com",
11          username : "jsmith1",
12          password : "SecretCatchphrase1"
13        },
14      },
15      stub
16    );
17    responseStub.onComplete()
18    .then((resp) => {
19      var profileQ =  new Parse.Query("Profile");
20      profileQ.equalTo("lastname", "Smith");
21      return profileQ.find({useMasterKey : true});
22    })
23    // Check to make sure the profile we retrieve is valid
24    .then((profiles) => {
25      if (profiles.length === 0) throw new Error("No profile's found");
26      expect(profiles[0].get('firstname')).toBe("John");
27      // get the corresponding user
28      return profiles[0].get("user").fetch({useMasterKey : true})
29    })
30    // Check to make sure the user is what we expect
31    .then((user) => {
32      expect(user.getUsername()).toBe("jsmith1");
33    })
34    .catch((e) => {
35      console.log(e)
36      fail(e);
37    })
38    .then(() => done());
39  });
```

Ok this is a lot, so let's step through what occurs.

We instantiate a response mock object, as in the first test case. Then we run signupUser with a request double containing **valid** parameters, as well as the response mock (lines 6-16).

Next, this code listens for the mock object’s onComplete method, which will return a Promise. The Promise will reject if a response.error was called, and resolve if a response.success was called. Any rejections will cause the chain of Promises to skip to the catch block. Therefore, the fail method is placed in the catch block, as the test should fail if the Promise rejects.

The response of the Promise **should** resolve to the profile object. Once it resolves, we will query for a profile of the same last name as we created (lines 19-21). Then the test confirms that the ‘firstname’ of the profile is the same one that we passed (lines 25-26).

The next block fetches the user object associated with the profile. Parse object pointers fetch separately, hence the need for another Promise block.

Finally, the code confirms that the corresponding user has the username that was passed to the signupUser function. Then the test finishes.

Go ahead and run the suite one more time:
Go ahead and run the test using the following:

:::BlockQuote
$ ./node\_modules/jasmine/bin/jasmine.js spec/signup-user.spec.js
:::

You should see the following output:

:::BlockQuote
Randomized with seed 24618
Started
..


2 specs, 0 failures
Finished in 2.876 seconds
Randomized with seed 24618 (jasmine --random=true --seed=24618)
:::

Awesome! we wrote some cloud code, and integrated a testing framework.

## Conclusion

If you got lost at all, or merely want the code for this example head over to the [**GitHub Repo**](https://github.com/back4app/template-cloud-code-unit-test). Follow the instructions to download and run.

If something is not clear, or doesn’t work, please reach out to me via my Gmail, jackconsidine3.

I hope you enjoyed this tutorial, and gained some insight!
