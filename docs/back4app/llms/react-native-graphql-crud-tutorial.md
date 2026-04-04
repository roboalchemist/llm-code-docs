# Source: https://docs-containers.back4app.com/docs/react-native/graphql/data-objects/react-native-graphql-crud-tutorial.md

---
title: Basic Operations
slug: docs/react-native/graphql/data-objects/react-native-graphql-crud-tutorial
description: In this guide you'll learn how to perform basic data operations (CRUD) with GraphQL using Relay on React Native
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-20T13:59:15.487Z
updatedAt: 2025-01-16T20:14:13.119Z
---

# React Native GraphQL CRUD tutorial

## Introduction

Managing data on Back4App using GraphQL is a powerful option for any type of application, speeding up queries and simplifying the most complex ones. Back4App uses common conventions for GraphQL configuration and provides great tools to help your environment setup for development.

In this guide, you will learn how to perform basic data operations through a CRUD example app, which will show you how to create, read, update and delete data from your Parse server database in React Native using GraphQL and Relay.

You will first create your component functions for each CRUD operation, using them later in a complete screen layout, resulting in a to-do list app.

:::hint{type="success"}
**At any time, you can access this project via our GitHub repositories to checkout the styles and complete code.**

- [**JavaScript Example Repository**](https://github.com/templates-back4app/react-native-graphql-relay-js-users)
:::

## Prerequisites

- **For this tutorial we will use the Parse Server in the 4.4 version. If you want to use other versions you can check the corresponding mutation code at&#x20;**[**GraphQL Logout Guide&#x20;**](https://www.back4app.com/docs/parse-graphql/graphql-logout-mutation)**example for your respective version.**
- **A React Native App created and connected to Back4App;**
- **Conclude the&#x20;**[**Relay Environment setup tutorial**](https://www.back4app.com/docs/react-native/graphql/relay-setup)**:**
- **Good understanding of Relay Store and Relay Connection Updater; you can read more on&#x20;**[**Relay Modern Docs**](https://app.archbee.com/docs/_roxIyUMXoBue9I7uv49e/h4VZ_HqkkIJx7yL2doaHJ)**:**
- **We will be using JavaScript as the default implementation.**

## Goal

To build a basic CRUD application in React Native using Parse, GraphQL, and Relay.

## 1 - Creating the Todo class

In this first step, we need to define the class that the application will be operating with. The Todo class needs only to have a title(string) field describing the task and a done(boolean) field indicating if the task is completed. You can use a generic mutation to create the class into your database if you don’t have it, following our guide in the [**GraphQL Cookbook**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object). You can also create the class using Back4App’s dashboard, through the database browser itself or from the JS, or GraphQL consoles.

After creating this new class, remember to download the schema.json file from the dashboard and save it in your application inside the data directory. This is necessary for the Relay Compiler to automatically generate the types from queries, mutations, etc.

At this point, your Back4App dashboard will have automatically generate CRUD Mutations for the class object, to see them you can go to the GraphQL Console, open the docs tab, and search for Todo:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/2VZfpsqkBnaEhd3cJN0Rg_image.png" signedSrc size="70" width="431" height="763" position="center" caption}

## 2 - Querying and Rendering the Objects

Let’s now create a component that will be responsible for making the list query in the Back4App server, establishing a connection for the Objects, and automatically rendering and updating the list contents as they change.

Create a new file named TodoListQueryRenderer.js in your src directory with the following code:

```javascript
1	import React from 'react';
2	import { View, Text } from 'react-native';
3	import { graphql, QueryRenderer } from 'react-relay';
4	
5	// prerequisite: properly configured relay environment
6	import environment from '../../relay/environment';
7	
8	// This will be created in the next steps
9	import TodoList from './TodoList';
10	
11	const TodoListQueryRenderer = () => {
12	    return (
13	        // The QueryRenderer acts as a wrapper to any code, providing query results to
14	        // the child components and updating them as needed
15	        // Note that the query is using a fragment called TodoList_query,
16	        // which will be created in the next steps
17	        <QueryRenderer
18	            environment={environment}
19	            query={graphql`
20	            query TodoListQueryRendererQuery {
21	              ...TodoList_query
22	            }
23	          `}
24	            variables={null}
25	            render={({ error, props }) => {
26	                if (error) {
27	                    return (
28	                        <View>
29	                            <Text>{error.message}</Text>
30	                        </View>
31	                    );
32	                } else if (props) {
33	                    return <TodoList query={props} />;
34	                }
35	                return (
36	                    <View>
37	                        <Text>Loading...</Text>
38	                    </View>
39	                );
40	            }}
41	        />
42	    );
43	}
44	
45	export default TodoListQueryRenderer;
```

## 3 - Create the List component and Fragment of Object

Let’s now create our list component, which will render the data retrieved from the QueryRenderer. The component will for now contain only a simple scroll view containing a map function rendering each node. Go ahead and create a new file in your src directory called TodoList.js and add the following code:

```javascript
1	import React, {useState} from 'react';
2	import {
3	  View,
4	  SafeAreaView,
5	  Image,
6	  ScrollView,
7	  StatusBar,
8	  StyleSheet,
9	  TouchableOpacity,
10	} from 'react-native';
11	
12	import {
13	  List,
14	  Text as PaperText,
15	  Button as PaperButton,
16	  TextInput as PaperTextInput,
17	} from 'react-native-paper';
18	import {createFragmentContainer} from 'react-relay';
19	
20	const TodoList = props => {
21	  const [newTodoTitle, setNewTodoTitle] = useState('');
22	
23	  const {query} = props;
24	  const {todos} = query;
25	
26	  const renderTodos = () => {
27	    if (!todos) {
28	      return null;
29	    }
30	
31	    return todos.edges.map(({node: todo}) => (
32	      <List.Item
33	        key={todo.id}
34	        title={todo.title}
35	        titleStyle={todo.done ? Styles.todo_text_done : Styles.todo_text}
36	        style={Styles.todo_item}
37	        right={props => (
38	          <>
39	            {!todo.done && (
40	              <TouchableOpacity onPress={() => updateTodo(todo.id, true)}>
41	                <List.Icon {...props} icon="check" color={'#4CAF50'} />
42	              </TouchableOpacity>
43	            )}
44	
45	            <TouchableOpacity onPress={() => deleteTodo(todo.id)}>
46	              <List.Icon {...props} icon="close" color={'#ef5350'} />
47	            </TouchableOpacity>
48	          </>
49	        )}
50	      />
51	    ));
52	  };
53	
54	  return (
55	    <>
56	      <StatusBar backgroundColor="#208AEC" />
57	      <SafeAreaView style={Styles.container}>
58	        <View style={Styles.header}>
59	          <PaperText style={Styles.header_text_bold}>
60	            {'React Native on Back4App'}
61	          </PaperText>
62	          <PaperText style={Styles.header_text}>{'Product Creation'}</PaperText>
63	        </View>
64	        <View style={Styles.create_todo_container}>
65	        </View>
66	        <ScrollView style={Styles.todo_list}>{renderTodos()}</ScrollView>
67	      </SafeAreaView>
68	    </>
69	  );
70	};
71	
72	const TodoListFragmentContainer = createFragmentContainer(TodoList, {
73	  query: graphql`
74	    fragment TodoList_query on Query {
75	      todos(first: 50) @connection(key: "TodoList_todos", filters: []) {
76	        edges {
77	          node {
78	            id
79	            title
80	            done
81	          }
82	        }
83	      }
84	    }
85	  `,
86	});
```

The Query Renderer in Step 2 expects a fragment of data named TodoList\_query, so we added it to the list component as well at the end of the file. Remember that GraphQL fragments are structures responsible for calling the data the components need to render and specifying what needs to be returned.

## 4 - Creating the Objects

The first step to manage your data in your Back4App GraphQL database is to have some on it. We need to create a function to call to create a new Todo in our list component using a mutation responsible for it.

Let’s begin with the mutation, so create a new file named CreateTodoMutation.js in the src/mutations directory containing the following code:

```javascript
1	import { commitMutation, graphql } from "react-relay";
2	import { ROOT_ID, ConnectionHandler } from 'relay-runtime';
3	
4	const connectionCreateEdgeUpdater = (store, nodeId) => {
5	  const parentProxy = store.get(ROOT_ID);
6	  const todoConnection = ConnectionHandler.getConnection(parentProxy, 'TodoList_todos');
7	
8	  const newTodo = store.get(nodeId);
9	  const edge = ConnectionHandler.createEdge(store, todoConnection, newTodo, 'TodoEdge');
10	  
11	  // No cursor provided, append the edge at the end.
12	  ConnectionHandler.insertEdgeAfter(todoConnection, edge);
13	}
14	
15	const mutation = graphql`
16	  mutation CreateTodoMutation($input: CreateTodoInput!) {
17	    createTodo(input: $input) {
18	      todo {
19	        id
20	        title
21	        done
22	      }
23	    }
24	  }
25	`;
26	
27	function commit({ environment, input, onCompleted, onError }) {
28	  const variables = { input };
29	
30	  commitMutation(environment, {
31	    mutation,
32	    variables,
33	    onCompleted,
34	    onError,
35	    updater: (store) => {
36	      const todoId = store.getRootField('createTodo').getLinkedRecord('todo').getValue('id');
37	
38	      connectionCreateEdgeUpdater(store, todoId)
39	    }
40	  });
41	}
```

Relay Modern provides us a bunch of API endpoints to be used to update the data after mutation calls. In this function, we used some of its functions to get the new Todo created and update the already existing list on the frontend. With this approach, we avoid a new call to the backend saving time that would be spent on a new request, user internet, over fetching, and more.

Now add the following function to the TodoList component, which will call the CreateTodoMutation and will be referenced later by a button.

```javascript
1	const createTodo = () => {
2	    const input = {
3	        fields: {
4	            title: newTodoTitle,
5	            done: false,
6	        },
7	    };
8	
9	    CreateTodoMutation.commit({
10	        environment,
11	        input: input,
12	        onCompleted: () => {
13	            Alert.alert('Success!', 'Todo created!');
14	            setNewTodoTitle('');
15	        },
16	        onError: (errors) => {
17	            Alert.alert('Error!', errors);
18	        },
19	    });
20	}
```

## 5 - Updating the Objects

Updating an object is similar to creating it, with the addition that, when you are updating an object using Relay Modern, you just need to ask the fields that you want to update with the new state on the output of the mutation.

Create a new file named UpdateTodoMutation.js in the src/mutations directory containing the following code:

```javascript
1	import { commitMutation, graphql } from "react-relay";
2	
3	const mutation = graphql`
4	  mutation UpdateTodoMutation($input: UpdateTodoInput!) {
5	    updateTodo(input: $input) {
6	      todo {
7	        id
8	        title
9	        done
10	      }
11	    }
12	  }
13	`;
14	
15	function commit({ environment, input, onCompleted, onError }) {
16	  const variables = { input };
17	
18	  commitMutation(environment, {
19	    mutation,
20	    variables,
21	    onCompleted,
22	    onError,
23	  });
24	}
25	
26	export default {
27	  commit,
28	};
```

Just like in the previous step, add the following function to theTodoListcomponent, which will call theUpdateTodoMutationand will be referenced later by a button.

```javascript
1	const updateTodo = (todoId, done) => {
2	    const input = {
3	        id: todoId,
4	        fields: {
5	            done,
6	        }
7	    }
8	
9	    UpdateTodoMutation.commit({
10	        environment,
11	        input: input,
12	        onCompleted: () => {
13	            Alert.alert('Success!', 'Todo updated!');
14	        },
15	        onError: (errors) => {
16	            Alert.alert('Error!', errors);
17	        },
18	    });
19	}
```

## 6 - Deleting the Objects

When you are deleting an object, with the Relay Store APIs you can update the list and removing the old object from the frontend. We will call an updater callback, similar to the update from createTodo, but we will pass the connection and the id of the to-do to remove it from the list. In this way, we keep the frontend faithfully updated to our server.

Create a new file named DeleteTodoMutation.js in the src/mutations directory containing the following code:

```javascript
1	import { commitMutation, graphql } from "react-relay";
2	import { ROOT_ID, ConnectionHandler } from 'relay-runtime';
3	
4	const connectionDeleteEdgeUpdater = (store, nodeId) => {
5	  const parentProxy = store.get(ROOT_ID);
6	  const connection = ConnectionHandler.getConnection(parentProxy, 'TodoList_todos');
7	
8	  const newCount = connection.getValue('count');
9	  connection.setValue(newCount - 1, 'count');
10	
11	  ConnectionHandler.deleteNode(connection, nodeId);
12	}
13	
14	const mutation = graphql`
15	  mutation DeleteTodoMutation($input: DeleteTodoInput!) {
16	    deleteTodo(input: $input) {
17	      todo {
18	        id
19	      }
20	    }
21	  }
22	`;
23	
24	function commit({ environment, input, onCompleted, onError }) {
25	  const variables = { input };
26	
27	  commitMutation(environment, {
28	    mutation,
29	    variables,
30	    onCompleted,
31	    onError,
32	    updater: (store) => {
33	      connectionDeleteEdgeUpdater(store, input.id)
34	    }
35	  });
36	}
37	
38	export default {
39	  commit,
40	};
```

Just like in the previous step, add the following function to theTodoListcomponent, which will call theDeleteTodoMutationand will be referenced later by a button.

```javascript
1	const deleteTodo = (todoId) => {
2	    const input = {
3	        id: todoId,
4	    }
5	
6	    DeleteTodoMutation.commit({
7	        environment,
8	        input: input,
9	        onCompleted: () => {
10	            Alert.alert('Success!', 'Todo deleted!');
11	        },
12	        onError: (errors) => {
13	            Alert.alert('Error!', errors);
14	        },
15	    });
16	}
```

## 7 - Using CRUD in a React Native component

Let´s now complete our TodoList component code with the styled user interface elements, state variables, and calls to your CRUD functions.

```javascript
1	import React, {useState} from 'react';
2	import {
3	  Alert,
4	  View,
5	  SafeAreaView,
6	  Image,
7	  ScrollView,
8	  StatusBar,
9	  StyleSheet,
10	  TouchableOpacity,
11	} from 'react-native';
12	
13	import {
14	  List,
15	  Text as PaperText,
16	  Button as PaperButton,
17	  TextInput as PaperTextInput,
18	} from 'react-native-paper';
19	import {createFragmentContainer} from 'react-relay';
20	import CreateTodoMutation from './mutations/CreateTodoMutation';
21	import UpdateTodoMutation from './mutations/UpdateTodoMutation';
22	import DeleteTodoMutation from './mutations/DeleteTodoMutation';
23	
24	import environment from '../../relay/environment';
25	
26	const TodoList = props => {
27	  const [newTodoTitle, setNewTodoTitle] = useState('');
28	
29	  const {query} = props;
30	  const {todos} = query;
31	
32	  const createTodo = () => {
33	    const input = {
34	      fields: {
35	        title: newTodoTitle,
36	        done: false,
37	      },
38	    };
39	
40	    CreateTodoMutation.commit({
41	      environment,
42	      input: input,
43	      onCompleted: () => {
44	        Alert.alert('Success!', 'Todo created!');
45	        setNewTodoTitle('');
46	      },
47	      onError: errors => {
48	        Alert.alert('Error!', errors);
49	      },
50	    });
51	  };
52	
53	  const updateTodo = (todoId, done) => {
54	    const input = {
55	      id: todoId,
56	      fields: {
57	        done,
58	      },
59	    };
60	
61	    UpdateTodoMutation.commit({
62	      environment,
63	      input: input,
64	      onCompleted: () => {
65	        Alert.alert('Success!', 'Todo updated!');
66	      },
67	      onError: errors => {
68	        Alert.alert('Error!', errors);
69	      },
70	    });
71	  };
72	
73	  const deleteTodo = todoId => {
74	    const input = {
75	      id: todoId,
76	    };
77	
78	    DeleteTodoMutation.commit({
79	      environment,
80	      input: input,
81	      onCompleted: () => {
82	        Alert.alert('Success!', 'Todo deleted!');
83	      },
84	      onError: errors => {
85	        Alert.alert('Error!', errors);
86	      },
87	    });
88	  };
89	
90	  const renderTodos = () => {
91	    if (!todos) {
92	      return null;
93	    }
94	
95	    return todos.edges.map(({node: todo}) => (
96	      <List.Item
97	        key={todo.id}
98	        title={todo.title}
99	        titleStyle={todo.done ? Styles.todo_text_done : Styles.todo_text}
100	        style={Styles.todo_item}
101	        right={props => (
102	          <>
103	            {!todo.done && (
104	              <TouchableOpacity onPress={() => updateTodo(todo.id, true)}>
105	                <List.Icon {...props} icon="check" color={'#4CAF50'} />
106	              </TouchableOpacity>
107	            )}
108	
109	            <TouchableOpacity onPress={() => deleteTodo(todo.id)}>
110	              <List.Icon {...props} icon="close" color={'#ef5350'} />
111	            </TouchableOpacity>
112	          </>
113	        )}
114	      />
115	    ));
116	  };
117	
118	  return (
119	    <>
120	      <StatusBar backgroundColor="#208AEC" />
121	      <SafeAreaView style={Styles.container}>
122	        <View style={Styles.header}>
123	          <Image
124	            style={Styles.header_logo}
125	            source={ {
126	              uri:
127	                'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png',
128	            } }
129	          />
130	          <PaperText style={Styles.header_text_bold}>
131	            {'React Native on Back4App'}
132	          </PaperText>
133	          <PaperText style={Styles.header_text}>{'Product Creation'}</PaperText>
134	        </View>
135	        <View style={Styles.create_todo_container}>
136	          {/* Todo create text input */}
137	          <PaperTextInput
138	            value={newTodoTitle}
139	            onChangeText={text => setNewTodoTitle(text)}
140	            label="New Todo"
141	            mode="outlined"
142	            style={Styles.create_todo_input}
143	          />
144	          {/* Todo create button */}
145	          <PaperButton
146	            onPress={() => createTodo()}
147	            mode="contained"
148	            icon="plus"
149	            color={'#208AEC'}
150	            style={Styles.create_todo_button}>
151	            {'Add'}
152	          </PaperButton>
153	        </View>
154	        <ScrollView style={Styles.todo_list}>{renderTodos()}</ScrollView>
155	      </SafeAreaView>
156	    </>
157	  );
158	};
159	
160	const TodoListFragmentContainer = createFragmentContainer(TodoList, {
161	  query: graphql`
162	    fragment TodoList_query on Query {
163	      todos(first: 1000) @connection(key: "TodoList_todos", filters: []) {
164	        edges {
165	          node {
166	            id
167	            title
168	            done
169	          }
170	        }
171	      }
172	    }
173	  `,
174	});
175	
176	const Styles = StyleSheet.create({
177	  container: {
178	    flex: 1,
179	    backgroundColor: '#FFF',
180	  },
181	  wrapper: {
182	    width: '90%',
183	    alignSelf: 'center',
184	  },
185	  header: {
186	    alignItems: 'center',
187	    paddingTop: 10,
188	    paddingBottom: 20,
189	    backgroundColor: '#208AEC',
190	  },
191	  header_logo: {
192	    width: 170,
193	    height: 40,
194	    marginBottom: 10,
195	    resizeMode: 'contain',
196	  },
197	  header_text_bold: {
198	    color: '#fff',
199	    fontSize: 14,
200	    fontWeight: 'bold',
201	  },
202	  header_text: {
203	    marginTop: 3,
204	    color: '#fff',
205	    fontSize: 14,
206	  },
207	  flex_between: {
208	    flexDirection: 'row',
209	    alignItems: 'center',
210	    justifyContent: 'space-between',
211	  },
212	  create_todo_container: {
213	    flexDirection: 'row',
214	    paddingLeft: 10,
215	    paddingRight: 10,
216	  },
217	  create_todo_input: {
218	    flex: 1,
219	    height: 38,
220	    marginBottom: 16,
221	    backgroundColor: '#FFF',
222	    fontSize: 14,
223	  },
224	  create_todo_button: {
225	    marginTop: 6,
226	    marginLeft: 15,
227	    height: 40,
228	  },
229	  todo_list: {
230	    paddingLeft: 10,
231	    paddingRight: 10,
232	  },
233	  todo_item: {
234	    borderBottomWidth: 1,
235	    borderBottomColor: 'rgba(0, 0, 0, 0.12)',
236	  },
237	  todo_text: {
238	    fontSize: 15,
239	  },
240	  todo_text_done: {
241	    color: 'rgba(0, 0, 0, 0.3)',
242	    fontSize: 15,
243	    textDecorationLine: 'line-through',
244	  },
245	});
246	
247	export default TodoListFragmentContainer;
```

Before running your project, don´t forget to run yarn relay and update the Relay \_\_generated\_\_ types:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Nd4DwtvEmsFAoRVprGYvX_image.png" signedSrc size="80" width="513" height="222" position="center" caption}

If your component is properly set up, you should see something like this after building and running the app:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/TeC_-iegf8yDxcwZNSjs9_image.png" signedSrc size="60" width="421" height="839" position="center" caption}

Go ahead and add some to-dos by typing its titles in the input box one at a time and pressing the Add button. Note that after every successful creation, the createTodo function triggers the updater callback into the Mutation, refreshing your task list automatically. You should now have a sizeable to-do list like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/fZwXEt94yjPQHVwi55J9F_image.png" signedSrc size="60" width="423" height="841" position="center" caption}

You can now mark your tasks as done by clicking in the checkmark beside it, causing their done value to be updated to true and changing its icon status on the left. As said in the update function step, the Relay will update automatically the todo with the new value of the field done.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/J5kZwJeNNgD6TrkHqV9Zb_image.png" signedSrc size="60" width="425" height="843" position="center" caption}

The only remaining data operation is now the delete one, which can be done by pressing on the trash can icon at the far right of your to-do list object. After successfully deleting an object, you should get an alert message like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/mQDfk4qh08fZPSKiP_Be8_image.png" signedSrc size="60" width="423" height="842" position="center" caption}

## Conclusion

At the end of this guide, you learned how to perform basic data operations (CRUD) with GrapqhQL and Relay Modern on React Native, while also learning the Relay Connection APIs that help us updating our frontend.
