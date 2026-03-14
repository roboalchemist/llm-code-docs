# Source: https://docs.logrocket.com/reference/graphql-1.md

# GraphQL

By default, LogRocket will automatically capture all GraphQL requests/responses along with bodies/headers from the front-end:

![894](https://files.readme.io/a12028c-network_reqs_graphql.png "network reqs graphql.png")

Use this data to help troubleshoot the root cause of issues.

### Apollo Client with GraphQL

If network requests are not appearing when using Apollo Client, add this code to your application:

```javascript apollo-client
import { ApolloClient } from 'apollo-client';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { createHttpLink } from 'apollo-link-http';

const fetcher = (...args) => {
  return window.fetch(...args);
};

const client = new ApolloClient({
  link: createHttpLink({ 
    uri: 'https://yourgraphql.api',
    fetch: fetcher,
  }),
  cache: new InMemoryCache()
});
```