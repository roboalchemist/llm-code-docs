# Source: https://docs.apify.com/sdk/python/reference/class/ActorDatasetPushPipeline.md

# ActorDatasetPushPipeline<!-- -->

A Scrapy pipeline for pushing items to an Actor's default dataset.

This pipeline is designed to be enabled only when the Scrapy project is run as an Actor.

## Index[**](#Index)

### Methods

* [**process\_item](https://docs.apify.com/sdk/python/sdk/python/reference/class/ActorDatasetPushPipeline.md#process_item)

## Methods<!-- -->[**](#Methods)

### [**](#process_item)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/pipelines/actor_dataset_push.py#L22)process\_item

* **async **process\_item**(item, spider): Item

- Pushes the provided Scrapy item to the Actor's default dataset.

  ***

  #### Parameters

  * ##### item: Item
  * ##### spider: Spider

  #### Returns Item
