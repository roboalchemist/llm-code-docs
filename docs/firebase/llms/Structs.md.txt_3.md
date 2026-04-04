# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs.md.txt

# FirebaseFirestore Framework Reference

# Structures

The following structures are available globally.
- `


  ### [DocumentID](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DocumentID)


  ` A property wrapper type that marks a `DocumentReference?` or `String?` field to
  be populated with a document identifier when it is read.

  Apply the `@DocumentID` annotation to a `DocumentReference?` or `String?`
  property in a `Codable` object to have it populated with the document
  identifier when it is read and decoded from Firestore.
  Important

  The name of the property annotated with `@DocumentID` must not
  match the name of any fields in the Firestore document being read or else
  an error will be thrown. For example, if the `Codable` object has a
  property named `firstName` annotated with `@DocumentID`, and the Firestore
  document contains a field named `firstName`, an error will be thrown when
  attempting to decode the document.
  - Example Read:

        struct Player: Codable {
        @DocumentID var playerID: String?
        var health: Int64
        }

  let p = try! await Firestore.firestore()
  .collection("players")
  .document("player-1")
  .getDocument(as: Player.self)
  print("(p.playerID!) Health: (p.health)")

  // Prints: "Player: player-1, Health: 95"


      - Important: Trying to encode/decode this type using encoders/decoders other than
        Firestore.Encoder throws an error.

      - Important: When writing a Codable object containing an `@DocumentID` annotated field,
        its value is ignored. This allows you to read a document from one path and
        write it into another without adjusting the value here.

  #### Declaration

  Swift

      @propertyWrapper
      public struct DocumentID<Value: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/DocumentIDWrappable & Codable>:
        StructureCodingUncodedUnkeyed

      extension DocumentID: Codable

      extension DocumentID: Equatable where Value: Equatable

      extension DocumentID: Hashable where Value: Hashable

- `


  ### [ExplicitNull](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ExplicitNull)


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


  ### [ServerTimestamp](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/ServerTimestamp)


  ` A property wrapper that marks an `Optional<Timestamp>` field to be
  populated with a server timestamp. If a `Codable` object being written
  contains a `nil` for an `@ServerTimestamp`-annotated field, it will be
  replaced with `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue#/c:objc(cs)FIRFieldValue(cm)fieldValueForServerTimestamp` as it is sent.

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
        where Value: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/ServerTimestampWrappable & Codable

      extension ServerTimestamp: Equatable where Value: Equatable

      extension ServerTimestamp: Hashable where Value: Hashable

      extension ServerTimestamp: Sendable where Value: Sendable

- `


  ### [FirestoreQuery](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery)


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
  in case mapping the Firestore documents wasn't successful:

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
      @MainActor
      public struct FirestoreQuery<T> : DynamicProperty

- `


  ### [AliasedAggregate](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs#/s:17FirebaseFirestore16AliasedAggregateV)


  ` An `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction` that has been given an alias.

  #### Declaration

  Swift

      public struct AliasedAggregate

- `


  ### [DistanceMeasure](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DistanceMeasure)


  ` Represents the distance measure to be used in a vector similarity search.

  #### Declaration

  Swift

      public struct DistanceMeasure : Sendable, Equatable, Hashable

- `


  ### [AliasedExpression](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs#/s:17FirebaseFirestore17AliasedExpressionV)


  ` An `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression` that has been given an alias.

  #### Declaration

  Swift

      public struct AliasedExpression : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols#/s:17FirebaseFirestore10SelectableP, SelectableWrapper, Sendable

- `


  ### [Constant](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Constant)


  ` A `Constant` is an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression` that represents a fixed, literal value within a Firestore
  pipeline.

  `Constant`s are used to introduce literal values into a query, which can be useful for:
  - Comparing a field to a specific value in a `where` clause.
  - Adding new fields with fixed values using `addFields`.
  - Providing literal arguments to functions like `sum` or `average`.

  Example of using a `Constant` to add a new field:

      // Add a new field "source" with the value "manual" to each document
      firestore.pipeline()
        .collection("entries")
        .addFields([
          Constant("manual").as("source")
        ])

  #### Declaration

  Swift

      public struct Constant : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression, BridgeWrapper, @unchecked Sendable

- `


  ### [Field](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field)


  ` A `Field` is an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression` that represents a field in a Firestore document.

  It is a central component for building queries and transformations in Firestore pipelines.
  A `Field` can be used to:
  - Reference a document field by its name or `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath`.
  - Create complex `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression`s for filtering in a `where` clause.
  - Perform mathematical operations on numeric fields.
  - Manipulate string and array fields.

  Example of creating a `Field` and using it in a `where` clause:

      // Reference the "price" field in a document
      let priceField = Field("price")

      // Create a query to find products where the price is greater than 100
      firestore.pipeline()
        .collection("products")
        .where(priceField.greaterThan(100))

  #### Declaration

  Swift

      public struct Field: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression, https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols#/s:17FirebaseFirestore10SelectableP, BridgeWrapper, SelectableWrapper,
        @unchecked Sendable

- `


  ### [Ordering](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering)


  ` An ordering for the documents in a pipeline.

  #### Declaration

  Swift

      public struct Ordering : @unchecked Sendable

- `


  ### [Direction](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Direction)


  ` A direction to order results in.

  #### Declaration

  Swift

      public struct Direction : Sendable, Equatable, Hashable

- `


  ### [Pipeline](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline)


  ` The `Pipeline` class provides a flexible and expressive framework for building complex data
  transformation and query pipelines for Firestore.

  A pipeline takes data sources, such as Firestore collections or collection groups, and applies
  a series of stages that are chained together. Each stage takes the output from the previous
  stage (or the data source) and produces an output for the next stage (or as the final output of
  the pipeline).

  Expressions can be used within each stage to filter and transform data through the stage.

  ## Usage Examples

  The following examples assume you have a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore` instance named `db`.

      import FirebaseFirestore

      // Example 1: Select specific fields and rename 'rating' to 'bookRating'.
      // Assumes `Field("rating").as("bookRating")` is a valid `Selectable` expression.
      do {
      let snapshot1 = try await db.pipeline().collection("books")
      .select(Field("title"), Field("author"), Field("rating").as("bookRating"))
      .execute()
      print("Results 1: \(snapshot1.results)")
      } catch {
      print("Error in example 1: \(error)")
      }

      // Example 2: Filter documents where 'genre' is "Science Fiction" and 'published' is after 1950.
      do {
      let snapshot2 = try await db.pipeline().collection("books")
      .where(
      Field("genre").equal("Science Fiction")
      && Field("published").greaterThan(1950)
      )
      .execute()
      print("Results 2: \(snapshot2.results)")
      } catch {
      print("Error in example 2: \(error)")
      }

      // Example 3: Calculate the average rating of books published after 1980.
      do {
      let snapshot3 = try await db.pipeline().collection("books")
      .where(Field("published").greaterThan(1980))
      .aggregate(Field("rating").average().as("averageRating"))
      .execute()
      print("Results 3: \(snapshot3.results)")
      } catch {
      print("Error in example 3: \(error)")
      }

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      public struct Pipeline : @unchecked Sendable

- `


  ### [PipelineResult](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult)


  ` Undocumented

  #### Declaration

  Swift

      public struct PipelineResult : @unchecked Sendable

- `


  ### [PipelineSource](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineSource)


  ` A `PipelineSource` is the entry point for building a Firestore pipeline. It allows you to
  specify the source of the data for the pipeline, which can be a collection, a collection group,
  a list of documents, or the entire database.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      public struct PipelineSource : @unchecked Sendable

- `


  ### [TimeGranularity](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/TimeGranularity)


  ` Undocumented

  #### Declaration

  Swift

      public struct TimeGranularity : Sendable, Equatable, Hashable

- `


  ### [TimeUnit](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/TimeUnit)


  ` Undocumented

  #### Declaration

  Swift

      public struct TimeUnit : Sendable, Equatable, Hashable