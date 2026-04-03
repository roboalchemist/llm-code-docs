# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.DocumentChange.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentChange.md.txt

# DocumentChange | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [firestore](https://firebase.google.com/docs/reference/node/firebase.firestore).
- DocumentChange
\< T \>

A `DocumentChange` represents a change to the documents matching a query.
It contains the document affected and the type of change that occurred.

### Type parameters

-

  #### T

## Index

### Properties

- [doc](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentChange#doc)
- [newIndex](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentChange#newindex)
- [oldIndex](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentChange#oldindex)
- [type](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentChange#type)

## Properties

### doc

doc: [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/node/firebase.firestore.QueryDocumentSnapshot)\<T\>  
The document affected by this change.

### newIndex

newIndex: number  
The index of the changed document in the result set immediately after
this `DocumentChange` (i.e. supposing that all prior `DocumentChange`
objects and the current `DocumentChange` object have been applied).
Is -1 for 'removed' events.

### oldIndex

oldIndex: number  
The index of the changed document in the result set immediately prior to
this `DocumentChange` (i.e. supposing that all prior `DocumentChange` objects
have been applied). Is -1 for 'added' events.

### type

type: [DocumentChangeType](https://firebase.google.com/docs/reference/node/firebase.firestore#documentchangetype)  
The type of change ('added', 'modified', or 'removed').