# Source: https://firebase.google.com/docs/reference/js/firestore_.persistencesettings.md.txt

# PersistenceSettings interface

Settings that can be passed to `enableIndexedDbPersistence()` to configure Firestore persistence.

Persistence cannot be used in a Node.js environment.

**Signature:**  

    export declare interface PersistenceSettings 

## Properties

|                                                              Property                                                               |  Type   |                                                                                                                        Description                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [forceOwnership](https://firebase.google.com/docs/reference/js/firestore_.persistencesettings.md#persistencesettingsforceownership) | boolean | Whether to force enable persistence for the client. This cannot be used with multi-tab synchronization and is primarily intended for use with Web Workers. Setting this to `true` will enable persistence, but cause other tabs using persistence to fail. |

## PersistenceSettings.forceOwnership

Whether to force enable persistence for the client. This cannot be used with multi-tab synchronization and is primarily intended for use with Web Workers. Setting this to `true` will enable persistence, but cause other tabs using persistence to fail.

**Signature:**  

    forceOwnership?: boolean;