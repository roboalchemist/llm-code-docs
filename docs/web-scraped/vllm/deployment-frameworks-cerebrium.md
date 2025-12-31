# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/cerebrium/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/cerebrium.md "Edit this page")

# Cerebrium[¶](#cerebrium "Permanent link")

[![vLLM_plus_cerebrium](https://i.ibb.co/hHcScTT/Screenshot-2024-06-13-at-10-14-54.png)](https://i.ibb.co/hHcScTT/Screenshot-2024-06-13-at-10-14-54.png)

vLLM can be run on a cloud based GPU machine with [Cerebrium](https://www.cerebrium.ai/), a serverless AI infrastructure platform that makes it easier for companies to build and deploy AI based applications.

To install the Cerebrium client, run:

    pip install cerebrium
    cerebrium login

Next, create your Cerebrium project, run:

    cerebrium init vllm-project

Next, to install the required packages, add the following to your cerebrium.toml:

    [cerebrium.deployment]
    docker_base_image_url = "nvidia/cuda:12.1.1-runtime-ubuntu22.04"

    [cerebrium.dependencies.pip]
    vllm = "latest"

Next, let us add our code to handle inference for the LLM of your choice (`mistralai/Mistral-7B-Instruct-v0.1` for this example), add the following code to your `main.py`:

Code

    from vllm import LLM, SamplingParams

    llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.1")

    def run(prompts: list[str], temperature: float = 0.8, top_p: float = 0.95):

        sampling_params = SamplingParams(temperature=temperature, top_p=top_p)
        outputs = llm.generate(prompts, sampling_params)

        # Print the outputs.
        results = []
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            results.append()

        return 

Then, run the following code to deploy it to the cloud:

    cerebrium deploy

If successful, you should be returned a CURL command that you can call inference against. Just remember to end the url with the function name you are calling (in our case`/run`)

Command

    curl -X POST https://api.cortex.cerebrium.ai/v4/p-xxxxxx/vllm/run \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <JWT TOKEN>' \
    --data ''

You should get a response like:

Response

    ,
                ,
                ,
                
            ]
        },
        "run_time_ms": 152.53663063049316
    }

You now have an autoscaling endpoint where you only pay for the compute you use!

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 14, 2025] ]