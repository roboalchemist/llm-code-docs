# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes.md.txt

# FirebaseDatabase Framework Reference

# Classes

The following classes are available globally.
- `


  ### [DataSnapshot](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot)


  ` A DataSnapshot contains data from a Firebase Database location. Any time
  you read Firebase data, you receive the data as a DataSnapshot.

  DataSnapshots are passed to the blocks you attach with
  `observe(_:with:)` or `observeSingleEvent(of:with:)`. They are
  efficiently-generated immutable copies of the data at a Firebase Database
  location. They can't be modified and will never change. To modify data at a
  location, use a DatabaseReference (e.g. with `setValue(_:)`).

  #### Declaration

  Swift

      class DataSnapshot : NSObject, @unchecked Sendable

- `


  ### [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference)


  ` A FIRDatabaseReference represents a particular location in your Firebase
  Database and can be used for reading or writing data to that Firebase
  Database location.

  This class is the starting point for all Firebase Database operations. After
  you've obtained your first FIRDatabaseReference via \[FIRDatabase reference\],
  you can use it to read data (ie. observeEventType:withBlock:), write data
  (ie. setValue:), and to create new FIRDatabaseReferences (ie. child:).

  #### Declaration

  Swift

      class DatabaseReference : https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery

- `


  ### [Database](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database)


  ` The entry point for accessing a Firebase Database. You can get an instance
  by calling `https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(cm)database`. To access a location in the database and
  read or write data, use `FIRDatabase.reference()`.

  #### Declaration

  Swift

      class Database : NSObject

- `


  ### [DatabaseQuery](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseQuery)


  ` A `DatabaseQuery` instance represents a query over the data at a particular
  location.

  You create one by calling one of the query methods (`queryOrdered(byChild:)`,
  `queryStarting(atValue:)`, etc.) on a `https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference`. The query methods
  can be chained to further specify the data you are interested in observing.

  #### Declaration

  Swift

      class DatabaseQuery : NSObject

- `


  ### [MutableData](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData)


  ` A `MutableData` instance is populated with data from a Firebase Database
  location. When you are using `runTransactionBlock(_:)`, you will be given an
  instance containing the current data at that location. Your block will be
  responsible for updating that instance to the data you wish to save at that
  location, and then returning using `https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/TransactionResult#/c:objc(cs)FIRTransactionResult(cm)successWithValue:`.

  To modify the data, set its value property to any of the Objective-C types
  supported by Firebase Database, or any equivalent natively bridgeable Swift
  type:
  - `NSNumber` (includes booleans)
  - `NSDictionary`
  - `NSArray`
  - `NSString`
  - `nil` / `NSNull` to remove the data

  Note that changes made to a child `MutableData` instance will be visible to
  the parent.

  #### Declaration

  Swift

      class MutableData : NSObject

- `


  ### [ServerValue](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/ServerValue)


  ` Placeholder values you may write into Firebase Database as a value or
  priority that will automatically be populated by the Firebase Database
  server.

  #### Declaration

  Swift

      class ServerValue : NSObject

- `


  ### [TransactionResult](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/TransactionResult)


  ` Used for `runTransactionBlock(_:)`. A `TransactionResult` instance is a
  container for the results of the transaction.

  #### Declaration

  Swift

      class TransactionResult : NSObject