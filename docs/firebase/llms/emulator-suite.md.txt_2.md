# Source: https://firebase.google.com/docs/reference/emulator-suite.md.txt

# Log Query Language for Emulator Suite UI

[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite) provides a rich user
interface that includes support for viewing emulator logs. You can filter logs
in the Emulator Suite UI using the query syntax described on this page.

The logs query language supports exact comparisons and `and`
operations. Other operations are not currently supported.

Quotes are generally optional, except when using spaces or newlines.

Note this query syntax is available in Emulator Suite UI only. Emulators
output additional logs in the `*-debug.log` files in your project
directory (e.g., `firestore-debug.log`).

```
// Find only info logs.
level=info

//Find logs for the sayHelloWorld function
metadata.emulator.name=functions
metadata.function.name=sayHelloWorld

//Find any log mentioning "hello world"
hello world // turns into search="hello world" internally

//Return any Hosting POST requests
metadata.emulator.name=hosting
search=POST
```

## Keywords

### level

Log level. One of `warn, info, error`.

### search

Text to match in a fuzzy search. For example, `search=abc`
returns logs with the text "abc".

Use the `search` keyword to combine fuzzy searches with other keyword
searches using the `and` operator.

### metadata

Query on a specific emulator or on a function name.

#### metadata.emulator.name

Query logs from a specified emulator. One of `firestore, functions,
database, pubsub, hosting, storage`.

#### metadata.function.name

The function name as defined in user app code.

### user

Any JSON data the user logged from in-app code, for example:

    console.log(JSON.stringify({hello: world}))

The above log output can be queried with `user.hello`.