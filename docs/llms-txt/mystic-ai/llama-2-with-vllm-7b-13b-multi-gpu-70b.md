# Source: https://docs.mystic.ai/docs/llama-2-with-vllm-7b-13b-multi-gpu-70b.md

# Llama 2 chat with vLLM (7B, 13B & multi-gpu 70B)

This guide shows how to accelerate Llama 2 inference using the vLLM library for the 7B, 13B and multi GPU vLLM with 70B.

Llama 2 is an open source LLM family from Meta. This example demonstrates how to achieve faster inference with the Llama 2 models by using the open source project [vLLM](https://github.com/vllm-project/vllm). This guide will run the chat version on the models, and for the 70B variation ray will be used for multi GPU support. Also, formatting messages to the same syntax as ChatGPT from OpenAI is demonstrated so that you can directly swap over models.

Below is a table outlining the GPU VRAM requirements for the models (all models are in bfloat16 mode with a single conversation being processed):

| Model                                                                                                                      | Required VRAM | GPUs         | Tokens per second | Cost per 1k tokens |
| :------------------------------------------------------------------------------------------------------------------------- | :------------ | :----------- | :---------------- | :----------------- |
| 7B vLLM ([source](https://github.com/mystic-ai/pipeline/blob/main/examples/text-to-text/llama2-13b-vllm/new_pipeline.py))  | 25GB          | A100         | \~49              | $0.0113            |
| 13B vLLM ([source](https://github.com/mystic-ai/pipeline/blob/main/examples/text-to-text/llama2-13b-vllm/new_pipeline.py)) | \~37GB        | A100         | \~32              | $0.0174            |
| 70B vLLM                                                                                                                   | 160GB         | 2x A100 80GB | \~13              | $0.128             |

You can also play with the models right now to test out the performance for yourself:

* [Llama 2 7B chat](https://www.mystic.ai/meta/llama2-7B-chat/play)
* [Llama 2 13B chat](https://www.mystic.ai/meta/llama2-13B-chat/play)

# Weights

Both Meta and Huggingface have gated access to the weights so you have to agree with the licenses in both locations:

* Huggingface
  * <https://huggingface.co/meta-llama/Llama-2-7b-chat-hf>
  * <https://huggingface.co/meta-llama/Llama-2-13b-chat-hf>
  * <https://huggingface.co/meta-llama/Llama-2-70b-chat-hf>
* Meta: <https://ai.meta.com/resources/models-and-libraries/llama-downloads/>

These wights are now available to you with your huggingface API token, and will be used later.

# Inference pipeline creation

> 📘 Make sure you're logged in before continuing
>
> You need to authenticate your local system with Mystic or your pcore deployment to run the following code: `pipeline cluster login mystic-api YOUR_TOKEN -a`

Before creating our pipeline you first have to create your virtual environment for remote inference (the packages must be installed on your local system also to verify the pipeline):

```yaml
runtime:
  container_commands:
    - apt-get update
  python:
    version: "3.10"
    requirements:
      - pipeline-ai==2.0.15
      - torch==2.0.1
      - transformers==4.31.0
      - diffusers==0.19.3
      - accelerate==0.21.0
      - hf-transfer~=0.1
      - vllm==0.1.4
    cuda_version: "11.4"
accelerators: ["nvidia_a100"]
pipeline_graph: new_pipeline:my_new_pipeline
pipeline_name: llama2-13b-vllm
```

For wrapping the model to run in the venv we will use pipeline `entity` classes that will load the model weights and perform the inference requests:

```python
from huggingface_hub import snapshot_download
from vllm import LLM, SamplingParams

from pipeline import entity, pipe


@entity
class LlamaPipeline:
    @pipe(on_startup=True, run_once=True)
    def load_model(self) -> None:
        model_dir = "/tmp/llama2-7b-cache/"
        snapshot_download(
            "meta-llama/Llama-2-7b-chat-hf",
            local_dir=model_dir,
            token="YOUR_HUGGINGFACE_TOKEN",
        )
        self.llm = LLM(
            model_dir,
            dtype="bfloat16",
        )
        self.tokenizer = self.llm.get_tokenizer()
```

## Formatting chats

As Llama2 chat was fine-tuned on specific input syntax, we have to make sure that our input string is matching that syntax. This example shows to perform inference on multiple chats simultaneously, where each chat is of course constituted of multiple messages. Each message has an associated role, and there are three roles:

* `system` - A prompt to guide the chat bot for a character profile of your choosing (must be first or a default one will be put in)
* `user` - A message from a user
* `assistant` - The output result from the model.

An example input with 2 conversations:

```python
[
  [
    {
      "role": "system",
      "content": "Reply with only a JSON, like {\"category\": \"{categories}\"}. Classify the tweet into one of the following categories: 'Social media', 'Cats', 'Technology', 'Politics', 'Raves', 'Lifestyle'."
    },
    {
      "role": "user",
      "content": "I love the new Meta Llama 2 model it's really good, yay Zuck!"
    }
  ],
  [
    {
      "role": "system",
      "content": "You are an essay writing assistant."
    },
    {
      "role": "user",
      "content": "I love the new Meta Llama 2 model it's really good, yay Zuck!"
    },
    {
      "role": "assistant",
      "content": "Here's a long essay..."
    },
    {
      "role": "user",
      "content": "I don't like it make another!"
    }
    
  ],
  
]	
```

The code to properly format these inputs to a full series of prompts is shown below inside the previously defined `entity` class:

```python
from pipeline.objects.graph import InputField, InputSchema, Variable

class ModelKwargs(InputSchema):
    do_sample: bool | None = InputField(default=False)
    use_cache: bool | None = InputField(default=True)
    temperature: float | None = InputField(default=0.6)
    top_k: float | None = InputField(default=50)
    top_p: float | None = InputField(default=0.9)
    max_new_tokens: int | None = InputField(default=100, ge=1, le=1000)
    presence_penalty: float | None = InputField(default=1.0)
    default_system_prompt: str | None = InputField(
        default="""You are a helpful, respectful and honest assistant.
Always answer as helpfully as possible, while being safe. Your answers should not include any harmful,
unethical, racist, sexist, toxic, dangerous, or illegal content.
Please ensure that your responses are socially unbiased and positive in nature.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct.
If you don't know the answer to a question, please don't share false information."""
    )

@entity
class LlamaPipeline:
    ...
    @pipe
    def inference(self, dialogs: list, kwargs: ModelKwargs) -> List[str]:
        B_INST, E_INST = "[INST]", "[/INST]"
        B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
        DEFAULT_SYSTEM_PROMPT = kwargs.default_system_prompt

        sampling_params = SamplingParams(
            temperature=kwargs.temperature,
            top_p=kwargs.top_p,
            max_tokens=kwargs.max_new_tokens,
            presence_penalty=kwargs.presence_penalty,
        )

        prompt_tokens = []
        for dialog in dialogs:
            if dialog[0]["role"] != "system":
                dialog = [
                    {
                        "role": "system",
                        "content": DEFAULT_SYSTEM_PROMPT,
                    }
                ] + dialog
            dialog = [
                {
                    "role": dialog[1]["role"],
                    "content": B_SYS
                    + dialog[0]["content"]
                    + E_SYS
                    + dialog[1]["content"],
                }
            ] + dialog[2:]
            assert all([msg["role"] == "user" for msg in dialog[::2]]) and all(
                [msg["role"] == "assistant" for msg in dialog[1::2]]
            ), (
                "model only supports 'system', 'user' and 'assistant' roles, "
                "starting with 'system', then 'user' and alternating (u/a/u/a/u...)"
            )

            dialog_tokens = sum(
                [
                    [
                        [self.tokenizer.bos_token_id]
                        + self.tokenizer(
                            f"{B_INST} {(prompt['content']).strip()} {E_INST} {(answer['content']).strip()} "
                        ).input_ids
                        + [self.tokenizer.eos_token_id]
                    ]
                    for prompt, answer in zip(
                        dialog[::2],
                        dialog[1::2],
                    )
                ],
                [],
            )
            assert (
                dialog[-1]["role"] == "user"
            ), f"Last message must be from user, got {dialog[-1]['role']}"
            dialog_tokens += [
                [self.tokenizer.bos_token_id]
                + self.tokenizer(
                    f"{B_INST} {(dialog[-1]['content']).strip()} {E_INST}"
                ).input_ids
            ]

            prompt_tokens.append(dialog_tokens)
        generation_tokens = []
        input_num_tokens = []
        for prompt_tok in prompt_tokens:
            prompt_tok = [[item for sublist in prompt_tok for item in sublist]]
            if kwargs.max_new_tokens == -1:
                sampling_params.max_new_tokens = self.tokenizer.model_max_length - len(
                    prompt_tok[0]
                )
            generation_tokens.append(
                self.llm.generate(
                    prompt_token_ids=prompt_tok,
                    sampling_params=sampling_params,
                )
            )
            input_num_tokens.append(len(prompt_tok[0]))

        return [
            {
                "role": "assistant",
                "content": t[0].outputs[0].text,
            }
            for i, t in enumerate(generation_tokens)
        ]
```

## Running and uploading

and now to wrap all of the code into an inference pipeline:

```python
from pipeline import Pipeline
from pipeline.cloud.compute_requirements import Accelerator
from pipeline.configuration import current_configuration

current_configuration.set_debug_mode(True)


with Pipeline() as builder:
    prompt = Variable(list)
    kwargs = Variable(ModelKwargs)

    _pipeline = LlamaPipeline()
    _pipeline.load_model()
    out = _pipeline.inference(prompt, kwargs)

    builder.output(out)


my_pipeline = builder.get_pipeline()
```

This can then be uploaded using `pipeline container push` or to run it locally use `pipeline container up`

# Multi GPU with Llama2 70B

Some very minimal changes are required to run the 70B variation, and they're all in the initial load function and upload:

```python
@entity
class LlamaPipeline:
    @pipe(on_startup=True, run_once=True)
    def load_model(self) -> None:
        model_dir = "/tmp/llama2-70b-cache/"
        snapshot_download(
            "meta-llama/Llama-2-70b-hf",
            local_dir=model_dir,
            token="YOUR_HUGGINGFACE_TOKEN",
            ignore_patterns=["*.safetensors"], # Don't download everything
        )

        self.llm = LLM(
            model_dir,
            dtype="bfloat16",
            tensor_parallel_size=2, # This changes the GPU support to 2
        )

```