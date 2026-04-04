# Source: https://docs.openpipe.ai/features/datasets/exporting-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting Data

>  Export your past requests as a JSONL file in their raw form.

## Dataset export

After you've collected, filtered, and transformed your dataset entries for fine-tuning, you can export them as a JSONL file.

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/datasets/exporting-dataset-entries.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=9088bdf4ba8b33055ef267f2f94808fa" alt="" data-og-width="2262" width="2262" data-og-height="684" height="684" data-path="images/features/datasets/exporting-dataset-entries.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/datasets/exporting-dataset-entries.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=6dc1d8e49e863ebce517c8c525445658 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/datasets/exporting-dataset-entries.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=3744a3ba0c4b6461fc8e65d5d982402d 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/datasets/exporting-dataset-entries.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=a8094b06f4ab20b3b532b4ec8a95b473 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/datasets/exporting-dataset-entries.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=86b2a7f6d81c97d05f79f12b7a2ce6cd 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/datasets/exporting-dataset-entries.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=212af45f04057266001f01848fb4afa9 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/datasets/exporting-dataset-entries.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=5e580096a1fb8180d001a174bed749fe 2500w" /></Frame>

### Fields

* **`messages`:** The complete chat history.
* **`tools`:** The tools provided to the model.
* **`tool_choice`:** The tool required for the model to use.
* **`split`:** The train/test split to which the entry belongs.

### Example

```jsonl  theme={null}
{"messages":[{"role":"system","content":"You are a helpful assistant"},{"role":"user","content":"What is the capital of Tasmania?"},{"role":"assistant","content":null,"tool_calls":[{"id":"","type":"function","function":{"name":"identify_capital","arguments":"{\"capital\":\"Hobart\"}"}}]}],"tools":[{"type":"function","function":{"name":"identify_capital","parameters":{"type":"object","properties":{"capital":{"type":"string"}}}}}]}
{"messages":[{"role":"system","content":"You are a helpful assistant"},{"role":"user","content":"What is the capital of Sweden?"},{"role":"assistant","content":null,"tool_calls":[{"id":"","type":"function","function":{"name":"identify_capital","arguments":"{\"capital\":\"Stockholm\"}"}}]}],"tools":[{"type":"function","function":{"name":"identify_capital","parameters":{"type":"object","properties":{"capital":{"type":"string"}}}}}]}
```
