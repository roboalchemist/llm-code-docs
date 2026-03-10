# Source: https://firebase.google.com/docs/firestore/enterprise/delete-data-native.md.txt

<br />

The following examples demonstrate how to delete documents, fields, and
collections.

## Delete documents

To delete a document, use the following language-specific `delete()` methods:

### Web

Use the `deleteDoc()` method:

```javascript
import { doc, deleteDoc } from "firebase/firestore";

await deleteDoc(doc(db, "cities", "DC"));
```

### Web

Use the `delete()` method:

```javascript
db.collection("cities").doc("DC").delete().then(() => {
    console.log("Document successfully deleted!");
}).catch((error) => {
    console.error("Error removing document: ", error);
});
```

##### Swift

Use the `delete()` method:
**Note:** This product is not available on watchOS and App Clip targets.

```swift
do {
  try await db.collection("cities").document("DC").delete()
  print("Document successfully removed!")
} catch {
  print("Error removing document: \(error)")
}
```

##### Objective-C

Use the `deleteDocumentWithCompletion:` method:
**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
[[[self.db collectionWithPath:@"cities"] documentWithPath:@"DC"]
    deleteDocumentWithCompletion:^(NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error removing document: %@", error);
      } else {
        NSLog(@"Document successfully removed!");
      }
}];
```

### Kotlin

Use the `delete()` method:

```kotlin
db.collection("cities").document("DC")
    .delete()
    .addOnSuccessListener { Log.d(TAG, "DocumentSnapshot successfully deleted!") }
    .addOnFailureListener { e -> Log.w(TAG, "Error deleting document", e) }
```

### Java

Use the `delete()` method:

```java
db.collection("cities").document("DC")
        .delete()
        .addOnSuccessListener(new OnSuccessListener<Void>() {
            @Override
            public void onSuccess(Void aVoid) {
                Log.d(TAG, "DocumentSnapshot successfully deleted!");
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Log.w(TAG, "Error deleting document", e);
            }
        });
```

### Dart

Use the `delete()` method:

```dart
db.collection("cities").doc("DC").delete().then(
      (doc) => print("Document deleted"),
      onError: (e) => print("Error updating document $e"),
    );
```

##### Java

Use the `delete()` method:

    // asynchronously delete a document
    ApiFuture<WriteResult> writeResult = db.collection("cities").document("DC").delete();
    // ...
    System.out.println("Update time : " + writeResult.get().getUpdateTime());https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L299-L302

##### Python

Use the `delete()` method:

    db.collection("cities").document("DC").delete()https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L826-L826

### Python

Use the `delete()` method:

    await db.collection("cities").document("DC").delete()https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L680-L680

##### C++

Use the `Delete()` method:

```c++
db->Collection("cities").Document("DC").Delete().OnCompletion(
    [](const Future<void>& future) {
      if (future.error() == Error::kErrorOk) {
        std::cout << "DocumentSnapshot successfully deleted!" << std::endl;
      } else {
        std::cout << "Error deleting document: " << future.error_message()
                  << std::endl;
      }
    });
```

##### Node.js

Use the `delete()` method:

    const res = await db.collection('cities').doc('DC').delete();https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L362-L362

##### Go

Use the `Delete()` method:


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func deleteDoc(ctx context.Context, client *firestore.Client) error {
    	_, err := client.Collection("cities").Doc("DC").Delete(ctx)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }
    https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/save_data_delete_doc.go#L18-L35

##### PHP

Use the `delete()` method:

    $db->collection('samples/php/cities')->document('DC')->delete();https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/data_delete_doc.php#L40-L40

##### Unity

Use the `DeleteAsync()` method:

```c#
DocumentReference cityRef = db.Collection("cities").Document("DC");
cityRef.DeleteAsync();
```

##### C#

Use the `DeleteAsync()` method:

    DocumentReference cityRef = db.Collection("cities").Document("DC");
    await cityRef.DeleteAsync();https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/DeleteData/Program.cs#L38-L39

##### Ruby

Use the `delete()` method:

    city_ref = firestore.doc "#{collection_path}/DC"
    city_ref.deletehttps://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/delete_data.rb#L24-L25

> [!WARNING]
> **Warning:** Deleting a document does not delete its subcollections!

When you delete a document, Cloud Firestore does not automatically
delete the documents within its
subcollections. You can still access the subcollection documents by reference.
For example, you can access the document at path
`/mycoll/mydoc/mysubcoll/mysubdoc` even
if you delete the parent document at `/mycoll/mydoc`.

Non-existent parent documents [appear in the console](https://firebase.google.com/docs/firestore/using-console#non-existent-parent-documents),
but they don't appear in query results and snapshots.

If you want to delete a document and all the documents within its
subcollections, you must do so manually. For more information, see
[Delete Collections](https://firebase.google.com/docs/firestore/enterprise/delete-data-native#collections).

## Delete fields

To delete specific fields from a document, use the following language-specific `FieldValue.delete()` methods
when you update a document:

### Web

Use the `deleteField()` method:

```javascript
import { doc, updateDoc, deleteField } from "firebase/firestore";

const cityRef = doc(db, 'cities', 'BJ');

// Remove the 'capital' field from the document
await updateDoc(cityRef, {
    capital: deleteField()
});
```

### Web

Use the `FieldValue.delete()` method:

```javascript
var cityRef = db.collection('cities').doc('BJ');

// Remove the 'capital' field from the document
var removeCapital = cityRef.update({
    capital: firebase.firestore.FieldValue.delete()
});
```

##### Swift

Use the `FieldValue.delete()` method:
**Note:** This product is not available on watchOS and App Clip targets.

```swift
do {

  try await db.collection("cities").document("BJ").updateData([
    "capital": FieldValue.delete(),
  ])
  print("Document successfully updated")
} catch {
  print("Error updating document: \(error)")
}
```

##### Objective-C

Use the `fieldValueForDelete:` method:
**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
[[[self.db collectionWithPath:@"cities"] documentWithPath:@"BJ"] updateData:@{
  @"capital": [FIRFieldValue fieldValueForDelete]
} completion:^(NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"Error updating document: %@", error);
  } else {
    NSLog(@"Document successfully updated");
  }
}];
```

### Kotlin

Use the `FieldValue.delete()` method:

```kotlin
val docRef = db.collection("cities").document("BJ")

// Remove the 'capital' field from the document
val updates = hashMapOf<String, Any>(
    "capital" to FieldValue.delete(),
)

docRef.update(updates).addOnCompleteListener { }
```

### Java

Use the `FieldValue.delete()` method:

```java
DocumentReference docRef = db.collection("cities").document("BJ");

// Remove the 'capital' field from the document
Map<String,Object> updates = new HashMap<>();
updates.put("capital", FieldValue.delete());

docRef.update(updates).addOnCompleteListener(new OnCompleteListener<Void>() {
    // ...
    // ...https://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1321-L1332
```

### Dart

Use the `FieldValue.delete()` method:

```dart
final docRef = db.collection("cities").doc("BJ");

// Remove the 'capital' field from the document
final updates = <String, dynamic>{
  "capital": FieldValue.delete(),
};

docRef.update(updates);
```

##### Java

Use the `FieldValue.delete()` method:

    DocumentReference docRef = db.collection("cities").document("BJ");
    Map<String, Object> updates = new HashMap<>();
    updates.put("capital", FieldValue.delete());
    // Update and delete the "capital" field in the document
    ApiFuture<WriteResult> writeResult = docRef.update(updates);
    System.out.println("Update time : " + writeResult.get());https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L286-L291

##### Python

Use the `firestore.DELETE_FIELD` method:

    city_ref = db.collection("cities").document("BJ")
    city_ref.update({"capital": firestore.DELETE_FIELD})https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L833-L834

### Python

Use the `firestore.DELETE_FIELD` method:

    city_ref = db.collection("cities").document("BJ")
    await city_ref.update({"capital": firestore.DELETE_FIELD})https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L687-L688

##### C++

Use the `FieldValue::Delete()` method:

```c++
DocumentReference doc_ref = db->Collection("cities").Document("BJ");
doc_ref.Update({{"capital", FieldValue::Delete()}})
    .OnCompletion([](const Future<void>& future) { /*...*/ });
```

##### Node.js

Use the `FieldValue.delete()` method:

    // Create a document reference
    const cityRef = db.collection('cities').doc('BJ');

    // Remove the 'capital' field from the document
    const res = await cityRef.update({
      capital: FieldValue.delete()
    });https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L324-L330

##### Go

Use the `firestore.Delete` method:


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func deleteField(ctx context.Context, client *firestore.Client) error {
    	_, err := client.Collection("cities").Doc("BJ").Update(ctx, []firestore.Update{
    		{
    			Path:  "capital",
    			Value: firestore.Delete,
    		},
    	})
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	// ...
    	return err
    }
    https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/save_data_delete_field.go#L18-L47

##### PHP

Use the `FieldValue::deleteField()` method:

    $cityRef = $db->collection('samples/php/cities')->document('BJ');
    $cityRef->update([
        ['path' => 'capital', 'value' => FieldValue::deleteField()]
    ]);https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/data_delete_field.php#L41-L44

##### Unity

Use the `FieldValue.Delete` method:

```c#
DocumentReference cityRef = db.Collection("cities").Document("BJ");
Dictionary<string, object> updates = new Dictionary<string, object>
{
    { "Capital", FieldValue.Delete }
};
```

##### C#

Use the `FieldValue.Delete` method:

    DocumentReference cityRef = db.Collection("cities").Document("BJ");
    Dictionary<string, object> updates = new Dictionary<string, object>
    {
        { "Capital", FieldValue.Delete }
    };
    await cityRef.UpdateAsync(updates);https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/DeleteData/Program.cs#L48-L53

##### Ruby

Use the `firestore.field_delete` method:

    city_ref = firestore.doc "#{collection_path}/BJ"
    city_ref.update({ capital: firestore.field_delete })https://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/delete_data.rb#L36-L37

## Delete collections

To delete an entire collection or subcollection in Cloud Firestore,
retrieve (read) all the documents within the collection or subcollection and delete
them. This process incurs both read and delete costs. If you have larger
collections, you may want to delete the documents in smaller batches to avoid
out-of-memory errors. Repeat the process until you've deleted the entire
collection or subcollection.

Deleting a collection requires coordinating an unbounded number of
individual delete requests. If you need to delete entire collections, do so only
from a trusted server environment. While it is possible to delete a collection
from a mobile/web client, doing so has negative security and performance implications.

The following snippets are simplified for clarity and don't include error
handling, security, deleting subcollections, or performance optimizations. To learn more
about one recommended approach to deleting collections in production, see
[Deleting Collections and Subcollections](https://firebase.google.com/docs/firestore/solutions/delete-collections).

##### Web

```
// Deleting collections from a Web client is not recommended.
```

##### Swift

**Note:** This product is not available on watchOS and App Clip targets.

```swift
// Deleting collections from an Apple client is not recommended.
```

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets.

```objective-c
// Deleting collections from an Apple client is not recommended.
  
```

### Kotlin

```kotlin
// Deleting collections from an Android client is not recommended.
```

### Java

```java
// Deleting collections from an Android client is not recommended.
```

### Dart

Deleting collections from the client is not recommended.

##### Java

    /**
     * Delete a collection in batches to avoid out-of-memory errors. Batch size may be tuned based on
     * document size (atmost 1MB) and application requirements.
     */
    void deleteCollection(CollectionReference collection, int batchSize) {
      try {
        // retrieve a small batch of documents to avoid out-of-memory errors
        ApiFuture<QuerySnapshot> future = collection.limit(batchSize).get();
        int deleted = 0;
        // future.get() blocks on document retrieval
        List<QueryDocumentSnapshot> documents = future.get().getDocuments();
        for (QueryDocumentSnapshot document : documents) {
          document.getReference().delete();
          ++deleted;
        }
        if (deleted >= batchSize) {
          // retrieve and delete another batch
          deleteCollection(collection, batchSize);
        }
      } catch (Exception e) {
        System.err.println("Error deleting collection : " + e.getMessage());
      }
    }
    https://github.com/googleapis/java-firestore/blob/2be59896fef7a7bb458cfaf06344654e82acc74c/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L307-L330

##### Python

    def delete_collection(coll_ref):

        print(f"Recursively deleting collection: {coll_ref}")
        db.recursive_delete(coll_ref)
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-client/snippets.py#L842-L846

### Python

    async def delete_collection(coll_ref):

        await db.recursive_delete(coll_ref)
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/7d099b48020d1d4ed32e9dea0b65df3abb51f4cb/firestore/cloud-async-client/snippets.py#L696-L699

##### C++

```c++
// This is not supported. Delete data using CLI as discussed below.
  
```

##### Node.js

    async function deleteCollection(db, collectionPath) {
      const collectionRef = db.collection(collectionPath);
      return await db.recursiveDelete(collectionRef);
    }
    https://github.com/firebase/snippets-node/blob/92a575a9eb70b9193aac4d63954e7647cf50fd8f/firestore/main/index.js#L950-L954

##### Go


    import (
    	"context"
    	"fmt"
    	"io"

    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )

    func deleteCollection(w io.Writer, projectID, collectionName string,
    	batchSize int) error {

    	// Instantiate a client
    	ctx := context.Background()
    	client, err := firestore.NewClient(ctx, projectID)
    	if err != nil {
    		return err
    	}

    	col := client.Collection(collectionName)
    	bulkwriter := client.BulkWriter(ctx)

    	for {
    		// Get a batch of documents
    		iter := col.Limit(batchSize).Documents(ctx)
    		numDeleted := 0

    		// Iterate through the documents, adding
    		// a delete operation for each one to the BulkWriter.
    		for {
    			doc, err := iter.Next()
    			if err == iterator.Done {
    				break
    			}
    			if err != nil {
    				return err
    			}

    			bulkwriter.Delete(doc.Ref)
    			numDeleted++
    		}

    		// If there are no documents to delete,
    		// the process is over.
    		if numDeleted == 0 {
    			bulkwriter.End()
    			break
    		}

    		bulkwriter.Flush()
    	}
    	fmt.Fprintf(w, "Deleted collection \"%s\"", collectionName)
    	return nil
    }
    https://github.com/GoogleCloudPlatform/golang-samples/blob/323d864f13303fca135899042d1ecce6efd62722/firestore/save_data_delete_collection.go#L18-L73

##### PHP

    function data_delete_collection(string $projectId, string $collectionName, int $batchSize)
    {
        // Create the Cloud Firestore client
        $db = new FirestoreClient([
            'projectId' => $projectId,
        ]);
        $collectionReference = $db->collection($collectionName);
        $documents = $collectionReference->limit($batchSize)->documents();
        while (!$documents->isEmpty()) {
            foreach ($documents as $document) {
                printf('Deleting document %s' . PHP_EOL, $document->id());
                $document->reference()->delete();
            }
            $documents = $collectionReference->limit($batchSize)->documents();
        }
    }https://github.com/GoogleCloudPlatform/php-docs-samples/blob/57f7e42e9df09d95da84f23fe6688f51ab8aa0ef/firestore/src/data_delete_collection.php#L36-L51

##### Unity

```c#
// This is not supported. Delete data using CLI as discussed below.
```

##### C#

    private static async Task DeleteCollection(CollectionReference collectionReference, int batchSize)
    {
        QuerySnapshot snapshot = await collectionReference.Limit(batchSize).GetSnapshotAsync();
        IReadOnlyList<DocumentSnapshot> documents = snapshot.Documents;
        while (documents.Count > 0)
        {
            foreach (DocumentSnapshot document in documents)
            {
                Console.WriteLine("Deleting document {0}", document.Id);
                await document.Reference.DeleteAsync();
            }
            snapshot = await collectionReference.Limit(batchSize).GetSnapshotAsync();
            documents = snapshot.Documents;
        }
        Console.WriteLine("Finished deleting all documents from the collection.");
    }https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/f0105e127957cddda7c57872b3c2b9a405b0a97d/firestore/api/DeleteData/Program.cs#L59-L74

##### Ruby

    cities_ref = firestore.col collection_path
    query      = cities_ref

    query.get do |document_snapshot|
      puts "Deleting document #{document_snapshot.document_id}."
      document_ref = document_snapshot.ref
      document_ref.delete
    endhttps://github.com/googleapis/google-cloud-ruby/blob/56f30b3c8e79535bd66d78b7e43b0174b728d3f0/google-cloud-firestore/samples/delete_data.rb#L48-L55

## Delete data with TTL policies

A TTL policy designates a given field as the expiration time for documents in a
given collection group. TTL delete operations count towards your document delete
costs.

For information about setting TTL, see [Manage data retention with TTL policies](https://firebase.google.com/docs/firestore/ttl).

## Bulk deletion jobs

Cloud Firestore supports several tools for bulk deletion. You should
select a tool based on the number of documents you need to delete and the
level of configurability you need.

> [!NOTE]
> **Note:** Deleting a large number of documents [can impact latency](https://firebase.google.com/docs/firestore/best-practices#avoid-skipping). If latency is caused by too many recent deletes, the issue should automatically resolve after some time. If the issue does not resolve, [contact support](https://firebase.google.com/support).

For smaller jobs
of thousands of documents, use the console or the Firebase CLI. For larger
jobs, these tools might start to timeout and require you to run the tool multiple
times.

### Console

You can [delete documents and collections from the
Cloud Firestore page in the console](https://firebase.google.com/docs/firestore/using-console#delete_data). Deleting a document from the
console deletes all of the nested data in that document, including any
subcollections.

### Firebase CLI

You can also use the [Firebase CLI](https://firebase.google.com/docs/cli)
to delete documents and collections. Use the following command to delete
data:

> [!NOTE]
> **Note:** Deleting data with the Firebase CLI incurs read and delete costs. For more information, see [Pricing](https://firebase.google.com/docs/firestore/pricing#pricing_by_location).

    firebase firestore:delete  --database=DATABASE_ID PATH

Replace <var translate="no">DATABASE_ID</var> with your database ID and <var translate="no">PATH</var> with a path to a document or collection.

For large deletion jobs (millions of documents), use one of the following:

### Managed bulk delete


Cloud Firestore supports bulk deleting one or more collection groups.
For more information, see [Bulk delete data](https://firebase.google.com/docs/firestore/manage-data/bulk-delete).

### Dataflow connector


You can use [Dataflow](https://cloud.google.com/dataflow/docs/overview)
for bulk operations on your database. This option is the most configurable,
but also requires more set up than other bulk delete options.
See the Cloud Firestore connector for
Dataflow introduction
[blog post](https://cloud.google.com/blog/topics/developers-practitioners/using-firestore-and-apache-beam-data-processing)
has an example of deleting all documents in a collection group.