# Source: https://docs.hypermode.com/dgraph/guides/to-do-app/schema-design.md

# Schema Design

> Starting with listing the entities that are involved in a basic to-do app, this step in the GraphQL tutorial walks you through schema design.

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

<Note>This is part 1 of [Building a To-Do List App](./introduction).</Note>

Let's start with listing down the entities that are involved in a basic to do
app.

* Task
* User

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=52937df379de664e6dac3d7d2caf6ab7" alt="To do Graph" width="581" height="221" data-path="images/dgraph/guides/to-do-app/todo-graph.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=47538a713fea7e8d9dca8302b8bd1519 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=24ec19e73f4e21c8ec7bdb01fe62ca1a 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=4d06112fa3a181a13b236faf0f02bd85 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=9950b92801cbc968f9bede5f00fe7eeb 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=d0f77748248d89b7805c34a275273db1 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=b4b754d04819716fe75a3a5338ae1448 2500w" data-optimize="true" data-opv="2" />

Equivalent GraphQL schema for this graph is be as follow:

```graphql
type Task {
    ...
}

type User {
    ...
}
```

What are the fields that these two simple entities contain?

There is a title and a status to check if it was completed or not in the `Task`
type. Then the `User` type has a username (unique identifier), name and the
tasks.

So each user can have many tasks.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph-2.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=31cd6b1489de0216c7f7ebc2e6419753" alt="To do Graph complete" width="581" height="221" data-path="images/dgraph/guides/to-do-app/todo-graph-2.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph-2.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=4d8c5033f9724dcf0af785e4005dcf65 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph-2.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=0787b1d4cf5e0a0914be7daa6e566a9a 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph-2.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=b1afa5696f7a101caf8658e7aa3c0b56 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph-2.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=cdd3dc70bbb01da481e680351d09465b 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph-2.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=e817c351312adf23567a192d5db46716 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/to-do-app/todo-graph-2.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=2a02788ba28263fe0d950cdf221af555 2500w" data-optimize="true" data-opv="2" />

<Note>' \* ' signifies one-to-many relationship</Note>

Now let's add `@id` directive to `username` which makes it the unique key & also
add `@hasInverse` directive to enable the relationship between tasks and user.
We represent that in the GraphQL schema shown below:

```graphql
type Task {
  id: ID!
  title: String!
  completed: Boolean!
  user: User!
}

type User {
  username: String! @id
  name: String
  tasks: [Task] @hasInverse(field: user)
}
```

Save the content in a file `schema.graphql`.

## Running

Before we begin, make sure that you have
[Docker](https://docs.docker.com/install/) installed on your machine.

Let's begin by starting Dgraph standalone by running the command below:

```sh
docker run -it -p 8080:8080 dgraph/standalone:%VERSION_HERE
```

Let's load up the GraphQL schema file to Dgraph:

```sh
curl -X POST localhost:8080/admin/schema --data-binary '@schema.graphql'
```

You can access that GraphQL endpoint with any of the great GraphQL developer
tools. Good choices include GraphQL Playground, Insomnia, GraphiQL and Altair.

Set up any of them and point it at `http://localhost:8080/graphql`. If you know
lots about GraphQL, you might want to explore the schema, queries and mutations
that were generated from the schema.

## Mutating data

Let's add a user and some to dos in our To Do app.

```graphql
mutation {
  addUser(
    input: [
      {
        username: "alice@dgraph.io"
        name: "Alice"
        tasks: [
          { title: "Avoid touching your face", completed: false }
          { title: "Stay safe", completed: false }
          { title: "Avoid crowd", completed: true }
          { title: "Wash your hands often", completed: true }
        ]
      }
    ]
  ) {
    user {
      username
      name
      tasks {
        id
        title
      }
    }
  }
}
```

## Querying data

Let's fetch the to dos to list in our To Do app:

```graphql
query {
  queryTask {
    id
    title
    completed
    user {
      username
    }
  }
}
```

Running this query should return JSON response as shown below:

```json
{
  "data": {
    "queryTask": [
      {
        "id": "0x3",
        "title": "Avoid touching your face",
        "completed": false,
        "user": {
          "username": "alice@dgraph.io"
        }
      },
      {
        "id": "0x4",
        "title": "Stay safe",
        "completed": false,
        "user": {
          "username": "alice@dgraph.io"
        }
      },
      {
        "id": "0x5",
        "title": "Avoid crowd",
        "completed": true,
        "user": {
          "username": "alice@dgraph.io"
        }
      },
      {
        "id": "0x6",
        "title": "Wash your hands often",
        "completed": true,
        "user": {
          "username": "alice@dgraph.io"
        }
      }
    ]
  }
}
```

## Querying data with filters

Before we get into querying data with filters, we're required to define search
indexes to the specific fields.

Let's say we want to run a query on the `completed` field, for which we add
`@search` directive to the field, as shown in the schema below:

```graphql
type Task {
  id: ID!
  title: String!
  completed: Boolean! @search
  user: User!
}
```

The `@search` directive is added to support the native search indexes of
**Dgraph**.

Resubmit the updated schema -

```sh
curl -X POST localhost:8080/admin/schema --data-binary '@schema.graphql'
```

Now, let's fetch all to dos which are completed:

```graphql
query {
  queryTask(filter: { completed: true }) {
    title
    completed
  }
}
```

Next, let's say we want to run a query on the `title` field, for which we add
another `@search` directive to the field, as shown in the schema below:

```graphql
type Task {
  id: ID!
  title: String! @search(by: [fulltext])
  completed: Boolean! @search
  user: User!
}
```

The `fulltext` search index provides the advanced search capability to perform
equality comparison as well as matching with language-specific stemming and
stopwords.

Resubmit the updated schema -

```sh
curl -X POST localhost:8080/admin/schema --data-binary '@schema.graphql'
```

Now, let's try to fetch to dos whose title has the word "avoid":

```graphql
query {
  queryTask(filter: { title: { alloftext: "avoid" } }) {
    id
    title
    completed
  }
}
```
