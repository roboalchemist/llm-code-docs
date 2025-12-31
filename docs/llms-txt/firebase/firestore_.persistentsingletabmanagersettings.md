# Source: https://firebase.google.com/docs/reference/js/firestore_.persistentsingletabmanagersettings.md.txt

# PersistentSingleTabManagerSettings interface

Type to configure an `PersistentSingleTabManager` instance.

**Signature:**  

    export declare interface PersistentSingleTabManagerSettings 

## Properties

|                                                                             Property                                                                              |  Type   |                                                                                                                                  Description                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [forceOwnership](https://firebase.google.com/docs/reference/js/firestore_.persistentsingletabmanagersettings.md#persistentsingletabmanagersettingsforceownership) | boolean | Whether to force-enable persistent (IndexedDB) cache for the client. This cannot be used with multi-tab synchronization and is primarily intended for use with Web Workers. Setting this to `true` will enable IndexedDB, but cause other tabs using IndexedDB cache to fail. |

## PersistentSingleTabManagerSettings.forceOwnership

Whether to force-enable persistent (IndexedDB) cache for the client. This cannot be used with multi-tab synchronization and is primarily intended for use with Web Workers. Setting this to `true` will enable IndexedDB, but cause other tabs using IndexedDB cache to fail.

**Signature:**  

    forceOwnership?: boolean;