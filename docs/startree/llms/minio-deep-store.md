# Source: https://docs.startree.ai/recipes/minio-deep-store.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Using MinIO as Deep Store for an Offline Table

In this recipe we'll learn how to use [MinIO](https://docs.min.io/docs/aws-cli-with-minio) as a Pinot deep store.

To understand how this recipe processes data, examine the commands executed in the Makefile.

| Pinot Version | 1.1.0                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------- |
| Code          | [startreedata/pinot-recipes/minio](https://github.com/startreedata/pinot-recipes//tree/main/recipes/minio) |

## Prerequisites

To follow the code examples in this guide, do the following:

* [Install Docker](https://docs.docker.com/get-docker/).
* Download recipes

## Makefile

Clone this repository and navigate to this recipe:

```bash  theme={null}
make recipe
```

## Validate

Check that minio has the segment in the deep store. You can also log into the minio console and check. [http://localhost:9001/browser/deepstore](http://localhost:9001/browser/deepstore).

```
docker exec minio mc ls myminio/deepstore/transcript
```

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
