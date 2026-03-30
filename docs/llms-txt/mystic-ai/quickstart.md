# Source: https://docs.mystic.ai/docs/quickstart.md

# Quickstart

Speed run creating and deploying a pipeline

To run your projects on the Mystic suite of software you need to use our Python SDK. You can install this by running:

```shell
pip install pipeline-ai
```

> 👍 You'll also need Docker running on your system, see: <https://docs.docker.com/desktop/>

You can use the Mystic SDK to create "Pipelines" which can run locally or be uploaded and run remotely on Mystic or your PCore deployment. Pipelines are specially prepared Docker containers that run your inference code. In the next step, we'll initialise a Pipeline and take a closer look at how they work.

In an empty directory, run the following command and follow the prompts:

```shell shell
pipeline container init
```

This will create two files, `pipeline.yaml` and `new_pipeline.py`. Out of the box, these files are ready to get a Pipeline up and running. Let's take a look at that first, and then dive into what these files actually do.

Run the following command to build the Pipeline:

```shell shell
pipeline container build
```

> 🚧 Building a Pipeline will generate a Dockerfile which will be used by the build process. If you try edit this file, changes will be overwritten, so remember to edit your pipeline.yaml file instead!

You should see build logs similar to what you would get from a Docker image build. A successful build will end with something like the following:

```shell shell
Pipeline 11:33:05 - [SUCCESS]: Built container a8fab0143dba
Pipeline 11:33:05 - [SUCCESS]: Created tag my_user/my_pipeline
Pipeline 11:33:05 - [SUCCESS]: Created tag my_user/my_pipeline:a8fab0143dba
```

We can now run the pipeline locally and test it out!

```shell
pipeline container up
```

Pipelines come with their own [web UI](http://localhost:14300/play) for testing, and [API docs](http://localhost:14300/redoc). Both should be accessible with the above command. You can run the Pipeline directly in the web UI or from an API tool like `curl`.

Let's take a closer look now at the Pipeline files themselves. Here's `pipeline.yaml`:

```yaml yaml
runtime:
  container_commands:
  - apt-get update
  - apt-get install -y git
  python:
    version: '3.10'
    requirements:
    - pipeline-ai
    cuda_version: '11.4'
accelerators: []
accelerator_memory: null
pipeline_graph: new_pipeline:my_new_pipeline
pipeline_name: my_user/my_pipeline
```

This file tells the Pipeline library how to configure and build your container. You can add Python dependencies, specify GPU requirements (for Mystic deployments) and add Dockerfile build commands.

> 🚧 You should replace my\_user with your own username. If you try to upload a pipeline with a different username it will fail.

The `pipeline_graph` entry specifies the Python object that houses your inference code (`<.py file name>:<pipeline object>`). We'll see more of this when we look at the other file `new_pipeline.py`:

```python Python
from pipeline import Pipeline, Variable, entity, pipe


# Put your model inside of the below entity class
@entity
class MyModelClass:
    @pipe(run_once=True, on_startup=True)
    def load(self) -> None:
        # Perform any operations needed to load your model here
        print("Loading model...")

        ...

        print("Model loaded!")

    @pipe
    def predict(self, output_number: int) -> str:
        # Perform any operations needed to predict with your model here
        print("Predicting...")

        ...

        print("Prediction complete!")

        return f"Your number: {output_number}"


with Pipeline() as builder:
    input_var = Variable(
        int,
        description="A basic input number to do things with",
        title="Input number",
    )

    my_model = MyModelClass()
    my_model.load()

    output_var = my_model.predict(input_var)

    builder.output(output_var)

my_new_pipeline = builder.get_pipeline()

```

Here we can see a Pipeline object being created, with inputs and outputs defined through the Mystic SDK. Inside the Pipeline itself is code that is run at startup, and code that is run every time inference happens. You can read more about how inputs and outputs work [here](https://docs.mystic.ai/docs/inputs-outputs). Also note that all files in the current working directly will be copied into the container, so you can use Python modules and other files as normal in your Pipeline.

And that's it! You're now ready to build your own Pipeline, using any AI library you want. In the next section we'll take a look at uploading and running a Pipeline on Mystic.

# Uploading a Pipeline

The Mystic SDK allows you to authenticate with Mystic by running:

```
pipeline cluster login mystic-api API_TOKEN -u https://www.mystic.ai -a
```

If you don't have an API token yet, you can create one on your Mystic account [here](https://www.mystic.ai/api-tokens).

\[Note: you can also authenticate using environment variables if this is more convenient. You just need to set `PIPELINE_API_TOKEN=<YOUR_TOKEN>`]

Uploading your Pipeline is then as simple as running:

```Text shell
pipeline container push
```

The last few lines of your deployment will look something like:

```shell shell
Pipeline 14:35:25 - [SUCCESS]: Created new pipeline deployment for my_user/my_pipeline -> pipeline_76873283cece44e6bd04d91cfdb2b632 (image=registry:5000/my_user/my_pipeline:a8fab0143dba)
```

Notice that your Pipeline now has an associated Pipeline ID, which you can use to run inference. You should also be able to find your Pipeline in your Mystic account's [Pipelines page](https://www.mystic.ai/pipelines), where you can run inference through the web UI.

# Running a Pipeline

The SDK provides a way to run your pipeline directly in Python (make sure to run this in a separate file to your pipeline):

```python
from pipeline.cloud.pipelines import run_pipeline

pointer = "my_user/my_pipeline:v1"

result = run_pipeline(pointer, 1)

print(result.outputs_formatted())
```

You can also run your API directly with a tool like `curl`:

```shell shell
curl -X POST 'https://www.mystic.ai/v4/runs' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
	"pipeline": "my_user/my_pipeline:v1",
	"inputs": 
		[
			{"type":"integer","value":5}
		]
	}
'
```

Keep in mind that if you've changed your input types in your Pipeline, you'll need to change this command. You can find an auto-generated schema on your pipeline page on [www.mystic.ai](https://www.mystic.ai).

Congratulations! You are now ready to deploy AI models at scale with Mystic AI.