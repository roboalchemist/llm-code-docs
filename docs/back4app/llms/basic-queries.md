# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/data-objects/basic-queries.md

---
title: Basic Queries
slug: docs/ios/parse-swift-sdk/data-objects/basic-queries
description: In this guide you will learn how to query data from a Back4App Database.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T12:56:24.145Z
updatedAt: 2025-01-16T20:59:07.613Z
---

## Basic Queries

### Introduction

In most use cases, we require to fetch data from a database with certain conditions. These conditions may include complex comparisons and ordering requirements. Thus, in any application, it is fundamental to construct efficient queries and, at the same time, the database has to be able to execute them as fast as possible.

The ParseSwift SDK does provide the necessary tools for you to construct any query according to the application requirements. In this tutorial, we explore these tools and use them in a real-world application.

This tutorial uses a basic app created in Xcode 12 and **iOS 14**.

:::hint{type="success"}
At any time, you can access the complete Project via our GitHub repositories.

- [**iOS Example Repository**](https://github.com/templates-back4app/ios-crud-to-do-list)
:::

## Goal

- To understand how to create basic queries to retrieve data from a Back4App Database.

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- Xcode.
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK (Swift) Tutorial**](https://www.back4app.com/docs/ios/parse-swift-sdk) to create an Xcode Project connected to Back4App.
:::

## Understanding our Constacts App

The project template is a Contacts App where the user adds a contact’s information to save it on a Back4App Database

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/B0R7v-NV5x-uLPAJ96d8r_image.png" signedSrc size="50" width="1242" height="2208" position="center" caption}

On the app’s homescreen you will find a set of buttons for different types of queries. Using the + button located on the top-right side of the navigation bar, we can add as many Contacts as needed.

## Quick reference of commands we are going to use

For this example, we use the object Contact

```swift
1   import Foundation
2   import ParseSwift
3
4   struct Contact: ParseObject {
5       // Required properties from ParseObject protocol
6       var originalData: Data?
7       var objectId: String?
8       var createdAt: Date?
9       var updatedAt: Date?
10      var ACL: ParseACL?
11    
12      // Custom fields for the contact's information
13      var name: String?
14      var birthday: Date?
15      var numberOfFriends: Int?
16      var favoriteFoods: [String]?
17    
18      ...
19  }
```

The following methods will allows us to save and queryContactobjects:

:::CodeblockTabs
Create contact

```swift
//When creating and saving a new instance of Contact we can use
1   var newContact: Contact = Contact(name: "John Doe", birthday: Date(), numberOfFriends: 5, favoriteFoods: ["Bread", "Pizza"])
2
3   // Saves newContact on your Back4App Database synchronously and returns the new saved Item. It throws and error if something went wrong.
4   let savedContact = try? newContact.save()
5
6   // Saves newContact on your Back4App Database asynchronously, and passes a Result<Contact, ParseError> object to the completion block to handle the save process.
7   newContact.save { result in
8       // Handle the result to check wether the save process was successfull or not
9   }
```

Query all

```swift
//For retrieving all the Contact items saved on a Back4App Database, we construct a Query<Contact> object and call the find() method on it
1   let contactsQuery = Contact.query() // A query to fetch all Contact items on your Back4App Database.
2
3   // Fetches the items synchronously or throws an error if found.
4   let fetchedContacts = try? query.find()
5
6   // Fetches the items asynchronously and calls a completion block passing a result object containing the result of the operation.
7   query.find { result in
8       // Handle the result
9   }
```

Query by name

```swift
//In order to create a query with a specific condition, we use the static method query(_:) provided by the ParseObject protocol. We pass a QueryConstraint object to the method as a parameter. This QueryConstraint object represents the type of constraint we are imposing on the query. For queries involving comparison constraints, the ParseSwift SDK provides the following methods to create them
1   import ParseSwift
2
3   // A constraint to retreive all Contact items that have exactly the string 'Jhon Doe' in their 'name' field
4   let constraint1 = try? equalTo(key: "name", value: "John Doe")
5
6   // An operator-like implementation for the equalTo(key:value:) method
7   let constraint2: QueryConstraint = "name" == "Jhon Doe"
8
9   // A constraint to retrieve all Contact items that have the string 'John' in their 'name' field (only workd with String-type fields)
10  let constraint3: QueryConstraint = containsString(key: "name", substring: "Jhon")
11
12  let query = Contact.Query(constrint1) // Depending on your use case, you can send any of the above constraints as parameter
13
14  // Executes the query synchronously. It throws an error if something happened
15  let fetchedContacts = try? query.find()
16
17  // Executes que query asynchronously and returns a Result<[Contact], ParseError> object with the result
18  query.find() { result in
19      // Handle the result
20  }
```

Query by friend count

```swift
//When we want to query contacts which have a certain amount of friends or more, we do it in the following way
1   import ParseSwift
2
3   // A constraint to retrieve all Contact items that have 30 or more number of friends
4   let constraint1: QueryConstraint = "numberOfFriends" >= 30
5
6   // A constraint to retrieve all Contact items that have more than 30 number of friends
7   let constraint2: QueryConstraint = "numberOfFriends" > 30
8
9   let query = Contact.query(constraint1) // Depending on your use case, you can send any of the above constraints as parameter
10
11  // Executes the query synchronously. It throws an error if something happened
12  let fetchedContacts = try? query.find()
13
14  // Executes que query asynchronously and returns a Result<[Contact], ParseError> object with the result
15  query.find() { result in
16       // Handle the result
17  }
```

Query with ordering

```swift
//Adding an ordering option to queries is straightforward. Any Query<Contact> object has the order(_:) method to do so. A simple query using the birthday as descending order can be implemented in the folowing way
1   import ParseSwift
2
3   // A query without order to retrieve all the Contact items
4   let unorderedQuery = Contact.query()
5
6   // Sorts the result by the brithday field. The parameter in the enumeration is the key of the field used to order the results
7   let descendingOrder = Query<Contact>.Order.descending("birthday")
8
9   let orderedQuery = unorderedQuery.order([descendingOrder]) // Returns a new query with the requested (descending) ordering option
10
11  // Executes the query synchronously. It throws an error if something happened
12  let orderedContacts = try? orderedQuery.find()
13
14  // Executes que query asynchronously and returns a Result<[Contact], ParseError> object with the result
15  orderedContacts.find() { result in
16      // Handle the result
17  }
```
:::

## 1 - Download the Contacts App Template

The XCode project has the following structure

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/63yY4ygI7vQ4MRHG4U8h4_image.png)

:::hint{type="success"}
At any time, you can access the complete Project via our GitHub repositories.

- [**iOS Example Repository**](https://github.com/templates-back4app/ios-crud-to-do-list)
:::

To focus on the main objective of this guide, we will only detail the sections strictly related to queries and the **ParseSwift SDK**.

## 2 - Additional CRUD flow

Before getting started with queries, it is necessary to have some contacts already saved on your Back4App Database. In the NewContactController class, we implement a basic form to add a Contact. To save an instance of a Contact object, we use the handleAddContact() method implemented in the NewContactController class

```swift
1   // NewContactController.swift file
2   ...
3
4   extension NewContactController {
5       /// Retrieves the info the user entered for a new contact and stores it on your Back4App Database
6       @objc fileprivate func handleAddContact() {
7           view.endEditing(true)
8        
9           // Collect the contact's information from the form
10          guard let name = nameTextField.text,
11                let numberOfFriendsString = numberOfFriendsTextField.text,
12                let numberOfFriends = Int(numberOfFriendsString),
13                let favoriteFoods = favoriteFoodsTextField.text?.split(separator: ",") else {
14              return showAlert(title: "Error", message: "The data you entered is con valid.")
15          }
16        
17          // Once the contact's information is collected, instantiate a Contact object to save it on your Back4App Database
18          let contact = Contact(
19              name: name,
20              birthday: birthdayDatePicker.date,
21              numberOfFriends: numberOfFriends,
22              favoriteFoods: favoriteFoods.compactMap { String($0).trimmingCharacters(in: .whitespaces) }
23          )
24        
25          // Save the new Contact
26          contact.save { [weak self] result in
27              switch result {
28              case .success(_):
29                  self?.showAlert(title: "Success", message: "Contact saved.") {
30                      self?.dismiss(animated: true, completion: nil)
31                  }
32              case .failure(let error):
33                  self?.showAlert(title: "Error", message: "Failed to save contact: \(error.message)")
34              }
35          }
36      }
37  }
```

:::hint{type="success"}
For more details about this step, you can go to the [**basic operations guide**](https://www.back4app.com/docs/ios/parse-swift-sdk/data-objects/swift-crud-database-operations).
:::

## 3 - Performing basic queries

**- By name**

The first example we look at is a query that allows us to retrieve contacts which have a specific substring in their name field. In order to do this, we first create a QueryConstraint object. This object will contain the constraint we want. The ParseSwift SDK provides the following methods to (indirectly) create a QueryConstraint

```swift
1   // QueryConstraint.swift file
2
3   /**
4     Add a constraint for finding string values that contain a provided substring.
5     - warning: This will be slow for large datasets.
6     - parameter key: The key that the string to match is stored in.
7     - parameter substring: The substring that the value must contain.
8     - parameter modifiers: Any of the following supported PCRE modifiers (defaults to nil):
9       - `i` - Case insensitive search
10      - `m` - Search across multiple lines of input
11    - returns: The resulting `QueryConstraint`.
12   */
13  public func containsString(key: String, substring: String, modifiers: String? = nil) -> QueryConstraint
14
15  /**
16   Add a constraint that requires that a key is equal to a value.
17   - parameter key: The key that the value is stored in.
18   - parameter value: The value to compare.
19   - returns: The same instance of `QueryConstraint` as the receiver.
20   - warning: See `equalTo` for more information.
21   Behavior changes based on `ParseSwift.configuration.isUsingEqualQueryConstraint`
22   where isUsingEqualQueryConstraint == true is known not to work for LiveQuery on
23   Parse Servers  <= 5.0.0.
24   */
25  public func == <T>(key: String, value: T) -> QueryConstraint where T: Encodable
```

For instance, a query that allows us to retrieve all the Contact’s with **John** in their name field can be created with

```swift
1   // Create the query sending the constraint as parameter
2   let constraint: QueryConstraint = containsString(key: "name", substring: "John") // The first parameter (key) referres to the name of the field
3   let query = Contact.query(constrain)
4
5   // Retrieve the contacts asynchronously (or sinchronously if needed)
6   query.find() { result in
7       // Handle the result and do the corresponding UI update
8   }
```

In case the constraint requires the name field to match exactly a given string, we can use

```swift
1   // Create the query sending the constraint as parameter
2   let value = "John"
3   let constraint: QueryConstraint = "name" == value
4   let query = Contact.query(constrain)
```

**- By number of friends**

A query with a constraint involving a numerical comparison can be constructed by creating aQueryConstraint with

```swift
1   /**
2    Add a constraint that requires that a key is greater than a value.
3    - parameter key: The key that the value is stored in.
4    - parameter value: The value to compare.
5    - returns: The same instance of `QueryConstraint` as the receiver.
6    */
7   public func > <T>(key: String, value: T) -> QueryConstraint where T: Encodable
8
9   /**
10   Add a constraint that requires that a key is greater than or equal to a value.
11   - parameter key: The key that the value is stored in.
12   - parameter value: The value to compare.
13   - returns: The same instance of `QueryConstraint` as the receiver.
14   */
15  public func >= <T>(key: String, value: T) -> QueryConstraint where T: Encodable
16
17  /**
18   Add a constraint that requires that a key is less than a value.
19   - parameter key: The key that the value is stored in.
20   - parameter value: The value to compare.
21   - returns: The same instance of `QueryConstraint` as the receiver.
22   */
23  public func < <T>(key: String, value: T) -> QueryConstraint where T: Encodable
24
25  /**
26   Add a constraint that requires that a key is less than or equal to a value.
27   - parameter key: The key that the value is stored in.
28   - parameter value: The value to compare.
29   - returns: The same instance of `QueryConstraint` as the receiver.
30   */
31  public func <= <T>(key: String, value: T) -> QueryConstraint where T: Encodable

```

To query all contacts with 30 or more friends, we use

```swift
1   let query = Contacts.query("numberOfFriends" >= 30)
2
3   // Retrieve the contacts asynchronously (or sinchronously if needed)
4   query.find() { result in
5       // Handle the result and do the corresponding UI update
6   }
```

**- Ordering query results**

For ordering the results from a query, the Query\<contacts> object provides the method order(\_:) which returns a new Query\<contact> object considering the requested ordering option. As a parameter, we pass an enumeration (Query\<contact>.Order) to indicate the ordering we want. The following snippet applies a descending order based on the birthday field

```swift
1   // A query without order to retrieve all the Contact items
2   let unorderedQuery = Contact.query()
3
4   // Sorts the contacts based on their brithday. The parameter in the enumeration is the key of the field used to order the results
5   let descendingOrder = Query<Contact>.Order.descending("birthday")
6
7   let orderedQuery = unorderedQuery.order([descendingOrder]) // Returns a new query with the requested (descending) ordering option
8
9   // Executes que query asynchronously and returns a Result<[Contact], ParseError> object with the result
10  orderedContacts.find() { result in
11      // Handle the result
12  }
```

In the [**project example**](https://github.com/templates-back4app/ios-basic-queries-example), we implemented the queries mentioned above. The ContactsController class has the method fetchContacts() where you will find the following snippet&#x20;

```swift
1   ...
2
3   class ContactsController {
4       let queryType: QueryType
5
6       ...
7
8       private func fetchContacts() {
9           // We create a Query<Contact> according to the queryType enumeration
10          let query: Query<Contact> = {
11              switch queryType {
12              case .byName(let value):
13                  return Contact.query(containsString(key: "name", substring: value))
14              case .byNumberOfFriends(let quantity):
15                  return Contact.query("numberOfFriends" >= quantity)
16              case .byOrdering(let order):
17                  let query = Contact.query()
18                  switch order {
19                  case .ascending: return query.order([.ascending("birthday")])
20                  case .descending: return query.order([.descending("birthday")])
21                  }
22              case .all:
23                  return Contact.query()
24              }
25          }()
26        
27          // Execute the query
28          query.find { [weak self] result in
29              switch result {
30              case .success(let contacts):
31                  self?.contacts = contacts
32                
33                  // Update the UI
34                  DispatchQueue.main.async { self?.tableView.reloadData() }
35              case .failure(let error):
36                  // Notify the user about the error that happened during the fetching process
37                  self?.showAlert(title: "Error", message: "Failed to retrieve contacts: \(error.message)")
38                  return
39              }
40          }
41      }
42  }
```

## 4 - Run the app!

:::hint{type="info"}
Before pressing the run button on XCode, do not forget to configure your Back4App application in the AppDelegate class!
:::

Using the+button in the navigation bar, add a counple of contacts and test the different queries.
