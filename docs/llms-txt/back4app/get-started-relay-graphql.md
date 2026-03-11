# Source: https://docs-containers.back4app.com/docs/react-native/graphql/get-started-relay-graphql.md

---
title: Getting Started
slug: docs/react-native/graphql/get-started-relay-graphql
description: In this guide you learn whats is Relay, how to work with schema and understand how to work GraphQL on back4app
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T18:25:56.131Z
updatedAt: 2024-03-29T01:38:48.029Z
---

# Get Started with GraphQL Relay

## Introduction

In this guide you will learn what is Relay, how to work with schema and understand how to work with GraphQL on back4app

## Prerequisites

:::hint{type="info"}
**This is not a tutorial yet, but to feel free confortable reading it you will need:**

- Basic JavaScript knowledge.
- Basic understand about GraphQL. If you don’t have, the [**GraphQL.js**](https://github.com/graphql/graphql-js) its a perfect place to start
:::

## Relay

Relay is a GraphQL client developed by Facebook Engineering Team and designed for performance when building data-driven applications. More precisely, Relay is a framework for declaratively fetching and managing GraphQL data on the client-side that uses strict conventions to help your application succeed. It was built with scalability in mind to power complex applications like Facebook. The ultimate goal of GraphQL and Relay is to deliver instant UI-response interactions.

One of the main advantages of using GraphQL is that you can fetch with a single query all the data needed to build an application page, for example. Off course that this is good(you can save round-trips to the server) but with that comes a problem. You may use different queries to the same component when reusing this component in different parts of your application. To avoid this kind of problem Relay uses an important concept: colocation.

## Colocation

When using Relay, components and their data requirements live together. Components data requirements are declared inside them. That means all the components declare the data that they need. Relay ensures that each component has the data it needs when renders.

The Relay structure behind the Colocation concept are the containers. The most common is the Relay Fragment Container. The container is the component that attempts to fulfill the data required when rendering each component. The containers declare their data dependency using GraphQL fragments.

Every component will have its own fragment container. The container doesn’t fetch the data directly; it only declares the specification for the data needed when rendering. The data will be fetched on the server-side. Relay will make sure that the data is available before the rendering occurs. Relay composes a tree of data with those containers, ignoring the redundancies, and fetching the data on the server.

Let’s illustrate the concept with an example. A fragment is a selection of fields on a GraphQL type. Relay works with fragment, pagination and refetch container. The most common is a fragment container. See below a fragment in GraphQL and after the same on Relay.

```graphql
1   query Health {
2     health
3   }
```

```typescript
1	type HomeProps = {
2	  query: Home_query;
3	};
4	
5	const Home = ({query}: HomeProps) => {
6	  return (
7	    <View>
8	      <Text>API Health: {query.health ? 'Health' : 'Not health' }</Text>
9	    </View>
10	  );
11	};
12	
13	const HomeFragment = createFragmentContainer(Home, {
14	  query: graphql`
15	    fragment Home_query on Query {
16	      health
17	    }
18	  `,
19	});
20	
21	export default createQueryRendererModern(HomeFragment, Home, {
22	  query: graphql`
23	    query HomeQuery {
24	      ...Home_query
25	    }
26	  `,
27	  hideSplash: true,
28	});
```

On the first code you can see the GraphQL version that allows us to split this query into reusable fragments. On the next code you can see the Relay one that is showing the fragments and the data together in the same component.
Colocation means that data definitions and view definitions live together. Collocation has some benefits. We just need to declare exactly the date that we need. That means it is hard to over fetch data which improves our application and is hard to under fetch data which prevent errors with missing data. Another important concept is Data Masking which means that components can only access data they asked for. Data Masking helps to prevent dependency errors. Also, components are only updated if the data they are using change.

## Query Renderer Modern

:::hint{type="info"}
We recommend to take a look at the [**official Query Renderer docs**](https://relay.dev/docs/en/query-renderer.html#docsNav) for a better understanding.
:::

Based on the fragment containers, Relay will read them and make the request to the server based on the data they have. But, how does this requisition happen? This is where Query Renderer Modern comes in.

The Query Renderer Modern is the component that reads the fragment containers, makes the request to the server and returns the data to the component.

Every root component will have a Query Renderer Modern making this request. In the example above what we have an abstraction so that we pass only the fragment that must be read and so all the rest of the work is done inside createQueryRendererModern.

:::hint{type="info"}
In the next step of the doc we will enter the createQueryRendererModern to understand the abstraction based on the pure example above
:::

Below is a pure example of Query Render Modern:

```typescript
1	export default function ArtistRenderer({artistID}) {
2	  return (
3	    <QueryRenderer
4	      environment={environment}
5	      query={graphql`
6	        query QueryRenderersArtistQuery($artistID: String!) {
7	          # The root field for the query
8	          artist(id: $artistID) {
9	            # A reference to your fragment container
10	            ...ArtistHeader_artist
11	          }
12	        }
13	      `}
14	      variables={ {artistID} }
15	      render={({error, props}) => {
16	        if (error) {
17	          return <div>{error.message}</div>;
18	        } else if (props) {
19	          return <Artist artist={props.artist} />;
20	        }
21	        return <div>Loading</div>;
22	      }}
23	    />
24	  );
25	}
```

We can see that the Query Renderer Modern is a [**HOC component**](https://reactjs.org/docs/higher-order-components.html). In other words, wrap the component that owns the container with the data to be requested, make the request with the Relay environment and return the data downwards passing to the component.

## Automatic Type Generation

Working with Relay we can build an application type safely. As we said every component will be the owner of their data. So, when we run the relay-compiler, it reads every fragment of data and makes a check with your graphql schema. If all checks of Relay compiler is ok, the types it will be generate in a folder called **generated**. This folder is create inside of the root components folders.

See the example below:

Component home checking the API health:

```graphql
1	const Home = ({query}: HomeProps) => {
2	  return (
3	    <View>
4	      <Text>API Health: {query.health ? 'Health' : 'Not health' }</Text>
5	    </View>
6	  );
7	};
8	
9	const HomeFragment = createFragmentContainer(Home, {
10	  query: graphql`
11	    fragment Home_query on Query {
12	      health
13	    }
14	  `,
15	});
16	
17	export default createQueryRendererModern(HomeFragment, Home, {
18	  query: graphql`
19	    query HomeQuery {
20	      ...Home_query
21	    }
22	  `,
23	  hideSplash: true,
24	});
```

Generated folder containing the types for Home component:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/TjOKbbJomDUZHH3P56c9i_image.png" signedSrc size="50" width="218" height="66" position="center" caption}

And the types generated:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/P8873lGO8IRZ5DN0zRAhM_image.png" signedSrc size="80" width="416" height="566" position="center" caption}

After this we just need import the type on component and compose it:

```typescript
1   import {Home_query} from "./__generated__/Home_query.graphql";
2
3   type HomeProps = {
4     query: Home_query;
5   };
```

The type is generate in Flow, the core language for types from Facebook. But, with a library you can generate in Typescript. This is most common to work with React Native. Resuming, with Relay compiler we can check the data implementation before run time. This helps us to prevent bugs and then improve the application quality and development time.

On queries, we can avoid duplicate data in N different components. It check if some data is duplicate. If has it will remove the redundancies. This will reduce the payload size of queries and increase the performance of application even more.

## Developing

On queries, we can avoid duplicate data in N different components. It check if some data is duplicate. If has it will remove the redundancies. This will reduce the payload size of queries and increase the performance of application even more.

# On the server Side - Back4App

Back4App generates a ready-to-use Relay compliant GraphQL API to use on your project. What Back4App generates for you so you don’t have to build by yourself on server side:

## Infrastructure

On Back4app Dashboard you can create a complete data model with classes, types and everything else a database needs. You don’t have to worry about setup and maintain server by yourself. After create your data model Back4App we will generate everything that is necessary to consume it on the frontend side using GraphQL. Let’s take a look at the GraphQL API Schema.

## Schema

The schema file is the core of any GraphQL application. It describes the whole server available to be use on client side. Relay works using your schema file to confirm the queries
string and generated file to appear in ./**generated**/MyComponent.graphql, as we said on **Automatic Type Generation** topic.

To use the Relay Compiler, you need either a .graphql or .json GraphQL schema file describing your GraphQL server’s API. These files are local representations of a server source of truth and are not edited.

Every schema of GraphQL can be compose by query type, mutation type and subscription type. To work with a schema being consume by Relay on front end, you need some of core concepts on back-end: node interface and connection.

:::hint{type="success"}
We recommend reading about node interface and Relay connections to turn this reading more easier to abstract.
:::

## Node Interfaces

The node interface implements every type on GraphQL to help fetch data via id. This is an implementation to make more easy fetch data from server and updated. So each data of each type it will have a unique id, called as global unique id, being implemented by a node interface. With node, Relay avoid nested queries and make the fetch and re-fetch using it. This is hard to implement and needs a bit of work, but we already build this for you!

## Pagination

Build to be compose, as on front-end on back-end the Relay it will help us to compose our data to. For work with pagination we have connections. Those connections implements the node from the type we are fetching and have a standard model, facilitating the implementation of pagination on server side. Fortunately, again, we have this already build to use on frontend.

## Conclusion

In this guide we introduced what is Relay, its main concepts and how it works. Also we could see how Back4App automates the GraphQL server creation and delivers us a complete database with GraphQL API to work with.

Resuming, the whole backend is already built by back4app. You only need to create your types on the dashboard and start to consume based on schema generated. In the next section we will explain how to handle this schema on the front end and how to prepare your environment to use Relay. We also have a [**GraphQL Cookbook**](https://www.back4app.com/docs/parse-graphql/graphql-getting-started), you can use it to help you to understand more concepts on our dashboard.
