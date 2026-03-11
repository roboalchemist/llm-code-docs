# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/real-time/react-native-real-time.md

---
title: Usage
slug: docs/react-native/parse-sdk/real-time/react-native-real-time
description: In this section you will learn how to build queries with **Parse React Native** and make use of its core features in **React Native** Apps.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T13:52:20.440Z
updatedAt: 2025-01-17T19:52:01.598Z
---

# Using the useParseQuery hook to build a real time React Native App

## Introduction

In this guide, you will explore the main features of @parse/react-native lib using a ToDO React Native app example. You will use the useParseQuery hook to query tasks in real-time and store results locally on this App. Using various Parse Queries, you will discover how to use the new Parse Lib on your project.

:::hint{type="danger"}
Parse React Native is currently on the Alpha version. The lib is under testing, so we recommend to proceed with caution. Your feedback is very appreciated, so feel free to use the lib and send us your questions and first impressions by dropping an email to community\@back4app.com
:::

## Goal

Explore the main use cases for the Parse React Native lib by creating a ToDo App.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An app created on Back4App.
- Follow the [**Enable Live Query**](https://www.back4app.com/docs/platform/parse-live-query) tutorial.
- **Note:&#x20;**&#x46;ollow the [**Parse React Native tutorial**](https://www.back4app.com/docs/react-native/parse-sdk/real-time/react-hook-real-time) to learn how to get started with @parse/react-native
:::

## 1 - Setup the initial project

Before getting started, you will need to get the bootstrap React Native project that we have setup as a starting point for this tutorial. It is a simple react-native init project with all dependencies and styles pre-defined for you to focus on exploring @parse/react-native features. You may [**download de Zip**](https://github.com/templates-back4app/react-native-todo-app/archive/main.zip) or clone the project.

:::BlockQuote
git clone https:*//github.com/templates-back4app/react-native-todo-app.git*
:::

Next, install the project dependencies:

:::BlockQuote
cd react-native-todo-app

&#x20;\# Using yarn
yarn install

&#x20; \# Using npm
npm install
:::

For iOS, install pods:

:::BlockQuote
cd ios **&&** npx po&#x64;**-**&#x69;nstall
:::

In the previous guide, [**Getting started**](https://www.back4app.com/docs/react-native/parse-react-native-sdk/getting-started), you learned how to use initializeParse to enable connection with Back4app servers. Set up your App Id and JavaScriptKey in the entry point component located at src/index.js:&#x20;

```javascript
1   // src/index.js
2   initializeParse(
3   'https://parseapi.back4app.com/',
4   'APPLICATION_ID',
5   'JAVASCRIPT_KEY'
6   );
```

Go ahead and run the project:

:::BlockQuote
\# For iOS
npx react-native run-ios

\# For Android
npx react-native run-android
:::

After that you will have successfully setup the starter project and the App will look like the following:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ARgyL376qWC8HXTY40ure_image.png" signedSrc size="50" width="306" height="645" position="center" caption}

The project’s directory structure:

:::BlockQuote
react-native-todo-app
├── src/
│   ├── config/
│   │   └── ReactotronConfig.js
│   ├── images/
│   │   ├── back4app\_logo.png
│   │   └── bg.jpg
│   ├── components/
│   │   └── CardTodoButton/
│   │       └── index.js // card button item component
│   │   └── Menu/
│   │       └── index.js // menu with card buttons
│   │   └── TaskList/
│   │       └── index.js // List of tasks component
│   ├── pages/
│   │   └── AddTodo/
│   │       └── index.js // Add todo page &#x20;
│   │   └── Learning/
│   │       └── index.js // learning page &#x20;
│   │   └── Main/
│   │       └── index.js // main page
│   │   └── Shopping/
│   │       └── index.js // shopping page
│   │   └── Work/
│   │       └── index.js // work page
│   ├── services/
│   │   └── api.js
│   ├── index.js // App entrypoint
│   └── routes.js // navigation routes config
├── .editorconfig
├── .eslintrc.json
├── .gitignore
├── babel.config.js
├── dependencies.json
├── devDependencies.json
├── index.js
├── jsconfig.js
├── LICENSE
├── package.json
└── README.md
:::

The initial project have main 4 pages:

- **Learning Page**: shows tasks that belongs to the learning category
- **Shopping Page**: shows tasks that belongs to the shopping category
- **Work Page**: shows tasks that belongs to the work category
- **AddTodo Page**: basic form to create a new task

## 2 - Creating a new Task

A commom feature in a ToDo app is allowing users to create new tasks. For that, the create task function will use the Parse Javascript SDK to create a new Parse Object and save it on Back4app. On the AddTodo page from the starter project, you will have a basic form with an input to insert the task description, some check boxes to select the task category and a submit button. In this tutorial, you will create Parse.Object for the tasks which will have the following attributes:

:::hint{type="info"}
Look at the Parse Javascript SDK [**Save Data**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-save-data) guide for more info on creating Parse objects.&#x20;
:::

```javascript
1	{
2	  description: 'simple string of task descrition',
3	  author: 'person creating the task',
4	  completed: false, // or true
5	  createdAt: Date, // automatically created by back4app
6	}
```

Now implement the method to create a task when the user clicks on submit. At thepages/AddTodo/index.jscomponent, let’s implement thehandleSubmitmethod:

```javascript
1	  async function handleSubmit() {
2	    try {
3	      const Task = new Parse.Object.extend('Task');
4	      // Create a new instance of that class.
5	      const task = new Task();
6	      task.set('description', description);
7	      task.set('category', category);
8	      task.set('author', 'Anonymous');
9	      task.set('completed', false);
10	      await task.save();
11	
12	      Alert.alert('New Task Created.');
13	    } catch (error) {
14	      console.log('Error while creating task: ', error);
15	    }
16	  }
```

After that, you will now be able to create some tasks. Feel free to create as many tasks as you want. In the next steps you will be querying them.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/0QEgLvOn78QvuJGwDzcBF_image.png" signedSrc size="50" width="301" height="647" position="center" caption}

## 3 - Querying & Filtering Tasks

Now that you have created some tasks, it is time to use Parse React Native Lib. You will write some queries and pass them to useParseQuery hook. The queries will list all the non-completed tasks in the learning category. This is the first use case of the hook, you will build a one-time fetch query, by setting enableLiveQuery\:false, that runs when the learning page component renders. The enableLiveQuery is true by default, and changing to false will disable the real-time changes subscription.

On the pages/Learning/index.js component, let’s write our Parse.query:

```javascript
1     const Task = new Parse.Object.extend('Task');
2     const query = new Parse.Query(Task);
3     query.equalTo('completed', false);
4     query.equalTo('category', 'learning');
```

Pass the query as argument to theuseParseQueryhook:

:::BlockQuote
const \{results} = useParseQuery(query, \{enableLiveQuery: false});
:::

The above code shows a basic use for the Parse hook. The useParseQuery hook is a new resource that you can use with any Parse.Query. Use [**all Parse.Query capabitilies**](https://docs.parseplatform.org/js/guide/#queries) to retrieve your data objects and the hook will make this experience even better. After getting the results, pass them down to the TaskList component to display tasks on the App:

```javascript
1	//Learning/index.js
2	import React, {useEffect} from 'react';
3	import {ActivityIndicator} from 'react-native';
4	import TaskList from '../../components/TaskList';
5	import Parse from 'parse/react-native.js';
6	import {useParseQuery} from '@parse/react-native';
7	
8	const Learning = () => {
9	  const Task = new Parse.Object.extend('Task');
10	  const query = new Parse.Query(Task);
11	  query.equalTo('completed', false);
12	  query.equalTo('category', 'learning');
13	
14	  const {results, isLoading} = useParseQuery(query, {enableLiveQuery: false});
15	
16	  if (isLoading) {
17	    return <ActivityIndicator/>;
18	  }
19	
20	  return <TaskList todos={results} />;
21	};
22	
23	export default Learning;
```

Your App should successfuly show the list of tasks like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ElXKoPQfM6X0CAuZR10JY_image.png" signedSrc size="50" width="308" height="647" position="center" caption}

## 4 - Realtime changes

The second usage you are going to explore is real-time updates. The useParseQuery hook encapsulates the Parse Live Query and provides out of the box support for real-time changes. When passing a query to the hook, it creates a WebSocket connection to communicate with the Back4app LiveQuery server, which synchronizes automatically. You will add this feature to the tasks in the shopping category.

It is important to note that Live Query and Back4App subdomain must be enabled on your Back4app Dashboard App. Once you do that, add your subdomain url to initializeParse and the results from the Parse React Native hook will always have updated data. If you do not configure the subdomain, useParseQuery hook will not be able to retrieve data in real-time.

```javascript
1	// src/index.js
2	initializeParse(
3	'<yoursubdomain>.b4a.io',
4	'APPLICATION_ID',
5	'JAVASCRIPT_KEY'
6	);
```

On thepages/Shopping/index.jscomponent, let’s write ourParse.query:

```javascript
1     const Task = new Parse.Object.extend('Task');
2     const query = new Parse.Query(Task);
3     query.equalTo('completed', false);
4     query.equalTo('category', 'shopping');
```

Then, pass the query as argument to theuseParseQueryhook:

:::BlockQuote
const \{results, isLoading, isSyncing} = useParseQuery(query);
:::

Note that there is no need for extra parameters since the real-time changes is enabled by default. After getting the results, pass them down to theTaskListcomponent to display tasks on the App:

```javascript
1	import React from 'react';
2	import {ActivityIndicator} from 'react-native';
3	import TaskList from '../../components/TaskList';
4	import Parse from 'parse/react-native.js';
5	import {useParseQuery} from '@parse/react-native';
6	
7	const Shopping = () => {
8	  const Task = new Parse.Object.extend('Task');
9	  const query = new Parse.Query(Task);
10	  query.equalTo('completed', false);
11	  query.equalTo('category', 'shopping');
12	
13	  const {results, isLoading, isSyncing} = useParseQuery(query);
14	
15	  if (isLoading || isSyncing) {
16	    return <ActivityIndicator />;
17	  }
18	  return <TaskList todos={results || []} />;
19	};
20	
21	export default Shopping;
```

## 5 - Offline Support

The third use case for @parse/react-native is using offline caching of query results. This is useful in case your React Native App needs to work when users have network latency or Internet connectivity issues. Offline support improves your React Native Apps responsiveness and user expirience. The great news is that no extra steps are required! The offline-first approach and real-time subscriptions are enabled by default.

In short, simply using useParseQuery hook assures that your app will be caching query results for offline support combined with Live Query subscriptions for when your user goes back online.

## 6 - Limiting & Sorting queries

Suppose that the task list from the work category is too much for a person to handle and you want to show only a subset of them for the day. Also, order by date of creation.

On the pages/Shopping/index.js component, let’s write our Parse.query:

```javascript
1     const Task = new Parse.Object.extend('Task');
2     const query = new Parse.Query(Task);
3     query.equalTo('completed', false);
4     query.equalTo('category', 'work');
5     query.ascending('createdAt'); // order by creation date
6     query.limit(5); // limit to 5 tasks
```

Then, pass the query as argument to the useParseQuery hook and pass them down to the TaskList component to display tasks on the App:

```javascript
1	import React from 'react';
2	import {ActivityIndicator} from 'react-native';
3	import Parse from 'parse/react-native.js';
4	import {useParseQuery} from '@parse/react-native';
5	import TaskList from '../../components/TaskList';
6	// import { Container } from './styles';
7	
8	const Work = () => {
9	  const Task = new Parse.Object.extend('Task');
10	  const query = new Parse.Query(Task);
11	  query.equalTo('completed', false);
12	  query.equalTo('category', 'work');
13	  query.ascending('createdAt');
14	  query.limit(5);
15	
16	  const {results, isLoading} = useParseQuery(query, {
17	    enableLiveQuery: false,
18	  });
19	
20	  if (isLoading) {
21	    return <ActivityIndicator />;
22	  }
23	  return <TaskList todos={results} />;
24	};
25	
26	export default Work;
```

## 7 - Specifying useParseQuery arguments

You used @parse/react-native to retrive data from Back4app with features such Live Query in the previous steps. Therefore, an explanation of the interface exported is required. The useParseQuery hook accepts a Parse.Query and an UseParseQueryOptions object as its arguments. The default optional configuration object is the following:

```javascript
1   {
2     enableLiveQuery: true,
3     enableLocalDatastore: true,
4     initialLoad: []
5   }
```

- **enableLiveQuery**: Realtime Live Query feature is enabled by default
- **enableLocalDatastore**: Enables local caching of data results, default is true but you can turn off by setting to false
- **initialLoad**: If you already have some data loaded in memory then you can set them to show a preview of the data to users.

## It’s Done!

At this point, you’ve learned how to use the @parse/react-native lib by creating a React Native todo App on Back4App.
