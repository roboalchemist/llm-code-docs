# Initialize the model
llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.3", dtype="bfloat16", max_model_len=20000, gpu_memory_utilization=0.9)

```

We need to add our Hugging Face token to our [Cerebrium Secrets](https://docs.cerebrium.ai/cerebrium/environments/using-secrets) since using the Mistral model requires authentication. Please make sure the Huggingface token you added, has <b>WRITE</b> permissions. On first deploy, it will download the model and store it on disk therefore for subsequent calls it will load the model from disk.

Add the following to your main.py:

```python
def run(prompt: str, temperature: float = 0.8, top_p: float = 0.75, top_k: int = 40, max_tokens: int = 256, frequency_penalty: int = 1):
  
    sampling_params = SamplingParams(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty
    )

    outputs = llm.generate([item.prompt], sampling_params)

    generated_text = []
    for output in outputs:
        generated_text.append(output.outputs[0].text)

    return {"result": generated_text}
```

Every function in Cerebrium is callable through and API endpoint. Code at the top most layer (ie: not in a function) is instantiated only when the container is spun up the first time so for subsequent calls, it will simply run the code defined in the function you call.

Our final main.py should look like this:

```python
from vllm import LLM, SamplingParams
from huggingface_hub import login
from cerebrium import get_secret