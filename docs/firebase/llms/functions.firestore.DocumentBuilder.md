# Source: https://firebase.google.com/docs/reference/functions/test/functions.firestore.DocumentBuilder.md.txt

# Interface: DocumentBuilder

# functions.firestore.DocumentBuilder

interface static

The Cloud Firestore document builder interface.

Access via [`functions.firestore.document()`](https://firebase.google.com/docs/reference/functions/test/functions.firestore#.document).

## Methods

### onCreate

onCreate(handler) returns functions.CloudFunction containing non-null [functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot)

Event handler that fires every time new data is created in Cloud Firestore.

|                                                                                                                                                     #### Parameter                                                                                                                                                     ||
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| handler | function(non-null functions.Event containing non-null [functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot)) Event handler which is run every time new data is created in Cloud Firestore. Value must not be null. |

Returns

:   `non-null functions.CloudFunction containing non-null `[functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot) A Cloud Function which you can export.

### onDelete

onDelete(handler) returns functions.CloudFunction containing non-null [functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot)

Event handler that fires every time data is deleted from Cloud Firestore.

|                                                                                                                                                    #### Parameter                                                                                                                                                    ||
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| handler | function(non-null functions.Event containing non-null [functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot)) Event handler which is run every time data is deleted from Cloud Firestore. Value must not be null. |

Returns

:   `non-null functions.CloudFunction containing non-null `[functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot) A Cloud Function which you can export.

### onUpdate

onUpdate(handler) returns functions.CloudFunction containing non-null [functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot)

Event handler that fires every time data is updated in Cloud Firestore.

|                                                                                                                                                   #### Parameter                                                                                                                                                   ||
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| handler | function(non-null functions.Event containing non-null [functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot)) Event handler which is run every time data is updated in Cloud Firestore. Value must not be null. |

Returns

:   `non-null functions.CloudFunction containing non-null `[functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot) A Cloud Function which you can export.

### onWrite

onWrite(handler) returns functions.CloudFunction containing non-null [functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot)

Event handler that fires every time a Cloud Firestore write of any kind (creation, update, or delete) occurs.

|                                                                                                                                                 #### Parameter                                                                                                                                                 ||
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| handler | function(non-null functions.Event containing non-null [functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot)) Event handler which is run every time a Cloud Firestore write occurs. Value must not be null. |

Returns

:   `non-null functions.CloudFunction containing non-null `[functions.firestore.DeltaDocumentSnapshot](https://firebase.google.com/docs/reference/functions/test/functions.firestore.DeltaDocumentSnapshot) A Cloud Function which you can export.