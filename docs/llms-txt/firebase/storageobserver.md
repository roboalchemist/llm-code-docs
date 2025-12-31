# Source: https://firebase.google.com/docs/reference/js/v8/storageobserver.md.txt

# StorageObserver | JavaScript SDK

# - StorageObserver
\< T \>

### Type parameters

-

  #### T

## Index

### Properties

- [complete](https://firebase.google.com/docs/reference/js/v8/storageobserver#complete)
- [error](https://firebase.google.com/docs/reference/js/v8/storageobserver#error)
- [next](https://firebase.google.com/docs/reference/js/v8/storageobserver#next)

## Properties

### Optional complete

complete: CompleteFn \| null

### Optional error

error: (error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError)) =\> void \| null  

#### Type declaration

-
  - (error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError)): void \| null

  <!-- -->

  -

    #### Parameters

    -

      ##### error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError)

    #### Returns void \| null

### Optional next

next: NextFn\<T\> \| null