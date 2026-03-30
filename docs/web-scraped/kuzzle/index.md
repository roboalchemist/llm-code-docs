# Source: https://docs.kuzzle.io

Title: Kuzzle Documentation

URL Source: https://docs.kuzzle.io/

Markdown Content:
Why Choose a Ready-Made Backend? [#](https://docs.kuzzle.io/#why-choose-a-ready-made-backend)
---------------------------------------------------------------------------------------------

If you're here, you're probably planning to build a backend system for your:

*   Mobile application
*   Web platform
*   IoT project

The Traditional Approach [#](https://docs.kuzzle.io/#the-traditional-approach)
------------------------------------------------------------------------------

Your first instinct might be to:

1.   Build everything from scratch
2.   Use a framework to speed things up

While frameworks provide helpful structures and patterns, you'll still need to implement fundamental features like:

*   Database operations and search functionality
*   Permission systems
*   User authentication
*   API endpoints

Building these basic components isn't just about writing code. It involves:

*   Extensive debugging
*   Security hardening
*   Testing
*   Ongoing maintenance

This represents significant time spent on infrastructure rather than value-adding features.

What You Could Focus On Instead [#](https://docs.kuzzle.io/#what-you-could-focus-on-instead)
--------------------------------------------------------------------------------------------

The time saved could be better invested in:

*   Core business features
*   Frontend experience
*   Comprehensive testing
*   DevOps optimization
*   Marketing initiatives

The Solution: Kuzzle [#](https://docs.kuzzle.io/#the-solution-kuzzle)
---------------------------------------------------------------------

This is why Kuzzle was created - a pre-built backend platform that handles all the foundational elements, allowing developers to focus on what truly matters: building distinctive features for their users.

Think of it as skipping the "infrastructure homework" and jumping straight to the unique aspects of your application.

How it works [#](https://docs.kuzzle.io/#how-it-works)
------------------------------------------------------

Kuzzle is a **backend with ready-to-use features** that can be extended in the same way as any other framework.

When you start Kuzzle, you automatically have access to an API exposing a wide range of features:

![Image 1: database illustration](https://docs.kuzzle.io/core/2/assets/feature-data-storage-LiJLrwK9.svg)

![Image 2: Advanced permission system illustration](https://docs.kuzzle.io/core/2/assets/feature-acl-BLqKByOX.svg)

![Image 3: authentification illustration](https://docs.kuzzle.io/core/2/assets/feature-auth-BuOuOv_k.svg)

![Image 4: api illustration](https://docs.kuzzle.io/core/2/assets/feature-api-wKOXZD7c.svg)

![Image 5: realtime engine illustration](https://docs.kuzzle.io/core/2/assets/feature-realtime-1LmdIUa6.svg)

![Image 6: cluster interconnected illustration](https://docs.kuzzle.io/core/2/assets/feature-cluster-DmPGWsv_.svg)

You can also develop your custom business and high level features by [extending Kuzzle API](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/api-controllers) or [modifying API methods behavior](https://docs.kuzzle.io/core/2/guides/develop-on-kuzzle/event-system#pipe).

**Example:** Basic Kuzzle application

```
import { Backend } from 'kuzzle';

// Instantiate a new application
const app = new Backend('playground');

// Declare a "greeting" controller
app.controller.register('greeting', {
  actions: {
    // Declare a "sayHello" action
    sayHello: {
      handler: request => `Hello, ${request.input.args.name}`
    }
  }
});

// Start the application
app.start()
  .then(() => {
    app.log.info('Application started');
  });
```

Complete ecosystem [#](https://docs.kuzzle.io/#complete-ecosystem)
------------------------------------------------------------------

In addition to Kuzzle, we are developing many other projects to facilitate the use of our backend.

These projects are available under the Apache-2 license on [Github](https://github.com/kuzzleio).

### Admin Console [#](https://docs.kuzzle.io/#admin-console)

The [Admin Console](https://next-console.kuzzle.io/) is a Single Page Application (SPA) written in Vue.js.

It is used to manage its data and the user permissions system.

As it is a single-page application (SPA), no data related to your Kuzzle application will pass through our servers, so you can use the online version available at [http://next-console.kuzzle.io](http://next-console.kuzzle.io/).

![Image 7: Screenshot of the admin console interface](https://docs.kuzzle.io/core/2/assets/ecosystem-admin-console-De26wBEM.png)

### SDKs [#](https://docs.kuzzle.io/#sdks)

We provide many SDKs to facilitate the use of Kuzzle in applications.

These SDKs are available for the most common languages and the majority of frontend development platforms:

*   [Javascript / Typescript](https://docs.kuzzle.io/sdk/js/7) : [Node](https://docs.kuzzle.io/sdk/js/7/getting-started/node-js), [React](https://docs.kuzzle.io/sdk/js/7/getting-started/react/standalone), [React Native](https://docs.kuzzle.io/sdk/js/7/getting-started/react-native), [Vue.js](https://docs.kuzzle.io/sdk/js/7/getting-started/vuejs/standalone), Angular, etc
*   [Dart](https://docs.kuzzle.io/sdk/dart/2) : [Flutter](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter)
*   [Csharp](https://docs.kuzzle.io/sdk/csharp/2) : Xamarin, [.NET](https://docs.kuzzle.io/sdk/csharp/2/getting-started/standalone)
*   [Java / Kotlin](https://docs.kuzzle.io/sdk/jvm/1) : Android, JVM

![Image 8: List of sdk (js java, c#, kotln dart, go) and platforms (react / react native, android studio, flutter, xamarin, angular, node, vuejs, microsoft.net)](https://docs.kuzzle.io/core/2/assets/ecosystem-sdk-platforms-D2TBKNcL.png)

### Kourou [#](https://docs.kuzzle.io/#kourou)

Kourou is a command line interface that speeds up development with Kuzzle.

It can be used to execute any API action or even code snippets directly.

[See Kourou on Gitub](https://github.com/kuzzleio/kourou)

### Business plugins [#](https://docs.kuzzle.io/#business-plugins)

We also develop and distribute plugins for Kuzzle.

These plugins allow you to use the functionalities of other services such as [Amazon S3](https://docs.kuzzle.io/official-plugins/s3/2) or [Prometheus](https://github.com/kuzzleio/kuzzle-plugin-prometheus).

The community is also able and encouraged to develop and distribute its own plugins to enrich the ecosystem.

![Image 9: List of business plugins](https://docs.kuzzle.io/core/2/assets/ecosystem-business-plugins-CxjShUp0.png)

### Expert Professional Support [#](https://docs.kuzzle.io/#expert-professional-support)

The Kuzzle backend and all our projects are developed by a team of engineers based in Montpellier, France.

Our multidisciplinary team of experts is capable of addressing any type of issue and assisting projects of all sizes.

You can thus pass the development and production phases with a relaxed spirit, knowing that you can rely on quality professional support.

[Get a quote](https://info.kuzzle.io/contact-us)
