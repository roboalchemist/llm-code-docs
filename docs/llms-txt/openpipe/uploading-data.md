# Source: https://docs.openpipe.ai/features/datasets/uploading-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Uploading Data

>  Upload external data to kickstart your fine-tuning process. Use the OpenAI chat fine-tuning format.

Upload a JSONL file populated with a list of training examples.

<Frame><img src="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/uploading-data.png?fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=dc4d74b4e77ace8c4e631b0e2d0304ec" alt="" data-og-width="2330" width="2330" data-og-height="1470" height="1470" data-path="images/features/uploading-data.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/uploading-data.png?w=280&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=156e5d64c9d294cf6a8c9099ad291bb0 280w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/uploading-data.png?w=560&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=662910dfa2244c953868c1c496390e7b 560w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/uploading-data.png?w=840&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=bb115b01d93d68b2c2f7216ada3babec 840w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/uploading-data.png?w=1100&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=c0feb5824b915948f23c5df6a77f48a8 1100w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/uploading-data.png?w=1650&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=e2444ee3e1e9958665905a22749931a3 1650w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/uploading-data.png?w=2500&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=959e108ef25ac9514e5263b93fb74281 2500w" /></Frame>

Each line of the file should be compatible with the OpenAI [chat format](https://platform.openai.com/docs/api-reference/chat/object), with additional optional fields.

### OpenAI Fields

* **`messages`: Required** - Formatted as a list of OpenAI [chat completion messages](https://platform.openai.com/docs/guides/gpt/chat-completions-api). The list should end with an assistant message.
* **`tools`: Optional** - An array of tools (functions) available for the model to call. For more information read OpenAI's [function calling docs](https://platform.openai.com/docs/guides/function-calling).
* **`tool_choice`: Optional** - You can set this to indicate that the model should be required to call the given tool. For more information read OpenAI's [function calling docs](https://platform.openai.com/docs/guides/function-calling).

#### Deprecated

* **`functions`: Deprecated | Optional** - An array of functions available for the model to call.
* **`function_call`: Deprecated | Optional** - You can set this to indicate that the model should be required to call the given function.

You can include other parameters from the OpenAI chat completion input format (eg. temperature), but they will be ignored since they aren't relevant for training.

### Additional Fields

* **`split`: Optional** - One of "TRAIN" or "TEST". If you don't set this field we'll automatically divide your inputs into train and test splits with a target ratio of 90:10.
* **`rejected_message`: Optional** - Add a rejected output for entries on which you want to perform direct preference optimization (DPO). You can find more information about that here: [Direct Preference Optimization](/features/dpo/overview)
* **`metadata`: Optional** - A string=>string dictionary of any additional information you want to associate with an entry. This can be useful for tracking information like prompt IDs.

### Example

```jsonl  theme={null}
...
{"messages":[{"role":"system","content":"You are a helpful assistant"},{"role":"user","content":"What is the capital of Tasmania?"},{"role":"assistant","content":"Hobart"}], "rejected_message":{"role": "assistant", "content": "Paris"}, "split": "TRAIN", "metadata": {"prompt_id": "capital_cities", "any_key": "any_value"}}
{"messages":[{"role":"system","content":"You are a helpful assistant"},{"role":"user","content":"What is the capital of Sweden?"},{"role":"assistant","content":"Stockholm"}], "rejected_message":{"role": "assistant", "content": "London"}, "split": "TEST", "metadata": {"prompt_id": "capital_cities", "any_key": "any_value"}}
...
```
