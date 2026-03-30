# Source: https://relay.dev/docs/api-reference/store/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API Reference]
-   [Relay Runtime]
-   [Store]

[Version: v20.1.0]

On this page

<div>

# Store

</div>

The Relay Store can be used to programmatically update client-side data inside [`updater` functions](/docs/guided-tour/updating-data/graphql-mutations/). The following is a reference of the Relay Store interface.

Table of Contents:

-   [RecordSourceSelectorProxy](#recordsourceselectorproxy)
-   [RecordProxy](#recordproxy)
-   [RecordSourceProxy](#recordsourceproxy)
-   [ConnectionHandler](#connectionhandler)

## RecordSourceSelectorProxy[​](#recordsourceselectorproxy "Direct link to RecordSourceSelectorProxy") 

The `RecordSourceSelectorProxy` is the type of the `store` that [`updater` functions](/docs/guided-tour/updating-data/graphql-mutations/) receive as an argument. The following is the `RecordSourceSelectorProxy` interface:

``` 
interface RecordSourceSelectorProxy 
```

### `create(dataID: string, typeName: string): RecordProxy`[​](#createdataid-string-typename-string-recordproxy "Direct link to createdataid-string-typename-string-recordproxy") 

Creates a new record in the store given a `dataID` and the `typeName` as defined by the GraphQL schema. Returns a [`RecordProxy`](#recordproxy) which serves as an interface to mutate the newly created record.

#### Example[​](#example "Direct link to Example") 

``` 
const record = store.create(dataID, 'Todo');
```

### `delete(dataID: string): void`[​](#deletedataid-string-void "Direct link to deletedataid-string-void") 

Deletes a record from the store given its `dataID`. For existing edges to the deleted record, `undefined` will be returned in the default case even when the value is typed as non-nullable. When [`@throwOnFieldError`](/docs/guides/throw-on-field-error-directive/) is present, the missing data will throw an error.

#### Example[​](#example-1 "Direct link to Example") 

``` 
store.delete(dataID);
```

### `get(dataID: string): ?RecordProxy`[​](#getdataid-string-recordproxy "Direct link to getdataid-string-recordproxy") 

Retrieves a record from the store given its `dataID`. Returns a [`RecordProxy`](#recordproxy) which serves as an interface to mutate the record.

#### Example[​](#example-2 "Direct link to Example") 

``` 
const record = store.get(dataID);
```

### `getRoot(): RecordProxy`[​](#getroot-recordproxy "Direct link to getroot-recordproxy") 

Returns the [`RecordProxy`](#recordproxy) representing the root of the GraphQL document.

#### Example[​](#example-3 "Direct link to Example") 

Given the GraphQL document:

``` 
viewer 
```

Usage:

``` 
// Represents root query
const root = store.getRoot();
// Get the viewer linked record
const viewer = root.getLinkedRecord('viewer');
```

### `getRootField(fieldName: string): ?RecordProxy`[​](#getrootfieldfieldname-string-recordproxy "Direct link to getrootfieldfieldname-string-recordproxy") 

Retrieves a root field from the store given the `fieldName`, as defined by the GraphQL document. Returns a [`RecordProxy`](#recordproxy) which serves as an interface to mutate the record.

#### Example[​](#example-4 "Direct link to Example") 

Given the GraphQL document:

``` 
viewer 
```

Usage:

``` 
const viewer = store.getRootField('viewer');
```

### `getPluralRootField(fieldName: string): ?Array<?RecordProxy>`[​](#getpluralrootfieldfieldname-string-arrayrecordproxy "Direct link to getpluralrootfieldfieldname-string-arrayrecordproxy") 

Retrieves a root field that represents a collection from the store given the `fieldName`, as defined by the GraphQL document. Returns an array of [`RecordProxies`](#recordproxy).

#### Example[​](#example-5 "Direct link to Example") 

Given the GraphQL document:

``` 
nodes(first: 10) 
```

Usage:

``` 
const nodes = store.getPluralRootField('nodes');
```

### `invalidateStore(): void`[​](#invalidatestore-void "Direct link to invalidatestore-void") 

Globally invalidates the Relay store. This will cause any data that was written to the store before invalidation occurred to be considered stale, and will be considered to require refetch the next time a query is checked with `environment.check()`.

#### Example[​](#example-6 "Direct link to Example") 

``` 
store.invalidateStore();
```

After global invalidation, any query that is checked before refetching it will be considered stale:

``` 
environment.check(query) === 'stale'
```

## RecordProxy[​](#recordproxy "Direct link to RecordProxy") 

The `RecordProxy` serves as an interface to mutate records:

``` 
interface RecordProxy 
```

### `getDataID(): string`[​](#getdataid-string "Direct link to getdataid-string") 

Returns the `dataID` of the current record.

#### Example[​](#example-7 "Direct link to Example") 

``` 
const id = record.getDataID();
```

### `getType(): string`[​](#gettype-string "Direct link to gettype-string") 

Gets the type of the current record, as defined by the GraphQL schema.

#### Example[​](#example-8 "Direct link to Example") 

``` 
const type = user.getType();  // User
```

### `getValue(name: string, arguments?: ?Object): mixed`[​](#getvaluename-string-arguments-object-mixed "Direct link to getvaluename-string-arguments-object-mixed") 

Gets the value of a field in the current record given the field name.

#### Example[​](#example-9 "Direct link to Example") 

Given the GraphQL document:

``` 
viewer 
```

Usage:

``` 
const name = viewer.getValue('name');
```

Optionally, if the field takes arguments, you can pass a bag of `variables`.

#### Example[​](#example-10 "Direct link to Example") 

Given the GraphQL document:

``` 
viewer 
```

Usage:

``` 
const name = viewer.getValue('name', );
```

### `getLinkedRecord(name: string, arguments?: ?Object): ?RecordProxy`[​](#getlinkedrecordname-string-arguments-object-recordproxy "Direct link to getlinkedrecordname-string-arguments-object-recordproxy") 

Retrieves a record associated with the current record given the field name, as defined by the GraphQL document. Returns a `RecordProxy`.

#### Example[​](#example-11 "Direct link to Example") 

Given the GraphQL document:

``` 
rootField 
}
```

Usage:

``` 
const rootField = store.getRootField('rootField');
const viewer = rootField.getLinkedRecord('viewer');
```

Optionally, if the linked record takes arguments, you can pass a bag of `variables` as well.

#### Example[​](#example-12 "Direct link to Example") 

Given the GraphQL document:

``` 
rootField 
}
```

Usage:

``` 
const rootField = store.getRootField('rootField');
const viewer = rootField.getLinkedRecord('viewer', );
```

### `getLinkedRecords(name: string, arguments?: ?Object): ?Array<?RecordProxy>`[​](#getlinkedrecordsname-string-arguments-object-arrayrecordproxy "Direct link to getlinkedrecordsname-string-arguments-object-arrayrecordproxy") 

Retrieves the set of records associated with the current record given the field name, as defined by the GraphQL document. Returns an array of `RecordProxies`.

#### Example[​](#example-13 "Direct link to Example") 

Given the GraphQL document:

``` 
rootField 
}
```

Usage:

``` 
const rootField = store.getRootField('rootField');
const nodes = rootField.getLinkedRecords('nodes');
```

Optionally, if the linked record takes arguments, you can pass a bag of `variables` as well.

#### Example[​](#example-14 "Direct link to Example") 

Given the GraphQL document:

``` 
rootField 
}
```

Usage:

``` 
const rootField = store.getRootField('rootField');
const nodes = rootField.getLinkedRecords('nodes', );
```

### `getOrCreateLinkedRecord(name: string, typeName: string, arguments?: ?Object)`[​](#getorcreatelinkedrecordname-string-typename-string-arguments-object "Direct link to getorcreatelinkedrecordname-string-typename-string-arguments-object") 

Retrieves a record associated with the current record given the field name, as defined by the GraphQL document. If the linked record does not exist, it will be created given the type name. Returns a `RecordProxy`.

#### Example[​](#example-15 "Direct link to Example") 

Given the GraphQL document:

``` 
rootField 
}
```

Usage:

``` 
const rootField = store.getRootField('rootField');
const newViewer = rootField.getOrCreateLinkedRecord('viewer', 'User'); // Will create if it doesn't exist
```

Optionally, if the linked record takes arguments, you can pass a bag of `variables` as well.

### `setValue(value: mixed, name: string, arguments?: ?Object): RecordProxy`[​](#setvaluevalue-mixed-name-string-arguments-object-recordproxy "Direct link to setvaluevalue-mixed-name-string-arguments-object-recordproxy") 

Mutates the current record by setting a new value on the specified field. Returns the mutated record.

Given the GraphQL document:

``` 
viewer 
```

Usage:

``` 
viewer.setValue('New Name', 'name');
```

Optionally, if the field takes arguments, you can pass a bag of `variables`.

``` 
viewer.setValue('New Name', 'name', );
```

### `copyFieldsFrom(sourceRecord: RecordProxy): void`[​](#copyfieldsfromsourcerecord-recordproxy-void "Direct link to copyfieldsfromsourcerecord-recordproxy-void") 

Mutates the current record by copying the fields over from the passed in record `sourceRecord`.

#### Example[​](#example-16 "Direct link to Example") 

``` 
const record = store.get(id1);
const otherRecord = store.get(id2);
record.copyFieldsFrom(otherRecord); // Mutates `record`
```

### `setLinkedRecord(record: RecordProxy, name: string, arguments?: ?Object)`[​](#setlinkedrecordrecord-recordproxy-name-string-arguments-object "Direct link to setlinkedrecordrecord-recordproxy-name-string-arguments-object") 

Mutates the current record by setting a new linked record on the given field name.

#### Example[​](#example-17 "Direct link to Example") 

Given the GraphQL document:

``` 
rootField 
}
```

Usage:

``` 
const rootField = store.getRootField('rootField');
const newViewer = store.create(/* ... */);
rootField.setLinkedRecord(newViewer, 'viewer');
```

Optionally, if the linked record takes arguments, you can pass a bag of `variables` as well.

### `setLinkedRecords(records: Array<RecordProxy>, name: string, variables?: ?Object)`[​](#setlinkedrecordsrecords-arrayrecordproxy-name-string-variables-object "Direct link to setlinkedrecordsrecords-arrayrecordproxy-name-string-variables-object") 

Mutates the current record by setting a new set of linked records on the given field name.

#### Example[​](#example-18 "Direct link to Example") 

Given the GraphQL document:

``` 
rootField 
}
```

Usage:

``` 
const rootField = store.getRootField('rootField');
const newNode = store.create(/* ... */);
const newNodes = [...rootField.getLinkedRecords('nodes'), newNode];
rootField.setLinkedRecords(newNodes, 'nodes');
```

Optionally, if the linked record takes arguments, you can pass a bag of `variables` as well.

### `invalidateRecord(): void`[​](#invalidaterecord-void "Direct link to invalidaterecord-void") 

Invalidates the record. This will cause any query that references this record to be considered stale until the next time it is refetched, and will be considered to require a refetch the next time such a query is checked with `environment.check()`.

#### Example[​](#example-19 "Direct link to Example") 

``` 
const record = store.get('4');
record.invalidateRecord();
```

After invalidating a record, any query that references the invalidated record and that is checked before refetching it will be considered stale:

``` 
environment.check(query) === 'stale'
```

## RecordSourceProxy[​](#recordsourceproxy "Direct link to RecordSourceProxy") 

The `RecordSourceProxy` serves as an interface to mutate record.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTUuMDUuMzFjLjgxIDIuMTcuNDEgMy4zOC0uNTIgNC4zMUMzLjU1IDUuNjcgMS45OCA2LjQ1LjkgNy45OGMtMS40NSAyLjA1LTEuNyA2LjUzIDMuNTMgNy43LTIuMi0xLjE2LTIuNjctNC41Mi0uMy02LjYxLS42MSAyLjAzLjUzIDMuMzMgMS45NCAyLjg2IDEuMzktLjQ3IDIuMy41MyAyLjI3IDEuNjctLjAyLjc4LS4zMSAxLjQ0LTEuMTMgMS44MSAzLjQyLS41OSA0Ljc4LTMuNDIgNC43OC01LjU2IDAtMi44NC0yLjUzLTMuMjItMS4yNS01LjYxLTEuNTIuMTMtMi4wMyAxLjEzLTEuODkgMi43NS4wOSAxLjA4LTEuMDIgMS44LTEuODYgMS4zMy0uNjctLjQxLS42Ni0xLjE5LS4wNi0xLjc4QzguMTggNS4zMSA4LjY4IDIuNDUgNS4wNS4zMkw1LjAzLjNsLjAyLjAxeiI+PC9wYXRoPjwvc3ZnPg==)]danger

`RecordSourceProxy` exposes many low level APIs that are not typesafe. Users should consider using [typesafe updaters](/docs/guided-tour/updating-data/typesafe-updaters-faq/), [optimistic updates](/docs/guided-tour/updating-data/graphql-mutations/#optimistic-updates), and [relay resolvers](/docs/guides/relay-resolvers/introduction/) instead if their use case can be covered by these alternatives.

``` 
interface RecordSourceProxy 
```

### `create(dataID: DataID, typeName: string): RecordProxy`[​](#createdataid-dataid-typename-string-recordproxy "Direct link to createdataid-dataid-typename-string-recordproxy") 

Creates a new record in the store given a `dataID` and the `typeName` as defined by the GraphQL schema. Returns a [`RecordProxy`](#recordproxy) which serves as an interface to mutate the newly created record.

#### Example[​](#example-20 "Direct link to Example") 

``` 
const record = store.create(dataID, 'Todo');
```

### `delete(dataID: DataID): void`[​](#deletedataid-dataid-void "Direct link to deletedataid-dataid-void") 

Deletes a record from the store given its `dataID`. For existing edges to the deleted record, `undefined` will be returned in the default case even when the value is typed as non-nullable. When [`@throwOnFieldError`](/docs/guides/throw-on-field-error-directive/) is present, the missing data will throw an error.

#### Example[​](#example-21 "Direct link to Example") 

``` 
store.delete(dataID);
```

### `get(dataID: DataID): ?RecordProxy`[​](#getdataid-dataid-recordproxy "Direct link to getdataid-dataid-recordproxy") 

Retrieves a record from the store given its `dataID`. Returns a [`RecordProxy`](#recordproxy) which serves as an interface to read/mutate the record.

#### Example[​](#example-22 "Direct link to Example") 

``` 
const record = store.get(dataID);
```

### `getRoot(): RecordProxy`[​](#getroot-recordproxy-1 "Direct link to getroot-recordproxy-1") 

Returns the [`RecordProxy`](#recordproxy) representing the root of the GraphQL document.

#### Example[​](#example-23 "Direct link to Example") 

Given the GraphQL document:

``` 
viewer 
```

Usage:

``` 
// Represents root query
const root = store.getRoot();
// Get the viewer linked record
const viewer = root.getLinkedRecord('viewer');
```

### `invalidateStore(): void;`[​](#invalidatestore-void-1 "Direct link to invalidatestore-void-1") 

Globally invalidates the Relay store. This will cause any data that was written to the store before invalidation occurred to be considered stale, and will be considered to require refetch the next time a query is checked with `environment.check()` or is fetched with a `store-or-network` [fetch policy](/docs/guided-tour/reusing-cached-data/fetch-policies/).

#### Example[​](#example-24 "Direct link to Example") 

``` 
store.invalidateStore();
```

After global invalidation, any query that is checked before refetching it will be considered stale:

``` 
environment.check(query) === 'stale'
```

### `readUpdatableFragment(fragment: UpdatableFragment<TFragmentType, TData>,fragmentReference: HasUpdatableSpread<TFragmentType>): UpdatableData<TData>;`[​](#readupdatablefragmentfragment-updatablefragmenttfragmenttype-tdatafragmentreference-hasupdatablespreadtfragmenttype-updatabledatatdata "Direct link to readupdatablefragmentfragment-updatablefragmenttfragmenttype-tdatafragmentreference-hasupdatablespreadtfragmenttype-updatabledatatdata") 

Fetches an updatable fragment from the store. This updatable fragment\'s fields can then be imperatively modified to update data in the store.

For more information on updating the store imperatively, see this [section](/docs/guided-tour/updating-data/imperatively-modifying-store-data/) of the guided tour.

#### Example[​](#example-25 "Direct link to Example") 

``` 
const fragment = graphql`
  fragment StoryLikeButton_updatable on Story @updatable 
`;
const  = store.readUpdatableFragment(
  fragment,
  story
);
updatableData.likeCount = updatableData.likeCount + 1
```

### `readUpdatableQuery(query: UpdatableQuery<TVariables, TData>,variables: TVariables): UpdatableData<TData>`[​](#readupdatablequeryquery-updatablequerytvariables-tdatavariables-tvariables-updatabledatatdata "Direct link to readupdatablequeryquery-updatablequerytvariables-tdatavariables-tvariables-updatabledatatdata") 

Reads an updatable query from the store. This updatable query\'s fields can be imperatively modified to update data in the store. Unlike `readUpdatableFragment`, you do not need to pass in a `fragmentReference` as an input argument.

For more information on updating the store imperatively, see this [section](/docs/guided-tour/updating-data/imperatively-modifying-store-data/) of the guided tour.

#### Example[​](#example-26 "Direct link to Example") 

``` 
const  = store.readUpdatableQuery(
  graphql`
    query NameUpdaterUpdateQuery @updatable 
    }
  `,
  
);
const viewer = updatableData.viewer;
viewer.name = newName;
```

## ConnectionHandler[​](#connectionhandler "Direct link to ConnectionHandler") 

`ConnectionHandler` is a utility module exposed by `relay-runtime` that aids in the manipulation of connections. `ConnectionHandler` exposes the following interface:

``` 
interface ConnectionHandler 
```

### `getConnection(record: RecordProxy, key: string, filters?: ?Object)`[​](#getconnectionrecord-recordproxy-key-string-filters-object "Direct link to getconnectionrecord-recordproxy-key-string-filters-object") 

Given a record and a connection key, and optionally a set of filters, `getConnection` retrieves a [`RecordProxy`](#recordproxy) that represents a connection that was annotated with a `@connection` directive.

First, let\'s take a look at a plain connection:

``` 
fragment FriendsFragment on User 
    }
  }
}
```

Accessing a plain connection field like this is the same as other regular fields:

``` 
// The `friends` connection record can be accessed with:
const user = store.get(userID);
const friends = user && user.getLinkedRecord('friends');

// Access fields on the connection:
const edges = friends && friends.getLinkedRecords('edges');
```

When using [usePaginationFragment](/docs/api-reference/use-pagination-fragment/), we usually annotate the actual connection field with `@connection` to tell Relay which part needs to be paginated:

``` 
fragment FriendsFragment on User 
    }
  }
}
```

For connections like the above, `ConnectionHandler` helps us find the record:

``` 
import  from 'relay-runtime';

// The `friends` connection record can be accessed with:
const user = store.get(userID);
const friends = ConnectionHandler.getConnection(
 user,                        // parent record
 'FriendsFragment_friends',   // connection key
        // 'filters' that is used to identify the connection
);
// Access fields on the connection:
const edges = friends.getLinkedRecords('edges');
```

### Edge creation and insertion[​](#edge-creation-and-insertion "Direct link to Edge creation and insertion") 

#### `createEdge(store: RecordSourceProxy, connection: RecordProxy, node: RecordProxy, edgeType: string)`[​](#createedgestore-recordsourceproxy-connection-recordproxy-node-recordproxy-edgetype-string "Direct link to createedgestore-recordsourceproxy-connection-recordproxy-node-recordproxy-edgetype-string") 

Creates an edge given a [`store`](#recordsourceselectorproxy), a connection, the edge node, and the edge type.

#### `insertEdgeBefore(connection: RecordProxy, newEdge: RecordProxy, cursor?: ?string)`[​](#insertedgebeforeconnection-recordproxy-newedge-recordproxy-cursor-string "Direct link to insertedgebeforeconnection-recordproxy-newedge-recordproxy-cursor-string") 

Given a connection, inserts the edge at the beginning of the connection, or before the specified `cursor`.

#### `insertEdgeAfter(connection: RecordProxy, newEdge: RecordProxy, cursor?: ?string)`[​](#insertedgeafterconnection-recordproxy-newedge-recordproxy-cursor-string "Direct link to insertedgeafterconnection-recordproxy-newedge-recordproxy-cursor-string") 

Given a connection, inserts the edge at the end of the connection, or after the specified `cursor`.

#### Example[​](#example-27 "Direct link to Example") 

``` 
const user = store.get(userID);
const friends = ConnectionHandler.getConnection(user, 'FriendsFragment_friends');
const newFriend = store.get(newFriendId);
const edge = ConnectionHandler.createEdge(store, friends, newFriend, 'UserEdge');

// No cursor provided, append the edge at the end.
ConnectionHandler.insertEdgeAfter(friends, edge);

// No cursor provided, insert the edge at the front:
ConnectionHandler.insertEdgeBefore(friends, edge);
```

### `deleteNode(connection: RecordProxy, nodeID: string): void`[​](#deletenodeconnection-recordproxy-nodeid-string-void "Direct link to deletenodeconnection-recordproxy-nodeid-string-void") 

Given a connection, deletes any edges whose node id matches the given id.

#### Example[​](#example-28 "Direct link to Example") 

``` 
const user = store.get(userID);
const friends = ConnectionHandler.getConnection(user, 'FriendsFragment_friends');
ConnectionHandler.deleteNode(friends, idToDelete);
```

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/api-reference/relay-runtime/store.md)