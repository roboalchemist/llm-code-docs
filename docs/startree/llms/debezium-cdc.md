# Source: https://docs.startree.ai/recipes/debezium-cdc.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Ingest CDC Data using PostgreSQL, Kafka, and Debezium

This recipe downloads Postgres change data capture (CDC) about `dvdrentals` and connects Kafka to Debezium. CDC data is written to Kafka, and then consumed by Apache Pinot.

To understand how this recipe processes data, examine the commands executed in the Makefile.

| Pinot Version | 1.0.0                                                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/debezium-cdc](https://github.com/startreedata/pinot-recipes/tree/main/recipes/debezium-cdc) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In the terminal, navigate to this recipe's directory:

```bash  theme={null}
cd pinot-recipes/recipes/debezium-cdc
```

1. Spin up a Pinot cluster using the Makefile, which uses Docker compose:

```bash  theme={null}
make recipe
```

1. Navigate to [localhost:9000/#/query](http://localhost:9000/#/query) to see the data in Apache Pinot.

## Clean up

```bash  theme={null}
make clean
```

## Troubleshooting

To clean up old Docker installations that may be interfering with your testing of this recipe, run the following command:

```bash  theme={null}
docker system prune
```

Built with [Mintlify](https://mintlify.com).
