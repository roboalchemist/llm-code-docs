# Source: https://firebase.google.com/docs/database/ios/read-and-write.md.txt

## (Optional) Prototype and test with Firebase Local Emulator Suite

Before talking about how your app reads from and writes to Realtime Database,
let's introduce a set of tools you can use to prototype and test Realtime Database
functionality: Firebase Local Emulator Suite. If you're trying out different data
models, optimizing your security rules, or working to find the most
cost-effective way to interact with the back-end, being able to work locally
without deploying live services can be a great idea.

A Realtime Database emulator is part of the Local Emulator Suite, which
enables your app to interact with your emulated database content and config, as
well as optionally your emulated project resources (functions, other databases,
and security rules).

Using the Realtime Database emulator involves just a few steps:

1. Adding a line of code to your app's test config to connect to the emulator.
2. From the root of your local project directory, running `firebase emulators:start`.
3. Making calls from your app's prototype code using a Realtime Database platform SDK as usual, or using the Realtime Database REST API.

A detailed [walkthrough involving Realtime Database and Cloud Functions](https://firebase.google.com/docs/emulator-suite/connect_and_prototype?database=RTDB) is available. You should also have a look at the [Local Emulator Suite introduction](https://firebase.google.com/docs/emulator-suite).

## Get a FIRDatabaseReference

To read or write data from the database, you need an instance of
`FIRDatabaseReference`:

### Swift


**Note:** This Firebase product is not available on the App Clip target.

```swift
var ref: DatabaseReference!

ref = Database.database().reference()
```

<br />

### Objective-C


**Note:** This Firebase product is not available on the App Clip target.

```objective-c
@property (strong, nonatomic) FIRDatabaseReference *ref;

self.ref = [[FIRDatabase database] reference];
```

## Write data

This document covers the basics of reading and writing Firebase data.

Firebase data is written to a `Database` reference and retrieved by
attaching an asynchronous listener to the reference. The listener is triggered
once for the initial state of the data and again anytime the data changes.

> [!NOTE]
> **Note:** By default, read and write access to your database is restricted so only authenticated users can read or write data. To get started without setting up [Authentication](https://firebase.google.com/docs/auth), you can [configure your rules for public access](https://firebase.google.com/docs/rules/basics#default_rules_locked_mode). This does make your database open to anyone, even people not using your app, so be sure to restrict your database again when you set up authentication.

### Basic write operations

For basic write operations, you can use `setValue` to save data to a specified
reference, replacing any existing data at that path. You can use this method to:

- Pass types that correspond to the available JSON types as follows:
  - `NSString`
  - `NSNumber`
  - `NSDictionary`
  - `NSArray`

For instance, you can add a user with `setValue` as follows:

### Swift


**Note:** This Firebase product is not available on the App Clip target.

```swift
self.ref.child("users").child(user.uid).setValue(["username": username])
```

<br />

### Objective-C


**Note:** This Firebase product is not available on the App Clip target.

```objective-c
[[[self.ref child:@"users"] child:authResult.user.uid]
    setValue:@{@"username": username}];
```

Using `setValue` in this way overwrites data at the specified location,
including any child nodes. However, you can still update a child without
rewriting the entire object. If you want to allow users to update their profiles
you could update the username as follows:

### Swift


**Note:** This Firebase product is not available on the App Clip target.

```swift
self.ref.child("users/\(user.uid)/username").setValue(username)
```

### Objective-C


**Note:** This Firebase product is not available on the App Clip target.

```objective-c
[[[[_ref child:@"users"] child:user.uid] child:@"username"] setValue:username];
```

## Read data

### Read data by listening for value events

To read data at a path and listen for changes, use the
`observeEventType:withBlock` of `FIRDatabaseReference` to observe
`FIRDataEventTypeValue` events.

| Event type | Typical usage |
|---|---|
| `FIRDataEventTypeValue` | Read and listen for changes to the entire contents of a path. |

You can use the `FIRDataEventTypeValue` event to read the data at a given path,
as it exists at the time of the event. This method is triggered once when the
listener is attached and again every time the data, including any children,
changes. The event callback is passed a `snapshot` containing all data at that
location, including child data. If there is no data, the snapshot will return
`false` when you call `exists()` and `nil` when you read its `value` property.

> [!IMPORTANT]
> **Important:** The `FIRDataEventTypeValue` event is fired every time data is changed at the specified database reference, including changes to children. To limit the size of your snapshots, attach only at the highest level needed for watching changes. For example, attaching a listener to the root of your database is not recommended.

The following example demonstrates a social blogging application retrieving the
details of a post from the database:

### Swift


**Note:** This Firebase product is not available on the App Clip target.

```swift
refHandle = postRef.observe(DataEventType.value, with: { snapshot in
  // ...
})
```

### Objective-C


**Note:** This Firebase product is not available on the App Clip target.

```objective-c
_refHandle = [_postRef observeEventType:FIRDataEventTypeValue withBlock:^(FIRDataSnapshot * _Nonnull snapshot) {
  NSDictionary *postDict = snapshot.value;
  // ...
}];
```

The listener receives a `FIRDataSnapshot` that contains the data at the specified
location in the database at the time of the event in its `value` property. You
can assign the values to the appropriate native type, such as `NSDictionary`.
If no data exists at the location, the `value` is `nil`.

### Read data once

#### Read once using getData()

The SDK is designed to manage interactions with database servers whether your
app is online or offline.

Generally, you should use the value events techniques described above to read
data to get notified of updates to the data from the backend. Those technique
reduce your usage and billing, and are optimized to give your users the best
experience as they go online and offline.

If you need the data only once, you can use `getData()` to get a snapshot of the
data from the database. If for any reason `getData()` is unable to return the
server value, the client will probe the local storage cache and return an error
if the value is still not found.

The following example demonstrates retrieving a user's public-facing username
a single time from the database:

### Swift


**Note:** This Firebase product is not available on the App Clip target.

```swift
do {
  let snapshot = try await ref.child("users/\(uid)/username").getData()
  let userName = snapshot.value as? String ?? "Unknown"
} catch {
  print(error)
}
```

### Objective-C


**Note:** This Firebase product is not available on the App Clip target.

```objective-c
NSString *userPath = [NSString stringWithFormat:@"users/%@/username", uid];
[[ref child:userPath] getDataWithCompletionBlock:^(NSError * _Nullable error, FIRDataSnapshot * _Nonnull snapshot) {
  if (error) {
    NSLog(@"Received an error %@", error);
    return;
  }
  NSString *userName = snapshot.value;
}];
```

Unnecessary use of `getData()` can increase use of bandwidth and lead to loss
of performance, which can be prevented by using a realtime listener as shown
above.

#### Read data once with an observer

In some cases you may want the value from the local cache to be returned
immediately, instead of checking for an updated value on the server. In those
cases you can use `observeSingleEventOfType` to get the data from the
local disk cache immediately.

This is useful for data that only needs to be loaded once and isn't expected to
change frequently or require active listening. For instance, the blogging app
in the previous examples uses this method to load a user's profile when they
begin authoring a new post:

### Swift


**Note:** This Firebase product is not available on the App Clip target.

```swift
let userID = Auth.auth().currentUser?.uid
ref.child("users").child(userID!).observeSingleEvent(of: .value, with: { snapshot in
  // Get user value
  let value = snapshot.value as? NSDictionary
  let username = value?["username"] as? String ?? ""
  let user = User(username: username)

  // ...
}) { error in
  print(error.localizedDescription)
}
```

### Objective-C


**Note:** This Firebase product is not available on the App Clip target.

```objective-c
NSString *userID = [FIRAuth auth].currentUser.uid;
[[[_ref child:@"users"] child:userID] observeSingleEventOfType:FIRDataEventTypeValue withBlock:^(FIRDataSnapshot * _Nonnull snapshot) {
  // Get user value
  User *user = [[User alloc] initWithUsername:snapshot.value[@"username"]];

  // ...
} withCancelBlock:^(NSError * _Nonnull error) {
  NSLog(@"%@", error.localizedDescription);
}];
```

## Updating or deleting data

### Update specific fields

To simultaneously write to specific children of a node without overwriting other
child nodes, use the `updateChildValues` method.

<>
When calling `updateChildValues`, you can update lower-level child values by
specifying a path for the key. If data is stored in multiple locations to scale
better, you can update all instances of that data using
[data fan-out](https://firebase.google.com/docs/database/ios/structure-data#fanout). For example, a
social blogging app might want to create a post and simultaneously update it to
the recent activity feed and the posting user's activity feed. To do this, the
blogging application uses code like this:

### Swift


**Note:** This Firebase product is not available on the App Clip target.

```swift
guard let key = ref.child("posts").childByAutoId().key else { return }
let post = ["uid": userID,
            "author": username,
            "title": title,
            "body": body]
let childUpdates = ["/posts/\(key)": post,
                    "/user-posts/\(userID)/\(key)/": post]
ref.updateChildValues(childUpdates)
```

### Objective-C


**Note:** This Firebase product is not available on the App Clip target.

```objective-c
NSString *key = [[_ref child:@"posts"] childByAutoId].key;
NSDictionary *post = @{@"uid": userID,
                       @"author": username,
                       @"title": title,
                       @"body": body};
NSDictionary *childUpdates = @{[@"/posts/" stringByAppendingString:key]: post,
                               [NSString stringWithFormat:@"/user-posts/%@/%@/", userID, key]: post};
[_ref updateChildValues:childUpdates];
```

This example uses `childByAutoId` to create a post in the node containing posts for
all users at `/posts/$postid` and simultaneously retrieve the key with
`getKey()`. The key can then be used to create a second entry in the user's
posts at `/user-posts/$userid/$postid`.

Using these paths, you can perform simultaneous updates to multiple locations in
the JSON tree with a single call to `updateChildValues`, such as how this example
creates the new post in both locations. Simultaneous updates made this way
are atomic: either all updates succeed or all updates fail.

### Add a Completion Block

If you want to know when your data has been committed, you can add a
completion block. Both `setValue` and `updateChildValues` take an optional
completion block that is called when the write has been committed to the
database. This listener can be useful for keeping track of which data has been
saved and which data is still being synchronized. If the call was unsuccessful,
the listener is passed an error object indicating why the failure occurred.

### Swift


**Note:** This Firebase product is not available on the App Clip target.

```swift
do {
  try await ref.child("users").child(user.uid).setValue(["username": username])
  print("Data saved successfully!")
} catch {
  print("Data could not be saved: \(error).")
}
```

### Objective-C


**Note:** This Firebase product is not available on the App Clip target.

```objective-c
[[[_ref child:@"users"] child:user.uid] setValue:@{@"username": username} withCompletionBlock:^(NSError *error, FIRDatabaseReference *ref) {
  if (error) {
    NSLog(@"Data could not be saved: %@", error);
  } else {
    NSLog(@"Data saved successfully.");
  }
}];
```

### Delete data

The simplest way to delete data is to call `removeValue` on a reference to the
location of that data.

You can also delete by specifying `nil` as the value for another write
operation such as `setValue` or `updateChildValues`. You can use this technique
with `updateChildValues` to delete multiple children in a single API call.

## Detach listeners

Observers don't automatically stop syncing data when you leave a
`ViewController`. If an observer isn't properly removed, it continues to sync
data to local memory. When an observer is no longer needed, remove it by passing
the associated `FIRDatabaseHandle` to the `removeObserverWithHandle` method.

When you add a callback block to a reference, a `FIRDatabaseHandle` is returned.
These handles can be used to remove the callback block.

If multiple listeners have been added to a database reference, each listener is
called when an event is raised. In order to stop syncing data at that location,
you must remove all observers at a location by calling the `removeAllObservers`
method.

Calling `removeObserverWithHandle` or `removeAllObservers` on a listener does
not automatically remove listeners registered on its child nodes; you must also
keep track of those references or handles to remove them.

## Save data as transactions

When working with data that could be corrupted by concurrent
modifications, such as incremental counters, you can use a
[transaction operation](https://firebase.google.com/docs/reference/ios/firebasedatabase/interface_f_i_r_database_reference#a796bff455159479a44b225eeaa2ba9d6).
You give this operation two arguments: an update function and an optional
completion callback. The update function takes the current state of the data as
an argument and returns the new desired state you would like to write.

For instance, in the example social blogging app, you could allow users to
star and unstar posts and keep track of how many stars a post has received
as follows:

### Swift


**Note:** This Firebase product is not available on the App Clip target.

```swift
ref.runTransactionBlock({ (currentData: MutableData) -> TransactionResult in
  if var post = currentData.value as? [String: AnyObject],
    let uid = Auth.auth().currentUser?.uid {
    var stars: [String: Bool]
    stars = post["stars"] as? [String: Bool] ?? [:]
    var starCount = post["starCount"] as? Int ?? 0
    if let _ = stars[uid] {
      // Unstar the post and remove self from stars
      starCount -= 1
      stars.removeValue(forKey: uid)
    } else {
      // Star the post and add self to stars
      starCount += 1
      stars[uid] = true
    }
    post["starCount"] = starCount as AnyObject?
    post["stars"] = stars as AnyObject?

    // Set value and report transaction success
    currentData.value = post

    return TransactionResult.success(withValue: currentData)
  }
  return TransactionResult.success(withValue: currentData)
}) { error, committed, snapshot in
  if let error = error {
    print(error.localizedDescription)
  }
}
```

### Objective-C


**Note:** This Firebase product is not available on the App Clip target.

```objective-c
[ref runTransactionBlock:^FIRTransactionResult * _Nonnull(FIRMutableData * _Nonnull currentData) {
  NSMutableDictionary *post = currentData.value;
  if (!post || [post isEqual:[NSNull null]]) {
    return [FIRTransactionResult successWithValue:currentData];
  }

  NSMutableDictionary *stars = post[@"stars"];
  if (!stars) {
    stars = [[NSMutableDictionary alloc] initWithCapacity:1];
  }
  NSString *uid = [FIRAuth auth].currentUser.uid;
  int starCount = [post[@"starCount"] intValue];
  if (stars[uid]) {
    // Unstar the post and remove self from stars
    starCount--;
    [stars removeObjectForKey:uid];
  } else {
    // Star the post and add self to stars
    starCount++;
    stars[uid] = @YES;
  }
  post[@"stars"] = stars;
  post[@"starCount"] = @(starCount);

  // Set value and report transaction success
  currentData.value = post;
  return [FIRTransactionResult successWithValue:currentData];
} andCompletionBlock:^(NSError * _Nullable error,
                       BOOL committed,
                       FIRDataSnapshot * _Nullable snapshot) {
  // Transaction completed
  if (error) {
    NSLog(@"%@", error.localizedDescription);
  }
}];
```

Using a transaction prevents star counts from being incorrect if multiple
users star the same post at the same time or the client had stale data. The
value contained in the `FIRMutableData` class is initially the client's last
known value for the path, or `nil` if there is none. The server compares the
initial value against its current value and accepts the transaction if the
values match, or rejects it. If the transaction is rejected, the server returns
the current value to the client, which runs the transaction again with the
updated value. This repeats until the transaction is accepted or too many
attempts have been made.

> [!NOTE]
> **Note:** Because `runTransactionBlock:andCompletionBlock:` is called multiple times, it must be able to handle `nil` data. Even if there is existing data in your remote database, it may not be locally cached when the transaction function is run, resulting in `nil` for the initial value.

### Atomic server-side increments

In the above use case we're writing two values to the database: the ID of
the user who stars/unstars the post, and the incremented star count. If we
already know that user is starring the post, we can use an atomic increment
operation instead of a transaction.

### Swift


**Note:** This Firebase product is not available on the App Clip target.

```swift
let updates = [
  "posts/\(postID)/stars/\(userID)": true,
  "posts/\(postID)/starCount": ServerValue.increment(1),
  "user-posts/\(postID)/stars/\(userID)": true,
  "user-posts/\(postID)/starCount": ServerValue.increment(1)
] as [String : Any]
Database.database().reference().updateChildValues(updates)
```

### Objective-C


**Note:** This Firebase product is not available on the App Clip target.

```objective-c
NSDictionary *updates = @{[NSString stringWithFormat: @"posts/%@/stars/%@", postID, userID]: @TRUE,
                        [NSString stringWithFormat: @"posts/%@/starCount", postID]: [FIRServerValue increment:@1],
                        [NSString stringWithFormat: @"user-posts/%@/stars/%@", postID, userID]: @TRUE,
                        [NSString stringWithFormat: @"user-posts/%@/starCount", postID]: [FIRServerValue increment:@1]};
[[[FIRDatabase database] reference] updateChildValues:updates];
```

This code does not use a transaction operation, so it does not automatically get
re-run if there is a conflicting update. However, since the increment operation
happens directly on the database server, there is no chance of a conflict.

If you want to detect and reject application-specific conflicts, such as a user
starring a post that they already starred before, you should write custom
security rules for that use case.

## Work with data offline

If a client loses its network connection, your app will continue functioning
correctly.

Every client connected to a Firebase database maintains its own internal version
of any active data. When data is written, it's written to this local version
first. The Firebase client then synchronizes that data with the remote database
servers and with other clients on a "best-effort" basis.

As a result, all writes to the database trigger local events immediately, before
any data is written to the server. This means your app remains
responsive regardless of network latency or connectivity.

Once connectivity is reestablished, your app receives the appropriate set of
events so that the client syncs with the current server state, without having to
write any custom code.

We'll talk more about offline behavior in
[Learn more about online and offline capabilities](https://firebase.google.com/docs/database/ios/offline-capabilities).

## Next Steps

- [Working with lists of data](https://firebase.google.com/docs/database/ios/lists-of-data)
- [Learn how to structure data](https://firebase.google.com/docs/database/ios/structure-data)
- [Learn more about online and offline capabilities](https://firebase.google.com/docs/database/ios/offline-capabilities)