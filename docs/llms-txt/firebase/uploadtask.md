# Source: https://firebase.google.com/docs/reference/js/v8/uploadtask.md.txt

# UploadTask | JavaScript SDK

# - UploadTask

Represents the process of uploading an object. Allows you to monitor and
manage the upload.

## Index

### Properties

- [snapshot](https://firebase.google.com/docs/reference/js/v8/uploadtask#snapshot)

### Methods

- [cancel](https://firebase.google.com/docs/reference/js/v8/uploadtask#cancel)
- [catch](https://firebase.google.com/docs/reference/js/v8/uploadtask#catch)
- [on](https://firebase.google.com/docs/reference/js/v8/uploadtask#on)
- [pause](https://firebase.google.com/docs/reference/js/v8/uploadtask#pause)
- [resume](https://firebase.google.com/docs/reference/js/v8/uploadtask#resume)
- [then](https://firebase.google.com/docs/reference/js/v8/uploadtask#then)

## Properties

### snapshot

snapshot: firebase.storage.UploadTaskSnapshot  
A snapshot of the current task state.

## Methods

### cancel

- cancel ( ) : boolean
- Cancels a running task. Has no effect on a complete or failed task.

  #### Returns boolean

  True if the cancel had an effect.

### catch

- catch ( onRejected : ( error : [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError) ) =\> any ) : Promise \< any \>
- Equivalent to calling `then(null, onRejected)`.

  #### Parameters

  -

    ##### onRejected: (error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError)) =\> any

    -
      - (error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError)): any

      <!-- -->

      -

        #### Parameters

        -

          ##### error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError)

        #### Returns any

  #### Returns Promise\<any\>

### on

- on ( event : [TaskEvent](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskevent) , nextOrObserver ? : [StorageObserver](https://firebase.google.com/docs/reference/js/v8/storageobserver) \< [UploadTaskSnapshot](https://firebase.google.com/docs/reference/js/v8/uploadtasksnapshot) \> \| null \| ( ( snapshot : [UploadTaskSnapshot](https://firebase.google.com/docs/reference/js/v8/uploadtasksnapshot) ) =\> any ) , error ? : ( ( error : [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError) ) =\> any ) \| null , complete ? : firebase.Unsubscribe \| null ) : Function
- Listens for events on this task.

  Events have three callback functions (referred to as `next`, `error`, and
  `complete`).

  If only the event is passed, a function that can be used to register the
  callbacks is returned. Otherwise, the callbacks are passed after the event.

  Callbacks can be passed either as three separate arguments *or* as the
  `next`, `error`, and `complete` properties of an object. Any of the three
  callbacks is optional, as long as at least one is specified. In addition,
  when you add your callbacks, you get a function back. You can call this
  function to unregister the associated callbacks.

  example

  :   **Pass callbacks separately or in an object.**

          var next = function(snapshot) {};
          var error = function(error) {};
          var complete = function() {};

          // The first example.
          uploadTask.on(
              firebase.storage.TaskEvent.STATE_CHANGED,
              next,
              error,
              complete);

          // This is equivalent to the first example.
          uploadTask.on(firebase.storage.TaskEvent.STATE_CHANGED, {
            'next': next,
            'error': error,
            'complete': complete
          });

          // This is equivalent to the first example.
          var subscribe = uploadTask.on(firebase.storage.TaskEvent.STATE_CHANGED);
          subscribe(next, error, complete);

          // This is equivalent to the first example.
          var subscribe = uploadTask.on(firebase.storage.TaskEvent.STATE_CHANGED);
          subscribe({
            'next': next,
            'error': error,
            'complete': complete
          });

  example

  :   **Any callback is optional.**

          // Just listening for completion, this is legal.
          uploadTask.on(
              firebase.storage.TaskEvent.STATE_CHANGED,
              null,
              null,
              function() {
                console.log('upload complete!');
              });

          // Just listening for progress/state changes, this is legal.
          uploadTask.on(firebase.storage.TaskEvent.STATE_CHANGED, function(snapshot) {
            var percent = snapshot.bytesTransferred / snapshot.totalBytes * 100;
            console.log(percent + "% done");
          });

          // This is also legal.
          uploadTask.on(firebase.storage.TaskEvent.STATE_CHANGED, {
            'complete': function() {
              console.log('upload complete!');
            }
          });

  example

  :   **Use the returned function to remove callbacks.**

          var unsubscribe = uploadTask.on(
              firebase.storage.TaskEvent.STATE_CHANGED,
              function(snapshot) {
                var percent = snapshot.bytesTransferred / snapshot.totalBytes * 100;
                console.log(percent + "% done");
                // Stop after receiving one update.
                unsubscribe();
              });

          // This code is equivalent to the above.
          var handle = uploadTask.on(firebase.storage.TaskEvent.STATE_CHANGED);
          unsubscribe = handle(function(snapshot) {
            var percent = snapshot.bytesTransferred / snapshot.totalBytes * 100;
            console.log(percent + "% done");
            // Stop after receiving one update.
            unsubscribe();
          });

  #### Parameters

  -

    ##### event: [TaskEvent](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskevent)

    The event to listen for.
  -

    ##### Optional nextOrObserver: [StorageObserver](https://firebase.google.com/docs/reference/js/v8/storageobserver)\<[UploadTaskSnapshot](https://firebase.google.com/docs/reference/js/v8/uploadtasksnapshot)\> \| null \| ((snapshot: [UploadTaskSnapshot](https://firebase.google.com/docs/reference/js/v8/uploadtasksnapshot)) =\> any)

        The `next` function, which gets called for each item in
        the event stream, or an observer object with some or all of these three
        properties (`next`, `error`, `complete`).

  -

    ##### Optional error: ((error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError)) =\> any) \| null

    A function that gets called with a `FirebaseStorageError`
    if the event stream ends due to an error.
  -

    ##### Optional complete: firebase.Unsubscribe \| null

    A function that gets called if the
    event stream ends normally.

  #### Returns Function

      If only the event argument is passed, returns a function you can use to
      add callbacks (see the examples above). If more than just the event
      argument is passed, returns a function you can call to unregister the
      callbacks.

### pause

- pause ( ) : boolean
- Pauses a running task. Has no effect on a paused or failed task.

  #### Returns boolean

  True if the pause had an effect.

### resume

- resume ( ) : boolean
- Resumes a paused task. Has no effect on a running or failed task.

  #### Returns boolean

  True if the resume had an effect.

### then

- then ( onFulfilled ? : ( ( snapshot : firebase.storage.UploadTaskSnapshot ) =\> any ) \| null , onRejected ? : ( ( error : [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError) ) =\> any ) \| null ) : Promise \< any \>
- This object behaves like a Promise, and resolves with its snapshot data when
  the upload completes.

  #### Parameters

  -

    ##### Optional onFulfilled: ((snapshot: firebase.storage.UploadTaskSnapshot) =\> any) \| null

        The fulfillment callback. Promise chaining works as normal.

  -

    ##### Optional onRejected: ((error: [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError)) =\> any) \| null

    The rejection callback.

  #### Returns Promise\<any\>