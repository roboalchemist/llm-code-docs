# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery.md.txt

# FirebaseFirestore Framework Reference

# FIRQuery


    @interface FIRQuery : NSObject

A `Query` refers to a query which you can read or listen to. You can also construct
refined `Query` objects by adding filters and ordering.
- `
  ``
  ``
  `

  ### [firestore](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(py)firestore)

  `
  `  
  The `Firestore` instance that created this query (useful for performing transactions, etc.).  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore.html *_Nonnull firestore;

[## Retrieving Data](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/Retrieving-Data)

- `
  ``
  ``
  `

  ### [-getDocumentsWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)getDocumentsWithCompletion:)

  `
  `  
  Reads the documents matching this query.

  This method attempts to provide up-to-date data when possible by waiting for
  data from the server, but it may return cached data or fail if you are
  offline and the server cannot be reached. See the
  `getDocuments(source:completion:)` method to change this behavior.  

  #### Declaration

  Objective-C  

      - (void)getDocumentsWithCompletion:
          (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot.html *_Nullable,
                            NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | a block to execute once the documents have been successfully read. documentSet will be `nil` only if error is `non-nil`. |

- `
  ``
  ``
  `

  ### [-getDocumentsWithSource:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)getDocumentsWithSource:completion:)

  `
  `  
  Reads the documents matching this query.  

  #### Declaration

  Objective-C  

      - (void)getDocumentsWithSource:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreSource.html)source
                          completion:(nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot.html *_Nullable,
                                                       NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*source*` `     | indicates whether the results should be fetched from the cache only (`Source.cache`), the server only (`Source.server`), or to attempt the server and fall back to the cache (`Source.default`). |
  | ` `*completion*` ` | a block to execute once the documents have been successfully read. documentSet will be `nil` only if error is `non-nil`.                                                                         |

- `
  ``
  ``
  `

  ### [-addSnapshotListener:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)addSnapshotListener:)

  `
  `  
  Attaches a listener for `QuerySnapshot` events.  

  #### Declaration

  Objective-C  

      - (nonnull id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration.html>)addSnapshotListener:
          (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot.html *_Nullable, NSError *_Nullable))listener;

  #### Parameters

  |------------------|-------------------------|
  | ` `*listener*` ` | The listener to attach. |

  #### Return Value

  A `ListenerRegistration` object that can be used to remove this listener.
- `
  ``
  ``
  `

  ### [-addSnapshotListenerWithIncludeMetadataChanges:listener:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)addSnapshotListenerWithIncludeMetadataChanges:listener:)

  `
  `  
  Attaches a listener for `QuerySnapshot` events.  

  #### Declaration

  Objective-C  

      - (nonnull id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration.html>)
          addSnapshotListenerWithIncludeMetadataChanges:(BOOL)includeMetadataChanges
                                               listener:
                                                   (nonnull void (^)(
                                                       https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot.html *_Nullable,
                                                       NSError *_Nullable))listener;

  #### Parameters

  |--------------------------------|---------------------------------------------------------------------------------------------------------------|
  | ` `*includeMetadataChanges*` ` | Whether metadata-only changes (i.e. only `DocumentSnapshot.metadata` changed) should trigger snapshot events. |
  | ` `*listener*` `               | The listener to attach.                                                                                       |

  #### Return Value

  A `ListenerRegistration` that can be used to remove this listener.
- `
  ``
  ``
  `

  ### [-addSnapshotListenerWithOptions:listener:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)addSnapshotListenerWithOptions:listener:)

  `
  `  
  Attaches a listener for `QuerySnapshot` events.  

  #### Declaration

  Objective-C  

      - (nonnull id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration.html>)
          addSnapshotListenerWithOptions:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotListenOptions.html *)options
                                listener:
                                    (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuerySnapshot.html *_Nullable,
                                                      NSError *_Nullable))listener;

  #### Parameters

  |------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*options*` `  | Sets snapshot listener options, including whether metadata-only changes should trigger snapshot events, the source to listen to, the executor to use to call the listener, or the activity to scope the listener to. |
  | ` `*listener*` ` | The listener to attach.                                                                                                                                                                                              |

  #### Return Value

A `ListenerRegistration` that can be used to remove this listener.  
[## Filtering Data](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/Filtering-Data)

- `
  ``
  ``
  `

  ### [-queryWhereFilter:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFilter:)

  `
  `  
  Creates and returns a new Query with the additional filter.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFilter:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter.html *)filter;

  #### Parameters

  |----------------|------------------------------------------------|
  | ` `*filter*` ` | The new filter to apply to the existing query. |

  #### Return Value

  The newly created Query.
- `
  ``
  ``
  `

  ### [-queryWhereField:isEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereField:isEqualTo:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value must be equal to the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereField:(nonnull NSString *)field
                                  isEqualTo:(nonnull id)value;

  #### Parameters

  |---------------|---------------------------------------|
  | ` `*field*` ` | The name of the field to compare.     |
  | ` `*value*` ` | The value the field must be equal to. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereFieldPath:isNotEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFieldPath:isNotEqualTo:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value does not equal the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                   isNotEqualTo:(nonnull id)value;

  #### Parameters

  |---------------|---------------------------------------|
  | ` `*path*` `  | The path of the field to compare.     |
  | ` `*value*` ` | The value the field must be equal to. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereField:isNotEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereField:isNotEqualTo:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value does not equal the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereField:(nonnull NSString *)field
                               isNotEqualTo:(nonnull id)value;

  #### Parameters

  |---------------|---------------------------------------|
  | ` `*field*` ` | The name of the field to compare.     |
  | ` `*value*` ` | The value the field must be equal to. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereFieldPath:isEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFieldPath:isEqualTo:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value must be equal to the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                      isEqualTo:(nonnull id)value;

  #### Parameters

  |---------------|---------------------------------------|
  | ` `*path*` `  | The path of the field to compare.     |
  | ` `*value*` ` | The value the field must be equal to. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereField:isLessThan:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereField:isLessThan:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value must be less than the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereField:(nonnull NSString *)field
                                 isLessThan:(nonnull id)value;

  #### Parameters

  |---------------|----------------------------------------|
  | ` `*field*` ` | The name of the field to compare.      |
  | ` `*value*` ` | The value the field must be less than. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereFieldPath:isLessThan:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFieldPath:isLessThan:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value must be less than the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                     isLessThan:(nonnull id)value;

  #### Parameters

  |---------------|----------------------------------------|
  | ` `*path*` `  | The path of the field to compare.      |
  | ` `*value*` ` | The value the field must be less than. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereField:isLessThanOrEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereField:isLessThanOrEqualTo:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value must be less than or equal to the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereField:(nonnull NSString *)field
                        isLessThanOrEqualTo:(nonnull id)value;

  #### Parameters

  |---------------|----------------------------------------------------|
  | ` `*field*` ` | The name of the field to compare                   |
  | ` `*value*` ` | The value the field must be less than or equal to. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereFieldPath:isLessThanOrEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFieldPath:isLessThanOrEqualTo:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value must be less than or equal to the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                            isLessThanOrEqualTo:(nonnull id)value;

  #### Parameters

  |---------------|----------------------------------------------------|
  | ` `*path*` `  | The path of the field to compare                   |
  | ` `*value*` ` | The value the field must be less than or equal to. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereField:isGreaterThan:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereField:isGreaterThan:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value must greater than the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereField:(nonnull NSString *)field
                              isGreaterThan:(nonnull id)value;

  #### Parameters

  |---------------|-------------------------------------------|
  | ` `*field*` ` | The name of the field to compare          |
  | ` `*value*` ` | The value the field must be greater than. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereFieldPath:isGreaterThan:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFieldPath:isGreaterThan:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value must greater than the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                  isGreaterThan:(nonnull id)value;

  #### Parameters

  |---------------|-------------------------------------------|
  | ` `*path*` `  | The path of the field to compare          |
  | ` `*value*` ` | The value the field must be greater than. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereField:isGreaterThanOrEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereField:isGreaterThanOrEqualTo:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value must be greater than or equal to the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereField:(nonnull NSString *)field
                     isGreaterThanOrEqualTo:(nonnull id)value;

  #### Parameters

  |---------------|-------------------------------------------|
  | ` `*field*` ` | The name of the field to compare          |
  | ` `*value*` ` | The value the field must be greater than. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereFieldPath:isGreaterThanOrEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFieldPath:isGreaterThanOrEqualTo:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  contain the specified field and the value must be greater than or equal to the specified value.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                         isGreaterThanOrEqualTo:(nonnull id)value;

  #### Parameters

  |---------------|-------------------------------------------|
  | ` `*path*` `  | The path of the field to compare          |
  | ` `*value*` ` | The value the field must be greater than. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereField:arrayContains:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereField:arrayContains:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must contain
  the specified field, it must be an array, and the array must contain the provided value.

  A query can have only one `arrayContains` filter.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereField:(nonnull NSString *)field
                              arrayContains:(nonnull id)value;

  #### Parameters

  |---------------|-----------------------------------------------------|
  | ` `*field*` ` | The name of the field containing an array to search |
  | ` `*value*` ` | The value that must be contained in the array       |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereFieldPath:arrayContains:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFieldPath:arrayContains:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must contain
  the specified field, it must be an array, and the array must contain the provided value.

  A query can have only one `arrayContains` filter.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                  arrayContains:(nonnull id)value;

  #### Parameters

  |---------------|-----------------------------------------------------|
  | ` `*path*` `  | The path of the field containing an array to search |
  | ` `*value*` ` | The value that must be contained in the array       |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereField:arrayContainsAny:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereField:arrayContainsAny:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must contain
  the specified field, the value must be an array, and that array must contain at least one value
  from the provided array.

  A query can have only one `arrayContainsAny` filter and it cannot be combined with
  `arrayContains` or `in` filters.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereField:(nonnull NSString *)field
                           arrayContainsAny:(nonnull NSArray<id> *)values;

  #### Parameters

  |----------------|------------------------------------------------------|
  | ` `*field*` `  | The name of the field containing an array to search. |
  | ` `*values*` ` | The array that contains the values to match.         |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereFieldPath:arrayContainsAny:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFieldPath:arrayContainsAny:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must contain
  the specified field, the value must be an array, and that array must contain at least one value
  from the provided array.

  A query can have only one `arrayContainsAny` filter and it cannot be combined with
  `arrayContains` or `in` filters.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                               arrayContainsAny:(nonnull NSArray<id> *)values;

  #### Parameters

  |----------------|------------------------------------------------------|
  | ` `*path*` `   | The path of the field containing an array to search. |
  | ` `*values*` ` | The array that contains the values to match.         |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereField:in:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereField:in:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must contain
  the specified field and the value must equal one of the values from the provided array.

  A query can have only one `in` filter, and it cannot be combined with an `arrayContainsAny`
  filter.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereField:(nonnull NSString *)field
                                         in:(nonnull NSArray<id> *)values;

  #### Parameters

  |----------------|----------------------------------------------|
  | ` `*field*` `  | The name of the field to search.             |
  | ` `*values*` ` | The array that contains the values to match. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereFieldPath:in:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFieldPath:in:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must contain
  the specified field and the value must equal one of the values from the provided array.

  A query can have only one `in` filter, and it cannot be combined with an `arrayContainsAny`
  filter.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                             in:(nonnull NSArray<id> *)values;

  #### Parameters

  |----------------|----------------------------------------------|
  | ` `*path*` `   | The path of the field to search.             |
  | ` `*values*` ` | The array that contains the values to match. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereField:notIn:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereField:notIn:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must contain
  the specified field and the value does not equal any of the values from the provided array.

  One special case is that `notIn` filters cannot match `nil` values. To query for documents
  where a field exists and is `nil`, use a `notEqual` filter, which can handle this special case.

  A query can have only one `notIn` filter, and it cannot be combined with an `arrayContains`,
  `arrayContainsAny`, `in`, or `notEqual` filter.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereField:(nonnull NSString *)field
                                      notIn:(nonnull NSArray<id> *)values;

  #### Parameters

  |----------------|----------------------------------------------|
  | ` `*field*` `  | The name of the field to search.             |
  | ` `*values*` ` | The array that contains the values to match. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryWhereFieldPath:notIn:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryWhereFieldPath:notIn:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must contain
  the specified field and the value does not equal any of the values from the provided array.

  One special case is that `notIn` filters cannot match `nil` values. To query for documents
  where a field exists and is `nil`, use a `notEqual` filter, which can handle this special case.

  Passing in a `null` value into the `values` array results in no document matches. To query
  for documents where a field is not `null`, use a `notEqual` filter.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                          notIn:(nonnull NSArray<id> *)values;

  #### Parameters

  |----------------|----------------------------------------------|
  | ` `*path*` `   | The path of the field to search.             |
  | ` `*values*` ` | The array that contains the values to match. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryFilteredUsingPredicate:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryFilteredUsingPredicate:)

  `
  `  
  Creates and returns a new `Query` with the additional filter that documents must
  satisfy the specified predicate.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryFilteredUsingPredicate:
          (nonnull NSPredicate *)predicate;

  #### Parameters

  |-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*predicate*` ` | The predicate the document must satisfy. Can be either comparison or compound of comparison. In particular, block-based predicate is not supported. |

  #### Return Value

The created `Query`.  
[## Sorting Data](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/Sorting-Data)

- `
  ``
  ``
  `

  ### [-queryOrderedByField:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryOrderedByField:)

  `
  `  
  Creates and returns a new `Query` that's additionally sorted by the specified field.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryOrderedByField:(nonnull NSString *)field;

  #### Parameters

  |---------------|-----------------------|
  | ` `*field*` ` | The field to sort by. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryOrderedByFieldPath:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryOrderedByFieldPath:)

  `
  `  
  Creates and returns a new `Query` that's additionally sorted by the specified field.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryOrderedByFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path;

  #### Parameters

  |--------------|-----------------------|
  | ` `*path*` ` | The field to sort by. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryOrderedByField:descending:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryOrderedByField:descending:)

  `
  `  
  Creates and returns a new `Query` that's additionally sorted by the specified field,
  optionally in descending order instead of ascending.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryOrderedByField:(nonnull NSString *)field
                                     descending:(BOOL)descending;

  #### Parameters

  |--------------------|-----------------------------|
  | ` `*field*` `      | The field to sort by.       |
  | ` `*descending*` ` | Whether to sort descending. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryOrderedByFieldPath:descending:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryOrderedByFieldPath:descending:)

  `
  `  
  Creates and returns a new `Query` that's additionally sorted by the specified field,
  optionally in descending order instead of ascending.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryOrderedByFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                         descending:(BOOL)descending;

  #### Parameters

  |--------------------|-----------------------------|
  | ` `*path*` `       | The field to sort by.       |
  | ` `*descending*` ` | Whether to sort descending. |

  #### Return Value

The created `Query`.  
[## Limiting Data](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/Limiting-Data)

- `
  ``
  ``
  `

  ### [-queryLimitedTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryLimitedTo:)

  `
  `  
  Creates and returns a new `Query` that only returns the first matching documents up to
  the specified number.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryLimitedTo:(NSInteger)limit;

  #### Parameters

  |---------------|----------------------------------------|
  | ` `*limit*` ` | The maximum number of items to return. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryLimitedToLast:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryLimitedToLast:)

  `
  `  
  Creates and returns a new `Query` that only returns the last matching documents up to
  the specified number.

  A query with a `limit(toLast:)` clause must have at least one `orderBy` clause.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryLimitedToLast:(NSInteger)limit;

  #### Parameters

  |---------------|----------------------------------------|
  | ` `*limit*` ` | The maximum number of items to return. |

  #### Return Value

The created `Query`.  
[## Choosing Endpoints](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/Choosing-Endpoints)

- `
  ``
  ``
  `

  ### [-queryStartingAtDocument:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryStartingAtDocument:)

  `
  `  
  Creates and returns a new `Query` that starts at the provided document (inclusive). The
  starting position is relative to the order of the query. The document must contain all of the
  fields provided in the orderBy of this query.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryStartingAtDocument:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html *)document;

  #### Parameters

  |------------------|-------------------------------------------|
  | ` `*document*` ` | The snapshot of the document to start at. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryStartingAtValues:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryStartingAtValues:)

  `
  `  
  Creates and returns a new `Query` that starts at the provided fields relative to the order of
  the query. The order of the field values must match the order of the order by clauses of the
  query.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryStartingAtValues:(nonnull NSArray *)fieldValues;

  #### Parameters

  |---------------------|----------------------------------------------------------------------------|
  | ` `*fieldValues*` ` | The field values to start this query at, in order of the query's order by. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryStartingAfterDocument:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryStartingAfterDocument:)

  `
  `  
  Creates and returns a new `Query` that starts after the provided document (exclusive). The
  starting position is relative to the order of the query. The document must contain all of the
  fields provided in the orderBy of this query.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryStartingAfterDocument:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html *)document;

  #### Parameters

  |------------------|----------------------------------------------|
  | ` `*document*` ` | The snapshot of the document to start after. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryStartingAfterValues:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryStartingAfterValues:)

  `
  `  
  Creates and returns a new `Query` that starts after the provided fields relative to the order
  of the query. The order of the field values must match the order of the order by clauses of the
  query.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryStartingAfterValues:(nonnull NSArray *)fieldValues;

  #### Parameters

  |---------------------|------------------------------------------------------------------------------|
  | ` `*fieldValues*` ` | The field values to start this query after, in order of the query's orderBy. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryEndingBeforeDocument:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryEndingBeforeDocument:)

  `
  `  
  Creates and returns a new `Query` that ends before the provided document (exclusive). The end
  position is relative to the order of the query. The document must contain all of the fields
  provided in the orderBy of this query.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryEndingBeforeDocument:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html *)document;

  #### Parameters

  |------------------|---------------------------------------------|
  | ` `*document*` ` | The snapshot of the document to end before. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryEndingBeforeValues:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryEndingBeforeValues:)

  `
  `  
  Creates and returns a new `Query` that ends before the provided fields relative to the order
  of the query. The order of the field values must match the order of the order by clauses of the
  query.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryEndingBeforeValues:(nonnull NSArray *)fieldValues;

  #### Parameters

  |---------------------|------------------------------------------------------------------------------|
  | ` `*fieldValues*` ` | The field values to end this query before, in order of the query's order by. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryEndingAtDocument:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryEndingAtDocument:)

  `
  `  
  Creates and returns a new `Query` that ends at the provided document (exclusive). The end
  position is relative to the order of the query. The document must contain all of the fields
  provided in the orderBy of this query.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryEndingAtDocument:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html *)document;

  #### Parameters

  |------------------|-----------------------------------------|
  | ` `*document*` ` | The snapshot of the document to end at. |

  #### Return Value

  The created `Query`.
- `
  ``
  ``
  `

  ### [-queryEndingAtValues:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)queryEndingAtValues:)

  `
  `  
  Creates and returns a new `Query` that ends at the provided fields relative to the order of
  the query. The order of the field values must match the order of the order by clauses of the
  query.  

  #### Declaration

  Objective-C  

      - (nonnull FIRQuery *)queryEndingAtValues:(nonnull NSArray *)fieldValues;

  #### Parameters

  |---------------------|--------------------------------------------------------------------------|
  | ` `*fieldValues*` ` | The field values to end this query at, in order of the query's order by. |

  #### Return Value

The created `Query`.  
[## Aggregation](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/Aggregation)

- `
  ``
  ``
  `

  ### [count](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(py)count)

  `
  `  
  A query that counts the documents in the result set of this query without actually downloading
  the documents.

  Using this `AggregateQuery` to count the documents is efficient because only the final count, not
  the documents' data, is downloaded. The `AggregateQuery` can count the documents in cases where
  the result set is prohibitively large to download entirely (thousands of documents).  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuery.html *_Nonnull count;

- `
  ``
  ``
  `

  ### [-aggregate:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery#/c:objc(cs)FIRQuery(im)aggregate:)

  `
  `  
  Creates and returns a new `AggregateQuery` that aggregates the documents in the result set
  of this query without actually downloading the documents.

  Using an `AggregateQuery` to perform aggregations is efficient because only the final aggregation
  values, not the documents' data, is downloaded. The returned `AggregateQuery` can perform
  aggregations of the documents in cases where the result set is prohibitively large to download
  entirely (thousands of documents).  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuery.html *)aggregate:
          (nonnull NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateField.html *> *)aggregateFields;

  #### Parameters

  |-------------------------|--------------------------------------------------------------------------------|
  | ` `*aggregateFields*` ` | Specifies the aggregate operations to perform on the result set of this query. |

  #### Return Value

  An `AggregateQuery` encapsulating this `Query` and `AggregateField`s, which can be used
  to query the server for the aggregation results.