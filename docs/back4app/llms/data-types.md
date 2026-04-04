# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/data-objects/data-types.md

---
title: Data Types
slug: docs/ios/parse-swift-sdk/data-objects/data-types
description: In this guide you will lear how to store objects with different type of properties.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-11T11:27:29.183Z
updatedAt: 2025-01-17T19:04:43.465Z
---

# Parse data types on Swift

## Introduction

When saving data on a Back4App Database, each entity is stored in a key-value pair format. The data type for the value field goes from the fundamental ones (such as **String**, **Int**, **Double**, **Float**, and **Bool**) to more complex structures. The main requirement for storing data on a Back4App Database is that the entity has to conform the **ParseSwift** protocol. On its turn, this protocol provides a set of methods to store, update and delete any instance of an entity.

In this guide, you will learn how to create and setup an entity to save it on your Back4App Database. In the project example the entity we are storing encloses information about a Recipe.

This tutorial uses a basic app created in Xcode 12 and **iOS 14**.

:::hint{type="success"}
At any time, you can access the complete Project via our GitHub repositories.

- [**iOS Example Repository**](https://github.com/templates-back4app/ios-crud-to-do-list)
:::

## Goal

To understand how objects are parsed and stored on a Back4App Database.

## Prerequisites

:::hint{type="info"}
**To complete this quickstart, you need:**

- Xcode.
- An app created at Back4App.
  - Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse app at Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK (Swift) Tutorial**](https://www.back4app.com/docs/ios/parse-swift-sdk) to create an Xcode Project connected to Back4App.
:::

## Understanding our Recipes App

The app functionality is based on a form where one can enter information about a recipe. Depending on the information, the data type may vary. In our example the recipe has the following features:

| Field                   | Data Type         | Description                                                                                     |
| ----------------------- | ----------------- | ----------------------------------------------------------------------------------------------- |
| Name                    | String            | Name of the recipe                                                                              |
| Servings                | Int               | Number of servings                                                                              |
| Available               | Bool              | Determines whether the recipe is available or not                                               |
| Category                | Category          | A custom enumeration which classifies a recipe in three categories: Breakfast, Lunch and Dinner |
| Ingredients             | \[Ingredients]    | The set of ingredients enclosed in a customIngredient\*\* \*\*struct                            |
| Side options            | \[String]         | Names of the additional options the recipe comes with                                           |
| Nutritional information | \[String\:String] | A dictionary containing information about the recipe’s nutritional content                      |
| Release date            | Date              | A date showing when the recipe was available                                                    |

Additionally, there are more data types which are used to implement Database functionality like relation between objects. These data types are not covered in this tutorial.

## Quick reference of commands we are going to use

Given an object, say Recipe, if you want to save it on a Back4App Database, you have to first make this object to conform the ParseSwift protocol (available via the ParseSwift SDK).

```swift
1   import Foundation
2   import ParseSwift
3
4   struct Recipe: ParseObject {
5       /// Enumeration for the recipe category
6       enum Category: Int, CaseIterable, Codable {
7           case breakfast = 0, lunch = 1, dinner = 2
8        
9           var title: String {
10              switch self {
11              case .breakfast: return "Breakfast"
12              case .lunch: return "Lunch"
13              case .dinner: return "Dinner"
14              }
15          }
16      }
17
18      ...
19
20      /// A *String* type property
21      var name: String?
22    
23      /// An *Integer* type property
24      var servings: Int?
25    
26      /// A *Double* (or *Float*) type property
27      var price: Double?
28    
29      /// A *Boolean* type property
30      var isAvailable: Bool?
31    
32      /// An *Enumeration* type property
33      var category: Category?
34    
35      /// An array of *structs*
36      var ingredients: [Ingredient]
37    
38      /// An array of *Strings*
39      var sideOptions: [String]
40    
41      /// A dictionary property
42      var nutritionalInfo: [String: String]
43    
44      /// A *Date* type property
45      var releaseDate: Date?
46  }
```

Before storing instances of this object in a Back4App Database, all its properties must conform the Codable and Hashable protocols.

We make use of the following methods for managing these objects on the Back4App Database:

:::CodeblockTabs
Create

```swift
//The procedure for reading and updating a Recipe object is similar since they rely on the save() method. How a Recipe is instantiated determines if we are creating or updating the object on the Back4App Database. When creating a new instance we use
1   var newRecipe: Recipe
2
3   // Setup newRecipe's properties
4   newRecipe.name = "My recipe's name"
5   newRecipe.servings = 4
6   newRecipe.price = 3.99
7   newRecipe.isAvailable = false
8   newRecipe.category = .breakfast
9   newRecipe.sideOptions = ["Juice"]
10  newRecipe.releaseDate = Date()
11  ...
12
13  // Saves newRecipe on your Back4App Database synchronously and returns the new saved Item. It throws and error if something went wrong.
14  let savedRecipe = try? savedRecipe.save()
15
16  // Saves savedRecipe on your Back4App Database asynchronously, and passes a Result<ToDoListItem, ParseError> object to the completion block to handle the save proccess.
17  savedRecipe.save { result in
18      // Handle the result to check the save was successfull or not
19  }
```

Update

```swift
//And to update an existing instance, we have to provide the objectId value which identifies the the object on the Back4App Database. A satandard update can be implemented in the following way
1   let recipeToUpdate = Recipe(objectId: "OBJECT_ID")
2
3   // Update the properties you need
4   recipeToUpdate.name = "My updated recipe's name"
5   recipeToUpdate.servings = 5
6   recipeToUpdate.price = 5.99
7   recipeToUpdate.isAvailable = true
8   recipeToUpdate.category = .lunch
9   recipeToUpdate.sideOptions = ["Juice", "Coffee"]
10  recipeToUpdate.releaseDate = Date().addingTimeInterval(3600 * 24)
11  ...
12
13  // Save changes synchronousty
14  try? recipeToUpdate.save()
15
16  // Or save changes asynchronously
17  recipeToUpdate.save { result in
18      // handle the result
19  }
```

Read

```swift
//For reading objects stored on your Back4App Database, Recipe now provides the query() static method which returns a Query<Recipe>. This query object can be constructed using one or more QueryConstraint objects in the following way
1   let query = Recipe.query() // A query to fetch all Recipe items on your Back4App Database.
2   let query = Recipe.query("name" == "Omelette") // A query to fetch all Recipe items with name "Omelette" on your Back4App Database.
3   let query = Recipe.query(["name" == "Omelette", "price" = 9.99]) // A query to fetch all Recipe items with name = "Omelette" and price = 9.99.
4
5   // Fetches the items synchronously or throws an error if found.
6   let fetchedRecipes = try? query.find()
7
8   // Fetches the items asynchronously and calls a completion block passing a result object containing the result of the operation.
9   query.find { result in
10      // Handle the result
11  }
```

Delete

```swift
//Any deletion process is performed by calling the method delete() on the object to be deleted
1   var recipeToDelete: Recipe
2
3   // Delete recipeToDelete synchronously
4   try? recipeToDelete.delete()
5
6   // Delete recipeToDelete asynchronously
7   recipeToDelete.delete { result in
8       // Handle the result
9   }
```
:::

## 1 - Create the Recipe App Template

We start by creating a new XCode project. This this tutorial the project should look like this

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uYHuakrS2iSPUtwmnURpp_image.png)

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
9           window?.rootViewController = UINavigationController(rootViewController: RecipesController())
10          window?.makeKeyAndVisible()
11
12          // Additional logic
13      }
14
15      ...
16  }
```

The root view controller class (RecipesController) for the navigation controller is a subclass of UIViewController in which we will layout a form to create and update Recipe objects on the Back4App Database.

## 2 - Setup the Recipe object

Objects you want to save on your Back4App Database have to conform the ParseObject protocol. On our Recipes app this object is Recipe. Therefore, you first need to create this object. Create a new file Recipe.swift and add the following

```swift
1   import Foundation
2   import ParseSwift
3
4   struct Recipe: ParseObject {
5       /// Enumeration for the recipe category
6       enum Category: Int, CaseIterable, Codable {
7           case breakfast = 0, lunch = 1, dinner = 2
8        
9           var title: String {
10              switch self {
11              case .breakfast: return "Breakfast"
12              case .lunch: return "Lunch"
13              case .dinner: return "Dinner"
14              }
15          }
16      }
17    
18      // Required properties from ParseObject protocol
19      var objectId: String?
20      var createdAt: Date?
21      var updatedAt: Date?
22      var ACL: ParseACL?
23    
24      /// A *String* type property
25      var name: String?
26    
27      /// An *Integer* type property
28      var servings: Int?
29    
30      /// A *Double* (or *Float*) type property
31      var price: Double?
32    
33      /// A *Boolean* type property
34      var isAvailable: Bool?
35    
36      /// An *Enumeration* type property
37      var category: Category?
38    
39      /// An array of *structs*
40      var ingredients: [Ingredient]
41    
42      /// An array of *Strings*
43      var sideOptions: [String]
44
45      /// A dictionary property
46      var nutritionalInfo: [String: String]
47        
48      /// A *Date* type property
49      var releaseDate: Date?
50    
51      /// Maps the nutritionalInfo property into an array of tuples
52      func nutritionalInfoArray() -> [(name: String, value: String)] {
53          return nutritionalInfo.map { ($0.key, $0.value) }
54      }
55  }
```

where we already added all the necessary properties to Recipe according to the recipes’s features table.

The Ingredient data type is a struct holding the quantity and the description of the ingredient. As mentioned before, this data type should conform the Codable and Hashable protocols to be part of Recipe’s properties

```swift
1   import Foundation
2
3   struct Ingredient: Hashable, Codable {
4       var quantity: Float
5       var description: String
6   }
```

Additionally, the property category in Recipe has an enumeration (Category) as data type which also conforms the corresponding protocols

```swift
1   struct Recipe: ParseObject {
2       /// Enumeration for the recipe category
3       enum Category: Int, CaseIterable, Codable {
4           case breakfast = 0, lunch = 1, dinner = 2
5        
6           ...
7       }
8       ...   
9   }
```

## 3 - Setting up RecipesController

In RecipesController we should implement all the necessary configuration for the navigationBar and the form used to capture all the Recipe properties. This tutorial does not cover how to implement the layout for the form. We then focus on the logic related with managing data types using ParseSwift SDK. Below we highlight the key points in RecipesController which allow us to understand how we implement the connection between the user interface and the data coming from your Back4App Database

```swift
1   class RecipesController: UIViewController {
2       enum PreviousNext: Int { case previous = 0, next = 1 }
3    
4       ...
5    
6       var recipes: [Recipe] = [] // 1: An array of recipes fetched from your Back4App Database
7    
8       // Section header labels
9       private let recipeLabel: UILabel = .titleLabel(title: "Recipe overview")
10      private let ingredientsLabel: UILabel = .titleLabel(title: "Ingredients")
11      private let nutritionalInfoLabel: UILabel = .titleLabel(title: "Nutritional information")
12    
13      // 2: A custom view containing input fields to enter the recipe's information (except nutritional info. and ingredients)
14      let recipeOverviewView: RecipeInfoView
15    
16      // 3: A  stack view containig the fields to enter the recipe's ingredients
17      let ingredientsStackView: UIStackView
18     
19      // 4: A  stack view containig the fields to enter the nutritional information
20      let nutritionalInfoStackView: UIStackView
21    
22      // 5: Buttons to handle the CRUD logic for the Recipe object currently displayed
23      private var saveButton: UIButton = UIButton(title: "Save")
24      private var updateButton: UIButton = UIButton(title: "Update")
25      private var reloadButton: UIButton = UIButton(title: "Reload")
26    
27      var currentRecipeIndex: Int? // 6: An integer containing the index of the current recipe presenten from the recipes property
28    
29      override func viewDidLoad() {
30          super.viewDidLoad()
31          setupNavigationBar()
32          setupViews()
33      }
34    
35      override func viewDidAppear(_ animated: Bool) {
36          super.viewDidAppear(animated)
37          handleReloadRecipes()
38      }
39    
40      private func setupNavigationBar() {
41          navigationController?.navigationBar.barTintColor = .primary
42          navigationController?.navigationBar.titleTextAttributes = [.foregroundColor: UIColor.white]
43          navigationController?.navigationBar.isTranslucent = false
44          navigationController?.navigationBar.barStyle = .black
45          navigationItem.title = "Parse data types".uppercased()
46      }
47    
48      private func setupViews() {
49          ... // See the project example for more details
50
51          saveButton.addTarget(self, action: #selector(handleSaveRecipe), for: .touchUpInside)
52          updateButton.addTarget(self, action: #selector(handleUpdateRecipe), for: .touchUpInside)
53          reloadButton.addTarget(self, action: #selector(handleReloadRecipes), for: .touchUpInside)
54      }
55    
56      ...
57  }
```

## 3 - Handling user input and parsing a Recipe object

In a separate file (called RecipesController+ParseSwiftLogic.swift), using an extension we now implement the methods handleSaveRecipe(), handleUpdateRecipe() and handleUpdateRecipe() to handle the input data

```swift
1   import UIKit
2   import ParseSwift
3
4   extension RecipesController {
5       /// Retrieves all the recipes stored on your Back4App Database
6       @objc func handleReloadRecipes() {
7           view.endEditing(true)
8           let query = Recipe.query()
9           query.find { [weak self] result in // Retrieves all the recipes stored on your Back4App Database and refreshes the UI acordingly
10              guard let self = self else { return }
11              switch result {
12              case .success(let recipes):
13                  self.recipes = recipes
14                  self.currentRecipeIndex = recipes.isEmpty ? nil : 0
15                  self.setupRecipeNavigation()
16                
17                  DispatchQueue.main.async { self.presentCurrentRecipe() }
18              case .failure(let error):
19                  DispatchQueue.main.async { self.showAlert(title: "Error", message: error.message) }
20              }
21          }
22      }
23    
24      /// Called when the user wants to update the information of the currently displayed recipe
25      @objc func handleUpdateRecipe() {
26          view.endEditing(true)
27          guard let recipe = prepareRecipeMetadata(), recipe.objectId != nil else { // Prepares the Recipe object for updating
28              return showAlert(title: "Error", message: "Recipe not found.")
29          }
30        
31          recipe.save { [weak self] result in
32              switch result {
33              case .success(let newRecipe):
34                  self?.recipes.append(newRecipe)
35                  self?.showAlert(title: "Success", message: "Recipe saved on your Back4App Database! (objectId: \(newRecipe.id)")
36              case .failure(let error):
37                  self?.showAlert(title: "Error", message: "Failedto save recipe: \(error.message)")
38              }
39          }
40      }
41    
42      /// Saves the currently displayed recipe on your Back4App Database
43      @objc func handleSaveRecipe() {
44          view.endEditing(true)
45          guard var recipe = prepareRecipeMetadata() else { // Prepares the Recipe object for storing
46              return showAlert(title: "Error", message: "Failed to retrieve all the recipe fields.")
47          }
48        
49          recipe.objectId = nil // When saving a Recipe object, we ensure it will be a new instance of it.
50          recipe.save { [weak self] result in
51              switch result {
52              case .success(let newRecipe):
53                  if let index = self?.currentRecipeIndex { self?.recipes[index] = newRecipe }
54                  self?.showAlert(title: "Success", message: "Recipe saved on your Back4App Database! (objectId: \(newRecipe.id))")
55              case .failure(let error):
56                  self?.showAlert(title: "Error", message: "Failed to save recipe: \(error.message)")
57              }
58          }
59      }
60    
61      /// When called it refreshes the UI according to the content of *recipes* and *currentRecipeIndex* properties
62      private func presentCurrentRecipe() {
63          ...
64      }
65    
66      /// Adds the 'Next recipe' and 'Previous recipe' button on the navigation bar. These are used to iterate over all the recipes retreived from your Back4App Database
67      private func setupRecipeNavigation() {
68          ...
69      }
70    
71      /// Reads the information the user entered via the form and returns it as a *Recipe* object
72      private func prepareRecipeMetadata() -> Recipe? {
73          let ingredientsCount = ingredientsStackView.arrangedSubviews.count
74          let nutritionalInfoCount = nutritionalInfoStackView.arrangedSubviews.count
75        
76          let ingredients: [Ingredient] = (0..<ingredientsCount).compactMap { row in
77              guard let textFields = ingredientsStackView.arrangedSubviews[row] as? DoubleTextField,
78                    let quantityString = textFields.primaryText,
79                    let quantity = Float(quantityString),
80                    let description = textFields.secondaryText
81              else {
82                  return nil
83              }
84              return Ingredient(quantity: quantity, description: description)
85          }
86        
87          var nutritionalInfo: [String: String] = [:]
88          
89          (0..<nutritionalInfoCount).forEach { row in
90              guard let textFields = nutritionalInfoStackView.arrangedSubviews[row] as? DoubleTextField,
91                    let content = textFields.primaryText, !content.isEmpty,
92                    let value = textFields.secondaryText, !value.isEmpty
93              else {
94                  return
95              }
96              nutritionalInfo[content] = value
97          }
98         
99          let recipeInfo = recipeOverviewView.parseInputToRecipe() // Reads all the remaining fields from the form (name, category, price, serving, etc) and returns them as a tuple
100 
101         // we collect all the information the user entered and create an instance of Recipe.
102         // The recipeInfo.objectId will be nil if the currently displayed information does not correspond to a recipe already saved on your Back4App Database
103         let newRecipe: Recipe = Recipe(
104             objectId: recipeInfo.objectId,
105             name: recipeInfo.name,
106             servings: recipeInfo.servings,
107             price: recipeInfo.price,
108             isAvailable: recipeInfo.isAvailable,
109             category: recipeInfo.category,
110             ingredients: ingredients,
111             sideOptions: recipeInfo.sideOptions,
112             nutritionalInfo: nutritionalInfo,
113             releaseDate: recipeInfo.releaseDate
114         )
115        
116         return newRecipe
117     }
118    
119     /// Called when the user presses the 'Previous recipe' or 'Next recipe' button
120     @objc private func handleSwitchRecipe(button: UIBarButtonItem) {
121         ...
122     }
123 }
```

## 4 - Run the app!

Before pressing the run button on XCode, do not forget to configure your Back4App application in the AppDelegate class!

The first time you run the project you should see something like this in the simulator (with all the fields empty)

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/LBSCbEJ5R0GQvtntzir12_image.png" signedSrc size="60" width="1242" height="2688" position="center" caption}

Now you can start entering a recipe to then save it on your Back4App Database. Once you have saved one recipe, go to your [**Back4App dashboard**](https://parse-dashboard.back4app.com/apps) and go to your application, in the Database section you will find the class Recipe where all recipes created by the iOS App.

In Particular, it is worth noting how non-fundamental data types like Ingredient, Recipe.Category or dictionaries are stored. If you navigate through the data saved under the Recipe class, you will find that

- The nutritionalInformation dictionary is stored as a JSON object.
- The \[Ingredients] array is stored as an array of JSON objects.
- The enumeration Recipe.Category, since it is has an integer data type as RawValue, it is transformed to a Number value type.
- The releaseDate property, a Date type value in **Swift**, is also stored as a Date type value.

To conclude, when retrieving data from your Back4App Database, you do not need to decode all these fields manually, ParseSwift SDK does decode them automatically. That means, when creating a query (Query\<Recipe> in case) to retrieve data, the query.find() method will parse all the data types and JSON objects to return a Recipe array, there is no additional parsing procedure to implement.
