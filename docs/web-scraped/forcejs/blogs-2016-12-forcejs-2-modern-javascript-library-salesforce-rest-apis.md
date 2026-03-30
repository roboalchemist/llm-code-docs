# Source: https://developer.salesforce.com/blogs/2016/12/forcejs-2-modern-javascript-library-salesforce-rest-apis

Title: ForceJS 2: Modern JavaScript Library for the Salesforce REST APIs

URL Source: https://developer.salesforce.com/blogs/2016/12/forcejs-2-modern-javascript-library-salesforce-rest-apis

Published Time: 2016-12-07T18:31:27.000Z

Markdown Content:
[ForceJS](https://github.com/ccoenraets/forcejs) is an open source library that makes it easy to work with the Salesforce REST APIs in JavaScript applications. ForceJS can be used to develop browser-based apps, hybrid mobile apps using the Salesforce Mobile SDK and Apache Cordova, and to authenticate with Salesforce when using Lightning Out.

The JavaScript world has changed a lot in the last couple of years since the first version of ForceJS. Modern JavaScript applications are now built with ECMAScript 6 (aka ECMAScript 2015) and beyond. The current version of modern frameworks (such as React, Angular 2, and Ionic 2) are built on top of ECMAScript Next as well.

To address the new requirements of modern JavaScript Applications, I’m excited to announce ForceJS 2, a brand new version of the library with the following characteristics:

*   Built on ECMAScript 6 and compatible with ECMAScript 5
*   Seamless integration with modern JavaScript frameworks: React, Angular 2, Ionic 2, etc.
*   Asynchronous calls return ECMAScript 6 promises
*   Support for modern developer workflows
*   Modular architecture. Includes OAuth and DataService modules.

Built on ECMAScript 6
---------------------

To support modern application development, and to integrate seamlessly with modern JavaScript frameworks, ForceJS 2 is built on top of ECMAScript 6 and leverages ES6 modules and promises. ForceJS 2 also supports modern development workflows (installation via npm, builds using Webpack or other build tools, etc.).

Here is a simple example showing how ForceJS 2 can be used in an ECMAScript 6 application to authenticate with Salesforce using OAuth and retrieve a list of contacts:

Compatible with ECMAScript 5
----------------------------

ForceJS 2 can also be used in plain ECMAScript 5 applications using AMD or CommonJS module loaders, or globally using the **force.OAuth** and **force.DataService** variables. This is achieved using a single code base by transpiling the ECMAScript 6 source code into an ECMAScript 5 compatible version using the Universal Module Definition (UMD) format.

Here is a simple example showing how ForceJS 2 can be used in an ECMAScript 5 application to authenticate with Salesforce using OAuth and retrieve a list of contacts:

Modular Architecture
--------------------

ForceJS is built on a modular architecture. It currently includes two modules:

*   **forcejs/oauth**: A module that makes it easy to authenticate with Salesforce using the OAuth User Agent workflow
*   **forcejs/data-service**: A module that makes it easy to access data through the Salesforce APIs

forcejs/oauth and forcejs/data-service are typically used together in an application, but you can use them separately. For example, you could use forcejs/oauth by itself if all you need is a Salesforce access token (Lightning Out use cases). Similarly, you could use forcejs/data-service by itself if you already have an access token, and all you need is a library to access the Salesforce APIs.

Getting Started and API Reference
---------------------------------

ForceJS is easy to use. To get started, try the Quick Starts available in repository’s [readme file](https://github.com/ccoenraets/forcejs/blob/master/README.md) where the API reference also lives.
