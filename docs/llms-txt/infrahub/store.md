# Source: https://docs.infrahub.app/python-sdk/guides/store.md

# Using the client store

The client in the SDK contains a store that is used to store objects in a local cache.

The store is mainly used for the internal working of the SDK. It is used to create relations between objects that might not yet exist in the database, or to store relations for objects that were retrieved from the database, amongst other things.

The store stores objects that we are retrieving from Infrahub using the different query methods. This allows to not have to keep references to objects throughout scripts, or avoids situations where we have to re-execute queries.

Objects are stored in the following scenario:

* The resulting objects from using the SDK client's `get`, `filters` or `all` methods

- Async
- Sync

```
tag = await client.get(kind="BuiltinTag", name__value="RED")
tag_in_store = client.store.get(key=tag.id)
```

```
tag = client.get(kind="BuiltinTag", name__value="RED")
tag_in_store = client.store.get(key=tag.id)
```

* The resulting related objects for objects retrieved using the SDK client's query methods, when we use the `prefetch_relationships` argument.

- Async
- Sync

```
device = await client.get(kind="InfraDevice", name__value="atl1-edge1", prefetch_relationships=True)
site = client.store.get(key=device.site.id)
```

```
device = client.get(kind="InfraDevice", name__value="atl1-edge1", prefetch_relationships=True)
site = client.store.get(key=device.site.id)
```

* The related objects of a object's relationship when the `fetch` method is used

- Async
- Sync

```
device = await client.get(kind="InfraDevice", name__value="atl1-edge1")
await device.site.fetch()
site = client.store.get(key=device.site.id)
```

```
device = client.get(kind="InfraDevice", name__value="atl1-edge1")
device.site.fetch()
site = client.store.get(key=device.site.id)
```

* Objects that get created using the SDK

- Async
- Sync

```
tag = await client.create("BuiltinTag", name="BLACK")
await tag.save()
tag_in_store = client.store.get(key=tag.id)
```

```
tag = client.create("BuiltinTag", name="BLACK")
tag.save()
tag_in_store = client.store.get(key=tag.id)
```

## Retrieving objects from the store[​](#retrieving-objects-from-the-store "Direct link to Retrieving objects from the store")

You can retrieve objects from the store using their `id` or `hfid`. When using the `hfid`, we also have to provide the `kind` of the object that we want to retrieve.

* Async
* Sync

```
tag = await client.get("BuiltinTag", name__value="BLACK")
tag_in_store = client.store.get(key=tag.id)
tag == tag_in_store

tag = await client.get("BuiltinTag", name__value="BLACK")
tag_in_store = client.store.get(key=tag.hfid, kind="BuiltinTag")
tag == tag_in_store
```

```
tag = client.get("BuiltinTag", name__value="BLACK")
tag_in_store = client.store.get(key=tag.id)
tag == tag_in_store

tag = client.get("BuiltinTag", name__value="BLACK")
tag_in_store = client.store.get(key=tag.hfid, kind="BuiltinTag")
tag == tag_in_store
```

## Manually storing objects in the store[​](#manually-storing-objects-in-the-store "Direct link to Manually storing objects in the store")

You can store objects in the store manually using the `set` method. This has the advantage that you can choose a key that you want to use to reference the object in the store, besides the `id` or `hfid`. For example, we could use the name attribute value of the node as the key.

* Async
* Sync

```
tag = await client.get(kind="BuiltinTag", name__value="RED", populate_store=False)
client.store.set(key=tag.name.value, node=tag)

tag_in_store = client.store.get(key=tag.name.value)
tag_in_store = client.store.get(key=tag.id)
tag_in_store = client.store.get(key=tag.hfid, kind="BuiltinTag")
```

```
tag = client.get(kind="BuiltinTag", name__value="RED", populate_store=False)
client.store.set(key=tag.name.value, node=tag)

tag_in_store = client.store.get(key=tag.name.value)
tag_in_store = client.store.get(key=tag.id)
tag_in_store = client.store.get(key=tag.hfid, kind="BuiltinTag")
```

## Disable storing objects in the store using the different query methods[​](#disable-storing-objects-in-the-store-using-the-different-query-methods "Direct link to Disable storing objects in the store using the different query methods")

In some scenarios it might not be desirable to automatically store the retrieved objects in the store, when using the SDK client's different query methods. In this case you can set the `populate_store` argument to `False`.

* Async
* Sync

```
tag = await client.get(kind="BuiltinTag", name__value="RED", populate_store=False)
```

```
tag = client.get(kind="BuiltinTag", name__value="RED", populate_store=False)
```
