# Source: https://firebase.google.com/docs/firestore/data-model.md.txt

<br />

Cloud Firestoreis a NoSQL, document-oriented database. Unlike a SQL database, there are no tables or rows. Instead, you store data in*documents* , which are organized into*collections*.

Each*document* contains a set of key-value pairs.Cloud Firestoreis optimized for storing large collections of small documents.

All documents must be stored in collections. Documents can contain*subcollections*and nested objects, both of which can include primitive fields like strings or complex objects like lists.

Collections and documents are created implicitly inCloud Firestore. Simply assign data to a document within a collection. If either the collection or document does not exist,Cloud Firestorecreates it.

## Documents

InCloud Firestore, the unit of storage is the document. A document is a lightweight record that contains fields, which map to values. Each document is identified by a name.

A document representing a user`alovelace`might look like this:

- classalovelace

  `first : "Ada"`  
  `last : "Lovelace"`  
  `born : 1815`  

| **Note:** Cloud Firestoresupports a variety of data types for values: boolean, number, string, geo point, binary blob, and timestamp. You can also use arrays or nested objects, called maps, to structure data within a document.

Complex, nested objects in a document are called maps. For example, you could structure the user's name from the example above with a map, like this:

- classalovelace

  `name :`  
  `first : "Ada"`  
  `last : "Lovelace"`  
  `born : 1815`  

You may notice that documents look a lot like JSON. In fact, they basically are. There are some differences (for example, documents support extra data types and are limited in size to 1 MB), but in general, you can treat documents as lightweight JSON records.

## Collections

![](https://firebase.google.com/static/docs/firestore/images/structure-data.png)

Documents live in collections, which are simply containers for documents. For example, you could have a`users`collection to contain your various users, each represented by a document:

- collections_bookmarkusers

  - classalovelace

    `first : "Ada"`  
    `last : "Lovelace"`  
    `born : 1815`  
  - classaturing

    `first : "Alan"`  
    `last : "Turing"`  
    `born : 1912`  

Cloud Firestoreis schemaless, so you have complete freedom over what fields you put in each document and what data types you store in those fields. Documents within the same collection can all contain different fields or store different types of data in those fields. However, it's a good idea to use the same fields and data types across multiple documents, so that you can query the documents more easily.

A collection contains documents and nothing else. It can't directly contain raw fields with values, and it can't contain other collections. (See[Hierarchical Data](https://firebase.google.com/docs/firestore/data-model#hierarchical-data)for an explanation of how to structure more complex data inCloud Firestore.)

The names of documents within a collection are unique. You can provide your own keys, such as user IDs, or you can letCloud Firestorecreate random IDs for you automatically.

You do not need to "create" or "delete" collections. After you create the first document in a collection, the collection exists. If you delete all of the documents in a collection, it no longer exists.

## References

Every document inCloud Firestoreis uniquely identified by its location within the database. The previous example showed a document`alovelace`within the collection`users`. To refer to this location in your code, you can create a*reference*to it.  

### Web

```javascript
import { doc } from "firebase/firestore";

const alovelaceDocumentRef = doc(db, 'users', 'alovelace');https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/doc_reference.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var alovelaceDocumentRef = db.collection('users').doc('alovelace');https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L195-L195
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let alovelaceDocumentRef = db.collection("users").document("alovelace")https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L241-L241
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *alovelaceDocumentRef =
    [[self.db collectionWithPath:@"users"] documentWithPath:@"alovelace"];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L170-L171
```

### Kotlin

```kotlin
val alovelaceDocumentRef = db.collection("users").document("alovelace")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L214-L214
```

### Java

```java
DocumentReference alovelaceDocumentRef = db.collection("users").document("alovelace");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L260-L260
```

### Dart

```dart
final alovelaceDocumentRef = db.collection("users").doc("alovelace");https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L85-L85
```

##### Java

    // Reference to a document with id "alovelace" in the collection "users"
    DocumentReference document = db.collection("users").document("alovelace");  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L52-L53

##### Python

    a_lovelace_ref = db.collection("users").document("alovelace")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L280-L280

### Python

    a_lovelace_ref = db.collection("users").document("alovelace")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L275-L275

##### C++

```c++
DocumentReference alovelace_document_reference =
    db->Collection("users").Document("alovelace");https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L45-L46
```

##### Node.js

    const alovelaceDocumentRef = db.collection('users').doc('alovelace');  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L132-L132

##### Go


    import (
    	"cloud.google.com/go/firestore"
    )

    func createDocReference(client *firestore.Client) {

    	alovelaceRef := client.Collection("users").Doc("alovelace")

    	_ = alovelaceRef
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/retrieve_data_reference_document.go#L18-L29

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $document = $db->collection('samples/php/users')->document('alovelace');  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_reference_document.php#L40-L40

##### Unity

```c#
DocumentReference documentRef = db.Collection("users").Document("alovelace");
```

##### C#

### C#

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    DocumentReference documentRef = db.Collection("users").Document("alovelace");  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/DataModel/Program.cs#L42-L42

##### Ruby

    document_ref = firestore.col("users").doc("alovelace")  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/data_model.rb#L22-L22

A reference is a lightweight object that just points to a location in your database. You can create a reference whether or not data exists there, and creating a reference does not perform any network operations.

You can also create references to*collections*:  

### Web

```javascript
import { collection } from "firebase/firestore";

const usersCollectionRef = collection(db, 'users');https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/collection_reference.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var usersCollectionRef = db.collection('users');https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L201-L201
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let usersCollectionRef = db.collection("users")https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L246-L246
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRCollectionReference *usersCollectionRef = [self.db collectionWithPath:@"users"];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L175-L175
```

### Kotlin

```kotlin
val usersCollectionRef = db.collection("users")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L220-L220
```

### Java

```java
CollectionReference usersCollectionRef = db.collection("users");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L266-L266
```

### Dart

```dart
final usersCollectionRef = db.collection("users");https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L89-L89
```

##### Java

    // Reference to the collection "users"
    CollectionReference collection = db.collection("users");  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L39-L40

##### Python

    users_ref = db.collection("users")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L288-L288

### Python

    users_ref = db.collection("users")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L283-L283

##### C++

```c++
CollectionReference users_collection_reference = db->Collection("users");https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L50-L50
```

##### Node.js

    const usersCollectionRef = db.collection('users');  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L136-L136

##### Go


    import (
    	"cloud.google.com/go/firestore"
    )

    func createCollectionReference(client *firestore.Client) {
    	usersRef := client.Collection("users")

    	_ = usersRef
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/retrieve_data_reference_collection.go#L18-L28

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $collection = $db->collection('samples/php/users');  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_reference_collection.php#L40-L40

##### Unity

```c#
CollectionReference collectionRef = db.Collection("users");
```

##### C#

### C#

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    CollectionReference collectionRef = db.Collection("users");  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/DataModel/Program.cs#L50-L50

##### Ruby

    collection_ref = firestore.col "users"  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/data_model.rb#L31-L31

| **Note:** *Collection references* and*document references*are two distinct types of references and let you perform different operations. For example, you could use a collection reference for querying the documents in the collection, and you could use a document reference to read or write an individual document.

For convenience, you can also create references by specifying the path to a document or collection as a string, with path components separated by a forward slash (`/`). For example, to create a reference to the`alovelace`document:  

### Web

```javascript
import { doc } from "firebase/firestore"; 

const alovelaceDocumentRef = doc(db, 'users/alovelace');https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/doc_reference_alternative.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var alovelaceDocumentRef = db.doc('users/alovelace');https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L207-L207
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let aLovelaceDocumentReference = db.document("users/alovelace")https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L258-L258
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *aLovelaceDocumentReference =
    [self.db documentWithPath:@"users/alovelace"];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L186-L187
```

### Kotlin

```kotlin
val alovelaceDocumentRef = db.document("users/alovelace")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L234-L234
```

### Java

```java
DocumentReference alovelaceDocumentRef = db.document("users/alovelace");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L280-L280
```

### Dart

```dart
final aLovelaceDocRef = db.doc("users/alovelace");https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L93-L93
```

##### Java

    // Reference to a document with id "alovelace" in the collection "users"
    DocumentReference document = db.document("users/alovelace");  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L65-L66

##### Python

    a_lovelace_ref = db.document("users/alovelace")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L296-L296

### Python

    a_lovelace_ref = db.document("users/alovelace")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L291-L291

##### C++

```c++
DocumentReference alovelace_document = db->Document("users/alovelace");https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L62-L62
```

##### Node.js

    const alovelaceDocumentRef = db.doc('users/alovelace');  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L142-L142

##### Go


    import (
    	"cloud.google.com/go/firestore"
    )

    func createDocReferenceFromString(client *firestore.Client) {
    	// Reference to a document with id "alovelace" in the collection "users"
    	alovelaceRef := client.Doc("users/alovelace")

    	_ = alovelaceRef
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/retrieve_data_reference_document_path.go#L18-L29

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $document = $db->document('users/alovelace');  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_reference_document_path.php#L40-L40

##### Unity

```c#
DocumentReference documentRef = db.Document("users/alovelace");
```

##### C#

### C#

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    DocumentReference documentRef = db.Document("users/alovelace");  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/DataModel/Program.cs#L58-L58

##### Ruby

    document_path_ref = firestore.doc "users/alovelace"  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/data_model.rb#L40-L40

## Hierarchical Data

To understand how hierarchical data structures work inCloud Firestore, consider an example chat app with messages and chat rooms.

You can create a collection called`rooms`to store different chat rooms:

- collections_bookmarkrooms

  - classroomA

    `name : "my chat room"`  
  - classroomB

    `...`  

Now that you have chat rooms, decide how to store your messages. You might not want to store them in the chat room's document. Documents inCloud Firestoreshould be lightweight, and a chat room could contain a large number of messages. However, you can create additional collections within your chat room's document, as subcollections.

### Subcollections

The best way to store messages in this scenario is by using subcollections. A subcollection is a collection associated with a specific document.
| **Note:** You can query across subcollections with the same collection ID by using[Collection Group Queries](https://firebase.google.com/docs/firestore/query-data/queries#collection-group-query).

You can create a subcollection called`messages`for every room document in your`rooms`collection:

- collections_bookmarkrooms

  - classroomA

    `name : "my chat room"`  
    - collections_bookmarkmessages

      - classmessage1

        `from : "alex"`  
        `msg : "Hello World!"`  
      - classmessage2

        `...`  
  - classroomB

    `...`  

In this example, you would create a reference to a message in the subcollection with the following code:  

### Web

```javascript
import { doc } from "firebase/firestore"; 

const messageRef = doc(db, "rooms", "roomA", "messages", "message1");https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/subcollection_reference.js#L8-L10
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
var messageRef = db.collection('rooms').doc('roomA')
                .collection('messages').doc('message1');https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L213-L214
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let messageRef = db
  .collection("rooms").document("roomA")
  .collection("messages").document("message1")https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L251-L253
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *messageRef =
    [[[[self.db collectionWithPath:@"rooms"] documentWithPath:@"roomA"]
    collectionWithPath:@"messages"] documentWithPath:@"message1"];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L179-L181
```

### Kotlin

```kotlin
val messageRef = db
    .collection("rooms").document("roomA")
    .collection("messages").document("message1")https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L226-L228
```

### Java

```java
DocumentReference messageRef = db
        .collection("rooms").document("roomA")
        .collection("messages").document("message1");https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L272-L274
```

### Dart

```dart
final messageRef = db
    .collection("rooms")
    .doc("roomA")
    .collection("messages")
    .doc("message1");https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L99-L103
```

##### Java

    // Reference to a document in subcollection "messages"
    DocumentReference document =
        db.collection("rooms").document("roomA").collection("messages").document("message1");  
    https://github.com/googleapis/java-firestore/blob/926fd8c393dfd91f532b61bdf2a50ed8d19d3618/samples/snippets/src/main/java/com/example/firestore/snippets/References.java#L78-L80

##### Python

    room_a_ref = db.collection("rooms").document("roomA")
    message_ref = room_a_ref.collection("messages").document("message1")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-client/snippets.py#L305-L306

### Python

    room_a_ref = db.collection("rooms").document("roomA")
    message_ref = room_a_ref.collection("messages").document("message1")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/1af32d126393c2c1b2500ad4c1a91ad6614d92d4/firestore/cloud-async-client/snippets.py#L300-L301

##### C++

```c++
DocumentReference message_reference = db->Collection("rooms")
    .Document("roomA")
    .Collection("messages")
    .Document("message1");https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L55-L58
```

##### Node.js

    const messageRef = db.collection('rooms').doc('roomA')
      .collection('messages').doc('message1');  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L146-L147

##### Go


    import (
    	"cloud.google.com/go/firestore"
    )

    func createSubcollectionReference(client *firestore.Client) {
    	messageRef := client.Collection("rooms").Doc("roomA").
    		Collection("messages").Doc("message1")

    	_ = messageRef
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/56b9c2b7156433d269f03f82a8df2ca9227f6a88/firestore/retrieve_data_reference_subcollection.go#L18-L29

##### PHP

### PHP

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    $document = $db
        ->collection('rooms')
        ->document('roomA')
        ->collection('messages')
        ->document('message1');  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_reference_subcollection.php#L40-L44

##### Unity

```c#
DocumentReference documentRef = db
	.Collection("Rooms").Document("RoomA")
	.Collection("Messages").Document("Message1");
```

##### C#

### C#

For more on installing and creating aCloud Firestoreclient, refer to[Cloud FirestoreClient Libraries](https://firebase.google.com/firestore/docs/reference/libraries).  

    DocumentReference documentRef = db
        .Collection("Rooms").Document("RoomA")
        .Collection("Messages").Document("Message1");  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/DataModel/Program.cs#L66-L68

##### Ruby

    message_ref = firestore.col("rooms").doc("roomA").col("messages").doc("message1")  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/data_model.rb#L49-L49

Notice the alternating pattern of collections and documents. Your collections and documents must always follow this pattern. You cannot reference a collection in a collection or a document in a document.

Subcollections allow you to structure data hierarchically, making data easier to access. To get all messages in`roomA`, you can create a collection reference to the subcollection`messages`and interact with it like you would any other collection reference.

Documents in subcollections can contain subcollections as well, allowing you to further nest data. You can nest data up to 100 levels deep.
| **Warning:** Deleting a document does not delete its subcollections!  
|
| When you delete a document that has subcollections, those subcollections are not deleted. For example, there may be a document located at`coll/doc/subcoll/subdoc`even though the document`coll/doc`no longer exists. If you want to delete documents in subcollections when deleting a parent document, you must do so manually, as shown in[Delete Collections](https://firebase.google.com/docs/firestore/manage-data/delete-data#collections).