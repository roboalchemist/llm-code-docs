# Source: https://www.apollographql.com/docs/react/api/react/useSubscription.md

# useSubscription

## [`useSubscription`](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription)

> Refer to the [Subscriptions](https://www.apollographql.com/docs/react/data/subscriptions.md) section for a more in-depth overview of `useSubscription`.

#### Consider using `onData` instead of `useEffect`

If you want to react to incoming data, please use the `onData` option instead of `useEffect`. State updates you make inside a `useEffect` hook might cause additional rerenders, and `useEffect` is mostly meant for side effects of rendering, not as an event handler. State updates made in an event handler like `onData` might - depending on the React version - be batched and cause only a single rerender.

Consider the following component:

JavaScript

```
export function Subscriptions() {
  const { data, error, loading } = useSubscription(query);
  const [accumulatedData, setAccumulatedData] = useState([]);

  useEffect(() => {
    setAccumulatedData((prev) => [...prev, data]);
  }, [data]);

  return (
    <>
      {loading && <p>Loading...</p>}
      {JSON.stringify(accumulatedData, undefined, 2)}
    </>
  );
}
```

Instead of using `useEffect` here, we can re-write this component to use the `onData` callback function accepted in `useSubscription`'s `options` object:

JavaScript

```
export function Subscriptions() {
  const [accumulatedData, setAccumulatedData] = useState([]);
  const { data, error, loading } = useSubscription(query, {
    onData({ data }) {
      setAccumulatedData((prev) => [...prev, data]);
    },
  });

  return (
    <>
      {loading && <p>Loading...</p>}
      {JSON.stringify(accumulatedData, undefined, 2)}
    </>
  );
}
```

> ⚠️ **Note:** The `useSubscription` option `onData` is available in Apollo Client >= 3.7. In previous versions, the equivalent option is named `onSubscriptionData`.

Now, the first message will be added to the `accumulatedData` array since `onData` is called *before* the component re-renders. React 18 automatic batching is still in effect and results in a single re-render, but with `onData` we can guarantee each message received after the component mounts is added to `accumulatedData`.

### [Example](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription-example)

JavaScript

```
 const COMMENTS_SUBSCRIPTION = gql`
   subscription OnCommentAdded($repoFullName: String!) {
     commentAdded(repoFullName: $repoFullName) {
       id
       content
     }
   }
 `;

 function DontReadTheComments({ repoFullName }) {
   const {
     data: { commentAdded },
     loading,
   } = useSubscription(COMMENTS_SUBSCRIPTION, { variables: { repoFullName } });
   return <h4>New comment: {!loading && commentAdded.content}</h4>;
 }
```

### [Signature](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription-signature)

TypeScript

```
useSubscription<TData, TVariables>(
  subscription: DocumentNode | TypedDocumentNode<TData, TVariables>,
  [options]: {} extends (TVariables) ? [
    options?: useSubscription.Options<NoInfer<TData>, NoInfer<TVariables>>
] : [options: useSubscription.Options<NoInfer<TData>, NoInfer<TVariables>>]
): useSubscription.Result<TData>
```

[(src/react/hooks/useSubscription.ts)](https://github.com/apollographql/apollo-client/blob/main/src/react/hooks/useSubscription.ts)

### [Parameters](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription-parameters)

Name / Type

Description

[`subscription`](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription-parameters-subscription)\
`DocumentNode | TypedDocumentNode<TData, TVariables>`

A GraphQL subscription document parsed into an AST by `gql`.

[`[options]`](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription-parameters-\[options])\
`{} extends (TVariables) ? [ options?: useSubscription.Options<NoInfer<TData>, NoInfer<TVariables>> ] : [options: useSubscription.Options<NoInfer<TData>, NoInfer<TVariables>>]`

### [Result](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription-result)

Query result object

```
useSubscription.Result<TData>
```

Show/hide child attributes

###### [`data`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription-result-data)

`MaybeMasked<TData>`

An object containing the result of your GraphQL subscription. Defaults to an empty object.

###### [`error`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription-result-error)

`ErrorLike`

A runtime error with `graphQLErrors` and `networkError` properties

###### [`loading`](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription-result-loading)

`boolean`

A boolean that indicates whether any initial data has been returned

###### [`restart`](https://www.apollographql.com/docs/react/api/react/useSubscription.md#usesubscription-result-restart)

`() => void`

A function that when called will disconnect and reconnect the connection to the subscription. If the subscription is deduplicated, this will restart the connection for all deduplicated subscriptions.
