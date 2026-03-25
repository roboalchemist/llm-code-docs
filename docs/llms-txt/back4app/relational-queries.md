# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/data-objects/relational-queries.md

---
title: Relational Queries
slug: docs/ios/parse-swift-sdk/data-objects/relational-queries
description: In this guide, you will learn how to perform relational data querying in ParseSwift on an iOS application
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T14:51:43.599Z
updatedAt: 2025-01-16T20:59:14.760Z
---

# Relational Queries

## Introduction

In the [**previous guide**](https://www.back4app.com/docs/ios/parse-swift-sdk/data-objects/query-cookbook) we detailed how we can perform miscellaneous queries on a Back4App Database. In this guide we focus on a specific type of query that involves objects with relations.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An App [**created on Back4App**](https://www.back4app.com/docs/get-started/new-parse-app).
- A basic iOS App to test queries
:::

## Goal

Query relational data stored on a Back4App Database using the ParseSwift SDK.

## 1 - Quick review about the Query\<U>class

Any query performed on a Back4App Database is done via the generic class Query\<U>. The generic parameter U (conforming to the ParseObject protocol) is the data type of the objects we are trying to retrieve from the database.

Given a data type like MyObject, we retrieve these objects from a Back4App Database in the following way

```swift
1   import ParseSwift
2
3   struct MyObject: ParseObject {
4     ...
5   }
6
7   let query = MyObject.query()
8
9   // Executes the query asynchronously
10  query.find { result in
11    // Handle the result (of type Result<[MyObject], ParseError>)
12  }
```

You can read more about the Query\<U> class [**here at the official documentation**](https://github.com/parse-community/Parse-Swift).&#x20;

## 2 - Save some data on a Back4App Database

Before we begin to execute queries, it is necessary to set up some data on a Back4App Database. We will store five types of objects:

:::CodeblockTabs
Author

```swift
1   struct Author: ParseObject {
2     ...
3     var name: String?
4   }
```

Book

```swift
1   struct Book: ParseObject {
2     ...
3     var title: String?
4     var publisher: Publisher?
5     var publishingDate: Date?
6   }
```

ISBD

```swift
1   struct ISBD: ParseObject {
2     ...
3     var isbn: String?
4     var book: Pointer<Book>?
5   }
```

Publisher

```swift
1   struct Publisher: ParseObject {
2     ...
3     var name: String?
4   }
```

BookStore

```swift
1   struct BookStore: ParseObject {
2     ...
3     var name: String?
4   }
```
:::

Additionally, in order to construct queries for relational data, we will implement the following relations

- **1:1&#x20;**&#x72;elation between Book and ISBD.
- **1\:N&#x20;**&#x72;elation between Book and Publisher.
- **M\:N&#x20;**&#x72;elation between Book and Author.
- **M\:N&#x20;**&#x72;elation between BookStore and Book.

We now proceed to store some data on the Back4App Database. This step can be implemented using Swift or directly from your app’s console on the Back4App platform.

:::CodeblockTabs
Swift

```swift
//After setting up your XCode project, calling the following method should save some sample data on your Back4App Database
1   import ParseSwift
2
3   func saveSampleData() {
4     do {
5       // Authors
6       let aaronWriter = try Author(name: "Aaron Writer").save()
7       let beatriceNovelist = try Author(name: "Beatrice Novelist").save()
8       let caseyColumnist = try Author(name: "Casey Columnist").save()
9            
10      // Publishers
11      let acaciaPublishings = try Publisher(name: "Acacia Publishings").save()
12      let birchDistributions = try Publisher(name: "Birch Distributions").save()
13            
14      // Books with their corresponding ISBD
15      let aLoveStoryBook = try Book(
16        title: "A Love Story",
17        publisher: acaciaPublishings,
18        publishingDate: Date(string: "05/07/1998")
19      ).save()
20      .relation?.add("authors", objects: [aaronWriter]).save() // Establishes the M:N relatin between Book and Author
21
22      // Fetches the ISBD associated to aLoveStoryBook and establishes the 1:1 relation
23      if let book = aLoveStoryBook, var isbd = try book.fetch(includeKeys: ["isbd"]).isbd  {
24        isbd.book = try Pointer<Book>(book)
25        _ = try isbd.save()
26      } else {
27        fatalError()
28      }
29            
30      let benevolentElvesBook = try Book(
31        title: "Benevolent Elves",
32        publisher: birchDistributions,
33        publishingDate: Date(string: "11/30/2008")
34      ).save()
35      .relation?.add("authors", objects: [beatriceNovelist]).save() // Establishes the M:N relatin between Book and Author
36
37      // Fetches the ISBD associated to benevolentElvesBook and establishes the 1:1 relation
38      if let book = benevolentElvesBook, var isbd = try book.fetch(includeKeys: ["isbd"]).isbd  {
39        isbd.book = try Pointer<Book>(book)
40        _ = try isbd.save()
41      } else {
42        fatalError()
43      }
44             
45      let canYouBelieveItBook = try Book(
46        title: "Can You Believe It",
47        publisher: birchDistributions,
48        publishingDate: Date(string: "08/21/2018")
49      ).save()
50      .relation?.add("authors", objects: [aaronWriter, caseyColumnist]).save() // Establishes the M:N relatin between Book and Author
51
52      // Fetches the ISBD associated to canYouBelieveItBook and establishes the 1:1 relation
53      if let book = canYouBelieveItBook, var isbd = try book.fetch(includeKeys: ["isbd"]).isbd  {
54        isbd.book = try Pointer<Book>(book)
55        _ = try isbd.save()
56      } else {
57        fatalError()
58      }
59
60      // Book store
61      guard let safeALoveStoryBook = aLoveStoryBook,
62            let safeBenevolentElvesBook = benevolentElvesBook,
63            let safeCanYouBelieveItBook = canYouBelieveItBook
64      else {
65        throw NSError(
66          domain: Bundle.main.description,  
67          code: 0,
68          userInfo: [NSLocalizedDescriptionKey: "Failed to unwrapp stored books."]
69        )
70      }
71
72      // Saves the stores together with their 1:N relation with Book's 
73      let booksOfLove = try BookStore(name: "Books of Love").save()
74      _ = try booksOfLove.relation?.add("books", objects: [safeALoveStoryBook]).save()
75              
76      let fantasyBooks = try BookStore(name: "Fantasy Books").save()
77      _ = try fantasyBooks.relation?.add("books", objects: [safeBenevolentElvesBook]).save()
78              
79      let generalBooks = try BookStore(name: "General Books").save()
80      _ = try generalBooks.relation?.add("books", objects: [safeALoveStoryBook, safeCanYouBelieveItBook]).save()
81            
82    } catch let error as ParseError {
83      print("ERROR:\n", error.message)
84    } catch {
85      print("ERROR:\n", error.localizedDescription)
86    }
87  }
```

Back4App's console

```swift
//A quick way to insert elements on your Back4App Database is via the console located in your App’s API section. Once you are there, you can start running Javascript code to save the sample data
1   // Authors
2   const aaronWriter = new Parse.Object('Author');
3   aaronWriter.set('name', 'Aaron Writer');
4   await aaronWriter.save();
5
6   const beatriceNovelist = new Parse.Object('Author');
7   beatriceNovelist.set('name', 'Beatrice Novelist');
8   await beatriceNovelist.save();
9
10  const caseyColumnist = new Parse.Object('Author');
11  caseyColumnist.set('name', 'Casey Columnist');
12  await caseyColumnist.save();
13
14  // Publishers
15  const acaciaPublishings = new Parse.Object('Publisher');
16  acaciaPublishings.set('name', 'Acacia Publishings');
17  await acaciaPublishings.save();
18
19  const birchDistributions = new Parse.Object('Publisher');
20  birchDistributions.set('name', 'Birch Distributions');
21  await birchDistributions.save();
22
23  // Books with their corresponding ISBD
24  const aLoveStoryISBD = new Parse.Object('ISBD');
25  aLoveStoryISBD.set('isbn', '9781401211868');
26  await aLoveStoryISBD.save();
27
28  const aLoveStoryBook = new Parse.Object('Book');
29  aLoveStoryBook.set('title', 'A Love Story');
30  aLoveStoryBook.set('publisher', acaciaPublishings);
31  aLoveStoryBook.set('publishingDate', new Date('05/07/1998'));
32  aLoveStoryBook.set('isbd', aLoveStoryISBD);
33  const bookARelation = aLoveStoryBook.relation("authors");
34  bookARelation.add(aaronWriter);
35  await aLoveStoryBook.save();
36  aLoveStoryISBD.set('book', aLoveStoryBook.toPointer());
37  await aLoveStoryISBD.save();
38
39  const benevolentElvesISBD = new Parse.Object('ISBD');
40  benevolentElvesISBD.set('isbn', '9781401211868');
41  await benevolentElvesISBD.save();
42
43  const benevolentElvesBook = new Parse.Object('Book');
44  benevolentElvesBook.set('title', 'Benevolent Elves');
45  benevolentElvesBook.set('publisher', birchDistributions);
46  benevolentElvesBook.set('publishingDate', new Date('11/31/2008'));
47  benevolentElvesBook.set('isbd', benevolentElvesISBD);
48  const bookBRelation = benevolentElvesBook.relation("authors");
49  bookBRelation.add(beatriceNovelist);
50  await benevolentElvesBook.save();
51  benevolentElvesISBD.set('book', benevolentElvesBook.toPointer());
52  await benevolentElvesISBD.save();
53  
54  const canYouBelieveItISBD = new Parse.Object('ISBD');
55  canYouBelieveItISBD.set('isbn', '9781401211868');
56  await canYouBelieveItISBD.save();
57
58  const canYouBelieveItBook = new Parse.Object('Book');
59  canYouBelieveItBook.set('title', 'Can You Believe It?');
60  canYouBelieveItBook.set('publisher', birchDistributions);
61  canYouBelieveItBook.set('publishingDate', new Date('08/21/2018'));
62  canYouBelieveItBook.set('isbd', canYouBelieveItISBD);
63  const bookCRelation = canYouBelieveItBook.relation("authors");
64  bookCRelation.add(aaronWriter);
65  bookCRelation.add(caseyColumnist);
66  await canYouBelieveItBook.save();
67  canYouBelieveItISBD.set('book', canYouBelieveItBook.toPointer());
68  await canYouBelieveItISBD.save();
69
70  // Book store
71  const booksOfLoveStore = new Parse.Object('BookStore');
72  booksOfLoveStore.set('name', 'Books of Love');
73  const bookStoreARelation = booksOfLoveStore.relation("books");
74  bookStoreARelation.add(aLoveStoryBook);
75  await booksOfLoveStore.save();
76
77  const fantasyBooksStore = new Parse.Object('BookStore');
78  fantasyBooksStore.set('name', 'Fantasy Books');
79  const bookStoreBRelation = fantasyBooksStore.relation("books");
80  bookStoreBRelation.add(benevolentElvesBook);
81  await fantasyBooksStore.save();
82
83  const generalBooksStore = new Parse.Object('BookStore');
84  generalBooksStore.set('name', 'General Books');
85  const bookStoreCRelation = generalBooksStore.relation("books");
86  bookStoreCRelation.add(aLoveStoryBook);
87  bookStoreCRelation.add(canYouBelieveItBook);
88  await generalBooksStore.save();
```
:::

## 3 - Query the data

Once the database has some sample data to work with, we start executing the different kinds of queries associated with the relations detailed earlier.

**Queries involving 1:1 relations**

Given two data types sharing a **1:1** relation (Book and ISBD in this case), we can retrieve one from the other as follows. The way we implemented the relation in Book allows us to retrieve its related ISBD object simply by calling the include(\_:) method on the query. Let us retrieve the ISBD from the book **A Love Story**:

```swift
1   let aLoveStoryBookQuery = Book.query("title" == "A Love Story").include("isbd") // Note how we include the ISBD with the include(_:) method
2
3   let book = try? aLoveStoryBookQuery.first() // Retrieves synchronously the book including its ISBD
4
5   aLoveStoryBookQuery.first { result in // Retrieves asynchronously the book including its ISBD
6     // Handle the result (of type Result<Book, ParseError>)
7   }
```

On the other hand, a query to retrieve a Book object related to a given ISBD is implemented in the following way. By looking at the implementation of ISBD, we note that the relation is represented by the book property (of type Pointer\<book>). This pointer provides a set of methods and properties to retrieve information about the object it points to. In particular, we call the fetch(...) method on the book property to fetch the associated Book

```swift
1   let someISBD: ISBD
2
3   let book: Book? = try? someISBD.book?.fetch() // Retrieves synchronously the book asscociated to someISBD
4
5   someISBD.book?.fetch { result in // Retrieves asynchronously the book asscociated to someISBD
6     // Handle the result (of type Result<Book, ParseError>)
7   }
```

We should remark that this implemetation for a **1:1** relation is not unique. Depending on your use case, you can implement **1:1** relations in different ways.

**Queries involving 1\:N relations**

In a scenario where we need to query all the books published by a given publisher, we first need to retrieve the publisher. For instance, we first retrieve the data object associated with the publisher **Acacia Publishings**. Depending on the situation, this procces may vary

```swift
1   do {
2     // Using the object's objectId
3     let acaciaPublishings = try Publisher(objectId: "SOME_OBJECT_ID").fetch()
4
5     // Or
6     // Using a Query
7     let acaciaPublishings = try Publisher.query("name" == "Acacia Publishings").first() // Returns (synchronously) the first Publisher with name 'Acacia Publishings'. The constraint is constructed using the == operator provided by the ParseSwift SDK
8  
9     ... // To be completed below
10  } catch {
11  // Hanlde the error (of type ParseError)
12  }
```

Now that we have access to acaciaPublishings, we can construct the query to retrieve its related books. We proceed to create the query by instantiating a Query\<Book> class. In this case, this class is instantiated using the static method query(...) provided by the Book object. The (variadic) arguments for this method are the standard QueryConstraint objects. Therefore, the books we are looking for are retrieved with the following snippet

```swift
1   do {
2     let acaciaPublishings = try Publisher.query("name" == "Acacia Publishings").first() // Returns the first Publisher with name 'Acacia Publishings'
3
4     let constraint: QueryConstraint = try "publisher" == publisher
5     let query = Book.query(constraint) // Creates the query to retrieve all Book objects where its publisher field equalt to 'acaciaPublishings'
6
7     let books: [Book] = try query.find() // Executes the query synchronously
8
9     // books should contain only one element: the book 'A Love Story'
10  } catch {
11    // Hanlde the error (of type ParseError)
12  }
```

An asynchronous implentation for the above snippet may be written in the following way

```swift
1   // We retrieve the Publisher with name 'Acacia Publishings'
2   Publisher.query("name" == "Acacia Publishings").first { result in
3     switch result {
4     case .success(let publisher):
5       guard let constraint: QueryConstraint = try? "publisher" == publisher else { fatalError() }
6
7       // Then, we retrieve the books with the corresponding constraint          
8       Book.query(constraint).find { result in
9         switch result {
10        case .success(let books):
11          // books should contain only one element: the book 'A Love Story'
12          break
13        case .failure(let error):
14          // handle the error (of type ParseError)
15          break
16        }
17      }
18
19    case .failure(let error):
20      // handle the error (of type ParseError)
21      break
22    }
23  }
```

**Queries involving M\:N relations (Case 1)**

To illustrate this case, we consider the following scenario; we want to list all the stores containing books published after a given date (e.g., **01/01/2010**). Firstly we require an intermediate query to select the books. Next, we construct the main query to list the stores.

Therefore, we prepare the first query for the books

```swift
1   let booksQuery = Book.query("publishingDate" > Date(string: "01/01/2010")) // We construct the date constraint using the > operator provided by the ParseSwift SDK
2        
3   do {
4     let books = try booksQuery.find()
5     ... // To be completed below
6   } catch let error as ParseError {
7     // Handle any potential error
8   } catch {
9     // Handle any potential error
10  }
```

We then construct the stores’ query using booksQuery’s results. The method containedIn(\_:array:) returns the constraint we need for this case

```swift
1   let booksQuery = Book.query("publishingDate" > Date(string: "01/01/2010")) // We construct the date constraint using the > operator provided by the ParseSwift SDK
2        
3   do {
4     let books = try booksQuery.find()
5  
6     // Here is where we construct the stores' query with the corresponding constraint
7     let storesQuery = BookStore.query(try containedIn(key: "books", array: books))
8    
9     let stores = try storesQuery.find()
10    
11    // stores should containt only one element: the 'General Books' BookStore 
12  } catch let error as ParseError {
13    // Handle any potential error
14  } catch {
15    // Handle any potential error
16  }
```

Similarly, we can implement this process asynchronously

```swift
1   let booksQuery = Book.query("publishingDate" > Date(string: "01/01/2010")) // We construct the date constraint using the > operator provided by the ParseSwift SDK
2
3   booksQuery.find { result in
4     switch result {
5     case .success(let books):
6       guard let constraint = try? containedIn(key: "books", array: books) else { fatalError() }
7       let storesQuery = BookStore.query(constraint)
8                
9       storesQuery.find { result in
10        switch result {
11        case .success(let stores):
12        
13        case .failure(let error):
14          // Handle the error (of type ParseError)
15        }
16      }
17    case .failure(let error):
18      // Handle the error (of type ParseError)
19    }
20  }
```

**Queries involving M\:N relations (Case 2)**

Suppose we need to select all the stores that have books written by a given author, say, **Aaron Writer**. In order to achieve this, we require two additional queries:

- A query (Query\<Author>) to obtain the object associated with the author Aaron Writer.
- A query (Query\<Book>)to select all the books written by **Aaron Writer**.
- The main query (Query\<BookStore>) to select the stores we are looking for.

The procedure to implement these queries are very similar to the previous ones:

```swift
1   let authorQuery = Author.query("name" == "Aaron Writer") // The first query to retrieve the data object associated to 'Aaron Writer'
2
3   do {
4     let aaronWriter = try authorQuery.first()
5            
6     let booksQuery = Book.query(try containedIn(key: "authors", array: [aaronWriter])) // The second query to retrieve the books written by 'Aaron Writer'
7            
8     let books = try booksQuery.find()
9            
10    let storesQuery = BookStore.query(try containedIn(key: "books", array: books)) // The main query to select the stores where the author ('Aaron Writer') has his books available
11  
12    let stores = try storesQuery.find()
13            
14    // stores should contain two items: 'Books of Love' and 'General Books'
15  } catch let error as ParseError {
16    // Handle the error
17  } catch {
18    // Handle the error
19  }
```

## Conclusion

With the ParseSwift SDK, we were able to construct relational queries that allowed us to select items based on the type of relations they have with other data types.
