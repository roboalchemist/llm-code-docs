# Source: https://firebase.google.com/docs/functions/local-shell.md.txt

<br />

The Cloud Functions shell provides an interactive shell for invoking functions with test data. The shell supports all trigger types.

## Set up admin credentials (optional)

If you want your functions tests to interact with Google APIs or other Firebase APIs via the[Firebase Admin SDK](https://firebase.google.com/docs/admin/setup), you may need to set up admin credentials.

- Cloud FirestoreandRealtime Databasetriggers already have sufficient credentials, and do**not**require additional setup.
- All other APIs, including Firebase APIs such asAuthenticationandFCMor Google APIs such as Cloud Translation or Cloud Speech, require the setup steps described in this section. This applies whether you're using theCloud Functionsshell or`firebase emulators:start`.

**To set up admin credentials for emulated functions:**

1. Open the[Service Accounts pane](https://console.cloud.google.com/iam-admin/serviceaccounts)of theGoogle Cloudconsole.
2. Make sure that**App Enginedefault service account** is selected, and use the options menu at right to select**Create key**.
3. When prompted, select**JSON** for the key type, and click**Create**.
4. Set your Google default credentials to point to the downloaded key:

   ### Unix

   ```
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/key.json"
   firebase functions:shell
   ```

   ### Windows

   ```
   set GOOGLE_APPLICATION_CREDENTIALS=path\to\key.json
   firebase functions:shell
   ```

After completing these steps, your functions tests can access Firebase and Google APIs using the[Admin SDK](https://firebase.google.com/docs/admin/setup). For example, when testing anAuthenticationtrigger, the emulated function could call`admin.auth().getUserByEmail(email)`.

## Serve functions using a Cloud Functions shell

The Cloud Functions shell emulates all types of function triggers with an interactive shell for invoking the functions with test data. Options vary by function type, but the basic usage format is:  

    myFunctionName(data, options)

The`data`parameter is required for Realtime Database, Cloud Firestore, and PubSub triggers, and optional for all other function types. Also, the optional`options`parameter is valid only for Realtime Database and Cloud Firestore functions.

Optionally, you can load test data from a local file by saving the file as a variable and invoking a function with it:  

    var data = require('./path/to/testData.json');
    myFunction(data);

### Install and configure the Cloud Functions shell

To use this feature,`firebase-tools`must have minimum version 3.11.0, and`firebase-functions`SDK must have minimum version 0.6.2. To update both, run the following commands in the`functions/`directory for your project:  

    npm install --save firebase-functions@latest
    npm install -g firebase-tools

If you're using custom functions configuration variables, first run the command to get your custom config (run this within the`functions`directory) in your local environment:  

```
firebase functions:config:get > .runtimeconfig.json
# If using Windows PowerShell, replace the above with:
# firebase functions:config:get | ac .runtimeconfig.json
```

Finally, run the shell with the following command:  

    firebase functions:shell

### Invoke HTTPS functions

For invoking HTTPS functions in the shell, usage is the same as the[`request`](https://www.npmjs.com/package/request)NPM module, but replace`request`with the name of the function you want to emulate. For example:  

    # invoke
    myHttpsFunction()
    myHttpsFunction.get()
    myHttpsFunction.post()

    # invoke at sub-path
    myHttpsFunction('/path')
    myHttpsFunction.get('/path')
    myHttpsFunction.post('/path')

    # send POST request with form data
    myHttpsFunction.post('/path').form( {foo: 'bar' })

### Invoke HTTPS Callable functions

When invoking HTTPS Callable functions locally, you'll need to provide appropriate test data.  

    # invoke
    myCallableFunction('test data')
    myCallableFunction({'foo': 'bar'})

Optionally, you may pass in a`Firebase-Instance-ID-token`as the second parameter. This must be a string.  

    # invoke with FCM registration token
    myCallableFunction('test data', {instanceIdToken: 'sample token'})

Emulation of`context.auth`is currently unavailable.

### Invoke Realtime Database functions

When running Realtime Database functions locally, you'll need to provide appropriate test data. This generally means providing new test data for`onCreate`operations, old/removed data for`onDelete`operations, and both for`onUpdate`or`onWrite`functions:  

    # invoke onCreate function
    myDatabaseFunction('new_data')

    # invoke onDelete function
    myDatabaseFunction('old_data')

    # invoke onUpdate or onWrite function
    myDatabaseFunction({before: 'old_data', after: 'new_data' })

In addition to the`before/after`options, the shell provides the`params`option to use in mocking wildcards in a path:  

    # mock wildcards in path, for example: if the path was input/{group}/{id}
    myDatabaseFunction('data', {params: {group: 'a', id: 123}})

By default, the shell runs Realtime Database functions with admin (service account) privileges. Use the`auth`option to instead run functions as a particular end user, or as an unauthenticated user:  

    # to mock unauthenticated user
    myDatabaseFunction('data', {authMode: 'USER'})
    # to mock end user
    myDatabaseFunction('data', {auth: {uid: 'abcd'}})

### Invoke Firestore functions

When running Firestore functions locally, you'll need to provide appropriate test data. This generally means providing new test data for`onCreate`operations, old/removed data for`onDelete`operations, and both for`onUpdate`or`onWrite`functions. Note that Firestore data has to be key-value pairs; see[Supported Data Types](https://firebase.google.com/docs/firestore/manage-data/data-types).  

    # invoke onCreate function
    myFirestoreFunction({foo: 'new'})

    # invoke onDelete function
    myFirestoreFunction({foo: 'old'})

    # invoke onUpdate or onWrite function
    myFirestoreFunction({before: {foo: 'old'}, after: {foo: 'new'} })

In addition to the`before/after`fields of the`data`object, you can use the`params`fields on the`options`object to mock wildcards in a document name:  

    # mock wildcards in document name, for example: if the name was input/{group}/{id}
    myFirestoreFunction({foo: 'new'}, {params: {group: 'a', id: 123}})

The shell always runs Firestore functions with administrative privileges, which means it mocks a create/update/delete event as if it were done by an administrative user.

### Invoke PubSub functions

For PubSub functions, insert your message payload in a`Buffer`instance and add optionally data attributes as shown:  

    // invokes a function with the JSON message { hello: 'world' } and attributes { foo: 'bar' }
    myPubsubFunction({data: new Buffer('{"hello":"world"}'), attributes: {foo: 'bar'}})

### Invoke Analytics functions

You can invoke an Analytics function without any data by running`myAnalyticsFunction()`in the shell. To run the function with test data, it is recommended to define a variable for the specific event data fields that your function needs:  

    var data = {
      eventDim: [{
        // populates event.data.params
        params: {foo: {stringValue: 'bar'} },
        // Also valid:
        //   {intValue: '10'}, {floatValue: '1.0'}, {doubleValue: '1.0'}
        // populates event.data.name
        name: 'event_name',
        // populates event.data.logTime, specify in microseconds
        timestampMicros: Date.now() * 1000,
        // populates event.data.previousLogTime, specify in microseconds
        previousTimestampMicros: Date.now() * 1000,
        // populates event.data.reportingDate, specify in 'YYYYMMDD' format
        date: '20170930',
        // populates event.data.valueInUSD
        valueInUsd: 230
      }],
      userDim: userDim
    };

    myAnalyticsFunction(data);

### Invoke Storage and Auth functions

For Storage and Auth functions, invoke the local function with the test data that you'd like to see inside of the function. Your test data must follow the corresponding data formats:

- ForCloud Storage:[`ObjectMetadata`](https://firebase.google.com/docs/reference/functions/firebase-functions.storage.objectmetadata)
- ForAuthentication:[`UserRecord`](https://firebase.google.com/docs/reference/functions/firebase-functions.auth#authuserrecord)

Specify only the fields that your code depends on, or none at all if you only want to run the function.