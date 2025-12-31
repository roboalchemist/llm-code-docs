# Source: https://firebase.google.com/docs/reference/functions/test/test.storage.md.txt

# Namespace: storage

# [test](https://firebase.google.com/docs/reference/functions/test/test).storage

namespace static

Namespace for testing Storage functions using the Cloud Functions for Firebase Test SDK.

## Methods

### exampleObjectMetadata

static

exampleObjectMetadata() returns functions.storage.ObjectMetadata

Fetch an example `ObjectMetadata` already populated with data.

Returns

:   `non-null functions.storage.ObjectMetadata`

### makeObjectMetaData

static

makeObjectMetaData(fields) returns functions.storage.ObjectMetadata

|                                                                                                               #### Parameter                                                                                                                ||
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fields | Object Fields of `ObjectMetadata` to specify. Can be any subset of the fields in [functions.storage.ObjectMetadata](https://firebase.google.com/docs/reference/functions/functions.storage.ObjectMetadata). Value must not be null. |

Returns

:   `non-null functions.storage.ObjectMetadata`