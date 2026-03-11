# Source: https://docs-containers.back4app.com/docs/ios/parse-swift-sdk/data-objects/relationships.md

# Source: https://docs-containers.back4app.com/docs/react/data-objects/relationships.md

# Source: https://docs-containers.back4app.com/docs/android/data-objects/relationships.md

---
title: Relationships
slug: docs/android/data-objects/relationships
description: In this guide you'll learn how to create and query one-to-many or many-to-many data object associations in Parse on Android
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-13T13:16:59.042Z
updatedAt: 2025-01-16T20:44:30.856Z
---

# Relationships on Android

## Introduction

Using Parse, you can store data objects establishing relations between them. To model this behavior, any ParseObject can be used as a value in other ParseObject. Internally, the Parse framework will store the referred-to object in just one place, to maintain consistency. That can give you extra power when building and running complex queries. There are three main relation types:

- one-to-one, establishing direct relations between two objects and only them;
- one-to-many, where one object can be related to many other objects;
- many-to-many, which can create many complex relations between many objects.

There are two ways to create a one-to-many relation in Parse:

- The first is using the Pointers in Child Class, which is the fastest in creation and query time.
- The second is using Arrays of Pointersin Parent Class which can lead to slow query times depending on their size. Because of this performance issue, we will use only pointers examples.

There are three ways to create a many-to-many relation in Parse.

- The first is using the Parse Relations, which is the fastest in creation and query time. We will use this in this guide.
- The second is using Arrays of Pointers which can lead to slow query times depending on their size.
- The third is using JoinTablewhere the idea from classical database. When there is a many-to-nany relation, we combine every objectId or Pointer from both sides together to build a new separate table in which the relationship is tracked.

This tutorial uses a basic app created in Android Studio 4.1.1 with buildToolsVersion=30.0.2 , Compile SDK Version = 30.0.2 and targetSdkVersion 30

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our Github repositories

- [**Kotlin Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Kotlin)
- [**Java Example Repository**](https://github.com/templates-back4app/Android-Parse-Sdk-Java)
:::

## Goal

Our goal is, understand Parse Relations by creating a practical Book app.

Here is a preview of what we are gonna achieve:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/4GItAcqwXy8pwNIso5U51_image.png" signedSrc size="30" width="346" height="750" position="center" caption}

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, we need:**

- [**Android Studio**](https://developer.android.com/studio/index.html)
- An app created on Back4App.
  - **Note:&#x20;**&#x46;ollow the [**New Parse App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- An android app connected to Back4App.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK tutoria**](https://www.back4app.com/docs/android/parse-android-sdk)l to create an Android Studio Project connected to Back4App.
- A device (or[**&#x20;virtual device**](https://developer.android.com/studio/run/managing-avds.html)) running Android 4.1 (Jelly Bean) or newer.
:::

## Understanding the Book App

The main object class you’ll be using is the Book class, storing each book entry in the registration. Also, these are the other three object classes:

- Publisher: book publisher name, one-to-many relation withBook
- Genre: book genre, one-to-many relation withBook. Note that for this example we will consider that a book can only have one genre;
- Author: book author, many-to-many relation withBook, since a book can have more than one author and an author can have more than one book as well;

A visual representation of these data model:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/WTHengaTCAsXpfHkt_uVp_image.png)

## Let’s get started!

:::hint{type="info"}
Before next steps, we need to connect Back4App to our application. You should save the appId and clientKey from the Back4App to string.xml file and then init Parse in our App.java or App.kt file.
Follow the [**New Parse App tutorial**](https://www.back4app.com/docs/android/parse-android-sdk) if you don’t know how to init Parse to your app.

Or you can download the projects we shared the github links above and edit only the appId and clientKey parts according to you.
:::

## 1 - Save and list related objects of books

In this step we will see how to save and list the Genres, Publishers and Authors classes related with the Book class.

### **1.1 - Save and list Genres**

We can register aGenreusing the following snippet.

:::CodeblockTabs
```java
1   private void addGenre(String name) {
2     //We are taking this name parameter from the input.
3     progressDialog.show();
4     ParseObject parseObject = new ParseObject("Genre");
5     parseObject.put("name", name);
6     parseObject.saveInBackground(e -> {
7       progressDialog.dismiss();
8       if (e == null) {
9         getGenres();
10        inputGenre.setText("");
11        Toast.makeText(this, "Genre saved successfully", Toast.LENGTH_SHORT).show();
12      } else { 
13      Toast.makeText(this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
14      }
15    });
16  }
```

```kotlin
1   private fun addGenre(name: String) {
2     //We are taking this name parameter from the input.
3     progressDialog.show()
4     val parseObject = ParseObject("Genre")
5     parseObject.put("name", name)
6     parseObject.saveInBackground {
7       progressDialog.dismiss()
8       if (it == null) {
9         getGenres()
10        inputGenre.setText("")
11        Toast.makeText(this, "Genre saved successfully", Toast.LENGTH_SHORT).show()
12      } else {
13          Toast.makeText(this, it.localizedMessage, Toast.LENGTH_SHORT).show()
14      }
15    }
16  }
```
:::

We can register aGenreusing the following snippet.

:::CodeblockTabs
```java
1   private void getGenres() {
2     progressDialog.show();
3     ParseQuery<ParseObject> query = new ParseQuery<>("Genre");
4     query.findInBackground((objects, e) -> {
5       progressDialog.dismiss();
6       List<ParseObjectModel> list = new ArrayList<>();
7       for (ParseObject parseObject : objects) {
8         list.add(new ParseObjectModel(parseObject));
9       }
10
11      GenreAdapter adapter = new GenreAdapter(list, this);
12      recyclerView.setLayoutManager(new LinearLayoutManager(this));
13      recyclerView.setAdapter(adapter);
14    });
15  }
```

```kotlin
1   private fun getGenres() {
2     progressDialog.show()
3     val query = ParseQuery<ParseObject>("Genre")
4     query.findInBackground { objects, e ->
5     progressDialog.dismiss()
6     var list: MutableList<ParseObjectModel> = ArrayList()
7     for (parseObject in objects) {
8       list.add(ParseObjectModel(parseObject))
9     }
10    val adapter = GenreAdapter(this, list)
11    recyclerView.layoutManager = LinearLayoutManager(this)
12    recyclerView.adapter = adapter
13    }
14  }
```
:::

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/27F_Ufr36FnQWAFtLAzkg_image.png" signedSrc size="30" width="532" height="1084" position="center" caption}

### **1.2 - Save and list Publishers**

We can register aPublisherusing the following snippet.

:::CodeblockTabs
```java
1   private void addPublisher(String name) {
2     //We are taking this name parameter from the input.
3     progressDialog.show();
4     ParseObject parseObject = new ParseObject("Publisher");
5     parseObject.put("name", name);
6     parseObject.saveInBackground(e -> {
7       progressDialog.dismiss();
8       if (e == null) {
9         getPublishers();
10        inputPublisher.setText("");
11        Toast.makeText(this, "Publisher saved successfully", Toast.LENGTH_SHORT).show();
12      } else {
13          Toast.makeText(this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
14      }
15    });
16  }
```

```kotlin
1   private fun addPublisher(name: String) {
2     //We are taking this name parameter from the input.
3     progressDialog.show()
4     val parseObject = ParseObject("Publisher")
5     parseObject.put("name", name)
6     parseObject.saveInBackground {
7       progressDialog.dismiss()
8       if (it == null) {
9         getPublishers()
10        inputPublisher.setText("")
11        Toast.makeText(this, "Publisher saved successfully", Toast.LENGTH_SHORT).show()
12      } else {
13        Toast.makeText(this, it.localizedMessage, Toast.LENGTH_SHORT).show()
14      }
15    }
16  }
```
:::

We can register aPublisherusing the following snippet.

:::CodeblockTabs
```java
1   private void getPublishers() {
2     progressDialog.show();
3     ParseQuery<ParseObject> query = new ParseQuery<>("Publisher");
4     query.findInBackground((objects, e) -> {
5       progressDialog.dismiss();
6       List<ParseObjectModel> list = new ArrayList<>();
7         for (ParseObject parseObject : objects) {
8           list.add(new ParseObjectModel(parseObject));
9         }
10      
11        PublisherAdapter adapter = new PublisherAdapter(list, this);
12        recyclerView.setLayoutManager(new LinearLayoutManager(this));
13        recyclerView.setAdapter(adapter);
14    });
15  }
```

```kotlin
1   private fun getPublishers() {
2     progressDialog.show()
3     val query = ParseQuery<ParseObject>("Publisher")
4     query.findInBackground { objects, e ->
5       progressDialog.dismiss()
6       val list: ArrayList<ParseObjectModel> = ArrayList()
7       for (parseObject in objects) {
8         list.add(ParseObjectModel(parseObject))
9       }
10  
11      val adapter = PublisherAdapter(this, list)
12      recyclerView.layoutManager = LinearLayoutManager(this)
13      recyclerView.adapter = adapter
14    }
15  }
```
:::

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/As2skdoT9UlsTddqEfirE_image.png" signedSrc size="30" width="532" height="1084" position="center" caption}

### **1.3 - Save and list Authors**

We can register aAuthorusing the following snippet.

:::CodeblockTabs
```java
1   private void addAuthor(String name){
2     //We are taking this name parameter from the input.
3     progressDialog.show();
4     ParseObject parseObject = new ParseObject("Author");
5     parseObject.put("name", name);
6     parseObject.saveInBackground(e -> {
7       progressDialog.dismiss();
8       if (e == null) {
9         getAuthors();
10        inputAuthor.setText("");
11        Toast.makeText(this, "Author saved successfully", Toast.LENGTH_SHORT).show();
12      } else {
13        Toast.makeText(this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
14      }
15    });
16  }
```

```kotlin
1   private fun addAuthor(name: String) {
2     //We are taking this name parameter from the input.
3     progressDialog.show()
4     val parseObject = ParseObject("Author")
5     parseObject.put("name", name)
6     parseObject.saveInBackground {
7       progressDialog.dismiss()
8       if (it == null) {
9         getAuthors()
10        inputAuthor.setText("")
11        Toast.makeText(this, "Author saved successfully", Toast.LENGTH_SHORT).show()
12      } else {
13          Toast.makeText(this, it.localizedMessage, Toast.LENGTH_SHORT).show()
14      }
15    }
16  }
```
:::

We can register aAuthorusing the following snippet.

:::CodeblockTabs
```java
1   private void getAuthors() {
2     progressDialog.show();
3     ParseQuery<ParseObject> query = new ParseQuery<>("Author");
4     query.findInBackground((objects, e) -> {
5       progressDialog.dismiss();
6       List<ParseObjectModel> list = new ArrayList<>();
7       for (ParseObject parseObject : objects) {
8         list.add(new ParseObjectModel(parseObject));
9       }
10
11      AuthorAdapter adapter = new AuthorAdapter(list, this);
12      recyclerView.setLayoutManager(new LinearLayoutManager(this));
13      recyclerView.setAdapter(adapter);
14    });
15  }
```

```kotlin
1   private fun getAuthors() {
2     progressDialog.show()
3     val query = ParseQuery<ParseObject>("Author")
4     query.findInBackground { objects: List<ParseObject>, e: ParseException? ->
5       progressDialog.dismiss()
6       val list: ArrayList<ParseObjectModel> = ArrayList()
7       for (parseObject in objects) {
8          list.add(ParseObjectModel(parseObject))
9       }
10      val adapter = AuthorAdapter(this, list)
11      recyclerView.layoutManager = LinearLayoutManager(this)
12      recyclerView.adapter = adapter
13    }
14  }
```
:::

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/KNTZxKCHMAjZAKFGtW9j5_image.png" signedSrc size="30" width="532" height="1084" position="center" caption}

In this part, we use a model class named ParseObjectModel. In this model class, we have a ParseObject variable to be able to read the data, and the isChecked variable, which we will use to save the book in the next step. We will be able to easily retrieve the selected objects with the isChecked variable.
Here is the our ParseObjectModel model.

:::CodeblockTabs
```java
1   public class ParseObjectModel {
2     ParseObject object;
3     boolean isChecked = false;
4  
5     public ParseObjectModel(ParseObject object) {
6       this.object = object;
7     }
8
9     public ParseObject getObject() {
10      return object;
11    }
12 
13    public ParseObjectModel setObject(ParseObject object) {
14      this.object = object;
15      return this;
16    }
17
18    public boolean isChecked() {
19      return isChecked;
20    }
21 
22    public ParseObjectModel setChecked(boolean checked) {
23      isChecked = checked;
24      return this;
25    }
26  }
```

```kotlin
1   class ParseObjectModel(obj: ParseObject) {
2     var obj: ParseObject? = null
3     var isChecked: Boolean = false
4  
5     init {
6       this.obj = obj
7     }
8   }
```
:::

## 2 - Save a Book object and its relations

### **2.1 - Save a Book object with 1\:N Relationship**

This function will create a new Book in Back4app database with 1\:N relations.

:::CodeblockTabs
```java
1   progressDialog.show();
2   book.put("genre", genre);
3   book.put("publisher", publisher);
4   book.put("title", title);
5   book.put("year", year);
6   book.saveInBackground(e -> {
7     progressDialog.hide();
8     if (e == null) {
9       Toast.makeText(AddBookActivity.this, "Book saved successfully", Toast.LENGTH_SHORT).show();
10      startActivity(new Intent(AddBookActivity.this, BookListActivity.class));
11      finish();
12    } else {
13      Toast.makeText(AddBookActivity.this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
14    }
15  });
```

```kotlin
1   progressDialog.show()
2   book.put("genre", genre)
3   book.put("publisher", publisher!!)
4   book.put("title", title)
5   book.put("year", year)
6   book.saveInBackground {
7     progressDialog.hide()
8     if (it == null) {
9       Toast.makeText(this, "Book saved successfully", Toast.LENGTH_SHORT).show()
10      startActivity(Intent(this@AddBookActivity, BookListActivity::class.java))
11      finish()
12    } else {
13      Toast.makeText(this, it.localizedMessage, Toast.LENGTH_SHORT).show()
14    }
15  }
```
:::

### **2.2 Save a Book object with N\:N Relationship**

This function will create a new Book in Back4app database with N\:N relations. For the Author relation, we find the selected Author/s in the adapter of the authorRecyclerView and save them as Parse Relation.

:::CodeblockTabs
```java
1   progressDialog.show();
2   book.put("genre", genre);
3   book.put("publisher", publisher);
4   book.put("title", title);
5   book.put("year", year);
6
7   //Here we are setting book relation with getSelectedItem function of BookAuthorAdapter.
8   if (recyclerViewAuthors.getAdapter() != null) {
9     relation = ((BookAuthorAdapter) recyclerViewAuthors.getAdapter()).getSelectedItems(book);
10      if (relation == null) {
11        Toast.makeText(this, "Please select Author/s", Toast.LENGTH_SHORT).show();
12        return;
13      }
14    } else {
15      Toast.makeText(this, "Something went wrong!!", Toast.LENGTH_SHORT).show();
16      return;
17    }
18
19  book.saveInBackground(e -> {
20    progressDialog.hide();
21    if (e == null) {
22      Toast.makeText(AddBookActivity.this, "Book saved successfully", Toast.LENGTH_SHORT).show();
23      startActivity(new Intent(AddBookActivity.this, BookListActivity.class));
24      finish();
25    } else {
26      Toast.makeText(AddBookActivity.this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
27    }
28  });
29
30  //This is the function for save Author/s relation of Book object.This function in BookAuthorAdapter.
31  public ParseRelation<ParseObject> getSelectedItems(ParseObject parseObject) {
32    ParseRelation<ParseObject> relation = parseObject.getRelation("author_relation");
33    for (ParseObjectModel object : this.list) {
34      if (object.isChecked())
35      relation.add(object.getObject());
36    }
37    return relation;
38  } 
```

```kotlin
1   progressDialog.show()
2   book.put("genre", genre)
3   book.put("publisher", publisher!!)
4   book.put("title", title)
5   book.put("year", year)
6
7   //Here we are setting book relation with getSelectedItem function of BookAuthorAdapter.
8
9   if (recyclerViewAuthors.adapter != null) {
10    relation = (recyclerViewAuthors.adapter as BookAuthorAdapter).getSelectedItems(book)
11    if (relation == null) {
12      Toast.makeText(this, "Please select Author/s", Toast.LENGTH_SHORT).show()
13      return
14    }
15  } else {
16    Toast.makeText(this, "Something went wrong!!", Toast.LENGTH_SHORT).show()
17    return
18  }
19
20  book.saveInBackground {
21    progressDialog.hide()
22    if (it == null) {
23      Toast.makeText(this, "Book saved successfully", Toast.LENGTH_SHORT).show()
24      startActivity(Intent(this@AddBookActivity, BookListActivity::class.java))
25      finish()
26    } else {
27      Toast.makeText(this, it.localizedMessage, Toast.LENGTH_SHORT).show()
28    }
29  }
30
31  //This is the function for save Author/s relation of Book object.This function in BookAuthorAdapter.
32
33  fun getSelectedItems(parseObject: ParseObject): ParseRelation<ParseObject>? {
34    var relation:ParseRelation<ParseObject>? = parseObject.getRelation("author_relation")
35    for (obj in this.list) {
36      if (obj.isChecked)
37        relation?.add(obj.obj)
38    }
39    return relation
40  }
```
:::

## 3 - Query the Book Details with Relations

With these functions, we will list our Books according to their Publishers. First, we throw a query to the Publisher class.

:::CodeblockTabs
```java
1   progressDialog.show();
2   ParseQuery<ParseObject> query = new ParseQuery<>("Publisher");
3   query.findInBackground((objects, e) -> {
4     progressDialog.hide();
5     if (e == null) {
6       BookListAdapter adapter = new BookListAdapter(objects, this);
7       recyclerView.setLayoutManager(new LinearLayoutManager(this));
8       recyclerView.setAdapter(adapter);
9     } else {
10      Toast.makeText(this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
11    }
12  });
```

```kotlin
1   progressDialog.show()
2   val query = ParseQuery<ParseObject>("Publisher")
3   query.findInBackground { objects: List<ParseObject>?, e: ParseException? ->
4     progressDialog.hide()
5     if (e == null) {
6       val adapter = BookListAdapter(this, objects!!)
7       recyclerView.layoutManager = LinearLayoutManager(this)
8       recyclerView.adapter = adapter
9     } else {
10      Toast.makeText(this, e.localizedMessage, Toast.LENGTH_SHORT).show()
11    }
12  }
```
:::

And then we query to list the Books that each Publisher item is related to.

:::CodeblockTabs
```java
1   ParseObject object = list.get(position);
2   holder.title.setText(object.getString("name"));
3   ParseQuery<ParseObject> query = new ParseQuery<>("Book");
4   query.whereEqualTo("publisher", object);
5   query.findInBackground((objects, e) -> {
6     if (e == null) {
7       BooksAdapter adapter = new BooksAdapter(objects, context);
8       holder.books.setLayoutManager(new LinearLayoutManager(context));
9       holder.books.setAdapter(adapter);
10    } else {
11      Toast.makeText(context, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
12    }
13  });
```

```kotlin
1   val `object` = list[position]
2   holder.title.text = `object`.getString("name")
3   val query = ParseQuery<ParseObject>("Book")
4   query.whereEqualTo("publisher", `object`)
5   query.findInBackground { objects: List<ParseObject>?, e: ParseException? ->
6     if (e == null) {
7       val adapter = BooksAdapter(context, objects!!)
8       holder.books.layoutManager = LinearLayoutManager(context)
9       holder.books.adapter = adapter
10    } else {
11      Toast.makeText(context, e.localizedMessage, Toast.LENGTH_SHORT).show()
12    }
13  }
```
:::

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/_mdZWSy6L--bhqBCF_Dz3_image.png" signedSrc size="30" width="532" height="1084" position="center" caption}

Now, when we click on any Book object, we send the Object Id of this Book with an intent to the page that will show the details of that Book. And we get all the details of the Book from the database by using this Object Id on that page.

:::CodeblockTabs
```java
1   private void getBookWithDetails() {
2     progressDialog.show();
3     ParseQuery<ParseObject> query = new ParseQuery<>("Book");
4     query.getInBackground(getIntent().getStringExtra("objectId"), (object, e) -> {
5       if (e == null) {
6         bookTitle.setText("Title: " +object.getString("title"));
7         bookYear.setText("Year: " +object.getString("year"));
8         try {
9           bookGenre.setText("Genre: " +object.getParseObject("genre").fetchIfNeeded().getString("name"));
10        } catch (ParseException parseException) {
11            parseException.printStackTrace();
12        }
13        try {
14          bookPublisher.setText("Publisher: " + object.getParseObject("publisher").fetchIfNeeded().getString("name"));
15        } catch (ParseException parseException) {
16          parseException.printStackTrace();
17        }
18      
19        object.getRelation("author_relation").getQuery().findInBackground((objects, e1) -> {
20          progressDialog.hide();
21          if (e1 == null) {
22            BookDetailAuthorAdapter adapter = new BookDetailAuthorAdapter(objects, this);
23            authorRecyclerView.setLayoutManager(new LinearLayoutManager(this));
24            authorRecyclerView.setAdapter(adapter);
25         } else {
26            Toast.makeText(this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
27          }
28        });
29      } else {
30        progressDialog.hide();
31        Toast.makeText(this, e.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
32      }
33    });
34  }
```

```kotlin
1   private fun getBookWithDetails() {
2     progressDialog.show()
3     val query = ParseQuery<ParseObject>("Book")
4  
5     query.getInBackground(intent.getStringExtra("objectId")) { `object`, e ->
6     if (e == null) {
7       bookTitle.text = "Title: " + `object`.getString("title")
8       bookYear.text = "Year: " + `object`.getString("year")
9       try {
10        bookGenre.text = "Genre: " + `object`.getParseObject("genre")?.fetchIfNeeded<ParseObject>()?.getString("name")
11      } catch (parseException: ParseException) {
12        parseException.printStackTrace()
13      }
14      try {
15        bookPublisher.text =
16        "Publisher: " + `object`.getParseObject("publisher")?.fetchIfNeeded<ParseObject>()?.getString("name")
17      } catch (parseException: ParseException) {
18        parseException.printStackTrace()
19      }
20
21      `object`.getRelation<ParseObject>("author_relation").query.findInBackground { objects, e1 ->
22      progressDialog.hide()
23        if (e1 == null) {
24          val adapter = BookDetailAuthorAdapter(this, objects)
25          authorRecyclerView.layoutManager = LinearLayoutManager(this)
26          authorRecyclerView.adapter = adapter
27        } else {
28          Toast.makeText(this, e1.localizedMessage, Toast.LENGTH_SHORT).show()
29        }
30     }
31    } else {
32        progressDialog.hide()
33        Toast.makeText(this, e.localizedMessage, Toast.LENGTH_SHORT).show()
34      }
35    }
36  }
```
:::

## It’s done!

At this point, we have learned Parse Relationships on Android.
