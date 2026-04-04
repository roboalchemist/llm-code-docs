# Source: https://wafris.org/docs/installation/nodejs/

Title: NodeJS

URL Source: https://wafris.org/docs/installation/nodejs/

Markdown Content:
[](https://wafris.org/docs/installation/nodejs/#wafris-for-node-express) Wafris for Node Express
------------------------------------------------------------------------------------------------

[](https://wafris.org/docs/installation/nodejs/#installation-and-configuration) Installation and Configuration
--------------------------------------------------------------------------------------------------------------

The Wafris Node package creates a middleware function that communicates with a Redis instance that you can insert into your Express application’s middleware stack.

### [](https://wafris.org/docs/installation/nodejs/#requirements) Requirements

* [redis](https://www.npmjs.com/package/redis)
* Express

[](https://wafris.org/docs/installation/nodejs/#setup) Setup
------------------------------------------------------------

### [](https://wafris.org/docs/installation/nodejs/#1-connect-on-wafris-hub) 1. Connect on Wafris Hub

Go to https://wafris.org/hub to create a new account and follow the instructions to link your Redis instance.

**Note:** In Step 3, you’ll use this same Redis URL in your app configuration.

### [](https://wafris.org/docs/installation/nodejs/#2-add-the-middleware-to-your-application) 2. Add the middleware to your application

Use your preferred package manager to add `node-wafris`. For instance, using `npm`

```
npm install https://github.com/Wafris/node-wafris.git
```

### [](https://wafris.org/docs/installation/nodejs/#3-initialize-the-middleware) 3. Initialize the middleware

Using the `node-wafris` middleware is fairly straightforward. Simply invoke the library’s exported function with a configuration and `use` the returned middleware function in your Express application:

**Note:** We recommend storing the Redis URL as an environment variable or in a secret management system of your choosing rather than hard coding the string in the initializer.

```
import express from "express";
import wafrisMiddleware from "wafris";

const app = express();
const redisUrl = process.env.REDIS_URL || "redis://localhost:6379";

const wafrisConfig = { redisUrl };
const wafris = await wafrisMiddleware(wafrisConfig);

app.use("/", wafris);
```

* * *
