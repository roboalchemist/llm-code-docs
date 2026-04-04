# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.PersistenceSettings.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.PersistenceSettings.md.txt

# PersistenceSettings | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- PersistenceSettings

Settings that can be passed to Firestore.enablePersistence() to configure
Firestore persistence.

## Index

### Properties

- [experimentalForceOwningTab](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.PersistenceSettings#experimentalforceowningtab)
- [synchronizeTabs](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.PersistenceSettings#synchronizetabs)

## Properties

### Optional experimentalForceOwningTab

experimentalForceOwningTab: boolean  
Whether to force enable persistence for the client. This cannot be used
with `synchronizeTabs:true` and is primarily intended for use with Web
Workers. Setting this to `true` will enable persistence, but cause other
tabs using persistence to fail.

This setting may be removed in a future release. If you find yourself
using it for a specific use case or run into any issues, please tell us
about it in
<https://github.com/firebase/firebase-js-sdk/issues/983>.

### Optional synchronizeTabs

synchronizeTabs: boolean  
Whether to synchronize the in-memory state of multiple tabs. Setting this
to `true` in all open tabs enables shared access to local persistence,
shared execution of queries and latency-compensated local document updates
across all connected instances.

To enable this mode, `synchronizeTabs:true` needs to be set globally in all
active tabs. If omitted or set to 'false', `enablePersistence()` will fail
in all but the first tab.