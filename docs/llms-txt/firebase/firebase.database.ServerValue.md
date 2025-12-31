# Source: https://firebase.google.com/docs/reference/node/firebase.database.ServerValue.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.database.ServerValue.md.txt

# ServerValue | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [database](https://firebase.google.com/docs/reference/js/v8/firebase.database).
- ServerValue

## Index

### Variables

- [TIMESTAMP](https://firebase.google.com/docs/reference/js/v8/firebase.database.ServerValue#timestamp)

### Functions

- [increment](https://firebase.google.com/docs/reference/js/v8/firebase.database.ServerValue#increment)

## Variables

### TIMESTAMP

TIMESTAMP: Object  
A placeholder value for auto-populating the current timestamp (time
since the Unix epoch, in milliseconds) as determined by the Firebase
servers.

example
:

        var sessionsRef = firebase.database().ref("sessions");
        sessionsRef.push({
          startedAt: firebase.database.ServerValue.TIMESTAMP
        });


## Functions

### increment

- increment ( delta : number ) : Object
- Returns a placeholder value that can be used to atomically increment the
  current database value by the provided delta.

  #### Parameters

  -

    ##### delta: number

    the amount to modify the current value atomically.

  #### Returns Object

a placeholder value for modifying data atomically server-side.