# Source: https://firebase.google.com/docs/firestore/manage-data/transactions.md.txt

<br />

Cloud Firestoresupports atomic operations for reading and writing data. In a set of atomic operations, either all of the operations succeed, or none of them are applied. There are two types of atomic operations inCloud Firestore:

- **Transactions** : a[transaction](https://firebase.google.com/docs/firestore/manage-data/transactions#transactions)is a set of read and write operations on one or more documents.
- **Batched Writes** : a[batched write](https://firebase.google.com/docs/firestore/manage-data/transactions#batched-writes)is a set of write operations on one or more documents.

## Updating data with transactions

Using theCloud Firestoreclient libraries, you can group multiple operations into a single transaction. Transactions are useful when you want to update a field's value based on its current value, or the value of some other field.

A transaction consists of any number of`get()`operations followed by any number of write operations such as`set()`,`update()`, or`delete()`. In the case of a concurrent edit,Cloud Firestoreruns the entire transaction again. For example, if a transaction reads documents and another client modifies any of those documents,Cloud Firestoreretries the transaction. This feature ensures that the transaction runs on up-to-date and consistent data.

Transactions never partially apply writes. All writes execute at the end of a successful transaction.

When using transactions, note that:

- Read operations must be executed before write operations.
- A function calling a transaction (transaction function) might run more than once if a concurrent edit affects a document that the transaction reads.
- Transaction functions should not directly modify application state.
- Transactions will fail when the client is offline.

The following example shows how to create and run a transaction:  

### Web

```javascript
import { runTransaction } from "firebase/firestore";

try {
  await runTransaction(db, async (transaction) => {
    const sfDoc = await transaction.get(sfDocRef);
    if (!sfDoc.exists()) {
      throw "Document does not exist!";
    }

    const newPopulation = sfDoc.data().population + 1;
    transaction.update(sfDocRef, { population: newPopulation });
  });
  console.log("Transaction successfully committed!");
} catch (e) {
  console.log("Transaction failed: ", e);
}https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/transaction.js#L8-L23
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
// Create a reference to the SF doc.
var sfDocRef = db.collection("cities").doc("SF");

// Uncomment to initialize the doc.
// sfDocRef.set({ population: 0 });

return db.runTransaction((transaction) => {
    // This code may get re-run multiple times if there are conflicts.
    return transaction.get(sfDocRef).then((sfDoc) => {
        if (!sfDoc.exists) {
            throw "Document does not exist!";
        }

        // Add one person to the city population.
        // Note: this could be done without a transaction
        //       by updating the population using FieldValue.increment()
        var newPopulation = sfDoc.data().population + 1;
        transaction.update(sfDocRef, { population: newPopulation });
    });
}).then(() => {
    console.log("Transaction successfully committed!");
}).catch((error) => {
    console.log("Transaction failed: ", error);
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L525-L548
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let sfReference = db.collection("cities").document("SF")

do {
  let _ = try await db.runTransaction({ (transaction, errorPointer) -> Any? in
    let sfDocument: DocumentSnapshot
    do {
      try sfDocument = transaction.getDocument(sfReference)
    } catch let fetchError as NSError {
      errorPointer?.pointee = fetchError
      return nil
    }

    guard let oldPopulation = sfDocument.data()?["population"] as? Int else {
      let error = NSError(
        domain: "AppErrorDomain",
        code: -1,
        userInfo: [
          NSLocalizedDescriptionKey: "Unable to retrieve population from snapshot \(sfDocument)"
        ]
      )
      errorPointer?.pointee = error
      return nil
    }

    // Note: this could be done without a transaction
    //       by updating the population using FieldValue.increment()
    transaction.updateData(["population": oldPopulation + 1], forDocument: sfReference)
    return nil
  })
  print("Transaction successfully committed!")
} catch {
  print("Transaction failed: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L524-L556
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *sfReference =
    [[self.db collectionWithPath:@"cities"] documentWithPath:@"SF"];
[self.db runTransactionWithBlock:^id (FIRTransaction *transaction, NSError **errorPointer) {
  FIRDocumentSnapshot *sfDocument = [transaction getDocument:sfReference error:errorPointer];
  if (*errorPointer != nil) { return nil; }

  if (![sfDocument.data[@"population"] isKindOfClass:[NSNumber class]]) {
    *errorPointer = [NSError errorWithDomain:@"AppErrorDomain" code:-1 userInfo:@{
      NSLocalizedDescriptionKey: @"Unable to retreive population from snapshot"
    }];
    return nil;
  }
  NSInteger oldPopulation = [sfDocument.data[@"population"] integerValue];

  // Note: this could be done without a transaction
  //       by updating the population using FieldValue.increment()
  [transaction updateData:@{ @"population": @(oldPopulation + 1) } forDocument:sfReference];

  return nil;
} completion:^(id result, NSError *error) {
  if (error != nil) {
    NSLog(@"Transaction failed: %@", error);
  } else {
    NSLog(@"Transaction successfully committed!");
  }
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L463-L488
```

### Kotlin

```kotlin
val sfDocRef = db.collection("cities").document("SF")

db.runTransaction { transaction ->
    val snapshot = transaction.get(sfDocRef)

    // Note: this could be done without a transaction
    //       by updating the population using FieldValue.increment()
    val newPopulation = snapshot.getDouble("population")!! + 1
    transaction.update(sfDocRef, "population", newPopulation)

    // Success
    null
}.addOnSuccessListener { Log.d(TAG, "Transaction success!") }
    .addOnFailureListener { e -> Log.w(TAG, "Transaction failure.", e) }https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L414-L427
```

### Java

```java
final DocumentReference sfDocRef = db.collection("cities").document("SF");

db.runTransaction(new Transaction.Function<Void>() {
    @Override
    public Void apply(@NonNull Transaction transaction) throws FirebaseFirestoreException {
        DocumentSnapshot snapshot = transaction.get(sfDocRef);

        // Note: this could be done without a transaction
        //       by updating the population using FieldValue.increment()
        double newPopulation = snapshot.getDouble("population") + 1;
        transaction.update(sfDocRef, "population", newPopulation);

        // Success
        return null;
    }
}).addOnSuccessListener(new OnSuccessListener<Void>() {
    @Override
    public void onSuccess(Void aVoid) {
        Log.d(TAG, "Transaction success!");
    }
})
.addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception e) {
        Log.w(TAG, "Transaction failure.", e);
    }
});https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L534-L560
```

### Dart

```dart
final sfDocRef = db.collection("cities").doc("SF");
db.runTransaction((transaction) async {
  final snapshot = await transaction.get(sfDocRef);
  // Note: this could be done without a transaction
  //       by updating the population using FieldValue.increment()
  final newPopulation = snapshot.get("population") + 1;
  transaction.update(sfDocRef, {"population": newPopulation});
}).then(
  (value) => print("DocumentSnapshot successfully updated!"),
  onError: (e) => print("Error updating document $e"),
);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L297-L307
```

##### Java

    // Initialize doc
    final DocumentReference docRef = db.collection("cities").document("SF");
    City city = new City("SF");
    city.setCountry("USA");
    city.setPopulation(860000L);
    docRef.set(city).get();

    // run an asynchronous transaction
    ApiFuture<Void> futureTransaction =
        db.runTransaction(
            transaction -> {
              // retrieve document and increment population field
              DocumentSnapshot snapshot = transaction.get(docRef).get();
              long oldPopulation = snapshot.getLong("population");
              transaction.update(docRef, "population", oldPopulation + 1);
              return null;
            });
    // block on transaction operation using transaction.get()  
    https://github.com/googleapis/java-firestore/blob/5ade48a0b3197378ea62ddf24c6743bf2530bd75/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L340-L357

##### Python

    transaction = db.transaction()
    city_ref = db.collection("cities").document("SF")

    @firestore.transactional
    def update_in_transaction(transaction, city_ref):
        snapshot = city_ref.get(transaction=transaction)
        transaction.update(city_ref, {"population": snapshot.get("population") + 1})

    update_in_transaction(transaction, city_ref)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/420b4003c11686f07de626c03f710d9b10b1160b/firestore/cloud-client/snippets.py#L395-L403

### Python

    transaction = db.transaction()
    city_ref = db.collection("cities").document("SF")

    @firestore.async_transactional
    async def update_in_transaction(transaction, city_ref):
        snapshot = await city_ref.get(transaction=transaction)
        transaction.update(city_ref, {"population": snapshot.get("population") + 1})

    await update_in_transaction(transaction, city_ref)  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/420b4003c11686f07de626c03f710d9b10b1160b/firestore/cloud-async-client/snippets.py#L389-L397

##### C++

```c++
DocumentReference sf_doc_ref = db->Collection("cities").Document("SF");
db->RunTransaction([sf_doc_ref](Transaction& transaction,
                                std::string& out_error_message) -> Error {
    Error error = Error::kErrorOk;

    DocumentSnapshot snapshot =
        transaction.Get(sf_doc_ref, &error, &out_error_message);

    // Note: this could be done without a transaction by updating the
    // population using FieldValue::Increment().
    std::int64_t new_population =
        snapshot.Get("population").integer_value() + 1;
    transaction.Update(
        sf_doc_ref,
        {{"population", FieldValue::Integer(new_population)}});

    return Error::kErrorOk;
  }).OnCompletion([](const Future<void>& future) {
  if (future.error() == Error::kErrorOk) {
    std::cout << "Transaction success!" << std::endl;
  } else {
    std::cout << "Transaction failure: " << future.error_message() << std::endl;
  }
});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L352-L375
```

##### Node.js

    // Initialize document
    const cityRef = db.collection('cities').doc('SF');
    await cityRef.set({
      name: 'San Francisco',
      state: 'CA',
      country: 'USA',
      capital: false,
      population: 860000
    });

    try {
      await db.runTransaction(async (t) => {
        const doc = await t.get(cityRef);

        // Add one person to the city population.
        // Note: this could be done without a transaction
        //       by updating the population using FieldValue.increment()
        const newPopulation = doc.data().population + 1;
        t.update(cityRef, {population: newPopulation});
      });

      console.log('Transaction success!');
    } catch (e) {
      console.log('Transaction failure:', e);
    }  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L370-L394

##### Go


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func runSimpleTransaction(ctx context.Context, client *firestore.Client) error {
    	// ...

    	ref := client.Collection("cities").Doc("SF")
    	err := client.RunTransaction(ctx, func(ctx context.Context, tx *firestore.Transaction) error {
    		doc, err := tx.Get(ref) // tx.Get, NOT ref.Get!
    		if err != nil {
    			return err
    		}
    		pop, err := doc.DataAt("population")
    		if err != nil {
    			return err
    		}
    		return tx.Set(ref, map[string]interface{}{
    			"population": pop.(int64) + 1,
    		}, firestore.MergeAll)
    	})
    	if err != nil {
    		// Handle any errors appropriately in this section.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/afaa7f40a550aee552c7b962c8a9ac3a390381ca/firestore/save_transaction_document_update.go#L18-L59

##### PHP

    $cityRef = $db->collection('samples/php/cities')->document('SF');
    $db->runTransaction(function (Transaction $transaction) use ($cityRef) {
        $snapshot = $transaction->snapshot($cityRef);
        $newPopulation = $snapshot['population'] + 1;
        $transaction->update($cityRef, [
            ['path' => 'population', 'value' => $newPopulation]
        ]);
    });  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/transaction_document_update.php#L41-L48

##### Unity

```c#
DocumentReference cityRef = db.Collection("cities").Document("SF");
db.RunTransactionAsync(transaction =>
    {
        return transaction.GetSnapshotAsync(cityRef).ContinueWith((snapshotTask) =>
        {
            DocumentSnapshot snapshot = snapshotTask.Result;
            long newPopulation = snapshot.GetValue<long>("Population") + 1;
            Dictionary<string, object> updates = new Dictionary<string, object>
            {
                { "Population", newPopulation}
            };
            transaction.Update(cityRef, updates);
        });
    });
```

##### C#

    DocumentReference cityRef = db.Collection("cities").Document("SF");
    await db.RunTransactionAsync(async transaction =>
    {
        DocumentSnapshot snapshot = await transaction.GetSnapshotAsync(cityRef);
        long newPopulation = snapshot.GetValue<long>("Population") + 1;
        Dictionary<string, object> updates = new Dictionary<string, object>
        {
            { "Population", newPopulation}
        };
        transaction.Update(cityRef, updates);
    });  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/TransactionsAndBatchedWrites/Program.cs#L38-L48

##### Ruby

    city_ref = firestore.doc "#{collection_path}/SF"

    firestore.transaction do |tx|
      new_population = tx.get(city_ref).data[:population] + 1
      puts "New population is #{new_population}."
      tx.update city_ref, { population: new_population }
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/transactions_and_batched_writes.rb#L23-L29

### Passing information out of transactions

Do not modify application state inside of your transaction functions. Doing so will introduce concurrency issues, because transaction functions can run multiple times and are not guaranteed to run on the UI thread. Instead, pass information you need out of your transaction functions. The following example builds on the previous example to show how to pass information out of a transaction:  

### Web

```javascript
import { doc, runTransaction } from "firebase/firestore";

// Create a reference to the SF doc.
const sfDocRef = doc(db, "cities", "SF");

try {
  const newPopulation = await runTransaction(db, async (transaction) => {
    const sfDoc = await transaction.get(sfDocRef);
    if (!sfDoc.exists()) {
      throw "Document does not exist!";
    }

    const newPop = sfDoc.data().population + 1;
    if (newPop <= 1000000) {
      transaction.update(sfDocRef, { population: newPop });
      return newPop;
    } else {
      return Promise.reject("Sorry! Population is too big");
    }
  });

  console.log("Population increased to ", newPopulation);
} catch (e) {
  // This will be a "population is too big" error.
  console.error(e);
}https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/transaction_promise.js#L8-L33
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
// Create a reference to the SF doc.
var sfDocRef = db.collection("cities").doc("SF");

db.runTransaction((transaction) => {
    return transaction.get(sfDocRef).then((sfDoc) => {
        if (!sfDoc.exists) {
            throw "Document does not exist!";
        }

        var newPopulation = sfDoc.data().population + 1;
        if (newPopulation <= 1000000) {
            transaction.update(sfDocRef, { population: newPopulation });
            return newPopulation;
        } else {
            return Promise.reject("Sorry! Population is too big.");
        }
    });
}).then((newPopulation) => {
    console.log("Population increased to ", newPopulation);
}).catch((err) => {
    // This will be an "population is too big" error.
    console.error(err);
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L555-L577
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
let sfReference = db.collection("cities").document("SF")

do {
  let object = try await db.runTransaction({ (transaction, errorPointer) -> Any? in
    let sfDocument: DocumentSnapshot
    do {
      try sfDocument = transaction.getDocument(sfReference)
    } catch let fetchError as NSError {
      errorPointer?.pointee = fetchError
      return nil
    }

    guard let oldPopulation = sfDocument.data()?["population"] as? Int else {
      let error = NSError(
        domain: "AppErrorDomain",
        code: -1,
        userInfo: [
          NSLocalizedDescriptionKey: "Unable to retrieve population from snapshot \(sfDocument)"
        ]
      )
      errorPointer?.pointee = error
      return nil
    }

    // Note: this could be done without a transaction
    //       by updating the population using FieldValue.increment()
    let newPopulation = oldPopulation + 1
    guard newPopulation <= 1000000 else {
      let error = NSError(
        domain: "AppErrorDomain",
        code: -2,
        userInfo: [NSLocalizedDescriptionKey: "Population \(newPopulation) too big"]
      )
      errorPointer?.pointee = error
      return nil
    }

    transaction.updateData(["population": newPopulation], forDocument: sfReference)
    return newPopulation
  })
  print("Population increased to \(object!)")
} catch {
  print("Error updating population: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L562-L605
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
FIRDocumentReference *sfReference =
[[self.db collectionWithPath:@"cities"] documentWithPath:@"SF"];
[self.db runTransactionWithBlock:^id (FIRTransaction *transaction, NSError **errorPointer) {
  FIRDocumentSnapshot *sfDocument = [transaction getDocument:sfReference error:errorPointer];
  if (*errorPointer != nil) { return nil; }

  if (![sfDocument.data[@"population"] isKindOfClass:[NSNumber class]]) {
    *errorPointer = [NSError errorWithDomain:@"AppErrorDomain" code:-1 userInfo:@{
      NSLocalizedDescriptionKey: @"Unable to retreive population from snapshot"
    }];
    return nil;
  }
  NSInteger population = [sfDocument.data[@"population"] integerValue];

  population++;
  if (population >= 1000000) {
    *errorPointer = [NSError errorWithDomain:@"AppErrorDomain" code:-2 userInfo:@{
      NSLocalizedDescriptionKey: @"Population too big"
    }];
    return @(population);
  }

  [transaction updateData:@{ @"population": @(population) } forDocument:sfReference];

  return nil;
} completion:^(id result, NSError *error) {
  if (error != nil) {
    NSLog(@"Transaction failed: %@", error);
  } else {
    NSLog(@"Population increased to %@", result);
  }
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L494-L525
```

### Kotlin

```kotlin
val sfDocRef = db.collection("cities").document("SF")

db.runTransaction { transaction ->
    val snapshot = transaction.get(sfDocRef)
    val newPopulation = snapshot.getDouble("population")!! + 1
    if (newPopulation <= 1000000) {
        transaction.update(sfDocRef, "population", newPopulation)
        newPopulation
    } else {
        throw FirebaseFirestoreException(
            "Population too high",
            FirebaseFirestoreException.Code.ABORTED,
        )
    }
}.addOnSuccessListener { result ->
    Log.d(TAG, "Transaction success: $result")
}.addOnFailureListener { e ->
    Log.w(TAG, "Transaction failure.", e)
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L433-L451
```

### Java

```java
final DocumentReference sfDocRef = db.collection("cities").document("SF");

db.runTransaction(new Transaction.Function<Double>() {
    @Override
    public Double apply(@NonNull Transaction transaction) throws FirebaseFirestoreException {
        DocumentSnapshot snapshot = transaction.get(sfDocRef);
        double newPopulation = snapshot.getDouble("population") + 1;
        if (newPopulation <= 1000000) {
            transaction.update(sfDocRef, "population", newPopulation);
            return newPopulation;
        } else {
            throw new FirebaseFirestoreException("Population too high",
                    FirebaseFirestoreException.Code.ABORTED);
        }
    }
}).addOnSuccessListener(new OnSuccessListener<Double>() {
    @Override
    public void onSuccess(Double result) {
        Log.d(TAG, "Transaction success: " + result);
    }
})
.addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception e) {
        Log.w(TAG, "Transaction failure.", e);
    }
});https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L566-L592
```

### Dart

```dart
final sfDocRef = db.collection("cities").doc("SF");
db.runTransaction((transaction) {
  return transaction.get(sfDocRef).then((sfDoc) {
    final newPopulation = sfDoc.get("population") + 1;
    transaction.update(sfDocRef, {"population": newPopulation});
    return newPopulation;
  });
}).then(
  (newPopulation) => print("Population increased to $newPopulation"),
  onError: (e) => print("Error updating document $e"),
);https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L315-L325
```

##### Java

    final DocumentReference docRef = db.collection("cities").document("SF");
    ApiFuture<String> futureTransaction =
        db.runTransaction(
            transaction -> {
              DocumentSnapshot snapshot = transaction.get(docRef).get();
              Long newPopulation = snapshot.getLong("population") + 1;
              // conditionally update based on current population
              if (newPopulation <= 1000000L) {
                transaction.update(docRef, "population", newPopulation);
                return "Population increased to " + newPopulation;
              } else {
                throw new Exception("Sorry! Population is too big.");
              }
            });
    // Print information retrieved from transaction
    System.out.println(futureTransaction.get());  
    https://github.com/googleapis/java-firestore/blob/5ade48a0b3197378ea62ddf24c6743bf2530bd75/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L373-L388

##### Python

    transaction = db.transaction()
    city_ref = db.collection("cities").document("SF")

    @firestore.transactional
    def update_in_transaction(transaction, city_ref):
        snapshot = city_ref.get(transaction=transaction)
        new_population = snapshot.get("population") + 1

        if new_population < 1000000:
            transaction.update(city_ref, {"population": new_population})
            return True
        else:
            return False

    result = update_in_transaction(transaction, city_ref)
    if result:
        print("Population updated")
    else:
        print("Sorry! Population is too big.")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/420b4003c11686f07de626c03f710d9b10b1160b/firestore/cloud-client/snippets.py#L410-L428

### Python

    transaction = db.transaction()
    city_ref = db.collection("cities").document("SF")

    @firestore.async_transactional
    async def update_in_transaction(transaction, city_ref):
        snapshot = await city_ref.get(transaction=transaction)
        new_population = snapshot.get("population") + 1

        if new_population < 1000000:
            transaction.update(city_ref, {"population": new_population})
            return True
        else:
            return False

    result = await update_in_transaction(transaction, city_ref)
    if result:
        print("Population updated")
    else:
        print("Sorry! Population is too big.")  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/420b4003c11686f07de626c03f710d9b10b1160b/firestore/cloud-async-client/snippets.py#L404-L422

##### C++

```c++
// This is not yet supported.
```

##### Node.js

    const cityRef = db.collection('cities').doc('SF');
    try {
      const res = await db.runTransaction(async t => {
        const doc = await t.get(cityRef);
        const newPopulation = doc.data().population + 1;
        if (newPopulation <= 1000000) {
          await t.update(cityRef, { population: newPopulation });
          return `Population increased to ${newPopulation}`;
        } else {
          throw 'Sorry! Population is too big.';
        }
      });
      console.log('Transaction success', res);
    } catch (e) {
      console.log('Transaction failure:', e);
    }  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L400-L415

##### Go


    import (
    	"context"
    	"errors"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func infoTransaction(ctx context.Context, client *firestore.Client) (int64, error) {
    	var updatedPop int64
    	ref := client.Collection("cities").Doc("SF")
    	err := client.RunTransaction(ctx, func(ctx context.Context, tx *firestore.Transaction) error {
    		doc, err := tx.Get(ref)
    		if err != nil {
    			return err
    		}
    		pop, err := doc.DataAt("population")
    		if err != nil {
    			return err
    		}
    		newpop := pop.(int64) + 1
    		if newpop <= 1000000 {
    			err := tx.Set(ref, map[string]interface{}{
    				"population": newpop,
    			}, firestore.MergeAll)
    			if err == nil {
    				updatedPop = newpop
    			}
    			return err
    		}
    		return errors.New("population is too big")
    	})
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}
    	return updatedPop, err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/afaa7f40a550aee552c7b962c8a9ac3a390381ca/firestore/save_transaction_document_update_conditional.go#L18-L57

##### PHP

    $cityRef = $db->collection('samples/php/cities')->document('SF');
    $transactionResult = $db->runTransaction(function (Transaction $transaction) use ($cityRef) {
        $snapshot = $transaction->snapshot($cityRef);
        $newPopulation = $snapshot['population'] + 1;
        if ($newPopulation <= 1000000) {
            $transaction->update($cityRef, [
                ['path' => 'population', 'value' => $newPopulation]
            ]);
            return true;
        } else {
            return false;
        }
    });

    if ($transactionResult) {
        printf('Population updated successfully.' . PHP_EOL);
    } else {
        printf('Sorry! Population is too big.' . PHP_EOL);
    }  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/transaction_document_update_conditional.php#L41-L59

##### Unity

```c#
DocumentReference cityRef = db.Collection("cities").Document("SF");
db.RunTransactionAsync(transaction =>
{
    return transaction.GetSnapshotAsync(cityRef).ContinueWith((task) =>
    {
        long newPopulation = task.Result.GetValue<long>("Population") + 1;
        if (newPopulation <= 1000000)
        {
            Dictionary<string, object> updates = new Dictionary<string, object>
            {
                { "Population", newPopulation}
            };
            transaction.Update(cityRef, updates);
            return true;
        }
        else
        {
            return false;
        } 
    });
}).ContinueWith((transactionResultTask) =>
{
    if (transactionResultTask.Result)
    {
        Console.WriteLine("Population updated successfully.");
    }
    else
    {
        Console.WriteLine("Sorry! Population is too big.");
    } 
});
```

##### C#

    DocumentReference cityRef = db.Collection("cities").Document("SF");
    bool transactionResult = await db.RunTransactionAsync(async transaction =>
    {
        DocumentSnapshot snapshot = await transaction.GetSnapshotAsync(cityRef);
        long newPopulation = snapshot.GetValue<long>("Population") + 1;
        if (newPopulation <= 1000000)
        {
            Dictionary<string, object> updates = new Dictionary<string, object>
            {
                { "Population", newPopulation}
            };
            transaction.Update(cityRef, updates);
            return true;
        }
        else
        {
            return false;
        }
    });

    if (transactionResult)
    {
        Console.WriteLine("Population updated successfully.");
    }
    else
    {
        Console.WriteLine("Sorry! Population is too big.");
    }  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/TransactionsAndBatchedWrites/Program.cs#L57-L84

##### Ruby

    city_ref = firestore.doc "#{collection_path}/SF"

    updated = firestore.transaction do |tx|
      new_population = tx.get(city_ref).data[:population] + 1
      if new_population < 1_000_000
        tx.update city_ref, { population: new_population }
        true
      end
    end

    if updated
      puts "Population updated!"
    else
      puts "Sorry! Population is too big."
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/transactions_and_batched_writes.rb#L40-L54

### Transaction failure

A transaction can fail for the following reasons:

- The transaction contains read operations after write operations. Read operations must always be executed before any write operations.
- The transaction read a document that was modified outside of the transaction. In this case, the transaction automatically runs again. The transaction is retried a finite number of times.
- The transaction exceeded the maximum request size of 10 MiB.

  Transaction size depends on the sizes of documents and index entries modified by the transaction. For a delete operation, this includes the size of the target document and the sizes of the index entries deleted in response to the operation.
- The transaction exceeded the lock deadline (20 seconds).Cloud Firestoreautomatically releases locks if a transaction cannot complete in time.

- The transaction exceeds the 270-second time[limit](https://firebase.google.com/docs/firestore/quotas#writes_and_transactions)or the 60-second idle expiration time. If no activity (reads or writes) occurs within the transaction, it will time out and fail.

A failed transaction returns an error and does not write anything to the database. You do not need to roll back the transaction;Cloud Firestoredoes this automatically.

## Batched writes

If you do not need to read any documents in your operation set, you can execute multiple write operations as a single batch that contains any combination of`set()`,`update()`, or`delete()`operations. Each operation in the batch counts separately towards yourCloud Firestoreusage. A batch of writes completes atomically and can write to multiple documents. The following example shows how to build and commit a write batch:  

### Web

```javascript
import { writeBatch, doc } from "firebase/firestore"; 

// Get a new write batch
const batch = writeBatch(db);

// Set the value of 'NYC'
const nycRef = doc(db, "cities", "NYC");
batch.set(nycRef, {name: "New York City"});

// Update the population of 'SF'
const sfRef = doc(db, "cities", "SF");
batch.update(sfRef, {"population": 1000000});

// Delete the city 'LA'
const laRef = doc(db, "cities", "LA");
batch.delete(laRef);

// Commit the batch
await batch.commit();https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/firestore-next/test-firestore/write_batch.js#L8-L26
```

### Web

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular Web API and its advantages over the namespaced API.  

```javascript
// Get a new write batch
var batch = db.batch();

// Set the value of 'NYC'
var nycRef = db.collection("cities").doc("NYC");
batch.set(nycRef, {name: "New York City"});

// Update the population of 'SF'
var sfRef = db.collection("cities").doc("SF");
batch.update(sfRef, {"population": 1000000});

// Delete the city 'LA'
var laRef = db.collection("cities").doc("LA");
batch.delete(laRef);

// Commit the batch
batch.commit().then(() => {
    // ...
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/firestore/test.firestore.js#L270-L290
```

##### Swift

**Note:**This product is not available on watchOS and App Clip targets.  

```swift
// Get new write batch
let batch = db.batch()

// Set the value of 'NYC'
let nycRef = db.collection("cities").document("NYC")
batch.setData([:], forDocument: nycRef)

// Update the population of 'SF'
let sfRef = db.collection("cities").document("SF")
batch.updateData(["population": 1000000 ], forDocument: sfRef)

// Delete the city 'LA'
let laRef = db.collection("cities").document("LA")
batch.deleteDocument(laRef)

// Commit the batch
do {
  try await batch.commit()
  print("Batch write succeeded.")
} catch {
  print("Error writing batch: \(error)")
}https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/swift/firestore-smoketest/ViewController.swift#L611-L632
```

##### Objective-C

**Note:**This product is not available on watchOS and App Clip targets.  

```objective-c
// Get new write batch
FIRWriteBatch *batch = [self.db batch];

// Set the value of 'NYC'
FIRDocumentReference *nycRef =
    [[self.db collectionWithPath:@"cities"] documentWithPath:@"NYC"];
[batch setData:@{} forDocument:nycRef];

// Update the population of 'SF'
FIRDocumentReference *sfRef =
    [[self.db collectionWithPath:@"cities"] documentWithPath:@"SF"];
[batch updateData:@{ @"population": @1000000 } forDocument:sfRef];

// Delete the city 'LA'
FIRDocumentReference *laRef =
    [[self.db collectionWithPath:@"cities"] documentWithPath:@"LA"];
[batch deleteDocument:laRef];

// Commit the batch
[batch commitWithCompletion:^(NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"Error writing batch %@", error);
  } else {
    NSLog(@"Batch write succeeded.");
  }
}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firestore/objc/firestore-smoketest-objc/ViewController.m#L531-L556
```

### Kotlin

```kotlin
val nycRef = db.collection("cities").document("NYC")
val sfRef = db.collection("cities").document("SF")
val laRef = db.collection("cities").document("LA")

// Get a new write batch and commit all write operations
db.runBatch { batch ->
    // Set the value of 'NYC'
    batch.set(nycRef, City())

    // Update the population of 'SF'
    batch.update(sfRef, "population", 1000000L)

    // Delete the city 'LA'
    batch.delete(laRef)
}.addOnCompleteListener {
    // ...
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L457-L473
```

### Java

```java
// Get a new write batch
WriteBatch batch = db.batch();

// Set the value of 'NYC'
DocumentReference nycRef = db.collection("cities").document("NYC");
batch.set(nycRef, new City());

// Update the population of 'SF'
DocumentReference sfRef = db.collection("cities").document("SF");
batch.update(sfRef, "population", 1000000L);

// Delete the city 'LA'
DocumentReference laRef = db.collection("cities").document("LA");
batch.delete(laRef);

// Commit the batch
batch.commit().addOnCompleteListener(new OnCompleteListener<Void>() {
    @Override
    public void onComplete(@NonNull Task<Void> task) {
        // ...
    }
});https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L598-L619
```

### Dart

```dart
// Get a new write batch
final batch = db.batch();

// Set the value of 'NYC'
var nycRef = db.collection("cities").doc("NYC");
batch.set(nycRef, {"name": "New York City"});

// Update the population of 'SF'
var sfRef = db.collection("cities").doc("SF");
batch.update(sfRef, {"population": 1000000});

// Delete the city 'LA'
var laRef = db.collection("cities").doc("LA");
batch.delete(laRef);

// Commit the batch
batch.commit().then((_) {
  // ...
});https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L331-L349
```

##### Java

    // Get a new write batch
    WriteBatch batch = db.batch();

    // Set the value of 'NYC'
    DocumentReference nycRef = db.collection("cities").document("NYC");
    batch.set(nycRef, new City());

    // Update the population of 'SF'
    DocumentReference sfRef = db.collection("cities").document("SF");
    batch.update(sfRef, "population", 1000000L);

    // Delete the city 'LA'
    DocumentReference laRef = db.collection("cities").document("LA");
    batch.delete(laRef);

    // asynchronously commit the batch
    ApiFuture<List<WriteResult>> future = batch.commit();
    // ...
    // future.get() blocks on batch commit operation
    for (WriteResult result : future.get()) {
      System.out.println("Update time : " + result.getUpdateTime());
    }  
    https://github.com/googleapis/java-firestore/blob/5ade48a0b3197378ea62ddf24c6743bf2530bd75/samples/snippets/src/main/java/com/example/firestore/snippets/ManageDataSnippets.java#L399-L420

##### Python

    batch = db.batch()

    # Set the data for NYC
    nyc_ref = db.collection("cities").document("NYC")
    batch.set(nyc_ref, {"name": "New York City"})

    # Update the population for SF
    sf_ref = db.collection("cities").document("SF")
    batch.update(sf_ref, {"population": 1000000})

    # Delete DEN
    den_ref = db.collection("cities").document("DEN")
    batch.delete(den_ref)

    # Commit the batch
    batch.commit()  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/420b4003c11686f07de626c03f710d9b10b1160b/firestore/cloud-client/snippets.py#L435-L450

### Python

    batch = db.batch()

    # Set the data for NYC
    nyc_ref = db.collection("cities").document("NYC")
    batch.set(nyc_ref, {"name": "New York City"})

    # Update the population for SF
    sf_ref = db.collection("cities").document("SF")
    batch.update(sf_ref, {"population": 1000000})

    # Delete DEN
    den_ref = db.collection("cities").document("DEN")
    batch.delete(den_ref)

    # Commit the batch
    await batch.commit()  
    https://github.com/GoogleCloudPlatform/python-docs-samples/blob/420b4003c11686f07de626c03f710d9b10b1160b/firestore/cloud-async-client/snippets.py#L429-L444

##### C++

```c++
// Get a new write batch
WriteBatch batch = db->batch();

// Set the value of 'NYC'
DocumentReference nyc_ref = db->Collection("cities").Document("NYC");
batch.Set(nyc_ref, {});

// Update the population of 'SF'
DocumentReference sf_ref = db->Collection("cities").Document("SF");
batch.Update(sf_ref, {{"population", FieldValue::Integer(1000000)}});

// Delete the city 'LA'
DocumentReference la_ref = db->Collection("cities").Document("LA");
batch.Delete(la_ref);

// Commit the batch
batch.Commit().OnCompletion([](const Future<void>& future) {
  if (future.error() == Error::kErrorOk) {
    std::cout << "Write batch success!" << std::endl;
  } else {
    std::cout << "Write batch failure: " << future.error_message() << std::endl;
  }
});https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L315-L337
```

##### Node.js

    // Get a new write batch
    const batch = db.batch();

    // Set the value of 'NYC'
    const nycRef = db.collection('cities').doc('NYC');
    batch.set(nycRef, {name: 'New York City'});

    // Update the population of 'SF'
    const sfRef = db.collection('cities').doc('SF');
    batch.update(sfRef, {population: 1000000});

    // Delete the city 'LA'
    const laRef = db.collection('cities').doc('LA');
    batch.delete(laRef);

    // Commit the batch
    await batch.commit();  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/firestore/main/index.js#L423-L439

##### Go


    import (
    	"context"
    	"log"

    	"cloud.google.com/go/firestore"
    )

    func batchWrite(ctx context.Context, client *firestore.Client) error {
    	// Get a new write batch.
    	batch := client.Batch()

    	// Set the value of "NYC".
    	nycRef := client.Collection("cities").Doc("NYC")
    	batch.Set(nycRef, map[string]interface{}{
    		"name": "New York City",
    	})

    	// Update the population of "SF".
    	sfRef := client.Collection("cities").Doc("SF")
    	batch.Set(sfRef, map[string]interface{}{
    		"population": 1000000,
    	}, firestore.MergeAll)

    	// Delete the city "LA".
    	laRef := client.Collection("cities").Doc("LA")
    	batch.Delete(laRef)

    	// Commit the batch.
    	_, err := batch.Commit(ctx)
    	if err != nil {
    		// Handle any errors in an appropriate way, such as returning them.
    		log.Printf("An error has occurred: %s", err)
    	}

    	return err
    }  
    https://github.com/GoogleCloudPlatform/golang-samples/blob/afaa7f40a550aee552c7b962c8a9ac3a390381ca/firestore/save_data_batch_writes.go#L18-L55

##### PHP

    $batch = $db->bulkWriter();

    # Set the data for NYC
    $nycRef = $db->collection('samples/php/cities')->document('NYC');
    $batch->set($nycRef, [
        'name' => 'New York City'
    ]);

    # Update the population for SF
    $sfRef = $db->collection('samples/php/cities')->document('SF');
    $batch->update($sfRef, [
        ['path' => 'population', 'value' => 1000000]
    ]);

    # Delete LA
    $laRef = $db->collection('samples/php/cities')->document('LA');
    $batch->delete($laRef);

    # Commit the batch
    $batch->commit();  
    https://github.com/GoogleCloudPlatform/php-docs-samples/blob/819b0089cc6bdecde9fe4ec1c54f80f130c4b4d1/firestore/src/data_batch_writes.php#L40-L59

##### Unity

```c#
WriteBatch batch = db.StartBatch();

// Set the data for NYC
DocumentReference nycRef = db.Collection("cities").Document("NYC");
Dictionary<string, object> nycData = new Dictionary<string, object>
{
    { "name", "New York City" }
};
batch.Set(nycRef, nycData);

// Update the population for SF
DocumentReference sfRef = db.Collection("cities").Document("SF");
Dictionary<string, object> updates = new Dictionary<string, object>
{
    { "Population", 1000000}
};
batch.Update(sfRef, updates);

// Delete LA
DocumentReference laRef = db.Collection("cities").Document("LA");
batch.Delete(laRef);

// Commit the batch
batch.CommitAsync();
```

##### C#

    WriteBatch batch = db.StartBatch();

    // Set the data for NYC
    DocumentReference nycRef = db.Collection("cities").Document("NYC");
    Dictionary<string, object> nycData = new Dictionary<string, object>
    {
        { "name", "New York City" }
    };
    batch.Set(nycRef, nycData);

    // Update the population for SF
    DocumentReference sfRef = db.Collection("cities").Document("SF");
    Dictionary<string, object> updates = new Dictionary<string, object>
    {
        { "Population", 1000000}
    };
    batch.Update(sfRef, updates);

    // Delete LA
    DocumentReference laRef = db.Collection("cities").Document("LA");
    batch.Delete(laRef);

    // Commit the batch
    await batch.CommitAsync();  
    https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/7c95aa33b780cf05c9d699b3c664812d40629c35/firestore/api/TransactionsAndBatchedWrites/Program.cs#L92-L115

##### Ruby

    firestore.batch do |b|
      # Set the data for NYC
      b.set "#{collection_path}/NYC", { name: "New York City" }

      # Update the population for SF
      b.update "#{collection_path}/SF", { population: 1_000_000 }

      # Delete LA
      b.delete "#{collection_path}/LA"
    end  
    https://github.com/googleapis/google-cloud-ruby/blob/0ed698db17c491e8e3dd82b79fa990c3ae3ef0fa/google-cloud-firestore/samples/transactions_and_batched_writes.rb#L64-L73

Like transactions, batched writes are atomic. Unlike transactions, batched writes do not need to ensure that read documents remain un-modified which leads to fewer failure cases. They are not subject to retries or to failures from too many retries. Batched writes execute even when the user's device is offline.

A batched write with hundreds of documents might require many index updates and might exceed the limit on transaction size. In this case, reduce the number of documents per batch. To write a large number of documents, consider using a bulk writer or parallelized individual writes instead.
| **Note:** For bulk data entry, use a[server client library](https://firebase.google.com/docs/firestore/client/libraries#server_client_libraries)with parallelized individual writes. Batched writes perform better than serialized writes but not better than parallel writes. You should use a server client library for bulk data operations and not a mobile/web SDK.

## Data validation for atomic operations

For mobile/web client libraries, you can validate data using[Cloud FirestoreSecurity Rules](https://firebase.google.com/docs/firestore/security/get-started). You can ensure that related documents are always updated atomically and always as part of a transaction or batched write. Use the[`getAfter()`](https://firebase.google.com/docs/reference/rules/rules.firestore#.getAfter)security rule function to access and validate the state of a document after a set of operations completes but*before* Cloud Firestorecommits the operations.

For example, imagine that the database for the`cities`example also contains a`countries`collection. Each`country`document uses a`last_updated`field to keep track of the last time any city related to that country was updated. The following security rules require that an update to a`city`document must also atomically update the related country's`last_updated`field:  

```css+lasso
service cloud.firestore {
  match /databases/{database}/documents {
    // If you update a city doc, you must also
    // update the related country's last_updated field.
    match /cities/{city} {
      allow write: if request.auth != null &&
        getAfter(
          /databases/$(database)/documents/countries/$(request.resource.data.country)
        ).data.last_updated == request.time;
    }

    match /countries/{country} {
      allow write: if request.auth != null;
    }
  }
}
```

### Security rules limits

In security rules for transactions or batched writes, there is a[limit](https://firebase.google.com/docs/firestore/quotas#security_rules)of 20 document access calls for the entire atomic operation in addition to the normal 10 call limit for each single document operation in the batch.

For example, consider the following rules for a chat application:  

```css+lasso
service cloud.firestore {
  match /databases/{db}/documents {
    function prefix() {
      return /databases/{db}/documents;
    }
    match /chatroom/{roomId} {
      allow read, write: if request.auth != null && roomId in get(/$(prefix())/users/$(request.auth.uid)).data.chats
                            || exists(/$(prefix())/admins/$(request.auth.uid));
    }
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId
                            || exists(/$(prefix())/admins/$(request.auth.uid));
    }
    match /admins/{userId} {
      allow read, write: if request.auth != null && exists(/$(prefix())/admins/$(request.auth.uid));
    }
  }
}
```

The snippets below illustrate the number of document access calls used for a few data access patterns:  

```gdscript
// 0 document access calls used, because the rules evaluation short-circuits
// before the exists() call is invoked.
db.collection('user').doc('myuid').get(...);

// 1 document access call used. The maximum total allowed for this call
// is 10, because it is a single document request.
db.collection('chatroom').doc('mygroup').get(...);

// Initializing a write batch...
var batch = db.batch();

// 2 document access calls used, 10 allowed.
var group1Ref = db.collection("chatroom").doc("group1");
batch.set(group1Ref, {msg: "Hello, from Admin!"});

// 1 document access call used, 10 allowed.
var newUserRef = db.collection("users").doc("newuser");
batch.update(newUserRef, {"lastSignedIn": new Date()});

// 1 document access call used, 10 allowed.
var removedAdminRef = db.collection("admin").doc("otheruser");
batch.delete(removedAdminRef);

// The batch used a total of 2 + 1 + 1 = 4 document access calls, out of a total
// 20 allowed.
batch.commit();
```

For more information on how to resolve latency issues caused by large writes and batched writes, errors due to contention from overlapping transactions, and other issues consider checking out the[troubleshooting page](https://cloud.google.com/firestore/docs/troubleshooting).