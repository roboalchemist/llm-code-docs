# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/dstack/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/dstack.md "Edit this page")

# dstack[¶](#dstack "Permanent link")

[![vLLM_plus_dstack](https://i.ibb.co/71kx6hW/vllm-dstack.png)](https://i.ibb.co/71kx6hW/vllm-dstack.png)

vLLM can be run on a cloud based GPU machine with [dstack](https://dstack.ai/), an open-source framework for running LLMs on any cloud. This tutorial assumes that you have already configured credentials, gateway, and GPU quotas on your cloud environment.

To install dstack client, run:

    pip install dstack[all]
    dstack server

Next, to configure your dstack project, run:

    mkdir -p vllm-dstack
    cd vllm-dstack
    dstack init

Next, to provision a VM instance with LLM of your choice (`NousResearch/Llama-2-7b-chat-hf` for this example), create the following `serve.dstack.yml` file for the dstack `Service`:

Config

    type: service

    python: "3.11"
    env:
        - MODEL=NousResearch/Llama-2-7b-chat-hf
    port: 8000
    resources:
        gpu: 24GB
    commands:
        - pip install vllm
        - vllm serve $MODEL --port 8000
    model:
        format: openai
        type: chat
        name: NousResearch/Llama-2-7b-chat-hf

Then, run the following CLI for provisioning:

Command

    $ dstack run . -f serve.dstack.yml

    ⠸ Getting run plan...
    Configuration  serve.dstack.yml
    Project        deep-diver-main
    User           deep-diver
    Min resources  2..xCPU, 8GB.., 1xGPU (24GB)
    Max price      -
    Max duration   -
    Spot policy    auto
    Retry policy   no

    #  BACKEND  REGION       INSTANCE       RESOURCES                               SPOT  PRICE
    1  gcp   us-central1  g2-standard-4  4xCPU, 16GB, 1xL4 (24GB), 100GB (disk)  yes   $0.223804
    2  gcp   us-east1     g2-standard-4  4xCPU, 16GB, 1xL4 (24GB), 100GB (disk)  yes   $0.223804
    3  gcp   us-west1     g2-standard-4  4xCPU, 16GB, 1xL4 (24GB), 100GB (disk)  yes   $0.223804
        ...
    Shown 3 of 193 offers, $5.876 max

    Continue? [y/n]: y
    ⠙ Submitting run...
    ⠏ Launching spicy-treefrog-1 (pulling)
    spicy-treefrog-1 provisioning completed (running)
    Service is published at ...

After the provisioning, you can interact with the model by using the OpenAI SDK:

Code

    from openai import OpenAI

    client = OpenAI(
        base_url="https://gateway.<gateway domain>",
        api_key="<YOUR-DSTACK-SERVER-ACCESS-TOKEN>",
    )

    completion = client.chat.completions.create(
        model="NousResearch/Llama-2-7b-chat-hf",
        messages=[
            
        ],
    )

    print(completion.choices[0].message.content)

Note

dstack automatically handles authentication on the gateway using dstack\'s tokens. Meanwhile, if you don\'t want to configure a gateway, you can provision dstack `Task` instead of `Service`. The `Task` is for development purpose only. If you want to know more about hands-on materials how to serve vLLM using dstack, check out [this repository](https://github.com/dstackai/dstack-examples/tree/main/deployment/vllm)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 14, 2025] ]