# Source: https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md.txt

An object used to control the rules unit test environment. Can be used to create RulesTestContext for different authentication situations.

<br />

**Signature:**  

    export interface RulesTestEnvironment 

## Properties

|                                                                              Property                                                                              |                                                                                                                                                                                                                                               Type                                                                                                                                                                                                                                               |                                         Description                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [emulators](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironmentemulators) | { database?:[HostAndPort](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.hostandport.md#hostandport_interface); firestore?:[HostAndPort](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.hostandport.md#hostandport_interface); storage?:[HostAndPort](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.hostandport.md#hostandport_interface); } | A readonly copy of the emulator config specified or discovered at test environment creation. |
| [projectId](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironmentprojectid) | string                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The project ID specified or discovered at test environment creation.                         |

## Methods

|                                                                                                     Method                                                                                                      |                                                                                                                                                                 Description                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [authenticatedContext(user_id, tokenOptions)](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironmentauthenticatedcontext) | Create a`RulesTestContext`which behaves like an authenticated Firebase Auth user.Requests created via the returned context will have a mock Firebase Auth token attached.                                                                                                                                                                    |
| [cleanup()](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironmentcleanup)                                                | At the very end of your test code, call the cleanup function. Destroy all RulesTestContexts created in test environment and clean up the underlying resources, allowing a clean exit.This method does not change the state in emulators in any way. To reset data between tests, see`clearDatabase()`,`clearFirestore()`and`clearStorage()`. |
| [clearDatabase()](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironmentcleardatabase)                                    | Clear all data in the Realtime Database emulator namespace.                                                                                                                                                                                                                                                                                  |
| [clearFirestore()](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironmentclearfirestore)                                  | Clear data in the Firestore that belongs to the`projectId`in the Firestore emulator.                                                                                                                                                                                                                                                         |
| [clearStorage()](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironmentclearstorage)                                      | Clear Storage files and metadata in all buckets in the Storage emulator.                                                                                                                                                                                                                                                                     |
| [unauthenticatedContext()](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironmentunauthenticatedcontext)                  | Create a`RulesTestContext`which behaves like client that is NOT logged in via Firebase Auth.Requests created via the returned context will not have Firebase Auth tokens attached.                                                                                                                                                           |
| [withSecurityRulesDisabled(callback)](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironmentwithsecurityrulesdisabled)    |                                                                                                                                                                                                                                                                                                                                              |

## RulesTestEnvironment.emulators

A readonly copy of the emulator config specified or discovered at test environment creation.

**Signature:**  

    readonly emulators: {
            database?: HostAndPort;
            firestore?: HostAndPort;
            storage?: HostAndPort;
        };

## RulesTestEnvironment.projectId

The project ID specified or discovered at test environment creation.

**Signature:**  

    readonly projectId: string;

## RulesTestEnvironment.authenticatedContext()

Create a`RulesTestContext`which behaves like an authenticated Firebase Auth user.

Requests created via the returned context will have a mock Firebase Auth token attached.

**Signature:**  

    authenticatedContext(user_id: string, tokenOptions?: TokenOptions): RulesTestContext;

### Parameters

|  Parameter   |                                                              Type                                                               |                                   Description                                    |
|--------------|---------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| user_id      | string                                                                                                                          | the User ID of the user. Specifies the value of "user_id" and "sub" on the token |
| tokenOptions | [TokenOptions](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#tokenoptions) | custom claims or overrides for Firebase Auth token payloads                      |

**Returns:**

[RulesTestContext](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestcontext.md#rulestestcontext_interface)

### Example

    const alice = testEnv.authenticatedContext('alice');
    await assertSucceeds(getDoc(alice.firestore(), '/doc/readable/by/alice'), { ... });

## RulesTestEnvironment.cleanup()

At the very end of your test code, call the cleanup function. Destroy all RulesTestContexts created in test environment and clean up the underlying resources, allowing a clean exit.

This method does not change the state in emulators in any way. To reset data between tests, see`clearDatabase()`,`clearFirestore()`and`clearStorage()`.

**Signature:**  

    cleanup(): Promise<void>;

**Returns:**

Promise\<void\>

## RulesTestEnvironment.clearDatabase()

Clear all data in the Realtime Database emulator namespace.

**Signature:**  

    clearDatabase(): Promise<void>;

**Returns:**

Promise\<void\>

## RulesTestEnvironment.clearFirestore()

Clear data in the default Firestore database for`projectId`in the Firestore emulator.

**Signature:**  

    clearFirestore(): Promise<void>;

**Returns:**

Promise\<void\>

## RulesTestEnvironment.clearStorage()

Clear Storage files and metadata in the active bucket in the Storage emulator.

**Signature:**  

    clearStorage(): Promise<void>;

**Returns:**

Promise\<void\>

## RulesTestEnvironment.unauthenticatedContext()

Create a`RulesTestContext`which behaves like client that is NOT logged in via Firebase Auth.

Requests created via the returned context will not have Firebase Auth tokens attached.

**Signature:**  

    unauthenticatedContext(): RulesTestContext;

**Returns:**

[RulesTestContext](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestcontext.md#rulestestcontext_interface)

### Example

    const unauthed = testEnv.unauthenticatedContext();
    await assertFails(getDoc(unauthed.firestore(), '/private/doc'), { ... });

## RulesTestEnvironment.withSecurityRulesDisabled()

**Signature:**  

    withSecurityRulesDisabled(callback: (context: RulesTestContext) => Promise<void>): Promise<void>;

### Parameters

| Parameter |                                                                                               Type                                                                                               | Description |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| callback  | (context:[RulesTestContext](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestcontext.md#rulestestcontext_interface)) =\> Promise\<void\> |             |

**Returns:**

Promise\<void\>