# Source: https://docs-containers.back4app.com/docs/react/quickstart.md

---
title: Quickstart
slug: docs/react/quickstart
description: In this guide you learn how to install and connect the Parse Server SDK to your React project
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T20:06:35.283Z
updatedAt: 2025-01-16T20:25:18.541Z
---

# Quickstart



## Introduction

In this section, you will learn how to get started with Back4App using an existing or new project using React. You will install the Parse SDK, initialize Parse using your App keys, and make your first API call saving and reading data objects from Back4App.

## Prerequisites

:::hint{type="info"}
- To complete this tutorial, you will need:

  An [**app created**](https://www.back4app.com/docs/get-started/new-parse-app) on Back4App;
  A recent version of[**&#x20;Node.js**](https://nodejs.org/), including yarn and npx
:::

## 1 - Creating a React project

If you already have a working React project, you can skip to the next step.

Run the following command on the directory in which you would want to store the project, informing its name as well, in this case, back4app-guide-react:

:::BlockQuote
npx create-react-app back4app-guide-react
:::

If Node.js is properly configured, you should see the project being created in your terminal prompt. After completion, you will see a message informing you that the process was successful.

Open the project in your favorite code editor and let’s start integrating Parse.

## 2 - Install dependencies

Let’s now install the only needed dependency, Parse JavaScript SDK, to integrate your App with Back4App servers. Run the following command on your project root directory:

:::BlockQuote
yarn add parse
:::

## 3 - Get your App Keys

After creating your App on Back4App, go to your App’s Dashboard and get your App Keys under App Settings->Security & Keys(check the image below). Note that you will always need two keys to connect with Back4App, the Application ID and Javascript KEY.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/AT6Q_UOcRE73pvLmreIA9_image.png)

## 4 - Initialize Parse and connect to Back4App

Go to your App.js and initialize the Parse SDK using both the Application ID and the Javascript KEY (check the previous step).

```javascript
1   // Import Parse minified version
2   import Parse from 'parse/dist/parse.min.js';
3
4   // Your Parse initialization configuration goes here
5   const PARSE_APPLICATION_ID = 'YOUR_APPLICATION_ID_HERE';
6   const PARSE_HOST_URL = 'https://parseapi.back4app.com/';
7   const PARSE_JAVASCRIPT_KEY = 'YOUR_JAVASCRIPT_KEY_HERE';
8   Parse.initialize(PARSE_APPLICATION_ID, PARSE_JAVASCRIPT_KEY);
9   Parse.serverURL = PARSE_HOST_URL;
```

## 5 - Save and Read a simple Data Object

Your App is initialized and can securely connect to Back4app cloud services. Let’s now create a component containing two simple functions inside to save and retrieve data from your Back4App database. Create a new file named PersonComponent.js in your src directory and add the following code:

```javascript
1   import React, { useState } from 'react';
2   import Parse from 'parse/dist/parse.min.js';
3
4   export const PersonComponent = () => {
5     // State variables
6     const [person, setPerson] = useState(null);
7
8     async function addPerson() {
9       try {
10        // create a new Parse Object instance
11        const Person = new Parse.Object('Person');
12        // define the attributes you want for your Object
13        Person.set('name', 'John');
14        Person.set('email', 'john@back4app.com');
15        // save it on Back4App Data Store
16        await Person.save();
17        alert('Person saved!');
18      } catch (error) {
19        console.log('Error saving new person: ', error);
20      }
21    }
22
23    async function fetchPerson() {
24      // create your Parse Query using the Person Class you've created
25      const query = new Parse.Query('Person');
26      // use the equalTo filter to look for user which the name is John. this filter can be used in any data type
27      query.equalTo('name', 'John');
28      // run the query
29      const Person = await query.first();
30      // access the Parse Object attributes
31      console.log('person name: ', Person.get('name'));
32      console.log('person email: ', Person.get('email'));
33      console.log('person id: ', Person.id);
34      setPerson(Person);
35    }
36
37    return (
38      <div>
39        <button onClick={addPerson}>Add Person</button>
40        <button onClick={fetchPerson}>Fetch Person</button>
41        {person !== null && (
42          <div>
43            <p>{`Name: ${person.get('name')}`}</p>
44            <p>{`Email: ${person.get('email')}`}</p>
45          </div>
46        )}
47      </div>
48    );
49  };
```

The addPerson method creates a new Parse.Object representing a Person class, sets its properties then saves it on the Back4App cloud data store. The method fetchPerson retrieves a Parse.Object which has the attribute name equals to John. When the query resolves, you will be able to access the person’s attributes using the get method.

Note also the interface elements in this component, they consist of two buttons calling the methods and also two paragraphs retrieving the fetched Person through a state variable.

We now need to import and use this component in your main App.js file. Your App.js file should look something like this, after removing most of the placeholder code in it.

```javascript
1   import './App.css';
2   import Parse from 'parse/dist/parse.min.js';
3   import { PersonComponent } from './PersonComponent';
4
5   // Your Parse initialization configuration goes here
6   const PARSE_APPLICATION_ID = 'YOUR_PARSE_APPLICATION_ID';
7   const PARSE_HOST_URL = 'https://parseapi.back4app.com/';
8   const PARSE_JAVASCRIPT_KEY = 'YOUR_PARSE_JAVASCRIPT_KEY';
9   Parse.initialize(PARSE_APPLICATION_ID, PARSE_JAVASCRIPT_KEY);
10  Parse.serverURL = PARSE_HOST_URL;
11
12  function App() {
13    return (
14      <div className="App">
15        <header className="App-header">
16          <PersonComponent />
17        </header>
18      </div>
19    );
20  }
21
22  export default App;
```

## 6 - Test your App

1. Open your project’s terminal.
2. Run yarn start. Your browser should open after building with the app running. Click the button to add a new Person first, then click to fetch the same Person.
3. You’ve saved and retrieved a data object from Back4App. You can also check the data on your [**App Dashboard**](https://parse-dashboard.back4app.com/apps/) and clicking on Person class.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xv98ndOU435vt5WzmJ7Oq_image.png)

## What to do next

As you have seen, the easiest way to integrate Back4App into your React project is through the [**Parse Javascript SDK**](https://www.npmjs.com/package/parse). The Parse SDK delivers an excellent development experience through a lightweight and easy-to-use layer that provides minimal configuration and code re-usability.
