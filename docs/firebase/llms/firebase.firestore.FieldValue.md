# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.FieldValue.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.FieldValue.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue.md.txt

# FieldValue | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- FieldValue

Sentinel values that can be used when writing document fields with `set()`
or `update()`.

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue#constructor)

### Methods

- [isEqual](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue#isequal)
- [arrayRemove](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue#arrayremove)
- [arrayUnion](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue#arrayunion)
- [delete](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue#delete)
- [increment](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue#increment)
- [serverTimestamp](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue#servertimestamp)

## Constructors

### Private constructor

- new FieldValue ( ) : [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)
-

  #### Returns [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)

## Methods

### isEqual

- isEqual ( other : [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue) ) : boolean
- Returns true if this `FieldValue` is equal to the provided one.

  #### Parameters

  -

    ##### other: [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)

    The `FieldValue` to compare against.

  #### Returns boolean

  true if this `FieldValue` is equal to the provided one.

### Static arrayRemove

- arrayRemove ( ... elements : any \[\] ) : [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)
- Returns a special value that can be used with `set()` or `update()` that tells
  the server to remove the given elements from any array value that already
  exists on the server. All instances of each element specified will be
  removed from the array. If the field being modified is not already an
  array it will be overwritten with an empty array.

  #### Parameters

  -

    ##### Rest ...elements: any\[\]

    The elements to remove from the array.

  #### Returns [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)

  The FieldValue sentinel for use in a call to `set()` or `update()`.

### Static arrayUnion

- arrayUnion ( ... elements : any \[\] ) : [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)
- Returns a special value that can be used with `set()` or `update()` that tells
  the server to union the given elements with any array value that already
  exists on the server. Each specified element that doesn't already exist in
  the array will be added to the end. If the field being modified is not
  already an array it will be overwritten with an array containing exactly
  the specified elements.

  #### Parameters

  -

    ##### Rest ...elements: any\[\]

    The elements to union into the array.

  #### Returns [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)

  The FieldValue sentinel for use in a call to `set()` or `update()`.

### Static delete

- delete ( ) : [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)
- Returns a sentinel for use with `update()` to mark a field for deletion.

  #### Returns [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)

### Static increment

- increment ( n : number ) : [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)
- Returns a special value that can be used with `set()` or `update()` that tells
  the server to increment the field's current value by the given value.

  If either the operand or the current field value uses floating point precision,
  all arithmetic follows IEEE 754 semantics. If both values are integers,
  values outside of JavaScript's safe number range (`Number.MIN_SAFE_INTEGER` to
  `Number.MAX_SAFE_INTEGER`) are also subject to precision loss. Furthermore,
  once processed by the Firestore backend, all integer operations are capped
  between -2\^63 and 2\^63-1.

  If the current field value is not of type `number`, or if the field does not
  yet exist, the transformation sets the field to the given value.

  #### Parameters

  -

    ##### n: number

    The value to increment by.

  #### Returns [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)

  The FieldValue sentinel for use in a call to `set()` or `update()`.

### Static serverTimestamp

- serverTimestamp ( ) : [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)
- Returns a sentinel used with `set()` or `update()` to include a
  server-generated timestamp in the written data.

  #### Returns [FieldValue](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldValue)