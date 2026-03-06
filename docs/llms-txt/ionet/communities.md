# Source: https://io.net/docs/reference/rag/graphs/communities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

## Community management endpoints

Communities are groups of entities that are connected to each other. They can be generated using a clustering and summarization algorithm implemented by R2R.

To automatically generate communities from entities and relationships present in the graph, you can use the following endpoint:

| Method | Endpoint                                                                                                 | Description            |
| ------ | -------------------------------------------------------------------------------------------------------- | ---------------------- |
| GET    | [/graphs/\{collection\_id}/communities/build](/reference/rag/graphs/communities/build-graph-communities) | Create a new community |

Once communities are generated, you can manage them using the following endpoints. You can also add your own communities to the graph.

| Method | Endpoint                                                                                                       | Description                   |
| ------ | -------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| GET    | [graphs/\{collection\_id}/communities](/reference/rag/graphs/communities/list-communities)                     | Get relationships for a graph |
| POST   | [/graphs/\{collection\_id}/communities/\{community\_id}](/reference/rag/graphs/communities/)                   | Retrieve a community          |
| POST   | [/graphs/\{collection\_id}/communities/\{community\_id}](/reference/rag/graphs/communities/update-a-community) | Update community              |
| DELETE | [graphs/\{collection\_id}/communities/\{community\_id}](/reference/rag/graphs/communities/delete-a-community)  | Delete community              |
