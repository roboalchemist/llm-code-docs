# Source: https://pipedream.com/docs/workflows/data-management/data-stores.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Stores

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/0WMcAnDF7FA" title="Data store Basics" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

**Data stores** are Pipedream’s built-in key-value store.

Data stores are useful for:

* Storing and retrieving data at a specific key
* Setting automatic expiration times for temporary data (TTL)
* Counting or summing values over time
* Retrieving JSON-serializable data across workflow executions
* Caching and rate limiting
* And any other case where you’d use a key-value store

You can connect to the same data store across workflows, so they’re also great for sharing state across different services.

You can use pre-built, no-code actions to store, update, and clear data, or interact with data stores programmatically in [Node.js](/workflows/building-workflows/code/nodejs/using-data-stores/) or [Python](/workflows/building-workflows/code/python/using-data-stores/).

## Using pre-built Data Store actions

Pipedream provides several pre-built actions to set, get, delete, and perform other operations with data stores.

### Inserting data

To insert data into a data store:

1. Add a new step to your workflow.
2. Search for the **Data Stores** app and select it.
3. Select the **Add or update a single record** pre-built action.

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d68ed100-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=120aded5fef4a4a05988d5a7dd157306" width="1344" height="784" data-path="images/d68ed100-image.png" />
</Frame>

Configure the action:

1. **Select or create a Data Store** — create a new data store or choose an existing data store.
2. **Key** - the unique ID for this data that you’ll use for lookup later
3. **Value** - The data to store at the specified `key`
4. **Time to Live (TTL)** - (Optional) The number of seconds until this record expires and is automatically deleted. Leave blank for records that should not expire.

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/c64ce2f1-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=8a0fa4762e4ba6efc0327adc3b253eaf" width="776" height="571" data-path="images/c64ce2f1-image.png" />
</Frame>

For example, to store the timestamp when the workflow was initially triggered, set the **Key** to **Triggered At** and the **Value** to `{{steps.trigger.context.ts}}`.

The **Key** must evaluate to a string. You can pass a static string, reference [exports](/workflows/#step-exports) from a previous step, or use [any valid expression](/workflows/building-workflows/using-props/#entering-expressions).

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/cb19db97-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=24bfb91572a1898cc87f078d4175b85b" width="771" height="573" data-path="images/cb19db97-image.png" />
</Frame>

<Note>
  Need to store multiple records in one action? Use the **Add or update multiple records** action instead.
</Note>

### Retrieving Data

The **Get record** action will retrieve the latest value of a data point in one of your data stores.

1. Add a new step to your workflow.
2. Search for the **Data Stores** app and select it.
3. Select the **Add or update a single record** pre-built action.

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/a15f51a4-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=63e58db5c44e0d596e548937c35a7a51" width="1354" height="804" data-path="images/a15f51a4-image.png" />
</Frame>

Configure the action:

1. **Select or create a Data Store** — create a new data store or choose an existing data store.
2. **Key** - the unique ID for this data that you’ll use for lookup later
3. **Create new record if key is not found** - if the specified key isn’t found, you can create a new record
4. **Value** - The data to store at the specified `key`

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/2deed27d-image.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=2af014c26554d219b11601a44461aee1" width="778" height="725" data-path="images/2deed27d-image.png" />
</Frame>

### Setting or updating record expiration (TTL)

You can set automatic expiration times for records using the **Update record expiration** action:

1. Add a new step to your workflow.
2. Search for the **Data Stores** app and select it.
3. Select the **Update record expiration** pre-built action.

Configure the action:

1. **Select a Data Store** - select the data store containing the record to modify
2. **Key** - the key for the record you want to update the expiration for
3. **Expiration Type** - choose from preset expiration times (1 hour, 1 day, 1 week, etc.) or select “Custom value” to enter a specific time in seconds
4. **Custom TTL (seconds)** - (only if “Custom value” is selected) enter the number of seconds until the record expires

To remove expiration from a record, select “No expiration” as the expiration type.

### Deleting Data

To delete a single record from your data store, use the **Delete a single record** action in a step:

<Frame>
  <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/e8479cab-image.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=9f9f16ef4252a3e09598ac107aed4ee6" width="1340" height="795" data-path="images/e8479cab-image.png" />
</Frame>

Then configure the action:

1. **Select a Data Store** - select the data store that contains the record to be deleted
2. **Key** - the key that identifies the individual record

For example, you can delete the data at the **Triggered At** key that we’ve created in the steps above:

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/abb2f2e7-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=40b0ddfe513bfadbc79b9ff11eace941" width="771" height="452" data-path="images/abb2f2e7-image.png" />
</Frame>

Deleting a record does not delete the entire data store. [To delete an entire data store, use the Pipedream Data Stores Dashboard](/workflows/data-management/data-stores/#deleting-data-stores).

## Managing data stores

You can view the contents of your data stores at any time in the [Pipedream Data Stores dashboard](https://pipedream.com/data-stores/). You can also add, edit, or delete data store records manually from this view.

### Editing data store values manually

1. Select the data store
2. Click the pencil icon on the far right of the record you want to edit. This will open a text box that will allow you to edit the contents of the value. When you’re finished with your edits, save by clicking the checkmark icon.

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/a070776e-CleanShot_2022-03-23_at_15.24.49_err0nt.gif?s=83d66102f47938ae8860caee52d53c95" width="184" height="110" data-path="images/a070776e-CleanShot_2022-03-23_at_15.24.49_err0nt.gif" />
</Frame>

### Deleting data stores

You can delete a data store from this dashboard as well. On the far right in the data store row, click the trash can icon.

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/74ff6d25-CleanShot_2022-03-23_at_15.29.00_qtvdcz.gif?s=1f318a0c91f925acc3b18edb3741ea24" width="174" height="106" data-path="images/74ff6d25-CleanShot_2022-03-23_at_15.29.00_qtvdcz.gif" />
</Frame>

**Deleting a data store is irreversible**.

<Warning>
  If the **Delete** option is greyed out and unclickable, you have workflows using the data store in a step. Click the **>** to the left of the data store’s name to expand the linked workflows.

  <Frame>
    <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/843184a5-Screenshot_2023-12-10_at_2.52.21_PM_tw2qwo.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=4893ef8ddde6b3047f118a18434c83a6" width="1070" height="358" data-path="images/843184a5-Screenshot_2023-12-10_at_2.52.21_PM_tw2qwo.png" />
  </Frame>

  Then remove the data store from any linked steps.
</Warning>

## Using data stores in code steps

Refer to the [Node.js](/workflows/building-workflows/code/nodejs/using-data-stores/) and [Python](/workflows/building-workflows/code/python/using-data-stores/) data store docs to learn how to use data stores in code steps. You can get, set, delete and perform any other data store operations in code. You cannot use data stores in [Bash](/workflows/building-workflows/code/bash/) or [Go](/workflows/building-workflows/code/go/) code steps.

## Compression

Data saved in data stores is [Brotli-compressed](https://github.com/google/brotli), minimizing storage. The total compression ratio depends on the data being compressed. To test this on your own data, run it through a package that supports Brotli compression and measure the size of the data before and after.

## Data store limits

Depending on your plan, Pipedream sets limits on:

1. The total number of data stores
2. The total number of keys across all data stores
3. The total storage used across all data stores, [after compression](/workflows/data-management/data-stores/#compression)

You’ll find your workspace’s limits in the **Data Stores** section of usage dashboard in the bottom-left of [https://pipedream.com](https://pipedream.com).

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/54ca2228-image_ryjbrh.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=9ebcd956b1be14fd3c1e503de18618f5" width="410" height="572" data-path="images/54ca2228-image_ryjbrh.png" />
</Frame>

## Atomic operations

Data store operations are not atomic or transactional, which can lead to race conditions. To ensure atomic operations, be sure to limit access to a data store key to a [single workflow with a single worker](/workflows/building-workflows/settings/concurrency-and-throttling/) or use a service that supports atomic operations from among our [integrated apps](https://pipedream.com/apps).

## Supported data types

Data stores can hold any JSON-serializable data within the storage limits. This includes data types including:

* Strings
* Objects
* Arrays
* Dates
* Integers
* Floats

But you cannot serialize functions, classes, sets, maps, or other complex objects.

## Exporting data to an external service

In order to stay within the [data store limits](/workflows/data-management/data-stores/#data-store-limits), you may need to export the data in your data store to an external service.

The following Node.js example action will export the data in chunks via an HTTP POST request. You may need to adapt the code to your needs. Click on [this link](https://pipedream.com/new?h=tch_egfAMv) to create a copy of the workflow in your workspace.

<Note>
  If the data contained in each key is large, consider lowering the number of `chunkSize`.
</Note>

* Adjust your [workflow memory and timeout settings](/workflows/building-workflows/settings/) according to the size of the data in your data store. Set the memory at 512 MB and timeout to 60 seconds and adjust higher if needed.

* Monitor the exports of this step after each execution for any potential errors preventing a full export. Run the step as many times as needed until all your data is exported.

<Warning>
  This action deletes the keys that were successfully exported. It is advisable to first run a test without deleting the keys. In case of any unforeseen errors, your data will still be safe.
</Warning>

```javascript  theme={null}
import { axios } from "@pipedream/platform";
 
export default defineComponent({
  props: {
    dataStore: {
      type: "data_store",
    },
    chunkSize: {
      type: "integer",
      label: "Chunk Size",
      description: "The number of items to export in one request",
      default: 100,
    },
    shouldDeleteKeys: {
      type: "boolean",
      label: "Delete keys after export",
      description: "Whether the data store keys will be deleted after export",
      default: true,
    },
  },
  methods: {
    async *chunkAsyncIterator(asyncIterator, chunkSize) {
      let chunk = [];
 
      for await (const item of asyncIterator) {
        chunk.push(item);
 
        if (chunk.length === chunkSize) {
          yield chunk;
          chunk = [];
        }
      }
 
      if (chunk.length > 0) {
        yield chunk;
      }
    },
  },
  async run({ steps, $ }) {
    const iterator = this.chunkAsyncIterator(this.dataStore, this.chunkSize);
    for await (const chunk of iterator) {
      try {
        // export data to external service
        await axios($, {
          url: "https://external_service.com",
          method: "POST",
          data: chunk,
          // may need to add authentication
        });
 
        // delete exported keys and values
        if (this.shouldDeleteKeys) {
          await Promise.all(chunk.map(([key]) => this.dataStore.delete(key)));
        }
 
        console.log(
          `number of remaining keys: ${(await this.dataStore.keys()).length}`
        );
      } catch (e) {
        // an error occurred, don't delete keys
        console.log(`error exporting data: ${e}`);
      }
    }
  },
});
```

Built with [Mintlify](https://mintlify.com).
