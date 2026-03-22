# Source: https://www.apollographql.com/docs/react/api/react/useFragment.md

# useFragment

## [`useFragment`](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment)

`useFragment` represents a lightweight live binding into the Apollo Client Cache and enables Apollo Client to broadcast very specific fragment results to individual components. This hook returns an always-up-to-date view of whatever data the cache currently contains for a given fragment. `useFragment` never triggers network requests of its own.

Note that the `useQuery` hook remains the primary hook responsible for querying and populating data in the cache ([see the API reference](https://www.apollographql.com/hooks#usequery)). As a result, the component reading the fragment data via `useFragment` is still subscribed to all changes in the query data, but receives updates only when that fragment's specific data change.

To view a `useFragment` example, see the [Fragments](https://www.apollographql.com/docs/react/data/fragments.md#usefragment) page.

### [Signature](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-signature)

TypeScript

```
useFragment<TData, TVariables>(
  { fragment, from, fragmentName, variables, optimistic, client, }: useFragment.Options<TData, TVariables>
): useFragment.Result<TData>
```

### [Parameters](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-parameters)

Name / Type

Description

[`{ fragment, from, fragmentName, variables, optimistic, client, }`](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-parameters-\{%20fragment,%20from,%20fragmentname,%20variables,%20optimistic,%20client,%20})\
`useFragment.Options<TData, TVariables>`

Show/hide child attributes

Operation options

###### [`client`*(optional)*](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-parameters-\{%20fragment,%20from,%20fragmentname,%20variables,%20optimistic,%20client,%20}-client)

`ApolloClient`

The instance of `ApolloClient` to use to look up the fragment.

By default, the instance that's passed down via context is used, but you can provide a different instance here.

Other

###### [`fragment`](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-parameters-\{%20fragment,%20from,%20fragmentname,%20variables,%20optimistic,%20client,%20}-fragment)

`DocumentNode | TypedDocumentNode<TData, TVariables>`

A GraphQL document created using the `gql` template string tag from `graphql-tag` with one or more fragments which will be used to determine the shape of data to read. If you provide more than one fragment in this document then you must also specify `fragmentName` to select a single.

###### [`fragmentName`*(optional)*](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-parameters-\{%20fragment,%20from,%20fragmentname,%20variables,%20optimistic,%20client,%20}-fragmentname)

`string`

The name of the fragment in your GraphQL document to be used. If you do not provide a `fragmentName` and there is only one fragment in your `fragment` document then that fragment will be used.

###### [`from`](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-parameters-\{%20fragment,%20from,%20fragmentname,%20variables,%20optimistic,%20client,%20}-from)

`useFragment.FromOptionValue<TData> | Array<useFragment.FromOptionValue<TData> | null> | null`

An object or array containing a `__typename` and primary key fields (such as `id`) identifying the entity object from which the fragment will be retrieved, or a `{ __ref: "..." }` reference, or a `string` ID (uncommon).

###### [`optimistic`*(optional)*](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-parameters-\{%20fragment,%20from,%20fragmentname,%20variables,%20optimistic,%20client,%20}-optimistic)

`boolean`

Whether to read from optimistic or non-optimistic cache data. If this named option is provided, the optimistic parameter of the readQuery method can be omitted.

###### [`variables`*(optional)*](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-parameters-\{%20fragment,%20from,%20fragmentname,%20variables,%20optimistic,%20client,%20}-variables)

`NoInfer<TVariables>`

Any variables that the GraphQL query may depend on.

### [Result](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-result)

```
useFragment.Result<TData>
```

Show/hide child attributes

###### [`complete`](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-result-complete)

`boolean`

###### [`data`](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-result-data)

`MaybeMasked<TData> | DataValue.Partial<MaybeMasked<TData>>`

###### [`missing`*(optional)*](https://www.apollographql.com/docs/react/api/react/useFragment.md#usefragment-result-missing)

`MissingTree`

A tree of all `MissingFieldError` messages reported during fragment reading, where the branches of the tree indicate the paths of the errors within the query result.
