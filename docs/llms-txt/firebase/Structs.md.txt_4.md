# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs.md.txt

# FirebaseFirestoreSwift Framework Reference

# Structures

The following structures are available globally.
- `


  ### [DocumentID](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/DocumentID)


  ` A value that is populated in Codable objects with the `DocumentReference`
  of the current document by the Firestore.Decoder when a document is read.

  If the field name used for this type conflicts with a read document field,
  an error is thrown. For example, if a custom object has a field `firstName`
  annotated with `@DocumentID`, and there is a property from the document
  named `firstName` as well, an error is thrown when you try to read the
  document.

  When writing a Codable object containing an `@DocumentID` annotated field,
  its value is ignored. This allows you to read a document from one path and
  write it into another without adjusting the value here.

  NOTE: Trying to encode/decode this type using encoders/decoders other than
  Firestore.Encoder leads to an error.

  #### Declaration

  Swift

      @propertyWrapper
      public struct DocumentID<Value: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/DocumentIDWrappable & Codable>:
        DocumentIDProtocol, Codable

      extension DocumentID: Equatable where Value: Equatable

      extension DocumentID: Hashable where Value: Hashable

- `


  ### [ExplicitNull](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/ExplicitNull)


  ` Wraps an `Optional` field in a `Codable` object such that when the field
  has a `nil` value it will encode to a null value in Firestore. Normally,
  optional fields are omitted from the encoded document.

  This is useful for ensuring a field is present in a Firestore document,
  even when there is no associated value.

  #### Declaration

  Swift

      @propertyWrapper
      public struct ExplicitNull<Value>

      extension ExplicitNull: Equatable where Value: Equatable

      extension ExplicitNull: Hashable where Value: Hashable

      extension ExplicitNull: Encodable where Value: Encodable

      extension ExplicitNull: Decodable where Value: Decodable

- `


  ### [ServerTimestamp](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/ServerTimestamp)


  ` A property wrapper that marks an `Optional<Timestamp>` field to be
  populated with a server timestamp. If a `Codable` object being written
  contains a `nil` for an `@ServerTimestamp`-annotated field, it will be
  replaced with `FieldValue.serverTimestamp()` as it is sent.

  Example:

      struct CustomModel {
        @ServerTimestamp var ts: Timestamp?
      }

  Then writing `CustomModel(ts: nil)` will tell server to fill `ts` with
  current timestamp.

  #### Declaration

  Swift

      @propertyWrapper
      public struct ServerTimestamp<Value>: Codable
        where Value: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Protocols/ServerTimestampWrappable & Codable

      extension ServerTimestamp: Equatable where Value: Equatable

      extension ServerTimestamp: Hashable where Value: Hashable

- `


  ### [FirestoreQuery](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery)


  ` A property wrapper that listens to a Firestore collection.

  In the following example, `FirestoreQuery` will fetch all documents from the
  `fruits` collection, filtering only documents whose `isFavourite` attribute
  is equal to `true`, map members of result set to the `Fruit` type, and make
  them available via the wrapped value `fruits`.

      struct ContentView: View {
        @FirestoreQuery(
          collectionPath: "fruits",
          predicates: [.whereField("isFavourite", isEqualTo: true)]
        ) var fruits: [Fruit]

        var body: some View {
          List(fruits) { fruit in
            Text(fruit.name)
          }
        }
      }

  `FirestoreQuery` also supports returning a `Result` type. The `.success` case
  returns an array of elements, whereas the `.failure` case returns an error
  in case mapping the Firestore docments wasn't successful:

      struct ContentView: View {
        @FirestoreQuery(
          collectionPath: "fruits",
          predicates: [.whereField("isFavourite", isEqualTo: true)]
        ) var fruitResults: Result<[Fruit], Error>

      var body: some View {
        if case let .success(fruits) = fruitResults {
          List(fruits) { fruit in
            Text(fruit.name)
          }
        } else if case let .failure(error) = fruitResults {
          Text("Couldn't map data: \(error.localizedDescription)")
        }
      }

  Alternatively, the *projected value* of the property wrapper provides access to
  the `error` as well. This allows you to display a list of all successfully mapped
  documents, as well as an error message with details about the documents that couldn't
  be mapped successfully (e.g. because of a field name mismatch).

      struct ContentView: View {
        @FirestoreQuery(
          collectionPath: "mappingFailure",
          decodingFailureStrategy: .ignore
        ) private var fruits: [Fruit]

        var body: some View {
          VStack(alignment: .leading) {
            List(fruits) { fruit in
              Text(fruit.name)
            }
            if $fruits.error != nil {
              HStack {
                Text("There was an error")
                  .foregroundColor(Color(UIColor.systemBackground))
                Spacer()
              }
              .padding(30)
              .background(Color.red)
            }
          }
        }
      }

  Internally, `@FirestoreQuery` sets up a snapshot listener and publishes
  any incoming changes via an `@StateObject`.

  The projected value of this property wrapper provides access to a
  configuration object of type `FirestoreQueryConfiguration` which can be used
  to modify the query criteria. Changing the filter predicates results in the
  underlying snapshot listener being unregistered and a new one registered.

      Button("Show only Apples and Oranges") {
        $fruits.predicates = [.whereField("name", isIn: ["Apple", "Orange]]
      }

  This property wrapper does not support updating the `wrappedValue`, i.e.
  you need to use Firestore's other APIs to add, delete, or modify documents.

  #### Declaration

  Swift

      @available(iOS 14.0, macOS 11.0, tvOS 14.0, watchOS 7.0, *)
      @propertyWrapper
      public struct FirestoreQuery<T> : DynamicProperty