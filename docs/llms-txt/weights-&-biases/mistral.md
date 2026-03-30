# Source: https://docs.wandb.ai/weave/guides/integrations/mistral.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# MistralAI

> Track and monitor MistralAI model calls with Weave's automatic tracing for chat completions, function calling, and model interactions.

<a target="_blank" href="https://colab.research.google.com/github/wandb/examples/blob/master/weave/docs/quickstart_mistral.ipynb" aria-label="Open in Google Colab">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
</a>

Weave automatically tracks and logs LLM calls made via the [MistralAI Python library](https://github.com/mistralai/client-python).

> We support the new Mistral v1.0 SDK, check the migration guide [here](https://github.com/mistralai/client-python/blob/main/MIGRATION.md)

## Traces

It’s important to store traces of LLM applications in a central database, both during development and in production. You’ll use these traces for debugging, and as a dataset that will help you improve your application.

Weave will automatically capture traces for [mistralai](https://github.com/mistralai/client-python). You can use the library as usual, start by calling `weave.init()`:

```python lines theme={null}
import weave
weave.init("cheese_recommender")

# then use mistralai library as usual
import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

messages = [
    {
        "role": "user",
        "content": "What is the best French cheese?",
    },
]

chat_response = client.chat.complete(
    model=model,
    messages=messages,
)
```

Weave will now track and log all LLM calls made through the MistralAI library. You can view the traces in the Weave web interface.

[<img src="https://mintcdn.com/wb-21fd5541/S0cRiDzxeODX77LU/weave/guides/integrations/imgs/mistral_trace.png?fit=max&auto=format&n=S0cRiDzxeODX77LU&q=85&s=07dfcb2716e550e4af7544172b96dd72" alt="mistral_trace.png" width="3024" height="1468" data-path="weave/guides/integrations/imgs/mistral_trace.png" />](https://wandb.ai/capecape/mistralai_project/weave/calls)

## Wrapping with your own ops

Weave ops make results *reproducible* by automatically versioning code as you experiment, and they capture their inputs and outputs. Simply create a function decorated with [`@weave.op()`](/weave/guides/tracking/ops) that calls into [`mistralai.client.MistralClient.chat()`](https://docs.mistral.ai/capabilities/completion) and Weave will track the inputs and outputs for you. Let's see how we can do this for our cheese recommender:

```python lines {1} theme={null}
@weave.op()
def cheese_recommender(region:str, model:str) -> str:
    "Recommend the best cheese in a given region"
    
    messages = [
        {
            "role": "user",
            "content": f"What is the best cheese in {region}?",
        },
    ]

    chat_response = client.chat.complete(
        model=model,
        messages=messages,
    )
    return chat_response.choices[0].message.content

cheese_recommender(region="France", model="mistral-large-latest")
cheese_recommender(region="Spain", model="mistral-large-latest")
cheese_recommender(region="Netherlands", model="mistral-large-latest")
```

[<img src="https://mintcdn.com/wb-21fd5541/S0cRiDzxeODX77LU/weave/guides/integrations/imgs/mistral_ops.png?fit=max&auto=format&n=S0cRiDzxeODX77LU&q=85&s=5ffde09f722987a36b7e1d9ce86e4f74" alt="mistral_ops.png" width="2877" height="1080" data-path="weave/guides/integrations/imgs/mistral_ops.png" />](https://wandb.ai/capecape/mistralai_project/weave/calls)

## Create a `Model` for easier experimentation

Organizing experimentation is difficult when there are many moving pieces. By using the [`Model`](/weave/guides/core-types/models) class, you can capture and organize the experimental details of your app like your system prompt or the model you're using. This helps organize and compare different iterations of your app.

In addition to versioning code and capturing inputs/outputs, [`Model`](/weave/guides/core-types/models)s capture structured parameters that control your application’s behavior, making it easy to find what parameters worked best. You can also use Weave Models with `serve`, and [`Evaluation`](/weave/guides/core-types/evaluations)s.

In the example below, you can experiment with `model` and `country`. Every time you change one of these, you'll get a new *version* of `CheeseRecommender`.

```python lines theme={null}
import weave
from mistralai import Mistral

weave.init("mistralai_project")

class CheeseRecommender(weave.Model): # Change to `weave.Model`
    model: str
    temperature: float

    @weave.op()
    def predict(self, region:str) -> str: # Change to `predict`
        "Recommend the best cheese in a given region"
        
        client = Mistral(api_key=api_key)

        messages = [
            {
                "role": "user",
                "content": f"What is the best cheese in {region}?",
            },
        ]

        chat_response = client.chat.complete(
            model=model,
            messages=messages,
            temperature=self.temperature
        )
        return chat_response.choices[0].message.content

cheese_model = CheeseRecommender(
    model="mistral-medium-latest",
    temperature=0.0
    )
result = cheese_model.predict(region="France")
print(result)
```

[<img src="https://mintcdn.com/wb-21fd5541/S0cRiDzxeODX77LU/weave/guides/integrations/imgs/mistral_model.png?fit=max&auto=format&n=S0cRiDzxeODX77LU&q=85&s=d85e760d2b7cad2b78ebc80477afea89" alt="mistral_model.png" width="3010" height="1536" data-path="weave/guides/integrations/imgs/mistral_model.png" />](https://wandb.ai/capecape/mistralai_project/weave/models)
