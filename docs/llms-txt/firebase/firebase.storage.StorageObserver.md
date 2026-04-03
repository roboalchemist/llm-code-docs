# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.StorageObserver.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.storage.StorageObserver.md.txt

# StorageObserver | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [storage](https://firebase.google.com/docs/reference/node/firebase.storage).
- StorageObserver
\< T \>

### Type parameters

-

  #### T

## Index

### Properties

- [complete](https://firebase.google.com/docs/reference/node/firebase.storage.StorageObserver#complete)
- [error](https://firebase.google.com/docs/reference/node/firebase.storage.StorageObserver#error)
- [next](https://firebase.google.com/docs/reference/node/firebase.storage.StorageObserver#next)

## Properties

### Optional complete

complete: CompleteFn \| null

### Optional error

error: (error: [FirebaseStorageError](https://firebase.google.com/docs/reference/node/firebase.storage.FirebaseStorageError)) =\> void \| null  

#### Type declaration

-
  - (error: [FirebaseStorageError](https://firebase.google.com/docs/reference/node/firebase.storage.FirebaseStorageError)): void \| null

  <!-- -->

  -

    #### Parameters

    -

      ##### error: [FirebaseStorageError](https://firebase.google.com/docs/reference/node/firebase.storage.FirebaseStorageError)

    #### Returns void \| null

### Optional next

next: NextFn\<T\> \| null