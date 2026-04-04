# Apollo Client Get Started Guide

Source: https://www.apollographql.com/docs/react/get-started

## Overview

Apollo Client is a comprehensive JavaScript library for managing GraphQL data in applications. This guide walks through initial setup, dependency installation, client initialization, React integration, and executing your first data queries.

## Step 1: Project Setup

Create a new React project using either:
- **Vite**: Local development environment
- **CodeSandbox**: Cloud-based development sandbox

## Step 2: Installing Required Packages

Three core packages are essential:

1. **@apollo/client** - "This single package contains virtually everything you need to set up Apollo Client"
2. **graphql** - Provides GraphQL query parsing logic
3. **rxjs** - Supplies the Observable primitive used throughout the library

Install via npm:

```bash
npm install @apollo/client graphql rxjs
```

The tutorial uses the FlyBy GraphQL API endpoint for demonstration purposes.

## Step 3: ApolloClient Initialization

### Import Required Symbols

```javascript
import { ApolloClient, HttpLink, InMemoryCache, gql } from "@apollo/client";
import { ApolloProvider } from "@apollo/client/react";
```

### Create Client Instance

```javascript
const client = new ApolloClient({
  link: new HttpLink({ uri: "https://flyby-router-demo.herokuapp.com/" }),
  cache: new InMemoryCache(),
});
```

**Configuration explanation:**
- **link**: Apollo Link that executes GraphQL operations against your server via HttpLink
- **cache**: InMemoryCache instance for storing fetched results

### Test with Plain JavaScript

```javascript
client
  .query({
    query: gql`
      query GetLocations {
        locations {
          id
          name
          description
          photo
        }
      }
    `,
  })
  .then((result) => console.log(result));
```

## Step 4: React Integration with ApolloProvider

Wrap your application with ApolloProvider near the root level:

```javascript
import React from "react";
import * as ReactDOM from "react-dom/client";
import { ApolloClient, InMemoryCache } from "@apollo/client";
import { ApolloProvider } from "@apollo/client/react";
import App from "./App";

const client = new ApolloClient({
  uri: "https://flyby-router-demo.herokuapp.com/",
  cache: new InMemoryCache(),
});

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>
);
```

## Step 5: Fetching Data with useQuery Hook

### Define Your Query

```javascript
import { gql } from "@apollo/client";
import { useQuery } from "@apollo/client/react";

const GET_LOCATIONS = gql`
  query GetLocations {
    locations {
      id
      name
      description
      photo
    }
  }
`;
```

### Create Display Component

```javascript
function DisplayLocations() {
  const { loading, error, data } = useQuery(GET_LOCATIONS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error : {error.message}</p>;

  return data.locations.map(({ id, name, description, photo }) => (
    <div key={id}>
      <h3>{name}</h3>
      <img width="400" height="250" alt="location-reference" src={`${photo}`} />
      <br />
      <b>About this location:</b>
      <p>{description}</p>
      <br />
    </div>
  ));
}
```

### Hook Return Values

The `useQuery` hook returns an object with:
- **loading**: Boolean tracking query execution state
- **error**: Contains error details if the query fails
- **data**: The actual query results once available
- **dataState**: Additional state information

### Integrate into App

```javascript
export default function App() {
  return (
    <div>
      <h2>My first Apollo app 🚀</h2>
      <br />
      <DisplayLocations />
    </div>
  );
}
```

## Next Learning Steps

After mastering basics, explore:
- **Queries**: Advanced query patterns with arguments
- **Fragments**: Data masking and component-driven architecture
- **Mutations**: Writing and updating data
- **TypeScript**: Adding type safety
- **API Reference**: Direct client access patterns

---

**Note**: Complete working examples are available on CodeSandbox for reference and comparison during development.
