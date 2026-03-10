# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.md.txt

# FirebaseFirestore Framework Reference

# Pipeline

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    public struct Pipeline : @unchecked Sendable

The `Pipeline` class provides a flexible and expressive framework for building complex data
transformation and query pipelines for Firestore.

A pipeline takes data sources, such as Firestore collections or collection groups, and applies
a series of stages that are chained together. Each stage takes the output from the previous
stage (or the data source) and produces an output for the next stage (or as the final output of
the pipeline).

Expressions can be used within each stage to filter and transform data through the stage.

## Usage Examples

The following examples assume you have a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html` instance named `db`.

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

- `


  ### [Snapshot](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline/Snapshot.html)


  ` A `Pipeline.Snapshot` contains the results of a pipeline execution.

  #### Declaration

  Swift

      public struct Snapshot : Sendable

- `


  ### [execute()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV7executeAC8SnapshotVyYaKF)


  ` Executes the defined pipeline and returns a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline/Snapshot.html` containing the results.

  This method asynchronously sends the pipeline definition to Firestore for execution.
  The resulting documents, transformed and filtered by the pipeline stages, are returned
  within a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline/Snapshot.html`.

      // let pipeline: Pipeline = ... // Assume a pipeline is already configured.
      do {
        let snapshot = try await pipeline.execute()
        // Process snapshot.results
        print("Pipeline executed successfully: \(snapshot.results)")
      } catch {
        print("Pipeline execution failed: \(error)")
      }

  Throws
  An error if the pipeline execution fails on the backend.

  #### Declaration

  Swift

      public func execute() async throws -> Pipeline.https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline/Snapshot.html

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline/Snapshot.html` containing the result of the pipeline execution.
- `


  ### [addFields(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV9addFieldsyACSayAA10Selectable_pGF)


  ` Adds new fields to outputs from previous stages.

  This stage allows you to compute values on-the-fly based on existing data from previous
  stages or constants. You can use this to create new fields or overwrite existing ones
  (if there is a name overlap).

      // let pipeline: Pipeline = ... // Assume initial pipeline from a collection.
      let updatedPipeline = pipeline.addFields([
        Field("rating").as("bookRating"), // Rename 'rating' to 'bookRating'.
        Field("quantity").add(5).as("totalQuantityPlusFive") // Calculate
      // 'totalQuantityPlusFive'.
      ])
      // let results = try await updatedPipeline.execute()

  #### Declaration

  Swift

      public func addFields(_ selectables: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP]) -> Pipeline

  #### Parameters

  |---|---|
  | ` selectables ` | An array of at least one `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP` to add to the documents. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [removeFields(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV12removeFieldsyACSayAA5FieldVGF)


  ` Removes fields from outputs of previous stages.

      // let pipeline: Pipeline = ... // Assume initial pipeline.
      let updatedPipeline = pipeline.removeFields([Field("confidentialData"),
      Field("internalNotes")])
      // let results = try await updatedPipeline.execute()

  #### Declaration

  Swift

      public func removeFields(_ fields: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html]) -> Pipeline

  #### Parameters

  |---|---|
  | ` fields ` | An array of at least one `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html` instance to remove. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [removeFields(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV12removeFieldsyACSaySSGF)


  ` Removes fields from outputs of previous stages using field names.

      // let pipeline: Pipeline = ... // Assume initial pipeline.
      // Removes fields 'rating' and 'cost' from the previous stage outputs.
      let updatedPipeline = pipeline.removeFields(["rating", "cost"])
      // let results = try await updatedPipeline.execute()

  #### Declaration

  Swift

      public func removeFields(_ fields: [String]) -> Pipeline

  #### Parameters

  |---|---|
  | ` fields ` | An array of at least one field name to remove. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [select(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV6selectyACSayAA10Selectable_pGF)


  ` Selects or creates a set of fields from the outputs of previous stages.

  The selected fields are defined using `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP` expressions, which can be:
  - `String`: Name of an existing field (implicitly converted to `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html`).
  - `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html`: References an existing field.
  - `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FunctionExpression.html`: Represents the result of a function with an assigned alias (e.g., `Field("address").toUpper().as("upperAddress")`).

  If no selections are provided, the output of this stage is typically empty.
  Use `addFields` if only additions are desired without replacing the existing document
  structure.

      // let pipeline: Pipeline = ... // Assume initial pipeline.
      let projectedPipeline = pipeline.select([
        Field("firstName"),
        Field("lastName"),
        Field("address").toUpper().as("upperAddress")
      ])
      // let results = try await projectedPipeline.execute()

  #### Declaration

  Swift

      public func select(_ selections: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP]) -> Pipeline

  #### Parameters

  |---|---|
  | ` selections ` | An array of at least one `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP` expression to include in the output documents. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [select(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV6selectyACSaySSGF)


  ` Selects a set of fields from the outputs of previous stages using field names.

  The selected fields are specified by their names. If no selections are provided,
  the output of this stage is typically empty. Use `addFields` if only additions are desired.

      // let pipeline: Pipeline = ... // Assume initial pipeline.
      let projectedPipeline = pipeline.select(["title", "author", "yearPublished"])
      // let results = try await projectedPipeline.execute()

  #### Declaration

  Swift

      public func select(_ selections: [String]) -> Pipeline

  #### Parameters

  |---|---|
  | ` selections ` | An array of at least one field name to include in the output documents. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [where(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV5whereyAcA17BooleanExpression_pF)


  ` Filters documents from previous stages, including only those matching the specified
  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html`.

  This stage applies conditions similar to a "WHERE" clause in SQL.
  Filter documents based on field values using `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` implementations, such as:
  - Field comparators: `equal`, `lessThan`, `greaterThan`.
  - Logical operators: `&&` (and), `||` (or), `!` (not).
  - Advanced functions: `regexMatch`, `arrayContains`.

      // let pipeline: Pipeline = ... // Assume initial pipeline.
      let filteredPipeline = pipeline.where(
          Field("rating").greaterThan(4.0)   // Rating greater than 4.0.
          && Field("genre").equal("Science Fiction") // Genre is "Science Fiction".
      )
      // let results = try await filteredPipeline.execute()

  #### Declaration

  Swift

      public func `where`(_ condition: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html) -> Pipeline

  #### Parameters

  |---|---|
  | ` condition ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/BooleanExpression.html` to apply. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [offset(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV6offsetyACs5Int32VF)


  ` Skips the first `offset` number of documents from the results of previous stages.

  A negative input number might count back from the end of the result set,
  depending on backend behavior. This stage is useful for pagination,
  typically used with `limit` to control page size.

      // let pipeline: Pipeline = ... // Assume initial pipeline, possibly sorted.
      // Retrieve the second page of 20 results (skip first 20, limit to next 20).
      let pagedPipeline = pipeline
                          .sort(Field("published").ascending()) // Example sort.
                          .offset(20)  // Skip the first 20 results.
                          .limit(20)   // Take the next 20 results.
      // let results = try await pagedPipeline.execute()

  #### Declaration

  Swift

      public func offset(_ offset: Int32) -> Pipeline

  #### Parameters

  |---|---|
  | ` offset ` | The number of documents to skip (a `Int32` value). |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [limit(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV5limityACs5Int32VF)


  ` Limits the maximum number of documents returned by previous stages to `limit`.

  A negative input number might count back from the end of the result set,
  depending on backend behavior. This stage helps retrieve a controlled subset of data.
  It's often used for:
  - **Pagination:** With `offset` to retrieve specific pages.
  - **Limiting Data Retrieval:** To improve performance with large collections.

      // let pipeline: Pipeline = ... // Assume initial pipeline.
      // Limit results to the top 10 highest-rated books.
      let topTenPipeline = pipeline
                           .sort([Field("rating").descending()])
                           .limit(10)
      // let results = try await topTenPipeline.execute()

  #### Declaration

  Swift

      public func limit(_ limit: Int32) -> Pipeline

  #### Parameters

  |---|---|
  | ` limit ` | The maximum number of documents to return (a `Int32` value). |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [distinct(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV8distinctyACSaySSGF)


  ` Returns a set of distinct documents based on specified grouping field names.

  This stage ensures that only unique combinations of values for the specified
  group fields are included from the previous stage's output.

      // let pipeline: Pipeline = ... // Assume initial pipeline.
      // Get a list of unique author and genre combinations.
      let distinctAuthorsGenresPipeline = pipeline.distinct(["author", "genre"])
      // To further select only the author:
      //   .select("author")
      // let results = try await distinctAuthorsGenresPipeline.execute()

  #### Declaration

  Swift

      public func distinct(_ groups: [String]) -> Pipeline

  #### Parameters

  |---|---|
  | ` groups ` | An array of at least one field name for distinct value combinations. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [distinct(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV8distinctyACSayAA10Selectable_pGF)


  ` Returns a set of distinct documents based on specified `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP` expressions.

  This stage ensures unique combinations of values from evaluated `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP`
  expressions (e.g., `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html` or `Function` results).

  `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP` expressions can be:
  - `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html`: A reference to an existing document field.
  - `Function`: The result of a function with an alias (e.g., `Function.toUppercase(Field("author")).as("authorName")`).

      // let pipeline: Pipeline = ... // Assume initial pipeline.
      // Get unique uppercase author names and genre combinations.
      let distinctPipeline = pipeline.distinct(
        Field("author").toUpper().as("authorName"),
        Field("genre")
      )
      // To select only the transformed author name:
      //   .select(Field("authorName"))
      // let results = try await distinctPipeline.execute()

  #### Declaration

  Swift

      public func distinct(_ groups: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP]) -> Pipeline

  #### Parameters

  |---|---|
  | ` groups ` | An array of at least one `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP` expression to consider. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [aggregate(_:groups:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV9aggregate_6groupsACSayAA16AliasedAggregateVG_SayAA10Selectable_pGSgtF)


  ` Performs optionally grouped aggregation operations on documents from previous stages.

  Calculates aggregate values, optionally grouping documents by fields or `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP`
  expressions.
  - **Grouping:** Defined by the `groups` parameter. Each unique combination of values from these `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP`s forms a group. If `groups` is `nil` or empty, all documents form a single group.
  - **Accumulators:** An array of `AggregateWithAlias` defining operations (e.g., sum, average) within each group.

      // let pipeline: Pipeline = ... // Assume pipeline from "books" collection.
      // Calculate the average rating for each genre.
      let groupedAggregationPipeline = pipeline.aggregate(
        [Field("rating").average().as("avg_rating")],
        groups: [Field("genre")] // Group by the "genre" field.
      )
      // let results = try await groupedAggregationPipeline.execute()
      // snapshot.results might be:
      // [
      //   ["genre": "SciFi", "avg_rating": 4.5],
      //   ["genre": "Fantasy", "avg_rating": 4.2]
      // ]

  #### Declaration

  Swift

      public func aggregate(_ aggregates: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs.html#/s:17FirebaseFirestore16AliasedAggregateV],
                            groups: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP]? = nil) -> Pipeline

  #### Parameters

  |---|---|
  | ` aggregates ` | An array of at least one `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs.html#/s:17FirebaseFirestore16AliasedAggregateV` expression for calculations. |
  | ` groups ` | Optional array of `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP` expressions for grouping. If `nil` or empty, aggregates across all documents. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [findNearest(field:vectorValue:distanceMeasure:limit:distanceField:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV11findNearest5field11vectorValue15distanceMeasure5limit0I5FieldAcA0L0V_So09FIRVectorH0CAA08DistanceJ0VSiSgSSSgtF)


  ` Performs a vector similarity search, ordering results by similarity.

  Returns up to `limit` documents, from most to least similar based on vector embeddings.
  The distance can optionally be included in a specified field.

      // let pipeline: Pipeline = ... // Assume pipeline from a collection with vector embeddings.
      let queryVector = VectorValue([0.1, 0.2, ..., 0.8]) // Example query vector.
      let nearestNeighborsPipeline = pipeline.findNearest(
        field: Field("embedding_field"),       // Field containing the vector.
        vectorValue: queryVector,              // Query vector for comparison.
        distanceMeasure: .cosine,              // Distance metric.
        limit: 10,                             // Return top 10 nearest neighbors.
        distanceField: "similarityScore"       // Optional: field for distance score.
      )
      // let results = try await nearestNeighborsPipeline.execute()

  #### Declaration

  Swift

      public func findNearest(field: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html,
                              vectorValue: VectorValue,
                              distanceMeasure: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DistanceMeasure.html,
                              limit: Int? = nil,
                              distanceField: String? = nil) -> Pipeline

  #### Parameters

  |---|---|
  | ` field ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html` containing vector embeddings. |
  | ` vectorValue ` | A `VectorValue` instance representing the query vector. |
  | ` distanceMeasure ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/DistanceMeasure.html` (e.g., `.euclidean`, `.cosine`) for comparison. |
  | ` limit ` | Optional. Maximum number of similar documents to return. |
  | ` distanceField ` | Optional. Name for a new field to store the calculated distance. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [sort(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV4sortyACSayAA8OrderingVGF)


  ` Sorts documents from previous stages based on one or more `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering.html` criteria.

  Specify multiple `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering.html` instances for multi-field sorting (ascending/descending).
  If documents are equal by one criterion, the next is used. If all are equal,
  relative order is unspecified.

      // let pipeline: Pipeline = ... // Assume initial pipeline.
      // Sort books by rating (descending), then by title (ascending).
      let sortedPipeline = pipeline.sort([
        Field("rating").descending(),
        Field("title").ascending()
      ])
      // let results = try await sortedPipeline.execute()

  #### Declaration

  Swift

      public func sort(_ orderings: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering.html]) -> Pipeline

  #### Parameters

  |---|---|
  | ` orderings ` | An array of at least one `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Ordering.html` criterion. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [replace(with:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV7replace4withAcA10Expression_p_tF)


  ` Fully overwrites document fields with those from a nested map identified by an `Expr`.

  "Promotes" a map value (dictionary) from a field to become the new root document.
  Each key-value pair from the map specified by `expression` becomes a field-value pair
  in the output document, discarding original document fields.

      // Assume input document:
      // { "id": "user123", "profile": { "name": "Alex", "age": 30 }, "status": "active" }
      // let pipeline: Pipeline = ...

      // Replace document with the contents of the 'profile' map.
      let replacedPipeline = pipeline.replace(with: Field("profile"))

      // let results = try await replacedPipeline.execute()
      // Output document would be: { "name": "Alex", "age": 30 }

  #### Declaration

  Swift

      public func replace(with expression: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html) -> Pipeline

  #### Parameters

  |---|---|
  | ` expression ` | The `Expr` (typically a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html`) that resolves to the nested map. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [replace(with:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV7replace4withACSS_tF)


  ` Fully overwrites document fields with those from a nested map identified by a field name.

  "Promotes" a map value (dictionary) from a field to become the new root document.
  Each key-value pair from the map in `fieldName` becomes a field-value pair
  in the output document, discarding original document fields.

      // Assume input document:
      // { "id": "user123", "details": { "role": "admin", "department": "tech" }, "joined":
      "2023-01-15" }
      // let pipeline: Pipeline = ...

      // Replace document with the contents of the 'details' map.
      let replacedPipeline = pipeline.replace(with: "details")

      // let results = try await replacedPipeline.execute()
      // Output document would be: { "role": "admin", "department": "tech" }

  #### Declaration

  Swift

      public func replace(with fieldName: String) -> Pipeline

  #### Parameters

  |---|---|
  | ` fieldName ` | The name of the field containing the nested map. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [sample(count:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV6sample5countACs5Int64V_tF)


  ` Performs pseudo-random sampling of input documents, returning a specific count.

  Filters documents pseudo-randomly. `count` specifies the approximate number
  to return. The actual number may vary and isn't guaranteed if the input set
  is smaller than `count`.

      // let pipeline: Pipeline = ... // Assume pipeline from a large collection.
      // Sample 25 books, if available.
      let sampledPipeline = pipeline.sample(count: 25)
      // let results = try await sampledPipeline.execute()

  #### Declaration

  Swift

      public func sample(count: Int64) -> Pipeline

  #### Parameters

  |---|---|
  | ` count ` | The target number of documents to sample (a `Int64` value). |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [sample(percentage:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV6sample10percentageACSd_tF)


  ` Performs pseudo-random sampling of input documents, returning a percentage.

  Filters documents pseudo-randomly. `percentage` (0.0 to 1.0) specifies
  the approximate fraction of documents to return from the input set.

      // let pipeline: Pipeline = ... // Assume initial pipeline.
      // Sample 50% of books.
      let sampledPipeline = pipeline.sample(percentage: 0.5)
      // let results = try await sampledPipeline.execute()

  #### Declaration

  Swift

      public func sample(percentage: Double) -> Pipeline

  #### Parameters

  |---|---|
  | ` percentage ` | The percentage of documents to sample (e.g., 0.5 for 50%; a `Double` value). |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [union(with:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV5union4withA2C_tF)


  ` Performs a union of all documents from this pipeline and another, including duplicates.

  Passes through documents from this pipeline's previous stage and also those from
  the `other` pipeline's previous stage. The order of emitted documents is undefined.
  Both pipelines should ideally have compatible document structures.

      // let db: Firestore = ...
      // let booksPipeline = db.pipeline().collection("books").select(["title", "category"])
      // let magazinesPipeline = db.pipeline().collection("magazines").select(["title",
      // Field("topic").as("category")])

      // Emit documents from both "books" and "magazines" collections.
      let combinedPipeline = booksPipeline.union(with: magazinesPipeline)
      // let results = try await combinedPipeline.execute()

  #### Declaration

  Swift

      public func union(with other: Pipeline) -> Pipeline

  #### Parameters

  |---|---|
  | ` other ` | Another `Pipeline` whose documents will be unioned. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [unnest(_:indexField:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV6unnest_10indexFieldAcA10Selectable_p_SSSgtF)


  ` Takes an array field from input documents and outputs a new document for each element.

  For each input document, this stage emits zero or more augmented documents based on
  an array field specified by `field` (a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP`). The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP` for `field`
  **must** have an alias; this alias becomes the field name in the output document
  containing the unnested element.

  The original field containing the array is effectively replaced by the array element
  under the new alias name in each output document. Other fields from the original document
  are typically preserved.

  If `indexField` is provided, a new field with this name is added, containing the
  zero-based index of the element within its original array.

  Behavior for non-array values or empty arrays depends on the backend.

      // Assume input document:
      // { "title": "The Hitchhiker's Guide", "authors": ["Douglas Adams", "Eoin Colfer"] }
      // let pipeline: Pipeline = ...

      // Unnest 'authors'. Each author becomes a new document with the author in a "authorName"
      field.
      let unnestedPipeline = pipeline.unnest(Field("authors").as("authorName"), indexField:
      "authorIndex")

      // let results = try await unnestedPipeline.execute()
      // Possible Output (other fields like "title" are preserved):
      // { "title": "The Hitchhiker's Guide", "authorName": "Douglas Adams", "authorIndex": 0 }
      // { "title": "The Hitchhiker's Guide", "authorName": "Eoin Colfer", "authorIndex": 1 }

  #### Declaration

  Swift

      public func unnest(_ field: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP, indexField: String? = nil) -> Pipeline

  #### Parameters

  |---|---|
  | ` field ` | A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/s:17FirebaseFirestore10SelectableP` resolving to an array field. **Must include an alias** (e.g., `Field("myArray").as("arrayElement")`) to name the output field. |
  | ` indexField ` | Optional. If provided, this string names a new field for the element's zero-based index from the original array. |

  #### Return Value

  A new `Pipeline` object with this stage appended.
- `


  ### [rawStage(name:params:options:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline#/s:17FirebaseFirestore8PipelineV8rawStage4name6params7optionsACSS_Says8Sendable_pGSDySSsAH_pGSgtF)


  ` Adds a generic stage to the pipeline by specifying its name and parameters.

  Use this to call backend-supported stages not yet strongly-typed in the SDK.
  This method does not offer compile-time type safety for stage parameters;
  the caller must ensure correct name, order, and types.

  Parameters in `params` and `options` are typically primitive types, `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html`,
  `Function`, `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html`, or arrays/dictionaries thereof.

      // let pipeline: Pipeline = ...
      // Example: Assuming a hypothetical backend stage "customFilterV2".
      let genericPipeline = pipeline.rawStage(
        name: "customFilterV2",
        params: [Field("userScore"), 80], // Ordered parameters.
        options: ["mode": "strict", "logLevel": 2]  // Optional named parameters.
      )
      // let results = try await genericPipeline.execute()

  #### Declaration

  Swift

      public func rawStage(name: String, params: [Sendable],
                           options: [String: Sendable]? = nil) -> Pipeline

  #### Parameters

  |---|---|
  | ` name ` | The unique name of the stage (as recognized by the backend). |
  | ` params ` | An array of ordered, `Sendable` parameters for the stage. |
  | ` options ` | Optional dictionary of named, `Sendable` parameters. |

  #### Return Value

  A new `Pipeline` object with this stage appended.