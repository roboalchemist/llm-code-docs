# Source: https://firebase.google.com/docs/database/web/read-and-write.md.txt

# Source: https://firebase.google.com/docs/database/ios/read-and-write.md.txt

# Source: https://firebase.google.com/docs/database/flutter/read-and-write.md.txt

# Source: https://firebase.google.com/docs/database/android/read-and-write.md.txt

# Source: https://firebase.google.com/docs/database/web/read-and-write.md.txt

# Source: https://firebase.google.com/docs/database/ios/read-and-write.md.txt

# Source: https://firebase.google.com/docs/database/flutter/read-and-write.md.txt

# Source: https://firebase.google.com/docs/database/android/read-and-write.md.txt

<br />

This document covers the basics of reading and writing Firebase data.

Firebase data is written to a`FirebaseDatabase`reference and retrieved by attaching an asynchronous listener to the reference. The listener is triggered once for the initial state of the data and again anytime the data changes.
| **Note:** By default, read and write access to your database is restricted so only authenticated users can read or write data. To get started without setting up[Authentication](https://firebase.google.com/docs/auth), you can[configure your rules for public access](https://firebase.google.com/docs/rules/basics#default_rules_locked_mode). This does make your database open to anyone, even people not using your app, so be sure to restrict your database again when you set up authentication.

## (Optional) Prototype and test withFirebase Local Emulator Suite

Before talking about how your app reads from and writes toRealtime Database, let's introduce a set of tools you can use to prototype and testRealtime Databasefunctionality:Firebase Local Emulator Suite. If you're trying out different data models, optimizing your security rules, or working to find the most cost-effective way to interact with the back-end, being able to work locally without deploying live services can be a great idea.

ARealtime Databaseemulator is part of theLocal Emulator Suite, which enables your app to interact with your emulated database content and config, as well as optionally your emulated project resources (functions, other databases, and security rules).

Using theRealtime Databaseemulator involves just a few steps:

1. Adding a line of code to your app's test config to connect to the emulator.
2. From the root of your local project directory, running`firebase emulators:start`.
3. Making calls from your app's prototype code using aRealtime Databaseplatform SDK as usual, or using theRealtime DatabaseREST API.

A detailed[walkthrough involvingRealtime DatabaseandCloud Functions](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=RTDB)is available. You should also have a look at the[Local Emulator Suiteintroduction](https://firebase.google.com/docs/emulator-suite).

## Get a DatabaseReference

To read or write data from the database, you need an instance of`DatabaseReference`:  

### Kotlin

```kotlin
private lateinit var database: DatabaseReference
// ...
database = Firebase.database.reference  
https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/ReadAndWriteSnippets.kt#L27-L27
```

### Java

```java
private DatabaseReference mDatabase;
// ...
mDatabase = FirebaseDatabase.getInstance().getReference();https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/ReadAndWriteSnippets.java#L33-L33
```

## Write data

### Basic write operations

For basic write operations, you can use`setValue()`to save data to a specified reference, replacing any existing data at that path. You can use this method to:

- Pass types that correspond to the available JSON types as follows:
  - `String`
  - `Long`
  - `Double`
  - `Boolean`
  - `Map<String, Object>`
  - `List<Object>`
- Pass a custom Java object, if the class that defines it has a default constructor that takes no arguments and has public getters for the properties to be assigned.

If you use a Java object, the contents of your object are automatically mapped to child locations in a nested fashion. Using a Java object also typically makes your code more readable and easier to maintain. For example, if you have an app with a basic user profile, your`User`object might look as follows:  

### Kotlin

```kotlin
@IgnoreExtraProperties
data class User(val username: String? = null, val email: String? = null) {
    // Null default values create a no-argument default constructor, which is needed
    // for deserialization from a DataSnapshot.
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/models/User.kt#L6-L10
```

### Java

```java
@IgnoreExtraProperties
public class User {

    public String username;
    public String email;

    public User() {
        // Default constructor required for calls to DataSnapshot.getValue(User.class)
    }

    public User(String username, String email) {
        this.username = username;
        this.email = email;
    }

}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/models/User.java#L6-L21
```

You can add a user with`setValue()`as follows:  

### Kotlin

```kotlin
fun writeNewUser(userId: String, name: String, email: String) {
    val user = User(name, email)

    database.child("users").child(userId).setValue(user)
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/ReadAndWriteSnippets.kt#L32-L36
```

### Java

```java
public void writeNewUser(String userId, String name, String email) {
    User user = new User(name, email);

    mDatabase.child("users").child(userId).setValue(user);
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/ReadAndWriteSnippets.java#L38-L42
```

Using`setValue()`in this way overwrites data at the specified location, including any child nodes. However, you can still update a child without rewriting the entire object. If you want to allow users to update their profiles you could update the username as follows:  

### Kotlin

```kotlin
database.child("users").child(userId).child("username").setValue(name)
```

### Java

```java
mDatabase.child("users").child(userId).child("username").setValue(name);
```

## Read data

### Read data with persistent listeners

To read data at a path and listen for changes, use the`addValueEventListener()`method to add a`ValueEventListener`to a`DatabaseReference`.

|       Listener       |  Event callback  |                         Typical usage                         |
|----------------------|------------------|---------------------------------------------------------------|
| `ValueEventListener` | `onDataChange()` | Read and listen for changes to the entire contents of a path. |

You can use the`onDataChange()`method to read a static snapshot of the contents at a given path, as they existed at the time of the event. This method is triggered once when the listener is attached and again every time the data, including children, changes. The event callback is passed a snapshot containing all data at that location, including child data. If there is no data, the snapshot will return`false`when you call`exists()`and`null`when you call`getValue()`on it.
| **Important:** The`onDataChange()`method is called every time data is changed at the specified database reference, including changes to children. To limit the size of your snapshots, attach only at the highest level needed for watching changes. For example, attaching a listener to the root of your database is not recommended.

The following example demonstrates a social blogging application retrieving the details of a post from the database:  

### Kotlin

```kotlin
val postListener = object : ValueEventListener {
    override fun onDataChange(dataSnapshot: DataSnapshot) {
        // Get Post object and use the values to update the UI
        val post = dataSnapshot.getValue<Post>()
        // ...
    }

    override fun onCancelled(databaseError: DatabaseError) {
        // Getting Post failed, log a message
        Log.w(TAG, "loadPost:onCancelled", databaseError.toException())
    }
}
postReference.addValueEventListener(postListener)https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/ReadAndWriteSnippets.kt#L57-L69
```

### Java

```java
ValueEventListener postListener = new ValueEventListener() {
    @Override
    public void onDataChange(DataSnapshot dataSnapshot) {
        // Get Post object and use the values to update the UI
        Post post = dataSnapshot.getValue(Post.class);
        // ..
    }

    @Override
    public void onCancelled(DatabaseError databaseError) {
        // Getting Post failed, log a message
        Log.w(TAG, "loadPost:onCancelled", databaseError.toException());
    }
};
mPostReference.addValueEventListener(postListener);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/ReadAndWriteSnippets.java#L69-L83
```

The listener receives a`DataSnapshot`that contains the data at the specified location in the database at the time of the event. Calling`getValue()`on a snapshot returns the Java object representation of the data. If no data exists at the location, calling`getValue()`returns`null`.

In this example,`ValueEventListener`also defines the`onCancelled()`method that is called if the read is canceled. For example, a read can be canceled if the client doesn't have permission to read from a Firebase database location. This method is passed a`DatabaseError`object indicating why the failure occurred.

### Read data once

#### Read once using get()

The SDK is designed to manage interactions with database servers whether your app is online or offline.

Generally, you should use the`ValueEventListener`techniques described above to read data to get notified of updates to the data from the backend. The listener techniques reduce your usage and billing, and are optimized to give your users the best experience as they go online and offline.

If you need the data only once, you can use`get()`to get a snapshot of the data from the database. If for any reason`get()`is unable to return the server value, the client will probe the local storage cache and return an error if the value is still not found.

Unnecessary use of`get()`can increase use of bandwidth and lead to loss of performance, which can be prevented by using a realtime listener as shown above.  

### Kotlin

    mDatabase.child("users").child(userId).get().addOnSuccessListener {
        Log.i("firebase", "Got value ${it.value}")
    }.addOnFailureListener{
        Log.e("firebase", "Error getting data", it)
    }

### Java

    mDatabase.child("users").child(userId).get().addOnCompleteListener(new OnCompleteListener<DataSnapshot>() {
        @Override
        public void onComplete(@NonNull Task<DataSnapshot> task) {
            if (!task.isSuccessful()) {
                Log.e("firebase", "Error getting data", task.getException());
            }
            else {
                Log.d("firebase", String.valueOf(task.getResult().getValue()));
            }
        }
    });

#### Read once using a listener

In some cases you may want the value from the local cache to be returned immediately, instead of checking for an updated value on the server. In those cases you can use`addListenerForSingleValueEvent`to get the data from the local disk cache immediately.

This is useful for data that only needs to be loaded once and isn't expected to change frequently or require active listening. For instance, the blogging app in the previous examples uses this method to load a user's profile when they begin authoring a new post.

## Updating or deleting data

### Update specific fields

To simultaneously write to specific children of a node without overwriting other child nodes, use the`updateChildren()`method.

<>When calling`updateChildren()`, you can update lower-level child values by specifying a path for the key. If data is stored in multiple locations to scale better, you can update all instances of that data using[data fan-out](https://firebase.google.com/docs/database/android/structure-data#fanout). For example, a social blogging app might have a`Post`class like this:  

### Kotlin

```kotlin
@IgnoreExtraProperties
data class Post(
    var uid: String? = "",
    var author: String? = "",
    var title: String? = "",
    var body: String? = "",
    var starCount: Int = 0,
    var stars: MutableMap<String, Boolean> = HashMap(),
) {

    @Exclude
    fun toMap(): Map<String, Any?> {
        return mapOf(
            "uid" to uid,
            "author" to author,
            "title" to title,
            "body" to body,
            "starCount" to starCount,
            "stars" to stars,
        )
    }
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/models/Post.kt#L8-L31
```

### Java

```java
@IgnoreExtraProperties
public class Post {

    public String uid;
    public String author;
    public String title;
    public String body;
    public int starCount = 0;
    public Map<String, Boolean> stars = new HashMap<>();

    public Post() {
        // Default constructor required for calls to DataSnapshot.getValue(Post.class)
    }

    public Post(String uid, String author, String title, String body) {
        this.uid = uid;
        this.author = author;
        this.title = title;
        this.body = body;
    }

    @Exclude
    public Map<String, Object> toMap() {
        HashMap<String, Object> result = new HashMap<>();
        result.put("uid", uid);
        result.put("author", author);
        result.put("title", title);
        result.put("body", body);
        result.put("starCount", starCount);
        result.put("stars", stars);

        return result;
    }
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/models/Post.java#L10-L45
```

To create a post and simultaneously update it to the recent activity feed and the posting user's activity feed, the blogging application uses code like this:  

### Kotlin

```kotlin
private fun writeNewPost(userId: String, username: String, title: String, body: String) {
    // Create new post at /user-posts/$userid/$postid and at
    // /posts/$postid simultaneously
    val key = database.child("posts").push().key
    if (key == null) {
        Log.w(TAG, "Couldn't get push key for posts")
        return
    }

    val post = Post(userId, username, title, body)
    val postValues = post.toMap()

    val childUpdates = hashMapOf<String, Any>(
        "/posts/$key" to postValues,
        "/user-posts/$userId/$key" to postValues,
    )

    database.updateChildren(childUpdates)
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/ReadAndWriteSnippets.kt#L74-L92
```

### Java

```java
private void writeNewPost(String userId, String username, String title, String body) {
    // Create new post at /user-posts/$userid/$postid and at
    // /posts/$postid simultaneously
    String key = mDatabase.child("posts").push().getKey();
    Post post = new Post(userId, username, title, body);
    Map<String, Object> postValues = post.toMap();

    Map<String, Object> childUpdates = new HashMap<>();
    childUpdates.put("/posts/" + key, postValues);
    childUpdates.put("/user-posts/" + userId + "/" + key, postValues);

    mDatabase.updateChildren(childUpdates);
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/ReadAndWriteSnippets.java#L88-L100
```

This example uses`push()`to create a post in the node containing posts for all users at`/posts/$postid`and simultaneously retrieve the key with`getKey()`. The key can then be used to create a second entry in the user's posts at`/user-posts/$userid/$postid`.

Using these paths, you can perform simultaneous updates to multiple locations in the JSON tree with a single call to`updateChildren()`, such as how this example creates the new post in both locations. Simultaneous updates made this way are atomic: either all updates succeed or all updates fail.

### Add a Completion Callback

If you want to know when your data has been committed, you can add a completion listener. Both`setValue()`and`updateChildren()`take an optional completion listener that is called when the write has been successfully committed to the database. If the call was unsuccessful, the listener is passed an error object indicating why the failure occurred.  

### Kotlin

```kotlin
database.child("users").child(userId).setValue(user)
    .addOnSuccessListener {
        // Write was successful!
        // ...
    }
    .addOnFailureListener {
        // Write failed
        // ...
    }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/ReadAndWriteSnippets.kt#L43-L51
```

### Java

```java
mDatabase.child("users").child(userId).setValue(user)
        .addOnSuccessListener(new OnSuccessListener<Void>() {
            @Override
            public void onSuccess(Void aVoid) {
                // Write was successful!
                // ...
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                // Write failed
                // ...
            }
        });https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/ReadAndWriteSnippets.java#L49-L63
```

### Delete data

The simplest way to delete data is to call`removeValue()`on a reference to the location of that data.

You can also delete by specifying`null`as the value for another write operation such as`setValue()`or`updateChildren()`. You can use this technique with`updateChildren()`to delete multiple children in a single API call.

## Detach listeners

Callbacks are removed by calling the`removeEventListener()`method on your Firebase database reference.

If a listener has been added multiple times to a data location, it is called multiple times for each event, and you must detach it the same number of times to remove it completely.

Calling`removeEventListener()`on a parent listener does not automatically remove listeners registered on its child nodes;`removeEventListener()`must also be called on any child listeners to remove the callback.

## Save data as transactions

When working with data that could be corrupted by concurrent modifications, such as incremental counters, you can use a[transaction operation](https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler). You give this operation two arguments: an update function and an optional completion callback. The update function takes the current state of the data as an argument and returns the new desired state you would like to write. If another client writes to the location before your new value is successfully written, your update function is called again with the new current value, and the write is retried.

For instance, in the example social blogging app, you could allow users to star and unstar posts and keep track of how many stars a post has received as follows:  

### Kotlin

```kotlin
private fun onStarClicked(postRef: DatabaseReference) {
    // ...
    postRef.runTransaction(object : Transaction.Handler {
        override fun doTransaction(mutableData: MutableData): Transaction.Result {
            val p = mutableData.getValue(Post::class.java)
                ?: return Transaction.success(mutableData)

            if (p.stars.containsKey(uid)) {
                // Unstar the post and remove self from stars
                p.starCount = p.starCount - 1
                p.stars.remove(uid)
            } else {
                // Star the post and add self to stars
                p.starCount = p.starCount + 1
                p.stars[uid] = true
            }

            // Set value and report transaction success
            mutableData.value = p
            return Transaction.success(mutableData)
        }

        override fun onComplete(
            databaseError: DatabaseError?,
            committed: Boolean,
            currentData: DataSnapshot?,
        ) {
            // Transaction completed
            Log.d(TAG, "postTransaction:onComplete:" + databaseError!!)
        }
    })
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/ReadAndWriteSnippets.kt#L96-L129
```

### Java

```java
private void onStarClicked(DatabaseReference postRef) {
    postRef.runTransaction(new Transaction.Handler() {
        @NonNull
        @Override
        public Transaction.Result doTransaction(@NonNull MutableData mutableData) {
            Post p = mutableData.getValue(Post.class);
            if (p == null) {
                return Transaction.success(mutableData);
            }

            if (p.stars.containsKey(getUid())) {
                // Unstar the post and remove self from stars
                p.starCount = p.starCount - 1;
                p.stars.remove(getUid());
            } else {
                // Star the post and add self to stars
                p.starCount = p.starCount + 1;
                p.stars.put(getUid(), true);
            }

            // Set value and report transaction success
            mutableData.setValue(p);
            return Transaction.success(mutableData);
        }

        @Override
        public void onComplete(DatabaseError databaseError, boolean committed,
                               DataSnapshot currentData) {
            // Transaction completed
            Log.d(TAG, "postTransaction:onComplete:" + databaseError);
        }
    });
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/ReadAndWriteSnippets.java#L108-L140
```

Using a transaction prevents star counts from being incorrect if multiple users star the same post at the same time or the client had stale data. If the transaction is rejected, the server returns the current value to the client, which runs the transaction again with the updated value. This repeats until the transaction is accepted or too many attempts have been made.
| **Note:** Because`doTransaction()`is called multiple times, it must be able to handle`null`data. Even if there is existing data in your remote database, it may not be locally cached when the transaction function is run, resulting in`null`for the initial value.

### Atomic server-side increments

In the above use case we're writing two values to the database: the ID of the user who stars/unstars the post, and the incremented star count. If we already know that user is starring the post, we can use an atomic increment operation instead of a transaction.  

### Kotlin

```kotlin
private fun onStarClicked(uid: String, key: String) {
    val updates: MutableMap<String, Any> = hashMapOf(
        "posts/$key/stars/$uid" to true,
        "posts/$key/starCount" to ServerValue.increment(1),
        "user-posts/$uid/$key/stars/$uid" to true,
        "user-posts/$uid/$key/starCount" to ServerValue.increment(1),
    )
    database.updateChildren(updates)
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/ReadAndWriteSnippets.kt#L133-L141
```

### Java

```java
private void onStarClicked(String uid, String key) {
    Map<String, Object> updates = new HashMap<>();
    updates.put("posts/"+key+"/stars/"+uid, true);
    updates.put("posts/"+key+"/starCount", ServerValue.increment(1));
    updates.put("user-posts/"+uid+"/"+key+"/stars/"+uid, true);
    updates.put("user-posts/"+uid+"/"+key+"/starCount", ServerValue.increment(1));
    mDatabase.updateChildren(updates);
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/database/app/src/main/java/com/google/firebase/referencecode/database/ReadAndWriteSnippets.java#L144-L151
```

This code does not use a transaction operation, so it does not automatically get re-run if there is a conflicting update. However, since the increment operation happens directly on the database server, there is no chance of a conflict.

If you want to detect and reject application-specific conflicts, such as a user starring a post that they already starred before, you should write custom security rules for that use case.

## Work with data offline

If a client loses its network connection, your app will continue functioning correctly.

Every client connected to a Firebase database maintains its own internal version of any data on which listeners are being used or which is flagged to be kept in sync with the server. When data is read or written, this local version of the data is used first. The Firebase client then synchronizes that data with the remote database servers and with other clients on a "best-effort" basis.

As a result, all writes to the database trigger local events immediately, before any interaction with the server. This means your app remains responsive regardless of network latency or connectivity.

Once connectivity is reestablished, your app receives the appropriate set of events so that the client syncs with the current server state, without having to write any custom code.

We'll talk more about offline behavior in[Learn more about online and offline capabilities](https://firebase.google.com/docs/database/android/offline-capabilities).

## Next steps

- [Working with lists of data](https://firebase.google.com/docs/database/android/lists-of-data)
- [Learn how to structure data](https://firebase.google.com/docs/database/android/structure-data)
- [Learn more about online and offline capabilities](https://firebase.google.com/docs/database/android/offline-capabilities)