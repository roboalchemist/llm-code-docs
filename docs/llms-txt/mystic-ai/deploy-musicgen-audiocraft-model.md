# Source: https://docs.mystic.ai/docs/deploy-musicgen-audiocraft-model.md

# Deploy MusicGen model from AudioCraft

AudioCraft is a PyTorch library for deep learning research on audio generation. AudioCraft contains inference and training code for two state-of-the-art AI generative models producing high-quality audio: AudioGen and MusicGen.

In this tutorial will show how to deploy MusicGen.

# Initialise a new pipeline

In an empty directory, you can initialise a new project by running the following command:

```shell
pipeline container init
```

You should see 2 new files appear, `my_new_pipeline.py` and `pipeline.yaml`, with some initial content that we will later update. The `.py` file should contain the code that should be executed at runtime while the `.yaml` file is a configuration file for the pipeline.

# The pipeline graph

Substitute the following code into `my_new_pipeline.py`:

```python my_new_pipeline.py
from pipeline import Pipeline, Variable, entity, pipe
from pipeline.objects import File


@entity
class MusicgenModel:
    def __init__(self):
        ...

    @pipe(on_startup=True, run_once=True)
    def load(self):
        from audiocraft.models import MusicGen

        self.model = MusicGen.get_pretrained("large")

    @pipe
    def predict(self, prompt: str, duration: int) -> File:
        from audiocraft.data.audio import audio_write

        self.model.set_generation_params(duration=duration)
        descriptions = [prompt]
        wav = self.model.generate(descriptions)

        for idx, one_wav in enumerate(wav):
            file_path = f"/tmp/{idx}"
            # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
            audio_write(
                file_path,
                one_wav.cpu(),
                self.model.sample_rate,
                strategy="loudness",
                loudness_compressor=True,
            )

        output_file = File(path=file_path + ".wav", allow_out_of_context_creation=True)
        return output_file


with Pipeline() as builder:
    prompt = Variable(
        str,
        title="Prompt",
        description='Describe the music to be generated, \
        e.g. "rock song with a long guitar solo"',
    )
    duration = Variable(
        int,
        title="Duration",
        description="Length of the music in seconds, \
        generation can take long so keep numbers low",
    )

    model = MusicgenModel()

    model.load()

    output = model.predict(prompt, duration)

    builder.output(output)

my_new_pipeline = builder.get_pipeline()
```

# The pipeline config

Substitute the following configuration into `pipeline.yaml`:

```yaml pipeline.yaml
runtime:
  container_commands:
    - apt-get update
    - apt-get install -y git libgl1-mesa-glx ffmpeg gcc
  python:
    version: "3.10"
    requirements:
      - pipeline-ai
      - torch==2.0.1
      - audiocraft
    cuda_version: "11.4"
accelerators: ["nvidia_a100"]
accelerator_memory: null
pipeline_graph: new_pipeline:my_new_pipeline
pipeline_name: musicgen-large
description: null
readme: null
extras: {}
```

Notice the additional `apt` packages that we have declared should be installed in the container, e.g. `ffmpeg`.

## Build pipeline docker image

To build a docker image of the pipeline, run the following command from the same directory containing the files:

```shell
pipeline container build
```

## Run container locally

Before uploading your pipeline, we strongly encourage to test your pipeline locally, to ensure it behaves as expected. To do so, run:

```shell
pipeline container up
```

It will take a little while for the model to be downloaded. The container comes with [an API](http;//localhost:14300), allowing you to make local inference requests. Check out the [play form ](http://localhost:14300/play) to quickly start testing out the pipeline.

## Push pipeline docker image

To upload the pipeline, or push the docker image of the pipeline to the Mystic docker registry, run the following command:

```shell
pipeline container push
```