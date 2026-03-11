# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/data-objects/one-to-one-relationship.md

---
title: 1:1 Relationship
slug: docs/react-native/parse-sdk/data-objects/one-to-one-relationship
description: In this guide you'll learn how to create and query one-to-one data object associations in Parse on React Native
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T12:00:36.734Z
updatedAt: 2025-01-28T13:50:33.161Z
---

# One to one Relationship



## Introduction

At the core of many backends, you will find the ability to store data. Using Parse, you can store data objects establishing relations between them. Data relations standardize how each data object is related or associated with other ones. That can give you extra power when building and running complex queries. There are three main relation types:

- one-to-many, where one object can be related to many other objects;
- one-to-one, establishing direct relations between two objects and only them;
- many-to-many, which can create many complex relations between many objects.

In this guide, we will focus on one-to-one relations. These relations are common in applications involving sensible data and user management which require unique fields that need to be enforced, such as ID numbers and phone numbers. Data storage backends usually will demand explicit declarations of these associations and Parse does not have an automatic solution for achieving such associations.

However, there are ways to implement 1:1 relations in Parse by using Parse.Cloud functions on your server, enforcing that table relations remain unique before saving data. This is done by creating beforeSave functions in both related classes and prevent saving if the father class already possesses one instance in the child class, and vice-versa.

You can also treat these cases in your application Parse code, querying the server before saving and guaranteeing said relation. This will be the way shown in this guide, but note that using cloud functions is much cleaner and more advised.

In this guide, you will implement a React Native book registration application that contains the three main kinds of data associations. You will learn how to create and query one-to-one data relations using Back4App and React Native.

:::hint{type="success"}
**At any time, you can access this project via our GitHub repositories to checkout the styles and complete code.**

- [**JavaScript Example Repository**](https://github.com/templates-back4app/react-native-js-associations)
- [**TypeScript Example Repository**](https://github.com/templates-back4app/react-native-ts-associations)
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and connected to [**Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
- If you want to test/use the screen layout provided by this guide, you should set up thereact-native-paper[**library**](https://github.com/callstack/react-native-paper).
:::

## Goal

To perform and demonstrate one-to-one database relations in React Native using Parse in a realistic scenario.

## 1 - Understanding the Book class

Since in this guide we will be using a book registration application example, you need to first understand how the object relations are laid out in this database. The main object class that you’ll be using is the Book class, which will store each book entry in the registration. These are the other four object classes:

- Publisher: book publisher name, one-to-many relation withBook
- Genre: book genre, one-to-many relation withBook. Note that for this example we will consider that a book can only have one genre;
- Author: book author, many-to-many relation withBook, since a book can have more than one author and an author can have more than one book as well;
- ISDB: book ISDB identifying number, one-to-one relation withBook, since this number is unique for each book.

Here is a visual representation of these database tables:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/yLKySy88tgZLtiFkWN2PO_image.png)

For simplicity, we will assume that each object class has only a string type name attribute (title for the Book), apart from any additional relational attribute.

## 2 - Creating one-to-many relations

Before going into this step we recommend you to clone and run the React Native Library app exmaple ([**JavaScript Example Repository**](https://github.com/templates-back4app/react-native-js-associations), [**TypeScript Example Repository**](https://github.com/templates-back4app/react-native-ts-associations)). This application has two main screens: one responsible for listing the registered books and the other for creating new books. In the book registration form, there are direct links to the other related objects and a TextInput field assigned to the book’s ISBD value, which will be used to create your one-to-one relation.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/eS4Xh4BrAAX1IPI9GO_ID_image.png" signedSrc size="50" width="352" height="741" position="center" caption}

Let’s take a look at the book creation method that is called when submitting this form:

:::CodeblockTabs
JavaScript

```javascript
1	const createBook = async function () {
2	  try {
3	    // These values come from state variables linked to
4	    // the screen form fields, retrieving the user choices
5	    // as a complete Parse.Object, when applicable;
6	    const bookTitleValue = bookTitle;
7	    const bookISBDValue = bookISBD;
8	    // For example, bookPublisher holds the value from
9	    // RadioButton.Group field with its options being every
10	    // Publisher parse object instance saved on server, which is
11	    // queried on screen load via useEffect
12	    const bookPublisherObject = bookPublisher;
13	    const bookGenreObject = bookGenre;
14	    // bookAuthors can be an array of Parse.Objects, since the book
15	    // may have more than one Author
16	    const bookAuthorsObjects = bookAuthors;
17	
18	    // Creates a new parse object instance
19	    let Book = new Parse.Object('Book');
20	
21	    // Set data to parse object
22	    // Simple title field
23	    Book.set('title', bookTitleValue);
24	
25	    // 1:1 relation, need to check for uniqueness of value before creating a new ISBD object
26	    let isbdQuery = new Parse.Query('ISBD');
27	    isbdQuery.equalTo('name', bookISBDValue);
28	    let isbdQueryResult = await isbdQuery.first();
29	    if (isbdQueryResult !== null && isbdQueryResult !== undefined) {
30	      // If first returns a valid object instance, it means that there
31	      // is at least one instance of ISBD with the informed value
32	      Alert.alert(
33	        'Error!',
34	        'There is already an ISBD instance with this value!',
35	      );
36	      return false;
37	    } else {
38	      // Create a new ISBD object instance to create a one-to-one relation on saving
39	      let ISBD = new Parse.Object('ISBD');
40	      ISBD.set('name', bookISBDValue);
41	      ISBD = await ISBD.save();
42	      // Set the new object to the new book object ISBD field
43	      Book.set('isbd', ISBD);
44	    }
45	
46	    // One-to-many relations can be set in two ways:
47	    // add direct object to field (Parse will convert to pointer on save)
48	    Book.set('publisher', bookPublisherObject);
49	    // or add pointer to field
50	    Book.set('genre', bookGenreObject.toPointer());
51	
52	    // many-to-many relation
53	    // Create a new relation so data can be added
54	    let authorsRelation = Book.relation('authors');
55	    // bookAuthorsObjects is an array of Parse.Objects,
56	    // you can add to relation by adding the whole array or object by object
57	    authorsRelation.add(bookAuthorsObjects);
58	
59	    // After setting the values, save it on the server
60	    try {
61	      await Book.save();
62	      // Success
63	      Alert.alert('Success!');
64	      navigation.goBack();
65	      return true;
66	    } catch (error) {
67	      // Error can be caused by lack of Internet connection
68	      Alert.alert('Error!', error.message);
69	      return false;
70	    }
71	  } catch (error) {
72	    // Error can be caused by lack of value selection
73	    Alert.alert(
74	      'Error!',
75	      'Make sure to select valid choices in Publisher, Genre and Author fields!',
76	    );
77	    return false;
78	  }
79	};
```

TodoList.tsx

```typescript
1	const createBook = async function (): Promise<boolean> {
2	  try {
3	    // These values come from state variables linked to
4	    // the screen form fields, retrieving the user choices
5	    // as a complete Parse.Object, when applicable;
6	    const bookTitleValue: string = bookTitle;
7	    const bookISBDValue: string = bookISBD;
8	    // For example, bookPublisher holds the value from
9	    // RadioButton.Group field with its options being every
10	    // Publisher parse object instance saved on server, which is
11	    // queried on screen load via useEffect
12	    const bookPublisherObject: Parse.Object = bookPublisher;
13	    const bookGenreObject: Parse.Object = bookGenre;
14	    // bookAuthors can be an array of Parse.Objects, since the book
15	    // may have more than one Author
16	    const bookAuthorsObjects: [Parse.Object] = bookAuthors;
17	
18	    // Creates a new parse object instance
19	    let Book: Parse.Object = new Parse.Object('Book');
20	
21	    // Set data to parse object
22	    // Simple title field
23	    Book.set('title', bookTitleValue);
24	
25	    // 1:1 relation, need to check for uniqueness of value before creating a new ISBD object
26	    let isbdQuery: Parse.Query = new Parse.Query('ISBD');
27	    isbdQuery.equalTo('name', bookISBDValue);
28	    let isbdQueryResult: Parse.Object = await isbdQuery.first();
29	    if (isbdQueryResult !== null && isbdQueryResult !== undefined) {
30	      // If first returns a valid object instance, it means that there
31	      // is at least one instance of ISBD with the informed value
32	      Alert.alert(
33	        'Error!',
34	        'There is already an ISBD instance with this value!',
35	      );
36	      return false;
37	    } else {
38	      // Create a new ISBD object instance to create a one-to-one relation on saving
39	      let ISBD: Parse.Object = new Parse.Object('ISBD');
40	      ISBD.set('name', bookISBDValue);
41	      ISBD = await ISBD.save();
42	      // Set the new object to the new book object ISBD field
43	      Book.set('isbd', ISBD);
44	    }
45	
46	    // One-to-many relations can be set in two ways:
47	    // add direct object to field (Parse will convert to pointer on save)
48	    Book.set('publisher', bookPublisherObject);
49	    // or add pointer to field
50	    Book.set('genre', bookGenreObject.toPointer());
51	
52	    // many-to-many relation
53	    // Create a new relation so data can be added
54	    let authorsRelation = Book.relation('authors');
55	    // bookAuthorsObjects is an array of Parse.Objects,
56	    // you can add to relation by adding the whole array or object by object
57	    authorsRelation.add(bookAuthorsObjects);
58	
59	    // After setting the values, save it on the server
60	    try {
61	      await Book.save();
62	      // Success
63	      Alert.alert('Success!');
64	      navigation.goBack();
65	      return true;
66	    } catch (error) {
67	      // Error can be caused by lack of Internet connection
68	      Alert.alert('Error!', error.message);
69	      return false;
70	    }
71	  } catch (error) {
72	    // Error can be caused by lack of value selection
73	    Alert.alert(
74	      'Error!',
75	      'Make sure to select valid choices in Publisher, Genre and Author fields!',
76	    );
77	    return false;
78	  }
79	};
```
:::

Look how the bookISBDValue is set to the new book Parse.Object instance. Creating and saving one-to-one and one-to-many relations in Parse are similar processes, in which you pass as an argument the Parse.Object instance using the Parse.Object.set method, which takes two arguments: the field name and the value to be set.

The catch here is that, before saving, you need to enforce that there are no ISBD objects containing the informed ISBD ID string value in your database and that there are no Book objects already related to it as well. The second part will always be true in this case, since you are creating a new Book object every time. Enforcing the ISBD uniqueness can be achieved by using the following highlighted query:

:::CodeblockTabs
JavaScript

```javascript
1	let isbdQuery = new Parse.Query('ISBD');
2	isbdQuery.equalTo('name', bookISBDValue);
3	let isbdQueryResult = await isbdQuery.first();
4	if (isbdQueryResult !== null && isbdQueryResult !== undefined) {
5	  // If first returns a valid object instance, it means that there
6	  // is at least one instance of ISBD with the informed value
7	  Alert.alert(
8	    'Error!',
9	    'There is already an ISBD instance with this value!',
10	  );
11	  return false;
12	}
```

TodoList.tsx

```typescript
1	let isbdQuery: Parse.Query = new Parse.Query('ISBD');
2	isbdQuery.equalTo('name', bookISBDValue);
3	let isbdQueryResult: Parse.Object = await isbdQuery.first();
4	if (isbdQueryResult !== null && isbdQueryResult !== undefined) {
5	  // If first returns a valid object instance, it means that there
6	  // is at least one instance of ISBD with the informed value
7	  Alert.alert(
8	    'Error!',
9	    'There is already an ISBD instance with this value!',
10	  );
11	  return false;
12	}
```
:::

After successfully saving your objects, Parse will create a pointer data type column and a direct link on your dashboard for quick access under the hood.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/F5vFvtQwa5BWn9HGb2wkA_image.png)

## 3 - Querying one-to-one relations

Querying one-to-one related objects is pretty straightforward as much of it is handled by Parse. Take a look at the query function in the book registers list screen:

:::CodeblockTabs
JavaScript

```javascript
1	const queryBooks = async function () {
2	  // These values come from state variables linked to
3	  // the screen query RadioButton.Group fields, with its options being every
4	  // parse object instance saved on server from the referred class, which is
5	  // queried on screen load via useEffect; these variables retrievie the user choices
6	  // as a complete Parse.Object;
7	  const queryPublisherValue = queryPublisher;
8	  const queryGenreValue = queryGenre;
9	  const queryAuthorValue = queryAuthor;
10	  const queryIsbdValue = queryIsbd;
11	
12	  // Reading parse objects is done by using Parse.Query
13	  const parseQuery = new Parse.Query('Book');
14	
15	  // One-to-many queries
16	  if (queryPublisherValue !== '') {
17	    parseQuery.equalTo('publisher', queryPublisherValue);
18	  }
19	  if (queryGenreValue !== '') {
20	    parseQuery.equalTo('genre', queryGenreValue);
21	  }
22	
23	  // One-to-one query
24	  if (queryIsbdValue !== '') {
25	    parseQuery.equalTo('isbd', queryIsbdValue);
26	  }
27	
28	  // Many-to-many query
29	  // In this case, we need to retrieve books related to the chosen author
30	  if (queryAuthorValue !== '') {
31	    parseQuery.equalTo('authors', queryAuthorValue);
32	  }
33	
34	  try {
35	    let books = await parseQuery.find();
36	    // Many-to-many objects retrieval
37	    // In this example we need to get every related author Parse.Object
38	    // and add it to our query result objects
39	    for (let book of books) {
40	      // This query is done by creating a relation and querying it
41	      let bookAuthorsRelation = book.relation('authors');
42	      book.authorsObjects = await bookAuthorsRelation.query().find();
43	    }
44	    setQueriedBooks(books);
45	    return true;
46	  } catch (error) {
47	    // Error can be caused by lack of Internet connection
48	    Alert.alert('Error!', error.message);
49	    return false;
50	  }
51	};
```

TodoList.tsx

```typescript
1	const queryBooks = async function (): Promise<boolean> {
2	  // These values come from state variables linked to
3	  // the screen query RadioButton.Group fields, with its options being every
4	  // parse object instance saved on server from the referred class, which is
5	  // queried on screen load via useEffect; these variables retrievie the user choices
6	  // as a complete Parse.Object;
7	  const queryPublisherValue: Parse.Object = queryPublisher;
8	  const queryGenreValue: Parse.Object = queryGenre;
9	  const queryAuthorValue: Parse.Object = queryAuthor;
10	  const queryIsbdValue: Parse.Object = queryIsbd;
11	
12	  // Reading parse objects is done by using Parse.Query
13	  const parseQuery: Parse.Query = new Parse.Query('Book');
14	
15	  // One-to-many queries
16	  if (queryPublisherValue !== '') {
17	    parseQuery.equalTo('publisher', queryPublisherValue);
18	  }
19	  if (queryGenreValue !== '') {
20	    parseQuery.equalTo('genre', queryGenreValue);
21	  }
22	
23	  // One-to-one query
24	  if (queryIsbdValue !== '') {
25	    parseQuery.equalTo('isbd', queryIsbdValue);
26	  }
27	
28	  // Many-to-many query
29	  // In this case, we need to retrieve books related to the chosen author
30	  if (queryAuthorValue !== '') {
31	    parseQuery.equalTo('authors', queryAuthorValue);
32	  }
33	
34	  try {
35	    let books: [Parse.Object] = await parseQuery.find();
36	    // Many-to-many objects retrieval
37	    // In this example we need to get every related author Parse.Object
38	    // and add it to our query result objects
39	    for (let book of books) {
40	      // This query is done by creating a relation and querying it
41	      let bookAuthorsRelation = book.relation('authors');
42	      book.authorsObjects = await bookAuthorsRelation.query().find();
43	    }
44	    setQueriedBooks(books);
45	    return true;
46	  } catch (error) {
47	    // Error can be caused by lack of Internet connection
48	    Alert.alert('Error!', error.message);
49	    return false;
50	  }
51	};
```
:::

In this case, to query any books related to a specific ISBD, you need only to perform a Parse.Query.equalTo method passing the Parse.Object instance as the parameter. After querying, Parse will store inside the resulting objects the complete instances of any one-to-one relational fields. To retrieve and show data from these object instances, you can chain the Parse.Object.get method like this: bookParseObject.get(('isbd').get('name'). Here is how the list screen looks like by using these getters to retrieve the ISBD name from the list items:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/0HJqpWWdXlfL-U8ZApFOP_image.png" signedSrc size="50" width="346" height="734" position="center" caption}

## Conclusion

At the end of this guide, you learned how to create and query one-to-one relations in Parse on React Native. In the next guide, we will show you how to register users.
