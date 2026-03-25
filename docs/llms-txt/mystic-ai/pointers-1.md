# Source: https://docs.mystic.ai/docs/pointers-1.md

# Pointers

Instead of referring to pipelines by ID, you can also use pointers. If you're familiar with Docker tags, this works in a similar way. The pointer "points" to the pipeline, so to speak, and you can use this pointer to specify a pipeline, rather than the pipeline ID.

There are many uses for pointers. A common one is if you have several versions of a pipeline but you want to signify which one is the most stable version. This then allows you to update the pointer to point to a more recent version in the future, without having to rely on using pipeline IDs.

## Versioned pointers

Pipelines are automatically versioned under the hood. This is achieved by creating an incremental pointer based on the name of the pipeline. For example, the first time uploading a pipeline named, `myuser/gptneo`, the pointer `myuser/gptneo:v1` will be created behind the scene. If we modify my pipeline and then upload it again using the same name, a new version will be created with pointer `myuser/gptneo:v2`.

## Listing pointers

You can view all the pointers you have available using the following CLI command:

```python shell
pipeline get pointers
```

## Creating a pointer

You can use the CLI to create a pointer:

```c shell
pipeline create pointers <pointer_name> <source_pipeline>
```

Here, `pointer_name` is the pointer you want to create and `source_pipeline` can either be a pipeline id or another pointer.

Note that the pointer name must start with your username and pipeline name in the format `username/pipeline_name:tag`

For example, you can create a `latest` tag that points to the `v2` version of the pipeline above, as follows:

```python shell
pipeline create pointers myuser/gptneo:latest myuser/gptneo:v2
```

or using the pipeline ID:

```c shell
pipeline create pointers myuser/gptneo:latest pipeline_abcd1234
```

Then, you can make an inference request by using this pointer value:

```shell
curl -X POST '<https://www.mystic.ai/v4/runs'>  
--header 'Authorization: Bearer YOUR_TOKEN'  
--header 'Content-Type: application/json'  
--data '{  
	"pipeline": "myuser/gptneo:latest",  
	}  
'
```