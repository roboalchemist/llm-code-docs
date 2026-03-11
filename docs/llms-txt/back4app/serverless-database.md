# Source: https://docs-containers.back4app.com/docs/javascript/serverless-database.md

---
title: Database Operations
slug: docs/javascript/serverless-database
description: Learn how to retrieve, insert, update and delete Parse Objects with no servers on your JavaScript Project.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-04T18:52:57.085Z
updatedAt: 2025-03-21T19:08:11.187Z
---

# Performing Serverless Database Operations

## Introduction

This section explains how to implement the **CRUD (Create, Read, Update and Delete) Operations**
in a JavaScript environment through Back4app.
It also provides code snippets and an online environment to execute and test your code with no local setup.

:::hint{type="success"}
See more about Parse SDK at [**Parse JavaScript SDK API Reference**](https://parseplatform.org/Parse-SDK-JS/api/4.3.1/) and [**Parse open source documentation for JavaScript SDK**](https://docs.parseplatform.org/js/guide/).
:::

## Prerequisites

:::hint{type="info"}
There are no additional requisites other than having the basic knowledge of JavaScript.
**Optional:** To complete this tutorial using your own app, you will need:

- An app created and configured for JavaScript at Back4app.
  - **Note: Follow the&#x20;**[**JavaScript Install Parse SDK tutorial**](https://www.back4app.com/docs/javascript/parse-javascript-sdk)**&#x20;to learn how you can do that.**
:::

## 1 - Set up the environment

This guide uses the [**JSbin**](https://jsbin.com/) platform as a code editor.
It’s very easy to use, all you need to do is open its main page and click on the HTML, JavaScript and Console buttons:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/F1dr16wL8lXj-IFiHtm5i_image.png)

The first step to start coding is to include the Parse API and to add your App’s keys.

For this tutorial, a public Back4app app has been created so that you can check your changes on the database without having to create your own app.

:::hint{type="info"}
**Optional:&#x20;**&#x54;o check the Parse database for this example, you need to create your own app and access the Parse Dashboard option.
:::

To include Parse API in your app, add the following line of code inside the HTML’s head tag:

```html
<script type="text/javascript" src="https://unpkg.com/parse/dist/parse.min.js"></script>
```

Then add your your credentials at the beginning of the JavaScript file. The default keys are the ones related to our public app.

```javascript
//Paste your Application Key and JavaScript Key, respectively
Parse.initialize("Your-Application-Id", "Your-Javascript-Key");
Parse.serverURL = "https://parseapi.back4app.com/";
```

In this tutorial, we will build the **CRUD Operations&#x20;**&#x62;ased on a Pet class that has name and age fields, in which name is a string and the age is a number. Because of that, the code should start by creating a subclass of the Pet class so that it can be used later in our functions, as shown below:

```javascript
var Pet = Parse.Object.extend("Pet");
```

All of the basic operations will require the user to say what is the desired Pet’s name. That way, create a global variable “textName”. It’s also a good idea to create a “textAge” one, which will be used in create and update methods.



```javascript
var textName = "myName";
var textAge = 10;
```

## 2 - Create

The create function will create a new Pet with the name and age that you provided in the “textName” and “textAge” variables.

To build that function, just follow these steps:

1. Make a new instance of the Parse’s Pet class with the command
2. Use the set function to set the parameters for this object.
3. Call the save function, which will effectively register the pet to your database in theParse Dashboard.

:::hint{type="info"}
You can open the [**Back4app JavaScript Create Function**](https://jsbin.com/bozuguh/edit?html,js,console) to see the code that has already been implemented.
:::

The code for the create function is written below:

:::CodeblockTabs
create.js

```javascript
create();

function create() {
    mypet = new Pet();
    mypet.set("name", textName);
    mypet.set("agePet", textAge);

    mypet.save().then(function(pet){
         console.log('Pet created successful with name: ' + pet.get("name") + ' and age: ' + pet.get("agePet"));
    }).catch(function(error){
         console.log('Error: ' + error.message);
    });
}
```
:::

:::hint{type="info"}
To test it, paste this code snippet in the JavaScript file in the [**JSbin**](https://jsbin.com/?html,js,output), click on
the Run button in the console part and wait for the output.
It should print that the pet was created successfully.
To confirm that the new object is in the database, you can access the Parse Dashboard or you can code the read function.
:::

## 3 - Read

The read function is responsible for querying the database and returning the object that matches your search criteria. It can also be used to check the existence of an object.
Here’s the step-by-step guide for building your own read function:

1. Make an instance of the Parse’s Query class.
2. Add constraints to your query to restraint the search. More constraints options can be found in [**Parse Query Documentation.**](http://docs.parseplatform.org/js/guide/#query-constraints)
3. Do a Query’s search method. This tutorial will use query.first to get only the first element that matches your criteria.
4. If the operations succeed, a pet object will be returned. If no object is found, the return object will have an value of **undefined**.

:::hint{type="info"}
You can open the [**Back4app JavaScript Read Function**](https://jsbin.com/roziroy/edit?html,js,output) to see the code that has already been implemented.
:::

The code for the read function is the following:

:::CodeblockTabs
read.js

```javascript
read();

function read() {
    query = new Parse.Query(Pet);
    query.equalTo("name", textName);
    query.first().then(function(pet){
        if(pet){
           console.log('Pet found successful with name: ' + pet.get("name") + ' and age: ' + pet.get("agePet"));
        } else {
           console.log("Nothing found, please try again");
        }
    }).catch(function(error){
        console.log("Error: " + error.code + " " + error.message);       
    });
}
```
:::

:::hint{type="info"}
To test the read function, paste the snippet to your JSBin JavaScript file. When the code runs, it wil print the age of the pet found (if found) or else will print that no pet was found.
:::

:::hint{type="danger"}
If while testing the printed age does not correspond to the age of your object, it means that there are
&#x20;more objects with the same name, but your query only returns one of them. So, to really test the read function, create an object with another name, one that no one has created yet, then run the function, which will correctly print the age of the object.
:::

## 4 - Update

For the update function, a pet is passed as parameter and the function changes it’s age to the one you provided in the “textAge” variable. To find the pet which will be passed, we use a modified version of our read function.

Below are the steps to make your own update function:

1. Write a modified read function called readThenUpdate, which calls the update function when it finds a pet successfully.
2. In the update function, use the set function to modify the parameters of your pet.
3. Call the save function for this pet to push the changes to the database.

:::hint{type="info"}
You can open the [**Back4app JavaScript Update Function**](https://jsbin.com/jidinim/edit?html,js,output) to see the code that has already been implemented.
:::

Here’s the code for the readThenUpdate function and update function:

:::CodeblockTabs
update.js

```javascript
readThenUpdate();

function readThenUpdate() {
    query = new Parse.Query(Pet);
    query.equalTo("name", textName);
    query.first().then(function (pet) {
      if (pet) {
        console.log('Pet found with name: ' + pet.get("name") + ' and age: ' + pet.get("agePet"));
        update(pet);
      } else {
        console.log("Nothing found, please try again");
      }
    }).catch(function (error) {
      console.log("Error: " + error.code + " " + error.message);
    });
}

function update(foundPet) {
    textName = "myNameUpdated";
    textAge = 20;
    console.log(textAge);
    foundPet.set('name', textName);
    foundPet.set('agePet', textAge);

    foundPet.save().then(function (pet) {
      console.log('Pet updated! Name: ' + pet.get("name") + ' and new age: ' + pet.get("agePet"));
    }).catch(function(error) {
      console.log('Error: ' + error.message);
    });
}
```
:::

:::hint{type="info"}
To confirm if the update function is working, paste the code above to the JavaScript file in the JSBin page.
Use an unusual name for your object to not conflict with other users, then follow these steps:

1\. Create an object with your desired name.
2\. Check that the object is created with your read function.
3\. Call your readThenUpdate function made in this topic with an age different than the original one.
4\. Check if the age of the Pet has changed by calling your read function again.
:::

## 5 - Delete

The delete function erases a pet received by the read function. It is an irreversible action, which means that you should be careful while using it, especially because your read function might return more objects than you actually want to delete. Because of that, it’s recommended to delete only one object at a time. The steps for writing your own delete function can be found below:

1. In the end of the success of your “read” function (readThenDelete in this example), make a call for the delete function.
2. In the deletePet function, call the destroy method on the received object “foundPet”.

:::hint{type="info"}
You can open the [**Back4app JavaScript Delete Function**](https://jsbin.com/vubiqoq/edit?html,js,output) to see the code that has already been implemented.
:::

Here’s the code for the readThenDelete function and deletePet function:

:::CodeblockTabs
delete.js

```javascript
readThenDelete();

function readThenDelete() {
    query = new Parse.Query(Pet);
    query.equalTo("name", textName);
    query.first().then(function (pet) {
        if (pet) {
            console.log('Pet found with name: ' + pet.get("name") + ' and age: ' + pet.get("agePet"));
            deletePet(pet);
        } else {
            console.log("Nothing found, please try again");
            return null;
        }
    }).catch(function (error) {
        console.log("Error: " + error.code + " " + error.message);
        return null;
    });
}

function deletePet(foundPet) {
    foundPet.destroy().then(function(response) {
      console.log('Pet '+ foundPet.get("name") + ' erased successfully');
    }).catch(function(response, error) {
      console.log('Error: '+ error.message);
    });
}
```
:::

:::hint{type="info"}
To test it, it’s recommended to create an object with an unusual name just like the other functions to
&#x20;not conflict with objects from other users.
Just paste the snippet to the JSBin and run the code with the name of your object and the object that will be deleted.
Then, you can call your read function to confirm that there are no objects with that name.
:::

:::hint{type="danger"}
If the read returns an object, which it shouldn’t, it probably means that you have more objects with the
&#x20;same name and it returned one of them as the delete function just deletes one object.
You can check your object by accessing your Parse Dashboard.
:::

## It’s done!

At this point, you have learned how to do the basic CRUD operations with JavaScript.
