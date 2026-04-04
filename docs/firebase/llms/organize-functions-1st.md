# Source: https://firebase.google.com/docs/functions/1st-gen/organize-functions-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Organize multiple functions](https://firebase.google.com/docs/functions/organize-functions).

As you integrate Cloud Functions into your project, your code could expand to contain many independent functions. You may have too many functions to reasonably fit in a single file, or different teams may deploy different groups of functions, creating a risk of one team overwriting or accidentally deleting another team's functions. Cloud Functions offers different ways to organize your code to make it easier to navigate and maintain your functions.

## Organize functions in codebases

You can use the`codebase`property of the functions configuration object in`firebase.json`to manage a large collection of functions across multiple repositories or sub-packages within a single repository monorepo setup:  

    # firebase.json
    "functions": {
      "codebase": "my-codebase"
      # NOTE: Codebase must be less than 63 characters and can contain only
      # lowercase letters, numeric characters, underscores, and dashes.
    }

The`codebase`property is supported in Firebase CLI v10.7.1 and above.

### Managing multiple repositories

The`codebase`property can help simplify the management of multiple repositories. Let's examine a case where you have two different repositories that deploy functions to the same Firebase project:  

    $  tree .
    âââ repoA
    â   âââ firebase.json
    â   âââ functions
    â       âââ index.js
    â       âââ package.json
    âââ repoB
        âââ firebase.json
        âââ functions
            âââ index.js
            âââ package.json

Without codebase annotations, the Firebase CLI would have prompted you to delete functions defined in the other repository at the time of deploy:  

    $ (cd repoA && firebase deploy --only functions)
    ...
    i  functions: preparing functions directory for uploading...
    â  functions: functions folder uploaded successfully
    The following functions are found in your project but do not exist in your local source code:
            fn1FromRepoB
            fn2FromRepoB
            ...
    ? Would you like to proceed with deletion? Selecting no will continue the rest of the deployments. (y/N)

You can avoid this problem by adding a unique codebase annotation in the functions configuration section of the`firebase.json`in each project repository:  

    # repoA/firebase.json
    "functions": {
      "codebase": "repo-a"
    }

    # repoB/firebase.json
    "functions": {
      "codebase": "repo-b"
    }

With codebase annotation, the Firebase CLI no longer prompts you to delete functions defined outside of your immediate repository:  

    $ (cd repoA && firebase deploy --only functions)
    ...
    i  functions: preparing functions directory for uploading...
    â  functions: functions folder uploaded successfully
    #  Gleefully ignores functions from repoB
    i  functions: creating Node.js 16 function fnFromRepoA (us-central1)...
    â  Deploy Complete!

### Managing multiple source packages (monorepo)

The`codebase`property can help simplify the management of multiple source packages in a single repository. Let's examine a case where you have a firebase project directory with function definitions spread across several sub-packages:  

    $  tree .
    âââ firebase.json
    âââ teamA
    â   âââ index.js
    â   âââ package.json
    âââ teamB
        âââ index.js
        âââ package.json

This setup fits the following use cases:

- You have a*monorepo*setup and have different teams manage their own function definitions in an isolated package.
- You have a function with a heavy external dependency and a long-running initialization, and want to isolate that function from other, latency-sensitive functions.

To support monrepo setup like this, define multiple functions configurations in`firebase.json`:  

    "functions": [
      {
        "source": "teamA",
        "codebase": "team-a"
      },
      {
        "source": "teamB",
        "codebase": "team-b"
      },
    ]

With this configuration, the Firebase CLI deploys functions from all packages in a single deploy command:  

    $ firebase deploy --only functions
    i  deploying functions
    i  functions: preparing codebase team-a for deployment
    i  functions: preparing codebase team-b for deployment
    i  functions: creating Node.js 16 function team-a:helloATeam(us-central1)...
    i  functions: creating Node.js 16 function team-b:helloBTeam(us-central1)...
    ...

You can also deploy a specific codebase:  

    $ firebase deploy --only functions:team-b
    i  deploying functions
    i  functions: preparing codebase team-b for deployment
    i  functions: updating Node.js 16 function team-b:helloBTeam(us-central1)...
    ...

## Write functions in multiple files

When getting started withCloud Functionsyou might put your first few functions in a single file:  

### index.js

    const functions = require('firebase-functions/v1');
    exports.foo = functions.https.onRequest((request, response) => {
      // ...
    });
    exports.bar = functions.https.onRequest((request, response) => {
      // ...
    });

### main.py

    from firebase_functions import https_fn

    @https_fn.on_request()
    def foo(req: https_fn.Request) -> https_fn.Response:
        return https_fn.Response("Hello foo!")

    @https_fn.on_request()
    def bar(req: https_fn.Request) -> https_fn.Response:
        return https_fn.Response("Hello bar!")

This can become hard to manage with more than a few functions. Instead, you can put all of your logic for each function in its own file and use your source file as a list of exports:  

### Node.js

**foo.js**  

```javascript
const functions = require('firebase-functions/v1');
exports.foo = functions.https.onRequest((request, response) => {
  // ...
});
```

<br />

**bar.js**  

```javascript
const functions = require('firebase-functions/v1');
exports.bar = functions.https.onRequest((request, response) => {
  // ...
});
```

<br />

**index.js**  

```javascript
const foo = require('./foo');
const bar = require('./bar');
exports.foo = foo.foo;
exports.bar = bar.bar;
```

<br />

### Python

**foo.py**  

    from firebase_functions import https_fn

    @https_fn.on_request()
    def foo(req: https_fn.Request) -> https_fn.Response:
        return https_fn.Response("Hello foo!")

**bar.py**  

    from firebase_functions import https_fn

    @https_fn.on_request()
    def bar(req: https_fn.Request) -> https_fn.Response:
        return https_fn.Response("Hello foo!")

**main.py**  

    from fn_impl.foo import *
    from fn_impl.bar import *

This setup assumes a project directory structure like the following:  

    my-project
    âââ firebase.json
    âââ functions
        âââ fn_impl
        â   âââ __init__.py
        â   âââ foo.py
        â   âââ bar.py
        âââ main.py
        âââ requirements.txt

`fn_impl`: Can have any name

`__init__.py`: Required, but can be empty

## Group functions

In many projects, functions can be separated into logical groups that should be deployed and maintained together. For example, you might have a group of functions used for reporting metrics:

**metrics.js**  

```gdscript

const functions = require('firebase-functions/v1');
exports.usageStats = functions.https.onRequest((request, response) => {
  // ...
});
exports.nightlyReport = functions.https.onRequest((request, response) => {
  // ...
});
```

<br />

You can put these functions into a group when exporting them in your`index.js`file:

**index.js**  

```gdscript

// Export both functions from metrics.js in the "metrics" group:
//  - metrics-usageStats
//  - metrics-nightlyReport
exports.metrics = require('./metrics');
```

<br />

When deployed, functions will be prefixed with the name of their group, so in this example the functions would be named`metrics-usageStats`and`metrics-nightlyReport`.

When deploying functions you can limit the action to a single group:  

```ecl

firebase deploy --only functions:metrics
```
| **Note:** While[#organize_functions_in_codebases](https://firebase.google.com/docs/functions/1st-gen/organizing%20functions%20in%20a%20codebase)lets you benefit by skipping unmodified functions during deploy, writing functions in multiple files will still affect the node module for your functions and you won't benefit from skipped deploys.

## Next steps

To learn more aboutCloud Functions, see:

- [Handling dependencies](https://firebase.google.com/docs/functions/handle-dependencies).
- [Manage functions deployment and runtime options](https://firebase.google.com/docs/functions/1st-gen/manage-functions-1st).