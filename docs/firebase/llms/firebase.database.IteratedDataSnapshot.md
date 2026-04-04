# Source: https://firebase.google.com/docs/reference/js/v8/firebase.database.IteratedDataSnapshot.md.txt

# IteratedDataSnapshot | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [database](https://firebase.google.com/docs/reference/js/v8/firebase.database).
- IteratedDataSnapshot

## Index

### Properties

- [key](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#key)
- [ref](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#ref)

### Methods

- [child](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#child)
- [exists](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#exists)
- [exportVal](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#exportval)
- [forEach](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#foreach)
- [getPriority](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#getpriority)
- [hasChild](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#haschild)
- [hasChildren](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#haschildren)
- [numChildren](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#numchildren)
- [toJSON](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#tojson)
- [val](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot#val)

## Properties

### key

key: string
| Overrides [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[key](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#key)

### ref

ref: [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference)
Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[ref](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#ref)  
The `Reference` for the location that generated this `DataSnapshot`.

## Methods

### child

- child ( path : string ) : [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot)
-
  Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[child](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#child)  
  Gets another `DataSnapshot` for the location at the specified relative path.

  Passing a relative path to the `child()` method of a DataSnapshot returns
  another `DataSnapshot` for the location at the specified relative path. The
  relative path can either be a simple child name (for example, "ada") or a
  deeper, slash-separated path (for example, "ada/name/first"). If the child
  location has no data, an empty `DataSnapshot` (that is, a `DataSnapshot`
  whose value is `null`) is returned.

  example
  :

          // Assume we have the following data in the Database:
          {
            "name": {
              "first": "Ada",
              "last": "Lovelace"
            }
          }

          // Test for the existence of certain keys within a DataSnapshot
          var ref = firebase.database().ref("users/ada");
          ref.once("value")
            .then(function(snapshot) {
              var name = snapshot.child("name").val(); // {first:"Ada",last:"Lovelace"}
              var firstName = snapshot.child("name/first").val(); // "Ada"
              var lastName = snapshot.child("name").child("last").val(); // "Lovelace"
              var age = snapshot.child("age").val(); // null
            });


  #### Parameters

  -

    ##### path: string

    A relative path to the location of child data.

  #### Returns [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot)

### exists

- exists ( ) : boolean
-
  Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[exists](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#exists)  
  Returns true if this `DataSnapshot` contains any data. It is slightly more
  efficient than using `snapshot.val() !== null`.

  example
  :

          // Assume we have the following data in the Database:
          {
            "name": {
              "first": "Ada",
              "last": "Lovelace"
            }
          }

          // Test for the existence of certain keys within a DataSnapshot
          var ref = firebase.database().ref("users/ada");
          ref.once("value")
            .then(function(snapshot) {
              var a = snapshot.exists();  // true
              var b = snapshot.child("name").exists(); // true
              var c = snapshot.child("name/first").exists(); // true
              var d = snapshot.child("name/middle").exists(); // false
            });


  #### Returns boolean

### exportVal

- exportVal ( ) : any
-
  Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[exportVal](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#exportval)  
  Exports the entire contents of the DataSnapshot as a JavaScript object.

  The `exportVal()` method is similar to `val()`, except priority information
  is included (if available), making it suitable for backing up your data.

  #### Returns any

  The DataSnapshot's contents as a JavaScript value (Object,
  Array, string, number, boolean, or `null`).

### forEach

- forEach ( action : ( a : [IteratedDataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot) ) =\> boolean \| void ) : boolean
-
  Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[forEach](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#foreach)  
  Enumerates the top-level children in the `DataSnapshot`.

  Because of the way JavaScript objects work, the ordering of data in the
  JavaScript object returned by `val()` is not guaranteed to match the ordering
  on the server nor the ordering of `child_added` events. That is where
  `forEach()` comes in handy. It guarantees the children of a `DataSnapshot`
  will be iterated in their query order.

  If no explicit `orderBy*()` method is used, results are returned
  ordered by key (unless priorities are used, in which case, results are
  returned by priority).

  example
  :

          // Assume we have the following data in the Database:
          {
            "users": {
              "ada": {
                "first": "Ada",
                "last": "Lovelace"
              },
              "alan": {
                "first": "Alan",
                "last": "Turing"
              }
            }
          }

          // Loop through users in order with the forEach() method. The callback
          // provided to forEach() will be called synchronously with a DataSnapshot
          // for each child:
          var query = firebase.database().ref("users").orderByKey();
          query.once("value")
            .then(function(snapshot) {
              snapshot.forEach(function(childSnapshot) {
                // key will be "ada" the first time and "alan" the second time
                var key = childSnapshot.key;
                // childData will be the actual contents of the child
                var childData = childSnapshot.val();
            });
          });


  example
  :

          // You can cancel the enumeration at any point by having your callback
          // function return true. For example, the following code sample will only
          // fire the callback function one time:
          var query = firebase.database().ref("users").orderByKey();
          query.once("value")
            .then(function(snapshot) {
              snapshot.forEach(function(childSnapshot) {
                var key = childSnapshot.key; // "ada"

                // Cancel enumeration
                return true;
            });
          });


  #### Parameters

  -

    ##### action: (a: [IteratedDataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot)) =\> boolean \| void

    A function
    that will be called for each child DataSnapshot. The callback can return
    true to cancel further enumeration.
    -
      - (a: [IteratedDataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot)): boolean \| void

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [IteratedDataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.iterateddatasnapshot)

        #### Returns boolean \| void

  #### Returns boolean

  true if enumeration was canceled due to your callback
  returning true.

### getPriority

- getPriority ( ) : string \| number \| null
-
  Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[getPriority](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#getpriority)  
  Gets the priority value of the data in this `DataSnapshot`.

  Applications need not use priority but can order collections by
  ordinary properties (see
  [Sorting and filtering data](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data)).

  #### Returns string \| number \| null

### hasChild

- hasChild ( path : string ) : boolean
-
  Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[hasChild](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#haschild)  
  Returns true if the specified child path has (non-null) data.

  example
  :

          // Assume we have the following data in the Database:
          {
            "name": {
              "first": "Ada",
              "last": "Lovelace"
            }
          }

          // Determine which child keys in DataSnapshot have data.
          var ref = firebase.database().ref("users/ada");
          ref.once("value")
            .then(function(snapshot) {
              var hasName = snapshot.hasChild("name"); // true
              var hasAge = snapshot.hasChild("age"); // false
            });


  #### Parameters

  -

    ##### path: string

    A relative path to the location of a potential child.

  #### Returns boolean

  `true` if data exists at the specified child path; else
  `false`.

### hasChildren

- hasChildren ( ) : boolean
-
  Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[hasChildren](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#haschildren)  
  Returns whether or not the `DataSnapshot` has any non-`null` child
  properties.

  You can use `hasChildren()` to determine if a `DataSnapshot` has any
  children. If it does, you can enumerate them using `forEach()`. If it
  doesn't, then either this snapshot contains a primitive value (which can be
  retrieved with `val()`) or it is empty (in which case, `val()` will return
  `null`).

  example
  :

          // Assume we have the following data in the Database:
          {
            "name": {
              "first": "Ada",
              "last": "Lovelace"
            }
          }

          var ref = firebase.database().ref("users/ada");
          ref.once("value")
            .then(function(snapshot) {
              var a = snapshot.hasChildren(); // true
              var b = snapshot.child("name").hasChildren(); // true
              var c = snapshot.child("name/first").hasChildren(); // false
            });


  #### Returns boolean

  true if this snapshot has any children; else false.

### numChildren

- numChildren ( ) : number
-
  Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[numChildren](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#numchildren)  
  Returns the number of child properties of this `DataSnapshot`.

  example
  :

          // Assume we have the following data in the Database:
          {
            "name": {
              "first": "Ada",
              "last": "Lovelace"
            }
          }

          var ref = firebase.database().ref("users/ada");
          ref.once("value")
            .then(function(snapshot) {
              var a = snapshot.numChildren(); // 1 ("name")
              var b = snapshot.child("name").numChildren(); // 2 ("first", "last")
              var c = snapshot.child("name/first").numChildren(); // 0
            });


  #### Returns number

### toJSON

- toJSON ( ) : Object \| null
-
  Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[toJSON](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#tojson)  
  Returns a JSON-serializable representation of this object.

  #### Returns Object \| null

### val

- val ( ) : any
-
  Inherited from [DataSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot).[val](https://firebase.google.com/docs/reference/js/v8/firebase.database.DataSnapshot#val)  
  Extracts a JavaScript value from a `DataSnapshot`.

  Depending on the data in a `DataSnapshot`, the `val()` method may return a
  scalar type (string, number, or boolean), an array, or an object. It may also
  return null, indicating that the `DataSnapshot` is empty (contains no data).

  example
  :

          // Write and then read back a string from the Database.
          ref.set("hello")
            .then(function() {
              return ref.once("value");
            })
            .then(function(snapshot) {
              var data = snapshot.val(); // data === "hello"
            });


  example
  :

          // Write and then read back a JavaScript object from the Database.
          ref.set({ name: "Ada", age: 36 })
            .then(function() {
             return ref.once("value");
            })
            .then(function(snapshot) {
              var data = snapshot.val();
              // data is { "name": "Ada", "age": 36 }
              // data.name === "Ada"
              // data.age === 36
            });


  #### Returns any

  The DataSnapshot's contents as a JavaScript value (Object,
Array, string, number, boolean, or `null`).