# Source: https://firebase.google.com/docs/reference/rules/rules.firestore.md.txt

# Namespace: firestore

# [rules](https://firebase.google.com/docs/reference/rules/rules).firestore

namespace static

Context specific variables and methods for Cloud Firestore
security rules.

Functions in this namespace are only available inside
`service cloud.firestore { ... }` blocks and
do not need to be prefixed when used (`get()`
not `firestore.get()`).

## Interfaces

### [Request](https://firebase.google.com/docs/reference/rules/rules.firestore.Request)

The incoming request context for a Firestore operation.

### [Resource](https://firebase.google.com/docs/reference/rules/rules.firestore.Resource)

The Firestore document being read or written.

## Properties

### request

static

non-null [rules.firestore.Request](https://firebase.google.com/docs/reference/rules/rules.firestore.Request)

The request context, including authentication information
and pending data.

### resource

static

non-null [rules.firestore.Resource](https://firebase.google.com/docs/reference/rules/rules.firestore.Resource)

The resource being read or written.

## Methods

### exists

static

exists(path) returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Check if a document exists.

|                                                  #### Parameter                                                   ||
|------|-------------------------------------------------------------------------------------------------------------|
| path | [rules.Path](https://firebase.google.com/docs/reference/rules/rules.Path) The path. Value must not be null. |

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) true if the resource exists.

#### Example

    // Check if another document exists
    allow write: if exists(/databases/$(database)/documents/things/other)

### existsAfter

static

existsAfter(path) returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Check if a document exists, assuming the current request succeeds. Equivalent
to getAfter(path) != null.

|                                                  #### Parameter                                                   ||
|------|-------------------------------------------------------------------------------------------------------------|
| path | [rules.Path](https://firebase.google.com/docs/reference/rules/rules.Path) The path. Value must not be null. |

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) true if the resource exists.

### get

static

get(path) returns [rules.firestore.Resource](https://firebase.google.com/docs/reference/rules/rules.firestore.Resource)

Get the contents of a firestore document.

|                                                  #### Parameter                                                   ||
|------|-------------------------------------------------------------------------------------------------------------|
| path | [rules.Path](https://firebase.google.com/docs/reference/rules/rules.Path) The path. Value must not be null. |

Returns

:   `non-null `[rules.firestore.Resource](https://firebase.google.com/docs/reference/rules/rules.firestore.Resource) the document, or null if it does not
    exist.

#### Example

    // Get the 'thing1' document from the 'things' collection
    get(/databases/$(database)/documents/things/thing1)

### getAfter

static

getAfter(path) returns [rules.firestore.Resource](https://firebase.google.com/docs/reference/rules/rules.firestore.Resource)

Get the projected contents of a document. The document is returned as
if the current request had succeeded. Useful for validating documents
that are part of a batched write or transaction.

|                                                  #### Parameter                                                   ||
|------|-------------------------------------------------------------------------------------------------------------|
| path | [rules.Path](https://firebase.google.com/docs/reference/rules/rules.Path) The path. Value must not be null. |

Returns

:   `non-null `[rules.firestore.Resource](https://firebase.google.com/docs/reference/rules/rules.firestore.Resource) the document, or null if it does not
    exist.