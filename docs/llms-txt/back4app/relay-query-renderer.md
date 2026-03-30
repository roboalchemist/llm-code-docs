# Source: https://docs-containers.back4app.com/docs/react-native/graphql/relay-query-renderer.md

---
title: Query Renderer
slug: docs/react-native/graphql/relay-query-renderer
description: In this guide you will learn how to make your first graphql query on Back4App
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T18:48:27.695Z
updatedAt: 2025-01-17T01:28:49.675Z
---

# Query Renderer on Back4App

## Introduction

In our previous [**guide**](https://www.back4app.com/docs/react-native/graphql/relay-setup), we have learned how to prepare our Relay Environment. Now you’re ready to start developing your React Native app.

In this guide, you will learn how to make your first query on Back4App. We’re going to dive into the Relay Query Render, understanding its main principles and use it to consume your first data from Back4App.

## Goals

Get an overview of Relay Query Renderer;

Make a query on Back4App GraphQL API from a React Native App using Relay;

## Prerequisites

:::hint{type="info"}
- Application created at Back4App dashboard
- React Native application and with Relay Environment configured by the previous docs.
- Read about Relay Node and Connections
:::

## What is the Query Renderer?

As well as React builds a tree of components, Relay builds a tree of data components. This means that each component of the application will be the owner of their fragment data. The fragment will contain the data information necessary to render it on screen and Relay ensures that this data is available before rendering the component.

Handling this whole approach, the Query Renderer is a root component necessary to compose those fragments and prepare the query to be fetched from our back-end.

## Why understand the Query renderer?

Understanding the use of Query Renderer makes it important to abstract your application in different ways. A good abstract of code could prevent hours of work, errors, debugging time, etc.

## How it works the renderer together with Back4app APIs

In the last tutorial, we have prepared the Relay Environment file, which specifies the Back4App connection info. Using this configuration, Relay will take care of the communication with Back4App APIs. You don’t need to worry about the connection. Just focus on building the data components.

## 1 - Creating a Class on Back4App Dashboard

Let’s create your first class and populate it with a few objects using the Back4App GraphQL Console. The Person class has 2 fields name which is a string and salary which is an integer. Go to the Dashboard->Core->GraphQL Console and use the code below:

```graphql
1	mutation CreateClass {
2	  createClass(input:{
3	    name: "Person"
4	    schemaFields: {
5	      addStrings: [{name: "name"}]
6	      addNumbers: [{name: "salary"}]
7	    }
8	  }){
9	    class{
10	      schemaFields{
11	        name
12	        __typename
13	      }
14	    }
15	  }
16	}
```

You’ll see the result below:

- **creating class&#x20;**

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/POIZNKLV_Hb36QMPoWhAK_image.png)

Now let’s create some objects inside this Class. Go to the create object mutation [**guide**](https://www.back4app.com/docs/parse-graphql/graphql-mutation-create-object#mutation-generic) and see how to handle this case. Make sure you are using the latest Parse Server Version in order to use the most recent GraphQL API notation available on Back4App.

```graphql
1	mutation CreateObject{
2	  createHero(input: {fields: {name: "Allana Foley", salary: 1000}}){
3	    person {
4	      id
5	      name
6	      salary
7	    }
8	  }
9	}
```

- **creating object&#x20;**

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/l1kwoq9WTDEOK9lTsqMfy_image.png)

Now, the Person class is created and has a name and salary field.

After creating a new class, Back4App automatically generates all the necessary resources to use the back-end safely.

One example is the list of objects. Back4App already created the connections necessary to query the list of Person: People.

To better understand, go to the playground, refresh and open the docs tab and look for People. Back4App generated the connection field. You can also query the class person as a list. Note that the Query.people field is a PersonConnection.

Relay will consume the connection field to render a list of the Person’s objects.

Person Field doc:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/or6J-14M3FXWU4lna7dmQ_image.png" signedSrc size="50" width="292" height="847" position="center" caption}

And People (Person) connection Field docs:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/f2yzig7_jejw4Ibf4K5q4_image.png" signedSrc size="50" width="295" height="321" position="center" caption}

## 2 - Updating the Schema

It is important to remember that if a new class goes into your application, it will be necessary to update the schema inside the root of the React Native application.

If necessary, go to [**Download Schema**](https://www.back4app.com/docs/react-native/graphql/download-schema) docs and repeat the steps to update the schema.

## 3 - First example of fragment container

Before we continue the tutorial, let’s introduce you to the fragment container.

Let’s create a component that will be the Person info owner. This component will contain the person’s name and salary. Here you can ask any person field to build your component. Now, we’re going to proceed with these two fields.

- Creates a file and name it PersonCard.js
- inside of it, let’s create a simple function component

```javascript
1	import React from 'react';
2	
3	const PersonCard = () => {
4	    return (
5	        <div>
6	            
7	        </div>
8	    );
9	};
```

Replace the line of export default by the code below:

```javascript
1	export default createFragmentContainer(PersonCard, {
2	    person: graphql`
3	    fragment PersonCard_person on Person {
4	      id
5	      name
6	      salary
7	    }
8	  `,
9	});
```

The code above will create a fragment of a Person that asks only for id, name, and salary.

Finish updating the rest of the component with the following code:

```javascript
1	const PersonCard = ({person}) => {
2	    return (
3	        <View>
4	            <Text>Name: {person.name}</Text>
5	            <Text>Salary: {person.salary}</Text>
6	        </View>
7	    );
8	};
```

The final result should look like this:

```javascript
1	import React from "react";
2	import { createFragmentContainer, graphql } from "react-relay";
3	import { View, Text } from "react-native";
4	
5	const PersonCard = ({person}) => {
6	    return (
7	        <View>
8	            <Text>Name: {person.name}</Text>
9	            <Text>Salary: {person.salary}</Text>
10	        </View>
11	    );
12	};
13	
14	export default createFragmentContainer(PersonCard, {
15	    person: graphql`
16	    fragment PersonCard_person on Person {
17	      id
18	      name
19	      salary
20	    }
21	  `,
22	});
```

## 4 - Creating The Query Renderer

The next step is to create the Query Renderer for your objects list. The Query Renderer is a root component for retrieving the data components and preparing them to fetch data from the backend. You will learn how to retrieve data for a Person Class on Back4App.

### **4.1 - Creating the file**

- Create a new file and name it PersonRenderer.js
- Copy the code below and paste it into PersonRenderer file.

```javascript
1	const PersonRenderer = () => {
2	  return (
3	    <QueryRenderer
4	      environment={Environment}
5	      query={graphql``}
6	      variables={null}
7	      render={({error, props}) => {
8	        if (error) {
9	          return (
10	            <View>
11	              <Text>{error.message}</Text>
12	            </View>
13	          );
14	        } else if (props) {
15	          // @todo here will be implement the person card for each item from result
16	        }
17	        return (
18	          <View>
19	            <Text>loading</Text>
20	          </View>
21	        );
22	      }}
23	    />
24	  );
25	};
26	
27	export default PersonRenderer;
```

### **4.2 - Understanding the props of QueryRenderer**

Let’s start with a Query Renderer with their props empty: graphql, variables, and render. Step by step, you will implement each one incrementally.

First of all, your application needs to inform the query for Query Renderer. Here, our application will consume a list of People. On query props, paste the following code:

```graphql
1	graphql`
2	  query PersonRendererQuery {
3	    people {
4	      edges {
5	        node {
6	          ...PersonCard_person
7	        }
8	      }
9	    }
10	  }`
```

The graphql comes from react-relay and implements the query as a string.

:::hint{type="info"}
It is Important to understand edges and node connection. The query above is consuming a node connection of people from the Back4App server. Every time you create a new class, it will be followed by a node connection.
:::

**Variables**

When necessary, the query renderer will consume variables. A good example: when the application requests a query for a person by id. As this is not the case right now, let’s pass by null on the variables props.

**Populating the Person Card**

This query will return a list of people. The query renderer ensures that the data will be available to render. If it doesn’t, shoot an error. The props responsible for this is the render.

Populate the render props with the following code:

```javascript
1	render={({error, props}) => {
2	  if (error) {
3	    return (
4	      <View>
5	        <Text>{error.message}</Text>
6	      </View>
7	    );
8	  } else if (props) {
9	     return props.people.edges.map(({node}) => <PersonCard person={node} />);
10	  }
11	  return (
12	    <View>
13	      <Text>loading</Text>
14	    </View>
15	  );
16	}}
```

Replace the commented todo for a javascript map for rendering a person card for each result from the list.

As said, the query renderer takes responsibility for making the data available only when it is ready. Until then, a loading message will be displayed. If an error occurs, it will be displayed on the screen preventing an unexpected application crash.

By last, let improves the render of person replacing the .map by a new function. Put it before the Query Renderer:

```graphql
1   const renderPersons = (people) => {
2     return people.edges.map(({node}) => <PersonCard person={node} />);
3   };
```

And the final result should look like:

```graphql
1	import React from "react";
2	import { QueryRenderer } from "react-relay";
3	import Environment from "./relay/Environment";
4	import PersonCard from "./PersonCard";
5	import { View, Text } from "react-native";
6	
7	const PersonRenderer = () => {
8	  const renderPersons = (people) => {
9	    return people.edges.map(({node}) => <PersonCard person={node} />);
10	  };
11	
12	  return (
13	    <QueryRenderer
14	      environment={Environment}
15	      query={graphql`
16	        query PersonRendererQuery {
17	          people {
18	            edges {
19	              node {
20	                ...PersonCard_person
21	              }
22	            }
23	          }
24	        }
25	      `}
26	      variables={null}
27	      render={({error, props}) => {
28	        if (error) {
29	          return (
30	            <View>
31	              <Text>{error.message}</Text>
32	            </View>
33	          );
34	        } else if (props) {
35	          return renderPersons(props.people);
36	        }
37	        return (
38	          <View>
39	            <Text>loading</Text>
40	          </View>
41	        );
42	      }}
43	    />
44	  );
45	};
46	
47	export default PersonRenderer;
```

## 5 - Making your first query

Now it is time to fetch the Person using the PersonRenderer. If everything is ok, your application now has two new components: PersonRenderer and PersonCard.

Before starting the application, the Relay needs the Relay Compiler to run and generate the component types. For this, run into your terminal:

:::BlockQuote
yarn relay
:::

On app.js add the followng code:

```javascript
1	import React from 'react';
2	import { SafeAreaView, StatusBar, View, Text } from 'react-native';
3	
4	import Providers from './Providers';
5	import PersonRenderer from '../components/home/person/PersonRenderer';
6	
7	const App = () => {
8	  return (
9	    <Providers>
10	      <StatusBar barStyle="dark-content" />
11	      <SafeAreaView>
12	        <View
13	          style={ {
14	            flexDirection: 'column',
15	            justifyContent: 'center',
16	            alignItems: 'center',
17	            marginTop: 100,
18	          } }>
19	          <Text style={ {fontWeight: "bold", textAlign: "center"} }>
20	            Back4App React Native Relay - Query Renderer List Example
21	          </Text>
22	          <PersonRenderer />
23	        </View>
24	      </SafeAreaView>
25	    </Providers>
26	  );
27	};
28	
29	export default App;
```

:::hint{type="info"}
The code of app.js comes originally from create-react-native-app. It added a View with a style to center the content on the screen with a margin of 10px from the top. Inside of it has a text with a label to give some context for the print and the PersonRenderer to show the list of person.
:::

You need to get the following result:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/8weoMupLKSfT9rOv8hZha_image.png" signedSrc size="80" width="772" height="288" position="center" caption}

- **Rendering**

In our Back4App React Native application, we import the PersonRenderer directly into the App.js. As the PersonRenderer is a root component and has its QueryRenderer, the Person must be displayed without any error:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/UI6gJgtD9X82_SeJ3s9Zv_image.png" signedSrc size="50" width="742" height="1536" position="center" caption}

## 6 - Typing the components

:::hint{type="info"}
This step makes sense for an application that works with typescript. If your application doesn’t use typescript, go ahead.
:::

One of the powers of the Relay Compiler is to generate the types from each data component. Let’s type the PersonRenderer and PersonCard to make the application more powerful.

**Typing PersonRenderer**

Type the renderPerson function arg people into PersonRenderer:

```javascript
1   const renderPersons = (people: PersonRendererQuery['response']['people']) => {
2     return people.edges.map(({node}) => <PersonCard person={node} />);
3   };
```

Import the PersonRendererQuery type from \_\_generated\_\_ folder created inside of the same folder of the PersonRenderer.

**Typing PersonCard**

Go ahead to PersonCard, create a new type object and name it PersonCardProps:

```javascript
1    type PersonCardProps = {};
```

Import thePersonCard\_persontype from\_\_generated\_\_folders:

```javascript
1    import {PersonCard_person} from './__generated__/PersonCard_person.graphql';
```

Add the person inside the type PersonCardProps:

```javascript
1    type PersonCardProps = {
2      person: PersonCard_person;
3    };
```

On props arguments from PersonCard, type the component with thePersonCardProps:

:::BlockQuote
1   **const** PersonCard **=** (\{person}: PersonCardProps) **=>** \{ ... }
:::

The final result of both components should look like:

- **PersonRenderer**

```javascript
1	import React from 'react';
2	import {graphql, QueryRenderer} from 'react-relay';
3	import {Environment} from '../../../relay';
4	import PersonCard from './PersonCard';
5	import {View, Text} from 'react-native';
6	import {PersonRendererQuery} from './__generated__/PersonRendererQuery.graphql';
7	
8	const PersonRenderer = () => {
9	const renderPersons = (people: PersonRendererQuery['response']['people']) => {
10	    return people.edges.map(({node}) => <PersonCard person={node} />);
11	  };
12	
13	  return (
14	    <QueryRenderer
15	      environment={Environment}
16	      query={graphql`
17	        query PersonRendererQuery {
18	          people {
19	            edges {
20	              node {
21	                ...PersonCard_person
22	              }
23	            }
24	          }
25	        }
26	      `}
27	      variables={null}
28	      render={({error, props}) => {
29	        if (error) {
30	          return (
31	            <View>
32	              <Text>{error.message}</Text>
33	            </View>
34	          );
35	        } else if (props) {
36	          return renderPersons(props.people);
37	        }
38	        return (
39	          <View>
40	            <Text>loading</Text>
41	          </View>
42	        );
43	      }}
44	    />
45	  );
46	};
47	
48	export default PersonRenderer;
```

- **PersonCard**

```javascript
1	import React from 'react';
2	
3	import {createFragmentContainer, graphql} from 'react-relay';
4	
5	import {View, Text} from 'react-native';
6	import {PersonCard_person} from './__generated__/PersonCard_person.graphql';
7	
8	type PersonCardProps = {
9	  person: PersonCard_person;
10	};
11	
12	const PersonCard = ({person}: PersonCardProps) => {
13	  return (
14	    <View>
15	      <Text>Name: {person.name}</Text>
16	      <Text>Salary: {person.salary}</Text>
17	    </View>
18	  );
19	};
20	
21	export default createFragmentContainer(PersonCard, {
22	  person: graphql`
23	    fragment PersonCard_person on Person {
24	      id
25	      name
26	      salary
27	    }
28	  `,
29	});
```

## Conclusion

The final result of QueryRenderer demonstrated how the application can be abstracted. The application can display the Person inside of the Query Renderer. As the PersonCard has more components, it doesn’t change the way the Query Renderer was built.

The PersonRenderer was built to show how a query can be done in easy steps, combined with the power of the Back4App server. In the next guide, you will learn how to retrieve a specific Person object and show their attributes.
