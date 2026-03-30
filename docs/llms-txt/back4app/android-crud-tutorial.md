# Source: https://docs-containers.back4app.com/docs/android/data-objects/android-crud-tutorial.md

---
title: Basic Operations
slug: docs/android/data-objects/android-crud-tutorial
description: In this guide you learn how to use the Android SDK to saving, retrieving, updating and deleting objects
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T21:18:24.147Z
updatedAt: 2025-01-16T20:44:22.617Z
---

# CRUD Parse objects in Android

## Introduction

In this section we are gonna build an Android application that performs basic CRUD operations. CRUD is abbreviation of Create-Read-Update-Delete. When you store data on Parse it is built around ParseObject and each one contains key-value pairs of JSON-compatible data.

The values you can store in Back4App Database could be in type of String, Number, Bool, Array, Object, Date, File, Pointer, Relation and null.

You can get more information about data types by clicking [**here**](https://docs.parseplatform.org/js/guide/#data-types).

This tutorial uses a basic app created in Android Studio 4.1.1 with buildToolsVersion=30.0.2 , Compile SDK Version = 30.0.2 and targetSdkVersion 30

:::hint{type="success"}
**At any time, you can access the complete Project via our GitHub repositories.**

- [**Kotlin Example Repository**](https://github.com/templates-back4app/android_crud_operations_kotlin)
- [**Java Example Repository**](https://github.com/templates-back4app/android_crud_operations_java)
:::

## Goal

Here is a preview of what we are gonna achive:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/FxSZDT3Wxn0M43vVJGUkN_image.png" signedSrc size="30" width="346" height="750" position="center" caption}

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

## Understanding our Todo App

To better understand Parse on Android, you will see the CRUD operations implemented on a ToDo App. The application will have a simple interface, with a title and description text field to register a task and a list of registered tasks. You can update each task’s title or description.

:::hint{type="info"}
**Note:**

- In this tutorial we will make our own custom alert dialog. Therefore, the codes will be configured to follow the template. You can adjust it to your own design.
- If you have any trouble, check the GitHub repositories for [**Kotlin&#x20;**](https://github.com/templates-back4app/android_crud_operations_kotlin)and [**Java**](https://github.com/templates-back4app/android_crud_operations_java).
:::

## Let’s get started!

Following the next steps, you will be able to build a Todo App that will store the tasks at Back4App Database.

## 1 - Create Todo App Template

Go to Android Studio, and find activity\_main.xml layout file from the Project (Project/app/res/layout/activity\_main.xml) and then replace the code below with your own code. This xml code will be our MainActivity's design, and we will bind this views to our MainActivity.java class and use them.

```xml
1   <?xml version="1.0" encoding="utf-8"?>
2   <androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
3       xmlns:app="http://schemas.android.com/apk/res-auto"
4       xmlns:tools="http://schemas.android.com/tools"
5       android:layout_width="match_parent"
6       android:layout_height="match_parent"
7       tools:context=".MainActivity">
8
9       <!--Title-->>
10      <TextView
11          android:id="@+id/textView"
12          android:layout_width="0dp"
13          android:layout_height="wrap_content"
14          android:background="@color/blue_700"
15          android:gravity="center_horizontal"
16          android:padding="24dp"
17          android:text="TODO List"
18          android:textColor="@color/white"
19          app:layout_constraintEnd_toEndOf="parent"
20          app:layout_constraintStart_toStartOf="parent"
21          app:layout_constraintTop_toTopOf="parent" />
22
23      <!--We will open a pop-up view when clicked to this button-->>
24      <com.google.android.material.floatingactionbutton.FloatingActionButton
25          android:id="@+id/fab"
26          style="@style/Widget.MaterialComponents.FloatingActionButton"
27          android:layout_width="wrap_content"
28          android:layout_height="wrap_content"
29          android:layout_margin="16dp"
30          android:scaleType="centerInside"
31          android:src="@drawable/ic_baseline_add_24"
32          app:backgroundTint="@color/blue_700"
33          app:fabSize="normal"
34          app:layout_constraintBottom_toBottomOf="parent"
35          app:layout_constraintEnd_toEndOf="parent"
36          app:tint="@color/white" />
37
38      <!--We will show this text view when data list is empty-->>
39      <TextView
40          android:id="@+id/empty_text"
41          android:layout_width="wrap_content"
42          android:layout_height="wrap_content"
43          android:text="List is empty"
44          android:layout_marginTop="32dp"
45          android:textSize="20sp"
46          android:visibility="gone"
47          app:layout_constraintEnd_toEndOf="parent"
48          app:layout_constraintStart_toStartOf="parent"
49          app:layout_constraintTop_toBottomOf="@+id/textView" />
50
51      <!--We will adapt the data list to this RecyclerView-->
52      <androidx.recyclerview.widget.RecyclerView
53          android:id="@+id/recyclerView"
54          android:layout_width="0dp"
55          android:layout_height="0dp"
56          app:layout_constraintBottom_toBottomOf="parent"
57          app:layout_constraintEnd_toEndOf="parent"
58          app:layout_constraintStart_toStartOf="parent"
59          app:layout_constraintTop_toBottomOf="@+id/textView">
60      </androidx.recyclerview.widget.RecyclerView>
61  </androidx.constraintlayout.widget.ConstraintLayout>
```

## 2 - Create Object

The create function will create a new Task with the title and description.

To add a TODO, we enter the title and description values in the pop-up that appears on the screen, set it to the ParseObject and save this object. We save this object in the database by using the function that Parse has provided us.

:::hint{type="info"}
**Note:**

- In this project we will make our own custom alert dialog. You can design your Alert dialog as you want and set it to the view of the dialog you will use later.
:::

:::CodeblockTabs
```java
1    openInputPopupDialogButton.setOnClickListener(fabButtonView -> {
2             AlertDialog.Builder alertDialogBuilder = new AlertDialog.Builder(MainActivity.this);
3             alertDialogBuilder.setTitle("Create a TODO");
4             alertDialogBuilder.setCancelable(true);
5             initPopupViewControls();
6             //We are setting our custom popup view by AlertDialog.Builder
7             alertDialogBuilder.setView(popupInputDialogView);
8             final AlertDialog alertDialog = alertDialogBuilder.create();
9             alertDialog.show();
10            saveTodoButton.setOnClickListener(saveButtonView -> saveTodo(alertDialog));
11            cancelUserDataButton.setOnClickListener(cancelButtonView -> alertDialog.cancel());
12        });   
13
14    //This is our saveTodo function
15    private void saveTodo(AlertDialog alertDialog) {
16        ParseObject todo = new ParseObject("Todo");
17        if (titleInput.getText().toString().length() != 0 && descriptionInput.getText().toString().length() != 0) {
18            alertDialog.cancel();
19            progressDialog.show();
20            todo.put("title", titleInput.getText().toString());
21            todo.put("description", descriptionInput.getText().toString());
22            todo.saveInBackground(e -> {
23                progressDialog.dismiss();
24                if (e == null) {
25                    //We saved the object and fetching data again
26                    getTodoList();
27                } else {
28                    //We have an error.We are showing error message here.
29                    showAlert("Error", e.getMessage());
30                }
31            });
32        } else {
33            showAlert("Error", "Please enter a title and description");
34        }
35    }
```

```kotlin
1    openInputPopupDialogButton?.setOnClickListener { fabButtonView ->
2             val alertDialogBuilder = AlertDialog.Builder(this@MainActivity)
3             alertDialogBuilder.setTitle("Create a TODO")
4             alertDialogBuilder.setCancelable(true)
5            initPopupViewControls()
6            //We are setting our custom popup view by AlertDialog.Builder
7            alertDialogBuilder.setView(popupInputDialogView)
8            val alertDialog = alertDialogBuilder.create()
9            alertDialog.show()
10            saveTodoButton?.setOnClickListener { saveButtonView ->
11                saveData(alertDialog)
12            }
13            cancelUserDataButton?.setOnClickListener { cancelButtonView ->
14                alertDialog.cancel()
15            }
16        }
17
18    //This is our saveTodo function
19    private fun saveData(alertDialog: AlertDialog) {
20        val todo = ParseObject("Todo")
21        if (titleInput?.text.toString().isNotEmpty() && descriptionInput?.text.toString().isNotEmpty()) {
22            alertDialog.cancel()
23            progressDialog?.show()
24            todo.put("title", titleInput?.text.toString())
25            todo.put("description", descriptionInput?.text.toString())
26            todo.saveInBackground { e ->
27                progressDialog?.dismiss()
28                if (e == null) {
29                    //We saved the object and fetching data again
30                    getTodoList()
31                } else {
32                    //We have an error.We are showing error message here.
33                    showAlert("Error", e.message!!)
34                }
35            }
36        } else {
37            showAlert("Error", "Please enter a title and description")
38        }
39    }
```
:::

## 3 - Read Object

With the function that Parse has provided us, we can fetch all the data in a class as ParseObject list. We create a query like the one below and fetch all the data in the Todo class.

:::CodeblockTabs
```java
1     private void getTodoList() {
2         progressDialog.show();
3         ParseQuery<ParseObject> query = ParseQuery.getQuery("Todo");
4         query.orderByDescending("createdAt");
5         query.findInBackground((objects, e) -> {
6             progressDialog.dismiss();
7             if (e == null) {
8                 //We are initializing Todo object list to our adapter
9                 initTodoList(objects);
10            } else {
11                showAlert("Error", e.getMessage());
12            }
13        });
14    }
```

```kotlin
1     private fun getTodoList() {
2          progressDialog?.show()
3          val query = ParseQuery.getQuery<ParseObject>("Todo")
4          query.orderByDescending("createdAt")
5          query.findInBackground { objects, e ->
6              progressDialog?.dismiss()
7              if (e == null) {
8                  //We are initializing Todo object list to our adapter
9                  initTodoList(objects)
10             } else {
11                 showAlert("Error", e.message!!)
12             }
13         }
14    }
```
:::

In this function, we give the returned list as a parameter to our adapter, set this adapter, to our RecyclerView, and we print the values of each object of this list into its own views. And if list has no item, we are setting our empty\_text, view’s as VISIBLE.

:::CodeblockTabs
```java
1    private void initTodoList(List<ParseObject> list) {
2         if (list == null || list.isEmpty()) {
3             empty_text.setVisibility(View.VISIBLE);
4             return;
5         }
6         empty_text.setVisibility(View.GONE);
7
8         TodoAdapter adapter = new TodoAdapter(list, this);
9
10        recyclerView.setLayoutManager(new LinearLayoutManager(this));
11        recyclerView.setAdapter(adapter);
12    }
```

```kotlin
1    private fun initTodoList(list: List<ParseObject>?) {
2         if (list == null || list.isEmpty()) {
3             empty_text!!.visibility = View.VISIBLE
4             return
5         }
6         empty_text?.visibility = View.GONE
7
8         val adapter = TodoAdapter(list as ArrayList<ParseObject>, this)
9
10        recyclerView?.layoutManager = LinearLayoutManager(this)
11        recyclerView?.adapter = adapter
12    }
```
:::

## 4 - Update Object

With the edit button in the view of our adapter, we are performing our updates. With the MutableLivedata, object provided by Android, we can listen to the click event of the edit button on our home page. When this button is clicked, we open the same pop-up and this time we populate this pop up with the title and description values of the object we clicked. Then, when the user changes this description and title and press save, first we fetch from the database with the id of this object, then we set the new variables and save object again.

:::hint{type="info"}
**Note:**

- MutableLiveData is a subclass of LiveData which is used for some of it’s properties (setValue/postValue) and using these properties we can easily notify the ui.
:::

:::CodeblockTabs
```java
1     adapter.onEditListener.observe(this, parseObject -> {
2              AlertDialog.Builder alertDialogBuilder = new AlertDialog.Builder(MainActivity.this);
3              alertDialogBuilder.setTitle("Update a TODO");
4              alertDialogBuilder.setCancelable(true);
5              //We are initializing PopUp Views with title and description parameters of ParseObject
6              initPopupViewControls(parseObject.getString("title"), parseObject.getString("description"));
7              alertDialogBuilder.setView(popupInputDialogView);
8              final AlertDialog alertDialog = alertDialogBuilder.create();
9              alertDialog.show();
10             saveTodoButton.setOnClickListener(saveTodoButtonView -> {
11                 if (titleInput.getText().toString().length() != 0 && descriptionInput.getText().toString().length() != 0) {
12                     alertDialog.cancel();
13                     progressDialog.show();
14                     parseObject.put("title", titleInput.getText().toString());
15                     parseObject.put("description", descriptionInput.getText().toString());
16                     parseObject.saveInBackground(e1 -> {
17                         progressDialog.dismiss();
18                         if (e1 == null) {
19                             getTodoList();
20                         } else {
21                             showAlert("Error", e1.getMessage());
22                         }
23                     });
24                 } else {
25                     showAlert("Error", "Please enter a title and description");
26                 }
27             });
28             cancelUserDataButton.setOnClickListener(cancelButtonView -> alertDialog.cancel());
29         });
```

```kotlin
1     adapter.clickListenerToEdit.observe(this@MainActivity, { parseObject ->
2              val alertDialogBuilder = AlertDialog.Builder(this@MainActivity)
3              alertDialogBuilder.setTitle("Update a TODO")
4              alertDialogBuilder.setCancelable(true)
5
6              //We are initializing PopUp Views with title and description parameters of ParseObject
7
8              initPopupViewControls(
9                  parseObject.getString("title")!!,
10                 parseObject.getString("description")!!
11             )
12
13             alertDialogBuilder.setView(popupInputDialogView)
14             val alertDialog = alertDialogBuilder.create()
15             alertDialog.show()
16
17             saveTodoButton?.setOnClickListener { saveButtonView ->
18                 if (titleInput?.text.toString().isNotEmpty() && descriptionInput?.text.toString().isNotEmpty()) {
19                     alertDialog.cancel()
20                     progressDialog?.show()
21                     parseObject.put("title", titleInput?.text.toString())
22                     parseObject.put("description", descriptionInput?.text.toString())
23                     parseObject.saveInBackground { e1 ->
24                         progressDialog?.dismiss()
25                         if (e1 == null) {
26                             getTodoList()
27                         } else {
28                             showAlert("Error", e1.message!!)
29                         }
30                     }
31                 } else {
32                     showAlert("Error", "Please enter a title and description")
33                 }
34             }
35         })
```
:::

## 5 - Delete Object

We listen to the click event of the delete button in the view of our adapter with the MutableLivedataobject from the home page, as in the edit button. When the delete button is clicked, we give the object id of the ParseObject as a parameter to the delete function that Parse has provided us and delete this object from the database.

:::CodeblockTabs
```java
1    adapter.onDeleteListener.observe(this, parseObject -> {
2             progressDialog.show();
3             parseObject.deleteInBackground(e -> {
4                 progressDialog.dismiss();
5                 if (e == null) {
6                     //We deleted the object and fetching data again.
7                     getTodoList();
8                 } else {
9                     showAlert("Error",e.getMessage());
10                }
11            });
12        });
```

```kotlin
1    adapter.onDeleteListener.observe(this@MainActivity, { parseObject ->
2             progressDialog?.show()
3             parseObject.deleteInBackground { e ->
4                 progressDialog?.dismiss()
5                 if (e == null) {
6                     //We deleted the object and fetching data again.
7                     getTodoList()
8                 } else {
9                     showAlert("Error", e.message!!)
10                }
11            }
12        })
```
:::

## It’s done!

At this point, you have learned how to do the basic CRUD operations with Parse on Android.
