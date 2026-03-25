# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/data-objects/swift-crud-database-operations.md

---
title: Basic Operations
slug: docs/ios/parse-swift-sdk/data-objects/swift-crud-database-operations
description: In this guide you learn how to use the iOS SDK to saving, retrieving, updating and deleting objects
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T10:53:23.083Z
updatedAt: 2025-01-16T20:58:53.333Z
---

# CRUD Parse objects in iOS

## Introduction

Storing data on Parse is built around the Parse.Object class. Each Parse.Object contains key-value pairs of JSON-compatible data. This data is schemaless, which means that you don’t need to specify ahead of time what keys exist on each Parse.Object. You can simply set whatever key-value pairs you want, and our backend will store it.

You can also specify the datatypes according to your application needs and persist types such as number, boolean,string, DateTime, list, GeoPointers, and Object, encoding them to JSON before saving. Parse also supports store and query relational data by using the types Pointers and Relations.

In this guide, you will learn how to perform basic data operations through a CRUD example app (ToDo list App), which will show you how to create, read, update and delete data from your Parse server database using the ParseSwift SDK.

This tutorial uses a basic app created in Xcode 12 and **iOS 14**.

:::hint{type="success"}
At any time, you can access the complete Project via our GitHub repositories.

- [**iOS Example Repository**](https://github.com/templates-back4app/ios-crud-to-do-list)
:::

## Goal

To learn how to perform basic database operations on back4app using a ToDo list app as an example

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- Xcode.
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK (Swift) Tutorial**](https://www.back4app.com/docs/ios/parse-swift-sdk) to create an Xcode Project connected to Back4App.
:::

## Understanding our To-do List App

To better understand the ParseSwift SDK you will perform CRUD operations on a To-do List App. The application database will have a simple task class with a title and a description (both strings). You can update each task’s title and/or description.

## Quick reference of commands we are going to use

Once an object conforms the ParseSwift protocol, it automatically implements a set of methods that will allow you to manage the object and update any changes on your Back4App Database. Given the object ToDoListItem

```swift
1   struct ToDoListItem: ParseObject {
2       ...
3    
4       /// Title for the todo item
5       var title: String?
6    
7       /// Description for the todo item
8       var description: String?
9   }
```

these methods are listed below.

:::CodeblockTabs
Create

```swift
  //Once created an instance of ToDoListItem object and set its custom properties, you can save it on your Back4App Database by calling any of the following methods
1   var newItem: ToDoIListtem
2   // newItem's properties
3
4   // Saves newItem on your Back4App Database synchronously and returns the new saved Item. It throws and error if something went wrong.
5   let savedItem = try? newItem.save()
6
7   // Saves newItem on your Back4App Database asynchronously, and passes a Result<ToDoListItem, ParseError> object to the completion block to handle the save proccess.
8   newItem.save { result in
9       // Handle the result to check the save was successfull or not
10  } 
11 
```

Read

```swift
//For reading objects stored on your Back4App Database, ToDoListItem now provides the query() static method which returns a Query<ToDoListItem>. This query object can be constructed using on or more QueryConstraint objects int he following way
1   let query = ToDoListItem.query() // A query to fetch all ToDoListItem items on your Back4App Database.
2   let query = ToDoListItem.query("title" == "Some title") // A query to fetch all ToDoListItem items with title "Some title" on your Back4App Database.
3   let query = ToDoListItem.query(["title" == "Some title", "description" = "Ok"]) // A query to fetch all ToDoListItem items with title = "Some title" and description = "Ok".
4
5   // Fetchs the items synchronously or throws an error if found.
6   let fetchedItems = try? query.find()
7
8   // Fetchs the items asynchronously and calls a completion block passing a result object containing the result of the operation.
9   query.find { result in
10      // Handle the result
11  }
```

Update

```swift
//Given the objectId of an object stored on you Back4App Database, you can update it in the following way
1   let itemToUpdate = ToDoListItem(objectId: "OOBJECT_ID")
2   // Update the properites of itemToUpdate
3
4   // Save changes synchronousty
5   itemToUpdate.save()
6
7   // Or save changes asynchronously
8   itemToUpdate.save { result in
9       // handle the result
10  }
```

Delete

```swift
//The deletion process is performed by calling the method delete() on the object to be deleted
1   var itemToDelete: ToDoListItem
2
3   // Delete itemToDelete synchronously
4   try? itemToDelete.delete()
5
6   // Delte itemToDelete asynchronously
7   itemToDelete.delete { result in
8       // Handleresult
9   }
```
:::

## 1 - Create To-do List App Template

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vHgxQhVfQwjNx1FCYIC30_image.png)

:::hint{type="success"}
At any time, you can access the complete Project via our GitHub repositories.

- [**iOS Example Repository**](https://github.com/templates-back4app/ios-crud-to-do-list)
:::

Go to Xcode, and find the SceneDelegate.swift file. In order to add a navigation bar on top of the app, we setup a UINavigationController as the root view controller in the following way

```swift
1   class SceneDelegate: UIResponder, UIWindowSceneDelegate {
2
3       var window: UIWindow?
4
5       func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
6           guard let scene = (scene as? UIWindowScene) else { return }
7        
8           window = .init(windowScene: scene)
9           window?.rootViewController = UINavigationController(rootViewController: ToDoListController())
10          window?.makeKeyAndVisible()
11
12          // Additional logic
13      }
14
15      ...
16  }
```

The root view controller class (ToDoListController) for the navigation controller is a subclass of UITableViewController, this makes easy to layout a list of items.

## 2 - Setup the CRUD object

Objects you want to save on your Back4App Database have to conform the ParseObject protocol. On our To-do Liat app this object is ToDoListItem. Therefore, you first need to create this object:

```swift
1   import Foundation
2   import ParseSwift
3
4   struct ToDoListItem: ParseObject {
5       // Required properties from ParseObject protocol
6       var objectId: String?
7       var createdAt: Date?
8       var updatedAt: Date?
9       var ACL: ParseACL?
10    
11      /// Title for the todo item
12      var title: String?
13    
14      /// Description for the todo item
15      var description: String?
16  }
```

This object defines a class in your Back4App Database. Any new instance of this object is then stored in your database under the ToDoListItem class.

## 3 - Setup ToDoListController

In ToDoListController we should implement all the necessary configuration for the navigationBar, and tableView properties

```swift
1   class ToDoListController: UITableViewController {    
2       var items: [ToDoListItem] = []
3    
4       override func viewDidLoad() {
5           super.viewDidLoad()
6        
7           setupTableView()
8           setupNavigationBar()
9       }
10    
11      private func setupNavigationBar() {
12          navigationItem.title = "To-do list".uppercased()
13          navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .add, target: self, action: #selector(handleNewItem))
14      }
15    
16      private func setupTableView() {
17          tableView.register(ToDoListItemCell.self, forCellReuseIdentifier: ToDoListItemCell.identifier)
18      }
19
20      override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
21          items.count
22      }
23    
24      override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
25          let cell = tableView.dequeueReusableCell(withIdentifier: ToDoListItemCell.identifier, for: indexPath) as! ToDoListItemCell
26          cell.item = items[indexPath.row]
27          return cell
28      }
29
30      /// This method is called when the user wants to add a new item to the to-do list
31      @objc private func handleNewItem() {
32          ...
33      }
34
35      ...
36  }
```

To conclude this step, we implement the custom table view cell ToDoListItemCell

```swift
1   // Content of ToDoListItemCell.swift file
2   class ToDoListItemCell: UITableViewCell {
3       class var identifier: String { "\(NSStringFromClass(Self.self)).identifier" } // Cell's identifier
4    
5       /// When set, it updates the title and detail texts of the cell
6       var item: ToDoListItem? {
7           didSet {
8               textLabel?.text = item?.title
9               detailTextLabel?.text = item?.description
10          }
11      }
12    
13      override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
14          super.init(style: .subtitle, reuseIdentifier: reuseIdentifier)
15          
16          accessoryType = .detailButton // This accessory button will be used to present edit options for the item
17      }
18    
19      required init?(coder: NSCoder) {
20          super.init(coder: coder)
21        
22          accessoryType = .detailButton // This accessory button will be used to present edit options for the item
23      }
24  }
```

## 4 - CRUD flow

We implement all CRUD logic in the ToDoListController class. Go to ToDoListController.swift and add the following methods to the ToDoListController class

```swift
1   // MARK: - CRUD Flow
2   extension ToDoListController {
3       /// Creates a ToDoListItem and stores it on your Back4App Database
4       /// - Parameters:
5       ///   - title: The title for the to-do task
6       ///   - description: An optional description for the to-to task
7       func createObject(title: String, description: String?) {
8
9       }
10    
11      /// Retrieves all the ToDoListItem objects from your Back4App Database
12      func readObjects() {
13
14      }
15    
16      /// Updates a ToDoListItem object on your Back4App Database
17      /// - Parameters:
18      ///   - objectId: The object id of the ToDoListItem to update
19      ///   - newTitle: New title for the to-to task
20      ///   - newDescription: New description for the to-do task
21      func updateObject(objectId: String, newTitle: String, newDescription: String?) {
22
23      }
24    
25      /// Deletes a ToDoListItem on your Back4App Database
26      /// - Parameter item: The item to be deleted on your Back4App Database
27      func deleteObject(item: ToDoListItem) {
28
29      }
30  }
```

**- Create Object**

Now we start implementing the createObject(title\:description:) method. Create an instance of ToDoListItem using the init(title\:description:) initializer. In order to save this new item on your Back4App Database, the ParseSwift protocol provides a save() method. This method can be called synchronously or asynchronously, choose one of them according to your use case. An asynchrononous implementation should look like this

```swift
1   func createObject(title: String, description: String?) {
2       let item = ToDoListItem(title: title, description: description)
3        
4       item.save { [weak self] result in
5           guard let self = self else { return }
6           switch result {
7           case .success(let savedItem):
8               self.items.append(savedItem)
9               DispatchQueue.main.async {
10                  self.tableView.insertRows(at: [IndexPath(row: self.items.count - 1, section: 0)], with: .right)
11              }
12          case .failure(let error):
13              DispatchQueue.main.async {
14                  self.showAlert(title: "Error", message: "Failed to save item: \(error.message)")
15              }
16          }
17      }
18  }
```

Now we can complete the action for the add button located at the right side of the navigation bar. Go toToDoListController and add the following

```swift
1   class ToDoListController: UITableViewController {
2       enum ItemDescription: Int { case title = 0, description = 1 }
3
4       ...
5
6       /// This method is called when the user wants to add a new item to the to-do list
7       @objc private func handleNewItem() {
8           showEditController(item: nil)
9       }
10    
11      /// Presents an alert where the user enters a to-do task for either create a new one (item parameter is nil) or edit an existing one
12      private func showEditController(item: ToDoListItem?) {
13          let controllerTitle: String = item == nil ? "New item" : "Update item"
14        
15          let editItemAlertController = UIAlertController(title: controllerTitle, message: nil, preferredStyle: .alert)
16        
17          editItemAlertController.addTextField { textField in
18              textField.tag = ItemDescription.title.rawValue
19              textField.placeholder = "Title"
20              textField.text = item?.title
21          }
22
23          editItemAlertController.addTextField { textField in
24              textField.tag = ItemDescription.description.rawValue
25              textField.placeholder = "Description"
26              textField.text = item?.description
27          }
28        
29          let mainActionTitle: String = item == nil ? "Add" : "Update"
30        
31          let mainAction: UIAlertAction = UIAlertAction(title: mainActionTitle, style: .default) { [weak self] _ in
32              guard let title = editItemAlertController.textFields?.first(where: { $0.tag == ItemDescription.title.rawValue })?.text else {
33                  return editItemAlertController.dismiss(animated: true, completion: nil)
34              }
35            
36              let description = editItemAlertController.textFields?.first(where: { $0.tag == ItemDescription.description.rawValue })?.text
37            
38              editItemAlertController.dismiss(animated: true) {
39                  if let objectId = item?.objectId { // if the item passed as parameter is not nil, the alert will update it
40                      self?.updateObject(objectId: objectId, newTitle: title, newDescription: description)
41                  } else {
42                      self?.createObject(title: title, description: description)
43                  }
44              }
45          }
46                
47          let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: nil)
48        
49          editItemAlertController.addAction(mainAction)
50          editItemAlertController.addAction(cancelAction)
51
52          present(editItemAlertController, animated: true, completion: nil)
53      }
54  }
```

**- Read Object**

We move to the readObjects() method. Retreiveing ToDoListItem items from your Back4App Database is performed via a Query\<ToDoListItem> object. This query is instanciated in the following way

```swift
1   func readObjects() {
2       let query = ToDoListItem.query()
3       ...
4   }
```

In this tutorial we use a query which will retreive all the items of type ToDoListItem from your Back4App Database. In case you want to retreive a set of specific items, you can provide QueryConstraint elements to ToDoListItem.query(QueryConstraint...). For instance, to fetch all items where title == "Some title", the query takes the form

```swift
1   let query = ToDoListItem.query("title" == "Some title")
```

Once you have the query ready, we proceed to retreive the items by callingquery.find(). Again, this can be done synchronously or asynchronously. In our To-do List app we implement it asynchronously

```swift
1   func readObjects() {
2       let query = ToDoListItem.query()
3        
4       query.find { [weak self] result in
5           guard let self = self else { return }
6           switch result {
7           case .success(let items):
8               self.items = items
9               DispatchQueue.main.async {
10                  self.tableView.reloadSections([0], with: .top)
11              }
12          case .failure(let error):
13              DispatchQueue.main.async {
14                  self.showAlert(title: "Error", message: "Failed to save item: \(error.message)")
15              }
16          }
17      }
18  }
```

With readObjects() completed, we can now fetch all the tasks stored in your Back4App Database and show them right after the app enters to foreground. Go back to ToDoListController and override the viewDidAppear() method

```swift
1   class ToDoListController: UITableViewController {
2       ...
3    
4       override func viewDidAppear(_ animated: Bool) {
5           super.viewDidAppear(animated)
6        
7           readObjects()
8       }
9
10      ...
11  }
```

**- Update object**

Given the objectId of a ToDoListItem object, it is straightforward to perform an update. We simply instanciate a ToDoListItem object using the init(objectId:) initializer. Next, we update the properties we need and call the save() method (of ToDoListItem) to save changes

```swift
1   func updateObject(objectId: String, newTitle: String, newDescription: String?) {
2       var item = ToDoListItem(objectId: objectId)
3       item.title = newTitle
4       item.description = newDescription
5        
6       item.save { [weak self] result in
7           switch result {
8           case .success:
9               if let row = self?.items.firstIndex(where: { $0.objectId == item.objectId }) {
10                  self?.items[row] = item
11                  DispatchQueue.main.async {
12                      self?.tableView.reloadRows(at: [IndexPath(row: row, section: 0)], with: .fade)
13                  }
14              }
15          case .failure(let error):
16              DispatchQueue.main.async {
17                  self?.showAlert(title: "Error", message: "Failed to save item: \(error.message)")
18              }
19          }
20      }
21  }
```

**- Delete object**

Deleting objects on your Back4App Database is very similar to creating objects. We begin by creating an instance of ToDoListItem with the objectId of the item we want to delete. Next, we simply call (synchronously or ascynchronously) the delete() method of the object. If the deletion was successfull we update the UI, otherwise we report the error

```swift
1   func deleteObject(item: ToDoListItem) {
2       item.delete { [weak self] result in
3           switch result {
4           case .success:
5               if let row = self?.items.firstIndex(where: { $0.objectId == item.objectId }) {
6                   self?.items.remove(at: row)
7                   DispatchQueue.main.async {
8                       self?.tableView.deleteRows(at: [IndexPath(row: row, section: 0)], with: .left)
9                   }
10              }
11          case .failure(let error):
12              DispatchQueue.main.async {
13                  self?.showAlert(title: "Error", message: "Failed to save item: \(error.message)")
14              }
15          }
16      }
17  }
```

With deleteObject(item:) and updateObject(objectId\:newTitle\:newDescription) completed, we proceed to add the corresponding actions to call these operations. Go back to ToDoListController and add

```swift
1   // MARK: UITableViewDataSource delegate
2   extension ToDoListController {
3       // When the user taps on the accessory button of a cell, we present the edit options for the to-do list task
4       override func tableView(_ tableView: UITableView, accessoryButtonTappedForRowWith indexPath: IndexPath) {
5           guard !items.isEmpty else { return }
6        
7           showEditOptions(item: items[indexPath.row])
8       }
9    
10      /// Presents a sheet where the user can select an action for the to-do list item
11      private func showEditOptions(item: ToDoListItem) {
12          let alertController = UIAlertController(title: title, message: nil, preferredStyle: .actionSheet)
13        
14          let editAction = UIAlertAction(title: "Edit", style: .default) { [weak self] _ in
15              self?.showEditController(item: item)
16          }
17        
18          let deleteAction = UIAlertAction(title: "Delete", style: .destructive) { [weak self] _ in
19              alertController.dismiss(animated: true) {
20                  self?.deleteObject(item: item)
21              }
22          }
23        
24          let cancelAction = UIAlertAction(title: "Cancel", style: .cancel) { _ in
25              alertController.dismiss(animated: true, completion: nil)
26          }
27        
28          alertController.addAction(editAction)
29          alertController.addAction(deleteAction)
30          alertController.addAction(cancelAction)
31
32          present(alertController, animated: true, completion: nil)
33      }
34  }
```

As we pointed out earlier, the accessory button in each ToDoListItemCell triggers an edit sheet via the tableView(\_:accessoryButtonTappedForRowWith:) delegate method.

### It’s done!

At this point, you have learned how to do the basic CRUD operations with Parse on iOS.
