# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md.txt

# app.App interface

A Firebase app holds the initialization information for a collection of services.

Do not call this constructor directly. Instead, use [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd) to create an app.

**Signature:**  

    interface App extends AppCore 

**Extends:** AppCore

## Methods

|                                                              Method                                                              |                                                                                                                          Description                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [appCheck()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappappcheck)                   |                                                                                                                                                                                                                                                               |
| [auth()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappauth)                           |                                                                                                                                                                                                                                                               |
| [database(url)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappdatabase)                |                                                                                                                                                                                                                                                               |
| [delete()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappdelete)                       | Renders this local `FirebaseApp` unusable and frees the resources of all associated services (though it does \*not\* clean up any backend resources). When running the SDK locally, this method must be called to ensure graceful termination of the process. |
| [firestore()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappfirestore)                 |                                                                                                                                                                                                                                                               |
| [installations()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappinstallations)         |                                                                                                                                                                                                                                                               |
| [instanceId()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappinstanceid)               |                                                                                                                                                                                                                                                               |
| [machineLearning()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappmachinelearning)     |                                                                                                                                                                                                                                                               |
| [messaging()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappmessaging)                 |                                                                                                                                                                                                                                                               |
| [projectManagement()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappprojectmanagement) |                                                                                                                                                                                                                                                               |
| [remoteConfig()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappremoteconfig)           |                                                                                                                                                                                                                                                               |
| [securityRules()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappsecurityrules)         |                                                                                                                                                                                                                                                               |
| [storage()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app_n.app.md#appappstorage)                     |                                                                                                                                                                                                                                                               |

## app.App.appCheck()

**Signature:**  

    appCheck(): appCheck.AppCheck;

**Returns:**

[appCheck.AppCheck](https://firebase.google.com/docs/reference/admin/node/firebase-admin.appcheck_n.md#appcheckappcheck)

## app.App.auth()

**Signature:**  

    auth(): auth.Auth;

**Returns:**

[auth.Auth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth_n.md#authauth)

## app.App.database()

**Signature:**  

    database(url?: string): database.Database;

### Parameters

| Parameter |  Type  | Description |
|-----------|--------|-------------|
| url       | string |             |

**Returns:**

[database.Database](https://firebase.google.com/docs/reference/admin/node/firebase-admin.database_n.md#databasedatabase)

## app.App.delete()

Renders this local `FirebaseApp` unusable and frees the resources of all associated services (though it does \*not\* clean up any backend resources). When running the SDK locally, this method must be called to ensure graceful termination of the process.

**Signature:**  

    delete(): Promise<void>;

**Returns:**

Promise\<void\>

### Example

    app.delete()
      .then(function() {
        console.log("App deleted successfully");
      })
      .catch(function(error) {
        console.log("Error deleting app:", error);
      });

## app.App.firestore()

**Signature:**  

    firestore(): firestore.Firestore;

**Returns:**

firestore.Firestore

## app.App.installations()

**Signature:**  

    installations(): installations.Installations;

**Returns:**

[installations.Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations_n.md#installationsinstallations)

## app.App.instanceId()

> | **Warning:** This API is now obsolete.
>
> Use [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class) instead.

**Signature:**  

    instanceId(): instanceId.InstanceId;

**Returns:**

[instanceId.InstanceId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instanceid_n.md#instanceidinstanceid)

## app.App.machineLearning()

**Signature:**  

    machineLearning(): machineLearning.MachineLearning;

**Returns:**

[machineLearning.MachineLearning](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machinelearning_n.md#machinelearningmachinelearning)

## app.App.messaging()

**Signature:**  

    messaging(): messaging.Messaging;

**Returns:**

[messaging.Messaging](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging_n.md#messagingmessaging)

## app.App.projectManagement()

**Signature:**  

    projectManagement(): projectManagement.ProjectManagement;

**Returns:**

[projectManagement.ProjectManagement](https://firebase.google.com/docs/reference/admin/node/firebase-admin.projectmanagement_n.md#projectmanagementprojectmanagement)

## app.App.remoteConfig()

**Signature:**  

    remoteConfig(): remoteConfig.RemoteConfig;

**Returns:**

[remoteConfig.RemoteConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remoteconfig_n.md#remoteconfigremoteconfig)

## app.App.securityRules()

**Signature:**  

    securityRules(): securityRules.SecurityRules;

**Returns:**

[securityRules.SecurityRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.securityrules_n.md#securityrulessecurityrules)

## app.App.storage()

**Signature:**  

    storage(): storage.Storage;

**Returns:**

[storage.Storage](https://firebase.google.com/docs/reference/admin/node/firebase-admin.storage_n.md#storagestorage)