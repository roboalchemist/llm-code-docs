# Cancel a job
curl -X POST https://api.mistral.ai/v1/fine_tuning/jobs/<jobid>/cancel \
--header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>

</Tabs>

## Use a fine-tuned model
When a fine-tuned job is finished, you will be able to see the fine-tuned model name via `retrieved_jobs.fine_tuned_model`.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
classifier_response = client.classifiers.classify(
    model=retrieved_job.fine_tuned_model,
    inputs=["It's nice", "It's terrible", "Why not"],
)
```

Use `classify_chat` to classify chats and multiturn interactions.

  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
const classifierResponse = await client.classifiers.classify({
    model: retrievedJob.fine_tuned_model,
    inputs: ["It's nice", "It's terrible", "Why not"],
})
```

Use `classifyChat` to classify chats and multiturn interactions.

  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl "https://api.mistral.ai/v1/classifications" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
    "model": "ft:classifier:ministral-3b-latest:XXX:20250401:XXX",
    "input": ["It's nice", "It's terrible", "Why not"]
  }'
```
  </TabItem>

</Tabs>

## Delete a fine-tuned model

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
client.models.delete(model_id=retrieved_job.fine_tuned_model)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
await client.models.delete({modelId:retrieved_job.fine_tuned_model})
```

  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location --request DELETE 'https://api.mistral.ai/v1/models/ft:classifier:ministral-3b-latest:XXX:20250401:XXX' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>

</Tabs>

## Cookbooks

Explore our guides and [cookbooks](https://github.com/mistralai/cookbook) leveraging the Classifier Factory:

- [Intent Classification](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/intent_classification.ipynb): Creating a single-target, single-label, intent classification model to predict user actions and improve customer interactions.
- [Moderation Classifier](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/moderation_classifier.ipynb): Build a single-target, multi-label, simple moderation model to label public comments.
- [Product Classification](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/product_classification.ipynb): Create a multi-target, single-label and multi-label, food classification model to categorize dishes and their country of origin and compare to classic LLM solutions, enhancing recipe recommendations and dietary planning.

## FAQ

**Q: Which models can we fine-tune to create our own classifiers?**
**A:** Currently, the classifier factory supports `ministral-3b`.

**Q: Where can I find the pricing?**
**A:** You can find it on our [pricing page](https://mistral.ai/pricing#api-pricing) in the "fine-tunable models" section of our API Pricing.


[Fine-tuning Overview]
Source: https://docs.mistral.ai/docs/capabilities/finetuning

:::warning[ ]
Every fine-tuning job comes with a minimum fee of $4, and there's a monthly storage fee of $2 for each model. For more detailed pricing information, please visit our [pricing page](https://mistral.ai/technology/#pricing). 
:::

## Fine-tuning Basics

### Fine-tuning vs. Prompting 

When deciding whether to use prompt engineering or fine-tuning for an AI model, it can be difficult to determine which method is best. It's generally recommended to start with prompt engineering, as it's faster and less resource-intensive. To help you choose the right approach, here are the key benefits of prompting and fine-tuning:

- **Benefits of Prompting**
    - A generic model can work out of the box (the task can be described in a zero shot fashion)
    - Does not require any fine-tuning data or training to work
    - Can easily be updated for new workflows and prototyping
  
  Check out our [prompting guide](https://docs.mistral.ai/guides/prompting_capabilities/) to explore various capabilities of Mistral models. 

- **Benefits of Fine-tuning**
    - Works significantly better than prompting
    - Typically works better than a larger model (faster and cheaper because it doesn't require a very long prompt)
    - Provides a better alignment with the task of interest because it has been specifically trained on these tasks 
    - Can be used to teach new facts and information to the model (such as advanced tools or complicated workflows)

### Common use cases

Fine-tuning has a wide range of use cases, some of which include:
- Customizing the model to generate responses in a specific format and tone
- Specializing the model for a specific topic or domain to improve its performance on domain-specific tasks
- Improving the model through distillation from a stronger and more powerful model by training it to mimic the behavior of the larger model 
- Enhancing the model’s performance by mimicking the behavior of a model with a complex prompt, but without the need for the actual prompt, thereby saving tokens, and reducing associated costs
- Reducing cost and latency by using a small yet efficient fine-tuned model

## Fine-tuning Services
- [Text & Vision General Fine-tuning](../text_vision_finetuning):
    - **SFT**: Supervised Fine-tuning, the most common fine-tuning method to teach the model knowledge and how to follow instructions.
- [Classifier Factory](../classifier_factory): A tool to finetune and create classifier specific models from a dataset of text.


[Text & Vision Fine-tuning]
Source: https://docs.mistral.ai/docs/capabilities/finetuning/text-vision-finetuning

Fine-tuning allows you to tailor a pre-trained language model to your specific needs by training it on your dataset. This guide explains how to fine-tune text and vision models, from preparing your data to training, whether you aim to improve domain-specific understanding or adapt to a unique conversational style.

:::tip[ ]
For detailed end-to-end fine-tuning examples and FAQ, check out our [fine-tuning guide](../../../guides/finetuning).
:::

You can both finetune directly in [la plateforme](https://console.mistral.ai/build/finetuned-models) or via our API.

## Dataset Format

Data must be stored in JSON Lines (`.jsonl`) files, which allow storing multiple JSON objects, each on a new line.

SFT Datasets should follow an instruction-following format representing a user-assistant conversation. Each JSON data sample should either consist of only user and assistant messages or include function-calling logic.

### 1. Default Instruct

Conversational data between user and assistant, which can be one-turn or multi-turn. 

#### Text only template

```json
{
    "messages": [
        {
            "role": "user",
            "content": "User interaction n°1"
        },
        {
            "role": "assistant",
            "content": "Bot interaction n°1"
        },
        {
            "role": "user",
            "content": "User interaction n°2"
        },
        {
            "role": "assistant",
            "content": "Bot interaction n°2"
        }
    ]
}
```

Note that the files must be in JSONL format, meaning every JSON object must be flattened into a single line, and each JSON object is on a new line.
<details>

<summary><b>Raw `.jsonl` file example.</b></summary>

```json
{"messages": [{"role": "user","content": "..."},{"role": "assistant","content": "..."},...]}
{"messages": [{"role": "user","content": "..."},{"role": "assistant","content": "..."},...]}
{"messages": [{"role": "user","content": "..."},{"role": "assistant","content": "..."},...]}
{"messages": [{"role": "user","content": "..."},{"role": "assistant","content": "..."},...]}
...
```

</details>

- Conversational data must be stored under the `"messages"` key as a list.
- Each list item is a dictionary containing the `"content"` and `"role"` keys. `"role"` is a string: `"system"`, `"user"`, `"assistant"` or `"tool"`.
- Loss computation is performed only on tokens corresponding to assistant messages (`"role" == "assistant"`).

While text-only fine-tuning covers multiple use cases, you can also fine-tune the vision capabilities of our models. This allows you to create models that can understand and generate responses based on both text and image inputs.

#### Vision template

```json
{
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type":"image_url",
                    "image_url":"User Image URL, usually in a base64 format." // "data:image/jpeg;base64,{image_base64}"
                },
                {
                    "type":"text",
                    "text":"User interaction n°1"
                }
            ]
        },
        {
            "role": "assistant",
            "content": "Bot interaction n°1"
        },
        {
            "role": "user",
            "content": [
                {
                    "type":"image_url",
                    "image_url":"User Image URL, usually in a base64 format." // "data:image/jpeg;base64,{image_base64}"
                },
                {
                    "type":"text",
                    "text":"User interaction n°2"
                }
            ]
        },
        {
            "role": "assistant",
            "content": "Bot interaction n°2"
        }
    ]
}
```

- Content can be a list of dictionaries, each containing a `"type"` key and either `"text"` or `"image_url"` keys.

### 2. Function-calling Instruct

Conversational data with tool usage. Example:

```json
{
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant with access to the following functions to help the user. You can use the functions if needed."
        },
        {
            "role": "user",
            "content": "Can you help me generate an anagram of the word 'listen'?"
        },
        {
            "role": "assistant",
            "tool_calls": [
                {
                    "id": "TX92Jm8Zi",
                    "type": "function",
                    "function": {
                        "name": "generate_anagram",
                        "arguments": "{\"word\": \"listen\"}"
                    }
                }
            ]
        },
        {
            "role": "tool",
            "content": "{\"anagram\": \"silent\"}",
            "tool_call_id": "TX92Jm8Zi"
        },
        {
            "role": "assistant",
            "content": "The anagram of the word 'listen' is 'silent'."
        },
        {
            "role": "user",
            "content": "That's amazing! Can you generate an anagram for the word 'race'?"
        },
        {
            "role": "assistant",
            "tool_calls": [
                {
                    "id": "3XhQnxLsT",
                    "type": "function",
                    "function": {
                        "name": "generate_anagram",
                        "arguments": "{\"word\": \"race\"}"
                    }
                }
            ]
        }
    ],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "generate_anagram",
                "description": "Generate an anagram of a given word",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "word": {
                            "type": "string",
                            "description": "The word to generate an anagram of"
                        }
                    },
                    "required": ["word"]
                }
            }
        }
    ]
}
```

- Conversational data must be stored under the `"messages"` key as a list.
- Each message is a dictionary containing the `"role"` and `"content"` or `"tool_calls"` keys. `"role"` should be one of `"system"`, `"user"`, `"assistant"` or `"tool"`.
- Only messages of type `"assistant"` can have a `"tool_calls"` key, representing the assistant performing a call to an available tool.
- An assistant message with a `"tool_calls"` key cannot have a `"content"` key and must be followed by a `"tool"` message, which in turn must be followed by another assistant message.
- The `"tool_call_id"` of tool messages must match the `"id"` of at least one of the previous assistant messages.
- Both `"id"` and `"tool_call_id"` are randomly generated strings of exactly 9 characters. We recommend generating these automatically in a data preparation script as done [here](https://github.com/mistralai/mistral-finetune/blob/208b25c0f7299bb78d06cea25b82adee03834319/utils/reformat_data_glaive.py#L74).
- The `"tools"` key must include definitions of all tools used in the conversation.
- Loss computation is performed only on tokens corresponding to assistant messages (`"role" == "assistant"`).

## Upload a file
Once you have the data file with the right format,
you can upload the data file to the Mistral Client,
making them available for use in fine-tuning jobs.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
from mistralai import Mistral


api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)

training_data = client.files.upload(
    file={
        "file_name": "training_file.jsonl",
        "content": open("training_file.jsonl", "rb"),
    }
)

validation_data = client.files.upload(
    file={
        "file_name": "validation_file.jsonl",
        "content": open("validation_file.jsonl", "rb"),
    }
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript


const apiKey = process.env.MISTRAL_API_KEY;

const client = new Mistral({apiKey: apiKey});

const training_file = fs.readFileSync('training_file.jsonl');
const training_data = await client.files.upload({
    file: {
        fileName: "training_file.jsonl",
        content: training_file,
    }
});

const validation_file = fs.readFileSync('validation_file.jsonl');
const validation_data = await client.files.upload({
    file: {
        fileName: "validation_file.jsonl",
        content: validation_file,
    }
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl https://api.mistral.ai/v1/files \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -F purpose="fine-tune" \
  -F file="@training_file.jsonl"

curl https://api.mistral.ai/v1/files \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -F purpose="fine-tune" \
  -F file="@validation_file.jsonl"
```
  </TabItem>

</Tabs>

## Create a fine-tuning job
The next step is to create a fine-tuning job. 
- model: the specific model you would like to fine-tune. The choices are:
  - Text Only:
    - `open-mistral-7b`
    - `mistral-small-latest`
    - `codestral-latest`
    - `open-mistral-nemo`
    - `mistral-large-latest`
    - `ministral-8b-latest`
    - `ministral-3b-latest`
  - Vision:
    - `pixtral-12b-latest`
- training_files: a collection of training file IDs, which can consist of a single file or multiple files
- validation_files: a collection of validation file IDs, which can consist of a single file or multiple files
- hyperparameters:  two adjustable hyperparameters, "training_steps" and "learning_rate", that users can modify.
- auto_start:
    - `auto_start=True`: Your job will be launched immediately after validation.
    - `auto_start=False` (default): You can manually start the training after validation by sending a POST request to `/fine_tuning/jobs/<uuid>/start`.
- integrations: external integrations we support such as Weights and Biases for metrics tracking during training.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python