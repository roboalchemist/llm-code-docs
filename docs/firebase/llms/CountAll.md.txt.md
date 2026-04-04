# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CountAll.md.txt

# FirebaseFirestore Framework Reference

# CountAll

    public class CountAll : https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.html, @unchecked Sendable

Represents an aggregation that counts all documents in the input set.

`CountAll` is used within the `aggregate` pipeline stage to get the total number of documents
that match the query criteria up to that point.

Example usage:

    // Count all books in the collection
    firestore.pipeline()
      .collection("books")
      .aggregate([
        CountAll().as("totalBooks")
      ])

    // Count all sci-fi books published after 1960
    firestore.pipeline()
      .collection("books")
      .where(Field("genre").equal("Science Fiction") && Field("published").greaterThan(1960))
      .aggregate([
        CountAll().as("sciFiBooksCount")
      ])

- `


  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CountAll#/s:17FirebaseFirestore8CountAllCACycfc)


  ` Initializes a new `CountAll` aggregation.

  #### Declaration

  Swift

      public init()