# Source: https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.testenvironmentconfig.md.txt

Configuration of the unit testing environment, including emulators.

<br />

**Signature:**  

    export interface TestEnvironmentConfig 

## Properties

|                                                                               Property                                                                               |                                                                        Type                                                                         |                                                                                                                                       Description                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [database](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.testenvironmentconfig.md#testenvironmentconfigdatabase)   | [EmulatorConfig](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#emulatorconfig)                 | The Database emulator. Its host and port can also be discovered automatically through the hub (see field "hub") or specified via the environment variable FIREBASE_DATABASE_EMULATOR_HOST.                                                                                              |
| [firestore](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.testenvironmentconfig.md#testenvironmentconfigfirestore) | [EmulatorConfig](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#emulatorconfig)                 | The Firestore emulator. Its host and port can also be discovered automatically through the hub (see field "hub") or specified via the environment variable FIRESTORE_EMULATOR_HOST.                                                                                                     |
| [hub](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.testenvironmentconfig.md#testenvironmentconfighub)             | [HostAndPort](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.hostandport.md#hostandport_interface) | The Firebase Emulator hub. Can also be specified via the environment variable FIREBASE_EMULATOR_HUB. If specified either way, other running emulators can be automatically discovered, and thus do not to be explicity specified.                                                       |
| [projectId](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.testenvironmentconfig.md#testenvironmentconfigprojectid) | string                                                                                                                                              | The project ID of the test environment. Can also be specified via the environment variable GCLOUD_PROJECT.A "demo-\*" project ID is strongly recommended, especially for unit testing. See: https://firebase.google.com/docs/emulator-suite/connect_firestore#choose_a_firebase_project |
| [storage](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.testenvironmentconfig.md#testenvironmentconfigstorage)     | [EmulatorConfig](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.md#emulatorconfig)                 | The Storage emulator. Its host and port can also be discovered automatically through the hub (see field "hub") or specified via the environment variable FIREBASE_STORAGE_EMULATOR_HOST.                                                                                                |

## TestEnvironmentConfig.database

The Database emulator. Its host and port can also be discovered automatically through the hub (see field "hub") or specified via the environment variable FIREBASE_DATABASE_EMULATOR_HOST.

**Signature:**  

    database?: EmulatorConfig;

## TestEnvironmentConfig.firestore

The Firestore emulator. Its host and port can also be discovered automatically through the hub (see field "hub") or specified via the environment variable FIRESTORE_EMULATOR_HOST.

**Signature:**  

    firestore?: EmulatorConfig;

## TestEnvironmentConfig.hub

The Firebase Emulator hub. Can also be specified via the environment variable FIREBASE_EMULATOR_HUB. If specified either way, other running emulators can be automatically discovered, and thus do not to be explicity specified.

**Signature:**  

    hub?: HostAndPort;

## TestEnvironmentConfig.projectId

The project ID of the test environment. Can also be specified via the environment variable GCLOUD_PROJECT.

A "demo-\*" project ID is strongly recommended, especially for unit testing. See: https://firebase.google.com/docs/emulator-suite/connect_firestore#choose_a_firebase_project

**Signature:**  

    projectId?: string;

## TestEnvironmentConfig.storage

The Storage emulator. Its host and port can also be discovered automatically through the hub (see field "hub") or specified via the environment variable FIREBASE_STORAGE_EMULATOR_HOST.

**Signature:**  

    storage?: EmulatorConfig;