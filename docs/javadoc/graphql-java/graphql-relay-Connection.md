JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

graphql.relay

## Interface Connection<T>

- 

All Known Implementing Classes:
DefaultConnection

---

```
@PublicApi
public interface Connection<T>
```

This represents a connection in Relay, which is a list of `edge`s
 as well as a `pageInfo` that describes the pagination of that list.

 See https://facebook.github.io/relay/graphql/connections.htm

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description

`java.util.List<Edge<T>>`
`getEdges()` 

`PageInfo`
`getPageInfo()` 

- 

  - 

### Method Detail

    - 

#### getEdges

```
java.util.List<Edge<T>> getEdges()
```

Returns:
a list of `Edge`s that are really a node of data and its cursor

    - 

#### getPageInfo

```
PageInfo getPageInfo()
```

Returns:
`PageInfo` pagination data about about that list of edges

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method