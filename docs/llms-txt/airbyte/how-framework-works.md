# Source: https://docs.airbyte.com/platform/connector-development/config-based/advanced-topics/how-framework-works.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/config-based/advanced-topics/how-framework-works.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/config-based/advanced-topics/how-framework-works.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/config-based/advanced-topics/how-framework-works.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/config-based/advanced-topics/how-framework-works.md

# How the Framework Works

Copy Page

1. Given the connection config and an optional stream state, the `PartitionRouter` computes the partitions that should be routed to read data.

2. Iterate over all the partitions defined by the stream's partition router.

3. For each partition,

   <!-- -->

   1. Submit a request to the partner API as defined by the requester
   2. Select the records from the response
   3. Repeat for as long as the paginator points to a next page

![connector-flow](/assets/images/connector-flow-8acd0f3ab6dcdc3b80bfbecc56f7ed11.png)
