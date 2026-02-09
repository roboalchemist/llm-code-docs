# Source: https://docs.apify.com/api/client/python/reference/class/DatasetClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/DatasetClient.md

# DatasetClient<!-- --> \<Data>

Client for managing a specific Dataset.

Datasets store structured data results from Actor runs. This client provides methods to push items, list and retrieve items, download items in various formats (JSON, CSV, Excel, etc.), and manage the dataset.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const datasetClient = client.dataset('my-dataset-id');

  // Push items to the dataset
  await datasetClient.pushItems([
    { url: 'https://example.com', title: 'Example' },
    { url: 'https://test.com', title: 'Test' }
  ]);

  // List all items
  const { items } = await datasetClient.listItems();

  // Download items as CSV
  const buffer = await datasetClient.downloadItems('csv');
  ```

* **@see**

  <https://docs.apify.com/platform/storage/dataset>

### Hierarchy

* ResourceClient
  * *DatasetClient*

## Index[**](#Index)

### Properties

* [**apifyClient](#apifyClient)
* [**baseUrl](#baseUrl)
* [**httpClient](#httpClient)
* [**id](#id)
* [**params](#params)
* [**publicBaseUrl](#publicBaseUrl)
* [**resourcePath](#resourcePath)
* [**safeId](#safeId)
* [**url](#url)

### Methods

* [**createItemsPublicUrl](#createItemsPublicUrl)
* [**delete](#delete)
* [**downloadItems](#downloadItems)
* [**get](#get)
* [**getStatistics](#getStatistics)
* [**listItems](#listItems)
* [**pushItems](#pushItems)
* [**update](#update)

## Properties<!-- -->[**](#Properties)

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L36)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L28)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L38)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L24)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L40)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L30)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L32)inheritedresourcePath

**resourcePath: string

Inherited from ResourceClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L26)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L34)inheritedurl

**url: string

Inherited from ResourceClient.url

## Methods<!-- -->[**](#Methods)

### [**](#createItemsPublicUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L356)createItemsPublicUrl

* ****createItemsPublicUrl**(options): Promise\<string>

- Generates a public URL for accessing dataset items.

  If the client has permission to access the dataset's URL signing key, the URL will include a cryptographic signature allowing access without authentication. This is useful for sharing dataset results with external services or users.

  * **@example**

    ```
    // Create a URL that expires in 1 hour with specific fields
    const url = await client.dataset('my-dataset').createItemsPublicUrl({
      expiresInSecs: 3600,
      fields: ['url', 'title'],
      limit: 100
    });
    console.log(`Share this URL: ${url}`);

    // Create a permanent public URL for clean items only
    const url = await client.dataset('my-dataset').createItemsPublicUrl({
      clean: true,
      skipEmpty: true
    });
    ```

  ***

  #### Parameters

  * ##### options: [DatasetClientCreateItemsUrlOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientCreateItemsUrlOptions.md) = <!-- -->{}

    URL generation options (extends all options from listItems)

  #### Returns Promise\<string>

  A public URL string for accessing the dataset items

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L88)delete

* ****delete**(): Promise\<void>

- Deletes the dataset.

  * **@see**

    <https://docs.apify.com/api/v2/dataset-delete>

  ***

  #### Returns Promise\<void>

### [**](#downloadItems)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L212)downloadItems

* ****downloadItems**(format, options): Promise\<Buffer>

- Downloads dataset items in a specific format.

  Unlike listItems which returns a [PaginatedList](https://docs.apify.com/api/client/js/api/client/js/reference/interface/PaginatedList.md) with an array of individual dataset items, this method returns the items serialized to the provided format (JSON, CSV, Excel, etc.) as a Buffer. Useful for exporting data for further processing.

  * **@see**

    <https://docs.apify.com/api/v2/dataset-items-get>

  * **@example**

    ```
    // Download as CSV with BOM for Excel compatibility
    const csvBuffer = await client.dataset('my-dataset').downloadItems('csv', { bom: true });
    require('fs').writeFileSync('output.csv', csvBuffer);

    // Download as Excel with custom options
    const xlsxBuffer = await client.dataset('my-dataset').downloadItems('xlsx', {
      fields: ['url', 'title', 'price'],
      skipEmpty: true,
      limit: 1000
    });

    // Download as XML with custom element names
    const xmlBuffer = await client.dataset('my-dataset').downloadItems('xml', {
      xmlRoot: 'products',
      xmlRow: 'product'
    });
    ```

  ***

  #### Parameters

  * ##### format: [DownloadItemsFormat](https://docs.apify.com/api/client/js/api/client/js/reference/enum/DownloadItemsFormat.md)

    Output format: `'json'`, `'jsonl'`, `'csv'`, `'xlsx'`, `'xml'`, `'rss'`, or `'html'`

  * ##### options: [DatasetClientDownloadItemsOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientDownloadItemsOptions.md) = <!-- -->{}

    Download and formatting options (extends all options from listItems)

  #### Returns Promise\<Buffer>

  Buffer containing the serialized data in the specified format

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L66)get

* ****get**(): Promise\<undefined | [Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

- Gets the dataset object from the Apify API.

  * **@see**

    <https://docs.apify.com/api/v2/dataset-get>

  ***

  #### Returns Promise\<undefined | [Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

  The Dataset object, or `undefined` if it does not exist

### [**](#getStatistics)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L309)getStatistics

* ****getStatistics**(): Promise\<undefined | [DatasetStatistics](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetStatistics.md)>

- Gets statistical information about the dataset.

  Returns statistics for each field in the dataset, including information about data types, null counts, and value ranges.

  * **@see**

    <https://docs.apify.com/api/v2/dataset-statistics-get>

  ***

  #### Returns Promise\<undefined | [DatasetStatistics](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetStatistics.md)>

  Dataset statistics, or `undefined` if not available

### [**](#listItems)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L136)listItems

* ****listItems**(options): PaginatedIterator\<Data>

- Lists items in the dataset.

  Returns a paginated list of dataset items. You can use pagination parameters to retrieve specific subsets of items, and various filtering and formatting options to customize the output.

  * **@see**

    <https://docs.apify.com/api/v2/dataset-items-get>

  * **@example**

    ```
    // Get first 100 items
    const { items, total } = await client.dataset('my-dataset').listItems({ limit: 100 });
    console.log(`Retrieved ${items.length} of ${total} total items`);

    // Get items with specific fields only
    const { items } = await client.dataset('my-dataset').listItems({
      fields: ['url', 'title'],
      skipEmpty: true,
      limit: 50
    });

    // Get items in descending order with pagination
    const { items } = await client.dataset('my-dataset').listItems({
      desc: true,
      offset: 100,
      limit: 50
    });
    ```

  ***

  #### Parameters

  * ##### options: [DatasetClientListItemOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientListItemOptions.md) = <!-- -->{}

    Options for listing items

  #### Returns PaginatedIterator\<Data>

  A paginated list with `items`, `total` count, `offset`, `count`, and `limit`

### [**](#pushItems)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L284)pushItems

* ****pushItems**(items): Promise\<void>

- Stores one or more items into the dataset.

  Items can be objects, strings, or arrays thereof. Each item will be stored as a separate record in the dataset. Objects are automatically serialized to JSON. If you provide an array, all items will be stored in order. This method is idempotent - calling it multiple times with the same data will not create duplicates, but will append items each time.

  * **@see**

    <https://docs.apify.com/api/v2/dataset-items-post>

  * **@example**

    ```
    // Store a single object
    await client.dataset('my-dataset').pushItems({
      url: 'https://example.com',
      title: 'Example Page',
      extractedAt: new Date()
    });

    // Store multiple items at once
    await client.dataset('my-dataset').pushItems([
      { url: 'https://example.com', title: 'Example' },
      { url: 'https://test.com', title: 'Test' },
      { url: 'https://demo.com', title: 'Demo' }
    ]);

    // Store string items
    await client.dataset('my-dataset').pushItems(['item1', 'item2', 'item3']);
    ```

  ***

  #### Parameters

  * ##### items: string | Data | string\[] | Data\[]

    A single item (object or string) or an array of items to store. Objects are automatically stringified to JSON. Strings are stored as-is.

  #### Returns Promise\<void>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L77)update

* ****update**(newFields): Promise<[Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

- Updates the dataset with specified fields.

  * **@see**

    <https://docs.apify.com/api/v2/dataset-put>

  ***

  #### Parameters

  * ##### newFields: [DatasetClientUpdateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientUpdateOptions.md)

    Fields to update in the dataset

  #### Returns Promise<[Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

  The updated Dataset object
