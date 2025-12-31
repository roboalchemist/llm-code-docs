# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/database.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/database.md.txt

# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/database.md.txt

# Source: https://firebase.google.com/docs/reference/security/database.md.txt

# Source: https://firebase.google.com/docs/reference/rest/database.md.txt

# Source: https://firebase.google.com/docs/reference/js/database.md.txt

# Source: https://firebase.google.com/docs/database.md.txt

# Firebase Realtime Database

plat_iosplat_androidplat_webplat_flutterplat_cppplat_unity  
Store and sync data with our NoSQL cloud database. Data is synced across all clients in realtime, and remains available when your app goes offline.  

### Realtime Database

### Cloud Firestore

Preferred  
TheFirebase Realtime Databaseis a cloud-hosted database. Data is stored as JSON and synchronized in realtime to every connected client. When you build cross-platform apps with our Apple platforms, Android, and JavaScript SDKs, all of your clients share oneRealtime Databaseinstance and automatically receive updates with the newest data.

Alternatively, consider trying[Cloud Firestore](https://firebase.google.com/docs/firestore)for modern applications requiring richer data models, queryability, scalability and higher availability.

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/database/ios/start)[Android](https://firebase.google.com/docs/database/android/start)[Web](https://firebase.google.com/docs/database/web/start)[Flutter](https://firebase.google.com/docs/database/flutter/start)[Unity](https://firebase.google.com/docs/database/unity/start)[C++](https://firebase.google.com/docs/database/cpp/start)[Admin](https://firebase.google.com/docs/database/admin/start)[REST API](https://firebase.google.com/docs/database/rest/start)  

## Key capabilities

|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Realtime                        | Instead of typical HTTP requests, theFirebase Realtime Databaseuses data synchronization---every time data changes, any connected device receives that update within milliseconds. Provide collaborative and immersive experiences without thinking about networking code.                                                                                                                                                                             |
| Offline                         | Firebase apps remain responsive even when offline because theFirebase Realtime DatabaseSDK persists your data to disk. Once connectivity is reestablished, the client device receives any changes it missed, synchronizing it with the current server state.                                                                                                                                                                                           |
| Accessible from Client Devices  | TheFirebase Realtime Databasecan be accessed directly from a mobile device or web browser; there's no need for an application server. Security and data validation are available through theFirebase Realtime DatabaseSecurity Rules, expression-based rules that are executed when data is read or written.                                                                                                                                           |
| Scale across multiple databases | WithFirebase Realtime Databaseon the Blaze pricing plan, you can support your app's data needs at scale by splitting your data across multiple database instances in the same Firebase project. Streamline authentication withFirebase Authenticationon your project and authenticate users across your database instances. Control access to the data in each database with customFirebase Realtime DatabaseSecurity Rulesfor each database instance. |

## How does it work?

TheFirebase Realtime Databaselets you build rich, collaborative applications by allowing secure access to the database directly from client-side code. Data is persisted locally, and even while offline, realtime events continue to fire, giving the end user a responsive experience. When the device regains connection, theRealtime Databasesynchronizes the local data changes with the remote updates that occurred while the client was offline, merging any conflicts automatically.

TheRealtime Databaseprovides a flexible, expression-based rules language, calledFirebase Realtime DatabaseSecurity Rules, to define how your data should be structured and when data can be read from or written to. When integrated withFirebase Authentication, developers can define who has access to what data, and how they can access it.

TheRealtime Databaseis a NoSQL database and as such has different optimizations and capabilities compared to a relational database. TheRealtime DatabaseAPI is designed to only allow operations that can be executed quickly. This lets you build a great realtime experience that can serve millions of users without compromising on responsiveness. Because of this, it is important to think about how users need to access your data and then[structure it accordingly](https://firebase.google.com/docs/database/web/structure-data).

## Implementation path

|---|---------------------------------------------|------------------------------------------------------------------------------------------------------------|
|   | Integrate theFirebase Realtime DatabaseSDKs | Quickly include clients using Gradle, CocoaPods, or a script include.                                      |
|   | CreateRealtime DatabaseReferences           | Reference your JSON data, such as "users/user:1234/phone_number" to set data or subscribe to data changes. |
|   | Set Data and Listen for Changes             | Use these references to write data or subscribe to changes.                                                |
|   | Enable Offline Persistence                  | Allow data to be written to the device's local disk so it can be available while offline.                  |
|   | Secure your data                            | UseFirebase Realtime DatabaseSecurity Rules to secure your data.                                           |

## Store other types of data

- [Cloud Firestore](https://firebase.google.com/docs/firestore)is a flexible, scalable database for mobile, web, and server development from Firebase and Google Cloud. To learn more about the differences between database options, see[Choose a database:Cloud FirestoreorRealtime Database](https://firebase.google.com/docs/firestore/rtdb-vs-firestore).
- [Firebase Remote Config](https://firebase.google.com/docs/remote-config)stores developer specified key-value pairs to change the behavior and appearance of your app without requiring users to download an update.
- [Firebase Hosting](https://firebase.google.com/docs/hosting)hosts the HTML, CSS, and JavaScript for your website as well as other developer-provided assets like graphics, fonts, and icons.
- [Cloud Storage](https://firebase.google.com/docs/storage)stores files such as images, videos, and audio as well as other user-generated content.

## Next steps:

- Set data and listen for changes using the[Apple platforms](https://firebase.google.com/docs/database/ios/start),[Android](https://firebase.google.com/docs/database/android/start),[Web](https://firebase.google.com/docs/database/web/start),[Admin](https://firebase.google.com/docs/database/admin/start)SDKs, or the[REST API](https://firebase.google.com/docs/database/rest/start).
- AddFirebase Realtime Databaseto your[Apple](https://firebase.google.com/docs/database/ios/start),[Android](https://firebase.google.com/docs/database/android/start), or[Web](https://firebase.google.com/docs/database/web/start)app.
- Learn about how to secure your files using[Firebase Realtime DatabaseSecurity Rules](https://firebase.google.com/docs/database/security).