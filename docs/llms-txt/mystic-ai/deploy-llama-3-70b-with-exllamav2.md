# Source: https://docs.mystic.ai/docs/deploy-llama-3-70b-with-exllamav2.md

# Deploy Llama 3 70B with ExLlamav2

In this tutorial we will cover how to deploy Llama 3 70B, quantised to 4bpw (bits-per-weight), using the inference engine [Exllamav2](https://github.com/turboderp/exllamav2), an ideal inference engine for quantised models running on single GPUs.

This guide assumes you are familiar with packaging a model with our Python SDK and Exllamav2.

After deploying you should expect the following performance,

| GPU         | Required vRAM | Batch size | Input tokens | Output tokens | Speed (tok/s) |
| :---------- | :------------ | :--------- | :----------- | :------------ | :------------ |
| 1xA100-80GB | 38.2 GB       | 1          | 93           | 300           | 26.12         |

> 👍 Since the total vRAM utilised by this model during inference is less than 40GB, we can use half an A100-80gb or H100 when deploying on Mystic. This frees up the rest of the GPU to be utilised by another of your pipelines or for higher concurrency, have 2 instances of the same model running in parallel.

# Build pipeline

Let's start by creating a container project. In your terminal, after installing the latest pipeline-ai package, run the following:

```
pipeline container init -n llama3-70b-4bpw
```

In the directory you will see 3 newly generated files, a README, a .py, and a .yaml file.

### Llama3 pipeline (streaming mode)

On the auto-generated python file, replace with the following:

```py
from huggingface_hub import snapshot_download
import os
from pathlib import Path
from pipeline import Pipeline, Variable, entity, pipe
from pipeline.objects.graph import InputField, InputSchema, Stream
from typing import Optional

from exllamav2 import(
    ExLlamaV2,
    ExLlamaV2Config,
    ExLlamaV2Cache,
    ExLlamaV2Tokenizer,
)

from exllamav2.generator import (
    ExLlamaV2StreamingGenerator,
    ExLlamaV2Sampler
)

import time
import torch

HF_TOKEN = "YOUR_HF_TOKEN"
MODEL_NAME = "turboderp/Llama-3-70B-Instruct-exl2"
REVISION="4.0bpw"

class PromptFormat_llama3():
    '''
    https://github.com/turboderp/exllamav2/blob/master/examples/chat_prompts.py
    '''

    description = "Llama3-instruct models"

    def __init__(self):
        pass

    def default_system_prompt(self):
        return \
            """Assist users with tasks and answer questions to the best of your knowledge. Provide helpful and informative """ + \
            """responses. Be conversational and engaging. If you are unsure or lack knowledge on a topic, admit it and try """ + \
            """to find the answer or suggest where to find it. Keep responses concise and relevant. Follow ethical """ + \
            """guidelines and promote a safe and respectful interaction."""

    def first_prompt(self):
        return \
            """<|start_header_id|>system<|end_header_id|>\n\n""" + \
            """<|system_prompt|><|eot_id|>""" + \
            """<|start_header_id|>user<|end_header_id|>\n\n""" + \
            """<|user_prompt|><|eot_id|>""" + \
            """<|start_header_id|>assistant<|end_header_id|>"""

    def subs_prompt(self):
        return \
            """<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n""" + \
            """<|user_prompt|><|eot_id|>""" + \
            """<|start_header_id|>assistant<|end_header_id|>"""

    def stop_conditions(self, tokenizer):
        return \
            [tokenizer.eos_token_id,
             tokenizer.single_id("<|eot_id|>"),
             tokenizer.single_id("<|start_header_id|>")]
    

prompt_format = PromptFormat_llama3()

class Kwargs(InputSchema):
    temperature: Optional[float] = InputField(0.99, title="Temperature", description="The temperature to use for sampling.")
    top_k: Optional[int] = InputField(100, title="Top k", description="The number of tokens to sample from.")
    top_p: Optional[float] = InputField(0.9, title="Top p", description="The cumulative probability to sample from.")

    enable_eot: Optional[bool] = InputField(True, title="Stop when stop-toen is generated", description="If True, model will end when stop-token is generated, if False it will carry on generating until max_new_tokens")

    system_prompt: Optional[str] = InputField(prompt_format.default_system_prompt(), title="System prompt", description="The system prompt to use.")
    print_metrics: Optional[bool] = InputField(False, title="Print metrics", description="If True, print metrics.")
    

# Put your model inside of the below entity class
@entity
class MyModelClass:

    def download_model(self):

        MODEL_WEIGHTS_PATH = Path(os.path.dirname(os.path.abspath(__file__)) + "/" + MODEL_NAME[MODEL_NAME.find('/'):] + "-" + REVISION).expanduser()
        MODEL_WEIGHTS_PATH.mkdir(parents=True, exist_ok=True)

        snapshot_download(
            MODEL_NAME,
            local_dir=MODEL_WEIGHTS_PATH,
            token=HF_TOKEN,
            revision=REVISION)
        
        self.model_weights_path = MODEL_WEIGHTS_PATH

    @pipe(run_once=True, on_startup=True)
    def setup(self) -> None:

        self.download_model()

        print("Loading model")
        # Initialize model and cache
        self.config = ExLlamaV2Config()
        self.config.debug_mode = True
        self.config.model_dir = self.model_weights_path
        self.config.prepare()

        self.model = ExLlamaV2(self.config)

        cache = ExLlamaV2Cache(self.model, lazy = True)
        self.model.load_autosplit(cache)

        self.settings = ExLlamaV2Sampler.Settings()
        self.tokenizer = ExLlamaV2Tokenizer(self.config)
        
        self.generator = ExLlamaV2StreamingGenerator(self.model, cache, self.tokenizer)
        self.generator.warmup()

        print("Model loaded")

    @pipe
    def predict(self, user_prompt: str, max_new_tokens: int, kwargs: Kwargs) -> Stream:
        self.settings.temperature = kwargs.temperature
        self.settings.top_k = kwargs.top_k
        self.settings.top_p = kwargs.top_p
        self.settings.token_repetition_penalty = 1.05
        self.settings.mirostat = True
        self.settings.mirostat_tau = 5.0

        # Prompt settings
        prompt = prompt_format.first_prompt() \
            .replace("<|system_prompt|>", kwargs.system_prompt) \
            .replace("<|user_prompt|>", user_prompt)
        

        # Generate exactly max_new_tokens, may lead to garbage outputs.
        # if removed, model will stop when it should stop, i.e question has been answered, no need to carry on generating.
        # self.settings.disallow_tokens(self.tokenizer, [self.tokenizer.single_id("<|eot_id|>")])
        if not kwargs.enable_eot:
            self.settings.disallow_tokens(self.tokenizer, [self.tokenizer.single_id("<|eot_id|>")])

        time_begin_prompt = time.time()

        input_ids = self.tokenizer.encode(prompt, encode_special_tokens = True)
        prompt_tokens = input_ids.shape[-1]
        self.generator.set_stop_conditions(prompt_format.stop_conditions(self.tokenizer))
        self.generator.begin_stream_ex(input_ids, self.settings)

        def generator():
            time_begin_stream = time.time()
            generated_tokens = 0

            eos = False
            while not eos:
                res = self.generator.stream_ex()
                chunk = res["chunk"]
                eos = res["eos"]

                generated_tokens += 1

                if generated_tokens >= max_new_tokens:
                    eos = True
                yield chunk

            time_end = time.time()

            time_prompt = time_begin_stream - time_begin_prompt
            time_tokens = time_end - time_begin_stream

            if kwargs.print_metrics:
                print(f"\n\nPrompt processed in {time_prompt:.2f} seconds, {prompt_tokens} tokens, {prompt_tokens / time_prompt:.2f} tokens/second ({time_prompt / prompt_tokens * 1000:.2f}ms/token)")
                print(f"Response generated in {time_tokens:.2f} seconds, {generated_tokens} tokens, {generated_tokens / time_tokens:.2f} tokens/second ({time_tokens / generated_tokens * 1000:.2f}ms/token)")
                print(f"Memory allocated: {torch.cuda.max_memory_allocated(0)/ 1024**3:.2f}GB")

        return Stream(generator())


with Pipeline() as builder:
    prompt = Variable(str, default="Give me a summary of stoic philosophy")
    max_new_tokens = Variable(int, default=150, title="Max tokens", description="Maximum number of tokens to generate per output sequence.")
    kwargs = Variable(Kwargs, title="Other parameters")

    my_model = MyModelClass()
    my_model.setup()

    output_var = my_model.predict(prompt, max_new_tokens, kwargs)

    builder.output(output_var)

my_new_pipeline = builder.get_pipeline()
```

The above script allows to package Llama-3 as a streaming endpoint. If you are interested in non-streaming, you can use the following script instead.

### Llama3 pipeline (non-streaming inference)

```py
from huggingface_hub import snapshot_download
import os
from pathlib import Path
from pipeline import Pipeline, Variable, entity, pipe
from pipeline.objects.graph import InputField, InputSchema, Stream
from typing import Optional

from exllamav2 import(
    ExLlamaV2,
    ExLlamaV2Config,
    ExLlamaV2Cache,
    ExLlamaV2Tokenizer,
)

from exllamav2.generator import (
    ExLlamaV2BaseGenerator,
    ExLlamaV2Sampler
)

import time
import torch

HF_TOKEN = "YOUR_HF_TOKEN"
MODEL_NAME = "turboderp/Llama-3-70B-Instruct-exl2"
REVISION="4.0bpw"

class PromptFormat_llama3():
    '''
    https://github.com/turboderp/exllamav2/blob/master/examples/chat_prompts.py
    '''

    description = "Llama3-instruct models"

    def __init__(self):
        pass

    def default_system_prompt(self):
        return \
            """Assist users with tasks and answer questions to the best of your knowledge. Provide helpful and informative """ + \
            """responses. Be conversational and engaging. If you are unsure or lack knowledge on a topic, admit it and try """ + \
            """to find the answer or suggest where to find it. Keep responses concise and relevant. Follow ethical """ + \
            """guidelines and promote a safe and respectful interaction."""

    def first_prompt(self):
        return \
            """<|start_header_id|>system<|end_header_id|>\n\n""" + \
            """<|system_prompt|><|eot_id|>""" + \
            """<|start_header_id|>user<|end_header_id|>\n\n""" + \
            """<|user_prompt|><|eot_id|>""" + \
            """<|start_header_id|>assistant<|end_header_id|>"""

    def subs_prompt(self):
        return \
            """<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n""" + \
            """<|user_prompt|><|eot_id|>""" + \
            """<|start_header_id|>assistant<|end_header_id|>"""

    def stop_conditions(self, tokenizer):
        return \
            [tokenizer.eos_token_id,
             tokenizer.single_id("<|eot_id|>"),
             tokenizer.single_id("<|start_header_id|>")]
    

prompt_format = PromptFormat_llama3()

class Kwargs(InputSchema):
    temperature: Optional[float] = InputField(0.99, title="Temperature", description="The temperature to use for sampling.")
    top_k: Optional[int] = InputField(100, title="Top k", description="The number of tokens to sample from.")
    top_p: Optional[float] = InputField(0.9, title="Top p", description="The cumulative probability to sample from.")

    enable_eot: Optional[bool] = InputField(True, title="Stop when stop-toen is generated", description="If True, model will end when stop-token is generated, if False it will carry on generating until max_new_tokens")

    system_prompt: Optional[str] = InputField(prompt_format.default_system_prompt(), title="System prompt", description="The system prompt to use.")
    print_metrics: Optional[bool] = InputField(False, title="Print metrics", description="If True, print metrics.")
    

# Put your model inside of the below entity class
@entity
class MyModelClass:

    def download_model(self):

        MODEL_WEIGHTS_PATH = Path(os.path.dirname(os.path.abspath(__file__)) + "/" + MODEL_NAME[MODEL_NAME.find('/'):] + "-" + REVISION).expanduser()
        MODEL_WEIGHTS_PATH.mkdir(parents=True, exist_ok=True)

        snapshot_download(
            MODEL_NAME,
            local_dir=MODEL_WEIGHTS_PATH,
            token=HF_TOKEN,
            revision=REVISION)
        
        self.model_weights_path = MODEL_WEIGHTS_PATH

    @pipe(run_once=True, on_startup=True)
    def setup(self) -> None:

        self.download_model()

        print("Loading model")
        # Initialize model and cache
        self.config = ExLlamaV2Config()
        self.config.debug_mode = True
        self.config.model_dir = self.model_weights_path
        # self.config.max_batch_size = 2
        self.config.prepare()

        self.model = ExLlamaV2(self.config)

        cache = ExLlamaV2Cache(self.model, lazy = True)
        self.model.load_autosplit(cache)

        self.settings = ExLlamaV2Sampler.Settings()
        self.tokenizer = ExLlamaV2Tokenizer(self.config)
        
        self.generator = ExLlamaV2BaseGenerator(self.model, cache, self.tokenizer)
        self.generator.warmup()

        print("Model loaded")

    @pipe
    def predict(self, user_prompt: str, max_new_tokens: int, kwargs: Kwargs) -> Stream:
        self.settings.temperature = kwargs.temperature
        self.settings.top_k = kwargs.top_k
        self.settings.top_p = kwargs.top_p
        self.settings.token_repetition_penalty = 1.05
        self.settings.mirostat = True
        self.settings.mirostat_tau = 5.0

        # Prompt settings

        prompt = prompt_format.first_prompt() \
            .replace("<|system_prompt|>", kwargs.system_prompt) \
            .replace("<|user_prompt|>", user_prompt)
        
        # Generate exactly max_new_tokens, may lead to garbage outputs.
        # if removed, model will stop when it should stop, i.e question has been answered, no need to carry on generating.
        # self.settings.disallow_tokens(self.tokenizer, [self.tokenizer.single_id("<|eot_id|>")])
        if not kwargs.enable_eot:
            self.settings.disallow_tokens(self.tokenizer, [self.tokenizer.single_id("<|eot_id|>")])

        time_begin = time.time()
        output = self.generator.generate_simple(prompt, self.settings, max_new_tokens, stop_token=self.tokenizer.single_id("<|eot_id|>"), encode_special_tokens = True)
        time_total = time.time() - time_begin


        generated_output = output[output.find("assistant\n\n")+len("assistant\n\n"):]
        generated_tokens = self.tokenizer.encode(generated_output).shape[1]
        
        if kwargs.print_metrics:
            print(f"Response generated in {time_total:.2f} seconds, {generated_tokens} output tokens, {generated_tokens / time_total:.2f} tokens/second")
            print(f"Memory allocated: {torch.cuda.max_memory_allocated(0)/ 1024**3:.2f}GB")

        return output


with Pipeline() as builder:
    prompt = Variable(str, default="Give me a summary of stoic philosophy")
    max_new_tokens = Variable(int, default=150, title="Max tokens", description="Maximum number of tokens to generate per output sequence.")
    kwargs = Variable(Kwargs, title="Other parameters")

    my_model = MyModelClass()
    my_model.setup()

    output_var = my_model.predict(prompt, max_new_tokens, kwargs)

    builder.output(output_var)

my_new_pipeline = builder.get_pipeline()
```

### Debug pipeline locally (optional)

If you have a GPU in your local machine, you can debug this pipeline locally without any docker involved by adding the following lines of code,

For streaming,

```py
output_generator = my_new_pipeline.run("Summarise stoicism in a couple of paragraphs", 500, Kwargs(print_metrics=True))[0]
for chunk in output_generator:
    print(chunk, flush=True, end="")
print("\n")
```

For normal inference,

```py
output = my_new_pipeline.run("Give me a summary of stoic philosophy", 500, Kwargs(print_metrics=True))[0]
print(output)
```

You can then run this script using your favorite debugger or simply by running `python my_pipeline.py` assuming you have all the python libraries installed in your environment (you can look at the yaml file below to check what python packages you should install in your local environment).

### Build pipeline

Once the pipeline file is done, the next step is to "build" the pipeline. This basically allows to build the docker image that will be pushed onto Mystic. To build your pipeline, you will need to make sure your yaml file is filled out. You can replace your auto-generated yaml file with the following,

```yaml
runtime:
  container_commands:
  - apt-get update
  - apt-get install -y git gcc g++ wget
  - apt-get install -y software-properties-common
  - apt-get update
  - wget https://developer.download.nvidia.com/compute/cuda/repos/debian11/x86_64/cuda-keyring_1.1-1_all.deb
  - dpkg -i cuda-keyring_1.1-1_all.deb
  - add-apt-repository contrib
  - apt-get update
  - apt-get -y install cuda-toolkit-12-3
python:
    version: '3.10'
    requirements:
    - pipeline-ai
    - torch safetensors sentencepiece
    - exllamav2
    - huggingface_hub
    - transformers
accelerators: []
accelerator_memory: null
pipeline_graph: new_pipeline:my_new_pipeline
pipeline_name: llama3-70b-4bpw
description: null
readme: README.md
extras: {}
cluster: null
```

It will build CUDA, as well as the right python libraries to run your pipeline (torch, transformers, exllamav2, etc.)

Now you can build this pipeline by running:

```
pipeline container build
```

You can validate the container builds and runs successfully by running the container locally. This will create a mini-frontend app so you can test your model. This step is optional, but highly recommended, as it's the final step before going to production. To do this, assuming you have a GPU in your local machine, you can run the following command,

```
pipeline container up
```

> 📘 You should always test your pipeline in a machine with a GPU before deploying it to Mystic.

Once we are happy with the pipeline you can deploy it to your Mystic account by running:

```
pipeline container push
```

This will then be available in your dashboard from where you can share it with the community or edit any other meta-data. If you want to deploy it to your own private cluster running in your own cloud account, check-out our BYOC integration for more details [Mystic BYOC](https://docs.mystic.ai/docs/deploying-pipelines)