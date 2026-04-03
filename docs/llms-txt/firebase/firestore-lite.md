# Source: https://firebase.google.com/docs/firestore/solutions/firestore-lite.md.txt

<br />

Firestore is a good scalable database solution to keep data in sync across Web clients.

For many apps, Firestore's managed offline support is especially important, letting you build responsive apps that work regardless of network latency or Internet connectivity. But feature-rich SDKs come at a size cost. What does Firebase offer for apps that only need to use basic create, read, update and delete operations, and don't need managed offline support?
| **Note:** Before using Firestore Lite, be sure you understand the standard Firestore Web API and Firestore's offline capabilities as part of the full[feature set](https://firebase.google.com/docs/firestore/index.html). We recommend Firestore Lite for developers who have experience building with Firestore and can evaluate the tradeoffs of using a lightweight version.

## Solution: Firestore Lite

Firestore Lite is a lightweight, standalone REST-only Firestore SDK that supports single document fetches, query execution, and document updates, at a fraction of the regular Web SDK size. Firestore Lite omits latency compensation, offline caching, query resumption and snapshot listeners, but for particular use cases, the reductions in library size and startup time make a great tradeoff.

### Import Firestore Lite

Firestore Lite is available via npm as part of the[modular SDK](https://firebase.google.com/docs/web/learn-more#modular-version). It is thus fully modular and tree-shakeable.

The following import style is supported.  

    import { initializeApp } from "firebase/app";
    import {
       getFirestore,
       getDoc,
       updateDoc
    } from 'firebase/firestore/lite';

### API features not supported by Firestore Lite

For size and speed, Firestore Lite omits these features from the standard Firestore SDK:

- **DocumentSnapshot event handlers** . The`onSnapshot`method and`DocumentChange`,`SnapshotListenerOptions`,`SnapshotMetadata`,`SnapshotOptions`and`Unsubscribe`objects are not included.
- **Persistence helpers** . The`enableIndexedDBPersistence`,`enableMultiTabIndexedDbPersistence`, and`clearIndexedDbPersistence`methods are not included.
- **Firestore bundles** . The`loadBundle`method and related methods, and the`LoadBundleTask`and`LoadBundleTaskProgress`objects are not included.

### Implement document fetches, queries and updates

After importing Firestore Lite, you can make all of the familiar API get and update calls. The use cases for[adding data](https://firebase.google.com/docs/firestore/manage-data/add-data)and[getting data](https://firebase.google.com/docs/firestore/query-data/get-data)all apply.  

    import {
     getFirestore,
     getDoc,
     updateDoc,
     doc
    } from '@firebase/firestore/lite';

    const firestore = getFirestore(app);
    const docRef = doc(firestore, 'collection/doc');
    const docSnap = await getDoc(docRef);
    await updateDoc(docRef, "field", 'value');

## When to use Firestore Lite

It can be tricky to decide when to let go of the standard Firestore SDK's offline persistence and caching features. You should understand these features before deciding to trade them away for the lower overhead of Firestore Lite. In general, weigh these factors when deciding whether to use Firestore Lite:

- **Online status**- Firestore Lite is good for apps that do not need live updates and have connectivity.
- **Size constraints**- Firestore Lite is great if you want to reduce your overall JavaScript bundle size.