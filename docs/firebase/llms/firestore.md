# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore.md.txt

# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore.md.txt

# Source: https://firebase.google.com/docs/reference/js/firestore.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore.md.txt

# Source: https://firebase.google.com/docs/firestore.md.txt

# Cloud Firestore

plat_iosplat_androidplat_webplat_flutterplat_cppplat_unityplat_nodeplat_javaplat_pythonplat_go  
Use our flexible, scalable NoSQL cloud database, built onGoogle Cloudinfrastructure, to store and sync data for client- and server-side development.  

Cloud Firestoreis a flexible, scalable database for mobile, web, and server development from Firebase andGoogle Cloud. LikeFirebase Realtime Database, it keeps your data in sync across client apps through realtime listeners and offers offline support for mobile and web so you can build responsive apps that work regardless of network latency or Internet connectivity.Cloud Firestorealso offers seamless integration with other Firebase andGoogle Cloudproducts, including Cloud Functions.

Cloud Firestoreis available in two editions to meet different needs.[Learn about the editions](https://firebase.google.com/docs/firestore/editions)

## Key capabilities

|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Flexibility           | TheCloud Firestoredata model supports flexible, hierarchical data structures. Store your data in documents, organized into collections. Documents can contain complex nested objects in addition to subcollections.                                                                                               |
| Expressive querying   | InCloud Firestore, you can use queries to retrieve individual, specific documents or to retrieve all the documents in a collection that match your query parameters. Your queries can include multiple, chained filters and combine filtering and sorting.                                                        |
| Realtime updates      | LikeRealtime Database,Cloud Firestoreuses data synchronization to update data on any connected device. However, it's also designed to make simple, one-time fetch queries efficiently.                                                                                                                            |
| Offline support       | Cloud Firestorecaches data that your app is actively using, so the app can write, read, listen to, and query data even if the device is offline. When the device comes back online,Cloud Firestoresynchronizes any local changes back toCloud Firestore.                                                          |
| Designed to scale     | Cloud Firestorebrings you the best ofGoogle Cloud's powerful infrastructure: automatic multi-region data replication, strong consistency guarantees, atomic batch operations, and ACID transaction support. We've designedCloud Firestoreto handle the toughest database workloads from the world's biggest apps. |
| MongoDB compatibility | Cloud Firestoreoffers a MongoDB-compatible API. You can use existing MongoDB application code, drivers, tools, and the open-source ecosystem of MongoDB integrations withCloud Firestorein the[Enterprise edition.](https://firebase.google.com/docs/firestore/enterprise/mongodb-compatibility-overview)         |

## How does it work?

![](https://firebase.google.com/static/docs/firestore/images/structure-data.png)

Cloud Firestoreis a cloud-hosted, NoSQL database that your Apple, Android, and web apps can access directly via native SDKs.Cloud Firestoreis also available in native Node.js, Java, Python, Unity, C++ and Go SDKs, in addition to REST and RPC APIs.

FollowingCloud Firestore's document data model, you store data that contain fields mapping to values. These documents are stored in collections, which are containers for your documents that you can use to organize your data and build queries. Documents support many different[data types](https://firebase.google.com/docs/firestore/manage-data/data-types), from simple strings and numbers, to complex, nested objects. You can also create subcollections within documents and build hierarchical data structures that scale as your database grows. TheCloud Firestore[data model](https://firebase.google.com/docs/firestore/data-model)supports whatever data structure works best for your app.

Additionally, querying inCloud Firestoreis expressive, efficient, and flexible. Create shallow queries to retrieve data at the document level without needing to retrieve the entire collection, or any nested subcollections. Add sorting, filtering, and limits to your queries or cursors to paginate your results. To keep data in your apps current, without retrieving your entire database each time an update happens, add realtime listeners. Adding realtime listeners to your app notifies you with a data snapshot whenever the data your client apps are listening to changes, retrieving only the new changes.

Protect access to your data inCloud FirestorewithFirebase AuthenticationandCloud FirestoreSecurity Rulesfor Android, Apple platforms, and JavaScript, or Identity and Access Management (IAM) for server-side languages.

## Implementation path

|---|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Integrate theCloud FirestoreSDKs | Quickly include clients via Gradle, CocoaPods, or a script include.                                                                              |
|   | Secure your data                 | UseCloud FirestoreSecurity Rulesor Identity and Access Management (IAM) to secure your data for mobile/web and server development, respectively. |
|   | Add Data                         | Create documents and collections in your database.                                                                                               |
|   | Get Data                         | Create queries or use realtime listeners to retrieve data from the database.                                                                     |

## Next steps

- [Get started](https://firebase.google.com/docs/firestore/quickstart)withCloud Firestore--- set up your database, then add data and start reading it.
- Learn more about theCloud Firestore[data model](https://firebase.google.com/docs/firestore/data-model).
- Explore the[differences betweenRealtime DatabaseandCloud Firestore](https://firebase.google.com/docs/firestore/rtdb-vs-firestore).