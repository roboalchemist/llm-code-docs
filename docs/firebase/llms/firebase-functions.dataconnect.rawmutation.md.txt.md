# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawmutation.md.txt

# dataconnect.RawMutation interface

**Signature:**

    export interface RawMutation<V, R> 

## Properties

| Property | Type | Description |
|---|---|---|
| [data](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawmutation.md#dataconnectrawmutationdata) | R |   |
| [errors](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawmutation.md#dataconnectrawmutationerrors) | Array\<[GraphqlError](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.graphqlerror.md#dataconnectgraphqlerror_interface)\> |   |
| [variables](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawmutation.md#dataconnectrawmutationvariables) | V |   |

## dataconnect.RawMutation.data

**Signature:**

    data: R;

## dataconnect.RawMutation.errors

**Signature:**

    errors: Array<GraphqlError>;

## dataconnect.RawMutation.variables

**Signature:**

    variables: V;