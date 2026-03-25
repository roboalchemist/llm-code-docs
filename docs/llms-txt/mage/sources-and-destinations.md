# Source: https://docs.mage.ai/contributing/backend/streaming/sources-and-destinations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Contributing

This doc talks about how to add a new source or destination to the streaming pipeline.

## Prerequisites

Follow this [doc](/contributing/overview) to set up the development environment for Mage.

## Add a new source

Example PR for adding a source: [https://github.com/mage-ai/mage-ai/pull/1953](https://github.com/mage-ai/mage-ai/pull/1953)

* Add the new source type to [mage\_ai/streaming/constants.py](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/streaming/constants.py).
* Add the source file to the folder [https://github.com/mage-ai/mage-ai/tree/master/mage\_ai/streaming/sources](https://github.com/mage-ai/mage-ai/tree/master/mage_ai/streaming/sources)
  * Define the source class which inherits from the `BaseSource`.
  * Define the source config class.
  * Implement the methods:
    * `init_client`: Initialize the client used to connect to the source.
    * `batch_read`: Batch read messages from the source and use `handler` method to process the messages.
* Add the new source to the [SourceFactory](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/streaming/sources/source_factory.py).
* Add a template file with example config to the folder: [https://github.com/mage-ai/mage-ai/tree/master/mage\_ai/data\_preparation/templates/data\_loaders/streaming](https://github.com/mage-ai/mage-ai/tree/master/mage_ai/data_preparation/templates/data_loaders/streaming)
* Add new source type to the frontend code.
  * [https://github.com/mage-ai/mage-ai/blob/master/mage\_ai/frontend/components/PipelineDetail/AddNewBlocks/utils.tsx#L31](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/frontend/components/PipelineDetail/AddNewBlocks/utils.tsx#L31)
  * [https://github.com/mage-ai/mage-ai/blob/master/mage\_ai/frontend/interfaces/DataSourceType.ts#L3](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/frontend/interfaces/DataSourceType.ts#L3)
  * [https://github.com/mage-ai/mage-ai/blob/master/mage\_ai/frontend/interfaces/DataSourceType.ts#L22](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/frontend/interfaces/DataSourceType.ts#L22)
* Add unit tests: [https://github.com/mage-ai/mage-ai/tree/master/mage\_ai/tests/streaming/sources](https://github.com/mage-ai/mage-ai/tree/master/mage_ai/tests/streaming/sources)
* Add doc: [https://github.com/mage-ai/mage-ai/tree/master/docs/guides/streaming/sources](https://github.com/mage-ai/mage-ai/tree/master/docs/guides/streaming/sources)

***

## Add a new destination (sink)

Example PR for adding a sink: [https://github.com/mage-ai/mage-ai/pull/2121](https://github.com/mage-ai/mage-ai/pull/2121)

* Add the new sink type to [mage\_ai/streaming/constants.py](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/streaming/constants.py).
* Add the sink file to the folder [https://github.com/mage-ai/mage-ai/tree/master/mage\_ai/streaming/sinks](https://github.com/mage-ai/mage-ai/tree/master/mage_ai/streaming/sinks)
  * Define the sink class which inherits from the `BaseSink`.
  * Define the sink config class.
  * Implement the methods:
    * `init_client`: Initialize the client used to connect to the destination.
    * `batch_write`: Batch write messages to destination.
* Add the new sink to the [SinkFactory](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/streaming/sinks/sink_factory.py).
* Add a template file with example config to the folder: [https://github.com/mage-ai/mage-ai/tree/master/mage\_ai/data\_preparation/templates/data\_exporters/streaming](https://github.com/mage-ai/mage-ai/tree/master/mage_ai/data_preparation/templates/data_exporters/streaming)
* Add new source type to the frontend code.
  * [https://github.com/mage-ai/mage-ai/blob/master/mage\_ai/frontend/components/PipelineDetail/AddNewBlocks/utils.tsx#L37](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/frontend/components/PipelineDetail/AddNewBlocks/utils.tsx#L37)
  * [https://github.com/mage-ai/mage-ai/blob/master/mage\_ai/frontend/interfaces/DataSourceType.ts#L3](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/frontend/interfaces/DataSourceType.ts#L3)
  * [https://github.com/mage-ai/mage-ai/blob/master/mage\_ai/frontend/interfaces/DataSourceType.ts#L22](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/frontend/interfaces/DataSourceType.ts#L22)
* Add unit tests: [https://github.com/mage-ai/mage-ai/tree/master/mage\_ai/tests/streaming/sinks](https://github.com/mage-ai/mage-ai/tree/master/mage_ai/tests/streaming/sinks)
* Add doc: [https://github.com/mage-ai/mage-ai/tree/master/docs/guides/streaming/destinations](https://github.com/mage-ai/mage-ai/tree/master/docs/guides/streaming/destinations)


Built with [Mintlify](https://mintlify.com).