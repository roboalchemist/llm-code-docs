# Source: https://deepinfra.com/docs/advanced/autogen

We use essential cookies to make our site work. With your consent, we may also
use non-essential cookies to improve user experience and analyze website
traffic…

AcceptReject

[FLUX.2 is live!](https://deepinfra.com/models?q=flux-2) High-fidelity image
generation made simple.

[](/)

[Models](/models)

By Category

* * *

[Automatic Speech Recognition](/models/automatic-speech-
recognition)[Embeddings](/models/embeddings)[Reranker](/models/reranker)[Text
Generation](/models/text-generation)[Text To Image](/models/text-to-
image)[Text To Speech](/models/text-to-speech)[Text To Video](/models/text-to-
video)[Zero Shot Image Classification](/models/zero-shot-image-classification)

[View all models](/models)

By Family

* * *

[![anthropic
logo](/_next/static/media/anthropic.c6636fa8.svg)/Claude](/claude)[![deepseek-
ai
logo](/_next/static/media/deepseek.b1ec6c4e.svg)/DeepSeek](/deepseek)[![black-
forest-labs logo](/_next/static/media/bfl.7e050ff6.svg)/Flux](/flux)[![google
logo](/_next/static/media/google.09551b71.svg)/Gemini](/gemini)[![meta-llama
logo](/_next/static/media/meta.56a2e6fd.svg)/Llama](/llama)[![mistralai
logo](/_next/static/media/mistralai.ecbe51d4.svg)/Mistral](/mistral)[![nvidia
logo](/_next/static/media/nvidia.2165073d.svg)/Nemotron](/nemotron)[![qwen
logo](/_next/static/media/qwen.d6d74288.svg)/Qwen](/qwen)

[Docs](/docs)[Pricing](/pricing)[GPUs](/gpu-
instances)[Chat](/chat)[DeepStart](/deepstart)[Blog](/blog)

[Contact Sales](/contact-sales)[Log In](/login)

[Models](/models)

[Automatic Speech Recognition](/models/automatic-speech-
recognition)[Embeddings](/models/embeddings)[Reranker](/models/reranker)[Text
Generation](/models/text-generation)[Text To Image](/models/text-to-
image)[Text To Speech](/models/text-to-speech)[Text To Video](/models/text-to-
video)[Zero Shot Image Classification](/models/zero-shot-image-classification)

[Docs](/docs)

[Pricing](/pricing)

[GPUs](/gpu-instances)

[Chat](/chat)

[DeepStart](/deepstart)

[Blog](/blog)

Feedback

[Contact Sales](/contact-sales)

[Log In](/login)

  1. [Getting Started](/docs)

     1. [Quick Start Guide](/docs/getting-started)

     2. [Available Models](/docs/models)

     3. [Running Inference](/docs/inference)

     4. [Data Privacy & Security](/docs/data)

  2. [API Reference](/docs/api-reference)

     1. [OpenAI-Compatible API](/docs/openai_api)

     2. [DeepInfra Native API](/docs/deep_infra_api)

     3. [Rate Limits](/docs/advanced/rate-limits)

     4. [Webhooks](/docs/advanced/webhooks)

     5. [Authentication & Tokens](/docs/advanced/scoped_jwt)

  3. [Model Features](/docs/model-features)

     1. [Function Calling](/docs/advanced/function_calling)

     2. [JSON Mode](/docs/advanced/json_mode)

     3. [Multimodal Models](/docs/advanced/multimodal)

     4. [Log Probabilities](/docs/advanced/log_probs)

     5. [Max Output Tokens](/docs/advanced/max_tokens_limit)

  4. [GPU Instances](/docs/gpu-instances)

     1. [Containers](/docs/gpu-instances/containers)

  5. [Custom Deployments](/docs/custom-deployments)

     1. [Custom LLMs](/docs/advanced/custom_llms)

     2. [LoRA Adapter Models](/docs/advanced/lora)

     3. [LoRA Image Adapters](/docs/advanced/lora_text_to_image)

  6. [Integrations](/docs/integrations)

     1. [LangChain](/docs/advanced/langchain)

     2. [LlamaIndex](/docs/advanced/llama-index)

     3. [AI SDK](/docs/advanced/aisdk)

     4. AutoGen

     5. [Okta SSO](/docs/advanced/okta)

  7. [Tutorials & Examples](/docs/tutorials)

     1. [Stable Diffusion (Text to Image)](/docs/tutorials/stable-diffusion)

     2. [Whisper (Speech to Text)](/docs/tutorials/whisper)

     3. [Deprecated Models](/docs/advanced/deprecated)

  8. [Miscellaneous](/docs/misc)

     1. [Data Subprocessors](/docs/misc/subprocessors)

Documentation

  1. [Getting Started](/docs)

     1. [Quick Start Guide](/docs/getting-started)

     2. [Available Models](/docs/models)

     3. [Running Inference](/docs/inference)

     4. [Data Privacy & Security](/docs/data)

  2. [API Reference](/docs/api-reference)

     1. [OpenAI-Compatible API](/docs/openai_api)

     2. [DeepInfra Native API](/docs/deep_infra_api)

     3. [Rate Limits](/docs/advanced/rate-limits)

     4. [Webhooks](/docs/advanced/webhooks)

     5. [Authentication & Tokens](/docs/advanced/scoped_jwt)

  3. [Model Features](/docs/model-features)

     1. [Function Calling](/docs/advanced/function_calling)

     2. [JSON Mode](/docs/advanced/json_mode)

     3. [Multimodal Models](/docs/advanced/multimodal)

     4. [Log Probabilities](/docs/advanced/log_probs)

     5. [Max Output Tokens](/docs/advanced/max_tokens_limit)

  4. [GPU Instances](/docs/gpu-instances)

     1. [Containers](/docs/gpu-instances/containers)

  5. [Custom Deployments](/docs/custom-deployments)

     1. [Custom LLMs](/docs/advanced/custom_llms)

     2. [LoRA Adapter Models](/docs/advanced/lora)

     3. [LoRA Image Adapters](/docs/advanced/lora_text_to_image)

  6. [Integrations](/docs/integrations)

     1. [LangChain](/docs/advanced/langchain)

     2. [LlamaIndex](/docs/advanced/llama-index)

     3. [AI SDK](/docs/advanced/aisdk)

     4. AutoGen

     5. [Okta SSO](/docs/advanced/okta)

  7. [Tutorials & Examples](/docs/tutorials)

     1. [Stable Diffusion (Text to Image)](/docs/tutorials/stable-diffusion)

     2. [Whisper (Speech to Text)](/docs/tutorials/whisper)

     3. [Deprecated Models](/docs/advanced/deprecated)

  8. [Miscellaneous](/docs/misc)

     1. [Data Subprocessors](/docs/misc/subprocessors)

# AutoGen

AutoGen is a framework that enables the development of LLM applications using
multiple agents that can converse with each other to solve tasks. To learn
more, please visit the [AutoGen](https://github.com/microsoft/autogen).

#### AutoGen with DeepInfra endpoints

    
    
    # install autogen
    pip install pyautogen
    
    
    copy

Here is how you can configure autogen to use DeepInfra endpoints.

The `base_url` is `https://api.deepinfra.com/v1/openai`. You can use any model
which is OpenAI compatible. For example, [meta-llama/Meta-
Llama-3-70B-Instruct](/meta-llama/Meta-Llama-3-70B-Instruct) is a model that
can be used to solve coding tasks.

    
    
    import autogen
    
    config_list = [
        {
            "model": "meta-llama/Meta-Llama-3-70B-Instruct",
            "base_url": "https://api.deepinfra.com/v1/openai",
            "api_key": "<your DeepInfra API key here>"
        }
    ]
    
    llm_config={"config_list": config_list, "seed": 42}
    
    assistant = autogen.AssistantAgent("assistant", llm_config=llm_config)
    user_proxy = autogen.UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
    user_proxy.initiate_chat(assistant, message="What time is it right now?")
    
    
    copy

In the example, two agents converse and solve the task. The assistant agent
provides a python code snippet which then gets executed on your local machine.
In AutoGen, code execution is triggered automatically by the UserProxyAgent
when it detects an executable code block in a received message.

Here is the output of the above code:

    
    
    user_proxy (to assistant):
    
    What time is it now?
    
    --------------------------------------------------------------------------------
    assistant (to user_proxy):
    
    To get the current time, you can use the `datetime` module in Python. Here's an example code:
    ```python
    import datetime
    
    current_time = datetime.datetime.now()
    print(current_time.strftime("%I:%M %p"))
    ```
    This code will print the current time in a 12-hour format with the AM/PM designation. If you want to print the time in a 24-hour format, you can use the `%H:%M` format specifier instead of `%I:%M %p`.
    
    You can save this code in a file with a `.py` extension and run it in a terminal or command prompt to see the current time.
    
    Note: This code assumes that you have Python installed on your computer. If you don't have Python installed, you can download it from the official Python website.
    
    --------------------------------------------------------------------------------
    Provide feedback to assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: 
    
    >>>>>>>> NO HUMAN INPUT RECEIVED.
    
    >>>>>>>> USING AUTO REPLY...
    
    >>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is python)...
    execute_code was called without specifying a value for use_docker. Since the python docker package is not available, code will be run natively. Note: this fallback behavior is subject to change
    user_proxy (to assistant):
    
    exitcode: 0 (execution succeeded)
    Code output: 
    02:20 PM
    
    
    --------------------------------------------------------------------------------
    assistant (to user_proxy):
    
    It looks like the code you provided ran successfully and returned the current time in a 12-hour format with the AM/PM designation. Here's the output:
    
    02:20 PM
    
    If you have any other questions or need further assistance, feel free to ask!
    
    --------------------------------------------------------------------------------
    Provide feedback to assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: exit
    
    
    copy

[AI SDK](/docs/advanced/aisdk)[Okta SSO](/docs/advanced/okta)

![Footer Logo](/_next/static/media/footer_logo.b3e9d8d3.svg)

![SOC 2
Certified](https://static.sprinto.com/_next/static/images/framework/soc2.png)![ISO
27001
Certified](https://static.sprinto.com/_next/static/images/framework/iso-27001.png)

Have questions or need a custom solution?

[Contact Sales](/contact-sales)

Company

[Pricing](/pricing)

[Docs](/docs)

[Compare](/compare)

[DeepStart](/deepstart)

[About](/about_us)

[Careers](https://jobs.gem.com/deep-infra)

[Contact us](/contact-sales)

[Trust Center](https://trust.deepinfra.com)

[DeepGPT](https://deepgpt.com)

Latest Models

[moonshotai/Kimi-K2-Instruct-0905](/moonshotai/Kimi-K2-Instruct-0905)[anthropic/claude-3-7-sonnet-
latest](/anthropic/claude-3-7-sonnet-latest)[deepseek-
ai/DeepSeek-V3.2-Exp](/deepseek-ai/DeepSeek-V3.2-Exp)[deepseek-
ai/DeepSeek-V3.1](/deepseek-ai/DeepSeek-V3.1)[zai-org/GLM-4.6](/zai-
org/GLM-4.6)

Featured Models

[Qwen/Qwen3-Coder-480B-A35B-Instruct](/Qwen/Qwen3-Coder-480B-A35B-Instruct)[meta-
llama/Llama-3.3-70B-Instruct-Turbo](/meta-llama/Llama-3.3-70B-Instruct-
Turbo)[MiniMaxAI/MiniMax-M2](/MiniMaxAI/MiniMax-M2)[Qwen/Qwen3-235B-A22B-Instruct-2507](/Qwen/Qwen3-235B-A22B-Instruct-2507)[deepseek-
ai/DeepSeek-R1-Distill-Llama-70B](/deepseek-ai/DeepSeek-R1-Distill-Llama-70B)

![Built With Love in Palo Alto](/_next/static/media/love.ce60156e.svg)

[](https://linkedin.com/company/deep-
infra)[](https://x.com/DeepInfra)[](https://github.com/DeepInfra)[](https://discord.gg/x88dCvhqYq)

© 2026 Deep Infra. All rights reserved.

[Privacy Policy](/privacy)[Terms of Service](/terms)

