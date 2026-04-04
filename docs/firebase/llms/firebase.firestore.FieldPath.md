# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FieldPath.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath.md.txt

# FieldPath | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [firestore](https://firebase.google.com/docs/reference/node/firebase.firestore).
- FieldPath

A FieldPath refers to a field in a document. The path may consist of a
single field name (referring to a top-level field in the document), or a
list of field names (referring to a nested field in the document).

Create a FieldPath by providing field names. If more than one field
name is provided, the path will point to a nested field in a document.

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath#constructor)

### Methods

- [isEqual](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath#isequal)
- [documentId](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath#documentid)

## Constructors

### constructor

- new FieldPath ( ... fieldNames : string \[\] ) : [FieldPath](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath)
- Creates a FieldPath from the provided field names. If more than one field
  name is provided, the path will point to a nested field in a document.

  #### Parameters

  -

    ##### Rest ...fieldNames: string\[\]

    A list of field names.

  #### Returns [FieldPath](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath)

## Methods

### isEqual

- isEqual ( other : [FieldPath](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath) ) : boolean
- Returns true if this `FieldPath` is equal to the provided one.

  #### Parameters

  -

    ##### other: [FieldPath](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath)

    The `FieldPath` to compare against.

  #### Returns boolean

  true if this `FieldPath` is equal to the provided one.

### Static documentId

- documentId ( ) : [FieldPath](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath)
- Returns a special sentinel `FieldPath` to refer to the ID of a document.
  It can be used in queries to sort or filter by the document ID.

  #### Returns [FieldPath](https://firebase.google.com/docs/reference/node/firebase.firestore.FieldPath)