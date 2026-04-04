# Source: https://docs-containers.back4app.com/docs/advanced-guides/parse-server-3.md

---
title: Upgrade to Parse 3.1
slug: docs/advanced-guides/parse-server-3
description: In this guide you learn how to use version 3.1 at Back4App
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-26T13:12:41.820Z
updatedAt: 2025-01-17T01:10:08.380Z
---

# More power to your App with Parse Server 3.1

## Introduction

The Parse Community recently released version [**3.1 of the Parse Server**](https://docs.parseplatform.org/parse-server/guide/). This update has cleaned up Cloud Code syntax: it is far more amenable to leveraging the es6 async and await constructs.

Additionally, some idiosyncrasies associated with using Parse were dropped, for example, Cloud functions simply return a Promise rather than using the error or success messages on the Response object.

You can upgrade your apps on Back4App easily on your Dashboard. This guide will demonstrate how to upgrade your code to leverage the new features of 3.1.

:::hint{type="info"}
To follow this guide you are welcome to take a look at the [**example project**](https://github.com/back4app/parse-server-break-changes) provided.
:::

This is a guest tutorial written by [**John Considine**](https://github.com/considine), lead developer at [**K-Optional**](https://koptional.com/).

## Goals

- To update your Back4App Parse Server to 3.1 and migrate your Cloud Code accordingly.

## Prerequisites

:::hint{type="info"}
To complete this tutorial, you need:

° An existing Back4App application that’s using Parse Server 2.x
&#x20;        °    Follow the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
:::

## Summary of changes

The most notable changes are the following:

**&#x20;1. Cloud Code runs with Parse-SDK 2.x.**&#x20;

Previously, Cloud Code ran with Parse-SDK 1.x. With Parse Server 3.1, it runs Parse-SDK 2.x.

:::hint{type="info"}
Look at [**Parse SDK releases**](https://github.com/parse-community/Parse-SDK-JS/releases) to understand better what this entails. This major version bump mostly involves bug fixes. It also adds [**containedBy**](https://parseplatform.org/Parse-SDK-JS/api/2.1.0/Parse.Query.html#containedBy) and [**includeAll**](https://parseplatform.org/Parse-SDK-JS/api/2.1.0/Parse.Query.html#includeAll) query methods, as well as abilities to fetch an object with includes.
:::

&#x20;**2**. **Aggregate update**

Since Parse 2.7.1, you can use the [**aggregate**](https://parseplatform.org/Parse-SDK-JS/api/2.1.0/Parse.Query.html#aggregate) method on a query. This allows you to leverage the underlying database a little bit more. Now, the syntax for the [**aggregate method**](https://parseplatform.org/Parse-SDK-JS/api/2.1.0/Parse.Query.html#aggregate) on Parse.Query has been updated.

You can execute a query using two stages: the match and the group stage.

:::BlockQuote
1    // matches users whose name are Foo, and groups by their objectId
2    const pipeline = \[\{ group: \{ objectId: \{} } }, \{ match: \{ name: 'Foo' } }];
3
4    var query = new Parse.Query("Person");
5    query.aggregate(pipeline)
:::

Previously, you didn’t need the pipeline key in the pipeline object. Due to the underlying API, you must now explicitly include the pipeline key. The value should be an array of one or two stages, featuring group and match.

:::hint{type="info"}
Look at [**Parse Official Documentation**](https://docs.parseplatform.org/js/guide/#aggregate) for more specific examples.
:::

**3**. **Under-the-hood optimizations**

Some under-the-hood optimizations have been made. For example, a [**Parse LiveQuery**](https://parseplatform.org/Parse-SDK-JS/api/2.1.0/Parse.LiveQuery.html) will fetch Class Level Permissions (CLPs) along with data to prevent double database access.

**4. Parse Reset Email**

When requesting a password reset email, the server will return success even if that email is not saved. Additionally, password reset tokens expire when a user’s email is reset.

**5.** **Cloud triggers update**

With this release, you can share data between the [**beforeSave**](https://docs.parseplatform.org/cloudcode/guide/#beforesave-triggers) and [**afterSave**](https://docs.parseplatform.org/cloudcode/guide/#aftersave-triggers) triggers on the same object. For example:

```javascript
1    Parse.Cloud.beforeSave('Comment', async request => {
2      request.context = {
3        foo: 'bar'
4      };
5    });
6
7    Parse.Cloud.afterSave('Comment', async request => {
8      console.log(request.context.foo); //Bar
9    });
```

:::hint{type="info"}
You can see more about changes on Parse Server in the official Parse 3.1 Changelog by clicking[**&#x20;here**](https://github.com/parse-community/parse-server/blob/alpha/CHANGELOG.md).
:::

**6. LiveQuery Improvement**

The Parse LiveQuery client allows you to subscribe to queries, and receive updates from the server as they come in. Traditional Queries are executed once by the client, so this is very helpful for cases like messaging, etc.

With Back4App you can also [**take advantage of this technology**](https://www.back4app.com/docs/platform/parse-server-live-query-example).

With the release of 3.x, the Parse community has improved the system for LiveQuery [**ACLs**](https://docs.parseplatform.org/js/guide/#security-for-other-objects).

You can pass a session token now to the subscribe method of a live query, and the Parse Server will manage only returning results that this user has access to. For example, a user may have read/write access to certain ‘Messages’, but not all.

```javascript
1   let query = new Parse.Query('Message');
2   // you can get session token with
3   // Parse.User.current().getSessionToken() when logged in
4   let subscription = client.subscribe(query, sessionToken); 
```

The above code will automatically subscribe to all messages that the user has access to, relieving you from the responsibility of querying specific messages.

**The main part of the changes pertains to how Cloud Code is handled. For this, see the migration guide below.**

## 1 - Aligning technical fundamentals

We’ll start with an example cloud project using the 2.x release. That way we can navigate through the appropriate changes of syntax. You can see [**the repository**](https://github.com/back4app/parse-server-break-changes) for this example project.

**If you’re familiar with async and await, you can skip this section.**

The evolution of asynchronous code in Javascript looks something like this:

- [**Callback Functions**](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)
- [**Promises**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [**Async / Await**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

Any modern Javascript application will likely use all three. Callback functions involve passing a function as an argument to another function. This second function can execute the first at some point.

```javascript
1   // Callbacks:
2   // executes callback function after waiting 100 milliseconds
3   setTimeout(function() {
4     alert('My callback function');
5   }, 100);
```

Callbacks are essential but can be unwieldy when it comes to chaining many of them. Specifically, nesting several layers can be difficult to read, and error handling proves difficult. Hence in ES2015 the Promise was introduced.

```javascript
1   // promises
2   // executes several promises in a row with no significant nesting
3   const myPromise = new Promise(function(resolve, reject) {
4     setTimeout(function() {
5        if (Math.random() < 0.2) reject(new Error('Random failure!'));
6        resolve('Finished');
7     }, 100);
8   });
9
10  // Executes this promise 4 times and catches errors involved
11  myPromise
12    .then(() => myPromise)
13    .then(() => myPromise)
14    .then(() => myPromise)
15    .then(() => myPromise)
16    .catch(e => console.log(e));
```

Promises improve the readability of asynchronous programming. They also make pipelines more explicit. But even bigger strides were made in [**ES2017**](https://www.ecma-international.org/ecma-262/8.0/#sec-async-function-definitions) with the async / await constructs. Your code can now wait for the results of a Promise without relying on the then / catch blocks (which can also become tough to read).&#x20;

```javascript
1   // Using the definition of myPromise from the above code:
2   async function foo() {
3     try {
4       let result = await myPromise;
5       result = await myPromise;
6       result = await myPromise;
7     } catch (e) {
8       console.log(e);
9     }
10  }
```

Perhaps for a very simple example, this may not seem more elegant than plain promises. But awaiting the results of an asynchronous function is often precisely what we want to do. Hence, it truly optimizes the readability of our code.

**Support for async/await**

As aforementioned, async/await was included in the [**ECMAScript 2017 specification**](https://www.ecma-international.org/ecma-262/8.0) (es8). For server code, versioning is hardly an issue since you can update to [**the version of Node.js that supports these features**](https://node.green/#ES2017). Rest assured, Back4App’s environment supports recent stable versions. For browser code, transpilers like [**Babel**](https://babeljs.io/) will produce an es2016 compatible with code that uses async / await and works in modern browsers.

## 2 - Thinking about your code differently

The main change with Cloud Code involves what the developer does versus what the library does. Previously, you would explicitly manage the response. Since most Cloud Code will execute asynchronously - making database queries and writes - it makes more sense to return a Promise, reducing the boilerplate code.

The intuition behind Cloud functions is that there is minimal setup and configuration involved with writing server-side code. This release embodies that idea; keep this in mind as you’re refactoring and creating new functions.

To show how Cloud Code functions work in Parse Server 3.1, we rewrote a functional Cloud Code sample from a version of Parse Server before migration. You can find this code by clicking [**here**](https://github.com/back4app/parse-server-break-changes/tree/step_1). The same Cloud Code function is written in Parse 3.1 as shown below.

```javascript
1   // Cloud Code BEFORE migration
2   // Full code found in link above
3   const POST = 'Post';
4   Parse.Cloud.define('posts:get', function(request, response) {
5     // needs a post ID
6     return new Parse.Query(POST)
7       .get(request.params.id, { useMasterKey: true })
8       .then(post => {
9         response.success(post);
10      })
11      .catch(e => {
12        response.error({ message: e.message });
13      });
14  });
```

## 3 - Adding all async markers

Any function that uses await must be declared with the async modifier. This simple refactoring will attach async to all Cloud Functions. It will also replace them with [**arrow functions**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) as they are more succinct in this case (and what the updated official Parse guide uses).

```javascript
1   // Snippet of step 2 code refactoring. See full code
2   //  here in the link at the top of this step
3   const POST = 'Post';
4   const COMMENT = 'Comment';
5
6   Parse.Cloud.define('posts:get', async (request) => {
7     // Needs a post ID
8     return new Parse.Query(POST)
9       .get(request.params.id, { useMasterKey: true });
10  }    
```

**Your code will look like&#x20;**[**this**](https://github.com/back4app/parse-server-break-changes/tree/step_2)**&#x20;after this refactoring**

Nothing crazy so far. In the next step, we’ll get our money’s worth for this change.

## 4 - Removing references to response, employ await

**Your code will look like&#x20;**[**this**](https://github.com/back4app/parse-server-break-changes/tree/step_3)**&#x20;after this refactoring**

This step is a little bit trickier. We need to:

- Remove all references to the ‘response’ variable, returning a promise instead
- In the case of multiple query/save functions, await the response

Check out the comment create method to see how this is done

```javascript
1   // Snippet of step 3 code refactoring. See full code
2   //  here in the link at the top of this step
3   Parse.Cloud.define('comment:create', async request => {
4     // Post should have text and should have a user and a post id
5     if (!request.user) {
6       throw new Error('unauthenticated!');
7     }
8
9     if (!request.params.text) {
10      throw new Error('A comment needs text!');
11    }
12    if (!request.params.post_id) {
13      throw new Error('A comment needs a post!');
14    }
15
16    //   Get the post
17
18    const post = await new Parse.Query(POST).get(request.params.post_id, {
19      useMasterKey: true
20    });
21    return new Parse.Object(COMMENT, {
22      text: request.params.text,
23      user: request.user,
24      post: post
25    }).save(null, { useMasterKey: true });
26  });
```

:::hint{type="info"}
Note that:


- Now a JavaScript Error is thrown instead of calling response.error. Parse will handle transforming this into a response for us.
- Deleting a ‘Post’ or ‘Comment’ involves grabbing the object first, then destroying it. By using ‘await’, the destroy method can access the saved object outside of a block.&#x20;
:::

That completes all necessary refactoring for migration. That’s to say if you do up until this Step, congrats! Your code will run on Back4App Parse 3.1!

## 5 - Advanced Tricks (optional)

The following changes are optional but can shorten your code significantly. I find they reduce boilerplate.

You probably noticed a lot of manual checks for parameters or the authenticated user. These ensure that strange behavior doesn’t occur. For example, we’ve decided our ‘Post’ object needs text, so if no ‘text’ parameter is passed, the object will get saved without it. One way to prevent this is to check that text was passed.

But manual checks can be time-consuming and inelegant. In this section, we take advantage of [**object destructuring**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) to implicitly complete these checks.

You should see the documentation above if you don’t know what destructuring is. But in short, it allows you to turn an object’s property into a variable with very concise syntax.

```javascript
1   // This
2   var obj = {
3     hi: true,
4     bye: false
5   };
6   var hi = obj.hi;
7   var bye = obj.bye;
8
9   // Is equivalent to this:
10  var obj = {
11    hi: true,
12    bye: false
13  };
14  var { hi, bye } = obj;
15
16  console.log(hi);
17  // true
18  console.log(bye);
19  // false
```

Destructuring is less verbose than manual assignment. It also allows you to declare parameter variables on the fly which is nice:

```javascript
1   Parse.Cloud.define('posts:get', async ({ params: { id } }) => {
2     // id is declared
3   });
```

When combined with an es2015 notation for [**object initialization**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#New_notations_in_ECMAScript_2015) we can optimize our parameter checks.

We can do this:

```javascript
1   // Iterates through object's keys. Makes sure, for each key, the value is set
2   const AssertParams = parameter_obj => {
3     for (var key of Object.keys(parameter_obj)) {
4       if (typeof parameter_obj[key] === 'undefined')
5         throw new Error(`Missing parameter ${key}`);
6     }
7   };
8
9   var obj = {
10    hi: true,
11    bye: false
12  };
13  var { hi, undef, bye } = obj; // undef will be undefined
14  var check_1 = { hi, bye };
15  var check_2 = { hi, undef };
16
17  // check = { hi : true, no : undefined }
18  AssertParams(check_1); // passes
19  AssertParams(check_2); // throws error
```

So for our Parse code, we can do this:

```javascript
1   // Snippet of advanced code refactoring. See full code
2   //  here in the link at the top of this step
3   Parse.Cloud.define('posts:delete', async ({ user, params: { id } }) => {
4     // Makes sure user is authenticated, and id parameter is passed
5     AssertParams({ user, id });
6     const post = await new Parse.Query(POST).get(id, {
7       useMasterKey: true
8     });
9     return post.destroy({ useMasterKey: true });
10  });
```

If this is daunting, don’t fret. The [**full code**](https://github.com/back4app/parse-server-break-changes/tree/step_advanced) example might help.

In short, ‘AssertParams’ is a utility function for throwing an error if a value is undefined. We can check for parameters in one motion by combining object destructuring and es2015 object initialization.

This removes eight or nine manual checks which start to become unsightly after a while.

## 6 - Upgrading on Back4App

Once you have migrated your code, you must do two more things to have it running on Back4App.

1. Upgrade your Back4App server version
2. Upload your new cloud code.

I’ve briefly mentioned the first step before. All you need to do is log into Back4App and go to your app’s dashboard. From there, just select “Server Settings” on the left, followed by the “Settings” button on the “Manage Parse Server” card. You may then select the Parse Server 3.1.1 radio button and hit “Save”.

Last but not least, you can upload your code via the [**Back4App CLI**](https://blog.back4app.com/2017/01/20/cli-parse-server/), or your dashboard using the manual upload. See [**this guide**](https://www.back4app.com/docs/android/parse-cloud-code) if you need more information on this step.

**Notes on launching a new version**

If your code is complex, it might be a good idea to run some tests before doing these two steps. Back4App has some guides on how to do this [**here**](https://www.back4app.com/docs/advanced-guides/parse-cloud-code-testing) and [**here**](https://www.back4app.com/docs/cloud-code-functions/unit-tests).

Finally, it’s important to note that these changes are **breaking**. Using the code we wrote on a 2.x Parse Server will fail, and using 2.x code on a 3.1 server will also fail. Therefore, you must make sure to upgrade your Back4App parse version right when you upload your upgraded Cloud Code. If you have many users and are concerned about the code upload and version upgrade being slightly out of sync, you can do something like this.

```javascript
1   const serverVersion =
2     Parse.CoreManager.get('VERSION') === 'js1.11.1' ? 'OLD' : 'NEW';
3
4   if (serverVersion === 'NEW') {
5     Parse.Cloud.define('posts:get', async ({ params: { id } }) => {
6       AssertParams({ id });
7       // Needs a post ID
8       return new Parse.Query(POST).get(id, {
9         useMasterKey: true
10      });
11    });
12  } else if (serverVersion === 'OLD') {
13    // Old definition here
14  }
```

This code dynamically figures out the version and defines Cloud Functions based on that. After uploading this, you would change to 3.1, and then you could re-upload the code with the old part removed. Including the check at first ensures there isn’t a point where your code will crash. Since you can upgrade and upload within a couple of seconds, it’s usually not necessary.

## Conclusion

At this guide, we demonstrated simply how to migrate your Cloud Code to the Parse 3.1 release. Remember to bump your Back4App version to 3.1 after you make these changes.

Also importantly, this guide demonstrated an improved syntax that Parse 3.1 leverages. Our refactorings cut the codebase from \~160 lines to \~90 and made it much more readable. For actual applications, this will pay dividends.
