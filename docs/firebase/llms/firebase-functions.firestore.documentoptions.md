# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md.txt

# firestore.DocumentOptions interface

DocumentOptions extend EventHandlerOptions with provided document and optional database and namespace.

**Signature:**  

    export interface DocumentOptions<Document extends string = string> extends EventHandlerOptions 

**Extends:** [EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)

## Properties

|                                                                             Property                                                                             |                                                                                 Type                                                                                 |       Description       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| [database](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptionsdatabase)   | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\>   | The Firestore database  |
| [document](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptionsdocument)   | Document \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> | The document path       |
| [namespace](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.firestore.documentoptions.md#firestoredocumentoptionsnamespace) | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\>   | The Firestore namespace |

## firestore.DocumentOptions.database

The Firestore database

**Signature:**  

    database?: string | Expression<string>;

## firestore.DocumentOptions.document

The document path

**Signature:**  

    document: Document | Expression<string>;

## firestore.DocumentOptions.namespace

The Firestore namespace

**Signature:**  

    namespace?: string | Expression<string>;