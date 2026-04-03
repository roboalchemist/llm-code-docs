# Source: https://firebase.google.com/docs/functions/unit-testing.md.txt

<br />

This page describes best practices and tools for writing unit tests for your functions, such as tests that would be a part of a Continuous Integration (CI) system. To make testing easier, Firebase provides theFirebase Test SDKforCloud Functions. It is distributed on npm as`firebase-functions-test`, and is a companion test SDK to`firebase-functions`. TheFirebase Test SDKforCloud Functions:

- Takes care of the appropriate setup and teardown for your tests, such as setting and unsetting environment variables needed by`firebase-functions`.
- Generates sample data and event context, so that you only have to specify the fields that are relevant to your test.

| **Note:** `firebase-functions-test`can only be used with functions written with`firebase-functions`2.0.0 or above.

## Test setup

Install both`firebase-functions-test`and[Mocha](https://mochajs.org), a testing framework, by running the following commands in your functions folder:  

    npm install --save-dev firebase-functions-test
    npm install --save-dev mocha

Next create a`test`folder inside the functions folder, create a new file inside it for your test code, and name it something like`index.test.js`.

Finally, modify`functions/package.json`to add the following:  

    "scripts": {
      "test": "mocha --reporter spec"
    }

Once you have written the tests, you can run them by running`npm test`inside your functions directory.

### InitializingFirebase Test SDKforCloud Functions

There are two ways to use`firebase-functions-test`:

1. **Online mode (recommended):**Write tests that interact with a Firebase project dedicated to testing so that database writes, user creates, etc. would actually happen, and your test code can inspect the results. This also means that other Google SDKs used in your functions will work as well.
2. **Offline mode:** Write siloed and offline unit tests with no side effects. This means that any method calls that interact with a Firebase product (e.g. writing to the database or creating a user) need to be stubbed. Using offline mode is generally not recommended if you haveCloud FirestoreorRealtime Databasefunctions, since it greatly increases the complexity of your test code.

#### Initialize SDK in online mode (recommended)

If you would like to write tests that interact with a test project, you need to supply the project config values that are needed for initializing the app through`firebase-admin`, and the path to a service account key file.

To get your Firebase project's config values:

1. Open your project settings in the[Firebaseconsole](https://console.firebase.google.com/project/_/settings/general).
2. In**Your apps,**select the desired app.
3. In the right pane, select the option to download a configuration file for Apple and Android apps.

   For web apps, select**Config**to display configuration values.

To create a key file:

1. Open the[Service Accounts pane](https://console.cloud.google.com/iam-admin/serviceaccounts)of theGoogle Cloudconsole.
2. Select theApp Enginedefault service account, and use the options menu at the right to select**Create key**.
3. When prompted, select JSON for the key type, and click**Create**.

After saving the key file, initialize the SDK:  

    // At the top of test/index.test.js
    // Make sure to use values from your actual Firebase configuration
    const test = require('firebase-functions-test')({
      databaseURL: 'https://<var translate="no">PROJECT_ID</var>.firebaseio.com',
      storageBucket: '<var translate="no">PROJECT_ID</var>`.firebasestorage.app`',
      projectId: '<var translate="no">PROJECT_ID</var>',
    }, 'path/to/serviceAccountKey.json');

| **Warning:** Use extra caution when handling service account credentials in your code. Do not commit them to a public repository, deploy them in a client app, or expose them in any way that could compromise the security of your Firebase project.

#### Initialize SDK in offline mode

If you would like to write completely offline tests, you can initialize the SDK without any parameters:  

    // At the top of test/index.test.js
    const test = require('firebase-functions-test')();

### Mocking config values

If you use`functions.config()`in your functions code, you can mock the config values. For example, if`functions/index.js`contains the following code:  

    const functions = require('firebase-functions/v1');
    const key = functions.config().stripe.key;

Then you can mock the value inside your test file like so:  

    // Mock functions config values
    test.mockConfig({ stripe: { key: '23wr42ewr34' }});

### Importing your functions

To import your functions, use`require`to import your main functions file as a module.**Be sure to only do this after initializing`firebase-functions-test`, and mocking config values.**  

    // after firebase-functions-test has been initialized
    const myFunctions = require('../index.js'); // relative path to functions code

If you initialized`firebase-functions-test`in[offline mode](https://firebase.google.com/docs/reference/functions/test/test), and you have`admin.initializeApp()`in your functions code, then you need to stub it before importing your functions:  

```gdscript
// If index.js calls admin.initializeApp at the top of the file,
// we need to stub it out before requiring index.js. This is because the
// functions will be executed as a part of the require process.
// Here we stub admin.initializeApp to be a dummy function that doesn't do anything.
adminInitStub = sinon.stub(admin, 'initializeApp');
// Now we can require index.js and save the exports inside a namespace called myFunctions.
myFunctions = require('../index');https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-rtdb/functions/test/test.offline.js#L40-L46
```

## Testing background (non-HTTP) functions

The process for testing non-HTTP functions involves the following steps:

1. Wrap the function you would like to test with the`test.wrap`method
2. Construct test data
3. Invoke the wrapped function with the test data you constructed and any event context fields you'd like to specify.
4. Make assertions about behavior.

First wrap the function you'd like to test. Let's say you have a function in`functions/index.js`called`makeUppercase`, which you'd like to test. Write the following in`functions/test/index.test.js`  

    // "Wrap" the makeUpperCase function from index.js
    const myFunctions = require('../index.js');
    const wrapped = test.wrap(myFunctions.makeUppercase);

`wrapped`is a function which invokes`makeUppercase`when it is called.`wrapped`takes 2 parameters:

1. **data** (required): the data to send to`makeUppercase`. This directly corresponds to the first parameter sent to the function handler that you wrote.`firebase-functions-test`provides methods for constructing custom data or example data.
2. **eventContextOptions** (optional): fields of the event context that you'd like to specify. The event context is the second parameter sent to the function handler that you wrote. If you do not include an`eventContextOptions`parameter when calling`wrapped`, an event context is still generated with sensible fields. You can override some of the generated fields by specifying them here. Note that you only have to include the fields that you'd like to override. Any fields that you did not override are generated.

    const data = ... // See next section for constructing test data

    // Invoke the wrapped function without specifying the event context.
    wrapped(data);

    // Invoke the function, and specify params
    wrapped(data, {
      params: {
        pushId: '234234'
      }
    });

    // Invoke the function, and specify auth and auth Type (for real time database functions only)
    wrapped(data, {
      auth: {
        uid: 'jckS2Q0'
      },
      authType: 'USER'
    });

    // Invoke the function, and specify all the fields that can be specified
    wrapped(data, {
      eventId: 'abc',
      timestamp: '2018-03-23T17:27:17.099Z',
      params: {
        pushId: '234234'
      },
      auth: {
        uid: 'jckS2Q0' // only for real time database functions
      },
      authType: 'USER' // only for real time database functions
    });

### Constructing test data

The first parameter of a wrapped function is the test data to invoke the underlying function with. There are a number of ways to construct test data.

#### Using custom data

`firebase-functions-test`has a number of functions for constructing data needed to test your functions. For example, use`test.firestore.makeDocumentSnapshot`to create a Firestore`DocumentSnapshot`. The first argument is the data, and the second argument is the full reference path, and there is an[optional third argument](https://firebase.google.com/docs/reference/functions/test/test.firestore.DocumentSnapshotOptions)for other properties of the snapshot you can specify.  

    // Make snapshot
    const snap = test.firestore.makeDocumentSnapshot({foo: 'bar'}, 'document/path');
    // Call wrapped function with the snapshot
    const wrapped = test.wrap(myFunctions.myFirestoreDeleteFunction);
    wrapped(snap);

If you are testing an`onUpdate`or`onWrite`function, you'll need to create two snapshots: one for the before state and one for the after state. Then, you can use the`makeChange`method to create a`Change`object with these snapshots.  

    // Make snapshot for state of database beforehand
    const beforeSnap = test.firestore.makeDocumentSnapshot({foo: 'bar'}, 'document/path');
    // Make snapshot for state of database after the change
    const afterSnap = test.firestore.makeDocumentSnapshot({foo: 'faz'}, 'document/path');
    const change = test.makeChange(beforeSnap, afterSnap);
    // Call wrapped function with the Change object
    const wrapped = test.wrap(myFunctions.myFirestoreUpdateFunction);
    wrapped(change);

| **Note:** You should only construct custom data forCloud FirestoreandRealtime Databaseif you initialized the SDK in[online mode](https://firebase.google.com/docs/functions/unit-testing#online-mode). Otherwise, you should use[stubbed data](https://firebase.google.com/docs/functions/unit-testing#stubbed-data)to avoid unexpected behavior.

See the[API reference](https://firebase.google.com/docs/reference/functions/test)for similar functions for all the other data types.

#### Using example data

If you don't need to customize the data used in the your tests, then`firebase-functions-test`offers methods for generating example data for each function type.  

    // For Firestore onCreate or onDelete functions
    const snap = test.firestore.exampleDocumentSnapshot();
    // For Firestore onUpdate or onWrite functions
    const change = test.firestore.exampleDocumentSnapshotChange();

| **Note:** You should only construct example data forCloud FirestoreandRealtime Databaseif you initialized the SDK in[online mode](https://firebase.google.com/docs/functions/unit-testing#online-mode). Otherwise, you should use[stubbed data](https://firebase.google.com/docs/functions/unit-testing#stubbed-data)to avoid unexpected behavior.

See the[API reference](https://firebase.google.com/docs/reference/functions/test)for methods for getting example data for every function type.

#### Using stubbed data (for offline mode)

If you initialized the SDK in offline mode, and are testing aCloud FirestoreorRealtime Databasefunction, you should use a plain object with stubs instead of creating an actual`DocumentSnapshot`or`DataSnapshot`.

Let's say you are writing a unit test for the following function:  

```gdscript
// Listens for new messages added to /messages/:pushId/original and creates an
// uppercase version of the message to /messages/:pushId/uppercase
exports.makeUppercase = functions.database.ref('/messages/{pushId}/original')
    .onCreate((snapshot, context) => {
      // Grab the current value of what was written to the Realtime Database.
      const original = snapshot.val();
      functions.logger.log('Uppercasing', context.params.pushId, original);
      const uppercase = original.toUpperCase();
      // You must return a Promise when performing asynchronous tasks inside a Functions such as
      // writing to the Firebase Realtime Database.
      // Setting an "uppercase" sibling in the Realtime Database returns a Promise.
      return snapshot.ref.parent.child('uppercase').set(uppercase);
    });https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-rtdb/functions/index.js#L46-L58
```

Inside of the function,`snap`is used twice:

- `snap.val()`
- `snap.ref.parent.child('uppercase').set(uppercase)`

In test code, create a plain object where both of these code paths will work, and use[Sinon](http://sinonjs.org)to stub the methods.  

```gdscript
// The following lines creates a fake snapshot, 'snap', which returns 'input' when snap.val() is called,
// and returns true when snap.ref.parent.child('uppercase').set('INPUT') is called.
const snap = {
  val: () => 'input',
  ref: {
    parent: {
      child: childStub,
    }
  }
};
childStub.withArgs(childParam).returns({ set: setStub });
setStub.withArgs(setParam).returns(true);https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-rtdb/functions/test/test.offline.js#L70-L81
```

### Making assertions

After initializing the SDK, wrapping the functions, and constructing data, you can invoke the wrapped functions with the constructed data and make assertions about behavior. You can use a library such as[Chai](http://chaijs.com)for making these assertions.

#### Making assertions in online mode

If you initialized theFirebase Test SDKforCloud Functionsin[online mode](https://firebase.google.com/docs/functions/unit-testing#online-mode), you can assert that the desired actions (such as a database write) has taken place by using the`firebase-admin`SDK.

The example below asserts that 'INPUT' has been written into the database of the test project.  

```gdscript
// Create a DataSnapshot with the value 'input' and the reference path 'messages/11111/original'.
const snap = test.database.makeDataSnapshot('input', 'messages/11111/original');

// Wrap the makeUppercase function
const wrapped = test.wrap(myFunctions.makeUppercase);
// Call the wrapped function with the snapshot you constructed.
return wrapped(snap).then(() => {
  // Read the value of the data at messages/11111/uppercase. Because `admin.initializeApp()` is
  // called in functions/index.js, there's already a Firebase app initialized. Otherwise, add
  // `admin.initializeApp()` before this line.
  return admin.database().ref('messages/11111/uppercase').once('value').then((createdSnap) => {
    // Assert that the value is the uppercased version of our input.
    assert.equal(createdSnap.val(), 'INPUT');
  });
});https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-rtdb/functions/test/test.online.js#L59-L73
```

#### Making assertions in offline mode

You can make assertions about the expected return value of the function:  

```gdscript
const childParam = 'uppercase';
const setParam = 'INPUT';
// Stubs are objects that fake and/or record function calls.
// These are excellent for verifying that functions have been called and to validate the
// parameters passed to those functions.
const childStub = sinon.stub();
const setStub = sinon.stub();
// The following lines creates a fake snapshot, 'snap', which returns 'input' when snap.val() is called,
// and returns true when snap.ref.parent.child('uppercase').set('INPUT') is called.
const snap = {
  val: () => 'input',
  ref: {
    parent: {
      child: childStub,
    }
  }
};
childStub.withArgs(childParam).returns({ set: setStub });
setStub.withArgs(setParam).returns(true);
// Wrap the makeUppercase function.
const wrapped = test.wrap(myFunctions.makeUppercase);
// Since we've stubbed snap.ref.parent.child(childParam).set(setParam) to return true if it was
// called with the parameters we expect, we assert that it indeed returned true.
return wrapped(snap).then(makeUppercaseResult => {
  return assert.equal(makeUppercaseResult, true);
});https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-rtdb/functions/test/test.offline.js#L62-L89
```

You can also used[Sinon spies](http://sinonjs.org/releases/v4.0.0/spies/)to assert that certain methods have been called, and with parameters you expect.

## Testing HTTP functions

To test HTTP onCall functions, use the same approach as[testing background functions](https://firebase.google.com/docs/functions/unit-testing#test-background).

If you are testing HTTP onRequest functions, you should use`firebase-functions-test`if:

- You use`functions.config()`
- Your function interacts with a Firebase project or other Google APIs, and you'd like to use a real Firebase project and its credentials for your tests.

An HTTP onRequest function takes two parameters: a request object and a response object. Here is how you might test the[`addMessage()`example function](https://github.com/Firebase/functions-samples/tree/main/Node-1st-gen/quickstarts/uppercase/functions/index.js):

- Override the redirect function in the response object, since`sendMessage()`calls it.
- Within the redirect function, use[chai.assert](http://chaijs.com/api/assert/)to help make assertions about what parameters the redirect function should be called with:

```gdscript
// A fake request object, with req.query.text set to 'input'
const req = { query: {text: 'input'} };
// A fake response object, with a stubbed redirect function which asserts that it is called
// with parameters 303, 'new_ref'.
const res = {
  redirect: (code, url) => {
    assert.equal(code, 303);
    assert.equal(url, 'new_ref');
    done();
  }
};

// Invoke addMessage with our fake request and response objects. This will cause the
// assertions in the response object to be evaluated.
myFunctions.addMessage(req, res);https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/quickstarts/uppercase-rtdb/functions/test/test.offline.js#L124-L138
```

## Test cleanup

At the very end of your test code, call the cleanup function. This unsets environment variables that the SDK set when it was initialized, and deletes Firebase apps that may have been created if you used the SDK to create a real time database`DataSnapshot`or Firestore`DocumentSnapshot`.  

    test.cleanup();

## Review complete examples and learn more

You can review the complete examples on the Firebase GitHub repository.

- [TestingRealtime Databaseand HTTP Functions in Online Mode](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/quickstarts/uppercase-rtdb/functions/test/test.online.js)
- [TestingRealtime Databaseand HTTP Functions in Offline Mode](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/quickstarts/uppercase-rtdb/functions/test/test.offline.js)

To learn more, refer to the[API reference](https://firebase.google.com/docs/reference/functions/test)for`firebase-functions-test`.