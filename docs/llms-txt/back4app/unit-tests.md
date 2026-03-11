# Source: https://docs-containers.back4app.com/docs/cloud-code-functions/unit-tests.md

---
title: Cloud Code Unit Tests
slug: docs/cloud-code-functions/unit-tests
description: Learn how to create a unit test from your cloud code functions through Back4App.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-28T13:56:55.364Z
updatedAt: 2025-01-17T01:08:31.659Z
---

# How to Create a Unit Test through their Cloud Code Functions

## Introduction

This section will allow you to check the operation and testing of your functions locally using the library [**parse-server-test-runner**](https://github.com/AmpMe/parse-server-test-runner).

## Prerequisites

:::hint{type="info"}
- To complete this tutorial, you will need:

- A local environment with Node.js installed to apply unit tests. You can follow the [**Official NodeJS tutorial**](https://nodejs.org/en/download/package-manager/) to successfully install Node.js at your terminal.
- An app created at Back4App.
- Follow the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Back4App Command Line Configured with the project.
- Follow the [**Setting up Cloud Code tutorial**](https://www.back4app.com/docs/local-development/parse-cli) to learn how to set up cloud code for a project.
:::

## First off, we need to talk about Unit Test!

When developers start writing a function with different intentions in mind, a major point evident in the software community is the application of imaginary scenarios for the created code to be tested. It is necessary to perform the Unit Tests procedure as it allows you to test the code in parts, which ensures that your main code remains intact and uncompromised.

### **And now, how about a simple practical example?**

Let’s assume that you need to write a function to show in a complete sentence, the name from the worker, the position and company. We’ll need to write the function to get the following input items:

- Company
- Position
- Worker name

## Steps to complete the simple test

In your terminal, initially, we’ll create a directory and configure your test App (package.json) first, using the following command:

:::BlockQuote
$ mkdir unit-test-sample && cd unit-test-sample
$ npm init
:::

:::hint{type="warning"}
Hint:
Using the npm init command, you’ll be able to create the package.json file. It only covers the most common items and tries to guess sensible defaults. Because of this, we’ll make available the dependencies necessary for the code to work.
:::

The result from “package.json” will be something like the example below:

```json
{
  "name": "yourfoldername",
  "version": "1.0.0",
  "description": "Just a unit test with using a simple function.",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": ""
  },
  "author": "Your Name",
  "license": "ISC",
  "bugs": {
    "url": "{url}/issues"
  },
  "homepage": ""
}
```

Now, let’s create the file (index.js) using the command below:

:::BlockQuote
\~/unit-test-sample$ touch index.js
:::

We will now insert the code below into the previously created file, and the function will insert an example that can demonstrate this test with the code:

```javascript
1   // index.js
2     module.exports = function(name, position, company) {
3     let sentence = "Hi, " + name + "! You are " + position + " in " + company + " company.";
4       return sentence;
5     };
```

:::hint{type="info"}
**In NodeJS, the module encapsulates the related code into a single unit of code, and when you’re using&#x20;*****module.exports*****, it increases encapsulated code that can be utilized in other files.**
:::

### **Let’s test 0/**

Finally, you can work with your terminal:

:::BlockQuote
\~/unit-test-sample$ node
\> var moduleBack4App = require('./index.js');
undefined
\> moduleBack4App("Jonathan", "Developer", "Back4App")
Hi, Jonathan! You are Developer in Back4App company.
:::

:::hint{type="warning"}
Hint:
&#x20;Using the require() function, you’re able to import and export modules, and in the case above, we are using this function to require a file inside an application.
:::

# And using Parse, can I test my function?

Of course, as a test parameter, we will create a backend to control the information of a company’s employees.

# Let’s structure the classes as:

### Parse.User (Reference for employees)

- username, email, password (required)

We recommend you to have a detailed look at the [**Parse Server**](http://docs.parseplatform.org/js/guide/#users) guide in order to get some more information about User properties.

### infoEmployee

- Position
- Department
- WorkShift
- userId (Pointer)

## 1 - Understand our final structure

Let’s get started! We will use the [**Parse Server Javascript Guide**](https://www.back4app.com/docs/cloud-code-functions/docs.parseplatform.org/js/guide/) as a parameter for the development of our functions. Firstly, after completing the setup using the Command Line Interface [**(see prereqs**](https://www.back4app.com/docs/cloud-code-functions/unit-tests#content-prerequisites)), we’ll understand how it will work with the final structure from the files:

:::BlockQuote
├──Back4AppProject
│  ├── cloud
│  │   ├── functions.js
│  │   ├── main.js
│  ├── public
│  ├── package.json
│  ├── index.js
│  ├── node\_modules
│  ├── src
│  │   ├── jasmine.js
:::

:::hint{type="info"}
**Notice:&#x20;**&#x57;hen you upload the files to your Cloud Code, the Command Line Interface (See [**prereqs**](https://www.back4app.com/docs/cloud-code-functions/unit-tests#content-prerequisites)) will ignore the other files and upload only the ones that are in the public and cloud folder.
:::

## 2 - Writing our function

After configuring the environment for the Command Line Interface, we’ll write the function to build the process to register the Employee and save the additional information. By refactoring the code, at the main.js file, we’ll import these functions into main, like:

```javascript
1   //In 1cloud/main.js
2
3   var cloudFunctions = require("./functions");
4
5   /* It's necessary to insert the Parse Instance in our code,
6   because at local context not is referenced.*/
7
8   Parse.Cloud.define("registerUser",  cloudFunctions.registerUser(Parse));
9
10  Parse.Cloud.beforeSave("infoEmployee", infoEmployee.infoEmployee(Parse));
```

The idea is to decouple the functions from the cloud interface so we may test them without sending HTTP requests inefficiently. This will make a lot of sense as we create the test suite.

:::CodeblockTabs
Parse Server 3.X

```javascript
1   //In cloud/functions.js
2
3   module.exports.registerUser = function(Parse){
4     return async(request) =>{
5       let params = request.params; //Parameters received  
6       let infoEmployee = Parse.Object.extend("infoEmployee"); //Store Information      
7
8       let userCreated = new Parse.User({
9         "email" : params.email,
10        "username": params.username,
11        "password" : params.password
12      })
13
14      //Save relation
15      try {
16        let result = await userCreated.save();
17
18        let information = new infoEmployee({
19          "position"   : params.position,
20          "department" : params.department,
21          "workShift"  : params.shift,
22          "user" : result
23        });
24
25        return information.save();
26      } catch (e) {
27          return e.message;
28      }
29    }
30  }
31
32  module.exports.infoEmployee = function(Parse){
33    return async (request) =>{
34      let req = request.object;
35
36      if (!req.get("position") || !req.get("department") || !req.get("workShift")) {
37        throw new Error("Missing params! The required parameters are: position, department. workShift");
38      } else {
39        return;
40      }
41    }
42  }
```

Parse Server 2.X

```javascript
1   //In cloud/functions.js
2
3   module.exports.registerUser = function(Parse){
4     return function (request, response){
5       var params = request.params; //Parameters received
6
7       var infoEmployee = Parse.Object.extend("infoEmployee"); //Store Information      
8
9       var userCreated = new Parse.User({
10        "email" : params.email,
11        "username": params.username,
12        "password" : params.password
13      })
14
15      //Save relation
16      userCreated.save().then((updatedUser) => {
17        var information = new infoEmployee({
18          "position"   : params.position,
19          "department" : params.department,
20          "workShift"  : params.shift,
21          "user" : updatedUser
22        });
23        return information.save();
24      }).then((info) => response.success(info))
25        .catch((e) => {
26          response.error(e.message);
27        })
28    }
29  }
30
31  module.exports.infoEmployee = function(Parse){
32    return function (request, response){
33      var req = request.object;
34
35      if (!req.get("position") || !req.get("department") || !req.get("workShift")) {
36        response.error("Missing params! The required parameters are: position, department. workShift");
37      } else {
38        response.success();
39      }
40    }
41  }
```
:::

## &#x20;3 - Setting up the environment to test the above code!

For our test suite, we will be using [**Jasmine**](https://jasmine.github.io/), a highly popular JavaScript testing framework. However, our code so far is completely agnostic of our tests, so you may use whatever framework or platform you prefer.

### **Install the development dependencies**

Let’s install Jasmine globally and use, with the commands below:

:::BlockQuote
\~/Back4AppProject$ sudo npm install -g jasmine
\~/Back4AppProject$ jasmine
Randomized with seed 48094
Started


No specs found
Finished in 0.002 seconds
Incomplete: No specs found
:::

## 4 - Configuring Parse Server Test Runner in the folder

With our methods implemented in the project Cloud folder in Back4App, we will create new files on our project on Node.js that will configure this interaction.

:::BlockQuote
\~/Back4AppProjectsrc$ touch index.js
\~/Back4AppProject$ mkdir src && cd src
\~/Back4AppProject/src$ touch jasmine.js
:::

Now, we will configure the files created above with the codes shown below:

:::CodeblockTabs
index.js

```javascript
1   const Promise = require('bluebird');
2     const express = require('express');
3     const http = require('http');
4     const {MongoClient} = require('mongodb');
5     const {ParseServer} = require('parse-server');
6
7     const mongoDBRunnerStart = require('mongodb-runner/mocha/before').bind({
8      timeout() {
9       },
10      slow() {
11      },
12    });
13    const mongoDBRunnerStop = require('mongodb-runner/mocha/after');
14
15    const startDB = () => (
16      new Promise((done, reject) => {
17        done.fail = reject;
18        mongoDBRunnerStart(done);
19      })
20    );
21
22    const stopDB = () => (
23      new Promise((done, reject) => {
24        done.fail = reject;
25        mongoDBRunnerStop(done);
26      })
27    );
28
29    const connectDB = (databaseURI) => new Promise((resolve, reject) => {
30      MongoClient.connect(databaseURI, (err, db) => {
31        if (err) {
32          reject(err);
33        } else {
34          resolve(db);
35        }
36      });
37    });
38
39    let parseServerState = {};
40
41    const dropDB = () => {
42      const {mongoConnection} = parseServerState;
43      return mongoConnection.dropDatabaseAsync();
44    };
45
46    /**
47      * Starts the ParseServer idropDatabaseAsyncnstance
48      * @param {Object} parseServerOptions Used for creating the `ParseServer`
49      * @return {Promise} Runner state
50     */
51    function startParseServer(parseServerOptions = {}) {
52      const mongodbPort = process.env.MONGODB_PORT || 27017;
53      const {
54        databaseName = 'parse-test',
55        databaseURI = 'mongodb://localhost:${mongodbPort}/${databaseName}',
56        masterKey = 'test',
57        javascriptKey = 'test',
58        appId = 'test',
59
60        port = 30001,
61        mountPath = '/1',
62        serverURL = 'http://localhost:${port}${mountPath}',
63      } = parseServerOptions;
64
65      return startDB()
66        .then(() => connectDB(databaseURI))
67        .then((mongoConnection) => {
68         parseServerOptions = Object.assign({
69            masterKey, javascriptKey, appId,
70            serverURL,
71            databaseURI,
72            silent: process.env.VERBOSE !== '1',
73          }, parseServerOptions);
74          const app = express();
75          const parseServer = new ParseServer(parseServerOptions);
76
77          app.use(mountPath, parseServer);
78
79          const httpServer = http.createServer(app);
80
81          Promise.promisifyAll(httpServer);
82          Promise.promisifyAll(mongoConnection);
83
84          return httpServer.listenAsync(port)
85            .then(() => Object.assign(parseServerState, {
86              parseServer,
87              httpServer,
88              mongoConnection,
89              expressApp: app,
90              parseServerOptions,
91            }));
92        });
93    }
94
95  /**
96   * Stops the ParseServer instance
97   * @return {Promise}
98   */
99    function stopParseServer() {
100     const {httpServer} = parseServerState;
101     return httpServer.closeAsync()
102       .then(stopDB)
103       .then(() => parseServerState = {});
104   }
105 
106   module.exports = {
107     dropDB,
108     startParseServer,
109     stopParseServer,
110     parseServerState,
111   };
```

jasmine.js

```javascript
1   const { startParseServer, stopParseServer, dropDB } = require('parse-server-test-runner');
2
3   describe('registerUser', () => {
4      beforeAll((done) => {
5       const appId = 'test';
6       const masterKey = 'test';
7       const javascriptKey = 'test';
8
9       startParseServer({ appId, masterKey, javascriptKey })
10        .then(() => {
11          Parse.initialize(appId, masterKey, javascriptKey);
12          Parse.serverURL = 'http://localhost:30001/1';
13        })
14        .then(done).catch(done.fail);
15    }, 300 * 60 * 2);
16
17    afterAll((done) => {
18      stopParseServer()
19        .then(done).catch(done.fail);
20    });
21
22    beforeEach((done) => {
23      dropDB()
24        .then(done).catch(done.fail);
25    });
26
27    it('should work', (done) => {
28      const q = new Parse.Query('_User')
29      q.limit(5)
30        .find({ useMasterKey: true })
31        .then(console.log)
32        .then(done).catch(done.fail);
33    });
34  });
```
:::

The last step is to configure the package.json, using the command: $ npm init in the root directory (the file below is just an example with the modules required):

```json
1   {
2     "name": "back4approject",
3     "version": "1.0.0",
4     "description": "Back4App guide using for reference the Parse Server Test Runner",
5     "main": "index.js",
6     "engines": {
7       "node": ">=6"
8     },
9     "repository": {
10      "type": "",
11      "url": ""
12    },
13    "keywords": [
14      "parse",
15      "parse-server",
16      "testing",
17      "tests"
18    ],
19    "author": "",
20    "license": "ISC",
21    "dependencies": {
22      "bluebird": "^3.5.0",
23      "express": "latest",
24      "mongodb": "^2.2.30",
25      "mongodb-runner": "^3.5.0",
26      "parse": "^1.10.0",
27      "parse-server": "^2.5.3",
28      "parse-server-test-runner": "^1.0.0"
29    }
30  }
```

And now, you’ll check that we approach the structure described in [**these previous**](https://www.back4app.com/docs/cloud-code-functions/unit-tests#content-structure) steps :)

## 5 - Returning to the terminal

We’ll start to configure the local testing, for this we’ll follow the command below to the code for set up programmatically for testing purposes.

:::BlockQuote
\~/Back4AppProject$ # in the same directory from package.json
\~/Back4AppProject$ npm install
:::

After the successful installation, you’re able to check your unit test locally with the command described and receive the result, such as:

:::BlockQuote
\~/Back4AppProject$ jasmine src/jasmine.js
Randomized with seed 79055
Started
✔  Downloaded MongoDB 3.6.5
\[]
.


1 spec, 0 failures
Finished in 19.983 seconds
Randomized with seed 79055 (jasmine --random=true --seed=79055)
:::




## Wonderful, it’s ready!

With the guide described above, you’re able to work with the Parse Server Test Runner and your functions developed for the Cloud Code to Back4App.
