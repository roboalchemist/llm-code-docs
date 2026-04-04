# Source: https://firebase.google.com/docs/admin/migrate-node-v10.md.txt

<br />

Version 10 of the Admin Node.js SDK introduces two important changes:

- Support for Node.js 10 is discontinued (this is a**breaking change**)
- The SDK has adopted a modular API pattern

This guide provides instructions and information to help developers upgrade existing Node.js apps from earlier versions of theAdmin SDKto v10.

## Update Node.js to v12 or higher

With the Admin Node.js SDK v10 release, Firebase has discontinued support for Node.js 10. Developers must use Node.js 12 or higher when using theAdmin SDK. If you're using the Admin Node.js SDK together withCloud Functions for Firebase, make sure that you have[upgraded your Node.js version](https://firebase.google.com/docs/functions/manage-functions#upgrade-node10)to 12 or higher.

## Use modules instead of namespaces

Since its inception, the Admin Node.js SDK has offered a stable API structured as a nested namespace hierarchy. As a result, you might have become familiar with writing code that looks like this:  

    // Import the global admin namespace
    import * as admin from 'firebase-admin';

    const app: admin.app.App = admin.initializeApp();

    const token: string = await admin.auth().createCustomToken('alice');

    const user: admin.auth.UserRecord = await admin.auth().getUser('bob');

Starting from v10, the Admin Node.js SDK offers multiple module entry points with named exports. We recommend developers to use these new entry points to access the various APIs of the SDK, as opposed to using the global`admin`namespace.

Here's what the above example would look like with the new module entry points:  

### TypeScript

    // Import only what you need
    import { initializeApp, App } from 'firebase-admin/app';
    import { getAuth, UserRecord } from 'firebase-admin/auth';

    const app: App = initializeApp();

    const token: string = await getAuth().createCustomToken('alice');

    const user: UserRecord = getAuth().getUser('bob');

### Node.js

    // Import only what you need
    const { initializeApp } = require('firebase-admin/app');
    const { getAuth } = require('firebase-admin/auth');

    const app = initializeApp();

    const token = await getAuth().createCustomToken('alice');

    const user = getAuth().getUser('bob');

### Using v10 modular entry points

Note that, in the examples above, you are no longer importing a global`admin`namespace. Instead, you explicitly import only the symbols you need from several module entry points. Also, TypeScript developers no longer have to use triple- nested type identifiers like`admin.auth.UserRecord`and`admin.database.Reference`. Since each type belongs to exactly one module, you can just import them by their short names like`UserRecord`and`Reference`.

Here are all the module entry points available in the SDK as of v10:

- firebase-admin/app
- firebase-admin/auth
- firebase-admin/database
- firebase-admin/firestore
- firebase-admin/instance-id
- firebase-admin/machine-learning
- firebase-admin/messaging
- firebase-admin/project-management
- firebase-admin/remote-config
- firebase-admin/security-rules
- firebase-admin/storage

The following table shows the replacement import syntax for each of the legacy namespace functions:

|           **v9**            |                                               **v10**                                                |
|-----------------------------|------------------------------------------------------------------------------------------------------|
| `admin.initializeApp()`     | `import { initializeApp } from 'firebase-admin/app'` `initializeApp();`                              |
| `admin.app()`               | `import { getApp } from 'firebase-admin/ap'` `getApp();`                                             |
| `admin.credential.cert()`   | `import { cert } from 'firebase-admin/app'` `cert();`                                                |
| `admin.auth()`              | `import { getAuth } from 'firebase-admin/auth'` `getAuth();`                                         |
| `admin.database()`          | `import { getDatabase } from 'firebase-admin/database'` `getDatabase();`                             |
| `admin.firestore()`         | `import { getFirestore } from 'firebase-admin/firestore'` `getFirestore();`                          |
| `admin.instanceId()`        | `import { getInstanceId } from 'firebase-admin/instance-id'` `getInstanceId();`                      |
| `admin.machineLearning()`   | `import { getMachineLearning } from 'firebase-admin/machine-learning'` `getMachineLearning();`       |
| `admin.messaging()`         | `import { getMessaging } from 'firebase-admin/messaging'` `getMessaging()`                           |
| `admin.projectManagement()` | `import { getProjectManagement } from 'firebase-admin/project-management'` `getProjectManagement();` |
| `admin.remoteConfig()`      | `import { getRemoteConfig } from 'firebase-admin/remote-config'` `getRemoteConfig();`                |
| `admin.securityRules()`     | `import { getSecurityRules } from 'firebase-admin/security-rules'` `getSecurityRules()`              |
| `admin.storage()`           | `import { getStorage } from 'firebase-admin/storage'` `getStorage();`                                |

## Use exported functions instead of methods on App

In the legacy API, the`App`object exposed a number of methods like`app.auth()`and`app.database()`. We recommend developers to avoid using these methods, and instead use the same module entry points described above to obtain service instances scoped to a given`App`object, and perform other app-specific tasks.

|          **v9**           |                                                 **v10**                                                 |
|---------------------------|---------------------------------------------------------------------------------------------------------|
| `app.auth()`              | `import { getAuth } from 'firebase-admin/auth';` `getAuth(app);`                                        |
| `app.database()`          | `import { getDatabase } from 'firebase-admin/database';` `getDatabase(app);`                            |
| `app.database(url)`       | `import { getDatabaseWithUrl } from 'firebase-admin/database';` `getDatabaseWithUrl(url, app);`         |
| `app.firestore()`         | `import { getFirestore } from 'firebase-admin/firestore'` `getFirestore(app);`                          |
| `app.instanceId()`        | `import { getInstanceId } from 'firebase-admin/instance-id'` `getInstanceId(app);`                      |
| `app.machineLearning()`   | `import { getMachineLearning } from 'firebase-admin/machine-learning'` `getMachineLearning(app);`       |
| `app.messaging()`         | `import { getMessaging } from 'firebase-admin/messaging'` `getMessaging(app);`                          |
| `app.projectManagement()` | `import { getProjectManagement } from 'firebase-admin/project-management'` `getProjectManagement(app);` |
| `app.remoteConfig()`      | `import { getRemoteConfig } from 'firebase-admin/remote-config'` `getRemoteConfig(app);`                |
| `app.securityRules()`     | `import { getSecurityRules } from 'firebase-admin/security-rules'` `getSecurityRules(app);`             |
| `app.storage()`           | `import { getStorage } from 'firebase-admin/storage'` `getStorage(app);`                                |
| `app.delete()`            | `import { deleteApp } from 'firebase-admin/app';` `deleteApp(app);`                                     |

## ES modules support

Node.js 12 and above come with experimental support for ES modules, enabling even non-TypeScript developers to use the`export`and`import`keywords in their code. Starting from the v10 release, the Admin Node.js SDK also provides ES modules support, so that developers implementing ES modules on plain Node.js can import the SDK using`import`syntax.

To use ES modules with theAdmin SDK, first make sure you have enabled ESM support for your Node.js runtime. This is usually done by adding a`"type":
"module"`field to your`package.json`file. Then you can write application code that looks like this:  

    // With {type: module} in the package.json...

    // Import only what you need
    import { initializeApp }  from 'firebase-admin/app';
    import { getAuth } from 'firebase-admin/auth';

    const app = initializeApp();

    const token = await getAuth().createCustomToken('alice');

    const user = getAuth().getUser('bob');