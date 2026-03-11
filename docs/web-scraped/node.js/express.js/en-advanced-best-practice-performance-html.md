# Source: https://expressjs.com/en/advanced/best-practice-performance.html

Title: Performance Best Practices Using Express in Production

URL Source: https://expressjs.com/en/advanced/best-practice-performance.html

Published Time: Tue, 03 Mar 2026 11:18:16 GMT

Markdown Content:
Performance Best Practices Using Express in Production
===============

[](https://expressjs.com/ "Go to homepage")

*   [Getting started](https://expressjs.com/en/starter/installing.html)
    *   [Installing](https://expressjs.com/en/starter/installing.html)
    *   [Hello world](https://expressjs.com/en/starter/hello-world.html)
    *   [Express generator](https://expressjs.com/en/starter/generator.html)
    *   [Basic routing](https://expressjs.com/en/starter/basic-routing.html)
    *   [Static files](https://expressjs.com/en/starter/static-files.html)
    *   [More examples](https://expressjs.com/en/starter/examples.html)
    *   [FAQ](https://expressjs.com/en/starter/faq.html)

*   [Guide](https://expressjs.com/en/guide/routing.html)
    *   [Routing](https://expressjs.com/en/guide/routing.html)
    *   [Writing middleware](https://expressjs.com/en/guide/writing-middleware.html)
    *   [Using middleware](https://expressjs.com/en/guide/using-middleware.html)
    *   [Overriding the Express API](https://expressjs.com/en/guide/overriding-express-api.html)
    *   [Using template engines](https://expressjs.com/en/guide/using-template-engines.html)
    *   [Error handling](https://expressjs.com/en/guide/error-handling.html)
    *   [Debugging](https://expressjs.com/en/guide/debugging.html)
    *   [Express behind proxies](https://expressjs.com/en/guide/behind-proxies.html)
    *   [Moving to Express 4](https://expressjs.com/en/guide/migrating-4.html)
    *   [Moving to Express 5](https://expressjs.com/en/guide/migrating-5.html)
    *   [Database integration](https://expressjs.com/en/guide/database-integration.html)

*   [API reference](https://expressjs.com/en/5x/api.html)
    *   [5.x](https://expressjs.com/en/5x/api.html)
    *   [4.x](https://expressjs.com/en/4x/api.html)
    *   [3.x (deprecated)](https://expressjs.com/en/3x/api.html)
    *   [2.x (deprecated)](https://expressjs.com/2x/)

*   [Advanced topics](https://expressjs.com/en/advanced/developing-template-engines.html)
    *   [Building template engines](https://expressjs.com/en/advanced/developing-template-engines.html)
    *   [Security updates](https://expressjs.com/en/advanced/security-updates.html)
    *   [Security best practices](https://expressjs.com/en/advanced/best-practice-security.html)
    *   [Performance best practices](https://expressjs.com/en/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/en/advanced/healthcheck-graceful-shutdown.html)

*   [Resources](https://expressjs.com/en/resources/community.html)
    *   [Community](https://expressjs.com/en/resources/community.html)
    *   [Glossary](https://expressjs.com/en/resources/glossary.html)
    *   [Middleware](https://expressjs.com/en/resources/middleware.html)
    *   [Utility modules](https://expressjs.com/en/resources/utils.html)
    *   [Contributing to Express](https://expressjs.com/en/resources/contributing.html)
    *   [Release Change Log](https://github.com/expressjs/express/releases)

*   [Support](https://expressjs.com/en/support)
*   [Blog](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Latest post](https://expressjs.com/2026/02/27/security-releases.html)
    *   [All posts](https://expressjs.com/en/blog/posts.html)
    *   [Write a Post](https://expressjs.com/en/blog/write-post.html)

*   [**English**](https://expressjs.com/en/advanced/best-practice-performance.html)
*   [Français](https://expressjs.com/fr/advanced/best-practice-performance.html)
*   [Deutsch](https://expressjs.com/de/advanced/best-practice-performance.html)
*   [Español](https://expressjs.com/es/advanced/best-practice-performance.html)
*   [Italiano](https://expressjs.com/it/advanced/best-practice-performance.html)
*   [日本語](https://expressjs.com/ja/advanced/best-practice-performance.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/advanced/best-practice-performance.html)
*   [繁體中文](https://expressjs.com/zh-tw/advanced/best-practice-performance.html)
*   [한국어](https://expressjs.com/ko/advanced/best-practice-performance.html)
*   [Português](https://expressjs.com/pt-br/advanced/best-practice-performance.html)

Production best practices: performance and reliability
======================================================

This article discusses performance and reliability best practices for Express applications deployed to production.

This topic clearly falls into the “devops” world, spanning both traditional development and operations. Accordingly, the information is divided into two parts:

*   Things to do in your code (the dev part): 
    *   [Use gzip compression](https://expressjs.com/en/advanced/best-practice-performance.html#use-gzip-compression)
    *   [Don’t use synchronous functions](https://expressjs.com/en/advanced/best-practice-performance.html#dont-use-synchronous-functions)
    *   [Do logging correctly](https://expressjs.com/en/advanced/best-practice-performance.html#do-logging-correctly)
    *   [Handle exceptions properly](https://expressjs.com/en/advanced/best-practice-performance.html#handle-exceptions-properly)

*   Things to do in your environment / setup (the ops part): 
    *   [Set NODE_ENV to “production”](https://expressjs.com/en/advanced/best-practice-performance.html#set-node_env-to-production)
    *   [Ensure your app automatically restarts](https://expressjs.com/en/advanced/best-practice-performance.html#ensure-your-app-automatically-restarts)
    *   [Run your app in a cluster](https://expressjs.com/en/advanced/best-practice-performance.html#run-your-app-in-a-cluster)
    *   [Cache request results](https://expressjs.com/en/advanced/best-practice-performance.html#cache-request-results)
    *   [Use a load balancer](https://expressjs.com/en/advanced/best-practice-performance.html#use-a-load-balancer)
    *   [Use a reverse proxy](https://expressjs.com/en/advanced/best-practice-performance.html#use-a-reverse-proxy)

Things to do in your code
-------------------------

Here are some things you can do in your code to improve your application’s performance:

*   [Use gzip compression](https://expressjs.com/en/advanced/best-practice-performance.html#use-gzip-compression)
*   [Don’t use synchronous functions](https://expressjs.com/en/advanced/best-practice-performance.html#dont-use-synchronous-functions)
*   [Do logging correctly](https://expressjs.com/en/advanced/best-practice-performance.html#do-logging-correctly)
*   [Handle exceptions properly](https://expressjs.com/en/advanced/best-practice-performance.html#handle-exceptions-properly)

### Use gzip compression

Gzip compressing can greatly decrease the size of the response body and hence increase the speed of a web app. Use the [compression](https://www.npmjs.com/package/compression) middleware for gzip compression in your Express app. For example:

```
const compression = require('compression')
const express = require('express')
const app = express()

app.use(compression())
```

For a high-traffic website in production, the best way to put compression in place is to implement it at a reverse proxy level (see [Use a reverse proxy](https://expressjs.com/en/advanced/best-practice-performance.html#use-a-reverse-proxy)). In that case, you do not need to use compression middleware. For details on enabling gzip compression in Nginx, see [Module ngx_http_gzip_module](http://nginx.org/en/docs/http/ngx_http_gzip_module.html) in the Nginx documentation.

### Don’t use synchronous functions

Synchronous functions and methods tie up the executing process until they return. A single call to a synchronous function might return in a few microseconds or milliseconds, however in high-traffic websites, these calls add up and reduce the performance of the app. Avoid their use in production.

Although Node and many modules provide synchronous and asynchronous versions of their functions, always use the asynchronous version in production. The only time when a synchronous function can be justified is upon initial startup.

You can use the 
```plaintext
--trace-sync-io
```
 command-line flag to print a warning and a stack trace whenever your application uses a synchronous API. Of course, you wouldn’t want to use this in production, but rather to ensure that your code is ready for production. See the [node command-line options documentation](https://nodejs.org/api/cli.html#cli_trace_sync_io) for more information.

### Do logging correctly

In general, there are two reasons for logging from your app: For debugging and for logging app activity (essentially, everything else). Using 
```plaintext
console.log()
```
 or 
```plaintext
console.error()
```
 to print log messages to the terminal is common practice in development. But [these functions are synchronous](https://nodejs.org/api/console.html#console) when the destination is a terminal or a file, so they are not suitable for production, unless you pipe the output to another program.

#### For debugging

If you’re logging for purposes of debugging, then instead of using 
```plaintext
console.log()
```
, use a special debugging module like [debug](https://www.npmjs.com/package/debug). This module enables you to use the DEBUG environment variable to control what debug messages are sent to 
```plaintext
console.error()
```
, if any. To keep your app purely asynchronous, you’d still want to pipe 
```plaintext
console.error()
```
 to another program. But then, you’re not really going to debug in production, are you?

#### For app activity

If you’re logging app activity (for example, tracking traffic or API calls), instead of using 
```plaintext
console.log()
```
, use a logging library like [Pino](https://www.npmjs.com/package/pino), which is the fastest and most efficient option available.

### Handle exceptions properly

Node apps crash when they encounter an uncaught exception. Not handling exceptions and taking appropriate actions will make your Express app crash and go offline. If you follow the advice in [Ensure your app automatically restarts](https://expressjs.com/en/advanced/best-practice-performance.html#ensure-your-app-automatically-restarts) below, then your app will recover from a crash. Fortunately, Express apps typically have a short startup time. Nevertheless, you want to avoid crashing in the first place, and to do that, you need to handle exceptions properly.

To ensure you handle all exceptions, use the following techniques:

*   [Use try-catch](https://expressjs.com/en/advanced/best-practice-performance.html#use-try-catch)
*   [Use promises](https://expressjs.com/en/advanced/best-practice-performance.html#use-promises)

Before diving into these topics, you should have a basic understanding of Node/Express error handling: using error-first callbacks, and propagating errors in middleware. Node uses an “error-first callback” convention for returning errors from asynchronous functions, where the first parameter to the callback function is the error object, followed by result data in succeeding parameters. To indicate no error, pass null as the first parameter. The callback function must correspondingly follow the error-first callback convention to meaningfully handle the error. And in Express, the best practice is to use the next() function to propagate errors through the middleware chain.

For more on the fundamentals of error handling, see:

*   [Error Handling in Node.js](https://www.tritondatacenter.com/node-js/production/design/errors)

#### Use try-catch

Try-catch is a JavaScript language construct that you can use to catch exceptions in synchronous code. Use try-catch, for example, to handle JSON parsing errors as shown below.

Here is an example of using try-catch to handle a potential process-crashing exception. This middleware function accepts a query field parameter named “params” that is a JSON object.

```
app.get('/search', (req, res) => {
  // Simulating async operation
  setImmediate(() => {
    const jsonStr = req.query.params
    try {
      const jsonObj = JSON.parse(jsonStr)
      res.send('Success')
    } catch (e) {
      res.status(400).send('Invalid JSON string')
    }
  })
})
```

However, try-catch works only for synchronous code. Because the Node platform is primarily asynchronous (particularly in a production environment), try-catch won’t catch a lot of exceptions.

#### Use promises

When an error is thrown in an 
```plaintext
async
```
 function or a rejected promise is awaited inside an 
```plaintext
async
```
 function, those errors will be passed to the error handler as if calling 
```plaintext
next(err)
```

```
app.get('/', async (req, res, next) => {
  const data = await userData() // If this promise fails, it will automatically call `next(err)` to handle the error.

  res.send(data)
})

app.use((err, req, res, next) => {
  res.status(err.status ?? 500).send({ error: err.message })
})
```

Also, you can use asynchronous functions for your middleware, and the router will handle errors if the promise fails, for example:

```
app.use(async (req, res, next) => {
  req.locals.user = await getUser(req)

  next() // This will be called if the promise does not throw an error.
})
```

Best practice is to handle errors as close to the site as possible. So while this is now handled in the router, it’s best to catch the error in the middleware and handle it without relying on separate error-handling middleware.

#### What not to do

One thing you should _not_ do is to listen for the 
```plaintext
uncaughtException
```
 event, emitted when an exception bubbles all the way back to the event loop. Adding an event listener for 
```plaintext
uncaughtException
```
 will change the default behavior of the process that is encountering an exception; the process will continue to run despite the exception. This might sound like a good way of preventing your app from crashing, but continuing to run the app after an uncaught exception is a dangerous practice and is not recommended, because the state of the process becomes unreliable and unpredictable.

Additionally, using 
```plaintext
uncaughtException
```
 is officially recognized as [crude](https://nodejs.org/api/process.html#process_event_uncaughtexception). So listening for 
```plaintext
uncaughtException
```
 is just a bad idea. This is why we recommend things like multiple processes and supervisors: crashing and restarting is often the most reliable way to recover from an error.

We also don’t recommend using [domains](https://nodejs.org/api/domain.html). It generally doesn’t solve the problem and is a deprecated module.

Things to do in your environment / setup
----------------------------------------

Here are some things you can do in your system environment to improve your app’s performance:

*   [Set NODE_ENV to “production”](https://expressjs.com/en/advanced/best-practice-performance.html#set-node_env-to-production)
*   [Ensure your app automatically restarts](https://expressjs.com/en/advanced/best-practice-performance.html#ensure-your-app-automatically-restarts)
*   [Run your app in a cluster](https://expressjs.com/en/advanced/best-practice-performance.html#run-your-app-in-a-cluster)
*   [Cache request results](https://expressjs.com/en/advanced/best-practice-performance.html#cache-request-results)
*   [Use a load balancer](https://expressjs.com/en/advanced/best-practice-performance.html#use-a-load-balancer)
*   [Use a reverse proxy](https://expressjs.com/en/advanced/best-practice-performance.html#use-a-reverse-proxy)

### Set NODE_ENV to “production”

The NODE_ENV environment variable specifies the environment in which an application is running (usually, development or production). One of the simplest things you can do to improve performance is to set NODE_ENV to 
```plaintext
production
```
.

Setting NODE_ENV to “production” makes Express:

*   Cache view templates.
*   Cache CSS files generated from CSS extensions.
*   Generate less verbose error messages.

[Tests indicate](https://www.dynatrace.com/news/blog/the-drastic-effects-of-omitting-node-env-in-your-express-js-applications/) that just doing this can improve app performance by a factor of three!

If you need to write environment-specific code, you can check the value of NODE_ENV with 
```plaintext
process.env.NODE_ENV
```
. Be aware that checking the value of any environment variable incurs a performance penalty, and so should be done sparingly.

In development, you typically set environment variables in your interactive shell, for example by using 
```plaintext
export
```
 or your 
```plaintext
.bash_profile
```
 file. But in general, you shouldn’t do that on a production server; instead, use your OS’s init system (systemd). The next section provides more details about using your init system in general, but setting 
```plaintext
NODE_ENV
```
 is so important for performance (and easy to do), that it’s highlighted here.

With systemd, use the 
```plaintext
Environment
```
 directive in your unit file. For example:

```
# /etc/systemd/system/myservice.service
Environment=NODE_ENV=production
```

For more information, see [Using Environment Variables In systemd Units](https://www.flatcar.org/docs/latest/setup/systemd/environment-variables/).

### Ensure your app automatically restarts

In production, you don’t want your application to be offline, ever. This means you need to make sure it restarts both if the app crashes and if the server itself crashes. Although you hope that neither of those events occurs, realistically you must account for both eventualities by:

*   Using a process manager to restart the app (and Node) when it crashes.
*   Using the init system provided by your OS to restart the process manager when the OS crashes. It’s also possible to use the init system without a process manager.

Node applications crash if they encounter an uncaught exception. The foremost thing you need to do is to ensure your app is well-tested and handles all exceptions (see [handle exceptions properly](https://expressjs.com/en/advanced/best-practice-performance.html#handle-exceptions-properly) for details). But as a fail-safe, put a mechanism in place to ensure that if and when your app crashes, it will automatically restart.

#### Use a process manager

In development, you started your app simply from the command line with 
```plaintext
node server.js
```
 or something similar. But doing this in production is a recipe for disaster. If the app crashes, it will be offline until you restart it. To ensure your app restarts if it crashes, use a process manager. A process manager is a “container” for applications that facilitates deployment, provides high availability, and enables you to manage the application at runtime.

In addition to restarting your app when it crashes, a process manager can enable you to:

*   Gain insights into runtime performance and resource consumption.
*   Modify settings dynamically to improve performance.
*   Control clustering (pm2).

Historically, it was popular to use a Node.js process manager like [PM2](https://github.com/Unitech/pm2). See their documentation if you wish to do this. However, we recommend using your init system for process management.

#### Use an init system

The next layer of reliability is to ensure that your app restarts when the server restarts. Systems can still go down for a variety of reasons. To ensure that your app restarts if the server crashes, use the init system built into your OS. The main init system in use today is [systemd](https://wiki.debian.org/systemd).

There are two ways to use init systems with your Express app:

*   Run your app in a process manager, and install the process manager as a service with the init system. The process manager will restart your app when the app crashes, and the init system will restart the process manager when the OS restarts. This is the recommended approach.
*   Run your app (and Node) directly with the init system. This is somewhat simpler, but you don’t get the additional advantages of using a process manager.

##### Systemd

Systemd is a Linux system and service manager. Most major Linux distributions have adopted systemd as their default init system.

A systemd service configuration file is called a _unit file_, with a filename ending in 
```plaintext
.service
```
. Here’s an example unit file to manage a Node app directly. Replace the values enclosed in 
```plaintext
<angle brackets>
```
 for your system and app:

```
[Unit]
Description=<Awesome Express App>

[Service]
Type=simple
ExecStart=/usr/local/bin/node </projects/myapp/index.js>
WorkingDirectory=</projects/myapp>

User=nobody
Group=nogroup

# Environment variables:
Environment=NODE_ENV=production

# Allow many incoming connections
LimitNOFILE=infinity

# Allow core dumps for debugging
LimitCORE=infinity

StandardInput=null
StandardOutput=syslog
StandardError=syslog
Restart=always

[Install]
WantedBy=multi-user.target
```

For more information on systemd, see the [systemd reference (man page)](http://www.freedesktop.org/software/systemd/man/systemd.unit.html).

### Run your app in a cluster

In a multi-core system, you can increase the performance of a Node app by many times by launching a cluster of processes. A cluster runs multiple instances of the app, ideally one instance on each CPU core, thereby distributing the load and tasks among the instances.

![Image 1: Balancing between application instances using the cluster API](https://expressjs.com/images/clustering.png)

IMPORTANT: Since the app instances run as separate processes, they do not share the same memory space. That is, objects are local to each instance of the app. Therefore, you cannot maintain state in the application code. However, you can use an in-memory datastore like [Redis](http://redis.io/) to store session-related data and state. This caveat applies to essentially all forms of horizontal scaling, whether clustering with multiple processes or multiple physical servers.

In clustered apps, worker processes can crash individually without affecting the rest of the processes. Apart from performance advantages, failure isolation is another reason to run a cluster of app processes. Whenever a worker process crashes, always make sure to log the event and spawn a new process using cluster.fork().

#### Using Node’s cluster module

Clustering is made possible with Node’s [cluster module](https://nodejs.org/api/cluster.html). This enables a master process to spawn worker processes and distribute incoming connections among the workers.

#### Using PM2

If you deploy your application with PM2, then you can take advantage of clustering _without_ modifying your application code. You should ensure your [application is stateless](https://pm2.keymetrics.io/docs/usage/specifics/#stateless-apps) first, meaning no local data is stored in the process (such as sessions, websocket connections and the like).

When running an application with PM2, you can enable **cluster mode** to run it in a cluster with a number of instances of your choosing, such as the matching the number of available CPUs on the machine. You can manually change the number of processes in the cluster using the 
```plaintext
pm2
```
 command line tool without stopping the app.

To enable cluster mode, start your application like so:

```
# Start 4 worker processes
$ pm2 start npm --name my-app -i 4 -- start
# Auto-detect number of available CPUs and start that many worker processes
$ pm2 start npm --name my-app -i max -- start
```

This can also be configured within a PM2 process file (
```plaintext
ecosystem.config.js
```
 or similar) by setting 
```plaintext
exec_mode
```
 to 
```plaintext
cluster
```
 and 
```plaintext
instances
```
 to the number of workers to start.

Once running, the application can be scaled like so:

```
# Add 3 more workers
$ pm2 scale my-app +3
# Scale to a specific number of workers
$ pm2 scale my-app 2
```

For more information on clustering with PM2, see [Cluster Mode](https://pm2.keymetrics.io/docs/usage/cluster-mode/) in the PM2 documentation.

### Cache request results

Another strategy to improve the performance in production is to cache the result of requests, so that your app does not repeat the operation to serve the same request repeatedly.

Use a caching server like [Varnish](https://www.varnish-cache.org/) or [Nginx](https://blog.nginx.org/blog/nginx-caching-guide) (see also [Nginx Caching](https://serversforhackers.com/nginx-caching/)) to greatly improve the speed and performance of your app.

### Use a load balancer

No matter how optimized an app is, a single instance can handle only a limited amount of load and traffic. One way to scale an app is to run multiple instances of it and distribute the traffic via a load balancer. Setting up a load balancer can improve your app’s performance and speed, and enable it to scale more than is possible with a single instance.

A load balancer is usually a reverse proxy that orchestrates traffic to and from multiple application instances and servers. You can easily set up a load balancer for your app by using [Nginx](https://nginx.org/en/docs/http/load_balancing.html) or [HAProxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts).

With load balancing, you might have to ensure that requests that are associated with a particular session ID connect to the process that originated them. This is known as _session affinity_, or _sticky sessions_, and may be addressed by the suggestion above to use a data store such as Redis for session data (depending on your application). For a discussion, see [Using multiple nodes](https://socket.io/docs/v4/using-multiple-nodes/).

### Use a reverse proxy

A reverse proxy sits in front of a web app and performs supporting operations on the requests, apart from directing requests to the app. It can handle error pages, compression, caching, serving files, and load balancing among other things.

Handing over tasks that do not require knowledge of application state to a reverse proxy frees up Express to perform specialized application tasks. For this reason, it is recommended to run Express behind a reverse proxy like [Nginx](https://www.nginx.org/) or [HAProxy](https://www.haproxy.org/) in production.

[Previous: Security Best Practices for Express in Production](https://expressjs.com/en/advanced/best-practice-security.html)[Next: Health Checks and Graceful Shutdown](https://expressjs.com/en/advanced/healthcheck-graceful-shutdown.html)[Edit this page](https://github.com/expressjs/expressjs.com/edit/gh-pages/en/advanced/best-practice-performance.md)

[](https://expressjs.com/en/advanced/best-practice-performance.html#)

[](https://openjsf.org/ "OpenJS Foundation")
Copyright [OpenJS Foundation](https://openjsf.org/) and Express contributors. All rights reserved. The [OpenJS Foundation](https://openjsf.org/) has registered trademarks and uses trademarks. For a list of trademarks of the [OpenJS Foundation](https://openjsf.org/), please see our [Trademark Policy](https://trademark-policy.openjsf.org/) and [Trademark List](https://trademark-list.openjsf.org/). Trademarks and logos not indicated on the [list of OpenJS Foundation trademarks](https://trademark-list.openjsf.org/) are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.

[Terms of Use](https://terms-of-use.openjsf.org/)[Privacy Policy](https://privacy-policy.openjsf.org/)[Code of Conduct](https://github.com/expressjs/.github/blob/HEAD/CODE_OF_CONDUCT.md)[Trademark Policy](https://trademark-policy.openjsf.org/)[Security Policy](https://github.com/expressjs/express/security/policy)

[](https://github.com/expressjs/express)

[](https://www.youtube.com/channel/UCYjxjAeH6TRik9Iwy5nXw7g)

[](https://x.com/UseExpressJS)

[](https://openjs-foundation.slack.com/archives/C02QB1731FH)

[](https://opencollective.com/express)

[](https://bsky.app/profile/expressjs.bsky.social)

[![Image 2: Preview Deploys by Netlify](https://www.netlify.com/v3/img/components/netlify-color-accent.svg)](https://www.netlify.com/)
