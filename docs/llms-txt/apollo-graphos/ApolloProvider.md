# Source: https://www.apollographql.com/docs/react/api/react/ApolloProvider.md

# ApolloProvider

## The `ApolloProvider` component

The `ApolloProvider` component uses [React's Context API](https://react.dev/reference/react/useContext) to make a configured Apollo Client instance available throughout a React component tree. This component can be imported directly from the `@apollo/client/react` package.

```js
import { ApolloProvider } from "@apollo/client/react";
```

### Props

| Option   | Type           | Description                 |
| -------- | -------------- | --------------------------- |
| `client` | `ApolloClient` | An `ApolloClient` instance. |

### Example

```jsx
const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: "http://localhost:4000/graphql",
  }),
});

ReactDOM.render(
  <ApolloProvider client={client}>
    <MyRootComponent />
  </ApolloProvider>,
  document.getElementById("root")
);
```
