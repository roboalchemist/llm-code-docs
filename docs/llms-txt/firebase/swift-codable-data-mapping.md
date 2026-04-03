# Source: https://firebase.google.com/docs/firestore/solutions/swift-codable-data-mapping.md.txt

Swift's Codable API, introduced in Swift 4, enables us to leverage the power of the compiler to make it easier to map data from serialized formats to Swift types.

You might have been using Codable to map data from a web API to your app's data model (and vice versa), but it is much more flexible than that.

In this guide, we're going to look at how Codable can be used to map data fromCloud Firestoreto Swift types and vice versa.

When fetching a document fromCloud Firestore, your app will receive a dictionary of key/value pairs (or an array of dictionaries, if you use one of the operations returning multiple documents).

Now, you can certainly continue to directly use dictionaries in Swift, and they offer some great flexibility that might be exactly what your use case calls for. However, this approach isn't type safe and it's easy to introduce hard-to-track-down bugs by misspelling attribute names, or forgetting to map the new attribute your team added when they shipped that exciting new feature last week.

In the past, many developers have worked around these shortcomings by implementing a simple mapping layer that allowed them to map dictionaries to Swift types. But again, most of these implementations are based on manually specifying the mapping betweenCloud Firestoredocuments and the corresponding types of your app's data model.

WithCloud Firestore's support for Swift's Codable API, this becomes a lot easier:

- You will no longer have to manually implement any mapping code.
- It's easy to define how to map attributes with different names.
- It has built-in support for many of Swift's types.
- And it's easy to add support for mapping custom types.
- Best of all: for simple data models, you won't have to write any mapping code at all.

## Mapping data

Cloud Firestorestores data in documents which map keys to values. To fetch data from an individual document, we can call`DocumentSnapshot.data()`, which returns a dictionary mapping the field names to an`Any`:`func data() -> [String : Any]?`.

This means we can use Swift's subscript syntax to access each individual field.
**Note:** The following snippet is here for illustration. It shows one basic, somewhat inefficient way to access document fields. We'll cover the Codable way to access data in the rest of this guide.  

    import FirebaseFirestore

    #warning("DO NOT MAP YOUR DOCUMENTS MANUALLY. USE CODABLE INSTEAD.")
    func fetchBook(documentId: String) {
      let docRef = db.collection("books").document(documentId)

      docRef.getDocument { document, error in
        if let error = error as NSError? {
          self.errorMessage = "Error getting document: \(error.localizedDescription)"
        }
        else {
          if let document = document {
            let id = document.documentID
            let data = document.data()
            let title = data?["title"] as? String ?? ""
            let numberOfPages = data?["numberOfPages"] as? Int ?? 0
            let author = data?["author"] as? String ?? ""
            self.book = Book(id:id, title: title, numberOfPages: numberOfPages, author: author)
          }
        }
      }
    }

While it might seem straightforward and easy to implement, this code is fragile, hard to maintain, and error-prone.

As you can see, we're making assumptions about the data types of the document fields. These might or might not be correct.

Remember, since there is no schema, you can easily add a new document to the collection and choose a different type for a field. You might accidentally choose string for the`numberOfPages`field, which would result in a difficult-to-find mapping issue. Also, you'll have to update your mapping code whenever a new field is added, which is rather cumbersome.

And let's not forget that we're not taking advantage of Swift's strong type system, which knows exactly the correct type for each of the properties of`Book`.
| **Key Point:** Please don't map your documents manually --- use Codable instead!

## What is Codable, anyway?

According to Apple's documentation, Codable is "a type that can convert itself into and out of an external representation." In fact, Codable is a type alias for the Encodable and Decodable protocols. By conforming a Swift type to this protocol, the compiler will synthesize the code needed to encode/decode an instance of this type from a serialized format, such as JSON.

A simple type for storing data about a book might look like this:  

    struct Book: Codable {
      var title: String
      var numberOfPages: Int
      var author: String
    }

As you can see, conforming the type to Codable is minimally invasive. We only had to add the conformance to the protocol; no other changes were required.

With this in place, we can now easily encode a book to a JSON object:  

    do {
      let book = Book(title: "The Hitchhiker's Guide to the Galaxy",
                      numberOfPages: 816,
                      author: "Douglas Adams")
      let encoder = JSONEncoder()
      let data = try encoder.encode(book)
    } 
    catch {
      print("Error when trying to encode book: \(error)")
    }

Decoding a JSON object to a`Book`instance works as follows:  

    let decoder = JSONDecoder()
    let data = /* fetch data from the network */
    let decodedBook = try decoder.decode(Book.self, from: data)

## Mapping to and from simple types inCloud Firestoredocuments
using Codable

Cloud Firestoresupports a broad set of data types, ranging from simple strings to nested maps. Most of these correspond directly to Swift's built-in types. Let's take a look at mapping some simple data types first before we dive into the more complex ones.

To mapCloud Firestoredocuments to Swift types, follow these steps:

1. Make sure you've added the`FirebaseFirestore`framework to your project. You can use[either the Swift Package Manager or CocoaPods](https://firebase.google.com/docs/firestore/quickstart?tab=ios%2B#set_up_your_development_environment)to do so.
2. Import`FirebaseFirestore`into your Swift file.
3. Conform your type to`Codable`.
4. (Optional, if you want to use the type in a`List`view) Add an`id`property to your type, and use`@DocumentID`to tellCloud Firestoreto map this to the document ID. We'll discuss this in more detail below.
5. Use`documentReference.data(as: )`to map a document reference to a Swift type.
6. Use`documentReference.setData(from: )`to map data from Swift types to aCloud Firestoredocument.
7. (Optional, but highly recommended) Implement proper error handling.

Let's update our`Book`type accordingly:  

    struct Book: Codable {
      @DocumentID var id: String?
      var title: String
      var numberOfPages: Int
      var author: String
    }

Since this type was already codable, we only had to add the`id`property and annotate it with the`@DocumentID`property wrapper.

Taking the previous code snippet for fetching and mapping a document, we can replace all the manual mapping code with a single line:  

    func fetchBook(documentId: String) {
      let docRef = db.collection("books").document(documentId)

      docRef.getDocument { document, error in
        if let error = error as NSError? {
          self.errorMessage = "Error getting document: \(error.localizedDescription)"
        }
        else {
          if let document = document {
            do {
              self.book = try document.data(as: Book.self)
            }
            catch {
              print(error)
            }
          }
        }
      }
    }

You can write this even more concisely by specifying the type of the document when calling`getDocument(as:)`. This will perform the mapping for you, and return a`Result`type containing the mapped document, or an error in case decoding failed:  

    private func fetchBook(documentId: String) {
      let docRef = db.collection("books").document(documentId)
      
      docRef.getDocument(as: Book.self) { result in
        switch result {
        case .success(let book):
          // A Book value was successfully initialized from the DocumentSnapshot.
          self.book = book
          self.errorMessage = nil
        case .failure(let error):
          // A Book value could not be initialized from the DocumentSnapshot.
          self.errorMessage = "Error decoding document: \(error.localizedDescription)"
        }
      }
    }

Updating an existing document is as simple as calling`documentReference.setData(from: )`. Including some basic error handling, here is the code to save a`Book`instance:  

    func updateBook(book: Book) {
      if let id = book.id {
        let docRef = db.collection("books").document(id)
        do {
          try docRef.setData(from: book)
        }
        catch {
          print(error)
        }
      }
    }

When adding a new document,Cloud Firestorewill automatically take care of assigning a new document ID to the document. This even works when the app is currently offline.  

    func addBook(book: Book) {
      let collectionRef = db.collection("books")
      do {
        let newDocReference = try collectionRef.addDocument(from: self.book)
        print("Book stored with new document reference: \(newDocReference)")
      }
      catch {
        print(error)
      }
    }

In addition to mapping simple data types,Cloud Firestoresupports a number of other datatypes, some of which are structured types that you can use to create nested objects inside a document.

### Nested custom types

Most attributes we want to map in our documents are simple values, such as the book's title or the author's name. But what about those cases when we need to store a more complex object? For example, we might want to store the URLs to the book's cover in different resolutions.

The easiest way to do this inCloud Firestoreis to use a map:

![Storing a nested custom type in a Firestore document](https://firebase.google.com/static/docs/firestore/images/firestore-codable-map.png)

When writing the corresponding Swift struct, we can make use of the fact thatCloud Firestoresupports URLs --- when storing a field that contains a URL, it will be converted to a string and vice versa:  

    struct CoverImages: Codable {
      var small: URL
      var medium: URL
      var large: URL
    }

    struct BookWithCoverImages: Codable {
      @DocumentID var id: String?
      var title: String
      var numberOfPages: Int
      var author: String
      var cover: CoverImages?
    }

Notice how we defined a struct,`CoverImages`, for the cover map in theCloud Firestoredocument. By marking the cover property on`BookWithCoverImages`as optional, we're able to handle the fact that some documents might not contain a cover attribute.

If you're curious why there is no code snippet for fetching or updating data, you will be pleased to hear that there is no need to adjust the code for reading or writing from/toCloud Firestore: all of this works with the code we've written in the initial section.

### Arrays

Sometimes, we want to store a collection of values in a document. The genres of a book are a good example: a book like*The Hitchhiker's Guide to the Galaxy*might fall into several categories --- in this case "Sci-Fi" and "Comedy":

![Storing an array in a Firestore document](https://firebase.google.com/static/docs/firestore/images/firestore-codable-genre.png)

InCloud Firestore, we can model this using an array of values. This is supported for any codable type (such as`String`,`Int`, etc.). The following shows how to add an array of genres to our`Book`model:  

    public struct BookWithGenre: Codable {
      @DocumentID var id: String?
      var title: String
      var numberOfPages: Int
      var author: String
      var genres: [String]
    }

Since this works for any codable type, we can use custom types as well. Imagine we want to store a list of tags for each book. Along with the name of the tag, we'd like to store the color of the tag as well, like this:

![Storing an array of custom types in a Firestore document](https://firebase.google.com/static/docs/firestore/images/firestore-codable-tags.png)

To store tags in this way, all we need to do is implement a`Tag`struct to represent a tag and make it codable:  

    struct Tag: Codable, Hashable {
      var title: String
      var color: String
    }

And just like that, we can store an array of`Tags`in our`Book`documents!  

    struct BookWithTags: Codable {
      @DocumentID var id: String?
      var title: String
      var numberOfPages: Int
      var author: String
      var tags: [Tag]
    }

### A quick word about mapping document IDs

Before we move on to mapping more types, let's talk about mapping document IDs for a moment.

We used the`@DocumentID`property wrapper in some of the previous examples to map the document ID of ourCloud Firestoredocuments to the`id`property of our Swift types. This is important for a number of reasons:

- It helps us to know which document to update in case the user makes local changes.
- SwiftUI's`List`requires its elements to be`Identifiable`in order to prevent elements from jumping around when they get inserted.

It's worth pointing out that an attribute marked as`@DocumentID`will not be encoded byCloud Firestore's encoder when writing the document back. This is because the document ID is not an attribute of the document itself --- so writing it to the document would be a mistake.

When working with nested types (such as the array of tags on the`Book`in an earlier example in this guide), it is not required to add a`@DocumentID`property: nested properties are a part of theCloud Firestoredocument, and do not constitute a separate document. Hence, they do not need a document ID.

### Dates and times

Cloud Firestorehas a built-in data type for handling dates and times, and thanks toCloud Firestore's support for Codable, it's straightforward to use them.

Let's take a look at this document which represents the mother of all programming languages, Ada, invented in 1843:

![Storing dates in a Firestore document](https://firebase.google.com/static/docs/firestore/images/firestore-codable-ada-date.png)

A Swift type for mapping this document might look like this:  

    struct ProgrammingLanguage: Codable {
      @DocumentID var id: String?
      var name: String
      var year: Date
    }

We cannot leave this section about dates and times without having a conversation about`@ServerTimestamp`. This property wrapper is a powerhouse when it comes to dealing with timestamps in your app.

In any distributed system, chances are that the clocks on the individual systems are not completely in sync all of the time. You might think this is not a big deal, but imagine the implications of a clock running slightly out of sync for a stock trade system: even a millisecond deviation might result in a difference of millions of dollars when executing a trade.

Cloud Firestorehandles attributes marked with`@ServerTimestamp`as follows: if the attribute is`nil`when you store it (using`addDocument()`, for example),Cloud Firestorewill populate the field with the current server timestamp at the time of writing it into the database. If the field is not`nil`when you call`addDocument()`or`updateData()`,Cloud Firestorewill leave the attribute value untouched. This way, it is easy to implement fields like`createdAt`and`lastUpdatedAt`.

### Geopoints

Geolocations are ubiquitous in our apps. Many exciting features become possible by storing them. For example, it might be useful to store a location for a task so your app can remind you about a task when you reach a destination.

Cloud Firestorehas a built-in data type,`GeoPoint`, which can store the longitude and latitude of any location. To map locations from/to aCloud Firestoredocument, we can use the`GeoPoint`type:  

    struct Office: Codable {
      @DocumentID var id: String?
      var name: String
      var location: GeoPoint
    }

The corresponding type in Swift is`CLLocationCoordinate2D`, and we can map between those two types with the following operation:  

    CLLocationCoordinate2D(latitude: office.location.latitude,
                          longitude: office.location.longitude)

To learn more about querying documents by physical location, check out[this solution guide](https://firebase.google.com/docs/firestore/solutions/geoqueries).

### Enums

Enums are probably one of the most underrated language features in Swift; there's much more to them than meets the eye. A common use case for enums is to model the discrete states of something. For example, we might be writing an app for managing articles. To track the status of an article, we might want to use an enum`Status`:  

    enum Status: String, Codable {
      case draft
      case inReview
      case approved
      case published
    }

Cloud Firestoredoesn't support enums natively (i.e., it cannot enforce the set of values), but we can still make use of the fact that enums can be typed, and choose a codable type. In this example, we've chosen`String`, which means all enum values will be mapped to/from string when stored in aCloud Firestoredocument.

And, since Swift supports custom raw values, we can even customize which values refer to which enum case. So for example, if we decided to store the`Status.inReview`case as "in review", we could just update the above enum as follows:  

    enum Status: String, Codable {
      case draft
      case inReview = "in review"
      case approved
      case published
    }

## Customizing the mapping

Sometimes, the attribute names of theCloud Firestoredocuments we want to map don't match up with the names of the properties in our data model in Swift. For example, one of our coworkers might be a Python developer, and decided to choose snake_case for all their attribute names.

Not to worry: Codable has us covered!

For cases like these, we can make use of`CodingKeys`. This is an enum we can add to a codable struct to specify how certain attributes will be mapped.

Consider this document:

![A Firestore document with a snake_cased attribute name](https://firebase.google.com/static/docs/firestore/images/firestore-codable-customize-mapping.png)

To map this document to a struct that has a name property of type`String`, we need to add a`CodingKeys`enum to the`ProgrammingLanguage`struct, and specify the name of the attribute in the document:  

    struct ProgrammingLanguage: Codable {
      @DocumentID var id: String?
      var name: String
      var year: Date
      
      enum CodingKeys: String, CodingKey {
        case id
        case name = "language_name"
        case year
      }
    }

By default, the Codable API will use the property names of our Swift types to determine the attribute names on theCloud Firestoredocuments we're trying to map. So as long as the attribute names match, there is no need to add`CodingKeys`to our codable types. However, once we use`CodingKeys`for a specific type, we need to add all property names we want to map.

In the code snippet above, we've defined an`id`property which we might want to use as the identifier in a SwiftUI`List`view. If we didn't specify it in`CodingKeys`, it wouldn't be mapped when fetching data, and thus become`nil`. This would result in the`List`view being filled with the first document.

Any property that is not listed as a case on the respective`CodingKeys`enum will be ignored during the mapping process. This can actually be convenient if we specifically want to exclude some of the properties from being mapped.

So for example, if we want to exclude the`reasonWhyILoveThis`property from being mapped, all we need to do is to remove it from the`CodingKeys`enum:  

    struct ProgrammingLanguage: Identifiable, Codable {
      @DocumentID var id: String?
      var name: String
      var year: Date
      var reasonWhyILoveThis: String = ""
      
      enum CodingKeys: String, CodingKey {
        case id
        case name = "language_name"
        case year
      }
    }

Occasionally we might want to write an empty attribute back into theCloud Firestoredocument. Swift has the notion of optionals to denote the absence of a value, andCloud Firestoresupports`null`values as well. However, the default behavior for encoding optionals that have a`nil`value is to just omit them.`@ExplicitNull`gives us some control over how Swift optionals are handled when encoding them: by flagging an optional property as`@ExplicitNull`, we can tellCloud Firestoreto write this property to the document with a null value if it contains a value of`nil`.

## Using a custom encoder and decoder for mapping colors

As a last topic in our coverage of mapping data with Codable, let's introduce custom encoders and decoders. This section doesn't cover a nativeCloud Firestoredatatype, but custom encoders and decoders are widely useful in yourCloud Firestoreapps.

"How can I map colors" is one of the most frequently asked developer questions, not only forCloud Firestore, but for mapping between Swift and JSON as well. There are plenty of solutions out there, but most of them focus on JSON, and almost all of them map colors as a nested dictionary composed of its RGB components.

It seems there should be a better, simpler solution. Why don't we use web colors (or, to be more specific, CSS hex color notation) --- they're easy to use (essentially just a string), and they even support transparency!

To be able to map a Swift`Color`to its hex value, we need to create a Swift extension that adds Codable to`Color`.  

    extension Color {

     init(hex: String) {
        let rgba = hex.toRGBA()

        self.init(.sRGB,
                  red: Double(rgba.r),
                  green: Double(rgba.g),
                  blue: Double(rgba.b),
                  opacity: Double(rgba.alpha))
        }

        //... (code for translating between hex and RGBA omitted for brevity)

    }

    extension Color: Codable {
      
      public init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        let hex = try container.decode(String.self)

        self.init(hex: hex)
      }
      
      public func encode(to encoder: Encoder) throws {
        var container = encoder.singleValueContainer()
        try container.encode(toHex)
      }

    }

By using`decoder.singleValueContainer()`, we can decode a`String`to its`Color`equivalent, without having to nest the RGBA components. Plus, you can use these values in the web UI of your app, without having to convert them first!

With this, we can update code for mapping tags, making it easier to handle the tag colors directly instead of having to map them manually in our app's UI code:  

    struct Tag: Codable, Hashable {
      var title: String
      var color: Color
    }

    struct BookWithTags: Codable {
      @DocumentID var id: String?
      var title: String
      var numberOfPages: Int
      var author: String
      var tags: [Tag]
    }

## Handling errors

In the above code snippets we intentionally kept error handling at a minimum, but in a production app, you'll want to make sure to gracefully handle any errors.

Here is a code snippet that shows how to use handle any error situations you might run into:  

    class MappingSimpleTypesViewModel: ObservableObject {
      @Published var book: Book = .empty
      @Published var errorMessage: String?
      
      private var db = Firestore.firestore()
      
      func fetchAndMap() {
        fetchBook(documentId: "hitchhiker")
      }
      
      func fetchAndMapNonExisting() {
        fetchBook(documentId: "does-not-exist")
      }
      
      func fetchAndTryMappingInvalidData() {
        fetchBook(documentId: "invalid-data")
      }
      
      private func fetchBook(documentId: String) {
        let docRef = db.collection("books").document(documentId)
        
        docRef.getDocument(as: Book.self) { result in
          switch result {
          case .success(let book):
            // A Book value was successfully initialized from the DocumentSnapshot.
            self.book = book
            self.errorMessage = nil
          case .failure(let error):
            // A Book value could not be initialized from the DocumentSnapshot.
            switch error {
            case DecodingError.typeMismatch(_, let context):
              self.errorMessage = "\(error.localizedDescription): \(context.debugDescription)"
            case DecodingError.valueNotFound(_, let context):
              self.errorMessage = "\(error.localizedDescription): \(context.debugDescription)"
            case DecodingError.keyNotFound(_, let context):
              self.errorMessage = "\(error.localizedDescription): \(context.debugDescription)"
            case DecodingError.dataCorrupted(let key):
              self.errorMessage = "\(error.localizedDescription): \(key)"
            default:
              self.errorMessage = "Error decoding document: \(error.localizedDescription)"
            }
          }
        }
      }
    }

### Handling errors in live updates

The previous code snippet demonstrates how to handle errors when fetching a single document. In addition to fetching data once,Cloud Firestorealso supports delivering updates to your app as they happen, using so-called snapshot listeners: we can register a snapshot listener on a collection (or query), andCloud Firestorewill call our listener whenever there is an update.

Here is a code snippet that shows how to register a snapshot listener, map data using Codable, and handle any errors that might occur. It also shows how to add a new document to the collection. As you will see, there is no need to update the local array holding the mapped documents ourselves, as this is taken care of by the code in the snapshot listener.  

    class MappingColorsViewModel: ObservableObject {
      @Published var colorEntries = [ColorEntry]()
      @Published var newColor = ColorEntry.empty
      @Published var errorMessage: String?
      
      private var db = Firestore.firestore()
      private var listenerRegistration: ListenerRegistration?
      
      public func unsubscribe() {
        if listenerRegistration != nil {
          listenerRegistration?.remove()
          listenerRegistration = nil
        }
      }
      
      func subscribe() {
        if listenerRegistration == nil {
          listenerRegistration = db.collection("colors")
            .addSnapshotListener { [weak self] (querySnapshot, error) in
              guard let documents = querySnapshot?.documents else {
                self?.errorMessage = "No documents in 'colors' collection"
                return
              }
              
              self?.colorEntries = documents.compactMap { queryDocumentSnapshot in
                let result = Result { try queryDocumentSnapshot.data(as: ColorEntry.self) }
                
                switch result {
                case .success(let colorEntry):
                  if let colorEntry = colorEntry {
                    // A ColorEntry value was successfully initialized from the DocumentSnapshot.
                    self?.errorMessage = nil
                    return colorEntry
                  }
                  else {
                    // A nil value was successfully initialized from the DocumentSnapshot,
                    // or the DocumentSnapshot was nil.
                    self?.errorMessage = "Document doesn't exist."
                    return nil
                  }
                case .failure(let error):
                  // A ColorEntry value could not be initialized from the DocumentSnapshot.
                  switch error {
                  case DecodingError.typeMismatch(_, let context):
                    self?.errorMessage = "\(error.localizedDescription): \(context.debugDescription)"
                  case DecodingError.valueNotFound(_, let context):
                    self?.errorMessage = "\(error.localizedDescription): \(context.debugDescription)"
                  case DecodingError.keyNotFound(_, let context):
                    self?.errorMessage = "\(error.localizedDescription): \(context.debugDescription)"
                  case DecodingError.dataCorrupted(let key):
                    self?.errorMessage = "\(error.localizedDescription): \(key)"
                  default:
                    self?.errorMessage = "Error decoding document: \(error.localizedDescription)"
                  }
                  return nil
                }
              }
            }
        }
      }
      
      func addColorEntry() {
        let collectionRef = db.collection("colors")
        do {
          let newDocReference = try collectionRef.addDocument(from: newColor)
          print("ColorEntry stored with new document reference: \(newDocReference)")
        }
        catch {
          print(error)
        }
      }
    }

All code snippets used in this post are part of a sample application that you can download from[this GitHub repository](https://github.com/peterfriese/Swift-Firestore-Guide).

## Go forth and use Codable!

Swift's Codable API provides a powerful and flexible way to map data from serialized formats to and from your applications data model. In this guide, you saw how easy it is to use in apps that useCloud Firestoreas their datastore.

Starting from a basic example with simple data types, we progressively increased the complexity of the data model, all the while being able to rely on Codable and Firebase's implementation to perform the mapping for us.

For more details about Codable, I recommend the following resources:

- John Sundell has a nice article about the[Basics of Codable](https://www.swiftbysundell.com/basics/codable/).
- If books are more your thing, check out Mattt's[Flight School Guide to Swift Codable](https://flight.school/books/codable/).
- And finally, Donny Wals has an entire[series about Codable](https://www.donnywals.com/category/codable/).

Although we did our best to compile a comprehensive guide for mappingCloud Firestoredocuments, this is not exhaustive, and you might be using other strategies to map your types. Using the**Send feedback** button below, let us know what strategies you use for mapping other types ofCloud Firestoredata or representing data in Swift.

There really is no reason for not usingCloud Firestore's Codable support.