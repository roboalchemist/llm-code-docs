# Source: https://firebase.google.com/docs/reference/rules/rules.debug.md.txt

# Namespace: debug

# [rules](https://firebase.google.com/docs/reference/rules/rules).debug

namespace static

## debug

debug()

A basic debug function that prints Security Rules language
objects, variables and statement results as they are being
evaluated by the Security Rules engine. The outputs of `debug` are written to
firestore-debug.log.

The `debug` function can only be called inside Rules
[conditions](https://firebase.google.com/docs/rules/rules-language#building_conditions).

`debug` function blocks are only executed by the Security Rules engine in
the Firestore emulator, part of the Firebase Emulator Suite. The debug
function has no effect in production.

Debug logfile entries are prepended by a string identifying the Rules
language data type of the log output (for example, `string_value`,
`map_value`).

Calls to `debug` can be nested.

Currently, the `debug` feature does not support the concept of logging
levels (for example, INFO, WARN, ERROR).  

```scilab
// firestore.rules
// Nested debug calls in the following match block....
match /carts/{cartID} {
  allow create: if request.auth != null && request.auth.uid == request.resource.data.ownerUID;
    allow read, update, delete: if
      debug(
        debug(request.auth.uid) == debug(resource.data.ownerUID)
      );
  }
...

// firestore-debug.log
// ...produce logfile output like the following.
string_value: "alice" // for debug(request.auth.uid)

string_value: "alice" // for debug(resource.data.ownerUID)

bool_value: true      // for the outermost enclosing debug() call
...
```