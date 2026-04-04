# Source: https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.database.Reference.md.txt

# Reference | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [database](https://firebase.google.com/docs/reference/node/firebase.database).
- Reference

A `Reference` represents a specific location in your Database and can be used
for reading or writing data to that Database location.

You can reference the root or child location in your Database by calling
`firebase.database().ref()` or `firebase.database().ref("child/path")`.

Writing is done with the `set()` method and reading can be done with the
`on()` method. See
[Read and Write Data on the Web](https://firebase.google.com/docs/database/web/read-and-write)

## Index

### Properties

- [key](https://firebase.google.com/docs/reference/node/firebase.database.Reference#key)
- [parent](https://firebase.google.com/docs/reference/node/firebase.database.Reference#parent)
- [ref](https://firebase.google.com/docs/reference/node/firebase.database.Reference#ref)
- [root](https://firebase.google.com/docs/reference/node/firebase.database.Reference#root)

### Methods

- [child](https://firebase.google.com/docs/reference/node/firebase.database.Reference#child)
- [endAt](https://firebase.google.com/docs/reference/node/firebase.database.Reference#endat)
- [endBefore](https://firebase.google.com/docs/reference/node/firebase.database.Reference#endbefore)
- [equalTo](https://firebase.google.com/docs/reference/node/firebase.database.Reference#equalto)
- [get](https://firebase.google.com/docs/reference/node/firebase.database.Reference#get)
- [isEqual](https://firebase.google.com/docs/reference/node/firebase.database.Reference#isequal)
- [limitToFirst](https://firebase.google.com/docs/reference/node/firebase.database.Reference#limittofirst)
- [limitToLast](https://firebase.google.com/docs/reference/node/firebase.database.Reference#limittolast)
- [off](https://firebase.google.com/docs/reference/node/firebase.database.Reference#off)
- [on](https://firebase.google.com/docs/reference/node/firebase.database.Reference#on)
- [onDisconnect](https://firebase.google.com/docs/reference/node/firebase.database.Reference#ondisconnect)
- [once](https://firebase.google.com/docs/reference/node/firebase.database.Reference#once)
- [orderByChild](https://firebase.google.com/docs/reference/node/firebase.database.Reference#orderbychild)
- [orderByKey](https://firebase.google.com/docs/reference/node/firebase.database.Reference#orderbykey)
- [orderByPriority](https://firebase.google.com/docs/reference/node/firebase.database.Reference#orderbypriority)
- [orderByValue](https://firebase.google.com/docs/reference/node/firebase.database.Reference#orderbyvalue)
- [push](https://firebase.google.com/docs/reference/node/firebase.database.Reference#push)
- [remove](https://firebase.google.com/docs/reference/node/firebase.database.Reference#remove)
- [set](https://firebase.google.com/docs/reference/node/firebase.database.Reference#set)
- [setPriority](https://firebase.google.com/docs/reference/node/firebase.database.Reference#setpriority)
- [setWithPriority](https://firebase.google.com/docs/reference/node/firebase.database.Reference#setwithpriority)
- [startAfter](https://firebase.google.com/docs/reference/node/firebase.database.Reference#startafter)
- [startAt](https://firebase.google.com/docs/reference/node/firebase.database.Reference#startat)
- [toJSON](https://firebase.google.com/docs/reference/node/firebase.database.Reference#tojson)
- [toString](https://firebase.google.com/docs/reference/node/firebase.database.Reference#tostring)
- [transaction](https://firebase.google.com/docs/reference/node/firebase.database.Reference#transaction)
- [update](https://firebase.google.com/docs/reference/node/firebase.database.Reference#update)

## Properties

### key

key: string \| null  
The last part of the `Reference`'s path.

For example, `"ada"` is the key for
`https://<DATABASE_NAME>.firebaseio.com/users/ada`.

The key of a root `Reference` is `null`.

example
:

        // The key of a root reference is null
        var rootRef = firebase.database().ref();
        var key = rootRef.key;  // key === null


example
:

        // The key of any non-root reference is the last token in the path
        var adaRef = firebase.database().ref("users/ada");
        var key = adaRef.key;  // key === "ada"
        key = adaRef.child("name/last").key;  // key === "last"


### parent

parent: [Reference](https://firebase.google.com/docs/reference/node/firebase.database.Reference) \| null  
The parent location of a `Reference`.

The parent of a root `Reference` is `null`.

example
:

        // The parent of a root reference is null
        var rootRef = firebase.database().ref();
        parent = rootRef.parent;  // parent === null


example
:

        // The parent of any non-root reference is the parent location
        var usersRef = firebase.database().ref("users");
        var adaRef = firebase.database().ref("users/ada");
        // usersRef and adaRef.parent represent the same location


### ref

ref: [Reference](https://firebase.google.com/docs/reference/node/firebase.database.Reference)
Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[ref](https://firebase.google.com/docs/reference/node/firebase.database.Query#ref)  
Returns a `Reference` to the `Query`'s location.

### root

root: [Reference](https://firebase.google.com/docs/reference/node/firebase.database.Reference)  
The root `Reference` of the Database.

example
:

        // The root of a root reference is itself
        var rootRef = firebase.database().ref();
        // rootRef and rootRef.root represent the same location


example
:

        // The root of any non-root reference is the root location
        var adaRef = firebase.database().ref("users/ada");
        // rootRef and adaRef.root represent the same location


## Methods

### child

- child ( path : string ) : [Reference](https://firebase.google.com/docs/reference/node/firebase.database.Reference)
- Gets a `Reference` for the location at the specified relative path.

  The relative path can either be a simple child name (for example, "ada") or
  a deeper slash-separated path (for example, "ada/name/first").

  example
  :

          var usersRef = firebase.database().ref('users');
          var adaRef = usersRef.child('ada');
          var adaFirstNameRef = adaRef.child('name/first');
          var path = adaFirstNameRef.toString();
          // path is now 'https://sample-app.firebaseio.com/users/ada/name/first'


  #### Parameters

  -

    ##### path: string

    A relative path from this location to the desired child
    location.

  #### Returns [Reference](https://firebase.google.com/docs/reference/node/firebase.database.Reference)

  The specified child location.

### endAt

- endAt ( value : number \| string \| boolean \| null , key ? : string ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[endAt](https://firebase.google.com/docs/reference/node/firebase.database.Query#endat)  
  Creates a `Query` with the specified ending point.

  Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()`
  allows you to choose arbitrary starting and ending points for your queries.

  The ending point is inclusive, so children with exactly the specified value
  will be included in the query. The optional key argument can be used to
  further limit the range of the query. If it is specified, then children that
  have exactly the specified value must also have a key name less than or equal
  to the specified key.

  You can read more about `endAt()` in
  [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

  example
  :

          // Find all dinosaurs whose names come before Pterodactyl lexicographically.
          // Include Pterodactyl in the result.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByKey().endAt("pterodactyl").on("child_added", function(snapshot) {
            console.log(snapshot.key);
          });


  #### Parameters

  -

    ##### value: number \| string \| boolean \| null

    The value to end at. The argument
    type depends on which `orderBy*()` function was used in this query.
    Specify a value that matches the `orderBy*()` type. When used in
    combination with `orderByKey()`, the value must be a string.
  -

    ##### Optional key: string

    The child key to end at, among the children with the
    previously specified priority. This argument is only allowed if ordering by
    child, value, or priority.

  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### endBefore

- endBefore ( value : number \| string \| boolean \| null , key ? : string ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[endBefore](https://firebase.google.com/docs/reference/node/firebase.database.Query#endbefore)  
  Creates a `Query` with the specified ending point (exclusive).

  Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()`
  allows you to choose arbitrary starting and ending points for your queries.

  The ending point is exclusive. If only a value is provided, children
  with a value less than the specified value will be included in the query.
  If a key is specified, then children must have a value lesss than or equal
  to the specified value and a a key name less than the specified key.

  example
  :

          // Find all dinosaurs whose names come before Pterodactyl lexicographically.
          // Do not include Pterodactyl in the result.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByKey().endBefore("pterodactyl").on("child_added", function(snapshot) {
            console.log(snapshot.key);
          });

          @param value The value to end before. The argument
            type depends on which `orderBy*()` function was used in this query.
            Specify a value that matches the `orderBy*()` type. When used in
            combination with `orderByKey()`, the value must be a string.
          @param key The child key to end before, among the children with the
            previously specified priority. This argument is only allowed if ordering by
            child, value, or priority.


  #### Parameters

  -

    ##### value: number \| string \| boolean \| null

  -

    ##### Optional key: string

  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### equalTo

- equalTo ( value : number \| string \| boolean \| null , key ? : string ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[equalTo](https://firebase.google.com/docs/reference/node/firebase.database.Query#equalto)  
  Creates a `Query` that includes children that match the specified value.

  Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()`
  allows you to choose arbitrary starting and ending points for your queries.

  The optional key argument can be used to further limit the range of the
  query. If it is specified, then children that have exactly the specified
  value must also have exactly the specified key as their key name. This can be
  used to filter result sets with many matches for the same value.

  You can read more about `equalTo()` in
  [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

  example
  :

          // Find all dinosaurs whose height is exactly 25 meters.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("height").equalTo(25).on("child_added", function(snapshot) {
            console.log(snapshot.key);
          });


  #### Parameters

  -

    ##### value: number \| string \| boolean \| null

    The value to match for. The
    argument type depends on which `orderBy*()` function was used in this
    query. Specify a value that matches the `orderBy*()` type. When used in
    combination with `orderByKey()`, the value must be a string.
  -

    ##### Optional key: string

    The child key to start at, among the children with the
    previously specified priority. This argument is only allowed if ordering by
    child, value, or priority.

  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### get

- get ( ) : Promise \< [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) \>
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[get](https://firebase.google.com/docs/reference/node/firebase.database.Query#get)  
  Gets the most up-to-date result for this query.

  #### Returns Promise\<[DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot)\>

  A promise which resolves to the resulting DataSnapshot if
  a value is available, or rejects if the client is unable to return
  a value (e.g., if the server is unreachable and there is nothing
  cached).

### isEqual

- isEqual ( other : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query) \| null ) : boolean
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[isEqual](https://firebase.google.com/docs/reference/node/firebase.database.Query#isequal)  
  Returns whether or not the current and provided queries represent the same
  location, have the same query parameters, and are from the same instance of
  `firebase.app.App`.

  Two `Reference` objects are equivalent if they represent the same location
  and are from the same instance of `firebase.app.App`.

  Two `Query` objects are equivalent if they represent the same location, have
  the same query parameters, and are from the same instance of
  `firebase.app.App`. Equivalent queries share the same sort order, limits, and
  starting and ending points.

  example
  :

          var rootRef = firebase.database.ref();
          var usersRef = rootRef.child("users");

          usersRef.isEqual(rootRef);  // false
          usersRef.isEqual(rootRef.child("users"));  // true
          usersRef.parent.isEqual(rootRef);  // true


  example
  :

          var rootRef = firebase.database.ref();
          var usersRef = rootRef.child("users");
          var usersQuery = usersRef.limitToLast(10);

          usersQuery.isEqual(usersRef);  // false
          usersQuery.isEqual(usersRef.limitToLast(10));  // true
          usersQuery.isEqual(rootRef.limitToLast(10));  // false
          usersQuery.isEqual(usersRef.orderByKey().limitToLast(10));  // false


  #### Parameters

  -

    ##### other: [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query) \| null

    The query to compare against.

  #### Returns boolean

  Whether or not the current and provided queries are
  equivalent.

### limitToFirst

- limitToFirst ( limit : number ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[limitToFirst](https://firebase.google.com/docs/reference/node/firebase.database.Query#limittofirst)  
  Generates a new `Query` limited to the first specific number of children.

  The `limitToFirst()` method is used to set a maximum number of children to be
  synced for a given callback. If we set a limit of 100, we will initially only
  receive up to 100 `child_added` events. If we have fewer than 100 messages
  stored in our Database, a `child_added` event will fire for each message.
  However, if we have over 100 messages, we will only receive a `child_added`
  event for the first 100 ordered messages. As items change, we will receive
  `child_removed` events for each item that drops out of the active list so
  that the total number stays at 100.

  You can read more about `limitToFirst()` in
  [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

  example
  :

          // Find the two shortest dinosaurs.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("height").limitToFirst(2).on("child_added", function(snapshot) {
            // This will be called exactly two times (unless there are less than two
            // dinosaurs in the Database).

            // It will also get fired again if one of the first two dinosaurs is
            // removed from the data set, as a new dinosaur will now be the second
            // shortest.
            console.log(snapshot.key);
          });


  #### Parameters

  -

    ##### limit: number

    The maximum number of nodes to include in this query.

  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### limitToLast

- limitToLast ( limit : number ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[limitToLast](https://firebase.google.com/docs/reference/node/firebase.database.Query#limittolast)  
  Generates a new `Query` object limited to the last specific number of
  children.

  The `limitToLast()` method is used to set a maximum number of children to be
  synced for a given callback. If we set a limit of 100, we will initially only
  receive up to 100 `child_added` events. If we have fewer than 100 messages
  stored in our Database, a `child_added` event will fire for each message.
  However, if we have over 100 messages, we will only receive a `child_added`
  event for the last 100 ordered messages. As items change, we will receive
  `child_removed` events for each item that drops out of the active list so
  that the total number stays at 100.

  You can read more about `limitToLast()` in
  [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

  example
  :

          // Find the two heaviest dinosaurs.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("weight").limitToLast(2).on("child_added", function(snapshot) {
            // This callback will be triggered exactly two times, unless there are
            // fewer than two dinosaurs stored in the Database. It will also get fired
            // for every new, heavier dinosaur that gets added to the data set.
            console.log(snapshot.key);
          });


  #### Parameters

  -

    ##### limit: number

    The maximum number of nodes to include in this query.

  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### off

- off ( eventType ? : [EventType](https://firebase.google.com/docs/reference/node/firebase.database#eventtype) , callback ? : ( a : [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) , b ? : string \| null ) =\> any , context ? : Object \| null ) : void
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[off](https://firebase.google.com/docs/reference/node/firebase.database.Query#off)  
  Detaches a callback previously attached with `on()`.

  Detach a callback previously attached with `on()`. Note that if `on()` was
  called multiple times with the same eventType and callback, the callback
  will be called multiple times for each event, and `off()` must be called
  multiple times to remove the callback. Calling `off()` on a parent listener
  will not automatically remove listeners registered on child nodes, `off()`
  must also be called on any child listeners to remove the callback.

  If a callback is not specified, all callbacks for the specified eventType
  will be removed. Similarly, if no eventType is specified, all callbacks
  for the `Reference` will be removed.

  example
  :

          var onValueChange = function(dataSnapshot) {  ... };
          ref.on('value', onValueChange);
          ref.child('meta-data').on('child_added', onChildAdded);
          // Sometime later...
          ref.off('value', onValueChange);

          // You must also call off() for any child listeners on ref
          // to cancel those callbacks
          ref.child('meta-data').off('child_added', onValueAdded);


  example
  :

          // Or you can save a line of code by using an inline function
          // and on()'s return value.
          var onValueChange = ref.on('value', function(dataSnapshot) { ... });
          // Sometime later...
          ref.off('value', onValueChange);


  #### Parameters

  -

    ##### Optional eventType: [EventType](https://firebase.google.com/docs/reference/node/firebase.database#eventtype)

    One of the following strings: "value",
    "child_added", "child_changed", "child_removed", or "child_moved." If
    omitted, all callbacks for the `Reference` will be removed.
  -

    ##### Optional callback: (a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot), b?: string \| null) =\> any

    The callback function that was passed to `on()` or
    `undefined` to remove all callbacks.
    -
      - (a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot), b?: string \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot)

        -

          ##### Optional b: string \| null

        #### Returns any

  -

    ##### Optional context: Object \| null

    The context that was passed to `on()`.

  #### Returns void

### on

- on ( eventType : [EventType](https://firebase.google.com/docs/reference/node/firebase.database#eventtype) , callback : ( a : [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) , b ? : string \| null ) =\> any , cancelCallbackOrContext ? : ( ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) ) =\> any ) \| Object \| null , context ? : Object \| null ) : ( a : [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) \| null , b ? : string \| null ) =\> any
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[on](https://firebase.google.com/docs/reference/node/firebase.database.Query#on)  
  Listens for data changes at a particular location.

  This is the primary way to read data from a Database. Your callback
  will be triggered for the initial data and again whenever the data changes.
  Use `off( )` to stop receiving updates. See
  [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data)
  for more details.

  #### value event

  This event will trigger once with the initial data stored at this location,
  and then trigger again each time the data changes. The `DataSnapshot` passed
  to the callback will be for the location at which `on()` was called. It
  won't trigger until the entire contents has been synchronized. If the
  location has no data, it will be triggered with an empty `DataSnapshot`
  (`val()` will return `null`).

  #### child_added event

  This event will be triggered once for each initial child at this location,
  and it will be triggered again every time a new child is added. The
  `DataSnapshot` passed into the callback will reflect the data for the
  relevant child. For ordering purposes, it is passed a second argument which
  is a string containing the key of the previous sibling child by sort order,
  or `null` if it is the first child.

  #### child_removed event

  This event will be triggered once every time a child is removed. The
  `DataSnapshot` passed into the callback will be the old data for the child
  that was removed. A child will get removed when either:
  - a client explicitly calls `remove()` on that child or one of its ancestors
  - a client calls `set(null)` on that child or one of its ancestors
  - that child has all of its children removed
  - there is a query in effect which now filters out the child (because it's sort order changed or the max limit was hit)

  #### child_changed event

  This event will be triggered when the data stored in a child (or any of its
  descendants) changes. Note that a single `child_changed` event may represent
  multiple changes to the child. The `DataSnapshot` passed to the callback will
  contain the new child contents. For ordering purposes, the callback is also
  passed a second argument which is a string containing the key of the previous
  sibling child by sort order, or `null` if it is the first child.

  #### child_moved event

  This event will be triggered when a child's sort order changes such that its
  position relative to its siblings changes. The `DataSnapshot` passed to the
  callback will be for the data of the child that has moved. It is also passed
  a second argument which is a string containing the key of the previous
  sibling child by sort order, or `null` if it is the first child.

  example

  :   **Handle a new value:**

          ref.on('value', function(dataSnapshot) {
            ...
          });

  example

  :   **Handle a new child:**

          ref.on('child_added', function(childSnapshot, prevChildKey) {
            ...
          });

  example

  :   **Handle child removal:**

          ref.on('child_removed', function(oldChildSnapshot) {
            ...
          });

  example

  :   **Handle child data changes:**

          ref.on('child_changed', function(childSnapshot, prevChildKey) {
            ...
          });

  example

  :   **Handle child ordering changes:**

          ref.on('child_moved', function(childSnapshot, prevChildKey) {
            ...
          });

  #### Parameters

  -

    ##### eventType: [EventType](https://firebase.google.com/docs/reference/node/firebase.database#eventtype)

    One of the following strings: "value",
    "child_added", "child_changed", "child_removed", or "child_moved."
  -

    ##### callback: (a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot), b?: string \| null) =\> any

    A
    callback that fires when the specified event occurs. The callback will be
    passed a DataSnapshot. For ordering purposes, "child_added",
    "child_changed", and "child_moved" will also be passed a string containing
    the key of the previous child, by sort order, or `null` if it is the
    first child.
    -
      - (a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot), b?: string \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot)

        -

          ##### Optional b: string \| null

        #### Returns any

  -

    ##### Optional cancelCallbackOrContext: ((a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error)) =\> any) \| Object \| null

    An optional
    callback that will be notified if your event subscription is ever canceled
    because your client does not have permission to read this data (or it had
    permission but has now lost it). This callback will be passed an `Error`
    object indicating why the failure occurred.
  -

    ##### Optional context: Object \| null

    If provided, this object will be used as `this`
    when calling your callback(s).

  #### Returns (a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) \| null, b?: string \| null) =\> any

  The provided
  callback function is returned unmodified. This is just for convenience if
  you want to pass an inline function to `on()` but store the callback
  function for later passing to `off()`.
  -
    - (a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) \| null, b?: string \| null): any

    <!-- -->

    -

      #### Parameters

      -

        ##### a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) \| null

      -

        ##### Optional b: string \| null

      #### Returns any

### onDisconnect

- onDisconnect ( ) : [OnDisconnect](https://firebase.google.com/docs/reference/node/firebase.database.OnDisconnect)
- Returns an `OnDisconnect` object - see
  [Enabling Offline Capabilities in JavaScript](https://firebase.google.com/docs/database/web/offline-capabilities) for more information on how
  to use it.

  #### Returns [OnDisconnect](https://firebase.google.com/docs/reference/node/firebase.database.OnDisconnect)

### once

- once ( eventType : [EventType](https://firebase.google.com/docs/reference/node/firebase.database#eventtype) , successCallback ? : ( a : [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) , b ? : string \| null ) =\> any , failureCallbackOrContext ? : ( ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) ) =\> void ) \| Object \| null , context ? : Object \| null ) : Promise \< [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) \>
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[once](https://firebase.google.com/docs/reference/node/firebase.database.Query#once)  
  Listens for exactly one event of the specified event type, and then stops
  listening.

  This is equivalent to calling [`on()`](https://firebase.google.com/docs/reference/node/firebase.database.Query#on), and
  then calling [`off()`](https://firebase.google.com/docs/reference/node/firebase.database.Query#off) inside the callback
  function. See [`on()`](https://firebase.google.com/docs/reference/node/firebase.database.Query#on) for details on the
  event types.

  example
  :

          // Basic usage of .once() to read the data located at ref.
          ref.once('value')
            .then(function(dataSnapshot) {
              // handle read data.
            });


  #### Parameters

  -

    ##### eventType: [EventType](https://firebase.google.com/docs/reference/node/firebase.database#eventtype)

    One of the following strings: "value",
    "child_added", "child_changed", "child_removed", or "child_moved."
  -

    ##### Optional successCallback: (a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot), b?: string \| null) =\> any

    A
    callback that fires when the specified event occurs. The callback will be
    passed a DataSnapshot. For ordering purposes, "child_added",
    "child_changed", and "child_moved" will also be passed a string containing
    the key of the previous child by sort order, or `null` if it is the
    first child.
    -
      - (a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot), b?: string \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot)

        -

          ##### Optional b: string \| null

        #### Returns any

  -

    ##### Optional failureCallbackOrContext: ((a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error)) =\> void) \| Object \| null

    An optional
    callback that will be notified if your client does not have permission to
    read the data. This callback will be passed an `Error` object indicating
    why the failure occurred.
  -

    ##### Optional context: Object \| null

    If provided, this object will be used as `this`
    when calling your callback(s).

  #### Returns Promise\<[DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot)\>

### orderByChild

- orderByChild ( path : string ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[orderByChild](https://firebase.google.com/docs/reference/node/firebase.database.Query#orderbychild)  
  Generates a new `Query` object ordered by the specified child key.

  Queries can only order by one key at a time. Calling `orderByChild()`
  multiple times on the same query is an error.

  Firebase queries allow you to order your data by any child key on the fly.
  However, if you know in advance what your indexes will be, you can define
  them via the .indexOn rule in your Security Rules for better performance. See
  the [.indexOn](https://firebase.google.com/docs/database/security/indexing-data) rule for more information.

  You can read more about `orderByChild()` in
  [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data).

  example
  :

          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("height").on("child_added", function(snapshot) {
            console.log(snapshot.key + " was " + snapshot.val().height + " m tall");
          });


  #### Parameters

  -

    ##### path: string

  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### orderByKey

- orderByKey ( ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[orderByKey](https://firebase.google.com/docs/reference/node/firebase.database.Query#orderbykey)  
  Generates a new `Query` object ordered by key.

  Sorts the results of a query by their (ascending) key values.

  You can read more about `orderByKey()` in
  [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data).

  example
  :

          var ref = firebase.database().ref("dinosaurs");
          ref.orderByKey().on("child_added", function(snapshot) {
            console.log(snapshot.key);
          });


  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### orderByPriority

- orderByPriority ( ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[orderByPriority](https://firebase.google.com/docs/reference/node/firebase.database.Query#orderbypriority)  
  Generates a new `Query` object ordered by priority.

  Applications need not use priority but can order collections by
  ordinary properties (see
  [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data) for alternatives to priority.

  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### orderByValue

- orderByValue ( ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[orderByValue](https://firebase.google.com/docs/reference/node/firebase.database.Query#orderbyvalue)  
  Generates a new `Query` object ordered by value.

  If the children of a query are all scalar values (string, number, or
  boolean), you can order the results by their (ascending) values.

  You can read more about `orderByValue()` in
  [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data).

  example
  :

          var scoresRef = firebase.database().ref("scores");
          scoresRef.orderByValue().limitToLast(3).on("value", function(snapshot) {
            snapshot.forEach(function(data) {
              console.log("The " + data.key + " score is " + data.val());
            });
          });


  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### push

- push ( value ? : any , onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> any ) : [ThenableReference](https://firebase.google.com/docs/reference/node/firebase.database.ThenableReference)
- Generates a new child location using a unique key and returns its
  `Reference`.

  This is the most common pattern for adding data to a collection of items.

  If you provide a value to `push()`, the value is written to the
  generated location. If you don't pass a value, nothing is written to the
  database and the child remains empty (but you can use the `Reference`
  elsewhere).

  The unique keys generated by `push()` are ordered by the current time, so the
  resulting list of items is chronologically sorted. The keys are also
  designed to be unguessable (they contain 72 random bits of entropy).

  See
  [Append to a list of data](https://firebase.google.com/docs/database/web/lists-of-data#append_to_a_list_of_data)

  See
  [The 2\^120 Ways to Ensure Unique Identifiers](https://firebase.googleblog.com/2015/02/the-2120-ways-to-ensure-unique_68.html)

  example
  :

          var messageListRef = firebase.database().ref('message_list');
          var newMessageRef = messageListRef.push();
          newMessageRef.set({
            'user_id': 'ada',
            'text': 'The Analytical Engine weaves algebraical patterns just as the Jacquard loom weaves flowers and leaves.'
          });
          // We've appended a new message to the message_list location.
          var path = newMessageRef.toString();
          // path will be something like
          // 'https://sample-app.firebaseio.com/message_list/-IKo28nwJLH0Nc5XeFmj'


  #### Parameters

  -

    ##### Optional value: any

    Optional value to be written at the generated location.
  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> any

    Callback called when write to server is
    complete.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns any

  #### Returns [ThenableReference](https://firebase.google.com/docs/reference/node/firebase.database.ThenableReference)

  Combined `Promise` and `Reference`; resolves when write is complete, but can be
  used immediately as the `Reference` to the child location.

### remove

- remove ( onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> void ) : Promise \< void \>
- Removes the data at this Database location.

  Any data at child locations will also be deleted.

  The effect of the remove will be visible immediately and the corresponding
  event 'value' will be triggered. Synchronization of the remove to the
  Firebase servers will also be started, and the returned Promise will resolve
  when complete. If provided, the onComplete callback will be called
  asynchronously after synchronization has finished.

  example
  :

          var adaRef = firebase.database().ref('users/ada');
          adaRef.remove()
            .then(function() {
              console.log("Remove succeeded.")
            })
            .catch(function(error) {
              console.log("Remove failed: " + error.message)
            });


  #### Parameters

  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> void

    Callback called when write to server is
    complete.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): void

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns void

  #### Returns Promise\<void\>

  Resolves when remove on server is complete.

### set

- set ( value : any , onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> void ) : Promise \< void \>
- Writes data to this Database location.

  This will overwrite any data at this location and all child locations.

  The effect of the write will be visible immediately, and the corresponding
  events ("value", "child_added", etc.) will be triggered. Synchronization of
  the data to the Firebase servers will also be started, and the returned
  Promise will resolve when complete. If provided, the `onComplete` callback
  will be called asynchronously after synchronization has finished.

  Passing `null` for the new value is equivalent to calling `remove()`; namely,
  all data at this location and all child locations will be deleted.

  `set()` will remove any priority stored at this location, so if priority is
  meant to be preserved, you need to use `setWithPriority()` instead.

  Note that modifying data with `set()` will cancel any pending transactions
  at that location, so extreme care should be taken if mixing `set()` and
  `transaction()` to modify the same data.

  A single `set()` will generate a single "value" event at the location where
  the `set()` was performed.

  example
  :

          var adaNameRef = firebase.database().ref('users/ada/name');
          adaNameRef.child('first').set('Ada');
          adaNameRef.child('last').set('Lovelace');
          // We've written 'Ada' to the Database location storing Ada's first name,
          // and 'Lovelace' to the location storing her last name.


  example
  :

          adaNameRef.set({ first: 'Ada', last: 'Lovelace' });
          // Exact same effect as the previous example, except we've written
          // Ada's first and last name simultaneously.


  example
  :

          adaNameRef.set({ first: 'Ada', last: 'Lovelace' })
            .then(function() {
              console.log('Synchronization succeeded');
            })
            .catch(function(error) {
              console.log('Synchronization failed');
            });
          // Same as the previous example, except we will also log a message
          // when the data has finished synchronizing.


  #### Parameters

  -

    ##### value: any

    The value to be written (string, number, boolean, object,
    array, or null).
  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> void

    Callback called when write to server is
    complete.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): void

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns void

  #### Returns Promise\<void\>

  Resolves when write to server is complete.

### setPriority

- setPriority ( priority : string \| number \| null , onComplete : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> void ) : Promise \< void \>
- Sets a priority for the data at this Database location.

  Applications need not use priority but can order collections by
  ordinary properties (see
  [Sorting and filtering data](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data)).

  #### Parameters

  -

    ##### priority: string \| number \| null

  -

    ##### onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> void

    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): void

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns void

  #### Returns Promise\<void\>

### setWithPriority

- setWithPriority ( newVal : any , newPriority : string \| number \| null , onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> void ) : Promise \< void \>
- Writes data the Database location. Like `set()` but also specifies the
  priority for that data.

  Applications need not use priority but can order collections by
  ordinary properties (see
  [Sorting and filtering data](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data)).

  #### Parameters

  -

    ##### newVal: any

  -

    ##### newPriority: string \| number \| null

  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> void

    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): void

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns void

  #### Returns Promise\<void\>

### startAfter

- startAfter ( value : number \| string \| boolean \| null , key ? : string ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[startAfter](https://firebase.google.com/docs/reference/node/firebase.database.Query#startafter)  
  Creates a `Query` with the specified starting point (exclusive).

  Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()`
  allows you to choose arbitrary starting and ending points for your queries.

  The starting point is exclusive. If only a value is provided, children
  with a value greater than the specified value will be included in the query.
  If a key is specified, then children must have a value greater than or equal
  to the specified value and a a key name greater than the specified key.

  example
  :

          // Find all dinosaurs that are more than three meters tall.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("height").startAfter(3).on("child_added", function(snapshot) {
            console.log(snapshot.key)
          });


  #### Parameters

  -

    ##### value: number \| string \| boolean \| null

    The value to start after. The argument
    type depends on which `orderBy*()` function was used in this query.
    Specify a value that matches the `orderBy*()` type. When used in
    combination with `orderByKey()`, the value must be a string.
  -

    ##### Optional key: string

    The child key to start after. This argument is only allowed
    if ordering by child, value, or priority.

  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### startAt

- startAt ( value : number \| string \| boolean \| null , key ? : string ) : [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[startAt](https://firebase.google.com/docs/reference/node/firebase.database.Query#startat)  
  Creates a `Query` with the specified starting point.

  Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()`
  allows you to choose arbitrary starting and ending points for your queries.

  The starting point is inclusive, so children with exactly the specified value
  will be included in the query. The optional key argument can be used to
  further limit the range of the query. If it is specified, then children that
  have exactly the specified value must also have a key name greater than or
  equal to the specified key.

  You can read more about `startAt()` in
  [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

  example
  :

          // Find all dinosaurs that are at least three meters tall.
          var ref = firebase.database().ref("dinosaurs");
          ref.orderByChild("height").startAt(3).on("child_added", function(snapshot) {
            console.log(snapshot.key)
          });


  #### Parameters

  -

    ##### value: number \| string \| boolean \| null

    The value to start at. The argument
    type depends on which `orderBy*()` function was used in this query.
    Specify a value that matches the `orderBy*()` type. When used in
    combination with `orderByKey()`, the value must be a string.
  -

    ##### Optional key: string

    The child key to start at. This argument is only allowed
    if ordering by child, value, or priority.

  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query)

### toJSON

- toJSON ( ) : Object
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[toJSON](https://firebase.google.com/docs/reference/node/firebase.database.Query#tojson)  
  Returns a JSON-serializable representation of this object.

  #### Returns Object

  A JSON-serializable representation of this object.

### toString

- toString ( ) : string
-
  Inherited from [Query](https://firebase.google.com/docs/reference/node/firebase.database.Query).[toString](https://firebase.google.com/docs/reference/node/firebase.database.Query#tostring)  
  Gets the absolute URL for this location.

  The `toString()` method returns a URL that is ready to be put into a browser,
  curl command, or a `firebase.database().refFromURL()` call. Since all of
  those expect the URL to be url-encoded, `toString()` returns an encoded URL.

  Append '.json' to the returned URL when typed into a browser to download
  JSON-formatted data. If the location is secured (that is, not publicly
  readable), you will get a permission-denied error.

  example
  :

          // Calling toString() on a root Firebase reference returns the URL where its
          // data is stored within the Database:
          var rootRef = firebase.database().ref();
          var rootUrl = rootRef.toString();
          // rootUrl === "https://sample-app.firebaseio.com/".

          // Calling toString() at a deeper Firebase reference returns the URL of that
          // deep path within the Database:
          var adaRef = rootRef.child('users/ada');
          var adaURL = adaRef.toString();
          // adaURL === "https://sample-app.firebaseio.com/users/ada".


  #### Returns string

  The absolute URL for this location.

### transaction

- transaction ( transactionUpdate : ( a : any ) =\> any , onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null , b : boolean , c : [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) \| null ) =\> void , applyLocally ? : boolean ) : Promise \< [TransactionResult](https://firebase.google.com/docs/reference/node/firebase.database.TransactionResult) \>
- Atomically modifies the data at this location.

  Atomically modify the data at this location. Unlike a normal `set()`, which
  just overwrites the data regardless of its previous value, `transaction()` is
  used to modify the existing value to a new value, ensuring there are no
  conflicts with other clients writing to the same location at the same time.

  To accomplish this, you pass `transaction()` an update function which is used
  to transform the current value into a new value. If another client writes to
  the location before your new value is successfully written, your update
  function will be called again with the new current value, and the write will
  be retried. This will happen repeatedly until your write succeeds without
  conflict or you abort the transaction by not returning a value from your
  update function.

  Note: Modifying data with `set()` will cancel any pending transactions at
  that location, so extreme care should be taken if mixing `set()` and
  `transaction()` to update the same data.

  Note: When using transactions with Security and Firebase Rules in place, be
  aware that a client needs `.read` access in addition to `.write` access in
  order to perform a transaction. This is because the client-side nature of
  transactions requires the client to read the data in order to transactionally
  update it.

  example
  :

          // Increment Ada's rank by 1.
          var adaRankRef = firebase.database().ref('users/ada/rank');
          adaRankRef.transaction(function(currentRank) {
            // If users/ada/rank has never been set, currentRank will be `null`.
            return currentRank + 1;
          });


  example
  :

          // Try to create a user for ada, but only if the user id 'ada' isn't
          // already taken
          var adaRef = firebase.database().ref('users/ada');
          adaRef.transaction(function(currentData) {
            if (currentData === null) {
              return { name: { first: 'Ada', last: 'Lovelace' } };
            } else {
              console.log('User ada already exists.');
              return; // Abort the transaction.
            }
          }, function(error, committed, snapshot) {
            if (error) {
              console.log('Transaction failed abnormally!', error);
            } else if (!committed) {
              console.log('We aborted the transaction (because ada already exists).');
            } else {
              console.log('User ada added!');
            }
            console.log("Ada's data: ", snapshot.val());
          });


  #### Parameters

  -

    ##### transactionUpdate: (a: any) =\> any

    A developer-supplied function which
    will be passed the current data stored at this location (as a JavaScript
    object). The function should return the new value it would like written (as
    a JavaScript object). If `undefined` is returned (i.e. you return with no
    arguments) the transaction will be aborted and the data at this location
    will not be modified.
    -
      - (a: any): any

      <!-- -->

      -

        #### Parameters

        -

          ##### a: any

        #### Returns any

  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null, b: boolean, c: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) \| null) =\> void

    A callback
    function that will be called when the transaction completes. The callback
    is passed three arguments: a possibly-null `Error`, a `boolean` indicating
    whether the transaction was committed, and a `DataSnapshot` indicating the
    final result. If the transaction failed abnormally, the first argument will
    be an `Error` object indicating the failure cause. If the transaction
    finished normally, but no data was committed because no data was returned
    from `transactionUpdate`, then second argument will be false. If the
    transaction completed and committed data to Firebase, the second argument
    will be true. Regardless, the third argument will be a `DataSnapshot`
    containing the resulting data in this location.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null, b: boolean, c: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) \| null): void

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        -

          ##### b: boolean

        -

          ##### c: [DataSnapshot](https://firebase.google.com/docs/reference/node/firebase.database.DataSnapshot) \| null

        #### Returns void

  -

    ##### Optional applyLocally: boolean

    By default, events are raised each time the
    transaction update function runs. So if it is run multiple times, you may
    see intermediate states. You can set this to false to suppress these
    intermediate states and instead wait until the transaction has completed
    before events are raised.

  #### Returns Promise\<[TransactionResult](https://firebase.google.com/docs/reference/node/firebase.database.TransactionResult)\>

  Returns a Promise that can optionally be used instead of the onComplete
  callback to handle success and failure.

### update

- update ( values : Object , onComplete ? : ( a : [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null ) =\> void ) : Promise \< void \>
- Writes multiple values to the Database at once.

  The `values` argument contains multiple property-value pairs that will be
  written to the Database together. Each child property can either be a simple
  property (for example, "name") or a relative path (for example,
  "name/first") from the current location to the data to update.

  As opposed to the `set()` method, `update()` can be use to selectively update
  only the referenced properties at the current location (instead of replacing
  all the child properties at the current location).

  The effect of the write will be visible immediately, and the corresponding
  events ('value', 'child_added', etc.) will be triggered. Synchronization of
  the data to the Firebase servers will also be started, and the returned
  Promise will resolve when complete. If provided, the `onComplete` callback
  will be called asynchronously after synchronization has finished.

  A single `update()` will generate a single "value" event at the location
  where the `update()` was performed, regardless of how many children were
  modified.

  Note that modifying data with `update()` will cancel any pending
  transactions at that location, so extreme care should be taken if mixing
  `update()` and `transaction()` to modify the same data.

  Passing `null` to `update()` will remove the data at this location.

  See
  [Introducing multi-location updates and more](https://firebase.googleblog.com/2015/09/introducing-multi-location-updates-and_86.html).

  example
  :

          var adaNameRef = firebase.database().ref('users/ada/name');
          // Modify the 'first' and 'last' properties, but leave other data at
          // adaNameRef unchanged.
          adaNameRef.update({ first: 'Ada', last: 'Lovelace' });


  #### Parameters

  -

    ##### values: Object

    Object containing multiple values.
  -

    ##### Optional onComplete: (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null) =\> void

    Callback called when write to server is
    complete.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null): void

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/node/firebase.functions.HttpsError#error) \| null

        #### Returns void

  #### Returns Promise\<void\>

Resolves when update on server is complete.