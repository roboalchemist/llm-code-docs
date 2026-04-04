# Source: https://docs-containers.back4app.com/docs/react/data-objects/react-crud-tutorial.md

---
title: Basic Operations
slug: docs/react/data-objects/react-crud-tutorial
description: In this guide you will learn how to perform basic data operations (CRUD) in Parse on React
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-12T14:26:46.555Z
updatedAt: 2025-01-17T14:14:01.245Z
---

# React CRUD tutorial

## Introduction

Storing data on Parse is built around the Parse.Object class. Each Parse.Object contains key-value pairs of JSON-compatible data. This data is schemaless, which means that you don’t need to specify ahead of time what keys exist on each Parse.Object. You can simply set whatever key-value pairs you want, and our backend will store it.

You can also specify the datatypes according to your application needs and persist types such as number, boolean, string, DateTime, list, GeoPointers, and Object, encoding them to JSON before saving. Parse also supports store and query relational data by using the types Pointers and Relations.

In this guide, you will learn how to perform basic data operations through a CRUD example app, which will show you how to create, read, update and delete data from your Parse server database in React. You will first create your component functions for each CRUD operation, using them later in a complete screen layout, resulting in a to-do list app.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React App created and [**connected to Back4App**](https://www.back4app.com/docs/react/quickstart)
- If you want to test/use the screen layout provided by this guide, you should set up the Ant Design [**library**](https://ant.design/docs/react/introduce).
:::

## Goal

To build a basic CRUD application in React using Parse.

## 1 - Creating data objects

The first step to manage your data in your Parse database is to have some on it. Let’s now make a createTodo function that will create a new instance of Parse.Object with the “Todo” subclass. The to-do will have a title (string) describing the task and a done(boolean) field indicating whether the task is completed.

:::CodeblockTabs
JavaScript

```javascript
1   const createTodo = async function () {
2     // This value comes from a state variable
3     const newTodoTitleValue = newTodoTitle;
4     // Creates a new Todo parse object instance
5     let Todo = new Parse.Object('Todo');
6     Todo.set('title', newTodoTitleValue);
7     Todo.set('done', false);
8     // After setting the to-do values, save it on the server
9     try {
10      await Todo.save();
11      // Success
12      alert('Success! To-do created!');
13      // Refresh to-dos list to show the new one (you will create this function later)
14      readTodos();
15      return true;
16    } catch (error) {
17      // Error can be caused by lack of Internet connection
18      alert(`Error! ${error.message}`);
19      return false;
20    };
21  };
```

```typescript
1   const createTodo = async function (): Promise<boolean> {
2     // This value comes from a state variable
3     const newTodoTitleValue: string = newTodoTitle;
4     // Creates a new Todo parse object instance
5     let Todo: Parse.Object = new Parse.Object('Todo');
6     Todo.set('title', newTodoTitleValue);
7     Todo.set('done', false);
8     // After setting the to-do values, save it on the server
9     try {
10      await Todo.save();
11      // Success
12      alert('Success! To-do created!');
13      // Refresh to-dos list to show the new one (you will create this function later)
14      readTodos();
15      return true;
16    } catch (error: any) {
17      // Error can be caused by lack of Internet connection
18      alert(`Error! ${error.message}`);
19      return false;
20    };
21  };
```
:::

Notice that if your database does not have a Todo table (or subclass) in it yet, Parse will create it automatically and also add any columns set inside the Parse.Object instance using the Parse.Object.set() method, which takes two arguments: the field name and the value to be set.

## 2 - Reading data objects

After creating some data in your database, your application can now be able to read it from the server and show it to your user. Go ahead and create a readTodos function, which will perform a Parse.Query, storing the result inside a state variable.

:::CodeblockTabs
JavaScript

```javascript
1   const readTodos = async function () {
2     // Reading parse objects is done by using Parse.Query
3     const parseQuery = new Parse.Query('Todo');
4     try {
5       let todos = await parseQuery.find();
6       // Be aware that empty or invalid queries return as an empty array
7       // Set results to state variable
8       setReadResults(todos);
9       return true;
10    } catch (error) {
11      // Error can be caused by lack of Internet connection
12      alert(`Error! ${error.message}`);
13      return false;
14    };
15  };
```

```typescript
1   const readTodos = async function (): Promise<boolean> {
2     // Reading parse objects is done by using Parse.Query
3     const parseQuery: Parse.Query = new Parse.Query('Todo');
4     try {
5       let todos: Parse.Object[] = await parseQuery.find();
6       // Be aware that empty or invalid queries return as an empty array
7       // Set results to state variable
8       setReadResults(todos);
9       return true;
10    } catch (error: any) {
11      // Error can be caused by lack of Internet connection
12      alert(`Error! ${error.message}`);
13      return false;
14    };
15  };
```
:::

Many constraints and orderings can be applied to your queries using the Parse.Query class, but for now, we will stick to this simple query, which will retrieve every saved Todo object.

## 3 - Updating data objects

Updating a Parse.Object instance is very similar to creating a new one, except that in this case, you need to assign the previously created objectId to it and then save, after setting your new values.

:::CodeblockTabs
JavaScript

```javascript
1   const updateTodo = async function (todoId, done) {
2     // Create a new Todo parse object instance and set todo id
3     let Todo = new Parse.Object('Todo');
4     Todo.set('objectId', todoId);
5     // Set new done value and save Parse Object changes
6     Todo.set('done', done);
7     try {
8       await Todo.save();
9       // Success
10      alert('Success! To-do updated!');
11      // Refresh to-dos list
12      readTodos();
13      return true;
14    } catch (error) {
15      // Error can be caused by lack of Internet connection
16      alert(`Error! ${error.message}`);
17      return false;
18    };
19  };
```

```typescript
1   const updateTodo = async function (
2     todoId: string,
3     done: boolean,
4   ): Promise<boolean> {
5     // Create a new Todo parse object instance and set todo id
6     let Todo: Parse.Object = new Parse.Object('Todo');
7     Todo.set('objectId', todoId);
8     // Set new done value and save Parse Object changes
9     Todo.set('done', done);
10    try {
11      await Todo.save();
12      // Success
13      alert('Success! To-do updated!');
14      // Refresh to-dos list
15      readTodos();
16      return true;
17    } catch (error: any) {
18      // Error can be caused by lack of Internet connection
19      alert(`Error! ${error.message}`);
20      return false;
21    };
22  };
```
:::

Since this example app represents a to-do list, your update function takes an additional argument, the done value, which will represent if the specific task is completed or not.

## 4 - Deleting data objects

To delete a data object, you need to call the .destroy() method in the Parse.Object instance representing it. Please be careful because this operation is not reversible.

:::CodeblockTabs
JavaScript

```javascript
1	const deleteTodo = async function (todoId) {
2	  // Create a new Todo parse object instance and set todo id
3	  const Todo = new Parse.Object('Todo');
4	  Todo.set('objectId', todoId);
5	  // .destroy should be called to delete a parse object
6	  try {
7	    await Todo.destroy();
8	    alert('Success! To-do deleted!');
9	    // Refresh to-dos list to remove this one
10	    readTodos();
11	    return true;
12	  } catch (error) {
13	    // Error can be caused by lack of Internet connection
14	    alert(`Error ${error.message}`);
15	    return false;
16	  };
17	};
```

```typescript
1	const deleteTodo = async function (todoId: string): Promise<boolean> {
2	  // Create a new Todo parse object instance and set todo id
3	  let Todo: Parse.Object = new Parse.Object('Todo');
4	  Todo.set('objectId', todoId);
5	  // .destroy should be called to delete a parse object
6	  try {
7	    await Todo.destroy();
8	    alert('Success! To-do deleted!');
9	    // Refresh to-dos list to remove this one
10	    readTodos();
11	    return true;
12	  } catch (error: any) {
13	    // Error can be caused by lack of Internet connection
14	    alert(`Error! ${error.message}`);
15	    return false;
16	  };
17	};
```
:::

Let’s now use these four functions in a complete component, so you can test it and make sure that every CRUD operation is working properly.

## 5 - Using CRUD in a React component

Here is the complete component code, including styled user interface elements (using Ant Design), state variables, and calls to your CRUD functions. You should create a separate component in a file called TodoList.js/TodoList.tsx in your src directory containing the following code or add it directly to your main application file (App.js/App.tsx).

:::CodeblockTabs
TodoList.js

```javascript
1   import React, { useState } from 'react';
2   import Parse from 'parse/dist/parse.min.js';
3   import './App.css';
4   import { Button, Input, List } from 'antd';
5   import {
6     CheckOutlined,
7     CloseOutlined,
8     PlusOutlined,
9     RedoOutlined,
10  } from '@ant-design/icons';
11
12  export const TodoList = () => {
13    // State variables
14    const [readResults, setReadResults] = useState([]);
15    const [newTodoTitle, setNewTodoTitle] = useState('');
16
17    // Functions used by the screen components
18    const createTodo = async function () {
19      // This value comes from a state variable
20      const newTodoTitleValue = newTodoTitle;
21      // Creates a new Todo parse object instance
22      let Todo = new Parse.Object('Todo');
23      Todo.set('title', newTodoTitleValue);
24      Todo.set('done', false);
25      // After setting the to-do values, save it on the server
26      try {
27        await Todo.save();
28        // Success
29        alert('Success! To-do created!');
30        // Refresh to-dos list to show the new one (you will create this function later)
31        readTodos();
32        return true;
33      } catch (error) {
34        // Error can be caused by lack of Internet connection
35        alert(`Error! ${error.message}`);
36        return false;
37      }
38    };
39
40    const readTodos = async function () {
41      // Reading parse objects is done by using Parse.Query
42      const parseQuery = new Parse.Query('Todo');
43      try {
44        let todos = await parseQuery.find();
45        // Be aware that empty or invalid queries return as an empty array
46        // Set results to state variable
47        setReadResults(todos);
48        return true;
49      } catch (error) {
50        // Error can be caused by lack of Internet connection
51        alert(`Error! ${error.message}`);
52        return false;
53      }
54    };
55
56    const updateTodo = async function (todoId, done) {
57      // Create a new to-do parse object instance and set todo id
58      let Todo = new Parse.Object('Todo');
59      Todo.set('objectId', todoId);
60      // Set new done value and save Parse Object changes
61      Todo.set('done', done);
62      try {
63        await Todo.save();
64        // Success
65        alert('Success! To-do updated!');
66        // Refresh todos list
67        readTodos();
68        return true;
69      } catch (error) {
70        // Error can be caused by lack of Internet connection
71        alert(`Error! ${error.message}`);
72        return false;
73      }
74    };
75
76    const deleteTodo = async function (todoId) {
77      // Create a new Todo parse object instance and set todo id
78      let Todo = new Parse.Object('Todo');
79      Todo.set('objectId', todoId);
80      // .destroy should be called to delete a parse object
81      try {
82        await Todo.destroy();
83        alert('Success! To-do deleted!');
84        // Refresh to-dos list to remove this one
85        readTodos();
86        return true;
87      } catch (error) {
88        // Error can be caused by lack of Internet connection
89        alert(`Error! ${error.message}`);
90        return false;
91      }
92    };
93
94    return (
95      <div>
96        <div className="header">
97          <img
98            className="header_logo"
99            alt="Back4App Logo"
100           src={
101             'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
102           }
103         />
104         <p className="header_text_bold">{'React on Back4App'}</p>
105         <p className="header_text">{'To-do List'}</p>
106       </div>
107       <div className="container">
108         <div className="flex_between">
109           <h2 className="list_heading">Todo List</h2>
110           {/* To-do read (refresh) button */}
111           <Button
112             type="primary"
113             shape="circle"
114             color={'#208AEC'}
115             size={'default'}
116             onClick={readTodos}
117             icon={<RedoOutlined />}
118           ></Button>
119         </div>
120         <div className="new_todo_wrapper flex_between">
121           {/* Todo create text input */}
122           <Input
123             value={newTodoTitle}
124             onChange={(event) => setNewTodoTitle(event.target.value)}
125             placeholder="New Todo"
126             size="large"
127           />
128           {/* Todo create button */}
129           <Button
130             type="primary"
131             className="create_todo_button"
132             color={'#208AEC'}
133             size={'large'}
134             onClick={createTodo}
135             icon={<PlusOutlined />}
136           >
137             Add
138           </Button>
139         </div>
140         <div>
141           {/* Todo read results list */}
142           {readResults !== null &&
143             readResults !== undefined &&
144             readResults.length > 0 && (
145               <List
146                 dataSource={readResults}
147                 renderItem={(item) => (
148                   <List.Item className="todo_item">
149                     <p
150                       className={
151                         item.get('done') === true
152                           ? 'todo_text_done'
153                           : 'todo_text'
154                       }
155                     >
156                       {item.get('title')}
157                     </p>
158                     <div className="flex_row">
159                       {/* Todo update button */}
160                       {item.get('done') !== true && (
161                         <Button
162                           type="primary"
163                           shape="circle"
164                           className="todo_button"
165                           onClick={() => updateTodo(item.id, true)}
166                           icon={
167                             <CheckOutlined className="todo_button_icon_done" />
168                           }
169                         ></Button>
170                       )}
171                       {/* Todo delete button */}
172                       <Button
173                         type="primary"
174                         shape="circle"
175                         className="todo_button"
176                         onClick={() => deleteTodo(item.id)}
177                         icon={
178                           <CloseOutlined className="todo_button_icon_remove" />
179                         }
180                       ></Button>
181                     </div>
182                   </List.Item>
183                 )}
184               />
185             )}
186         </div>
187       </div>
188     </div>
189   );
190 };
```

TodoList.tsx

```typescript
1   import React, { useState, FC, ReactElement } from 'react';
2   import './App.css';
3   import { Button, Input, List } from 'antd';
4   import {
5     CheckOutlined,
6     CloseOutlined,
7     PlusOutlined,
8     RedoOutlined,
9   } from '@ant-design/icons';
10  const Parse = require('parse/dist/parse.min.js');
11
12  export const TodoList: FC<{}> = (): ReactElement => {
13    // State variables
14    const initialReadResults: Parse.Object[] = [];
15    const [readResults, setReadResults] = useState(initialReadResults);
16    const [newTodoTitle, setNewTodoTitle] = useState('');
17
18    // Functions used by the screen components
19    const createTodo = async function (): Promise<boolean> {
20      // This value comes from a state variable
21      const newTodoTitleValue: string = newTodoTitle;
22      // Creates a new Todo parse object instance
23      let Todo: Parse.Object = new Parse.Object('Todo');
24      Todo.set('title', newTodoTitleValue);
25      Todo.set('done', false);
26      // After setting the to-do values, save it on the server
27      try {
28        await Todo.save();
29        // Success
30        alert('Success! To-do created!');
31        // Refresh to-dos list to show the new one (you will create this function later)
32        readTodos();
33        return true;
34      } catch (error: any) {
35        // Error can be caused by lack of Internet connection
36        alert('Error!' + error.message);
37        return false;
38      }
39    };
40
41    const readTodos = async function (): Promise<boolean> {
42      // Reading parse objects is done by using Parse.Query
43      const parseQuery: Parse.Query = new Parse.Query('Todo');
44      try {
45        let todos: Parse.Object[] = await parseQuery.find();
46        // Be aware that empty or invalid queries return as an empty array
47        // Set results to state variable
48        setReadResults(todos);
49        return true;
50      } catch (error: any) {
51        // Error can be caused by lack of Internet connection
52        alert('Error!' + error.message);
53        return false;
54      }
55    };
56
57    const updateTodo = async function (todoId: string, done: boolean): Promise<boolean> {
58      // Create a new to-do parse object instance and set todo id
59      let Todo: Parse.Object = new Parse.Object('Todo');
60      Todo.set('objectId', todoId);
61      // Set new done value and save Parse Object changes
62      Todo.set('done', done);
63      try {
64        await Todo.save();
65        // Success
66        alert('Success! To-do updated!');
67        // Refresh todos list
68        readTodos();
69        return true;
70      } catch (error: any) {
71        // Error can be caused by lack of Internet connection
72        alert('Error!' + error.message);
73        return false;
74      }
75    };
76
77    const deleteTodo = async function (todoId: string): Promise<boolean> {
78      // Create a new Todo parse object instance and set todo id
79      let Todo: Parse.Object = new Parse.Object('Todo');
80      Todo.set('objectId', todoId);
81      // .destroy should be called to delete a parse object
82      try {
83        await Todo.destroy();
84        alert('Success! To-do deleted!');
85        // Refresh to-dos list to remove this one
86        readTodos();
87        return true;
88      } catch (error: any) {
89        // Error can be caused by lack of Internet connection
90        alert('Error!' + error.message);
91        return false;
92      }
93    };
94
95    return (
96      <div>
97        <div className="header">
98          <img
99            className="header_logo"
100           alt="Back4App Logo"
101           src={
102             'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
103           }
104         />
105         <p className="header_text_bold">{'React on Back4App'}</p>
106         <p className="header_text">{'To-do List'}</p>
107       </div>
108       <div className="container">
109         <div className="flex_between">
110           <h2 className="list_heading">Todo List</h2>
111           {/* To-do read (refresh) button */}
112           <Button
113             type="primary"
114             shape="circle"
115             color={'#208AEC'}
116             onClick={readTodos}
117             icon={<RedoOutlined />}
118           ></Button>
119         </div>
120         <div className="new_todo_wrapper flex_between">
121           {/* Todo create text input */}
122           <Input
123             value={newTodoTitle}
124             onChange={(event: {target: {value: string}}) => setNewTodoTitle(event.target.value)}
125             placeholder="New Todo"
126             size="large"
127           />
128           {/* Todo create button */}
129           <Button
130             type="primary"
131             className="create_todo_button"
132             color={'#208AEC'}
133             size={'large'}
134             onClick={createTodo}
135             icon={<PlusOutlined />}
136           >
137             Add
138           </Button>
139         </div>
140         <div>
141           {/* Todo read results list */}
142           {readResults !== null &&
143             readResults !== undefined &&
144             readResults.length > 0 && (
145               <List
146                 dataSource={readResults}
147                 renderItem={(item: Parse.Object) => (
148                   <List.Item className="todo_item">
149                     <p
150                       className={
151                         item.get('done') === true
152                           ? 'todo_text_done'
153                           : 'todo_text'
154                       }
155                     >
156                       {item.get('title')}
157                     </p>
158                     <div className="flex_row">
159                       {/* Todo update button */}
160                       {item.get('done') !== true && (
161                         <Button
162                           type="primary"
163                           shape="circle"
164                           className="todo_button"
165                           onClick={() => updateTodo(item.id, true)}
166                           icon={
167                             <CheckOutlined className="todo_button_icon_done" />
168                           }
169                         ></Button>
170                       )}
171                       {/* Todo delete button */}
172                       <Button
173                         type="primary"
174                         shape="circle"
175                         className="todo_button"
176                         onClick={() => deleteTodo(item.id)}
177                         icon={
178                           <CloseOutlined className="todo_button_icon_remove" />
179                         }
180                       ></Button>
181                     </div>
182                   </List.Item>
183                 )}
184               />
185             )}
186         </div>
187       </div>
188     </div>
189   );
190 };
```
:::

Also, add these CSS styles at the end of your App.css file:

```css
1   /* ... */
2   /* Your other styles */
3
4   /* Back4App Guide Styles */
5
6   html {
7	   box-sizing: border-box;
8	   outline: none;
9	   overflow: auto;
10  }
11
12  *,
13  *:before,
14  *:after {
15	  margin: 0;
16	  padding: 0;
17	  box-sizing: inherit;
18  }
19
20  h1,
21  h2,
22  h3,
23  h4,
24  h5,
25  h6 {
26    margin: 0;
27  }
28
29  p {
30    margin: 0;
31  }
32
33  body {
34	  margin: 0;
35	  background-color: #fff;
36  }
37
38  .container {
39    width: 100%;
40    max-width: 600px;
41    margin: auto;
42    padding: 20px 0;
43  }
44
45  .wrapper {
46    width: '90%';
47    align-self: 'center';
48  }
49
50  .header {
51    align-items: center;
52    padding: 25px 0;
53    background-color: #208AEC;
54  }
55
56  .header_logo {
57    height: 55px;
58    margin-bottom: 20px;
59    object-fit: contain;
60  }
61
62  .header_text_bold {
63    margin-bottom: 3px;
64    color: rgba(255, 255, 255, 0.9);
65    font-size: 16px;
66    font-weight: bold;
67  }
68
69  .header_text {
70    color: rgba(255, 255, 255, 0.9);
71    font-size: 15px;
72  }
73
74  .flex_row {
75    display: flex;
76  }
77
78  .flex_between {
79    display: flex;
80    align-items: center;
81    justify-content: space-between;
82  }
83
84  .list_heading {
85    font-weight: bold;
86  }
87
88  .new_todo_wrapper {
89    margin-top: 20px;
90    margin-bottom: 10px;
91  }
92
93  .new_todo_wrapper > input {
94    margin-right: 20px;
95  }
96
97  .todo_item {
98    border-bottom-width: 1;
99    border-bottom-color: 'rgba(0, 0, 0, 0.12)';
100  }
101
102  .todo_text {
103    font-size: 15px;
104  }
105
106  .todo_text_done {
107    color: rgba(0, 0, 0, 0.3);
108    font-size: 15px;
109    text-decoration-line: line-through;
110  }
111
112  .todo_button {
113    width: 32px;
114    height: 32px;
115    margin-left: 5px;
116    background-color: transparent;
117    border-radius: 50px;
118    border: none;
119    cursor: pointer;
120  }
121
122  .todo_button:hover,
123  .todo_button:focus {
124    background-color: rgba(0, 0, 0, 0.1);
125  }
126
127  .todo_button_icon_done {
128    color: #52c41a;
129    font-size: 16px;
130  }
131
132  .todo_button_icon_remove {
133    color: #f5222d;
134    font-size: 16px;
135  }
```

If your component is properly set up, you should see something like this after running the app:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/D0I4xfjjvDNq4inZAbUcd_image.png)

Go ahead and add some to-dos by typing its titles in the input box one at a time and pressing on the Add button. Note that after every successful creation, the createTodo function triggers the readTodos one, refreshing your task list automatically. You should now have a sizeable to-do list like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vEEcPYfh_NX3Y6eEhsNzP_image.png)

You can now mark your tasks as done by clicking in the checkmark beside it, causing their done value to be updated to true and changing its icon status on the left.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/mrjtEdu2yMPdDh7Xh8c8t_image.png)

The only remaining data operation is now the delete one, which can be done by pressing on the trash can icon at the far right of your to-do list object. After successfully deleting an object, you should get an alert message like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/qs_4jFok4k9SHdbIkNehG_image.png)

## Conclusion

At the end of this guide, you learned how to perform basic data operations (CRUD) in Parse on React. In the next guide, we will show you which data types are supported in Parse and how to use them.
