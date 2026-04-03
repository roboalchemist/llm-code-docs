# Source: https://firebase.google.com/docs/reference/functions/test/test.EventContextOptions.md.txt

# Interface: EventContextOptions

# [test](https://firebase.google.com/docs/reference/functions/test/test).EventContextOptions

interface static

Fields of the event context that can be overridden/customized.

## Properties

### auth

nullable Object

This option is only available for Realtime Database functions. Authentication information for the user that triggered the function. This object contains `uid` and `token` properties for authenticated users. For more
detail including token keys, see the
[security rules reference](https://firebase.google.com/docs/firestore/reference/security#properties).

Defaults to null.

### authType

(string or undefined)

This option is only available for Realtime Database functions. The level of permissions for a user. Valid values are:

- `ADMIN` Developer user or user authenticated via a service account.
- `USER` Known user.
- `UNAUTHENTICATED` Unauthenticated action

If omitted, defaults to 'UNAUTHENTICATED'.

### eventId

(string or undefined)

The event's unique identifier. If omitted, a random ID will be generated.

### params

(non-null Object or undefined)

The values for the wildcards in the reference path that a database or Firestore function is listening to. If omitted, random values are generated.

### timestamp

(string or undefined)

Timestamp for the event as an
[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) string. If omitted, the current time is used.