# Source: https://firebase.google.com/docs/reference/js/database.md.txt

# database package

Firebase Realtime Database

## Functions

| Function | Description |
|---|---|
| **function(app, ...)** |   |
| [getDatabase(app, url)](https://firebase.google.com/docs/reference/js/database.md#getdatabase_d9cea01) | Returns the instance of the Realtime Database SDK that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). Initializes a new instance with default settings if no instance exists or if the existing instance uses a custom database URL. |
| **function(db, ...)** |   |
| [connectDatabaseEmulator(db, host, port, options)](https://firebase.google.com/docs/reference/js/database.md#connectdatabaseemulator_27b9e93) | Modify the provided instance to communicate with the Realtime Database emulator. Note: This method must be called before performing any other operation. |
| [goOffline(db)](https://firebase.google.com/docs/reference/js/database.md#gooffline_732b338) | Disconnects from the server (all Database operations will be completed offline).The client automatically maintains a persistent connection to the Database server, which will remain active indefinitely and reconnect when disconnected. However, the `goOffline()` and `goOnline()` methods may be used to control the client connection in cases where a persistent connection is undesirable.While offline, the client will no longer receive data updates from the Database. However, all Database operations performed locally will continue to immediately fire events, allowing your application to continue behaving normally. Additionally, each operation performed locally will automatically be queued and retried upon reconnection to the Database server.To reconnect to the Database and begin receiving remote events, see `goOnline()`. |
| [goOnline(db)](https://firebase.google.com/docs/reference/js/database.md#goonline_732b338) | Reconnects to the server and synchronizes the offline Database state with the server state.This method should be used after disabling the active connection with `goOffline()`. Once reconnected, the client will transmit the proper data and fire the appropriate events so that your client "catches up" automatically. |
| [ref(db, path)](https://firebase.google.com/docs/reference/js/database.md#ref_5f88fa2) | Returns a `Reference` representing the location in the Database corresponding to the provided path. If no path is provided, the `Reference` will point to the root of the Database. |
| [refFromURL(db, url)](https://firebase.google.com/docs/reference/js/database.md#reffromurl_98d95ad) | Returns a `Reference` representing the location in the Database corresponding to the provided Firebase URL.An exception is thrown if the URL is not a valid Firebase Database URL or it has a different domain than the current `Database` instance.Note that all query parameters (`orderBy`, `limitToLast`, etc.) are ignored and are not applied to the returned `Reference`. |
| **function()** |   |
| [forceLongPolling()](https://firebase.google.com/docs/reference/js/database.md#forcelongpolling) | Force the use of longPolling instead of websockets. This will be ignored if websocket protocol is used in databaseURL. |
| [forceWebSockets()](https://firebase.google.com/docs/reference/js/database.md#forcewebsockets) | Force the use of websockets instead of longPolling. |
| [orderByKey()](https://firebase.google.com/docs/reference/js/database.md#orderbykey) | Creates a new `QueryConstraint` that orders by the key.Sorts the results of a query by their (ascending) key values.You can read more about `orderByKey()` in [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data). |
| [orderByPriority()](https://firebase.google.com/docs/reference/js/database.md#orderbypriority) | Creates a new `QueryConstraint` that orders by priority.Applications need not use priority but can order collections by ordinary properties (see [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data) for alternatives to priority. |
| [orderByValue()](https://firebase.google.com/docs/reference/js/database.md#orderbyvalue) | Creates a new `QueryConstraint` that orders by value.If the children of a query are all scalar values (string, number, or boolean), you can order the results by their (ascending) values.You can read more about `orderByValue()` in [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data). |
| [serverTimestamp()](https://firebase.google.com/docs/reference/js/database.md#servertimestamp) | Returns a placeholder value for auto-populating the current timestamp (time since the Unix epoch, in milliseconds) as determined by the Firebase servers. |
| **function(delta, ...)** |   |
| [increment(delta)](https://firebase.google.com/docs/reference/js/database.md#increment_1a4266e) | Returns a placeholder value that can be used to atomically increment the current database value by the provided delta. |
| **function(enabled, ...)** |   |
| [enableLogging(enabled, persistent)](https://firebase.google.com/docs/reference/js/database.md#enablelogging_cd4f840) | Logs debugging information to the console. |
| **function(limit, ...)** |   |
| [limitToFirst(limit)](https://firebase.google.com/docs/reference/js/database.md#limittofirst_ec46c78) | Creates a new `QueryConstraint` that if limited to the first specific number of children.The `limitToFirst()` method is used to set a maximum number of children to be synced for a given callback. If we set a limit of 100, we will initially only receive up to 100 `child_added` events. If we have fewer than 100 messages stored in our Database, a `child_added` event will fire for each message. However, if we have over 100 messages, we will only receive a `child_added` event for the first 100 ordered messages. As items change, we will receive `child_removed` events for each item that drops out of the active list so that the total number stays at 100.You can read more about `limitToFirst()` in [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data). |
| [limitToLast(limit)](https://firebase.google.com/docs/reference/js/database.md#limittolast_ec46c78) | Creates a new `QueryConstraint` that is limited to return only the last specified number of children.The `limitToLast()` method is used to set a maximum number of children to be synced for a given callback. If we set a limit of 100, we will initially only receive up to 100 `child_added` events. If we have fewer than 100 messages stored in our Database, a `child_added` event will fire for each message. However, if we have over 100 messages, we will only receive a `child_added` event for the last 100 ordered messages. As items change, we will receive `child_removed` events for each item that drops out of the active list so that the total number stays at 100.You can read more about `limitToLast()` in [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data). |
| **function(logger, ...)** |   |
| [enableLogging(logger)](https://firebase.google.com/docs/reference/js/database.md#enablelogging_3886555) | Logs debugging information to the console. |
| **function(parent, ...)** |   |
| [child(parent, path)](https://firebase.google.com/docs/reference/js/database.md#child_28a1a9f) | Gets a `Reference` for the location at the specified relative path.The relative path can either be a simple child name (for example, "ada") or a deeper slash-separated path (for example, "ada/name/first"). |
| [push(parent, value)](https://firebase.google.com/docs/reference/js/database.md#push_c74661c) | Generates a new child location using a unique key and returns its `Reference`.This is the most common pattern for adding data to a collection of items.If you provide a value to `push()`, the value is written to the generated location. If you don't pass a value, nothing is written to the database and the child remains empty (but you can use the `Reference` elsewhere).The unique keys generated by `push()` are ordered by the current time, so the resulting list of items is chronologically sorted. The keys are also designed to be unguessable (they contain 72 random bits of entropy).See [Append to a list of data](https://firebase.google.com/docs/database/web/lists-of-data#append_to_a_list_of_data). See [The 2\^120 Ways to Ensure Unique Identifiers](https://firebase.googleblog.com/2015/02/the-2120-ways-to-ensure-unique_68.html). |
| **function(path, ...)** |   |
| [orderByChild(path)](https://firebase.google.com/docs/reference/js/database.md#orderbychild_fe1f8e4) | Creates a new `QueryConstraint` that orders by the specified child key.Queries can only order by one key at a time. Calling `orderByChild()` multiple times on the same query is an error.Firebase queries allow you to order your data by any child key on the fly. However, if you know in advance what your indexes will be, you can define them via the .indexOn rule in your Security Rules for better performance. See the<https://firebase.google.com/docs/database/security/indexing-data> rule for more information.You can read more about `orderByChild()` in [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data). |
| **function(query, ...)** |   |
| [get(query)](https://firebase.google.com/docs/reference/js/database.md#get_20b2416) | Gets the most up-to-date result for this query. |
| [off(query, eventType, callback)](https://firebase.google.com/docs/reference/js/database.md#off_17bb961) | Detaches a callback previously attached with the corresponding `on()`*(`onValue`, `onChildAdded`) listener. Note: This is not the recommended way to remove a listener. Instead, please use the returned callback function from the respective `on`* callbacks.Detach a callback previously attached with `on*()`. Calling `off()` on a parent listener will not automatically remove listeners registered on child nodes, `off()` must also be called on any child listeners to remove the callback.If a callback is not specified, all callbacks for the specified eventType will be removed. Similarly, if no eventType is specified, all callbacks for the `Reference` will be removed.Individual listeners can also be removed by invoking their unsubscribe callbacks. |
| [onChildAdded(query, callback, cancelCallback)](https://firebase.google.com/docs/reference/js/database.md#onchildadded_139c747) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildAdded` event will be triggered once for each initial child at this location, and it will be triggered again every time a new child is added. The `DataSnapshot` passed into the callback will reflect the data for the relevant child. For ordering purposes, it is passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child. |
| [onChildAdded(query, callback, options)](https://firebase.google.com/docs/reference/js/database.md#onchildadded_cf4f177) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildAdded` event will be triggered once for each initial child at this location, and it will be triggered again every time a new child is added. The `DataSnapshot` passed into the callback will reflect the data for the relevant child. For ordering purposes, it is passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child. |
| [onChildAdded(query, callback, cancelCallback, options)](https://firebase.google.com/docs/reference/js/database.md#onchildadded_456d092) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildAdded` event will be triggered once for each initial child at this location, and it will be triggered again every time a new child is added. The `DataSnapshot` passed into the callback will reflect the data for the relevant child. For ordering purposes, it is passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child. |
| [onChildChanged(query, callback, cancelCallback)](https://firebase.google.com/docs/reference/js/database.md#onchildchanged_c1edf58) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildChanged` event will be triggered when the data stored in a child (or any of its descendants) changes. Note that a single `child_changed` event may represent multiple changes to the child. The `DataSnapshot` passed to the callback will contain the new child contents. For ordering purposes, the callback is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child. |
| [onChildChanged(query, callback, options)](https://firebase.google.com/docs/reference/js/database.md#onchildchanged_cf4f177) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildChanged` event will be triggered when the data stored in a child (or any of its descendants) changes. Note that a single `child_changed` event may represent multiple changes to the child. The `DataSnapshot` passed to the callback will contain the new child contents. For ordering purposes, the callback is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child. |
| [onChildChanged(query, callback, cancelCallback, options)](https://firebase.google.com/docs/reference/js/database.md#onchildchanged_456d092) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildChanged` event will be triggered when the data stored in a child (or any of its descendants) changes. Note that a single `child_changed` event may represent multiple changes to the child. The `DataSnapshot` passed to the callback will contain the new child contents. For ordering purposes, the callback is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child. |
| [onChildMoved(query, callback, cancelCallback)](https://firebase.google.com/docs/reference/js/database.md#onchildmoved_c1edf58) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildMoved` event will be triggered when a child's sort order changes such that its position relative to its siblings changes. The `DataSnapshot` passed to the callback will be for the data of the child that has moved. It is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child. |
| [onChildMoved(query, callback, options)](https://firebase.google.com/docs/reference/js/database.md#onchildmoved_cf4f177) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildMoved` event will be triggered when a child's sort order changes such that its position relative to its siblings changes. The `DataSnapshot` passed to the callback will be for the data of the child that has moved. It is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child. |
| [onChildMoved(query, callback, cancelCallback, options)](https://firebase.google.com/docs/reference/js/database.md#onchildmoved_456d092) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildMoved` event will be triggered when a child's sort order changes such that its position relative to its siblings changes. The `DataSnapshot` passed to the callback will be for the data of the child that has moved. It is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child. |
| [onChildRemoved(query, callback, cancelCallback)](https://firebase.google.com/docs/reference/js/database.md#onchildremoved_47c1ae9) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildRemoved` event will be triggered once every time a child is removed. The `DataSnapshot` passed into the callback will be the old data for the child that was removed. A child will get removed when either:- a client explicitly calls `remove()` on that child or one of its ancestors - a client calls `set(null)` on that child or one of its ancestors - that child has all of its children removed - there is a query in effect which now filters out the child (because it's sort order changed or the max limit was hit) |
| [onChildRemoved(query, callback, options)](https://firebase.google.com/docs/reference/js/database.md#onchildremoved_7357cb6) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildRemoved` event will be triggered once every time a child is removed. The `DataSnapshot` passed into the callback will be the old data for the child that was removed. A child will get removed when either:- a client explicitly calls `remove()` on that child or one of its ancestors - a client calls `set(null)` on that child or one of its ancestors - that child has all of its children removed - there is a query in effect which now filters out the child (because it's sort order changed or the max limit was hit) |
| [onChildRemoved(query, callback, cancelCallback, options)](https://firebase.google.com/docs/reference/js/database.md#onchildremoved_e66d5b6) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onChildRemoved` event will be triggered once every time a child is removed. The `DataSnapshot` passed into the callback will be the old data for the child that was removed. A child will get removed when either:- a client explicitly calls `remove()` on that child or one of its ancestors - a client calls `set(null)` on that child or one of its ancestors - that child has all of its children removed - there is a query in effect which now filters out the child (because it's sort order changed or the max limit was hit) |
| [onValue(query, callback, cancelCallback)](https://firebase.google.com/docs/reference/js/database.md#onvalue_47c1ae9) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onValue` event will trigger once with the initial data stored at this location, and then trigger again each time the data changes. The `DataSnapshot` passed to the callback will be for the location at which `on()` was called. It won't trigger until the entire contents has been synchronized. If the location has no data, it will be triggered with an empty `DataSnapshot` (`val()` will return `null`). |
| [onValue(query, callback, options)](https://firebase.google.com/docs/reference/js/database.md#onvalue_7357cb6) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onValue` event will trigger once with the initial data stored at this location, and then trigger again each time the data changes. The `DataSnapshot` passed to the callback will be for the location at which `on()` was called. It won't trigger until the entire contents has been synchronized. If the location has no data, it will be triggered with an empty `DataSnapshot` (`val()` will return `null`). |
| [onValue(query, callback, cancelCallback, options)](https://firebase.google.com/docs/reference/js/database.md#onvalue_e66d5b6) | Listens for data changes at a particular location.This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.An `onValue` event will trigger once with the initial data stored at this location, and then trigger again each time the data changes. The `DataSnapshot` passed to the callback will be for the location at which `on()` was called. It won't trigger until the entire contents has been synchronized. If the location has no data, it will be triggered with an empty `DataSnapshot` (`val()` will return `null`). |
| [query(query, queryConstraints)](https://firebase.google.com/docs/reference/js/database.md#query_870e07a) | Creates a new immutable instance of `Query` that is extended to also include additional query constraints. |
| **function(ref, ...)** |   |
| [onDisconnect(ref)](https://firebase.google.com/docs/reference/js/database.md#ondisconnect_8616c19) | Returns an `OnDisconnect` object - see [Enabling Offline Capabilities in JavaScript](https://firebase.google.com/docs/database/web/offline-capabilities) for more information on how to use it. |
| [remove(ref)](https://firebase.google.com/docs/reference/js/database.md#remove_8616c19) | Removes the data at this Database location.Any data at child locations will also be deleted.The effect of the remove will be visible immediately and the corresponding event 'value' will be triggered. Synchronization of the remove to the Firebase servers will also be started, and the returned Promise will resolve when complete. If provided, the onComplete callback will be called asynchronously after synchronization has finished. |
| [runTransaction(ref, transactionUpdate, options)](https://firebase.google.com/docs/reference/js/database.md#runtransaction_a3641e5) | Atomically modifies the data at this location.Atomically modify the data at this location. Unlike a normal `set()`, which just overwrites the data regardless of its previous value, `runTransaction()` is used to modify the existing value to a new value, ensuring there are no conflicts with other clients writing to the same location at the same time.To accomplish this, you pass `runTransaction()` an update function which is used to transform the current value into a new value. If another client writes to the location before your new value is successfully written, your update function will be called again with the new current value, and the write will be retried. This will happen repeatedly until your write succeeds without conflict or you abort the transaction by not returning a value from your update function.Note: Modifying data with `set()` will cancel any pending transactions at that location, so extreme care should be taken if mixing `set()` and `runTransaction()` to update the same data.Note: When using transactions with Security and Firebase Rules in place, be aware that a client needs `.read` access in addition to `.write` access in order to perform a transaction. This is because the client-side nature of transactions requires the client to read the data in order to transactionally update it. |
| [set(ref, value)](https://firebase.google.com/docs/reference/js/database.md#set_c9eacde) | Writes data to this Database location.This will overwrite any data at this location and all child locations.The effect of the write will be visible immediately, and the corresponding events ("value", "child_added", etc.) will be triggered. Synchronization of the data to the Firebase servers will also be started, and the returned Promise will resolve when complete. If provided, the `onComplete` callback will be called asynchronously after synchronization has finished.Passing `null` for the new value is equivalent to calling `remove()`; namely, all data at this location and all child locations will be deleted.`set()` will remove any priority stored at this location, so if priority is meant to be preserved, you need to use `setWithPriority()` instead.Note that modifying data with `set()` will cancel any pending transactions at that location, so extreme care should be taken if mixing `set()` and `transaction()` to modify the same data.A single `set()` will generate a single "value" event at the location where the `set()` was performed. |
| [setPriority(ref, priority)](https://firebase.google.com/docs/reference/js/database.md#setpriority_f979832) | Sets a priority for the data at this Database location.Applications need not use priority but can order collections by ordinary properties (see [Sorting and filtering data](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data) ). |
| [setWithPriority(ref, value, priority)](https://firebase.google.com/docs/reference/js/database.md#setwithpriority_dc560e7) | Writes data the Database location. Like `set()` but also specifies the priority for that data.Applications need not use priority but can order collections by ordinary properties (see [Sorting and filtering data](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data) ). |
| [update(ref, values)](https://firebase.google.com/docs/reference/js/database.md#update_06756b7) | Writes multiple values to the Database at once.The `values` argument contains multiple property-value pairs that will be written to the Database together. Each child property can either be a simple property (for example, "name") or a relative path (for example, "name/first") from the current location to the data to update.As opposed to the `set()` method, `update()` can be use to selectively update only the referenced properties at the current location (instead of replacing all the child properties at the current location).The effect of the write will be visible immediately, and the corresponding events ('value', 'child_added', etc.) will be triggered. Synchronization of the data to the Firebase servers will also be started, and the returned Promise will resolve when complete. If provided, the `onComplete` callback will be called asynchronously after synchronization has finished.A single `update()` will generate a single "value" event at the location where the `update()` was performed, regardless of how many children were modified.Note that modifying data with `update()` will cancel any pending transactions at that location, so extreme care should be taken if mixing `update()` and `transaction()` to modify the same data.Passing `null` to `update()` will remove the data at this location.See [Introducing multi-location updates and more](https://firebase.googleblog.com/2015/09/introducing-multi-location-updates-and_86.html). |
| **function(value, ...)** |   |
| [endAt(value, key)](https://firebase.google.com/docs/reference/js/database.md#endat_51c2c8b) | Creates a `QueryConstraint` with the specified ending point.Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()` allows you to choose arbitrary starting and ending points for your queries.The ending point is inclusive, so children with exactly the specified value will be included in the query. The optional key argument can be used to further limit the range of the query. If it is specified, then children that have exactly the specified value must also have a key name less than or equal to the specified key.You can read more about `endAt()` in [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data). |
| [endBefore(value, key)](https://firebase.google.com/docs/reference/js/database.md#endbefore_51c2c8b) | Creates a `QueryConstraint` with the specified ending point (exclusive).Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()` allows you to choose arbitrary starting and ending points for your queries.The ending point is exclusive. If only a value is provided, children with a value less than the specified value will be included in the query. If a key is specified, then children must have a value less than or equal to the specified value and a key name less than the specified key. |
| [equalTo(value, key)](https://firebase.google.com/docs/reference/js/database.md#equalto_51c2c8b) | Creates a `QueryConstraint` that includes children that match the specified value.Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()` allows you to choose arbitrary starting and ending points for your queries.The optional key argument can be used to further limit the range of the query. If it is specified, then children that have exactly the specified value must also have exactly the specified key as their key name. This can be used to filter result sets with many matches for the same value.You can read more about `equalTo()` in [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data). |
| [startAfter(value, key)](https://firebase.google.com/docs/reference/js/database.md#startafter_51c2c8b) | Creates a `QueryConstraint` with the specified starting point (exclusive).Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()` allows you to choose arbitrary starting and ending points for your queries.The starting point is exclusive. If only a value is provided, children with a value greater than the specified value will be included in the query. If a key is specified, then children must have a value greater than or equal to the specified value and a a key name greater than the specified key. |
| [startAt(value, key)](https://firebase.google.com/docs/reference/js/database.md#startat_51c2c8b) | Creates a `QueryConstraint` with the specified starting point.Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()` allows you to choose arbitrary starting and ending points for your queries.The starting point is inclusive, so children with exactly the specified value will be included in the query. The optional key argument can be used to further limit the range of the query. If it is specified, then children that have exactly the specified value must also have a key name greater than or equal to the specified key.You can read more about `startAt()` in [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data). |

## Classes

| Class | Description |
|---|---|
| [Database](https://firebase.google.com/docs/reference/js/database.database.md#database_class) | Class representing a Firebase Realtime Database. |
| [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class) | A `DataSnapshot` contains data from a Database location.Any time you read data from the Database, you receive the data as a `DataSnapshot`. A `DataSnapshot` is passed to the event callbacks you attach with `on()` or `once()`. You can extract the contents of the snapshot as a JavaScript object by calling the `val()` method. Alternatively, you can traverse into the snapshot by calling `child()` to return child snapshots (which you could then call `val()` on).A `DataSnapshot` is an efficiently generated, immutable copy of the data at a Database location. It cannot be modified and will never change (to modify data, you always call the `set()` method on a `Reference` directly). |
| [OnDisconnect](https://firebase.google.com/docs/reference/js/database.ondisconnect.md#ondisconnect_class) | The `onDisconnect` class allows you to write or clear data when your client disconnects from the Database server. These updates occur whether your client disconnects cleanly or not, so you can rely on them to clean up data even if a connection is dropped or a client crashes.The `onDisconnect` class is most commonly used to manage presence in applications where it is useful to detect how many clients are connected and when other clients disconnect. See [Enabling Offline Capabilities in JavaScript](https://firebase.google.com/docs/database/web/offline-capabilities) for more information.To avoid problems when a connection is dropped before the requests can be transferred to the Database server, these functions should be called before writing any data.Note that `onDisconnect` operations are only triggered once. If you want an operation to occur each time a disconnect occurs, you'll need to re-establish the `onDisconnect` operations each time you reconnect. |
| [QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class) | A `QueryConstraint` is used to narrow the set of documents returned by a Database query. `QueryConstraint`s are created by invoking [endAt()](https://firebase.google.com/docs/reference/js/database.md#endat_51c2c8b), [endBefore()](https://firebase.google.com/docs/reference/js/database.md#endbefore_51c2c8b), [startAt()](https://firebase.google.com/docs/reference/js/database.md#startat_51c2c8b), [startAfter()](https://firebase.google.com/docs/reference/js/database.md#startafter_51c2c8b), [limitToFirst()](https://firebase.google.com/docs/reference/js/database.md#limittofirst_ec46c78), [limitToLast()](https://firebase.google.com/docs/reference/js/database.md#limittolast_ec46c78), [orderByChild()](https://firebase.google.com/docs/reference/js/database.md#orderbychild_fe1f8e4), [orderByChild()](https://firebase.google.com/docs/reference/js/database.md#orderbychild_fe1f8e4), [orderByKey()](https://firebase.google.com/docs/reference/js/database.md#orderbykey) , [orderByPriority()](https://firebase.google.com/docs/reference/js/database.md#orderbypriority) , [orderByValue()](https://firebase.google.com/docs/reference/js/database.md#orderbyvalue) or [equalTo()](https://firebase.google.com/docs/reference/js/database.md#equalto_51c2c8b) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/database.md#query_870e07a) to create a new query instance that also contains this `QueryConstraint`. |
| [TransactionResult](https://firebase.google.com/docs/reference/js/database.transactionresult.md#transactionresult_class) | A type for the resolve value of [runTransaction()](https://firebase.google.com/docs/reference/js/database.md#runtransaction_a3641e5). |

## Interfaces

| Interface | Description |
|---|---|
| [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | A `DatabaseReference` represents a specific location in your Database and can be used for reading or writing data to that Database location.You can reference the root or child location in your Database by calling `ref()` or `ref("child/path")`.Writing is done with the `set()` method and reading can be done with the `on*()` method. See <https://firebase.google.com/docs/database/web/read-and-write> |
| [IteratedDataSnapshot](https://firebase.google.com/docs/reference/js/database.iterateddatasnapshot.md#iterateddatasnapshot_interface) | Represents a child snapshot of a `Reference` that is being iterated over. The key will never be undefined. |
| [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An options objects that can be used to customize a listener. |
| [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | A `Query` sorts and filters the data at a Database location so only a subset of the child data is included. This can be used to order a collection of data by some attribute (for example, height of dinosaurs) as well as to restrict a large list of items (for example, chat messages) down to a number suitable for synchronizing to the client. Queries are created by chaining together one or more of the filter methods defined here.Just as with a `DatabaseReference`, you can receive data from a `Query` by using the `on*()` methods. You will only receive events and `DataSnapshot`s for the subset of the data that matches your query.See <https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data> for more information. |
| [ThenableReference](https://firebase.google.com/docs/reference/js/database.thenablereference.md#thenablereference_interface) | A `Promise` that can also act as a `DatabaseReference` when returned by [push()](https://firebase.google.com/docs/reference/js/database.md#push_c74661c). The reference is available immediately and the `Promise` resolves as the write to the backend completes. |
| [TransactionOptions](https://firebase.google.com/docs/reference/js/database.transactionoptions.md#transactionoptions_interface) | An options object to configure transactions. |

## Type Aliases

| Type Alias | Description |
|---|---|
| [EventType](https://firebase.google.com/docs/reference/js/database.md#eventtype) | One of the following strings: "value", "child_added", "child_changed", "child_removed", or "child_moved." |
| [QueryConstraintType](https://firebase.google.com/docs/reference/js/database.md#queryconstrainttype) | Describes the different query constraints available in this SDK. |
| [Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe) | A callback that can invoked to remove a listener. |

## function(app, ...)

### getDatabase(app, url)

Returns the instance of the Realtime Database SDK that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). Initializes a new instance with default settings if no instance exists or if the existing instance uses a custom database URL.

**Signature:**

    export declare function getDatabase(app?: FirebaseApp, url?: string): Database;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance that the returned Realtime Database instance is associated with. |
| url | string | The URL of the Realtime Database instance to connect to. If not provided, the SDK connects to the default instance of the Firebase App. |

**Returns:**

[Database](https://firebase.google.com/docs/reference/js/database.database.md#database_class)

The `Database` instance of the provided app.

## function(db, ...)

### connectDatabaseEmulator(db, host, port, options)

Modify the provided instance to communicate with the Realtime Database emulator.

<br />

Note: This method must be called before performing any other operation.

**Signature:**

    export declare function connectDatabaseEmulator(db: Database, host: string, port: number, options?: {
        mockUserToken?: EmulatorMockTokenOptions | string;
    }): void;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| db | [Database](https://firebase.google.com/docs/reference/js/database.database.md#database_class) | The instance to modify. |
| host | string | The emulator host (ex: localhost) |
| port | number | The emulator port (ex: 8080) |
| options | { mockUserToken?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/util.md#emulatormocktokenoptions) \| string; } |   |

**Returns:**

void

### goOffline(db)

Disconnects from the server (all Database operations will be completed offline).

The client automatically maintains a persistent connection to the Database server, which will remain active indefinitely and reconnect when disconnected. However, the `goOffline()` and `goOnline()` methods may be used to control the client connection in cases where a persistent connection is undesirable.

While offline, the client will no longer receive data updates from the Database. However, all Database operations performed locally will continue to immediately fire events, allowing your application to continue behaving normally. Additionally, each operation performed locally will automatically be queued and retried upon reconnection to the Database server.

To reconnect to the Database and begin receiving remote events, see `goOnline()`.

**Signature:**

    export declare function goOffline(db: Database): void;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| db | [Database](https://firebase.google.com/docs/reference/js/database.database.md#database_class) | The instance to disconnect. |

**Returns:**

void

### goOnline(db)

Reconnects to the server and synchronizes the offline Database state with the server state.

This method should be used after disabling the active connection with `goOffline()`. Once reconnected, the client will transmit the proper data and fire the appropriate events so that your client "catches up" automatically.

**Signature:**

    export declare function goOnline(db: Database): void;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| db | [Database](https://firebase.google.com/docs/reference/js/database.database.md#database_class) | The instance to reconnect. |

**Returns:**

void

### ref(db, path)

Returns a `Reference` representing the location in the Database corresponding to the provided path. If no path is provided, the `Reference` will point to the root of the Database.

**Signature:**

    export declare function ref(db: Database, path?: string): DatabaseReference;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| db | [Database](https://firebase.google.com/docs/reference/js/database.database.md#database_class) | The database instance to obtain a reference for. |
| path | string | Optional path representing the location the returned `Reference` will point. If not provided, the returned `Reference` will point to the root of the Database. |

**Returns:**

[DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface)

If a path is provided, a `Reference` pointing to the provided path. Otherwise, a `Reference` pointing to the root of the Database.

### refFromURL(db, url)

Returns a `Reference` representing the location in the Database corresponding to the provided Firebase URL.

An exception is thrown if the URL is not a valid Firebase Database URL or it has a different domain than the current `Database` instance.

Note that all query parameters (`orderBy`, `limitToLast`, etc.) are ignored and are not applied to the returned `Reference`.

**Signature:**

    export declare function refFromURL(db: Database, url: string): DatabaseReference;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| db | [Database](https://firebase.google.com/docs/reference/js/database.database.md#database_class) | The database instance to obtain a reference for. |
| url | string | The Firebase URL at which the returned `Reference` will point. |

**Returns:**

[DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface)

A `Reference` pointing to the provided Firebase URL.

## function()

### forceLongPolling()

Force the use of longPolling instead of websockets. This will be ignored if websocket protocol is used in databaseURL.

**Signature:**

    export declare function forceLongPolling(): void;

**Returns:**

void

### forceWebSockets()

Force the use of websockets instead of longPolling.

**Signature:**

    export declare function forceWebSockets(): void;

**Returns:**

void

### orderByKey()

Creates a new `QueryConstraint` that orders by the key.

Sorts the results of a query by their (ascending) key values.

You can read more about `orderByKey()` in [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data).

**Signature:**

    export declare function orderByKey(): QueryConstraint;

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

### orderByPriority()

Creates a new `QueryConstraint` that orders by priority.

Applications need not use priority but can order collections by ordinary properties (see [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data) for alternatives to priority.

**Signature:**

    export declare function orderByPriority(): QueryConstraint;

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

### orderByValue()

Creates a new `QueryConstraint` that orders by value.

If the children of a query are all scalar values (string, number, or boolean), you can order the results by their (ascending) values.

You can read more about `orderByValue()` in [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data).

**Signature:**

    export declare function orderByValue(): QueryConstraint;

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

### serverTimestamp()

Returns a placeholder value for auto-populating the current timestamp (time since the Unix epoch, in milliseconds) as determined by the Firebase servers.

**Signature:**

    export declare function serverTimestamp(): object;

**Returns:**

object

## function(delta, ...)

### increment(delta)

Returns a placeholder value that can be used to atomically increment the current database value by the provided delta.

**Signature:**

    export declare function increment(delta: number): object;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| delta | number | the amount to modify the current value atomically. |

**Returns:**

object

A placeholder value for modifying data atomically server-side.

## function(enabled, ...)

### enableLogging(enabled, persistent)

Logs debugging information to the console.

**Signature:**

    export declare function enableLogging(enabled: boolean, persistent?: boolean): any;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| enabled | boolean | Enables logging if `true`, disables logging if `false`. |
| persistent | boolean | Remembers the logging state between page refreshes if `true`. |

**Returns:**

any

## function(limit, ...)

### limitToFirst(limit)

Creates a new `QueryConstraint` that if limited to the first specific number of children.

The `limitToFirst()` method is used to set a maximum number of children to be synced for a given callback. If we set a limit of 100, we will initially only receive up to 100 `child_added` events. If we have fewer than 100 messages stored in our Database, a `child_added` event will fire for each message. However, if we have over 100 messages, we will only receive a `child_added` event for the first 100 ordered messages. As items change, we will receive `child_removed` events for each item that drops out of the active list so that the total number stays at 100.

You can read more about `limitToFirst()` in [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

**Signature:**

    export declare function limitToFirst(limit: number): QueryConstraint;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| limit | number | The maximum number of nodes to include in this query. |

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

### limitToLast(limit)

Creates a new `QueryConstraint` that is limited to return only the last specified number of children.

The `limitToLast()` method is used to set a maximum number of children to be synced for a given callback. If we set a limit of 100, we will initially only receive up to 100 `child_added` events. If we have fewer than 100 messages stored in our Database, a `child_added` event will fire for each message. However, if we have over 100 messages, we will only receive a `child_added` event for the last 100 ordered messages. As items change, we will receive `child_removed` events for each item that drops out of the active list so that the total number stays at 100.

You can read more about `limitToLast()` in [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

**Signature:**

    export declare function limitToLast(limit: number): QueryConstraint;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| limit | number | The maximum number of nodes to include in this query. |

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

## function(logger, ...)

### enableLogging(logger)

Logs debugging information to the console.

**Signature:**

    export declare function enableLogging(logger: (message: string) => unknown): any;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| logger | (message: string) =\> unknown | A custom logger function to control how things get logged. |

**Returns:**

any

## function(parent, ...)

### child(parent, path)

Gets a `Reference` for the location at the specified relative path.

The relative path can either be a simple child name (for example, "ada") or a deeper slash-separated path (for example, "ada/name/first").

**Signature:**

    export declare function child(parent: DatabaseReference, path: string): DatabaseReference;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| parent | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The parent location. |
| path | string | A relative path from this location to the desired child location. |

**Returns:**

[DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface)

The specified child location.

### push(parent, value)

Generates a new child location using a unique key and returns its `Reference`.

This is the most common pattern for adding data to a collection of items.

If you provide a value to `push()`, the value is written to the generated location. If you don't pass a value, nothing is written to the database and the child remains empty (but you can use the `Reference` elsewhere).

The unique keys generated by `push()` are ordered by the current time, so the resulting list of items is chronologically sorted. The keys are also designed to be unguessable (they contain 72 random bits of entropy).

See [Append to a list of data](https://firebase.google.com/docs/database/web/lists-of-data#append_to_a_list_of_data). See [The 2\^120 Ways to Ensure Unique Identifiers](https://firebase.googleblog.com/2015/02/the-2120-ways-to-ensure-unique_68.html).

**Signature:**

    export declare function push(parent: DatabaseReference, value?: unknown): ThenableReference;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| parent | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The parent location. |
| value | unknown | Optional value to be written at the generated location. |

**Returns:**

[ThenableReference](https://firebase.google.com/docs/reference/js/database.thenablereference.md#thenablereference_interface)

Combined `Promise` and `Reference`; resolves when write is complete, but can be used immediately as the `Reference` to the child location.

## function(path, ...)

### orderByChild(path)

Creates a new `QueryConstraint` that orders by the specified child key.

Queries can only order by one key at a time. Calling `orderByChild()` multiple times on the same query is an error.

Firebase queries allow you to order your data by any child key on the fly. However, if you know in advance what your indexes will be, you can define them via the .indexOn rule in your Security Rules for better performance. See the<https://firebase.google.com/docs/database/security/indexing-data> rule for more information.

You can read more about `orderByChild()` in [Sort data](https://firebase.google.com/docs/database/web/lists-of-data#sort_data).

**Signature:**

    export declare function orderByChild(path: string): QueryConstraint;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| path | string | The path to order by. |

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

## function(query, ...)

### get(query)

Gets the most up-to-date result for this query.

**Signature:**

    export declare function get(query: Query): Promise<DataSnapshot>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |

**Returns:**

Promise\<[DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class)\>

A `Promise` which resolves to the resulting DataSnapshot if a value is available, or rejects if the client is unable to return a value (e.g., if the server is unreachable and there is nothing cached).

### off(query, eventType, callback)

Detaches a callback previously attached with the corresponding `on*()` (`onValue`, `onChildAdded`) listener. Note: This is not the recommended way to remove a listener. Instead, please use the returned callback function from the respective `on*` callbacks.

Detach a callback previously attached with `on*()`. Calling `off()` on a parent listener will not automatically remove listeners registered on child nodes, `off()` must also be called on any child listeners to remove the callback.

If a callback is not specified, all callbacks for the specified eventType will be removed. Similarly, if no eventType is specified, all callbacks for the `Reference` will be removed.

Individual listeners can also be removed by invoking their unsubscribe callbacks.

**Signature:**

    export declare function off(query: Query, eventType?: EventType, callback?: (snapshot: DataSnapshot, previousChildName?: string | null) => unknown): void;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query that the listener was registered with. |
| eventType | [EventType](https://firebase.google.com/docs/reference/js/database.md#eventtype) | One of the following strings: "value", "child_added", "child_changed", "child_removed", or "child_moved." If omitted, all callbacks for the `Reference` will be removed. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class), previousChildName?: string \| null) =\> unknown | The callback function that was passed to `on()` or `undefined` to remove all callbacks. |

**Returns:**

void

### onChildAdded(query, callback, cancelCallback)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildAdded` event will be triggered once for each initial child at this location, and it will be triggered again every time a new child is added. The `DataSnapshot` passed into the callback will reflect the data for the relevant child. For ordering purposes, it is passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child.

**Signature:**

    export declare function onChildAdded(query: Query, callback: (snapshot: DataSnapshot, previousChildName?: string | null) => unknown, cancelCallback?: (error: Error) => unknown): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class), previousChildName?: string \| null) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| cancelCallback | (error: Error) =\> unknown | An optional callback that will be notified if your event subscription is ever canceled because your client does not have permission to read this data (or it had permission but has now lost it). This callback will be passed an `Error` object indicating why the failure occurred. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildAdded(query, callback, options)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildAdded` event will be triggered once for each initial child at this location, and it will be triggered again every time a new child is added. The `DataSnapshot` passed into the callback will reflect the data for the relevant child. For ordering purposes, it is passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child.

**Signature:**

    export declare function onChildAdded(query: Query, callback: (snapshot: DataSnapshot, previousChildName: string | null) => unknown, options: ListenOptions): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class), previousChildName: string \| null) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| options | [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An object that can be used to configure `onlyOnce`, which then removes the listener after its first invocation. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildAdded(query, callback, cancelCallback, options)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildAdded` event will be triggered once for each initial child at this location, and it will be triggered again every time a new child is added. The `DataSnapshot` passed into the callback will reflect the data for the relevant child. For ordering purposes, it is passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child.

**Signature:**

    export declare function onChildAdded(query: Query, callback: (snapshot: DataSnapshot, previousChildName: string | null) => unknown, cancelCallback: (error: Error) => unknown, options: ListenOptions): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class), previousChildName: string \| null) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| cancelCallback | (error: Error) =\> unknown | An optional callback that will be notified if your event subscription is ever canceled because your client does not have permission to read this data (or it had permission but has now lost it). This callback will be passed an `Error` object indicating why the failure occurred. |
| options | [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An object that can be used to configure `onlyOnce`, which then removes the listener after its first invocation. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildChanged(query, callback, cancelCallback)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildChanged` event will be triggered when the data stored in a child (or any of its descendants) changes. Note that a single `child_changed` event may represent multiple changes to the child. The `DataSnapshot` passed to the callback will contain the new child contents. For ordering purposes, the callback is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child.

**Signature:**

    export declare function onChildChanged(query: Query, callback: (snapshot: DataSnapshot, previousChildName: string | null) => unknown, cancelCallback?: (error: Error) => unknown): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class), previousChildName: string \| null) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| cancelCallback | (error: Error) =\> unknown | An optional callback that will be notified if your event subscription is ever canceled because your client does not have permission to read this data (or it had permission but has now lost it). This callback will be passed an `Error` object indicating why the failure occurred. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildChanged(query, callback, options)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildChanged` event will be triggered when the data stored in a child (or any of its descendants) changes. Note that a single `child_changed` event may represent multiple changes to the child. The `DataSnapshot` passed to the callback will contain the new child contents. For ordering purposes, the callback is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child.

**Signature:**

    export declare function onChildChanged(query: Query, callback: (snapshot: DataSnapshot, previousChildName: string | null) => unknown, options: ListenOptions): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class), previousChildName: string \| null) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| options | [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An object that can be used to configure `onlyOnce`, which then removes the listener after its first invocation. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildChanged(query, callback, cancelCallback, options)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildChanged` event will be triggered when the data stored in a child (or any of its descendants) changes. Note that a single `child_changed` event may represent multiple changes to the child. The `DataSnapshot` passed to the callback will contain the new child contents. For ordering purposes, the callback is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child.

**Signature:**

    export declare function onChildChanged(query: Query, callback: (snapshot: DataSnapshot, previousChildName: string | null) => unknown, cancelCallback: (error: Error) => unknown, options: ListenOptions): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class), previousChildName: string \| null) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| cancelCallback | (error: Error) =\> unknown | An optional callback that will be notified if your event subscription is ever canceled because your client does not have permission to read this data (or it had permission but has now lost it). This callback will be passed an `Error` object indicating why the failure occurred. |
| options | [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An object that can be used to configure `onlyOnce`, which then removes the listener after its first invocation. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildMoved(query, callback, cancelCallback)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildMoved` event will be triggered when a child's sort order changes such that its position relative to its siblings changes. The `DataSnapshot` passed to the callback will be for the data of the child that has moved. It is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child.

**Signature:**

    export declare function onChildMoved(query: Query, callback: (snapshot: DataSnapshot, previousChildName: string | null) => unknown, cancelCallback?: (error: Error) => unknown): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class), previousChildName: string \| null) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| cancelCallback | (error: Error) =\> unknown | An optional callback that will be notified if your event subscription is ever canceled because your client does not have permission to read this data (or it had permission but has now lost it). This callback will be passed an `Error` object indicating why the failure occurred. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildMoved(query, callback, options)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildMoved` event will be triggered when a child's sort order changes such that its position relative to its siblings changes. The `DataSnapshot` passed to the callback will be for the data of the child that has moved. It is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child.

**Signature:**

    export declare function onChildMoved(query: Query, callback: (snapshot: DataSnapshot, previousChildName: string | null) => unknown, options: ListenOptions): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class), previousChildName: string \| null) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| options | [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An object that can be used to configure `onlyOnce`, which then removes the listener after its first invocation. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildMoved(query, callback, cancelCallback, options)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildMoved` event will be triggered when a child's sort order changes such that its position relative to its siblings changes. The `DataSnapshot` passed to the callback will be for the data of the child that has moved. It is also passed a second argument which is a string containing the key of the previous sibling child by sort order, or `null` if it is the first child.

**Signature:**

    export declare function onChildMoved(query: Query, callback: (snapshot: DataSnapshot, previousChildName: string | null) => unknown, cancelCallback: (error: Error) => unknown, options: ListenOptions): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class), previousChildName: string \| null) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| cancelCallback | (error: Error) =\> unknown | An optional callback that will be notified if your event subscription is ever canceled because your client does not have permission to read this data (or it had permission but has now lost it). This callback will be passed an `Error` object indicating why the failure occurred. |
| options | [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An object that can be used to configure `onlyOnce`, which then removes the listener after its first invocation. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildRemoved(query, callback, cancelCallback)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildRemoved` event will be triggered once every time a child is removed. The `DataSnapshot` passed into the callback will be the old data for the child that was removed. A child will get removed when either:

- a client explicitly calls `remove()` on that child or one of its ancestors - a client calls `set(null)` on that child or one of its ancestors - that child has all of its children removed - there is a query in effect which now filters out the child (because it's sort order changed or the max limit was hit)

**Signature:**

    export declare function onChildRemoved(query: Query, callback: (snapshot: DataSnapshot) => unknown, cancelCallback?: (error: Error) => unknown): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class)) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| cancelCallback | (error: Error) =\> unknown | An optional callback that will be notified if your event subscription is ever canceled because your client does not have permission to read this data (or it had permission but has now lost it). This callback will be passed an `Error` object indicating why the failure occurred. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildRemoved(query, callback, options)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildRemoved` event will be triggered once every time a child is removed. The `DataSnapshot` passed into the callback will be the old data for the child that was removed. A child will get removed when either:

- a client explicitly calls `remove()` on that child or one of its ancestors - a client calls `set(null)` on that child or one of its ancestors - that child has all of its children removed - there is a query in effect which now filters out the child (because it's sort order changed or the max limit was hit)

**Signature:**

    export declare function onChildRemoved(query: Query, callback: (snapshot: DataSnapshot) => unknown, options: ListenOptions): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class)) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| options | [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An object that can be used to configure `onlyOnce`, which then removes the listener after its first invocation. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onChildRemoved(query, callback, cancelCallback, options)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onChildRemoved` event will be triggered once every time a child is removed. The `DataSnapshot` passed into the callback will be the old data for the child that was removed. A child will get removed when either:

- a client explicitly calls `remove()` on that child or one of its ancestors - a client calls `set(null)` on that child or one of its ancestors - that child has all of its children removed - there is a query in effect which now filters out the child (because it's sort order changed or the max limit was hit)

**Signature:**

    export declare function onChildRemoved(query: Query, callback: (snapshot: DataSnapshot) => unknown, cancelCallback: (error: Error) => unknown, options: ListenOptions): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class)) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot and a string containing the key of the previous child, by sort order, or `null` if it is the first child. |
| cancelCallback | (error: Error) =\> unknown | An optional callback that will be notified if your event subscription is ever canceled because your client does not have permission to read this data (or it had permission but has now lost it). This callback will be passed an `Error` object indicating why the failure occurred. |
| options | [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An object that can be used to configure `onlyOnce`, which then removes the listener after its first invocation. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onValue(query, callback, cancelCallback)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onValue` event will trigger once with the initial data stored at this location, and then trigger again each time the data changes. The `DataSnapshot` passed to the callback will be for the location at which `on()` was called. It won't trigger until the entire contents has been synchronized. If the location has no data, it will be triggered with an empty `DataSnapshot` (`val()` will return `null`).

**Signature:**

    export declare function onValue(query: Query, callback: (snapshot: DataSnapshot) => unknown, cancelCallback?: (error: Error) => unknown): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class)) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot. |
| cancelCallback | (error: Error) =\> unknown | An optional callback that will be notified if your event subscription is ever canceled because your client does not have permission to read this data (or it had permission but has now lost it). This callback will be passed an `Error` object indicating why the failure occurred. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onValue(query, callback, options)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onValue` event will trigger once with the initial data stored at this location, and then trigger again each time the data changes. The `DataSnapshot` passed to the callback will be for the location at which `on()` was called. It won't trigger until the entire contents has been synchronized. If the location has no data, it will be triggered with an empty `DataSnapshot` (`val()` will return `null`).

**Signature:**

    export declare function onValue(query: Query, callback: (snapshot: DataSnapshot) => unknown, options: ListenOptions): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class)) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot. |
| options | [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An object that can be used to configure `onlyOnce`, which then removes the listener after its first invocation. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### onValue(query, callback, cancelCallback, options)

Listens for data changes at a particular location.

This is the primary way to read data from a Database. Your callback will be triggered for the initial data and again whenever the data changes. Invoke the returned unsubscribe callback to stop receiving updates. See [Retrieve Data on the Web](https://firebase.google.com/docs/database/web/retrieve-data) for more details.

An `onValue` event will trigger once with the initial data stored at this location, and then trigger again each time the data changes. The `DataSnapshot` passed to the callback will be for the location at which `on()` was called. It won't trigger until the entire contents has been synchronized. If the location has no data, it will be triggered with an empty `DataSnapshot` (`val()` will return `null`).

**Signature:**

    export declare function onValue(query: Query, callback: (snapshot: DataSnapshot) => unknown, cancelCallback: (error: Error) => unknown, options: ListenOptions): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The query to run. |
| callback | (snapshot: [DataSnapshot](https://firebase.google.com/docs/reference/js/database.datasnapshot.md#datasnapshot_class)) =\> unknown | A callback that fires when the specified event occurs. The callback will be passed a DataSnapshot. |
| cancelCallback | (error: Error) =\> unknown | An optional callback that will be notified if your event subscription is ever canceled because your client does not have permission to read this data (or it had permission but has now lost it). This callback will be passed an `Error` object indicating why the failure occurred. |
| options | [ListenOptions](https://firebase.google.com/docs/reference/js/database.listenoptions.md#listenoptions_interface) | An object that can be used to configure `onlyOnce`, which then removes the listener after its first invocation. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/database.md#unsubscribe)

A function that can be invoked to remove the listener.

### query(query, queryConstraints)

Creates a new immutable instance of `Query` that is extended to also include additional query constraints.

**Signature:**

    export declare function query(query: Query, ...queryConstraints: QueryConstraint[]): Query;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) | The Query instance to use as a base for the new constraints. |
| queryConstraints | [QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)\[\] | The list of `QueryConstraint`s to apply. |

**Returns:**

[Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface)

#### Exceptions

if any of the provided query constraints cannot be combined with the existing or new constraints.

## function(ref, ...)

### onDisconnect(ref)

Returns an `OnDisconnect` object - see [Enabling Offline Capabilities in JavaScript](https://firebase.google.com/docs/database/web/offline-capabilities) for more information on how to use it.

**Signature:**

    export declare function onDisconnect(ref: DatabaseReference): OnDisconnect;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ref | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The reference to add OnDisconnect triggers for. |

**Returns:**

[OnDisconnect](https://firebase.google.com/docs/reference/js/database.ondisconnect.md#ondisconnect_class)

### remove(ref)

Removes the data at this Database location.

Any data at child locations will also be deleted.

The effect of the remove will be visible immediately and the corresponding event 'value' will be triggered. Synchronization of the remove to the Firebase servers will also be started, and the returned Promise will resolve when complete. If provided, the onComplete callback will be called asynchronously after synchronization has finished.

**Signature:**

    export declare function remove(ref: DatabaseReference): Promise<void>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ref | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The location to remove. |

**Returns:**

Promise\<void\>

Resolves when remove on server is complete.

### runTransaction(ref, transactionUpdate, options)

Atomically modifies the data at this location.

Atomically modify the data at this location. Unlike a normal `set()`, which just overwrites the data regardless of its previous value, `runTransaction()` is used to modify the existing value to a new value, ensuring there are no conflicts with other clients writing to the same location at the same time.

To accomplish this, you pass `runTransaction()` an update function which is used to transform the current value into a new value. If another client writes to the location before your new value is successfully written, your update function will be called again with the new current value, and the write will be retried. This will happen repeatedly until your write succeeds without conflict or you abort the transaction by not returning a value from your update function.

> [!NOTE]
> **Note:** Modifying data with `set()` will cancel any pending transactions at that location, so extreme care should be taken if mixing `set()` and `runTransaction()` to update the same data.

> [!NOTE]
> **Note:** When using transactions with Security and Firebase Rules in place, be aware that a client needs `.read` access in addition to `.write` access in order to perform a transaction. This is because the client-side nature of transactions requires the client to read the data in order to transactionally update it.

**Signature:**

    export declare function runTransaction(ref: DatabaseReference, transactionUpdate: (currentData: any) => unknown, options?: TransactionOptions): Promise<TransactionResult>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ref | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The location to atomically modify. |
| transactionUpdate | (currentData: any) =\> unknown | A developer-supplied function which will be passed the current data stored at this location (as a JavaScript object). The function should return the new value it would like written (as a JavaScript object). If `undefined` is returned (i.e. you return with no arguments) the transaction will be aborted and the data at this location will not be modified. |
| options | [TransactionOptions](https://firebase.google.com/docs/reference/js/database.transactionoptions.md#transactionoptions_interface) | An options object to configure transactions. |

**Returns:**

Promise\<[TransactionResult](https://firebase.google.com/docs/reference/js/database.transactionresult.md#transactionresult_class)\>

A `Promise` that can optionally be used instead of the `onComplete` callback to handle success and failure.

### set(ref, value)

Writes data to this Database location.

This will overwrite any data at this location and all child locations.

The effect of the write will be visible immediately, and the corresponding events ("value", "child_added", etc.) will be triggered. Synchronization of the data to the Firebase servers will also be started, and the returned Promise will resolve when complete. If provided, the `onComplete` callback will be called asynchronously after synchronization has finished.

Passing `null` for the new value is equivalent to calling `remove()`; namely, all data at this location and all child locations will be deleted.

`set()` will remove any priority stored at this location, so if priority is meant to be preserved, you need to use `setWithPriority()` instead.

Note that modifying data with `set()` will cancel any pending transactions at that location, so extreme care should be taken if mixing `set()` and `transaction()` to modify the same data.

A single `set()` will generate a single "value" event at the location where the `set()` was performed.

**Signature:**

    export declare function set(ref: DatabaseReference, value: unknown): Promise<void>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ref | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The location to write to. |
| value | unknown | The value to be written (string, number, boolean, object, array, or null). |

**Returns:**

Promise\<void\>

Resolves when write to server is complete.

### setPriority(ref, priority)

Sets a priority for the data at this Database location.

Applications need not use priority but can order collections by ordinary properties (see [Sorting and filtering data](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data) ).

**Signature:**

    export declare function setPriority(ref: DatabaseReference, priority: string | number | null): Promise<void>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ref | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The location to write to. |
| priority | string \| number \| null | The priority to be written (string, number, or null). |

**Returns:**

Promise\<void\>

Resolves when write to server is complete.

### setWithPriority(ref, value, priority)

Writes data the Database location. Like `set()` but also specifies the priority for that data.

Applications need not use priority but can order collections by ordinary properties (see [Sorting and filtering data](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data) ).

**Signature:**

    export declare function setWithPriority(ref: DatabaseReference, value: unknown, priority: string | number | null): Promise<void>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ref | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The location to write to. |
| value | unknown | The value to be written (string, number, boolean, object, array, or null). |
| priority | string \| number \| null | The priority to be written (string, number, or null). |

**Returns:**

Promise\<void\>

Resolves when write to server is complete.

### update(ref, values)

Writes multiple values to the Database at once.

The `values` argument contains multiple property-value pairs that will be written to the Database together. Each child property can either be a simple property (for example, "name") or a relative path (for example, "name/first") from the current location to the data to update.

As opposed to the `set()` method, `update()` can be use to selectively update only the referenced properties at the current location (instead of replacing all the child properties at the current location).

The effect of the write will be visible immediately, and the corresponding events ('value', 'child_added', etc.) will be triggered. Synchronization of the data to the Firebase servers will also be started, and the returned Promise will resolve when complete. If provided, the `onComplete` callback will be called asynchronously after synchronization has finished.

A single `update()` will generate a single "value" event at the location where the `update()` was performed, regardless of how many children were modified.

Note that modifying data with `update()` will cancel any pending transactions at that location, so extreme care should be taken if mixing `update()` and `transaction()` to modify the same data.

Passing `null` to `update()` will remove the data at this location.

See [Introducing multi-location updates and more](https://firebase.googleblog.com/2015/09/introducing-multi-location-updates-and_86.html).

**Signature:**

    export declare function update(ref: DatabaseReference, values: object): Promise<void>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ref | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The location to write to. |
| values | object | Object containing multiple values. |

**Returns:**

Promise\<void\>

Resolves when update on server is complete.

## function(value, ...)

### endAt(value, key)

Creates a `QueryConstraint` with the specified ending point.

Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()` allows you to choose arbitrary starting and ending points for your queries.

The ending point is inclusive, so children with exactly the specified value will be included in the query. The optional key argument can be used to further limit the range of the query. If it is specified, then children that have exactly the specified value must also have a key name less than or equal to the specified key.

You can read more about `endAt()` in [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

**Signature:**

    export declare function endAt(value: number | string | boolean | null, key?: string): QueryConstraint;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | number \| string \| boolean \| null | The value to end at. The argument type depends on which `orderBy()`*function was used in this query. Specify a value that matches the `orderBy`* `()` type. When used in combination with `orderByKey()`, the value must be a string. |
| key | string | The child key to end at, among the children with the previously specified priority. This argument is only allowed if ordering by child, value, or priority. |

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

### endBefore(value, key)

Creates a `QueryConstraint` with the specified ending point (exclusive).

Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()` allows you to choose arbitrary starting and ending points for your queries.

The ending point is exclusive. If only a value is provided, children with a value less than the specified value will be included in the query. If a key is specified, then children must have a value less than or equal to the specified value and a key name less than the specified key.

**Signature:**

    export declare function endBefore(value: number | string | boolean | null, key?: string): QueryConstraint;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | number \| string \| boolean \| null | The value to end before. The argument type depends on which `orderBy()`*function was used in this query. Specify a value that matches the `orderBy`* `()` type. When used in combination with `orderByKey()`, the value must be a string. |
| key | string | The child key to end before, among the children with the previously specified priority. This argument is only allowed if ordering by child, value, or priority. |

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

### equalTo(value, key)

Creates a `QueryConstraint` that includes children that match the specified value.

Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()` allows you to choose arbitrary starting and ending points for your queries.

The optional key argument can be used to further limit the range of the query. If it is specified, then children that have exactly the specified value must also have exactly the specified key as their key name. This can be used to filter result sets with many matches for the same value.

You can read more about `equalTo()` in [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

**Signature:**

    export declare function equalTo(value: number | string | boolean | null, key?: string): QueryConstraint;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | number \| string \| boolean \| null | The value to match for. The argument type depends on which `orderBy()`*function was used in this query. Specify a value that matches the `orderBy`* `()` type. When used in combination with `orderByKey()`, the value must be a string. |
| key | string | The child key to start at, among the children with the previously specified priority. This argument is only allowed if ordering by child, value, or priority. |

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

### startAfter(value, key)

Creates a `QueryConstraint` with the specified starting point (exclusive).

Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()` allows you to choose arbitrary starting and ending points for your queries.

The starting point is exclusive. If only a value is provided, children with a value greater than the specified value will be included in the query. If a key is specified, then children must have a value greater than or equal to the specified value and a a key name greater than the specified key.

**Signature:**

    export declare function startAfter(value: number | string | boolean | null, key?: string): QueryConstraint;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | number \| string \| boolean \| null | The value to start after. The argument type depends on which `orderBy()`*function was used in this query. Specify a value that matches the `orderBy`* `()` type. When used in combination with `orderByKey()`, the value must be a string. |
| key | string | The child key to start after. This argument is only allowed if ordering by child, value, or priority. |

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

### startAt(value, key)

Creates a `QueryConstraint` with the specified starting point.

Using `startAt()`, `startAfter()`, `endBefore()`, `endAt()` and `equalTo()` allows you to choose arbitrary starting and ending points for your queries.

The starting point is inclusive, so children with exactly the specified value will be included in the query. The optional key argument can be used to further limit the range of the query. If it is specified, then children that have exactly the specified value must also have a key name greater than or equal to the specified key.

You can read more about `startAt()` in [Filtering data](https://firebase.google.com/docs/database/web/lists-of-data#filtering_data).

**Signature:**

    export declare function startAt(value?: number | string | boolean | null, key?: string): QueryConstraint;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | number \| string \| boolean \| null | The value to start at. The argument type depends on which `orderBy()`*function was used in this query. Specify a value that matches the `orderBy`* `()` type. When used in combination with `orderByKey()`, the value must be a string. |
| key | string | The child key to start at. This argument is only allowed if ordering by child, value, or priority. |

**Returns:**

[QueryConstraint](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstraint_class)

## EventType

One of the following strings: "value", "child_added", "child_changed", "child_removed", or "child_moved."

**Signature:**

    export declare type EventType = 'value' | 'child_added' | 'child_changed' | 'child_moved' | 'child_removed';

## QueryConstraintType

Describes the different query constraints available in this SDK.

**Signature:**

    export declare type QueryConstraintType = 'endAt' | 'endBefore' | 'startAt' | 'startAfter' | 'limitToFirst' | 'limitToLast' | 'orderByChild' | 'orderByKey' | 'orderByPriority' | 'orderByValue' | 'equalTo';

## Unsubscribe

A callback that can invoked to remove a listener.

**Signature:**

    export declare type Unsubscribe = () => void;