# Source: https://firebase.google.com/docs/database/ios/offline-capabilities.md.txt

# Source: https://firebase.google.com/docs/database/web/offline-capabilities.md.txt

# Source: https://firebase.google.com/docs/database/flutter/offline-capabilities.md.txt

# Source: https://firebase.google.com/docs/database/android/offline-capabilities.md.txt

# Source: https://firebase.google.com/docs/database/web/offline-capabilities.md.txt

# Source: https://firebase.google.com/docs/database/flutter/offline-capabilities.md.txt

# Source: https://firebase.google.com/docs/database/android/offline-capabilities.md.txt

<br />

Firebase applications work even if your app temporarily loses its network connection. In addition, Firebase provides tools for persisting data locally, managing presence, and handling latency.  

## Disk Persistence

Firebase apps automatically handle temporary network interruptions. Cached data is available while offline and Firebase resends any writes when network connectivity is restored.

When you enable disk persistence, your app writes the data locally to the device so your app can maintain state while offline, even if the user or operating system restarts the app.

You can enable disk persistence with just one line of code.  

### Kotlin

```kotlin
Firebase.database.setPersistenceEnabled(true)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L18-L18
```

### Java

```java
FirebaseDatabase.getInstance().setPersistenceEnabled(true);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L23-L23
```  

### Persistence Behavior

By enabling persistence, any data that theFirebase Realtime Databaseclient would sync while online persists to disk and is available offline, even when the user or operating system restarts the app. This means your app works as it would online by using the local data stored in the cache. Listener callbacks will continue to fire for local updates.

TheFirebase Realtime Databaseclient automatically keeps a queue of all write operations that are performed while your app is offline. When persistence is enabled, this queue is also persisted to disk so all of your writes are available when the user or operating system restarts the app. When the app regains connectivity, all of the operations are sent to theFirebase Realtime Databaseserver.

If your app uses[Firebase Authentication](https://firebase.google.com/docs/auth/android/manage-users), theFirebase Realtime Databaseclient persists the user's authentication token across app restarts. If the auth token expires while your app is offline, the client pauses write operations until your app re-authenticates the user, otherwise the write operations might fail due to security rules.  

### Keeping Data Fresh

TheFirebase Realtime Databasesynchronizes and stores a local copy of the data for active listeners. In addition, you can keep specific locations in sync.  

### Kotlin

```kotlin
val scoresRef = Firebase.database.getReference("scores")
scoresRef.keepSynced(true)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L24-L25
```

### Java

```java
DatabaseReference scoresRef = FirebaseDatabase.getInstance().getReference("scores");
scoresRef.keepSynced(true);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L29-L30
```

TheFirebase Realtime Databaseclient automatically downloads the data at these locations and keeps it in sync even if the reference has no active listeners. You can turn synchronization back off with the following line of code.  

### Kotlin

```kotlin
scoresRef.keepSynced(false)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L29-L29
```

### Java

```java
scoresRef.keepSynced(false);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L34-L34
```

By default, 10MB of previously synced data is cached. This should be enough for most applications. If the cache outgrows its configured size, theFirebase Realtime Databasepurges data that has been used least recently. Data that is kept in sync is not purged from the cache.  

### Querying Data Offline

TheFirebase Realtime Databasestores data returned from a query for use when offline. For queries constructed while offline, theFirebase Realtime Databasecontinues to work for previously loaded data. If the requested data hasn't loaded, theFirebase Realtime Databaseloads data from the local cache. When network connectivity is available again, the data loads and will reflect the query.

For example, this code queries for the last four items in aFirebase Realtime Databaseof scores  

### Kotlin

```kotlin
val scoresRef = Firebase.database.getReference("scores")
scoresRef.orderByValue().limitToLast(4).addChildEventListener(object : ChildEventListener {
    override fun onChildAdded(snapshot: DataSnapshot, previousChild: String?) {
        Log.d(TAG, "The ${snapshot.key} dinosaur's score is ${snapshot.value}")
    }

    // ...
})https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L35-L50
```

### Java

```java
DatabaseReference scoresRef = FirebaseDatabase.getInstance().getReference("scores");
scoresRef.orderByValue().limitToLast(4).addChildEventListener(new ChildEventListener() {
    @Override
    public void onChildAdded(@NonNull DataSnapshot snapshot, String previousChild) {
        Log.d(TAG, "The " + snapshot.getKey() + " dinosaur's score is " + snapshot.getValue());
    }

    // ...
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L40-L60
```

Assume that the user loses connection, goes offline, and restarts the app. While still offline, the app queries for the last two items from the same location. This query will successfully return the last two items because the app had loaded all four items in the query above.  

### Kotlin

```kotlin
scoresRef.orderByValue().limitToLast(2).addChildEventListener(object : ChildEventListener {
    override fun onChildAdded(snapshot: DataSnapshot, previousChild: String?) {
        Log.d(TAG, "The ${snapshot.key} dinosaur's score is ${snapshot.value}")
    }

    // ...
})https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L54-L68
```

### Java

```java
scoresRef.orderByValue().limitToLast(2).addChildEventListener(new ChildEventListener() {
    @Override
    public void onChildAdded(@NonNull DataSnapshot snapshot, String previousChild) {
        Log.d(TAG, "The " + snapshot.getKey() + " dinosaur's score is " + snapshot.getValue());
    }

    // ...
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L64-L83
```

In the preceding example, theFirebase Realtime Databaseclient raises 'child added' events for the highest scoring two dinosaurs, by using the persisted cache. But it will not raise a 'value' event, since the app has never executed that query while online.

If the app were to request the last six items while offline, it would get 'child added' events for the four cached items straight away. When the device comes back online, theFirebase Realtime Databaseclient synchronizes with the server and gets the final two 'child added' and the 'value' events for the app.  

### Handling Transactions Offline

Any transactions that are performed while the app is offline, are queued. Once the app regains network connectivity, the transactions are sent to theRealtime Databaseserver.
|
| #### Transactions are not persisted across app restarts
|
| Even with persistence enabled, transactions are not persisted across app restarts. So you cannot rely on transactions done offline being committed to yourFirebase Realtime Database. To provide the best user experience, your app should show that a transaction has not been saved into yourFirebase Realtime Databaseyet, or make sure your app remembers them manually and executes them again after an app restart.
TheFirebase Realtime Databasehas many features for dealing with offline scenarios and network connectivity. The rest of this guide applies to your app whether or not you have persistence enabled.  

## Managing Presence

In realtime applications it is often useful to detect when clients connect and disconnect. For example, you may want to mark a user as 'offline' when their client disconnects.

Firebase Database clients provide simple primitives that you can use to write to the database when a client disconnects from the Firebase Database servers. These updates occur whether the client disconnects cleanly or not, so you can rely on them to clean up data even if a connection is dropped or a client crashes. All write operations, including setting, updating, and removing, can be performed upon a disconnection.

Here is a simple example of writing data upon disconnection by using the`onDisconnect`primitive:  

### Kotlin

```kotlin
val presenceRef = Firebase.database.getReference("disconnectmessage")
// Write a string when this client loses connection
presenceRef.onDisconnect().setValue("I disconnected!")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L74-L76
```

### Java

```java
DatabaseReference presenceRef = FirebaseDatabase.getInstance().getReference("disconnectmessage");
// Write a string when this client loses connection
presenceRef.onDisconnect().setValue("I disconnected!");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L89-L91
```  

### How onDisconnect Works

When you establish an`onDisconnect()`operation, the operation lives on theFirebase Realtime Databaseserver. The server checks security to make sure the user can perform the write event requested, and informs your app if it is invalid. The server then monitors the connection. If at any point the connection times out, or is actively closed by theRealtime Databaseclient, the server checks security a second time (to make sure the operation is still valid) and then invokes the event.

Your app can use the callback on the write operation to ensure the`onDisconnect`was correctly attached:  

### Kotlin

```kotlin
presenceRef.onDisconnect().removeValue { error, reference ->
    error?.let {
        Log.d(TAG, "could not establish onDisconnect event: ${error.message}")
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L80-L84
```

### Java

```java
presenceRef.onDisconnect().removeValue(new DatabaseReference.CompletionListener() {
    @Override
    public void onComplete(DatabaseError error, @NonNull DatabaseReference reference) {
        if (error != null) {
            Log.d(TAG, "could not establish onDisconnect event:" + error.getMessage());
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L95-L102
```

An`onDisconnect`event can also be canceled by calling`.cancel()`:  

### Kotlin

```kotlin
val onDisconnectRef = presenceRef.onDisconnect()
onDisconnectRef.setValue("I disconnected")
// ...
// some time later when we change our minds
// ...
onDisconnectRef.cancel()https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L88-L93
```

### Java

```java
OnDisconnect onDisconnectRef = presenceRef.onDisconnect();
onDisconnectRef.setValue("I disconnected");
// ...
// some time later when we change our minds
// ...
onDisconnectRef.cancel();https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L106-L111
```  

## Detecting Connection State

For many presence-related features, it is useful for your app to know when it is online or offline.Firebase Realtime Databaseprovides a special location at`/.info/connected`which is updated every time theFirebase Realtime Databaseclient's connection state changes. Here is an example:  

### Kotlin

```kotlin
val connectedRef = Firebase.database.getReference(".info/connected")
connectedRef.addValueEventListener(object : ValueEventListener {
    override fun onDataChange(snapshot: DataSnapshot) {
        val connected = snapshot.getValue(Boolean::class.java) ?: false
        if (connected) {
            Log.d(TAG, "connected")
        } else {
            Log.d(TAG, "not connected")
        }
    }

    override fun onCancelled(error: DatabaseError) {
        Log.w(TAG, "Listener was cancelled")
    }
})https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L99-L113
```

### Java

```java
DatabaseReference connectedRef = FirebaseDatabase.getInstance().getReference(".info/connected");
connectedRef.addValueEventListener(new ValueEventListener() {
    @Override
    public void onDataChange(@NonNull DataSnapshot snapshot) {
        boolean connected = snapshot.getValue(Boolean.class);
        if (connected) {
            Log.d(TAG, "connected");
        } else {
            Log.d(TAG, "not connected");
        }
    }

    @Override
    public void onCancelled(@NonNull DatabaseError error) {
        Log.w(TAG, "Listener was cancelled");
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L117-L133
```

`/.info/connected`is a boolean value which is not synchronized betweenRealtime Databaseclients because the value is dependent on the state of the client. In other words, if one client reads`/.info/connected`as false, this is no guarantee that a separate client will also read false.

On Android, Firebase automatically manages connection state to reduce bandwidth and battery usage. When a client has no active listeners, no pending write or`onDisconnect`operations, and is not explicitly disconnected by the[`goOffline`](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#goOffline())method, Firebase closes the connection after 60 seconds of inactivity.  

## Handling Latency

### Server Timestamps

TheFirebase Realtime Databaseservers provide a mechanism to insert timestamps generated on the server as data. This feature, combined with`onDisconnect`, provides an easy way to reliably make note of the time at which aRealtime Databaseclient disconnected:  

### Kotlin

```kotlin
val userLastOnlineRef = Firebase.database.getReference("users/joe/lastOnline")
userLastOnlineRef.onDisconnect().setValue(ServerValue.TIMESTAMP)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L119-L120
```

### Java

```java
DatabaseReference userLastOnlineRef = FirebaseDatabase.getInstance().getReference("users/joe/lastOnline");
userLastOnlineRef.onDisconnect().setValue(ServerValue.TIMESTAMP);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L139-L140
```  

### Clock Skew

While`firebase.database.ServerValue.TIMESTAMP`is much more accurate, and preferable for most read/write operations, it can occasionally be useful to estimate the client's clock skew with respect to theFirebase Realtime Database's servers. You can attach a callback to the location`/.info/serverTimeOffset`to obtain the value, in milliseconds, thatFirebase Realtime Databaseclients add to the local reported time (epoch time in milliseconds) to estimate the server time. Note that this offset's accuracy can be affected by networking latency, and so is useful primarily for discovering large (\> 1 second) discrepancies in clock time.  

### Kotlin

```kotlin
val offsetRef = Firebase.database.getReference(".info/serverTimeOffset")
offsetRef.addValueEventListener(object : ValueEventListener {
    override fun onDataChange(snapshot: DataSnapshot) {
        val offset = snapshot.getValue(Double::class.java) ?: 0.0
        val estimatedServerTimeMs = System.currentTimeMillis() + offset
    }

    override fun onCancelled(error: DatabaseError) {
        Log.w(TAG, "Listener was cancelled")
    }
})https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L126-L136
```

### Java

```java
DatabaseReference offsetRef = FirebaseDatabase.getInstance().getReference(".info/serverTimeOffset");
offsetRef.addValueEventListener(new ValueEventListener() {
    @Override
    public void onDataChange(@NonNull DataSnapshot snapshot) {
        double offset = snapshot.getValue(Double.class);
        double estimatedServerTimeMs = System.currentTimeMillis() + offset;
    }

    @Override
    public void onCancelled(@NonNull DatabaseError error) {
        Log.w(TAG, "Listener was cancelled");
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L146-L158
```  

## Sample Presence App

By combining disconnect operations with connection state monitoring and server timestamps, you can build a user presence system. In this system, each user stores data at a database location to indicate whether or not aRealtime Databaseclient is online. Clients set this location to true when they come online and a timestamp when they disconnect. This timestamp indicates the last time the given user was online.

Note that your app should queue the disconnect operations before a user is marked online, to avoid any race conditions in the event that the client's network connection is lost before both commands can be sent to the server.

Here is a simple user presence system:  

### Kotlin

```kotlin
// Since I can connect from multiple devices, we store each connection instance separately
// any time that connectionsRef's value is null (i.e. has no children) I am offline
val database = Firebase.database
val myConnectionsRef = database.getReference("users/joe/connections")

// Stores the timestamp of my last disconnect (the last time I was seen online)
val lastOnlineRef = database.getReference("/users/joe/lastOnline")

val connectedRef = database.getReference(".info/connected")
connectedRef.addValueEventListener(object : ValueEventListener {
    override fun onDataChange(snapshot: DataSnapshot) {
        val connected = snapshot.getValue<Boolean>() ?: false
        if (connected) {
            val con = myConnectionsRef.push()

            // When this device disconnects, remove it
            con.onDisconnect().removeValue()

            // When I disconnect, update the last time I was seen online
            lastOnlineRef.onDisconnect().setValue(ServerValue.TIMESTAMP)

            // Add this device to my connections list
            // this value could contain info about the device or a timestamp too
            con.setValue(java.lang.Boolean.TRUE)
        }
    }

    override fun onCancelled(error: DatabaseError) {
        Log.w(TAG, "Listener was cancelled at .info/connected")
    }
})https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/OfflineActivity.kt#L142-L172
```

### Java

```java
// Since I can connect from multiple devices, we store each connection instance separately
// any time that connectionsRef's value is null (i.e. has no children) I am offline
final FirebaseDatabase database = FirebaseDatabase.getInstance();
final DatabaseReference myConnectionsRef = database.getReference("users/joe/connections");

// Stores the timestamp of my last disconnect (the last time I was seen online)
final DatabaseReference lastOnlineRef = database.getReference("/users/joe/lastOnline");

final DatabaseReference connectedRef = database.getReference(".info/connected");
connectedRef.addValueEventListener(new ValueEventListener() {
    @Override
    public void onDataChange(@NonNull DataSnapshot snapshot) {
        boolean connected = snapshot.getValue(Boolean.class);
        if (connected) {
            DatabaseReference con = myConnectionsRef.push();

            // When this device disconnects, remove it
            con.onDisconnect().removeValue();

            // When I disconnect, update the last time I was seen online
            lastOnlineRef.onDisconnect().setValue(ServerValue.TIMESTAMP);

            // Add this device to my connections list
            // this value could contain info about the device or a timestamp too
            con.setValue(Boolean.TRUE);
        }
    }

    @Override
    public void onCancelled(@NonNull DatabaseError error) {
        Log.w(TAG, "Listener was cancelled at .info/connected");
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/database/app/src/main/java/com/google/firebase/referencecode/database/OfflineActivity.java#L164-L196
```