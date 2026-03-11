# Source: https://docs.startree.ai/recipes/pulsar.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Ingest from Apache Pulsar

> In this Apache Pinot Recipe, we'll learn how to ingest data from Apache Pulsar.

Apache Pulsar is a cloud-native, distributed messaging and streaming platform originally created at Yahoo!

| Pinot Version | 1.1.0                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/pulsar](https://github.com/startreedata/pinot-recipes/tree/main/recipes/pulsar) |

## Prerequisites

To follow the code examples in this guide, you must [install Docker](https://docs.docker.com/get-docker/) locally and download recipes.

Clone this repository and navigate to this recipe:

```bash  theme={null}
git clone git@github.com:startreedata/pinot-recipes.git
cd pinot-recipes/recipes/ingest-json-files
```

## Makefile

```bash  theme={null}
make recipe
```

To produce data into Pulsar, use the Python code below.

```python  theme={null}
import pulsar
import json
import time
import random
import uuid

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('events')

  message = {
    "ts": int(time.time() * 1000.0),
    "uuid": str(uuid.uuid4()).replace("-", ""),
    "count": random.randint(0, 1000)
}
payload = json.dumps(message, ensure_ascii=False).encode('utf-8')
producer.send(payload)
client.close()
```

## See the data

Navigate to [localhost:9000/#/query](http://localhost:9000/#/query) to see the data in Apache Pinot.

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
