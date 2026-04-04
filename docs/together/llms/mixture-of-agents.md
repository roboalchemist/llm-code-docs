# Source: https://docs.together.ai/docs/mixture-of-agents.md

# Together Mixture Of Agents (MoA)

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=02766bf41d0316857249b3c6f9ec2018" alt="" data-og-width="2588" width="2588" data-og-height="1350" height="1350" data-path="images/guides/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c6c27dc0c366ca8b2a755e260b272a6e 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0c4d554476f94c2fcaad2cddcd17bfec 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=29bad505a1c5776526b4d46f5eb8440a 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f4d742f2d7f2ed140ba87b4636a6c7a2 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7d0814be47799eb4a50e5cb73945f115 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a430e65b511573b35350a1202c43ba2a 2500w" />
</Frame>

## What is Together MoA?

Mixture of Agents (MoA) is a novel approach that leverages the collective strengths of multiple LLMs to enhance performance, achieving state-of-the-art results. By employing a layered architecture where each layer comprises several LLM agents, **MoA significantly outperforms** GPT-4 Omni’s 57.5% on AlpacaEval 2.0 with a score of 65.1%, using only open-source models!

The way Together MoA works is that given a prompt, like `tell me the best things to do in SF`, it sends it to 4 different OSS LLMs. It then combines results from all 4, sends it to a final LLM, and asks it to combine all 4 responses into an ideal response. That’s it! It’s just the idea of combining the results of 4 different LLMs to produce a better final output. It’s obviously slower than using a single LLM but it can be great for use cases where latency doesn't matter as much like synthetic data generation.

For a quick summary and 3-minute demo on how to implement MoA with code, watch the video below:

<Frame>
  <iframe class="embedly-embed" src="//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FTvGjgdNC0P8%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DTvGjgdNC0P8&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FTvGjgdNC0P8%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube" width="854" height="480" scrolling="no" title="YouTube embed" frameborder="0" allow="autoplay; fullscreen; encrypted-media; picture-in-picture;" allowfullscreen="true" />
</Frame>

## Together MoA in 50 lines of code

To get to get started with using MoA in your own apps, you'll need to install the Together python library, get your Together API key, and run the code below which uses our chat completions API to interact with OSS models.

1. Install the Together Python library

```bash Shell theme={null}
pip install together
```

2. Get your [Together API key](https://api.together.xyz/settings/api-keys) & export it

```bash Shell theme={null}
export TOGETHER_API_KEY='xxxx'
```

3. Run the code below, which interacts with our chat completions API.

This implementation of MoA uses 2 layers and 4 LLMs. We’ll define our 4 initial LLMs and our aggregator LLM, along with our prompt. We’ll also add in a prompt to send to the aggregator to combine responses effectively. Now that we have this, we’ll simply send the prompt to the 4 LLMs and compute all results simultaneously. Finally, we'll send the results from the four LLMs to our final LLM, along with a system prompt instructing it to combine them into a final answer, and we’ll stream results back.

```py Python theme={null}
# Mixture-of-Agents in 50 lines of code
import asyncio
import os
from together import AsyncTogether, Together

client = Together()
async_client = AsyncTogether()

user_prompt = "What are some fun things to do in SF?"
reference_models = [
    "Qwen/Qwen2-72B-Instruct",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "mistralai/Mixtral-8x22B-Instruct-v0.1",
    "databricks/dbrx-instruct",
]
aggregator_model = "mistralai/Mixtral-8x22B-Instruct-v0.1"
aggreagator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability.

Responses from models:"""


async def run_llm(model):
    """Run a single LLM call with a reference model."""
    response = await async_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": user_prompt}],
        temperature=0.7,
        max_tokens=512,
    )
    print(model)
    return response.choices[0].message.content


async def main():
    results = await asyncio.gather(
        *[run_llm(model) for model in reference_models]
    )

    finalStream = client.chat.completions.create(
        model=aggregator_model,
        messages=[
            {"role": "system", "content": aggreagator_system_prompt},
            {
                "role": "user",
                "content": ",".join(str(element) for element in results),
            },
        ],
        stream=True,
    )

    for chunk in finalStream:
        print(chunk.choices[0].delta.content or "", end="", flush=True)


asyncio.run(main())
```

## Advanced MoA example

In the previous example, we went over how to implement MoA with 2 layers (4 LLMs answering and one LLM aggregating). However, one strength of MoA is being able to go through several layers to get an even better response. In this example, we'll go through how to run MoA with 3+ layers.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0d8b3ab35cd1c934702082358f0aea7f" alt="" data-og-width="2036" width="2036" data-og-height="926" height="926" data-path="images/guides/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d5d56bcaa112033fd024a43c6873ffd4 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=476fbdc4c0e77ab6e281d11535799e85 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=838eb9b5f26594a63dab6c57effc376e 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=436b698543fd544c09b24ac4a0b4aec8 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8f99043f81c6b16b8581441f3ad2205e 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=19b41287a5693e2863443f3becfa36dd 2500w" />
</Frame>

```py Python theme={null}
# Advanced Mixture-of-Agents example – 3 layers
import asyncio
import os
import together
from together import AsyncTogether, Together

client = Together()
async_client = AsyncTogether()

user_prompt = "What are 3 fun things to do in SF?"
reference_models = [
    "Qwen/Qwen2-72B-Instruct",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "mistralai/Mixtral-8x22B-Instruct-v0.1",
    "databricks/dbrx-instruct",
]
aggregator_model = "mistralai/Mixtral-8x22B-Instruct-v0.1"
aggreagator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability.

Responses from models:"""
layers = 3


def getFinalSystemPrompt(system_prompt, results):
    """Construct a system prompt for layers 2+ that includes the previous responses to synthesize."""
    return (
        system_prompt
        + "\n"
        + "\n".join(
            [f"{i+1}. {str(element)}" for i, element in enumerate(results)]
        )
    )


async def run_llm(model, prev_response=None):
    """Run a single LLM call with a model while accounting for previous responses + rate limits."""
    for sleep_time in [1, 2, 4]:
        try:
            messages = (
                [
                    {
                        "role": "system",
                        "content": getFinalSystemPrompt(
                            aggreagator_system_prompt, prev_response
                        ),
                    },
                    {"role": "user", "content": user_prompt},
                ]
                if prev_response
                else [{"role": "user", "content": user_prompt}]
            )
            response = await async_client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=512,
            )
            print("Model: ", model)
            break
        except together.error.RateLimitError as e:
            print(e)
            await asyncio.sleep(sleep_time)
    return response.choices[0].message.content


async def main():
    """Run the main loop of the MOA process."""
    results = await asyncio.gather(
        *[run_llm(model) for model in reference_models]
    )

    for _ in range(1, layers - 1):
        results = await asyncio.gather(
            *[
                run_llm(model, prev_response=results)
                for model in reference_models
            ]
        )

    finalStream = client.chat.completions.create(
        model=aggregator_model,
        messages=[
            {
                "role": "system",
                "content": getFinalSystemPrompt(
                    aggreagator_system_prompt, results
                ),
            },
            {"role": "user", "content": user_prompt},
        ],
        stream=True,
    )
    for chunk in finalStream:
        print(chunk.choices[0].delta.content or "", end="", flush=True)


asyncio.run(main())
```

## Resources

* [Together MoA GitHub Repo](https://github.com/togethercomputer/MoA) (includes an interactive demo)
* [Together MoA blog post](https://www.together.ai/blog/together-moa)
* [MoA Technical Paper](https://arxiv.org/abs/2406.04692)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt