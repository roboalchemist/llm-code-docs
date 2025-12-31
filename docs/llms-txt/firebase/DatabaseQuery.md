# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.md.txt

# FirebaseDatabase Framework Reference

# DatabaseQuery

    class DatabaseQuery : NSObject

A `DatabaseQuery` instance represents a query over the data at a particular
location.

You create one by calling one of the query methods (`queryOrdered(byChild:)`,
`queryStarting(atValue:)`, etc.) on a [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html). The query methods
can be chained to further specify the data you are interested in observing.
[## Attach observers to read data](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/Attach-observers-to-read-data)

- `
  ``
  ``
  `

  ### [observe(_:with:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:withBlock:)

  `
  `  
  This method is used to listen for data changes at a particular location.
  This is the primary way to read data from the Firebase Database. Your
  block will be triggered for the initial data and again whenever the
  data changes.

  Use removeObserverWithHandle: to stop receiving updates.  

  #### Declaration

  Swift  

      func observe(_ eventType: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType.html, with block: @escaping (https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html) -> Void) -> UInt

  #### Parameters

  |-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*eventType*` ` | The type of event to listen for.                                                                                                                                                                                     |
  | ` `*block*` `     | The block that should be called with initial data and updates. It is passed the data as a [DataSnapshot](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html). |

  #### Return Value

  A handle used to unregister this block later using
  [removeObserver(withHandle:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)removeObserverWithHandle:)
- `
  ``
  ``
  `

  ### [observe(_:andPreviousSiblingKeyWith:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:andPreviousSiblingKeyWithBlock:)

  `
  `  
  This method is used to listen for data changes at a particular location.
  This is the primary way to read data from the Firebase Database. Your
  block will be triggered for the initial data and again whenever the data
  changes. In addition, for `DataEventTypeChildAdded`,
  `DataEventTypeChildMoved`, and `DataEventTypeChildChanged` events, your
  block will be passed the key of the previous node by priority order.

  Use [removeObserver(withHandle:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)removeObserverWithHandle:) to stop receiving updates.  

  #### Declaration

  Swift  

      func observe(_ eventType: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType.html, andPreviousSiblingKeyWith block: @escaping (https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html, String?) -> Void) -> UInt

  #### Parameters

  |-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*eventType*` ` | The type of event to listen for.                                                                                                                                                                                                                  |
  | ` `*block*` `     | The block that should be called with initial data and updates. It is passed the data as a [DataSnapshot](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html) and the previous child's key. |

  #### Return Value

  A handle used to unregister this block later using
  [removeObserver(withHandle:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)removeObserverWithHandle:)
- `
  ``
  ``
  `

  ### [observe(_:with:withCancel:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:withBlock:withCancelBlock:)

  `
  `  
  This method is used to listen for data changes at a particular location.
  This is the primary way to read data from the Firebase Database. Your
  block will be triggered for the initial data and again whenever the data
  changes.

  The `cancelBlock` will be called if you will no longer receive new events
  due to no longer having permission.

  Use [removeObserver(withHandle:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)removeObserverWithHandle:) to stop receiving updates.  

  #### Declaration

  Swift  

      func observe(_ eventType: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType.html, with block: @escaping (https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html) -> Void, withCancel cancelBlock: ((any Error) -> Void)? = nil) -> UInt

  #### Parameters

  |---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*eventType*` `   | The type of event to listen for.                                                                                                                                                                                     |
  | ` `*block*` `       | The block that should be called with initial data and updates. It is passed the data as a [DataSnapshot](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html). |
  | ` `*cancelBlock*` ` | The block that should be called if this client no longer has permission to receive these events                                                                                                                      |

  #### Return Value

  A handle used to unregister this block later using
  [removeObserver(withHandle:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)removeObserverWithHandle:)
- `
  ``
  ``
  `

  ### [observe(_:andPreviousSiblingKeyWith:withCancel:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:andPreviousSiblingKeyWithBlock:withCancelBlock:)

  `
  `  
  This method is used to listen for data changes at a particular location.
  This is the primary way to read data from the Firebase Database. Your block
  will be triggered for the initial data and again whenever the data changes.
  In addition, for `FIRDataEventTypeChildAdded`, `FIRDataEventTypeChildMoved`,
  and FIRDataEventTypeChildChanged events, your block will be passed the key
  of the previous node by priority order.

  The `cancelBlock` will be called if you will no longer receive new events due
  to no longer having permission.

  Use [removeObserver(withHandle:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)removeObserverWithHandle:) to stop receiving updates.  

  #### Declaration

  Swift  

      func observe(_ eventType: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType.html, andPreviousSiblingKeyWith block: @escaping (https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html, String?) -> Void, withCancel cancelBlock: ((any Error) -> Void)? = nil) -> UInt

  #### Parameters

  |---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*eventType*` `   | The type of event to listen for.                                                                                                                                                                                                                  |
  | ` `*block*` `       | The block that should be called with initial data and updates. It is passed the data as a [DataSnapshot](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html) and the previous child's key. |
  | ` `*cancelBlock*` ` | The block that should be called if this client no longer has permission to receive these events                                                                                                                                                   |

  #### Return Value

  A handle used to unregister this block later using
  [removeObserver(withHandle:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)removeObserverWithHandle:)
- `
  ``
  ``
  `

  ### [getData()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)getDataWithCompletionBlock:)

  `
  `  
  This method is used to get the most up-to-date value for this query. This
  method updates the cache and raises events if successful. If
  not connected, it returns a locally-cached value.  

  #### Declaration

  Swift  

      func getData() async throws -> https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html

  #### Parameters

  |---------------|--------------------------------------------------------------------------------------------------------------------------------|
  | ` `*block*` ` | The block that should be called with the most up-to-date value of this query, or an error if no such value could be retrieved. |

- `
  ``
  ``
  `

  ### [observeSingleEvent(of:with:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)observeSingleEventOfType:withBlock:)

  `
  `  
  This is equivalent to [observe(_:with:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:withBlock:), except the block is
  immediately canceled after the initial data is returned.  

  #### Declaration

  Swift  

      func observeSingleEvent(of eventType: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType.html, with block: @escaping (https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html) -> Void)

  #### Parameters

  |-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*eventType*` ` | The type of event to listen for.                                                                                                                                                       |
  | ` `*block*` `     | The block that should be called. It is passed the data as a [DataSnapshot](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html). |

- `
  ``
  ``
  `

  ### [observeSingleEventAndPreviousSiblingKey(of:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)observeSingleEventOfType:andPreviousSiblingKeyWithBlock:)

  `
  `  
  This is equivalent to [observe(_:with:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:withBlock:), except the block is
  immediately canceled after the initial data is returned. In addition, for
  `DataEventTypeChildAdded`, `DataEventTypeChildMoved`, and
  `DataEventTypeChildChanged` events, your block will be passed the key of the
  previous node by priority order.  

  #### Declaration

  Swift  

      func observeSingleEventAndPreviousSiblingKey(of eventType: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType.html) async -> (https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html, String?)

  #### Parameters

  |-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*eventType*` ` | The type of event to listen for.                                                                                                                                                                                    |
  | ` `*block*` `     | The block that should be called. It is passed the data as a [DataSnapshot](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html) and the previous child's key. |

- `
  ``
  ``
  `

  ### [observeSingleEvent(of:with:withCancel:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)observeSingleEventOfType:withBlock:withCancelBlock:)

  `
  `  
  This is equivalent to [observe(_:with:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:withBlock:), except the block is
  immediately canceled after the initial data is returned.

  The `cancelBlock` will be called if you do not have permission to read data
  at this location.  

  #### Declaration

  Swift  

      func observeSingleEvent(of eventType: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType.html, with block: @escaping (https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html) -> Void, withCancel cancelBlock: ((any Error) -> Void)? = nil)

  #### Parameters

  |---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*eventType*` `   | The type of event to listen for.                                                                                                                                                       |
  | ` `*block*` `       | The block that should be called. It is passed the data as a [DataSnapshot](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html). |
  | ` `*cancelBlock*` ` | The block that will be called if you don't have permission to access this data                                                                                                         |

- `
  ``
  ``
  `

  ### [observeSingleEvent(of:andPreviousSiblingKeyWith:withCancel:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)observeSingleEventOfType:andPreviousSiblingKeyWithBlock:withCancelBlock:)

  `
  `  
  This is equivalent to [observe(_:with:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:withBlock:), except the block is
  immediately canceled after the initial data is returned. In addition, for
  `DataEventTypeChildAdded`, `DataEventTypeChildMoved`, and
  `DataEventTypeChildChanged` events, your block will be passed the key of the
  previous node by priority order.

  The `cancelBlock` will be called if you do not have permission to read data
  at this location.  

  #### Declaration

  Swift  

      func observeSingleEvent(of eventType: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType.html, andPreviousSiblingKeyWith block: @escaping (https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html, String?) -> Void, withCancel cancelBlock: ((any Error) -> Void)? = nil)

  #### Parameters

  |---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*eventType*` `   | The type of event to listen for.                                                                                                                                                                                    |
  | ` `*block*` `       | The block that should be called. It is passed the data as a [DataSnapshot](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.html) and the previous child's key. |
  | ` `*cancelBlock*` ` | The block that will be called if you don't have permission to access this data                                                                                                                                      |

[## Detaching observers](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/Detaching-observers)

- `
  ``
  ``
  `

  ### [removeObserver(withHandle:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)removeObserverWithHandle:)

  `
  `  
  Detach a block previously attached with [observe(_:with:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:withBlock:), or another query
  observation method. After this method is called, the associated block
  registered to receive snapshot updates will no longer be invoked.  

  #### Declaration

  Swift  

      func removeObserver(withHandle handle: UInt)

  #### Parameters

  |----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*handle*` ` | The handle returned by the call to [observe(_:with:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:withBlock:) which we are trying to remove. |

- `
  ``
  ``
  `

  ### [removeAllObservers()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)removeAllObservers)

  `
  `  
  Detach all blocks previously attached to this Firebase Database location with
  [observe(_:with:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)observeEventType:withBlock:) and other query observation methods.  

  #### Declaration

  Swift  

      func removeAllObservers()

- `
  ``
  ``
  `

  ### [keepSynced(_:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)keepSynced:)

  `
  `  
  By calling `keepSynced(true)` on a location, the data for that location will
  automatically be downloaded and kept in sync, even when no listeners are
  attached for that location. Additionally, while a location is kept synced, it
  will not be evicted from the persistent disk cache.  

  #### Declaration

  Swift  

      func keepSynced(_ keepSynced: Bool)

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------|
  | ` `*keepSynced*` ` | Pass true to keep this location synchronized, or false to stop synchronization. |

[## Querying and limiting](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/Querying-and-limiting)

- `
  ``
  ``
  `

  ### [queryLimited(toFirst:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryLimitedToFirst:)

  `
  `  
  This method is used to generate a reference to a limited view of the
  data at this location. The `DatabaseQuery` instance returned by
  `queryLimited(toFirst:)` will respond to at most the first limit child nodes.  

  #### Declaration

  Swift  

      func queryLimited(toFirst limit: UInt) -> DatabaseQuery

  #### Parameters

  |---------------|---------------------------------------------------------------------------------|
  | ` `*limit*` ` | The upper bound, inclusive, for the number of child nodes to receive events for |

  #### Return Value

  A `DatabaseQuery` instance, limited to at most limit child nodes.
- `
  ``
  ``
  `

  ### [queryLimited(toLast:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryLimitedToLast:)

  `
  `  
  `queryLimited(toLast:)` is used to generate a reference to a limited view of
  the data at this location. The `DatabaseQuery` instance returned by
  this method will respond to at most the last limit child nodes.  

  #### Declaration

  Swift  

      func queryLimited(toLast limit: UInt) -> DatabaseQuery

  #### Parameters

  |---------------|---------------------------------------------------------------------------------|
  | ` `*limit*` ` | The upper bound, inclusive, for the number of child nodes to receive events for |

  #### Return Value

  A `DatabaseQuery` instance, limited to at most limit child nodes.
- `
  ``
  ``
  `

  ### [queryOrdered(byChild:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryOrderedByChild:)

  `
  `  
  This method is used to generate a reference to a view of the data that's
  been sorted by the values of a particular child key. This method is intended
  to be used in combination with [queryStarting(atValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)queryStartingAtValue:),
  [queryEnding(atValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)queryEndingAtValue:), or [queryEqual(toValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)queryEqualToValue:).  

  #### Declaration

  Swift  

      func queryOrdered(byChild key: String) -> DatabaseQuery

  #### Parameters

  |-------------|-------------------------------------------------------------------------------|
  | ` `*key*` ` | The child key to use in ordering data visible to the returned `DatabaseQuery` |

  #### Return Value

  A `DatabaseQuery` instance, ordered by the values of the specified
  child key.
- `
  ``
  ``
  `

  ### [queryOrderedByKey()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryOrderedByKey)

  `
  `  
  `queryOrdered(byKey:) is used to generate a reference to a view of the data
  that's been sorted by child key. This method is intended to be used in
  combination with`queryStarting(atValue:)`,`queryEnding(atValue:)`, or
  `queryEqual(toValue:)\`.  

  #### Declaration

  Swift  

      func queryOrderedByKey() -> DatabaseQuery

  #### Return Value

  A `DatabaseQuery` instance, ordered by child keys.
- `
  ``
  ``
  `

  ### [queryOrderedByValue()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryOrderedByValue)

  `
  `  
  `queryOrdered(byValue:)` is used to generate a reference to a view of the
  data that's been sorted by child value. This method is intended to be used in
  combination with [queryStarting(atValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)queryStartingAtValue:), [queryEnding(atValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)queryEndingAtValue:), or
  [queryEqual(toValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery.html#/c:objc(cs)FIRDatabaseQuery(im)queryEqualToValue:).  

  #### Declaration

  Swift  

      func queryOrderedByValue() -> DatabaseQuery

  #### Return Value

  A `DatabaseQuery` instance, ordered by child value.
- `
  ``
  ``
  `

  ### [queryOrderedByPriority()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryOrderedByPriority)

  `
  `  
  `queryOrdered(byPriority:) is used to generate a reference to a view of the
  data that's been sorted by child priority. This method is intended to be used
  in combination with`queryStarting(atValue:)`,`queryEnding(atValue:)`, or
  `queryEqual(toValue:)\`.  

  #### Declaration

  Swift  

      func queryOrderedByPriority() -> DatabaseQuery

  #### Return Value

  A `DatabaseQuery` instance, ordered by child priorities.
- `
  ``
  ``
  `

  ### [queryStarting(atValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryStartingAtValue:)

  `
  `  
  `queryStarting(atValue:)` is used to generate a reference to a limited view
  of the data at this location. The `DatabaseQuery` instance returned by
  `queryStarting(atValue:)` will respond to events at nodes with a value
  greater than or equal to `startValue`.  

  #### Declaration

  Swift  

      func queryStarting(atValue startValue: Any?) -> DatabaseQuery

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------|
  | ` `*startValue*` ` | The lower bound, inclusive, for the value of data visible to the returned `DatabaseQuery` |

  #### Return Value

  A `DatabaseQuery` instance, limited to data with value greater than
  or equal to `startValue`
- `
  ``
  ``
  `

  ### [queryStarting(atValue:childKey:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryStartingAtValue:childKey:)

  `
  `  
  `queryStarting(atValue:childKey:)` is used to generate a reference to a
  limited view of the data at this location. The `DatabaseQuery` instance
  returned by `queryStarting(atValue:childKey:)` will respond to events at
  nodes with a value greater than `startValue`, or equal to `startValue` and
  with a key greater than or equal to `childKey`. This is most useful when
  implementing pagination in a case where multiple nodes can match the
  `startValue`.  

  #### Declaration

  Swift  

      func queryStarting(atValue startValue: Any?, childKey: String?) -> DatabaseQuery

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------|
  | ` `*startValue*` ` | The lower bound, inclusive, for the value of data visible to the returned `DatabaseQuery` |
  | ` `*childKey*` `   | The lower bound, inclusive, for the key of nodes with value equal to `startValue`         |

  #### Return Value

  A `DatabaseQuery` instance, limited to data with value greater than
  or equal to `startValue`
- `
  ``
  ``
  `

  ### [queryStarting(afterValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryStartingAfterValue:)

  `
  `  
  `queryStarting(afterValue:)` is used to generate a reference to a
  limited view of the data at this location. The `DatabaseQuery` instance
  returned by `queryStarting(afterValue:)` will respond to events at nodes
  with a value greater than startAfterValue.  

  #### Declaration

  Swift  

      func queryStarting(afterValue startAfterValue: Any?) -> DatabaseQuery

  #### Parameters

  |-------------------------|-------------------------------------------------------------------------------------------|
  | ` `*startAfterValue*` ` | The lower bound, exclusive, for the value of data visible to the returned `DatabaseQuery` |

  #### Return Value

  A `DatabaseQuery` instance, limited to data with value greater
  `startAfterValue`
- `
  ``
  ``
  `

  ### [queryStarting(afterValue:childKey:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryStartingAfterValue:childKey:)

  `
  `  
  `queryStarting(afterValue:childKey:)` is used to generate a reference to a
  limited view of the data at this location. The `DatabaseQuery` instance
  returned by `queryStarting(afterValue:childKey:)` will respond to events at
  nodes with a value greater than `startAfterValue`, or equal to
  `startAfterValue` and with a key greater than `childKey`. This is most useful
  when implementing pagination in a case where multiple nodes can match the
  `startAfterValue`.  

  #### Declaration

  Swift  

      func queryStarting(afterValue startAfterValue: Any?, childKey: String?) -> DatabaseQuery

  #### Parameters

  |-------------------------|-------------------------------------------------------------------------------------------|
  | ` `*startAfterValue*` ` | The lower bound, inclusive, for the value of data visible to the returned `DatabaseQuery` |
  | ` `*childKey*` `        | The lower bound, exclusive, for the key of nodes with value equal to `startAfterValue`    |

  #### Return Value

  A `DatabaseQuery` instance, limited to data with value greater than
  `startAfterValue`, or equal to `startAfterValue` with a key greater than
  `childKey`
- `
  ``
  ``
  `

  ### [queryEnding(atValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryEndingAtValue:)

  `
  `  
  `queryEnding(atValue:)` is used to generate a reference to a limited view of
  the data at this location. The DatabaseQuery instance returned by
  `queryEnding(atValue:)` will respond to events at nodes with a value less
  than or equal to `endValue`.  

  #### Declaration

  Swift  

      func queryEnding(atValue endValue: Any?) -> DatabaseQuery

  #### Parameters

  |------------------|-------------------------------------------------------------------------------------------|
  | ` `*endValue*` ` | The upper bound, inclusive, for the value of data visible to the returned `DatabaseQuery` |

  #### Return Value

  A `DatabaseQuery` instance, limited to data with value less than or
  equal to `endValue`
- `
  ``
  ``
  `

  ### [queryEnding(atValue:childKey:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryEndingAtValue:childKey:)

  `
  `  
  `queryEnding(atValue:childKey:)` is used to generate a reference to a limited
  view of the data at this location. The `DatabaseQuery` instance returned by
  `queryEnding(atValue:childKey:)` will respond to events at nodes with a value
  less than `endValue`, or equal to `endValue` and with a key less than or
  equal to `childKey`. This is most useful when implementing pagination in a
  case where multiple nodes can match the `endValue`.  

  #### Declaration

  Swift  

      func queryEnding(atValue endValue: Any?, childKey: String?) -> DatabaseQuery

  #### Parameters

  |------------------|-------------------------------------------------------------------------------------------|
  | ` `*endValue*` ` | The upper bound, inclusive, for the value of data visible to the returned `DatabaseQuery` |
  | ` `*childKey*` ` | The upper bound, inclusive, for the key of nodes with value equal to `endValue`           |

  #### Return Value

  A `DatabaseQuery` instance, limited to data with value less than or
  equal to `endValue`
- `
  ``
  ``
  `

  ### [queryEnding(beforeValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryEndingBeforeValue:)

  `
  `  
  `queryEnding(beforeValue:) is used to generate a reference to a limited view
  of the data at this location. The`DatabaseQuery`instance returned by
  `queryEnding(beforeValue:)`will respond to events at nodes with a value less
  than`endValue\`.  

  #### Declaration

  Swift  

      func queryEnding(beforeValue endValue: Any?) -> DatabaseQuery

  #### Parameters

  |------------------|-------------------------------------------------------------------------------------------|
  | ` `*endValue*` ` | The upper bound, exclusive, for the value of data visible to the returned `DatabaseQuery` |

  #### Return Value

  A `DatabaseQuery` instance, limited to data with value less than
  `endValue`
- `
  ``
  ``
  `

  ### [queryEnding(beforeValue:childKey:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryEndingBeforeValue:childKey:)

  `
  `  
  `queryEnding(beforeValue:childKey:)` is used to generate a reference to a
  limited view of the data at this location. The `DatabaseQuery` instance
  returned by `queryEnding(beforeValue:childKey:)` will respond to events at
  nodes with a value less than `endValue`, or equal to `endValue` and with a
  key less than childKey.  

  #### Declaration

  Swift  

      func queryEnding(beforeValue endValue: Any?, childKey: String?) -> DatabaseQuery

  #### Parameters

  |------------------|-------------------------------------------------------------------------------------------|
  | ` `*endValue*` ` | The upper bound, inclusive, for the value of data visible to the returned `DatabaseQuery` |
  | ` `*childKey*` ` | The upper bound, exclusive, for the key of nodes with value equal to endValue             |

  #### Return Value

  A `DatabaseQuery` instance, limited to data with value less than or
  equal to endValue
- `
  ``
  ``
  `

  ### [queryEqual(toValue:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryEqualToValue:)

  `
  `  
  `queryEqual(toValue:)` is used to generate a reference to a limited view of
  the data at this location. The `DatabaseQuery` instance returned by
  `queryEqual(toValue:)` will respond to events at nodes with a value equal to
  the supplied argument.  

  #### Declaration

  Swift  

      func queryEqual(toValue value: Any?) -> DatabaseQuery

  #### Parameters

  |---------------|--------------------------------------------------------------------|
  | ` `*value*` ` | The value that the data returned by this `DatabaseQuery` will have |

  #### Return Value

  A `DatabaseQuery` instance, limited to data with the supplied value.
- `
  ``
  ``
  `

  ### [queryEqual(toValue:childKey:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(im)queryEqualToValue:childKey:)

  `
  `  
  `queryEqual(toValue:childKey:)` is used to generate a reference to a limited
  view of the data at this location. The `DatabaseQuery` instance returned by
  `queryEqual(toValue:childKey:)` will respond to events at nodes with a value
  equal to the supplied argument and with their key equal to `childKey`. There
  will be at most one node that matches because child keys are unique.  

  #### Declaration

  Swift  

      func queryEqual(toValue value: Any?, childKey: String?) -> DatabaseQuery

  #### Parameters

  |------------------|--------------------------------------------------------------------|
  | ` `*value*` `    | The value that the data returned by this `DatabaseQuery` will have |
  | ` `*childKey*` ` | The name of nodes with the right value                             |

  #### Return Value

  A `DatabaseQuery` instance, limited to data with the supplied value
and the key.  
[## Properties](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/Properties)

- `
  ``
  ``
  `

  ### [ref](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery#/c:objc(cs)FIRDatabaseQuery(py)ref)

  `
  `  
  Gets a [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html) for the location of this query.  

  #### Declaration

  Swift  

      var ref: FIRDatabaseReference { get }

  #### Return Value

  A [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html) for the location of this query.