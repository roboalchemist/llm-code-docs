# Source: https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md.txt

## Functions

| Function | Description |
|---|---|
| [assertFails(pr)](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#assertfails) | Assert the promise to be rejected with a "permission denied" error.Useful to assert a certain request to be denied by Security Rules. See example below. This function recognizes permission-denied errors from Database, Firestore, and Storage JS SDKs. |
| [assertSucceeds(pr)](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#assertsucceeds) | Assert the promise to be rejected with a "permission denied" error.This is a no-op function returning the passed promise as-is, but can be used for documentational purposes in test code to emphasize that a certain request should succeed (e.g. allowed by rules). |
| [initializeTestEnvironment(config)](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#initializetestenvironment) | Initializes a test environment for rules unit testing. Call this function first for test setup.Requires emulators to be running. This function tries to discover those emulators via environment variables or through the Firebase Emulator hub if hosts and ports are unspecified. It is strongly recommended to specify security rules for emulators used for testing. See minimal example below. |
| [withFunctionTriggersDisabled(fn)](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#withfunctiontriggersdisabled) | Run a setup function with background Cloud Functions triggers disabled. This can be used to import data into the Realtime Database or Cloud Firestore emulator without triggering locally emulated Cloud Functions.This method only works with Firebase CLI version 8.13.0 or higher. This overload works only if the Emulator hub host:port is specified by the environment variable FIREBASE_EMULATOR_HUB. |
| [withFunctionTriggersDisabled(hub, fn)](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#withfunctiontriggersdisabled) | Run a setup function with background Cloud Functions triggers disabled. This can be used to import data into the Realtime Database or Cloud Firestore emulator without triggering locally emulated Cloud Functions.This method only works with Firebase CLI version 8.13.0 or higher. The Emulator hub must be running, which host and port are specified in this overload. |

## Interfaces

| Interface | Description |
|---|---|
| [HostAndPort](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.hostandport.md#hostandport_interface) | An object containing the hostname and port number of an emulator. |
| [RulesTestContext](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestcontext.md#rulestestcontext_interface) | A test context that represents a client. Can be used to access emulators for rules unit testing. |
| [RulesTestEnvironment](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironment_interface) | An object used to control the rules unit test environment. Can be used to create RulesTestContext for different authentication situations. |
| [TestEnvironmentConfig](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.testenvironmentconfig.md#testenvironmentconfig_interface) | Configuration of the unit testing environment, including emulators. |

## Type Aliases

| Type Alias | Description |
|---|---|
| [EmulatorConfig](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#emulatorconfig) | Configuration for a given emulator. |
| [TokenOptions](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#tokenoptions) | More options for the mock user token to be used for testing, including developer-specfied custom claims or optional overrides for Firebase Auth token payloads. |

## assertFails()

Assert the promise to be rejected with a "permission denied" error.

Useful to assert a certain request to be denied by Security Rules. See example below. This function recognizes permission-denied errors from Database, Firestore, and Storage JS SDKs.

**Signature:**

    export declare function assertFails(pr: Promise<any>): Promise<any>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| pr | Promise\<any\> | the promise to be asserted |

**Returns:**

Promise\<any\>

a Promise that is fulfilled if pr is rejected with "permission denied". If pr is rejected with any other error or resolved, the returned promise rejects.

### Example

    const unauthed = testEnv.unauthenticatedContext();
    await assertFails(getDoc(unauthed.firestore(), '/private/doc'), { ... });

## assertSucceeds()

Assert the promise to be successful.

This is a no-op function returning the passed promise as-is, but can be used for documentational purposes in test code to emphasize that a certain request should succeed (e.g. allowed by rules).

**Signature:**

    export declare function assertSucceeds<T>(pr: Promise<T>): Promise<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| pr | Promise\<T\> |   |

**Returns:**

Promise\<T\>

### Example

    const alice = testEnv.authenticatedContext('alice');
    await assertSucceeds(getDoc(alice.firestore(), '/doc/readable/by/alice'), { ... });

## initializeTestEnvironment()

Initializes a test environment for rules unit testing. Call this function first for test setup.

Requires emulators to be running. This function tries to discover those emulators via environment variables or through the Firebase Emulator hub if hosts and ports are unspecified. It is strongly recommended to specify security rules for emulators used for testing. See minimal example below.

**Signature:**

    export declare function initializeTestEnvironment(config: TestEnvironmentConfig): Promise<RulesTestEnvironment>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| config | [TestEnvironmentConfig](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.testenvironmentconfig.md#testenvironmentconfig_interface) | the configuration for emulators. Most fields are optional if they can be discovered |

**Returns:**

Promise\<[RulesTestEnvironment](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.rulestestenvironment.md#rulestestenvironment_interface)\>

a promise that resolves with an environment ready for testing, or rejects on error.

### Example

    const testEnv = await initializeTestEnvironment({
      firestore: {
        rules: fs.readFileSync("/path/to/firestore.rules", "utf8"), // Load rules from file
        // host and port can be omitted if they can be discovered from the hub.
      },
      // ...
    });

## withFunctionTriggersDisabled()

Run a setup function with background Cloud Functions triggers disabled. This can be used to import data into the Realtime Database or Cloud Firestore emulator without triggering locally emulated Cloud Functions.

This method only works with Firebase CLI version 8.13.0 or higher. This overload works only if the Emulator hub host:port is specified by the environment variable FIREBASE_EMULATOR_HUB.

**Signature:**

    export declare function withFunctionTriggersDisabled<TResult>(fn: () => TResult | Promise<TResult>): Promise<TResult>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| fn | () =\> TResult \| Promise\<TResult\> | a function which may be sync or async (returns a promise) |

**Returns:**

Promise\<TResult\>

## withFunctionTriggersDisabled()

Run a setup function with background Cloud Functions triggers disabled. This can be used to import data into the Realtime Database or Cloud Firestore emulator without triggering locally emulated Cloud Functions.

This method only works with Firebase CLI version 8.13.0 or higher. The Emulator hub must be running, which host and port are specified in this overload.

**Signature:**

    export declare function withFunctionTriggersDisabled<TResult>(hub: {
        host: string;
        port: number;
    }, fn: () => TResult | Promise<TResult>): Promise<TResult>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| hub | { host: string; port: number; } | the host and port of the Emulator Hub (ex: `{host: 'localhost', port: 4400}`) |
| fn | () =\> TResult \| Promise\<TResult\> | a function which may be sync or async (returns a promise) |

**Returns:**

Promise\<TResult\>

## EmulatorConfig

Configuration for a given emulator.

**Signature:**

    export declare type EmulatorConfig = {
        rules?: string;
    } & (HostAndPort | {});

## TokenOptions

More options for the mock user token to be used for testing, including developer-specfied custom claims or optional overrides for Firebase Auth token payloads.

**Signature:**

    export declare type TokenOptions = {
        iat?: number;
        exp?: number;
        auth_time?: number;
        provider_id?: 'anonymous';
        email?: string;
        email_verified?: boolean;
        phone_number?: string;
        name?: string;
        picture?: string;
        firebase?: {
            sign_in_provider: FirebaseSignInProvider;
            identities?: {
                [provider in FirebaseSignInProvider]?: string[];
            };
        };
        aud?: string;
        iss?: string;
        [claim: string]: unknown;
        uid?: never;
        sub?: never;
        user_id?: never;
    };