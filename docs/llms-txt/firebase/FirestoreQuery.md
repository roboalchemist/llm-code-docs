# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery.md.txt

# FirebaseFirestoreSwift Framework Reference

# FirestoreQuery

    @available(iOS 14.0, macOS 11.0, tvOS 14.0, watchOS 7.0, *)
    @propertyWrapper
    public struct FirestoreQuery<T> : DynamicProperty

A property wrapper that listens to a Firestore collection.

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
- `
  ``
  ``
  `

  ### [Configuration](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery/Configuration.html)

  `
  `  
  The query's configurable properties.  

  #### Declaration

  Swift  

      public struct Configuration

- `
  ``
  ``
  `

  ### [wrappedValue](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery#/s:22FirebaseFirestoreSwift0B5QueryV12wrappedValuexvp)

  `
  `  
  The results of the query.

  This property returns an empty collection when there are no matching results.  

  #### Declaration

  Swift  

      public var wrappedValue: T { get }

- `
  ``
  ``
  `

  ### [projectedValue](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery#/s:22FirebaseFirestoreSwift0B5QueryV14projectedValueAC13ConfigurationVyx_Gvp)

  `
  `  
  A binding to the request's mutable configuration properties  

  #### Declaration

  Swift  

      public var projectedValue: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery/Configuration.html { get nonmutating set }

- `
  ``
  ``
  `

  ### [init(collectionPath:predicates:decodingFailureStrategy:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery#/s:22FirebaseFirestoreSwift0B5QueryV14collectionPath10predicates23decodingFailureStrategyACySayqd__GGSS_SayAA0D9PredicateOGAA08DecodingiJ0OtcAGRszSeRd__lufc)

  `
  `  
  Creates an instance by defining a query based on the parameters.  

  #### Declaration

  Swift  

      public init<U: Decodable>(collectionPath: String, predicates: [https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/QueryPredicate.html] = [],
                                decodingFailureStrategy: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy.html = .raise)
        where T == [U]

  #### Parameters

  |---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*collectionPath*` `          | The path to the Firestore collection to query.                                                                                                                                                                                                                                                                  |
  | ` `*predicates*` `              | An optional array of [QueryPredicate](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/QueryPredicate.html)s that defines a filter for the fetched results.                                                                                                          |
  | ` `*decodingFailureStrategy*` ` | The strategy to use when there is a failure during the decoding phase. Defaults to [DecodingFailureStrategy.raise](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy.html#/s:22FirebaseFirestoreSwift23DecodingFailureStrategyO5raiseyA2CmF). |

- `
  ``
  ``
  `

  ### [init(collectionPath:predicates:decodingFailureStrategy:)](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Structs/FirestoreQuery#/s:22FirebaseFirestoreSwift0B5QueryV14collectionPath10predicates23decodingFailureStrategyACys6ResultOySayqd__Gs5Error_pGGSS_SayAA0D9PredicateOGAA08DecodingiJ0OtcAKRszSeRd__lufc)

  `
  `  
  Creates an instance by defining a query based on the parameters.  

  #### Declaration

  Swift  

      public init<U: Decodable>(collectionPath: String, predicates: [https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/QueryPredicate.html] = [],
                                decodingFailureStrategy: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy.html = .raise)
        where T == Result<[U], Error>

  #### Parameters

  |---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*collectionPath*` `          | The path to the Firestore collection to query.                                                                                                                                                                                                                                                                  |
  | ` `*predicates*` `              | An optional array of [QueryPredicate](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/QueryPredicate.html)s that defines a filter for the fetched results.                                                                                                          |
  | ` `*decodingFailureStrategy*` ` | The strategy to use when there is a failure during the decoding phase. Defaults to [DecodingFailureStrategy.raise](https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/DecodingFailureStrategy.html#/s:22FirebaseFirestoreSwift23DecodingFailureStrategyO5raiseyA2CmF). |