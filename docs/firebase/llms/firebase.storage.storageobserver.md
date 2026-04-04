# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.storageobserver.md.txt

# StorageObserver | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage).
- StorageObserver
\< T \>

### Type parameters

-

  #### T

## Index

### Properties

- [complete](https://firebase.google.com/docs/reference/js/v8/firebase.storage.storageobserver#complete)
- [error](https://firebase.google.com/docs/reference/js/v8/firebase.storage.storageobserver#error)
- [next](https://firebase.google.com/docs/reference/js/v8/firebase.storage.storageobserver#next)

## Properties

### Optional complete

complete: CompleteFn \| null

### Optional error

error: (error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.firebasestorageerror)) =\> void \| null  

#### Type declaration

-
  - (error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.firebasestorageerror)): void \| null

  <!-- -->

  -

    #### Parameters

    -

      ##### error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.firebasestorageerror)

    #### Returns void \| null

### Optional next

next: NextFn\<T\> \| null