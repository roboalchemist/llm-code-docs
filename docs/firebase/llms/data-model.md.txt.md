# Source: https://firebase.google.com/docs/firestore/data-model.md.txt

[Video](https://www.youtube.com/watch?v=v_hR4K4auoQ)

Cloud Firestore is a NoSQL, document-oriented database. Unlike a SQL database,
there are no tables or rows. Instead, you store data in *documents* , which are
organized into *collections*.

Each *document* contains a set of key-value pairs. Cloud Firestore is
optimized for storing large collections of small documents.

All documents must be stored in collections. Documents can contain
*subcollections* and nested objects, both of which can include primitive fields
like strings or complex objects like lists.

Collections and documents are created implicitly in Cloud Firestore.
Simply assign data to a document within a collection. If either the collection
or document does not exist, Cloud Firestore creates it.

## Documents

In Cloud Firestore, the unit of storage is the document. A document is a
lightweight record that contains fields, which map to values. Each document is
identified by a name.

A document representing a user `alovelace` might look like this:

- alovelace

  `first : "Ada"`  

  `last : "Lovelace"`  

  `born : 1815`  

> [!NOTE]
> **Note:** Cloud Firestore supports a variety of data types for values: boolean, number, string, geo point, binary blob, and timestamp. You can also use arrays or nested objects, called maps, to structure data within a document.

Complex, nested objects in a document are called maps. For example, you could
structure the user's name from the example above with a map, like this:

- alovelace

  `name :`  

  `first : "Ada"`  

  `last : "Lovelace"`  

  `born : 1815`  

You may notice that documents look a lot like JSON. In fact, they basically are.
There are some differences (for example, documents support extra data types and
are limited to the [document size limit](https://firebase.google.com/docs/firestore/quotas#collections_documents_and_fields)), but in general, you can treat documents as
lightweight JSON records.

## Collections

![](https://firebase.google.com/static/docs/firestore/images/structure-data.png)

Documents live in collections, which are simply containers for documents. For
example, you could have a `users` collection to contain your various users, each
represented by a document:

- users

  - alovelace

    `first : "Ada"`  

    `last : "Lovelace"`  

    `born : 1815`  
  - aturing

    `first : "Alan"`  

    `last : "Turing"`  

    `born : 1912`  

Cloud Firestore is schemaless, so you have complete freedom over what
fields you put in each document and what data types you store in those fields.
Documents within the same collection can all contain different fields or store
different types of data in those fields. However, it's a good idea to use the
same fields and data types across multiple documents, so that you can query the
documents more easily.

A collection contains documents and nothing else. It can't directly contain raw
fields with values, and it can't contain other collections. (See [Hierarchical
Data](https://firebase.google.com/docs/firestore/data-model#hierarchical-data) for an explanation of how to structure more complex
data in Cloud Firestore.)

The names of documents within a collection are unique. You can provide your own
keys, such as user IDs, or you can let Cloud Firestore create random IDs
for you automatically.

You do not need to "create" or "delete" collections. After you create the first
document in a collection, the collection exists. If you delete all of the
documents in a collection, it no longer exists.

## References

Every document in Cloud Firestore is uniquely identified by its location
within the database. The previous example showed a document `alovelace` within
the collection `users`. To refer to this location in your code, you can create a
*reference* to it.

### Web

```javascript
import { doc } from "firebase/firestore";

const alovelaceDocumentRef = doc(db, 'users', 'alovelace');
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
var alovelaceDocumentRef = db.collection('users').doc('alovelace');
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
let alovelaceDocumentRef = db.collection("users").document("alovelace")
```

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
FIRDocumentReference *alovelaceDocumentRef =
    [[self.db collectionWithPath:@"users"] documentWithPath:@"alovelace"];
```

### Kotlin

```kotlin
val alovelaceDocumentRef = db.collection("users").document("alovelace")
```

### Java

```java
DocumentReference alovelaceDocumentRef = db.collection("users").document("alovelace");
```

### Dart

```dart
final alovelaceDocumentRef = db.collection("users").doc("alovelace");
```

##### Java

    // Reference to a document with id "alovelace" in the collection "users"
    DocumentReference document = db.collection("users").document("alovelace");https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L52-L53

##### Python

    a_lovelace_ref = db.collection("users").document("alovelace")https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L280-L280

### Python

    a_lovelace_ref = db.collection("users").document("alovelace")https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L275-L275

##### C++

```c++
DocumentReference alovelace_document_reference =
    db->Collection("users").Document("alovelace");
```

##### Node.js

    const alovelaceDocumentRef = db.collection('users').doc('alovelace');https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L132-L132

##### Go


    import (
    	"cloud.google.com/go/firestore"
    )

    func createDocReference(client *firestore.Client) {

    	alovelaceRef := client.Collection("users").Doc("alovelace")

    	_ = alovelaceRef
    }
    https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/retrieve_data_reference_document.go#L18-L29

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $document = $db->collection('samples/php/users')->document('alovelace');https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/data_reference_document.php#L40-L40

##### Unity

```c#
DocumentReference documentRef = db.Collection("users").Document("alovelace");
```

##### C#

### C#


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    DocumentReference documentRef = db.Collection("users").Document("alovelace");https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/DataModel/Program.cs#L42-L42

##### Ruby

    document_ref = firestore.col("users").doc("alovelace")https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/data_model.rb#L22-L22

A reference is a lightweight object that just points to a location in your
database. You can create a reference whether or not data exists there, and
creating a reference does not perform any network operations.

You can also create references to *collections*:

### Web

```javascript
import { collection } from "firebase/firestore";

const usersCollectionRef = collection(db, 'users');
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
var usersCollectionRef = db.collection('users');
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
let usersCollectionRef = db.collection("users")
```

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
FIRCollectionReference *usersCollectionRef = [self.db collectionWithPath:@"users"];
```

### Kotlin

```kotlin
val usersCollectionRef = db.collection("users")
```

### Java

```java
CollectionReference usersCollectionRef = db.collection("users");
```

### Dart

```dart
final usersCollectionRef = db.collection("users");
```

##### Java

    // Reference to the collection "users"
    CollectionReference collection = db.collection("users");https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L39-L40

##### Python

    users_ref = db.collection("users")https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L288-L288

### Python

    users_ref = db.collection("users")https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L283-L283

##### C++

```c++
CollectionReference users_collection_reference = db->Collection("users");
```

##### Node.js

    const usersCollectionRef = db.collection('users');https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L136-L136

##### Go


    import (
    	"cloud.google.com/go/firestore"
    )

    func createCollectionReference(client *firestore.Client) {
    	usersRef := client.Collection("users")

    	_ = usersRef
    }
    https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/retrieve_data_reference_collection.go#L18-L28

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $collection = $db->collection('samples/php/users');https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/data_reference_collection.php#L40-L40

##### Unity

```c#
CollectionReference collectionRef = db.Collection("users");
```

##### C#

### C#


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    CollectionReference collectionRef = db.Collection("users");https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/DataModel/Program.cs#L50-L50

##### Ruby

    collection_ref = firestore.col "users"https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/data_model.rb#L31-L31

> [!NOTE]
> **Note:** *Collection references* and *document references* are two distinct types of references and let you perform different operations. For example, you could use a collection reference for querying the documents in the collection, and you could use a document reference to read or write an individual document.

For convenience, you can also create references by specifying the path to a
document or collection as a string, with path components separated by a forward
slash (`/`). For example, to create a reference to the `alovelace` document:

### Web

```javascript
import { doc } from "firebase/firestore"; 

const alovelaceDocumentRef = doc(db, 'users/alovelace');
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
var alovelaceDocumentRef = db.doc('users/alovelace');
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
let aLovelaceDocumentReference = db.document("users/alovelace")
```

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
FIRDocumentReference *aLovelaceDocumentReference =
    [self.db documentWithPath:@"users/alovelace"];
```

### Kotlin

```kotlin
val alovelaceDocumentRef = db.document("users/alovelace")
```

### Java

```java
DocumentReference alovelaceDocumentRef = db.document("users/alovelace");
```

### Dart

```dart
final aLovelaceDocRef = db.doc("users/alovelace");
```

##### Java

    // Reference to a document with id "alovelace" in the collection "users"
    DocumentReference document = db.document("users/alovelace");https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L65-L66

##### Python

    a_lovelace_ref = db.document("users/alovelace")https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L296-L296

### Python

    a_lovelace_ref = db.document("users/alovelace")https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L291-L291

##### C++

```c++
DocumentReference alovelace_document = db->Document("users/alovelace");
```

##### Node.js

    const alovelaceDocumentRef = db.doc('users/alovelace');https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L142-L142

##### Go


    import (
    	"cloud.google.com/go/firestore"
    )

    func createDocReferenceFromString(client *firestore.Client) {
    	// Reference to a document with id "alovelace" in the collection "users"
    	alovelaceRef := client.Doc("users/alovelace")

    	_ = alovelaceRef
    }
    https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/retrieve_data_reference_document_path.go#L18-L29

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $document = $db->document('users/alovelace');https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/data_reference_document_path.php#L40-L40

##### Unity

```c#
DocumentReference documentRef = db.Document("users/alovelace");
```

##### C#

### C#


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    DocumentReference documentRef = db.Document("users/alovelace");https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/DataModel/Program.cs#L58-L58

##### Ruby

    document_path_ref = firestore.doc "users/alovelace"https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/data_model.rb#L40-L40

## Hierarchical Data

To understand how hierarchical data structures work in Cloud Firestore,
consider an example chat app with messages and chat rooms.

You can create a collection called `rooms` to store different chat rooms:

- rooms

  - roomA

    `name : "my chat room"`  
  - roomB

    `...`  

Now that you have chat rooms, decide how to store your messages. You might not
want to store them in the chat room's document. Documents in Cloud Firestore
should be lightweight, and a chat room could contain a large number of messages.
However, you can create additional collections within your chat room's document,
as subcollections.

### Subcollections

The best way to store messages in this scenario is by using subcollections. A
subcollection is a collection associated with a specific document.

> [!NOTE]
> **Note:** You can query across subcollections with the same collection ID by using [Collection Group Queries](https://firebase.google.com/docs/firestore/query-data/queries#collection-group-query).

You can create a subcollection called `messages` for every room document in
your `rooms` collection:

- rooms

  - roomA

    `name : "my chat room"`  
    -
      messages

      -
        message1

        `from : "alex"`  

        `msg : "Hello World!"`  
      -
        message2

        `...`  
  - roomB

    `...`  

In this example, you would create a reference to a message in the subcollection
with the following code:

### Web

```javascript
import { doc } from "firebase/firestore"; 

const messageRef = doc(db, "rooms", "roomA", "messages", "message1");
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
var messageRef = db.collection('rooms').doc('roomA')
                .collection('messages').doc('message1');
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
let messageRef = db
  .collection("rooms").document("roomA")
  .collection("messages").document("message1")
```

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
FIRDocumentReference *messageRef =
    [[[[self.db collectionWithPath:@"rooms"] documentWithPath:@"roomA"]
    collectionWithPath:@"messages"] documentWithPath:@"message1"];
```

### Kotlin

```kotlin
val messageRef = db
    .collection("rooms").document("roomA")
    .collection("messages").document("message1")
```

### Java

```java
DocumentReference messageRef = db
        .collection("rooms").document("roomA")
        .collection("messages").document("message1");
```

### Dart

```dart
final messageRef = db
    .collection("rooms")
    .doc("roomA")
    .collection("messages")
    .doc("message1");
```

##### Java

    // Reference to a document in subcollection "messages"
    DocumentReference document =
        db.collection("rooms").document("roomA").collection("messages").document("message1");https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L78-L80

##### Python

    room_a_ref = db.collection("rooms").document("roomA")
    message_ref = room_a_ref.collection("messages").document("message1")https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L305-L306

### Python

    room_a_ref = db.collection("rooms").document("roomA")
    message_ref = room_a_ref.collection("messages").document("message1")https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L300-L301

##### C++

```c++
DocumentReference message_reference = db->Collection("rooms")
    .Document("roomA")
    .Collection("messages")
    .Document("message1");
```

##### Node.js

    const messageRef = db.collection('rooms').doc('roomA')
      .collection('messages').doc('message1');https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L146-L147

##### Go


    import (
    	"cloud.google.com/go/firestore"
    )

    func createSubcollectionReference(client *firestore.Client) {
    	messageRef := client.Collection("rooms").Doc("roomA").
    		Collection("messages").Doc("message1")

    	_ = messageRef
    }
    https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/retrieve_data_reference_subcollection.go#L18-L29

##### PHP

### PHP


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    $document = $db
        ->collection('rooms')
        ->document('roomA')
        ->collection('messages')
        ->document('message1');https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/data_reference_subcollection.php#L40-L44

##### Unity

```c#
DocumentReference documentRef = db
	.Collection("Rooms").Document("RoomA")
	.Collection("Messages").Document("Message1");
```

##### C#

### C#


For more on installing and creating a Cloud Firestore client, refer to
[Cloud Firestore Client Libraries](https://firebase.google.com/firestore/docs/reference/libraries).

    DocumentReference documentRef = db
        .Collection("Rooms").Document("RoomA")
        .Collection("Messages").Document("Message1");https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/DataModel/Program.cs#L66-L68

##### Ruby

    message_ref = firestore.col("rooms").doc("roomA").col("messages").doc("message1")https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/data_model.rb#L49-L49

Notice the alternating pattern of collections and documents. Your collections
and documents must always follow this pattern. You cannot reference a collection
in a collection or a document in a document.

Subcollections allow you to structure data hierarchically, making data easier to
access. To get all messages in `roomA`, you can create a collection reference
to the subcollection `messages` and interact with it like you would any other
collection reference.

Documents in subcollections can contain subcollections as well, allowing you to
further nest data. You can nest data up to 100 levels deep.

> [!WARNING]
> **Warning:** Deleting a document does not delete its subcollections!  
>
> When you delete a document that has subcollections, those subcollections are not deleted. For example, there may be a document located at `coll/doc/subcoll/subdoc` even though the document `coll/doc` no longer exists. If you want to delete documents in subcollections when deleting a parent document, you must do so manually, as shown in [Delete
> Collections](https://firebase.google.com/docs/firestore/manage-data/delete-data#collections).