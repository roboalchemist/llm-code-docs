# Source: https://docs-containers.back4app.com/docs/flutter/parse-sdk/data-objects/flutter-one-to-many-relationship.md

---
title: 1:N Relationship
slug: docs/flutter/parse-sdk/data-objects/flutter-one-to-many-relationship
description: In this guide you'll learn how to create and query one-to-many data object associations in Parse on Flutter
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-15T15:14:39.658Z
updatedAt: 2025-01-16T20:36:37.366Z
---

# One to many Relationship on Flutter


Introduction
------------


Using Parse, you can store data objects establishing relations between them. To model this behavior, any ParseObject can be used as a value in other ParseObject. Internally, the Parse framework will store the referred-to object in just one place, to maintain consistency. That can give you extra power when building and running complex queries. There are three main relation types:

-
  one-to-one, establishing direct relations between two objects and only them;
-
  one-to-many, where one object can be related to many other objects;
-
  many-to-many, which can create many complex relations between many objects.


In this guide we will detail how the one-to-many relation works using a pratical app example. There are two ways to create a one-to-many relation in Parse:

-
  The first is using the Pointers in Child Class, which is the fastest in creation and query time.
-
  The second is using Arrays of Pointers in Parent Class which can lead to slow query times depending on their size. Because of this performance issue, we will use only pointers examples.

You will implement a Flutter book registration App and will create and query related objects using the Parse Pointers.

:::hint{type="info"}
Relation as one-to-one is not common and we are not going to cover on our guides. As an example a relationship between the User class and another class that will contain sensitive user data for [**security reasons**](https://blog.back4app.com/parse-server-best-practices/) (*1.4. Don’t let users have access to sensitive data from others*).
:::

::embed[]{url="https://www.youtube.com/embed/b6fdFD0hlJo"}

## Prerequisites

:::hint{type="info"}
- [**Flutter version 2.2.x or later**](https://flutter.dev/docs/get-started/install)
- [**Android Studio&#x20;**](https://developer.android.com/studio)or [**VS Code installed**](https://code.visualstudio.com/) (with [**Plugins**](https://docs.flutter.dev/get-started/editor) Dart and Flutter)
- An app [**created**](https://www.back4app.com/docs/get-started/new-parse-app) on Back4App:
  - **Note:&#x20;**&#x46;ollow the [**New Parse App Tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- An Flutter app connected to Back4app.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK on Flutter project**](https://www.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk) to create an Flutter Project connected to Back4App.
- A device (or virtual device) running Android or iOS.
:::

## Understanding the Book App


The main object class you’ll be using is the Book class, storing each book entry in the registration. Also, these are the other three object classes:


- Publisher: book publisher name, one-to-many relation with Book;
- Genre: book genre, one-to-many relation with Book. Note that for this example we will consider that a book can only have one genre;
- Author: book author, many-to-many relation with Book, since a book can have more than one author and an author can have more than one book as well;

A visual representation of these data model:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/A3OFhXHEJEAvPvi6DVVuq_image.png)

We will assume that each object class (Publisher, Genre) has only a string type name attribute and Book has title and year, apart from any additional relational attribute. In the previous guides we have already seen how to save and read ParseObject so in this guide, we will not cover how to save and read Genre and Publisher objects.

You will find the following screens on the Book App:

- **Registration and Listing of Genre**
- **Registration and List of Publishers**
- **Book Registration**
- **List of Publishers and Books**
- **Book details**

We won’t explain the Flutter application code once this guide’s primary focus is using the Flutter with Parse using relations.

## 1 - Create Book App Template

Let’s first run the Book App project template. Open your Flutter project from the previous guide **Flutter plugin for Parse Server**. The [**Book Flutter App**](https://github.com/templates-back4app/flutter_associations) repository is also available to you clone and run the project. Copy the [**main.dart**](https://github.com/templates-back4app/flutter_associations/blob/master/lib/main.dart) file and replace your current code from previous guides.

**Note:**
When debug parameter in function Parse().initialize is true, allows displaying Parse API calls on the console. This configuration can assist in debugging the code. It is advisable to disable debug in the release version.

### Step 2 - Connect Template to Back4app Project

Find your Application Id and Client Key credentials navigating to your app Dashboard at [**Back4App Dashboard->App Settings->Security & Keys**](https://www.back4app.com/docs/parse-dashboard/app-settings). Update your code in main.dart with the values of your project’s ApplicationId and ClientKey in Back4app.

- **keyApplicationId = App Id**
- **keyClientKey = Client Key**

Run the project, and the app will load as shown in the image.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/yMFpRGpZJLsxJjtLPBDdk_image.png" signedSrc size="30" width="323" height="627" position="center" caption}

Click on Add Genre to register and view the list of Genres that will be used in the registration of books.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/AXMne48nSmI_omEvIIFLT_image.png" signedSrc size="30" width="323" height="627" position="center" caption}

Click on Add Publisher to register and view the list of Publishers that will be used in the registration of books.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/s566XXvwuWEOBBdq6LHC5_image.png" signedSrc size="30" width="323" height="627" position="center" caption}

Click on Add Book to register new Book using relations with Genre and Publisher.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/jVUGzMZD8IIhrw57GNnRc_image.png" signedSrc size="30" width="328" height="637" position="center" caption}

Click on List Publisher/Book to view the list of Publishers and Books.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/EGNDJ3ZrgC9_P-vPrSZ_a_image.png" signedSrc size="30" width="323" height="627" position="center" caption}

## 3 - Save a Book object and its relations

This function will create a new Book in Back4app database with relations. Search for the function doSaveBook in file main.dart, and insert the code below inside the Future\<void> doSaveBook() function:

```dart
1       final book = ParseObject('Book')
2         ..set('title', controllerTitle.text.trim())
3         ..set('year', int.parse(controllerYear.text.trim()))
4         //the objectId will be converted to a Pointer on the save() method
5         ..set('genre', ParseObject('Genre')..objectId = genre.objectId)
6         //you can also convert to a Pointer object before the saving using the .toPointer() method
7         ..set(
8             'publisher',
9             (ParseObject('Publisher')..objectId = publisher.objectId)
10                .toPointer());
11
12      await book.save();
```

To build this function, follow these steps:

- 1\. Create a new instance of the Parse Book class with the command ParseObject('Book').
- 2\. Use the set function to set the fields for this object.
  - 2.1.title is a text attributes that receive value from the text controller.
  - 2.2.genre receives the value by defining a ParseObject with the objectId of the selected Genre. (*Parse will convert to pointer on save*)
  - 2.3.publisher receives the value by defining a ParseObject with the objectId of the selected Publisher. (*Note that we can specify for Parse that we want to save as a&#x20;*&#x70;ointe&#x72;*&#x20;using the&#x20;*&#x74;oPointer()*method*)
- 3\. Call the save function in ParseObject, which will effectively register the object to your database in the Back4app Dashboard.

Run the app and test the new function.

- Click on the Add Book button.
- Fill book information.

The app requires the selection of the Authors (s), but the code for them will be covered only in the next guide.

- Click on Save Book button



::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cssL-jdLG4ecfman8hIGp_image.png" signedSrc size="30" width="323" height="627" position="center" caption}

To confirm that the new object is save in the database with relations, you can access the Back4app Dashboard and access Book class.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/SEpUCYQHevWFwhR33NxCp_image.png)

If you access your Book class using the Dashboard you can click on the object pointer value and you will be redirected to the referenced object. It may seem like a harmless feature, but this makes debugging and error tracing much quicker than searching for it manually.

## 4 - Query the Book List and its related objects

This function will query Books in Back4app database with using relations with Publisher. Through the Publisher, we will get the list of books.

Search for the function getBookList in the file main.dart, then replace the code below inside Future\<List\<ParseObject>> getBookList(String publisherId) function:

```dart
1       QueryBuilder<ParseObject> queryBook =
2           QueryBuilder<ParseObject>(ParseObject('Book'))
3             ..whereEqualTo('publisher',
4                 (ParseObject('Publisher')..objectId = publisherId).toPointer())
5             ..orderByAscending('title');
6       final ParseResponse apiResponse = await queryBook.query();
7   
8       if (apiResponse.success && apiResponse.results != null) {
9         return apiResponse.results;
10      } else {
11        return [];
12      }
```

To build this function, follow these steps:

1. Create an instance of ParseQuery object for Book class. Insert a condition in the query, to search Books where publisher field is equal pointer of Publisher ParseObject.
2. We sort the result in ascending name order
3. Do a Query’s search method using query() method.
4. If the operations succeed, objects in Book will be returned.

Run the app and test the new Query. First, click on the List Publisher/Book button.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/hUJS9Me_FZYq1DeuzH22Z_image.png" signedSrc size="30" width="327" height="634" position="center" caption}

## It’s done!

At this point, you learned how to create and query one-to-many relations in Parse on Flutter. In the next guide, we’ll show you how to make many-to-many relationships and how to perform queries returning data from related objects.
