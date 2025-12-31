# Source: https://docs.apify.com/platform/storage/key-value-store.md

# Key-value store

**Store anything from Actor or task run results, JSON documents, or images. Learn how to access and manage key-value stores from Apify Console or via API.**

<!-- -->

***

The key-value store is simple storage that can be used for storing any kind of data. It can be JSON or HTML documents, zip files, images, or strings. The data are stored along with their https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types.

Each Actor run is assigned its own key-value store when it is created. The store contains the Actor's input, and, if necessary, other data such as its output.

Key-value stores are mutable–you can both add entries and delete them.

> Named key-value stores are retained indefinitely.<br />Unnamed key-value stores expire after 7 days unless otherwise specified.<br />> https://docs.apify.com/platform/storage/usage.md#named-and-unnamed-storages

## Basic usage

You can access key-value stores through several methods

* https://console.apify.com - provides an easy-to-understand interface.
* https://docs.apify.com/api/v2.md - for accessing your key-value stores programmatically.
* https://docs.apify.com/api.md - to access your key-value stores from any Node.js/Python application.
* https://docs.apify.com/sdk.md - when building your own JavaScript/Python Actor.

### Apify Console

In https://console.apify.com, you can view your key-value stores in the https://console.apify.com/storage section under the https://console.apify.com/storage?tab=keyValueStores tab.

![Key-value stores in app](/assets/images/key-value-stores-app-e32c8eb13addf4990370a0b02b7f3919.png)

To view a key-value store's content, click on its **Store ID**. Under the **Actions** menu, you can rename your store (and, in turn extend its https://docs.apify.com/platform/storage/usage.md#named-and-unnamed-storages) and grant https://docs.apify.com/platform/collaboration.md using the **Share** button. Click on the **API** button to view and test a store's https://docs.apify.com/api/v2/storage-key-value-stores.md.

![Key-value stores detail](/assets/images/key-value-stores-detail-header-065c0dbe9b1522325fb960e2a04069e5.png)

On the bottom of the page, you can view, download, and delete the individual records.

![Key-value stores detail](/assets/images/key-value-stores-detail-records-8b18bc5706eced51ac226112a5a79f40.png)

### Apify API

The https://docs.apify.com/api/v2/storage-key-value-stores.md enables you programmatic access to your key-value stores using https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods.

If you are accessing your datasets using the `username~store-name` https://docs.apify.com/platform/storage.md, you will need to use your secret API token. You can find the token (and your user ID) on the https://console.apify.com/account#/integrations tab of **Settings** page of your Apify account.

> When providing your API authentication token, we recommend using the request's `Authorization` header, rather than the URL. (https://docs.apify.com/platform/integrations/api.md#authentication).

To retrieve a list of your key-value stores, send a GET request to the https://docs.apify.com/api/v2/key-value-stores-get.md endpoint.


```
https://api.apify.com/v2/key-value-stores
```


To get information about a key-value store such as its creation time and item count, send a GET request to the https://docs.apify.com/api/v2/key-value-store-get.md endpoint.


```
https://api.apify.com/v2/key-value-stores/{STORE_ID}
```


To get a record (its value) from a key-value store, send a GET request to the https://docs.apify.com/api/v2/key-value-store-record-get.md endpoint.


```
https://api.apify.com/v2/key-value-stores/{STORE_ID}/records/{KEY_ID}
```


To add a record with a specific key in a key-value store, send a PUT request to the https://docs.apify.com/api/v2/key-value-store-record-put.md endpoint.


```
https://api.apify.com/v2/key-value-stores/{STORE_ID}/records/{KEY_ID}
```


Example payload:


```
{
    "foo": "bar",
    "fos": "baz"
}
```


To delete a record, send a DELETE request specifying the key from a key-value store to the https://docs.apify.com/api/v2/key-value-store-record-delete.md endpoint.


```
https://api.apify.com/v2/key-value-stores/{STORE_ID}/records/{KEY_ID}
```


For further details and a breakdown of each storage API endpoint, refer to the https://docs.apify.com/api/v2/storage-key-value-stores.md.

### Apify API Clients

#### JavaScript API client

The Apify https://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient (`apify-client`) enables you to access your key-value stores from any Node.js application, whether hosted on the Apify platform or externally.

After importing and initiating the client, you can save each key-value store to a variable for easier access.


```
const myKeyValStoreClient = apifyClient.keyValueStore(
    'jane-doe/my-key-val-store',
);
```


You can then use that variable to https://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient.

Check out the https://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient for https://docs.apify.com/api/client/js/docs and more details.

#### Python API client

The Apify https://docs.apify.com/api/client/python/reference/class/KeyValueStoreClient (`apify-client`) allows you to access your key-value stores from any Python application, whether it is running on the Apify platform or externally.

After importing and initiating the client, you can save each key-value store to a variable for easier access.


```
my_key_val_store_client = apify_client.key_value_store('jane-doe/my-key-val-store')
```


You can then use that variable to https://docs.apify.com/api/client/python/reference/class/KeyValueStoreClient.

Check out the https://docs.apify.com/api/client/python/reference/class/KeyValueStoreClient for https://docs.apify.com/api/client/python/docs/overview/introduction and more details.

### Apify SDKs

#### JavaScript SDK

When working with a JavaScript https://docs.apify.com/platform/actors.md, the https://docs.apify.com/sdk/js/docs/guides/result-storage#key-value-store is an essential tool, especially for key-value store management. The primary class for this purpose is the https://docs.apify.com/sdk/js/reference/class/KeyValueStore. This class allows you to decide whether your data will be stored locally or in the Apify cloud. For data manipulation, it offers the https://docs.apify.com/sdk/js/reference/class/KeyValueStore#getValue and https://docs.apify.com/sdk/js/reference/class/KeyValueStore#setValue methods to retrieve and assign values, respectively.

Additionally, you can iterate over the keys in your store using the https://docs.apify.com/sdk/js/reference/class/KeyValueStore#forEachKey method.

Every Actor run is linked to a default key-value store that is automatically created for that specific run. If you're running your Actors and opt to store data locally, you can easily supply the https://docs.apify.com/platform/actors/running/input-and-output.md by placing an *INPUT.json* file in the corresponding directory of the default key-value store. This method ensures that you Actor has all the necessary data readily available for its execution.

You can find *INPUT.json* and other key-value store files in the location below.


```
{APIFY_LOCAL_STORAGE_DIR}/key_value_stores/{STORE_ID}/{KEY}.{EXT}
```


The default key-value store's ID is *default*. The `{KEY}` is the record's *key* and `{EXT}` corresponds to the record value's MIME content type.

To manage your key-value stores, you can use the following methods. See the `KeyValueStore` class's https://docs.apify.com/sdk/js/reference/class/KeyValueStore for the full list.


```
import { Actor } from 'apify';

await Actor.init();
// ...

// Get the default input
const input = await Actor.getInput();

// Open a named key-value store
const exampleStore = await Actor.openKeyValueStore('my-store');

// Read a record in the exampleStore storage
const value = await exampleStore.getValue('some-key');

// Write a record to exampleStore
await exampleStore.setValue('some-key', { foo: 'bar' });

// Delete a record from exampleStore
await exampleStore.setValue('some-key', null);

// ...
await Actor.exit();
```


> Note that JSON is automatically parsed to a JavaScript object, text data returned as a string and other data is returned as binary buffer.


```
import { Actor } from 'apify';

await Actor.init();
// ...

// Get input of your Actor
const input = await Actor.getInput();
const value = await Actor.getValue('my-key');

// ...
await Actor.setValue('OUTPUT', imageBuffer, { contentType: 'image/jpeg' });

// ...
await Actor.exit();
```


The `Actor.getInput()` method is not only a shortcut to `Actor.getValue('INPUT')`; it is also compatible with https://docs.apify.com/platform/actors/development/programming-interface/metamorph.md. This is because a metamorphed Actor run's input is stored in the *INPUT-METAMORPH-1* key instead of *INPUT*, which hosts the original input.

Check out the https://docs.apify.com/sdk/js/docs/guides/result-storage#key-value-store and the `KeyValueStore` class's https://docs.apify.com/sdk/js/reference/class/KeyValueStore for details on managing your key-value stores with the JavaScript SDK.

#### Python SDK

For Python https://docs.apify.com/platform/actors.md, the https://docs.apify.com/sdk/python/docs/concepts/storages#working-with-key-value-stores is essential. The key-value store is represented by a https://docs.apify.com/sdk/python/reference/class/KeyValueStore class. You can use this class to specify whether your data is stored locally or in the Apify cloud. For further data manipulation it offers https://docs.apify.com/sdk/python/reference/class/KeyValueStore#get_value and https://docs.apify.com/sdk/python/reference/class/KeyValueStore#set_value methods to retrieve and assign values, respectively.

Every Actor run is linked to a default key-value store that is automatically created for that specific run. If you're running your Actors and opt to store data locally, you can easily supply the https://docs.apify.com/platform/actors/running/input-and-output.md by placing an *INPUT.json* file in the corresponding directory of the default key-value store. This method ensures that you Actor has all the necessary data readily available for its execution.

You can find *INPUT.json* and other key-value store files in the location below.


```
{APIFY_LOCAL_STORAGE_DIR}/key_value_stores/{STORE_ID}/{KEY}.{EXT}
```


The default key-value store's ID is *default*. The {KEY} is the record's *key* and {EXT} corresponds to the record value's MIME content type.

To manage your key-value stores, you can use the following methods. See the `KeyValueStore` class https://docs.apify.com/sdk/python/reference/class/KeyValueStore for the full list.


```
from apify import Actor
from apify.storages import KeyValueStore

async def main():
    async with Actor:
        # Open a named key-value store
        example_store: KeyValueStore = await Actor.open_key_value_store(name='my-store')

        # Read a record in the example_store storage
        value = await example_store.get_value('some-key')

        # Write a record to example_store
        await example_store.set_value('some-key', {'foo': 'bar'})

        # Delete a record from example_store
        await example_store.set_value('some-key', None)
```


> Note that JSON is automatically parsed to a Python dictionary, text data returned as a string and other data is returned as binary buffer.


```
from apify import Actor

async def main():
    async with Actor:
        value = await Actor.get_value('my-key')
        # ...
        image_buffer = ...  # Get image data
        await Actor.set_value(key='OUTPUT', value=image_buffer, content_type='image/jpeg')
```


The `Actor.get_input()` method is not only a shortcut to `Actor.get_value('INPUT')`; it is also compatible with https://docs.apify.com/platform/actors/development/programming-interface/metamorph.md. This is because a metamorphed Actor run's input is stored in the *INPUT-METAMORPH-1* key instead of *INPUT*, which hosts the original input.

Check out the https://docs.apify.com/sdk/python/docs/concepts/storages#working-with-key-value-stores and the `KeyValueStore` class's https://docs.apify.com/sdk/python/reference/class/KeyValueStore for details on managing your key-value stores with the Python SDK.

## Compression

Previously, when using the https://docs.apify.com/api/v2/key-value-store-record-put.md endpoint, every record was automatically compressed with Gzip before being uploaded. However, this process has been updated. *Now, records are stored exactly as you upload them.* This change means that it is up to you whether the record is stored compressed or uncompressed.

You can compress a record and use the https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding to let our platform know which compression it uses. We recommend compressing large key-value records to save storage space and network traffic.

*Using the https://docs.apify.com/sdk/js/reference/class/KeyValueStore#setValue or our https://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient#setRecord automatically compresses your files.* We advise utilizing the JavaScript API client for data compression prior to server upload and decompression upon retrieval, minimizing storage costs.

## Sharing

You can grant https://docs.apify.com/platform/collaboration.md to your key-value store through the **Share** button under the **Actions** menu. For more details check the https://docs.apify.com/platform/collaboration/list-of-permissions.md.

You can also share key-value stores by link using their ID or name, depending on your account or resource-level general access setting. Learn how link-based access works in https://docs.apify.com/platform/collaboration/general-resource-access.md.

For one-off sharing of specific records when access is restricted, you can generate time-limited pre-signed URLs. See https://docs.apify.com/platform/collaboration/general-resource-access.md#pre-signed-urls.

### Sharing key-value stores between runs

You can access a key-value store from any https://docs.apify.com/platform/actors.md or https://docs.apify.com/platform/actors/running/tasks.md run as long as you know its *name* or *ID*.

To access a key-value store from another run using the https://docs.apify.com/sdk.md, open it using the same method as you would do with any other store.

* JavaScript
* Python


```
import { Actor } from 'apify';

await Actor.init();

const otherStore = await Actor.openKeyValueStore('old-store');
// ...

await Actor.exit();
```



```
from apify import Actor

async def main():
    async with Actor:
        other_store = await Actor.open_key_value_store(name='old-store')
        # ...
```


In the https://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient as well as in https://docs.apify.com/api/client/python/reference/class/KeyValueStoreClient, you can access a store using its client. Once you've opened a store, read and manage its contents like you would do with a key-value store from your current run.

* JavaScript
* Python


```
const otherStoreClient = apifyClient.keyValueStore('jane-doe/old-store');
```



```
other_store_client = apify_client.key_value_store('jane-doe/old-store')
```


The same applies for the  - you can use  as you would normally do.

Check out the https://docs.apify.com/platform/storage/usage.md#sharing-storages-between-runs for details on sharing storages between runs.

## Data consistency

Key-value storage uses the https://aws.amazon.com/s3/ service. According to the https://aws.amazon.com/s3/consistency/, it provides *strong read-after-write* consistency.

## Limits

* The maximum length for key of key-value store is 63 characters.
