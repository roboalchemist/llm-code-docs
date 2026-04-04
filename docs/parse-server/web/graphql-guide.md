# Source: https://docs.parseplatform.org/graphql/guide/

Title: Parse

URL Source: https://docs.parseplatform.org/graphql/guide/

Published Time: Sat, 07 Feb 2026 17:30:01 GMT

Markdown Content:
[](https://docs.parseplatform.org/graphql/guide/#getting-started)Getting Started
--------------------------------------------------------------------------------

[GraphQL](https://graphql.org/), developed by Facebook, is an open-source data query and manipulation language for APIs. In addition to the traditional [REST API](https://docs.parseplatform.org/rest/guide/), Parse Server automatically generates a GraphQL API based on your current application schema. Specifically, Parse has opted for the [Relay](https://relay.dev/docs/en/introduction-to-relay) specification in-line with industry best-practices.

[](https://docs.parseplatform.org/graphql/guide/#fast-launch)Fast launch
------------------------------------------------------------------------

The easiest way to run the Parse GraphQL Server is using the CLI:

```
$ npm install -g parse-server mongodb-runner
$ mongodb-runner start
$ parse-server --appId APPLICATION_ID --masterKey MASTER_KEY --databaseURI mongodb://localhost/test --mountGraphQL --mountPlayground
```

Notes:

*   Run `parse-server --help` or refer to [Parse Server Options](https://parseplatform.org/parse-server/api/master/ParseServerOptions.html) for a complete list of Parse Server configuration options.
*   ⚠️ Please do not use `--mountPlayground` option in production as anyone could access your API Playground and read or change your application’s data. [Parse Dashboard](https://docs.parseplatform.org/graphql/guide/#running-parse-dashboard) has a built-in GraphQL Playground and it is the recommended option for production apps. If you want to secure your API in production take a look at [Class Level Permissions](https://docs.parseplatform.org/js/guide/#class-level-permissions)

After running the CLI command, you should have something like this in your terminal:

```
...
[35071] parse-server running on http://localhost:1337/parse
[35071] GraphQL running on http://localhost:1337/graphql
[35071] Playground running on http://localhost:1337/playground
```

Since you have already started your Parse GraphQL Server, you can now visit [http://localhost:1337/playground](http://localhost:1337/playground) in your web browser to start playing with your GraphQL API.

![Image 1: GraphQL Playground](https://docs.parseplatform.org/assets/images/graphql/graphql-playground.png)

[](https://docs.parseplatform.org/graphql/guide/#using-expressjs)Using Express.js
---------------------------------------------------------------------------------

You can also mount the GraphQL API in an Express.js application together with the REST API or solo. You first need to create a new project and install the required dependencies:

```
$ mkdir my-app
$ cd my-app
$ npm init
$ npm install parse-server express --save
```

Then, create an `index.js` file with the following content:

```
// index.js
const express = require('express');
const { default: ParseServer, ParseGraphQLServer } = require('parse-server');

// Create express app
const app = express();

// Create a Parse Server Instance
const parseServer = new ParseServer({
  databaseURI: 'mongodb://localhost:27017/test',
  appId: 'APPLICATION_ID',
  masterKey: 'MASTER_KEY',
  serverURL: 'http://localhost:1337/parse',
  publicServerURL: 'http://localhost:1337/parse'
});

// Create the GraphQL Server Instance
const parseGraphQLServer = new ParseGraphQLServer(
  parseServer,
  {
    graphQLPath: '/graphql',
    playgroundPath: '/playground'
  }
);

// (Optional) Mounts the REST API
await parseServer.start();
app.use('/parse', parseServer.app);
// Mounts the GraphQL API using graphQLPath: '/graphql'
parseGraphQLServer.applyGraphQL(app);
// (Optional) Mounts the GraphQL Playground - do NOT use in Production
parseGraphQLServer.applyPlayground(app);

// Start the server
app.listen(1337, function() {
  console.log('REST API running on http://localhost:1337/parse');
  console.log('GraphQL API running on http://localhost:1337/graphql');
  console.log('GraphQL Playground running on http://localhost:1337/playground');
});
```

And finally start your app:

```
$ npx mongodb-runner start
$ node index.js
```

After starting the app, you can visit [http://localhost:1337/playground](http://localhost:1337/playground) in your browser to start playing with your GraphQL API.

⚠️ Please do not mount the GraphQL Playground in production as anyone could access your API Playground and read or change your application’s data. [Parse Dashboard](https://docs.parseplatform.org/graphql/guide/#running-parse-dashboard) has a built-in GraphQL Playground and it is the recommended option for production apps. If you want to secure your API in production take a look at [Class Level Permissions](https://docs.parseplatform.org/js/guide/#class-level-permissions).

[](https://docs.parseplatform.org/graphql/guide/#adding-custom-schema)Adding Custom Schema
------------------------------------------------------------------------------------------

The Parse GraphQL API supports the use of custom user-defined schema. You can write your own types, queries, and mutations, which will be merged with the ones that are automatically generated. Your custom schema is resolved via [Cloud Code](https://docs.parseplatform.org/graphql/guide/#cloud-code-resolvers) functions.

First, add a utility for parsing GraphQL queries as a required dependency:

```
$ npm install graphql-tag --save
```

Then, modify your `index.js` file to include your custom schema, along with the path to your cloud code file:

```
const gql = require('graphql-tag');

const parseServer = new ParseServer({
  appId: 'APPLICATION_ID',
  cloud: './cloud/main.js',
});

const parseGraphQLServer = new ParseGraphQLServer(
  parseServer,
  {
    graphQLPath: '/graphql',
    playgroundPath: '/playground',
    graphQLCustomTypeDefs: gql`
      extend type Query {
        hello: String! @resolve
        hello2: String! @resolve(to: "hello")
      }
    `,
  }
);
```

Alternatively, you can create your custom schema in a dedicated `schema.graphql` file and reference the file in your `index.js`:

```
const gql = require('graphql-tag');
const fs = require('fs');
const customSchema = fs.readFileSync('./cloud/schema.graphql');

const parseServer = new ParseServer({
  appId: 'APPLICATION_ID',
  cloud: './cloud/main.js',
});

const parseGraphQLServer = new ParseGraphQLServer(
  parseServer,
  {
    graphQLPath: '/graphql',
    playgroundPath: '/playground',
    graphQLCustomTypeDefs: gql`${customSchema}`,
  }
);
```

```
# schema.graphql
extend type Query {
  hello: String! @resolve
  hello2: String! @resolve(to: "hello")
}
```

[](https://docs.parseplatform.org/graphql/guide/#running-parse-dashboard)Running Parse Dashboard
------------------------------------------------------------------------------------------------

[Parse Dashboard](https://github.com/parse-community/parse-dashboard) is a standalone dashboard for managing your Parse Server apps, including your objects’ schema and data, logs, jobs, CLPs, and push notifications. Parse Dashboard also has a built-in GraphQL Playground that you can use to play around with your auto-generated Parse GraphQL API. It is the recommended option for **production** applications.

The easiest way to run the Parse Dashboard is through its CLI:

```
$ npm install -g parse-dashboard
$ parse-dashboard --dev --appId APPLICATION_ID --masterKey MASTER_KEY --serverURL "http://localhost:1337/parse" --graphQLServerURL "http://localhost:1337/graphql" --appName MyAppName
```

After starting the dashboard, you can visit [http://0.0.0.0:4040/apps/MyAppName/api_console/graphql](http://0.0.0.0:4040/apps/MyAppName/api_console/graphql) in your browser:

![Image 2: Parse Dashboard GraphQL Playground](https://docs.parseplatform.org/assets/images/graphql/dashboard-graphql-playground.png)

To learn more about Parse Dashboard and its setup options, please visit the [Parse Dashboard Repository](https://github.com/parse-community/parse-dashboard).

[](https://docs.parseplatform.org/graphql/guide/#graphql)GraphQL
----------------------------------------------------------------

Before continuing, it is recommended to study some of the GraphQL documentation:

A GraphQL API contains 3 main concepts:

*   `Query`: Fetch data
*   `Mutation`: Create or update data
*   `Subscription`: Listen for data changes

[](https://docs.parseplatform.org/graphql/guide/#learn-query--mutation)Learn Query & Mutation
---------------------------------------------------------------------------------------------

To learn how to query data and execute operation on a GraphQL API [consult the official documentation](https://graphql.org/learn/queries/).

[](https://docs.parseplatform.org/graphql/guide/#relay)Relay
------------------------------------------------------------

The Parse Server GraphQL API follows latest standards currently available for highly-scalable APIs and ambitious front-end projects.

The Parse Open Source Team choose to follow the [GraphQL Server Relay Specification](https://relay.dev/docs/guides/graphql-server-specification).

Relay is a JavaScript framework for building data-driven React applications powered by GraphQL, designed from the ground up to be easy to use, extensible and, most of all, performant. Relay accomplishes this with static queries and ahead-of-time code generation.

Later we will see some Relay concepts like: Node, Connection and Cursor.

[](https://docs.parseplatform.org/graphql/guide/#api-doc)API Doc
----------------------------------------------------------------

GraphQL is a self documented API, to learn all available operations, it’s recommended to start the Parse GraphQL Server and visit the Docs tab on the GraphQL Playground.

```
$ npm install -g parse-server mongodb-runner
$ mongodb-runner start
$ parse-server --appId APPLICATION_ID --masterKey MASTER_KEY --databaseURI mongodb://localhost/test --mountGraphQL --mountPlayground
```

Visit your [Local GraphQL Playground](http://localhost:1337/playground)

![Image 3: GraphQL Playground](https://docs.parseplatform.org/assets/images/graphql/graphql-playground.png)

[](https://docs.parseplatform.org/graphql/guide/#health-check)Health Check
--------------------------------------------------------------------------

Now that you have set up your GraphQL environment, it is time to run your first query. Execute the following code in your GraphQL Playground to check your API’s health:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
query healthy {
  health
}
```

```
// Response
{
  "data": {
    "health": true
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#classes)Classes
----------------------------------------------------------------

Since your application does not have a schema yet, you can use the `createClass` mutation to create your first class through the GraphQL API. Run the following:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY"
}
```

```
# GraphQL
mutation createGameScoreClass {
  createClass(
    input: {
      clientMutationId: "anFrontId"
      name: "GameScore"
      schemaFields: {
        addStrings: [{ name: "playerName" }]
        addNumbers: [{ name: "score" }]
        addBooleans: [{ name: "cheatMode" }]
      }
    }
  ) {
    clientMutationId
    class {
      name
      schemaFields {
        name
        __typename
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "createClass": {
      "clientMutationId": "anFrontId",
      "class": {
        "name": "GameScore",
        "schemaFields": [
          {
            "name": "objectId",
            "__typename": "SchemaStringField"
          },
          {
            "name": "updatedAt",
            "__typename": "SchemaDateField"
          },
          {
            "name": "createdAt",
            "__typename": "SchemaDateField"
          },
          {
            "name": "playerName",
            "__typename": "SchemaStringField"
          },
          {
            "name": "score",
            "__typename": "SchemaNumberField"
          },
          {
            "name": "cheatMode",
            "__typename": "SchemaBooleanField"
          },
          {
            "name": "ACL",
            "__typename": "SchemaACLField"
          }
        ]
      }
    }
  }
}
```

Parse Server learned from the first class that you created and now you have the `GameScore` class in your schema. You can now start using the automatically generated operations!

[](https://docs.parseplatform.org/graphql/guide/#objects)Objects
----------------------------------------------------------------

[](https://docs.parseplatform.org/graphql/guide/#create)Create
--------------------------------------------------------------

For each class in your application’s schema, Parse Server automatically generates a custom mutation for creating this class’ objects through the GraphQL API.

For example, if you have a class named `GameScore` in the schema, Parse Server automatically generates a new mutation called `createGameScore`, and you should be able to run the code below in your GraphQL Playground:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
mutation createAGameScore {
  createGameScore(
    input: {
      clientMutationId: "anUniqueId"
      fields: { playerName: "Sean Plott", score: 1337, cheatMode: false }
    }
  ) {
    clientMutationId
    gameScore {
      id
      updatedAt
      createdAt
      playerName
      score
      cheatMode
      ACL {
        public {
          write
          read
        }
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "createGameScore": {
      "clientMutationId": "anUniqueId",
      "gameScore": {
        "id": "R2FtZVNjb3JlOjZtdGlNcmtXNnY=",
        "updatedAt": "2022-01-01T12:23:45.678Z",
        "createdAt": "2022-01-01T12:23:45.678Z",
        "playerName": "Sean Plott",
        "score": 1337,
        "cheatMode": false,
        "ACL": {
          "public": {
            "write": true,
            "read": true
          }
        }
      }
    }
  }
}
```

**Note:** The `id` is a [Relay Global Object Identification](https://facebook.github.io/relay/graphql/objectidentification.htm); it’s **not** a Parse `objectId`. Most of the time the `Relay Node Id` is a `Base64` of the `ParseClass` and the `objectId`.

[](https://docs.parseplatform.org/graphql/guide/#update)Update
--------------------------------------------------------------

For each class in your application’s schema, Parse Server automatically generates a custom mutation for updating this class’ objects through the GraphQL API.

For example, if you have a class named `GameScore` in the schema, Parse Server automatically generates a new mutation called `updateGameScore`.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
mutation updateAGameScore {
  updateGameScore(
    input: {
      id: "R2FtZVNjb3JlOmM3TVpDZEhQY2w="
      fields: { playerName: "Charles Francois" }
    }
  ) {
    gameScore {
      id
      playerName
    }
  }
}
```

```
// Response
{
  "data": {
    "updateGameScore": {
      "gameScore": {
        "id": "R2FtZVNjb3JlOmM3TVpDZEhQY2w=",
        "playerName": "Charles Francois"
      }
    }
  }
}
```

**Note:** If you use [Apollo Client](https://www.apollographql.com/docs/react/) it’s recommended to request the modified fields and `id` during the Mutation, then the [Apollo Client](https://www.apollographql.com/docs/react/) will automatically update its local store and push the new data across your app; i.e. If you update `playerName` you should request `playerName` and `id` like the code above.

### [](https://docs.parseplatform.org/graphql/guide/#unset-a-field)Unset a field

Across the whole GraphQL API you can simply unset a field by setting its value to `null`.

Following the official GraphQL API Specs, setting a field to `null` through the GraphQL API will completly unset the field in the database on the targeted Parse Object. GraphQL API will transform `null` on the server before saving the object to correctly unset the field into the database.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
mutation updateAGameScore {
  updateGameScore(
    input: { id: "R2FtZVNjb3JlOmM3TVpDZEhQY2w=", fields: { playerName: null } }
  ) {
    gameScore {
      id
      playerName
    }
  }
}
```

```
// Response
{
  "data": {
    "updateGameScore": {
      "gameScore": {
        "id": "R2FtZVNjb3JlOmM3TVpDZEhQY2w=",
        "playerName": null
      }
    }
  }
}
```

The GraphQL API will always return `null` if the field is `null` or `undefined` in the database. The GraphQL API does not differentiate between `null` and `undefined` in the data response.

[](https://docs.parseplatform.org/graphql/guide/#delete)Delete
--------------------------------------------------------------

For each class in your application’s schema, Parse Server automatically generates a custom mutation for deleting this class’ objects through the GraphQL API.

For example, if you have a class named `GameScore` in the schema, Parse Server automatically generates a new mutation called `deleteGameScore`.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
mutation deleteAGameScore {
  deleteGameScore(input: { id: "R2FtZVNjb3JlOmM3TVpDZEhQY2w=" }) {
    gameScore {
      id
      playerName
    }
  }
}
```

The code above should resolve to something similar to this:

```
// Response
{
  "data": {
    "deleteGameScore": {
      "gameScore": {
        "id": "R2FtZVNjb3JlOmM3TVpDZEhQY2w=",
        "playerName": "Charles Francois"
      }
    }
  }
}
```

**Note:** The API returns the deleted object, which can allow you to show messages like “The player Charles François has been successfully removed” on the front end.

[](https://docs.parseplatform.org/graphql/guide/#nested-mutation)Nested Mutation
--------------------------------------------------------------------------------

The GraphQL API supports nested mutations, so you can create objects with complex relationships in one request. Assuming that we have classes `Country`, `City` and `Company`.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
mutation aNestedMutation {
  createCountry(
    input: {
      fields: {
        name: "Mars"
        cities: {
          createAndAdd: [
            { name: "Alpha", companies: { createAndAdd: [{ name: "Motors" }] } }
          ]
        }
      }
    }
  ) {
    country {
      name
      cities {
        edges {
          node {
            name
            companies {
              edges {
                node {
                  name
                }
              }
            }
          }
        }
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "createCountry": {
      "country": {
        "name": "Mars",
        "cities": {
          "edges": [
            {
              "node": {
                "name": "Alpha",
                "companies": {
                  "edges": [
                    {
                      "node": {
                        "name": "Motors"
                      }
                    }
                  ]
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#queries)Queries
----------------------------------------------------------------

[](https://docs.parseplatform.org/graphql/guide/#get)Get
--------------------------------------------------------

For each class in your application’s schema, Parse Server automatically generates a custom query for getting this class’ objects through the API.

For example, if you have a class named `GameScore` in the schema, Parse Server automatically generates a new query called `gameScore`, and you should be able to run the code below in your GraphQL Playground:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
query getAGameScore {
  gameScore(id: "R2FtZVNjb3JlOjZtdGlNcmtXNnY=") {
    id
    score
    playerName
    score
    cheatMode
    ACL {
      public {
        read
        write
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "gameScore": {
      "id": "R2FtZVNjb3JlOjZtdGlNcmtXNnY=",
      "score": 1337,
      "playerName": "Sean Plott",
      "cheatMode": false,
      "ACL": {
        "public": {
          "read": true,
          "write": true
        }
      }
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#get-with-relay)Get with Relay
------------------------------------------------------------------------------

With the Relay specification you also have the choice to use [GraphQL Fragments](https://graphql.org/learn/queries/#fragments) through the `node` GraphQL Query. For a `GameScore` object the following query will do the job.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
query getGameScoreWithNodeRelay {
  node(id: "R2FtZVNjb3JlOjZtdGlNcmtXNnY") {
    id
    __typename
    ... on GameScore {
      playerName
      score
      cheatMode
    }
  }
}
```

```
// Response
{
  "data": {
    "node": {
      "id": "R2FtZVNjb3JlOjZtdGlNcmtXNnY=",
      "__typename": "GameScore",
      "playerName": "Sean Plott",
      "score": 1337,
      "cheatMode": false
    }
  }
}
```

Here using `Node Relay` is useful for writing generic requests for your front end components. For example, assuming we already have a `User` with a `Relay Node Id: X1VzZXI6Q1lMeWJYMjFjcw==` and `username: "johndoe"`.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
query genericGet {
  node(id: "X1VzZXI6Q1lMeWJYMjFjcw==") {
    id
    __typename
    ... on User {
      id
      username
    }
    ... on GameScore {
      playerName
      score
      cheatMode
    }
  }
}
```

```
// Response
{
  "data": {
    "node": {
      "id": "X1VzZXI6Q1lMeWJYMjFjcw==",
      "__typename": "User",
      "username": "johndoe"
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#find)Find
----------------------------------------------------------

For each class in your application’s schema, Parse Server automatically generates a custom query for finding this class’ objects through the GraphQL API.

For example, if you have a class named `GameScore` in the schema, Parse Server automatically generates a new query called `gameScores`, and you should be able to run the code below in your GraphQL Playground:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
query getSomeGameScores{
  gameScores {
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
    count
    edges {
      cursor
      node {
        id
        playerName
        score
        cheatMode
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "gameScores": {
      "pageInfo": {
        "hasNextPage": false,
        "hasPreviousPage": false,
        "startCursor": "YXJyYXljb25uZWN0aW9uOjA=",
        "endCursor": "YXJyYXljb25uZWN0aW9uOjI="
      },
      "count": 3,
      "edges": [
        {
          "cursor": "YXJyYXljb25uZWN0aW9uOjA=",
          "node": {
            "id": "R2FtZVNjb3JlOjZtdGlNcmtXNnY=",
            "playerName": "Sean Plott",
            "score": 1337,
            "cheatMode": false
          }
        },
        {
          "cursor": "YXJyYXljb25uZWN0aW9uOjE=",
          "node": {
            "id": "R2FtZVNjb3JlOnp2cHdTYXlmYnA=",
            "playerName": "John Doe",
            "score": 13,
            "cheatMode": true
          }
        },
        {
          "cursor": "YXJyYXljb25uZWN0aW9uOjI=",
          "node": {
            "id": "R2FtZVNjb3JlOjNmWjBoQVJDVU0=",
            "playerName": "Steve Jordan",
            "score": 134,
            "cheatMode": false
          }
        }
      ]
    }
  }
}
```

### [](https://docs.parseplatform.org/graphql/guide/#where)Where

You can use the `where` argument to add constraints to a class find query. See the example below:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
query getSomeGameScores {
  gameScores(where: {
  	score: { greaterThan: 158 }
  }) {
    count
    edges {
      cursor
      node {
        id
        playerName
        score
        cheatMode
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "gameScores": {
      "count": 1,
      "edges": [
        {
          "cursor": "YXJyYXljb25uZWN0aW9uOjA=",
          "node": {
            "id": "R2FtZVNjb3JlOjZtdGlNcmtXNnY=",
            "playerName": "Sean Plott",
            "score": 1337,
            "cheatMode": false
          }
        }
      ]
    }
  }
}
```

Visit your GraphQL Playground if you want to know all the available constraints.

### [](https://docs.parseplatform.org/graphql/guide/#order)Order

You can use the `order` argument to select in which order the results are returned in a class find query. See the example below:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
query getSomeGameScores {
  gameScores(
  	where: {
  	  cheatMode: { equalTo: false }
  	},
  	order: score_ASC
  ) {
    count
    edges {
      cursor
      node {
        id
        playerName
        score
        cheatMode
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "gameScores": {
      "count": 2,
      "edges": [
        {
          "cursor": "YXJyYXljb25uZWN0aW9uOjA=",
          "node": {
            "id": "R2FtZVNjb3JlOjNmWjBoQVJDVU0=",
            "playerName": "Steve Jordan",
            "score": 134,
            "cheatMode": false
          }
        },
        {
          "cursor": "YXJyYXljb25uZWN0aW9uOjE=",
          "node": {
            "id": "R2FtZVNjb3JlOjZtdGlNcmtXNnY=",
            "playerName": "Sean Plott",
            "score": 1337,
            "cheatMode": false
          }
        }
      ]
    }
  }
}
```

[Relay Node Cursor](https://facebook.github.io/relay/graphql/connections.htm) provides a simple way to get efficient and easy to use pagination.

With Relay you can build flexible pagination based on cursors, here is the main effect of each argument:

*   `skip`: a regular skip to exclude some results
*   `first`: similar to a `limit` parameter but starts from the first result, e.g. `first: 10` retrieves the first 10 results
*   `last`: retrieve the last results, e.g. `last: 10` retrieves the last 10 results
*   `before`: get objects before the provided `Cursor`, in combination with `after` it allows you to build inverted pagination
*   `after`: get objects after the provided `Cursor`, in combination with `first` you get a classic pagination similar to `skip & limit`

You can combine multiple parameters like: `before & last` or `after & first`, assuming you have an existing `cursor`.

Note: `cursor` is different to `id`, it is a temporary pagination ID for the query.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
query getSomeGameScores {
  gameScores(after: "YXJyYXljb25uZWN0aW9uOjE") {
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
    count
    edges {
      cursor
      node {
        id
        playerName
        score
        cheatMode
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "gameScores": {
      "pageInfo": {
        "hasNextPage": false,
        "hasPreviousPage": true,
        "startCursor": "YXJyYXljb25uZWN0aW9uOjI=",
        "endCursor": "YXJyYXljb25uZWN0aW9uOjI="
      },
      "count": 3,
      "edges": [
        {
          "cursor": "YXJyYXljb25uZWN0aW9uOjI=",
          "node": {
            "id": "R2FtZVNjb3JlOjNmWjBoQVJDVU0=",
            "playerName": "Steve Jordan",
            "score": 134,
            "cheatMode": false
          }
        }
      ]
    }
  }
}
```

**Note**: `count` is a global count for available results, it’s not the number of edges returned by the request.

[](https://docs.parseplatform.org/graphql/guide/#nested-query)Nested Query
--------------------------------------------------------------------------

The GraphQL API supports nested queries, so you can find object and then execute query on relational child fields. Assuming that we have classes `Country`, `City`, `Company`:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
query aNestedQuery {
  countries(where: {
    name: { matchesRegex: "Ma", options: "i" }
  }) {
    edges {
      node {
        name
        cities(where: {
          name: { matchesRegex: "pha", options: "i"}
        }) {
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "countries": {
      "edges": [
        {
          "node": {
            "name": "Mars",
            "cities": {
              "edges": [
                {
                  "node": {
                    "name": "Alpha"
                  }
                }
              ]
            }
          }
        }
      ]
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#relational-query)Relational Query
----------------------------------------------------------------------------------

The GraphQL API supports complex parent relational queries. It means that all the `Pointer` and `Relation` fields in your database can be used easily throughout the API to query complex relational data. Let’s take a look at the power of this feature.

### [](https://docs.parseplatform.org/graphql/guide/#parent-relation-style)Parent Relation Style

Assuming that we have a `Country` class, `City` class, `Street` class and `House` class.

*   `Country` has a `cities``Relation` field.
*   `City` has a `streets``Relation` field.
*   `Street` has a `houses``Relation` field.

Let’s build a query matching countries that contain at least one city with more than 20,000 people and that contain at least one street that matches `/rue/i` regex and this street should contain at least one house with a name equal to `Parse Members`.

The GraphQL API can handle this type of complex relational query with ease.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
{
  countries(
    where: {
      cities: {
        have: {
          peoplesNumber: { greaterThan: 20000 }
          streets: {
            have: {
              name: { matchesRegex: "rue", options: "i" }
              houses: { have: { name: { equalTo: "Parse Members" } } }
            }
          }
        }
      }
    }
  ) {
    edges {
      node {
        name
        cities {
          edges {
            node {
              name
              peoplesNumber
              streets {
                edges {
                  node {
                    name
                    houses {
                      edges {
                        node {
                          name
                        }
                        ... too many brackets here
}
```

```
// Response
{
  "data": {
    "countries": {
      "edges": [
        {
          "node": {
            "name": "France",
            "cities": {
              "edges": [
                {
                  "node": {
                    "name": "Toulouse",
                    "peoplesNumber": 400000,
                    "streets": {
                      "edges": [
                        {
                          "node": {
                            "name": "rue jean jaures",
                            "houses": {
                              "edges": [
                                {
                                  "node": {
                                    "name": "Parse Members"
                                  }
                                  ... too many brackets here
}
```

### [](https://docs.parseplatform.org/graphql/guide/#child-relation-style)Child Relation Style

Assuming that we have a `Country` class, `City` class, `Street` class, `House` class.

*   `House` has a `street``Pointer` field.
*   `Street` has a `city``Pointer` field.
*   `City` has a `country``Pointer` field.

Let’s build a query matching houses where the street has a city that has a country with a name equal to `France`.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
{
  houses(
    where: {
      street: {
        have: {
          city: {
            have: {
              country: {
                have: {
                  name: { equalTo: "France" }
                }
              }
            }
          }
        }
      }
    }
  ) {
    edges {
      node {
        name
        street {
          name
          city {
            name
            country {
              name
            }
          }
        }
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "houses": {
      "edges": [
        {
          "node": {
            "name": "Parse Members",
            "street": {
              "name": "rue jean jaures",
              "city": {
                "name": "Toulouse",
                "country": {
                  "name": "France"
                }
              }
            }
          }
        }
      ]
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#users)Users
------------------------------------------------------------

In general, users have the same features as other objects. The differences are that user objects must have a username and password, the password is automatically encrypted and stored securely, and Parse Server enforces the uniqueness of the username and email fields.

Therefore you can manage users objects using the `createUser`, `user`, `users`, `updateUser`, and `deleteUser` operations. Additionally, you can use the `signUp`, `logIn`, and `logOut` operations.

[](https://docs.parseplatform.org/graphql/guide/#signing-up)Signing Up
----------------------------------------------------------------------

Signing up a new user differs from creating another object in that the `username` and `password` fields are required. The `password` field is handled differently than the others; it is encrypted with bcrypt when stored in the database and never returned to any client request.

You can ask Parse Server to [verify user email addresses](https://docs.parseplatform.org/parse-server/guide/#welcome-emails-and-email-verification) in your application settings. With this setting enabled, all new user registrations with an email field will generate an email confirmation at that address. You can check whether the user has verified their email with the `emailVerified` field.

To sign up a new user, use the `signUp` mutation. For example:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
mutation signUp {
  signUp(
    input: {
      fields: {
        username: "johndoe"
        password: "ASuperStrongPassword"
        email: "john.doe@email.com"
      }
    }
  ) {
    viewer {
      sessionToken
      user {
        username
        email
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "signUp": {
      "viewer": {
        "sessionToken": "r:a0ec8428409b6b85c6f54ab1e654c53d",
        "user": {
          "username": "johndoe",
          "email": "john.doe@email.com"
        }
      }
    }
  }
}
```

Note that a field called `sessionToken` has been returned. This token can be used to authenticate subsequent operations as this user.

[](https://docs.parseplatform.org/graphql/guide/#logging-in)Logging In
----------------------------------------------------------------------

After you allow users to sign up, you need to let them log in to their account with a username and password in the future. To do this, use the `logIn` mutation:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
mutation logIn {
  logIn(input: { username: "johndoe", password: "ASuperStrongPassword" }) {
    viewer {
      sessionToken
      user {
        username
        email
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "logIn": {
      "viewer": {
        "sessionToken": "r:b0dfad1eeafa4425d9508f1c0a15c3fa",
        "user": {
          "username": "johndoe",
          "email": "john.doe@email.com"
        }
      }
    }
  }
}
```

Note that, when the user logs in, Parse Server generates a new `sessionToken` for future operations.

[](https://docs.parseplatform.org/graphql/guide/#3rd-party-authentication)3rd Party Authentication
--------------------------------------------------------------------------------------------------

You can log in a user via a [3rd party authentication](https://docs.parseplatform.org/parse-server/guide/#supported-3rd-party-authentications) system (Facebook, Twitter, Apple and many more) with the `logInWith` mutation.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
mutation LoginWithFacebook {
  logInWith(
    input: {
      authData: {
        facebook: {
          id: "user's Facebook id number as a string"
          access_token: "Facebook access token for the user"
          expiration_date: "token expiration date"
        }
      }
      fields: { email: "a.new@user.com" }
    }
  ) {
    viewer {
      sessionToken
      user {
        id
        email
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "logInWith": {
      "viewer": {
        "sessionToken": "r:b0dfad1eeafa4425d9508f1c0a15c3fa",
        "user": {
          "email": "a.new@user.com"
        }
      }
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#using-session-token)Using Session Token
----------------------------------------------------------------------------------------

For authenticating an operation as a specific user, you need to pass the `X-Parse-Session-Token` header with its valid session token.

You can easily do this in the GraphQL Playground. There is an option called `HTTP HEADERS` in its bottom left side. Use this option to replace the default `X-Parse-Master-Key` header by a valid `X-Parse-Session-Token` header. You should have something like this:

![Image 4: Session Token Header](https://docs.parseplatform.org/assets/images/graphql/session-token.png)

After setting up the `X-Parse-Session-Token` header, any operation will run as this user. For example, you can run the code below to validate the session token and return its associated user:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Session-Token": "r:b0dfad1eeafa4425d9508f1c0a15c3fa"
}
```

```
# GraphQL
query viewer {
  viewer {
    sessionToken
    user {
      username
      email
    }
  }
}
```

```
// Response
{
  "data": {
    "viewer": {
      "sessionToken": "r:b0dfad1eeafa4425d9508f1c0a15c3fa",
      "user": {
        "username": "johndoe",
        "email": "john.doe@email.com"
      }
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#logging-out)Logging Out
------------------------------------------------------------------------

You can log out a user through the `logOut` mutation. You need to send the `X-Parse-Session-Token` header and run code like the below example:

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Session-Token": "r:b0dfad1eeafa4425d9508f1c0a15c3fa"
}
```

```
# GraphQL
mutation logOut {
  logOut(input: { clientMutationId: "logOut" }) {
    clientMutationId
    viewer {
      user {
        username
        email
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "logOut": {
      "clientMutationId": "logOut",
      "viewer": {
        "user": {
          "username": "johndoe",
          "email": "john.doe@email.com"
        }
      }
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#resetting-passwords)Resetting Passwords
----------------------------------------------------------------------------------------

To use the `resetPassword` mutation your Parse Server must have an email adapter configured.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
}
```

```
# GraphQL
mutation resetPassword {
  resetPassword(input: { email: "email@email.email" }) {
    ok
  }
}
```

```
// Response
{
  "data": {
    "resetPassword": {
      "ok": true,
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#send-email-verification)Send Email Verification
------------------------------------------------------------------------------------------------

The verification email is automatically sent on sign up; this mutation is useful if the user didn’t receive the first email. Again, an email adapter must be configured for this mutation to work.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
}
```

```
# GraphQL
mutation sendVerificationEmail {
  sendVerificationEmail(input: { email: "email@email.email" }) {
    ok
  }
}
```

```
// Response
{
  "data": {
    "sendVerificationEmail": {
      "ok": true,
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#files)Files
------------------------------------------------------------

The GraphQL API supports file upload via [GraphQL Upload](https://github.com/jaydenseric/graphql-upload), to send a `File` through `GraphQL` it’s recommended to use the [Apollo Upload Client](https://github.com/jaydenseric/apollo-upload-client).

[](https://docs.parseplatform.org/graphql/guide/#add-a-file-field-to-a-class)Add a File field to a Class
--------------------------------------------------------------------------------------------------------

First of all we will update our `GameScore` class with a `screenshot` field of type `File`.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY"
}
```

```
# GraphQL
mutation updateGameScoreClass {
  updateClass(
    input: {
      name: "GameScore"
      schemaFields: { addFiles: [{ name: "screenshot" }] }
    }
  ) {
    class {
      name
    }
  }
}
```

```
// Response
{
  "data": {
    "updateClass": {
      "class": {
        "name": "GameScore"
      }
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#create-a-file)Create a File
----------------------------------------------------------------------------

The GraphQL API supports nested mutation for the `File` type, so you can send the file along with the Parse Object or just upload the file and get the returned information.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
# $file is a GraphQL Variable, see https://github.com/jaydenseric/apollo-upload-client
mutation createFile($file: Upload!) {
  createFile(input: { upload: $file }) {
    fileInfo {
      name
      url
    }
  }
}
```

```
// Response
{
  "data": {
    "createFile": {
      "fileInfo": {
        "name": "6a4d43c3f0512bcb6bf05b6b0e7db47d_file.png",
        "url": "http://localhost:1337/graphq/files/APPLICATION_ID/6a4d43c3f0512bcb6bf05b6b0e7db47d_file.png"
      }
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#add-an-existing-file)Add an existing file
------------------------------------------------------------------------------------------

You can add an existing file to an object.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
mutation createGameScore {
  createGameScore(
    input: {
      fields: {
        playerName: "John"
        screenshot: {
          file: {
            __type: "File"
            name: "6a4d43c3f0512bcb6bf05b6b0e7db47d_file.png"
            url: "http://localhost:1337/graphq/files/APPLICATION_ID/6a4d43c3f0512bcb6bf05b6b0e7db47d_file.png"
          }
        }
      }
    }
  ) {
    gameScore {
      screenshot {
        name
        url
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "createGameScore": {
      "gameScore": {
        "screenshot": {
          "name": "6a4d43c3f0512bcb6bf05b6b0e7db47d_file.png",
          "url": "http://localhost:1337/graphq/files/APPLICATION_ID/6a4d43c3f0512bcb6bf05b6b0e7db47d_file.png"
        }
      }
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#create-and-add-a-file)Create and add a file
--------------------------------------------------------------------------------------------

Lets create a new `GameScore` object and upload the file.

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
# GraphQL
# $file is a GraphQL Variable, see https://github.com/jaydenseric/apollo-upload-client
mutation createGameScore($file: Upload!) {
  createGameScore(
    input: { fields: { playerName: "John", screenshot: { upload: $file } } }
  ) {
    gameScore {
      screenshot {
        name
        url
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "createGameScore": {
      "gameScore": {
        "screenshot": {
          "name": "6a4d43c3f0512bcb6bf05b6b0e7db47d_file.png",
          "url": "http://localhost:1337/graphq/files/APPLICATION_ID/6a4d43c3f0512bcb6bf05b6b0e7db47d_file.png"
        }
      }
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#unlink-a-file)Unlink a file
----------------------------------------------------------------------------

Let’s update a `GameScore` object and unset the file linked in the `screenshot` field. By setting the `screenshot` field to `null`, the linked file will be removed from the `Gamescore` object.

**Note:** The file will be not deleted from your file storage.

```
# GraphQL
mutation updateGameScore($id: ID!) {
  updateGameScore(input: { id: $id, fields: { screenshot: null } }) {
    gameScore {
      screenshot {
        name
        url
      }
    }
  }
}
```

```
// Response
{
  "data": {
    "updateGameScore": {
      "gameScore": {
        "screenshot": null
      }
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#customisation)Customisation
----------------------------------------------------------------------------

Although we automatically generate a GraphQL schema based on your Parse Server database, we have provided a number of ways in which to configure and extend this schema.

[](https://docs.parseplatform.org/graphql/guide/#configuration)Configuration
----------------------------------------------------------------------------

Whilst it’s great to simply plug GraphQL into your Parse setup and immediately query any of your existing classes, you may find that this level of exposure is not suitable to your project. We have therefore provided a flexible way to limit which types, queries mutations are exposed within your GraphQL schema.

### [](https://docs.parseplatform.org/graphql/guide/#configuration-options)Configuration Options

By default, no configuration is needed to get GraphQL working with your Parse Server. All of the following settings are completely optional, and can be provided or omitted as desired. To configure your schema, you simply need to provide a valid JSON object with the expected properties as described below:

```
// The properties with ? are optional

interface ParseGraphQLConfiguration {
  // All classes enabled by default
  // Provide an empty array to disable all classes
  enabledForClasses?: Array<string>;

  // Selectively disable specific classes
  disabledForClasses?: Array<string>;

  // Provide an array of per-class settings
  classConfigs?: Array<{

    // You must provide a className
    // Only provide one config object per class
    className: string;

    type?: {

      // By default, all fields can be sent for
      // a create or update mutation. Use this
      // setting to limit to specific fields.
      inputFields?: {
        create?: Array<string>;
        update?: Array<string>;
      };

      // By default, all fields can be resolved
      // on a get or find query. Use this to limit
      // which fields can be selected.
      outputFields?: Array<string>;

      // By default, all valid fields can be used
      // to filter a query. Use this to limit
      // which fields can be used to constrain a query.
      constraintFields?: Array<string>;

      // By default, all valid fields can be used
      // to sort the results of a query. Use this to
      // limit which fields can be used to sort a query
      // and which direction that sort can be set to.
      sortFields?: {
        field: string;
        asc: boolean;
        desc: boolean;
      }[];
    };

    // By default, a get and find query type is created
    // for all included classes. Use this to disable
    // the available query types for this class.
    query?: {
      get?: boolean;
      find?: boolean;
      getAlias?: String;
      findAlias?: String;
    };

    // By default, all write mutation types are
    // exposed for all included classes. Use this to disable
    // the available mutation types for this class and optionally
    // override the default generated name with aliases.
    mutation?: {
      create?: boolean;
      update?: boolean;
      destroy?: boolean;
      createAlias?: String,
      updateAlias?: String,
      destroyAlias?: String,
    };
  }>
}
```

### [](https://docs.parseplatform.org/graphql/guide/#set-or-update-configuration)Set or Update Configuration

We have provided a public API in `ParseGraphQLServer` which accepts the above JSON object for setting (and updating) your Parse GraphQL Configuration, `setGraphQLConfig`:

```
const parseGraphQLServer = new ParseGraphQLServer(parseServer, {
    graphQLPath: parseServerConfig.graphQLPath,
    playgroundPath: parseServerConfig.playgroundPath
  });

  const config = {
    // ... ParseGraphQLConfiguration
  };

  await parseGraphQLServer.setGraphQLConfig(config);
```

### [](https://docs.parseplatform.org/graphql/guide/#include-or-exclude-classes)Include or Exclude Classes

By default, all of your Parse classes, including the defaults such as `Parse.User`, `Parse.Session`, `Parse.Role` are added to the schema. You can restrict this using the `enabledForClassess` or `disabledForClassess` options, which accepts an array of class names.

In the following example, we limit our GraphQL schema to only expose the default `_User` class, along with a few custom classes:

```
{
  "enabledForClasses": ["_User", "Book", "Review", "Comment"],
  "disabledForClasses": null
}
```

In the following example, we limit our GraphQL schema by hiding some sensitive classes:

```
{
  // undefined or null results in the default behaviour, i.e. include all classes
  "enabledForClasses": undefined,
  // override the included classes by filtering out the following:
  "disabledForClasses": [ "UserSensitiveData", "ProductOrder", "Invoice" ]
}
```

### [](https://docs.parseplatform.org/graphql/guide/#input-types)Input Types

By default, we enrich the schema by generating a number of [Input Types](https://graphql.org/learn/schema/#input-types) for each class. This, as a healthy side-effect, improves development experience by providing type-completion and docs, though the true purpose is to define exactly what fields are exposed and useable per operation type. You can provide a `type` setting for any or each of your classes to limit which fields are exposed:

In the following example, we have a custom class called `Review` where the fields `rating` and `body` are allowed on the `create` mutation, and the field `numberOfLikes` on the `update` mutation:

```
{
  "classConfigs": [
    {
      "className": "Review",
      "type": {
        "inputFields": {
          "create": ["rating", "body"],
          "update": ["numberOfLikes"]
        }
      }
    }
  ]
}
```

You may decide to restrict which fields can be resolved when getting or finding records from a given class, for example, if you have a class called `Video` which includes a sensitive field `dmcaFlags`, you can hide this field by explicitly stating the fields that can be resolved:

```
{
  "classConfigs": [
    {
      "className": "Video",
      "type": {
        "outputFields": ["name", "author", "numberOfViews",   "comments", "cdnUrl"]
      }
    }
  ]
}
```

In production-grade environments where performance optimisation is critical, complete control over query filters and sortability is required to ensure that unindexed queries are not executed. For this reason, we provide a way to limit which fields can be used to constrain a query, and which fields (including the direction) can be used to sort that query.

In the following example, we set the fields `name` and `age` as the only two that can be used to filter the `_User` class, and defining the `createdAt` and `age` fields the only sortable field whilst disabling the ascending direction on the `createdAt` field:

```
{
  "classConfigs": [
    {
      "className": "_User",
      "type": {
         "constraintFields": ["name", "age"],
          "sortFields": [
            {
              "field": "createdAt",
              "desc": true,
              "asc": false
            },
            {
              "field": "age",
              "desc": true,
              "asc": true
            }
          ]
        }
      }
  ]
}
```

### [](https://docs.parseplatform.org/graphql/guide/#queries-config)Queries

By default, the schema exposes a `get` and `find` operation for each class, for example, `get_User` and `find_User`. You can disable either of these for any class in your schema, like so:

```
{
  "classConfigs": [
    {
      "className": "_User",
      "query": {
        "get": true,
        "find": false
      }
    },
    {
      "className": "Review",
      "query": {
        "get": false,
        "find": true
      }
    }
  ]
}
```

By default, generated query names use pluralized version of `className`. You can override this behaviour with `getAlias`/`findAlias`. This is useful when your collection is named in plural or when singular/plural forms are same e.g. `Data`:

```
{
  "classConfigs": [
    {
      "className": "Likes",
      "query": {
        "getAlias": "like"
      }
    },
    {
      "className": "Data",
      "query": {
        "findAlias": "findData"
      }
    }
  ]
}
```

### [](https://docs.parseplatform.org/graphql/guide/#mutations-config)Mutations

By default, the schema exposes a `create`, `update` and `delete` operation for each class, for example, `create_User`, `update_User` and `delete_User`. You can disable any of these mutations for any class in your schema, like so:

```
{
  "classConfigs": [
    {
      "className": "_User",
      "mutation": {
        "create": true,
        "update": true,
        "destroy": true
      }
    },
    {
      "className": "Review",
      "mutation": {
        "create": true,
        "update": false,
        "destroy": true
      }
    }
  ]
}
```

**Note**: the `delete` mutation setting key is named `destroy` to avoid issues due to `delete` being a javascript reserved word.

You can optionally override the default generated mutation names with aliases:

```
{
  "classConfigs": [
    {
      "className": "Record",
      "mutation": {
        "createAlias": "newRecord",
        "updateAlias": "changeRecord",
        "destroyAlias": "eraseRecord"
      }
    }
  ]
}
```

### [](https://docs.parseplatform.org/graphql/guide/#remove-configuration)Remove Configuration

Deploying a custom configuration via `setGraphQLConfig` persists the changes into the database. As a result, simply deleting a configuration change and deploying again does not result in a default Parse GraphQL configuration. The configuration changes remain.

To remove a configuration, set the affected properties to `null` or `undefined` before deploying. The default Parse GraphQL configuration for those properties will be restored.

```
{
  "enabledForClasses": undefined,
  "disabledForClasses": undefined,
  "classConfigs": undefined,
}
```

Once a default configuration is restored, you can safely remove any unused configuration changes from your `parseGraphQLServer` setup.

[](https://docs.parseplatform.org/graphql/guide/#cloud-code-resolvers)Cloud Code Resolvers
------------------------------------------------------------------------------------------

The Parse GraphQL API supports the use of custom user-defined schema. The [Adding Custom Schema](https://docs.parseplatform.org/graphql/guide/#adding-custom-schema) section explains how to get started using this feature.

Cloud Code functions can then be used as custom resolvers for your user-defined schema.

### [](https://docs.parseplatform.org/graphql/guide/#query-resolvers)Query Resolvers

Here’s an example of a custom query and its related cloud code function resolver in action:

```
# schema.graphql
extend type Query {
  hello: String! @resolve
}
```

```
// main.js
Parse.Cloud.define("hello", () => "Hello, world!");
```

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Master-Key": "MASTER_KEY" // (optional)
}
```

```
query hello {
  hello
}
```

The code above should resolve to this:

```
// Response
{
  "data": {
    "hello": "Hello, world!"
  }
}
```

### [](https://docs.parseplatform.org/graphql/guide/#mutation-resolvers)Mutation Resolvers

At times, you may need more control over how your mutations modify data than what Parse’s auto-generated mutations can provide. For example, if you have classes named `Item` and `CartItem` in the schema, you can create an `addToCart` custom mutation that tests whether a specific item is already in the user’s cart. If found, the cart item’s quantity is incremented by one. If not, a new `CartItem` object is created.

The ability to branch your resolver logic enables you to replicate functionality found in Parse’s auto-generated `createCartItem` and `updateCartItem` mutations and combine those behaviors into a single custom resolver.

```
# schema.graphql
extend type Mutation {
  addToCart(id: ID!): CartItem! @resolve
}
```

**Note**: The `id` passed in to your Cloud Code function from a GraphQL query is a [Relay Global Object Identification](https://facebook.github.io/relay/graphql/objectidentification.htm); it is **not** a Parse `objectId`. Most of the time the `Relay Node Id` is a `Base64` of the `ParseClass` and the `objectId`. Cloud code does not recognize a `Relay Node Id`, so converting it to a Parse `objectId` is required.

Decoding and encoding `Relay Node Ids` in Cloud Code is needed in order to smoothly interface with your client-side GraphQL queries and mutations.

First, install the [Relay Library for GraphQL.js](https://www.npmjs.com/package/graphql-relay) as a required dependency to enable decoding and encoding `Relay Node Ids` in your cloud code functions:

```
$ npm install graphql-relay --save
```

Then, create your `main.js` cloud code file, import `graphql-relay`, and build your `addToCart` function:

```
// main.js
const { fromGlobalId, toGlobalId } = require('graphql-relay');

Parse.Cloud.define("addToCart", async (req) => {
  const { user, params: { id } } = req;

  // Decode the incoming Relay Node Id to a
  // Parse objectId for Cloud Code use.
  const { id: itemObjectId } = fromGlobalId(id);

  // Query the user's current cart.
  const itemQuery = new Parse.Query("Item");
  const item = await itemQuery.get(itemObjectId);
  const cartItemQuery = new Parse.Query("CartItem");
  cartItemQuery.equalTo("item", item);
  cartItemQuery.equalTo("user", user);
  const [existingCartItem] = await cartItemQuery.find();
  let savedCartItem;

  if (existingCartItem) {
    // The item is found in the user's cart; increment its quantity.
    const quantity = await existingCartItem.get("quantity");
    existingCartItem.set("quantity", quantity + 1);
    savedCartItem = await existingCartItem.save();
  } else {
    // The item has not yet been added; create a new cartItem object.
    const CartItem = Parse.Object.extend("CartItem");
    const cartItem = new CartItem();
    savedCartItem = await cartItem.save({ quantity: 1, item, user });
  }

  // Encode the Parse objectId to a Relay Node Id
  // for Parse GraphQL use.
  const cartItemId = toGlobalId('CartItem', savedCartItem.id);

  // Convert to a JSON object to handle adding the
  // Relay Node Id property.
  return { ...savedCartItem.toJSON(), id: cartItemId };
});
```

```
// Header
{
  "X-Parse-Application-Id": "APPLICATION_ID",
  "X-Parse-Session-Token": "r:b0dfad1eeafa4425d9508f1c0a15c3fa"
}
```

```
mutation addItemToCart {
  addToCart(id: "SXRlbTpEbDVjZmFWclRI") {
    id
    quantity
  }
}
```

The code above should resolve to something similar to this:

```
// Response
{
  "data": {
    "addToCart": {
      "id": "Q2FydEl0ZW06akVVTHlGZnVpQw==",
      "quantity": 1
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#optimization)Optimization
--------------------------------------------------------------------------

[](https://docs.parseplatform.org/graphql/guide/#indexing)Indexing
------------------------------------------------------------------

To optimize your server/database performance and response time you need to configure some indexes based on the types of queries that you use in your app. Currently index manipulations are not supported on the GraphQL API but you can use the [Parse JS SDK Indexes API](https://docs.parseplatform.org/js/guide/#indexes)

Here’s a simple example:

```
# First we update the user class
mutation {
  updateClass(
    input: {
      name: "_User"
      schemaFields: {
        addStrings: [{ name: "firstname" }, { name: "lastname" }]
        addDates: [{ name: "birthdate" }]
        addNumbers: [{ name: "credit" }]
      }
    }
  ) {
    class {
      name
    }
  }
}
```

```
# Then lets assume that we have this query in our app
query ASuperUsedQuery {
  users(
    where: {
      firstname: { in: ["John", "Michael", "Sabrina"] }
      lastname: { matchesRegex: "^Do" }
      birthdate: { exists: true }
      credit: { greaterThanOrEqualTo: 100 }
    },
    order: credit_ASC
  ) {
    edges {
      node {
        id
        firstname
      }
    }
  }
}
```

```
// Add the index to user class
const addAnIndexToUserClass = () => {
    // Get current class from database
    const UserClass = await (new Parse.Schema('_User')).get();
    UserClass.addIndex('ASuperUsedQueryIndex', {
        firstname: 1,
        lastname: 1,
        birthdate: 1,
        credit: 1
    });
    await UserClass.update()
    console.log('Index for ASuperUsedQuery created')
}
```

And thats all, your query is optimized and you should have blazing fast responses even with millions of objects.

**Warning:** Only add indexes for most used queries, an over indexed MongoDB will eat lots of RAM.

[](https://docs.parseplatform.org/graphql/guide/#relational)Relational
----------------------------------------------------------------------

When using the GraphQL API, use the same best practices to construct your database. In the Queries section we saw both parent and child relations.

In the majority of use cases it’s best to reference the parent object inside the child and use a child query style.

```
# A Good Schema
mutation EfficientSchema {
  City: createClass(
    input: {
      name: "City"
      schemaFields: {
        addStrings: [{ name: "name" }]
        addPointers: [
            {
                name: "country",
                targetClassName: "Country"
            }
        ]
      }
    }
  ) {
    class {
      name
    }
  }
  Country: createClass(
    input: {
        name: "Country",
        schemaFields: {
            addStrings: [{ name: "name" }]
        }
    }
  ) {
    class {
      name
    }
  }
}
```

```
# A Bad Schema
mutation NotEfficientSchema {
  City: createClass(
    input: {
        name: "City",
        schemaFields: {
            addStrings: [{ name: "name" }]
        }
    }
  ) {
    class {
      name
    }
  }
  Country: createClass(
    input: {
      name: "Country"
      schemaFields: {
        addStrings: [{ name: "name" }]
        addRelations: [
            {
                name: "cities",
                targetClassName: "City"
            }
        ]
      }
    }
  ) {
    class {
      name
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#graphql-clients)GraphQL Clients
--------------------------------------------------------------------------------

If you use a Graphql Client with a cache system like **Apollo Client** you must add the `id` field in each of your graphql `Queries` and `Mutations`, your client can now update dynamically its local cache based on your graphql operations.

**Note:** On `Mutation` it’s recommended to ask to GraphQL to return the modified fields, then your GraphQL Client can update the object in the local cache.

Here a quick example:

```
# Cache Optimized Mutation
mutation OptimizedMutation {
  updateUser(
    input: {
        id: "xxxx",
        fields: {
            firstname: "John",
            lastname: "Doe"
        }
    }
  ) {
    user {
      id
      firstname
      lastname
    }
  }
}
```

[](https://docs.parseplatform.org/graphql/guide/#learning-more)Learning More
----------------------------------------------------------------------------

If you look at the right side of your GraphQL Playground, you will see the DOCS and SCHEMA menus. They are automatically generated by analyzing your application schema and contain all operations that you can call for your application, including the automatic class queries and mutations. Please refer to them and learn more about everything that you can do with your Parse GraphQL API.

![Image 5: GraphQL Docs](https://docs.parseplatform.org/assets/images/graphql/graphql-docs.png)

Additionally, the [GraphQL Learn Section](https://graphql.org/learn/) is a very good source to start learning about the power of the GraphQL language.
