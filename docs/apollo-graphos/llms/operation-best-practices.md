# Source: https://www.apollographql.com/docs/react/data/operation-best-practices.md

# GraphQL query best practices

When creating queries and mutations, follow these best practices to get the most out of both GraphQL and Apollo tooling.

## Name all operations

These two queries fetch the same data:

```graphql
# Recommended ✅
query GetBooks {
  books {
    title
  }
}

# Not recommended ❌
query {
  books {
    title
  }
}
```

The first query is named `GetBooks`. The second query is **anonymous**.

You should define a name for *every* GraphQL operation in your application. Doing so provides the following benefits:

* You clarify the purpose of each operation for both yourself and your teammates.
* You avoid unexpected errors when combining multiple operations in a single query document (an anonymous operation can only appear alone).
* You improve debugging output in both client *and* server code, helping you identify exactly which operation is causing issues.
* [Apollo GraphOS Studio](https://www.apollographql.com/docs/graphos/graphs/studio-features) provides helpful operation-level metrics, which require named operations.

## Use GraphQL variables to provide arguments

These two queries can both fetch a `Dog` object with ID `"5"`:

```graphql
# Recommended ✅
query GetDog($dogId: ID!) {
  dog(id: $dogId) {
    name
    breed
  }
}

# Not recommended ❌
query GetDog {
  dog(id: "5") {
    name
    breed
  }
}
```

The first query uses a variable (`$dogId`) for the value of the `dog` field's required argument. This means you can use the query to fetch a `Dog` object with *any* ID, making it much more reusable.

You pass variable values to `useQuery` (or `useMutation`) like so:

```js title=dog.tsx
const GET_DOG = gql`
  query GetDog($dogId: ID!) {
    dog(id: $dogId) {
      name
      breed
    }
  }
`;

function Dog({ id }) {
  const { loading, error, data } = useQuery(GET_DOG, {
    variables: {
      dogId: id,
    },
  });
  // ...render component...
}
```

### Disadvantages of hardcoded GraphQL arguments

Beyond reusability, hardcoded arguments have other disadvantages relative to variables:

#### Reduced cache effectiveness

If two otherwise identical queries have different hardcoded argument values, they're considered *entirely different operations* by your GraphQL server's cache. The cache enables your server to *skip* parsing and validating operations that it's encountered before, improving performance.

The server-side cache also powers features like [automatic persisted queries](https://www.apollographql.com/docs/apollo-server/performance/apq/) and query plans in a [federated gateway](https://www.apollographql.com/docs/federation/building-supergraphs/router/). Hardcoded arguments reduce the performance gains of these features and take up useful space in the cache.

#### Reduced information privacy

The value of a GraphQL argument might include sensitive information, such as an access token or a user's personal info. If this information is included in a query string, it's cached with the rest of that query string.

Variable values are *not* included in query strings. You can also specify *which* variable values (if any) are [included in metrics reporting](https://www.apollographql.com/docs/apollo-server/api/plugin/usage-reporting/#sendvariablevalues) to Studio.

## Query only the data you need, where you need it

One of GraphQL's biggest advantages over a traditional REST API is its support for [declarative data fetching](https://www.apollographql.com/docs/intro/benefits/#graphql-provides-declarative-efficient-data-fetching). Each component can (and should) query exactly the fields it requires to render, with no superfluous data sent over the network.

If instead your root component executes a single, enormous query to obtain data for all of its children, it might query on behalf of components that *aren't even rendered* given the current state. This can result in a delayed response, and it drastically reduces the likelihood that the query's result can be reused by a [server-side response cache](https://www.apollographql.com/docs/apollo-server/performance/caching/).

In the large majority of cases, a query such as the following should be divided into *multiple* queries that are distributed among the appropriate components:

```graphql
# Not recommended ❌
query GetGlobalStatus {
  stores {
    id
    name
    address {
      street
      city
    }
    employees {
      id
    }
    manager {
      id
    }
  }
  products {
    id
    name
    price {
      amount
      currency
    }
  }
  employees {
    id
    role
    name {
      firstName
      lastName
    }
    store {
      id
    }
  }
  offers {
    id
    products {
      id
    }
    discount {
      discountType
      amount
    }
  }
}
```

* If you have collections of components that *are* always rendered together, you can use fragments to distribute the structure of a single query between them. See [Colocating fragments](https://www.apollographql.com/docs/react/data/fragments/#colocating-fragments).
* If you're querying a list field that returns more items than your component needs to render, you should [paginate that field](https://www.apollographql.com/docs/react/pagination/overview/).

## Query global data and user-specific data separately

Some fields return the exact same data regardless of which user queries them:

```graphql
# Returns all elements of the periodic table
query GetAllElements {
  elements {
    atomicNumber
    name
    symbol
  }
}
```

Other fields return *different* data depending on which user queries them:

```graphql
# Returns the current user's documents
query GetMyDocuments {
  myDocuments {
    id
    title
    url
    updatedAt
  }
}
```

To improve the performance of your [server-side response cache](https://www.apollographql.com/docs/apollo-server/performance/caching/), fetch these two types of fields in *separate queries* whenever possible. By doing so, your server can cache just a *single* response for a query like `GetAllElements` above, while caching separate responses for each user that executes `GetMyDocuments`.

## Set your app's `name` and `version` for metrics reporting (paid)

This recommendation is *most* pertinent to Studio organizations with a [paid plan](https://www.apollographql.com/pricing/), however it can be helpful for all apps.

The constructor of `ApolloClient` accepts the `clientAwareness` option with `name` and `version` properties:

```js
const client = new ApolloClient({
  link: new HttpLink({ uri: "http://localhost:4000/graphql" }),
  cache: new InMemoryCache(),
  clientAwareness: {
    name: "MarketingSite",
    version: "1.2",
  },
});
```

If you specify these values, Apollo Client automatically adds them to each operation request as HTTP headers (`apollographql-client-name` and `apollographql-client-version`).

Then if you've configured metrics reporting in Studio, Apollo Server includes your app's `name` and `version` in the operation traces it reports to Studio. This enables you to [segment metrics by client](https://www.apollographql.com/docs/graphos/metrics/client-awareness/).
