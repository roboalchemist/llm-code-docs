# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTask.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTask.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTask.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTask.md.txt

# LoadBundleTask | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [firestore](https://firebase.google.com/docs/reference/js/v8/firebase.firestore).
- LoadBundleTask

Represents the task of loading a Firestore bundle. It provides progress of bundle
loading, as well as task completion and error events.

The API is compatible with `Promise<LoadBundleTaskProgress>`.

## Index

### Methods

- [catch](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTask#catch)
- [onProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTask#onprogress)
- [then](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTask#then)

## Methods

### catch

- catch \< R \> ( onRejected : ( a : [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error) ) =\> R \| PromiseLike \< R \> ) : Promise \< R \| [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTaskProgress) \>
- Implements the `Promise<LoadBundleTaskProgress>.catch` interface.

  #### Type parameters

  -

    #### R

  #### Parameters

  -

    ##### onRejected: (a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)) =\> R \| PromiseLike\<R\>

    Called when an error occurs during bundle loading.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)): R \| PromiseLike\<R\>

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)

        #### Returns R \| PromiseLike\<R\>

  #### Returns Promise\<R \| [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTaskProgress)\>

### onProgress

- onProgress ( next ? : ( progress : [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTaskProgress) ) =\> any , error ? : ( error : [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error) ) =\> any , complete ? : ( ) =\> void ) : void
- Registers functions to listen to bundle loading progress events.

  #### Parameters

  -

    ##### Optional next: (progress: [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTaskProgress)) =\> any

    Called when there is a progress update from bundle loading. Typically `next` calls occur
    each time a Firestore document is loaded from the bundle.
    -
      - (progress: [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTaskProgress)): any

      <!-- -->

      -

        #### Parameters

        -

          ##### progress: [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTaskProgress)

        #### Returns any

  -

    ##### Optional error: (error: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)) =\> any

    Called when an error occurs during bundle loading. The task aborts after reporting the
    error, and there should be no more updates after this.
    -
      - (error: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)): any

      <!-- -->

      -

        #### Parameters

        -

          ##### error: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)

        #### Returns any

  -

    ##### Optional complete: () =\> void

    Called when the loading task is complete.
    -
      - (): void

      <!-- -->

      -

        #### Returns void

  #### Returns void

### then

- then \< T , R \> ( onFulfilled ? : ( a : [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTaskProgress) ) =\> T \| PromiseLike \< T \> , onRejected ? : ( a : [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error) ) =\> R \| PromiseLike \< R \> ) : Promise \< T \| R \>
-
  Overrides PromiseLike.then  
  Implements the `Promise<LoadBundleTaskProgress>.then` interface.

  #### Type parameters

  -

    #### T

  -

    #### R

  #### Parameters

  -

    ##### Optional onFulfilled: (a: [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTaskProgress)) =\> T \| PromiseLike\<T\>

    Called on the completion of the loading task with a final `LoadBundleTaskProgress` update.
    The update will always have its `taskState` set to `"Success"`.
    -
      - (a: [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTaskProgress)): T \| PromiseLike\<T\>

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/v8/firebase.firestore.LoadBundleTaskProgress)

        #### Returns T \| PromiseLike\<T\>

  -

    ##### Optional onRejected: (a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)) =\> R \| PromiseLike\<R\>

    Called when an error occurs during bundle loading.
    -
      - (a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)): R \| PromiseLike\<R\>

      <!-- -->

      -

        #### Parameters

        -

          ##### a: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)

        #### Returns R \| PromiseLike\<R\>

  #### Returns Promise\<T \| R\>