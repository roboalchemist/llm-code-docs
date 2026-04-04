# Source: https://docs.startree.ai/recipes/fixed-hostname.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# How to fix host names

In this recipe, we'll learn how to fix the host name of components in an Apache Pinot cluster.

| Pinot Version | 1.0.0                                                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/fixed-hostname](https://github.com/startreedata/pinot-recipes/tree/main/recipes/fixed-hostname) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally.

## Navigate to recipe

1. If you haven't already, download recipes.
2. In terminal, go to the recipe by running the following command:

```bash  theme={null}
cd pinot-recipes/recipes/fixed-hostname
```

## Launch Pinot Cluster

You can spin up a Pinot Cluster by running the following command:

```bash  theme={null}
docker-compose up
```

This command will run a single instance of the Pinot Controller, Pinot Server, Pinot Broker, Pinot Minion, and Zookeeper.
You can find the [docker-compose.yml](https://github.com/startreedata/pinot-recipes/blob/main/recipes/fixed-hostname/docker-compose.yml) file on GitHub.

Navigate to the [Pinot UI](http://localhost:9000) and you should see the following:

<img src="https://mintcdn.com/startree/SwAzqeuInnw8J52u/recipes/images/pinot-ui-fixed-hosts.png?fit=max&auto=format&n=SwAzqeuInnw8J52u&q=85&s=53d8a850b560179d90c14759a3978b8d" alt="Pinot UI showing fixed host names" className="mx-auto" style={{ width:"76%" }} width="856" height="971" data-path="recipes/images/pinot-ui-fixed-hosts.png" />

Fixed hostnames

## Configuring fixed host names

Let's have a look at the [Docker Compose file](https://github.com/startreedata/pinot-recipes/blob/main/recipes/fixed-hostname/docker-compose.yml) to see how we did this.
The commands to start the container for each component are described below:

**Controller**

```yml  theme={null}
StartController -zkAddress zookeeper-fixedhost:2181 -controllerHost pinot-controller-fixedhost
```

**Broker**

```yml  theme={null}
StartBroker -zkAddress zookeeper-fixedhost:2181  -brokerHost pinot-broker-fixedhost
```

**Server**

```yml  theme={null}
StartServer -zkAddress zookeeper-fixedhost:2181 -serverHost pinot-server-fixedhost
```

**Minion**

```yml  theme={null}
StartMinion -zkAddress zookeeper-fixedhost:2181 -minionHost pinot-minion-fixedhost
```

Built with [Mintlify](https://mintlify.com).
