# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/package-summary.md.txt

# com.google.firebase.firestore.pipeline

# com.google.firebase.firestore.pipeline

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AbstractOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A class that represents an aggregate function. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateHints` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | Performs optionally grouped aggregation operations on the documents from previous stages. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedAggregate` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedExpression` | Represents an expression that will be given the alias in the output document. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A class that represents a filter condition. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionGroupOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionGroupSource` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionHints` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionSource` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionSourceOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | Represents an expression that can be evaluated to a value within the execution of a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` | Represents a reference to a field in a Firestore document. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage` | Performs a vector similarity search, ordering the result set by most similar to least similar, and returning the first N documents in the result set. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FindNearestStage.DistanceMeasure` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/FunctionExpression` | This class defines the base class for Firestore `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` functions, which can be evaluated within pipeline execution. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | Represents an ordering criterion for sorting documents in a Firestore pipeline. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/RawStage` | Adds a stage to the pipeline by specifying the stage name as an argument. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | Performs a pseudo-random sampling of the input documents. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Mode` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable` | Expressions that have an alias are `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestOptions` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias. |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction` |   |