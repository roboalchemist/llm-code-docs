# Source: https://docs.mystic.ai/docs/cold-start-optimisations.md

# Cold start optimisations

Many models can take several minutes to load for the first time. The Pipeline SDK offers several features that help in reducing the impact of this on your inference requests.

Common reasons for long cold start times:

* Large pipeline docker image sizes, most likely due to large python dependencies (`torch`, `transformers`, `diffusers`, `tensorflow` etc)
* Downloading model weights. This is normally due to unreliable, volatile, and slow download speeds (commonly from Huggingface when using `transformers`)
* Initialising model weights on the GPU

The typical procedure before running inference is:

1. Startup VM instance in the cloud
2. Pull the pipeline docker image from the registry
3. Start docker container
4. Download model weights
5. Load model on GPU
6. Ready for inference

The next sections cover the features available for decreasing, or removing any cold start times from your pipelines.

# Preemptive caching

When you deploy a model to Mystic, steps 1-3 above are optimised behind the scenes for you, but 4-5 can be optimised in the Pipeline SDK when you create a pipeline. Mystic will automatically try to load your models by looking at the current and historical traffic going to those models. This is called **preemptive caching**. To make your pipelines compatible with this the Pipeline SDK has arguments in the `pipe` decorator, `on_startup` and `run_once`, we will cover these in shortly.

Here's an example basic StableDiffusion pipeline:

```python
from pathlib import Path
from typing import List

import torch
from diffusers import StableDiffusionPipeline

from pipeline import Pipeline, Variable, entity, pipe
from pipeline.cloud import compute_requirements, environments, pipelines
from pipeline.objects import File
from pipeline.objects.graph import InputField, InputSchema

@entity
class StableDiffusionModel:
    @pipe(on_startup=True, run_once=True)
    def load(self):
        model_id = "runwayml/stable-diffusion-v1-5"
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
        )
        self.pipe = self.pipe.to(device)

    @pipe
    def predict(self, prompt: str) -> List[File]:
        images = self.pipe(prompt).images

        output_images = []
        for i, image in enumerate(images):
            path = Path(f"/tmp/sd/image-{i}.jpg")
            path.parent.mkdir(parents=True, exist_ok=True)
            image.save(str(path))
            output_images.append(File(path=path, allow_out_of_context_creation=True))

        return output_images


with Pipeline() as builder:
    prompt = Variable(str)

    model = StableDiffusionModel()
    model.load()
    output = model.predict(prompt, kwargs)
    builder.output(output)

```

On line `14` we see the use of the two `on_startup` and `run_once` keyword arguments, but the Pipeline is built as normal as shown in line `37` onwards.

The keyword arguments act as their names describe:

* `on_startup` - Run the `pipe` when the Pipeline is first run, or when the Pipelines `startup` function is called
* `run_once` - Only run the function on the first call, and do not run it again