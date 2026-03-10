# This function uses nested loops to generate all possible combinations of segments of lengths `a`, `b`, and `c`, respectively. For each combination, it checks if the total length of the segments is equal to `n`, and if so, it updates the maximum number of segments found so far. The function returns the maximum number of segments that can be formed from `n`.
```

Here is another example of Mistral Large writing a function for computing square roots using the babylonian method. 

**Prompt:**
```
You are an expert Python programmer, and here is your task: Write a function for computing square roots using the babylonian method. Your code should pass these tests:

assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)
```
**Output:**
```python
def babylonian_squareroot(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;"
```

- **Multi-lingual tasks**

In addition to its exceptional performance in complex reasoning tasks and coding tasks, Mistral Large also demonstrates superior capabilities in handling multi-lingual tasks. Mistral-large has been specifically trained to understand and generate text in multiple languages, especially in French, German, Spanish and Italian. Mistral Large can be especially valuable for businesses and users that need to communicate in multiple languages.

**Prompt:**
```
Lequel est le plus lourd une livre de fer ou un kilogramme de plume
```
**Output:**
```
Un kilogramme de plumes est plus lourd qu'une livre de fer.

Pour comprendre cela, il est important de se rappeler que :

1. Une livre (lb) est une unité de mesure de masse principalement utilisée aux États-Unis et dans d'autres systèmes de mesure impériaux, tandis qu'un kilogramme (kg) est l'unité de base de masse dans le système international d'unités (SI).
2. 1 kilogramme est approximativement égal à 2,2 livres.

Donc, un kilogramme de plumes est plus lourd qu'une livre de fer, car il correspond à environ 2,2 livres de plumes.
```


[Models Overview]
Source: https://docs.mistral.ai/docs/getting-started/models/overview

Mistral provides two types of models: open models and premier models. 

:::note[ ]
- For API pricing details, please visit our [pricing page](https://mistral.ai/pricing#api-pricing). 
- If you are interested in purchasing a commercial license for our models, please [contact our team](https://mistral.ai/en/contact).
:::

### Premier models

| Model               | Weight availability|Available via API| Description | Max Tokens| API Endpoints|Version|
|--------------------|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
| Mistral Medium 3 | | :heavy_check_mark: | Our frontier-class multimodal model released May 2025. Learn more in our [blog post](https://mistral.ai/news/mistral-medium-3/) | 128k | `mistral-medium-2505` | 25.05|
| Magistral Medium 1.1 | | :heavy_check_mark: | Our frontier-class reasoning model released July 2025. | 40k | `magistral-medium-2507` | 25.07|
| Codestral 2508 | | :heavy_check_mark: | Our cutting-edge language model for coding released end of July 2025, Codestral specializes in low-latency, high-frequency tasks such as fill-in-the-middle (FIM), code correction and test generation. Learn more in our [blog post](https://mistral.ai/news/codestral-25-08/) | 256k  | `codestral-2508` | 25.08|
| Voxtral Mini Transcribe | | :heavy_check_mark: | An efficient audio input model, fine-tuned and optimized for transcription purposes only. | | `voxtral-mini-2507` via `audio/transcriptions` | 25.07|
| Devstral Medium | | :heavy_check_mark: | An enterprise grade text model, that excels at using tools to explore codebases, editing multiple files and power software engineering agents. Learn more in our [blog post](https://mistral.ai/news/devstral-2507) | 128k  | `devstral-medium-2507` | 25.07|
| Mistral OCR 2505 | | :heavy_check_mark: | Our OCR service powering our Document AI stack that enables our users to extract interleaved text and images |  | `mistral-ocr-2505` | 25.05|
| Magistral Medium 1 | | :heavy_check_mark: | Our first frontier-class reasoning model released June 2025. Learn more in our [blog post](https://mistral.ai/news/magistral/) | 40k | `magistral-medium-2506` | 25.06|
| Ministral 3B | | :heavy_check_mark: | World’s best edge model. Learn more in our [blog post](https://mistral.ai/news/ministraux/) | 128k  | `ministral-3b-2410` | 24.10|
| Ministral 8B | :heavy_check_mark: <br/> [Mistral Research License](https://mistral.ai/licenses/MRL-0.1.md)| :heavy_check_mark: |Powerful edge model with extremely high performance/price ratio. Learn more in our [blog post](https://mistral.ai/news/ministraux/) | 128k  | `ministral-8b-2410` | 24.10|
| Codestral 2501 | | :heavy_check_mark: | Our cutting-edge language model for coding with the second version released January 2025, Codestral specializes in low-latency, high-frequency tasks such as fill-in-the-middle (FIM), code correction and test generation. Learn more in our [blog post](https://mistral.ai/news/codestral-2501/) | 256k  | `codestral-2501` | 25.01|
| Mistral Large 2.1 |:heavy_check_mark: <br/> [Mistral Research License](https://mistral.ai/licenses/MRL-0.1.md)| :heavy_check_mark: | Our top-tier large model for high-complexity tasks with the lastest version released November 2024. Learn more in our [blog post](https://mistral.ai/news/pixtral-large/) | 128k  | `mistral-large-2411` | 24.11|
| Pixtral Large |:heavy_check_mark: <br/> [Mistral Research License](https://mistral.ai/licenses/MRL-0.1.md)| :heavy_check_mark: | Our first frontier-class multimodal model released November 2024. Learn more in our [blog post](https://mistral.ai/news/pixtral-large/) | 128k  | `pixtral-large-2411` | 24.11|
| Mistral Small 2| :heavy_check_mark: <br/> [Mistral Research License](https://mistral.ai/licenses/MRL-0.1.md) | :heavy_check_mark: | Our updated small version, released September 2024. Learn more in our [blog post](https://mistral.ai/news/september-24-release) | 32k  | `mistral-small-2407` | 24.07|
| Mistral Embed | | :heavy_check_mark: | Our state-of-the-art semantic for extracting representation of text extracts | 8k  | `mistral-embed` | 23.12|
| Codestral Embed | | :heavy_check_mark: | Our state-of-the-art semantic for extracting representation of code extracts | 8k  | `codestral-embed` | 25.05|
| Mistral Moderation | | :heavy_check_mark: | Our moderation service that enables our users to detect harmful text content | 8k  | `mistral-moderation-2411` | 24.11|

### Open models

| Model               | Weight availability|Available via API| Description | Max Tokens| API Endpoints|Version|
|--------------------|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
| Magistral Small 1.1 | :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | Our small reasoning model released July 2025. | 40k | `magistral-small-2507` | 25.07|
| Voxtral Small | :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | Our first model with audio input capabilities for instruct use cases.  | 32k  | `voxtral-small-2507` | 25.07|
| Voxtral Mini | :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | A mini version of our first audio input model.  | 32k | `voxtral-mini-2507` | 25.07|
| Mistral Small 3.2 | :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | An update to our previous small model, released June 2025. | 128k  | `mistral-small-2506` | 25.06|
| Magistral Small 1 | :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | Our first small reasoning model released June 2025. Learn more in our [blog post](https://mistral.ai/news/magistral/) | 40k | `magistral-small-2506` | 25.06|
| Devstral Small 1.1 | :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | An update to our open source model that excels at using tools to explore codebases, editing multiple files and power software engineering agents. Learn more in our [blog post](https://mistral.ai/news/devstral-2507) | 128k  | `devstral-small-2507` | 25.07|
| Mistral Small 3.1 | :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | A new leader in the small models category with image understanding capabilities, released March 2025. Learn more in our [blog post](https://mistral.ai/news/mistral-small-3-1/) | 128k  | `mistral-small-2503` | 25.03|
| Mistral Small 3| :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | A new leader in the small models category, released January 2025. Learn more in our [blog post](https://mistral.ai/news/mistral-small-3) | 32k  | `mistral-small-2501` | 25.01|
| Devstral Small 1| :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | A 24B text model, open source model that excels at using tools to explore codebases, editing multiple files and power software engineering agents. Learn more in our [blog post](https://mistral.ai/news/devstral/) | 128k  | `devstral-small-2505` | 25.05|
| Pixtral 12B | :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | A 12B model with image understanding capabilities in addition to text. Learn more in our [blog post](https://mistral.ai/news/pixtral-12b/)| 128k  | `pixtral-12b-2409` | 24.09|
| Mistral Nemo 12B | :heavy_check_mark: <br/> Apache2 | :heavy_check_mark: | Our best multilingual open source model released July 2024. Learn more in our [blog post](https://mistral.ai/news/mistral-nemo/) | 128k  | `open-mistral-nemo`| 24.07|

## API versioning 

Mistral AI API are versions with specific release dates. 
To prevent any disruptions due to model updates and breaking changes, 
it is recommended to use the dated versions of the Mistral AI API. 
Additionally, be prepared for the deprecation of certain endpoints in the coming months.

Here are the details of the available versions:
- `magistral-medium-latest`: currently points to `magistral-medium-2507`. 
- `magistral-small-latest`: currently points to `magistral-small-2507`. 
- `mistral-medium-latest`: currently points to `mistral-medium-2505`. 
- `mistral-large-latest`: currently points to `mistral-large-2411`. 
- `pixtral-large-latest`: currently points to `pixtral-large-2411`. 
- `mistral-moderation-latest`: currently points to `mistral-moderation-2411`.
- `ministral-3b-latest`: currently points to `ministral-3b-2410`.
- `ministral-8b-latest`: currently points to `ministral-8b-2410`.
- `open-mistral-nemo`: currently points to `open-mistral-nemo-2407`.
- `mistral-small-latest`: currently points to `mistral-small-2506`.
- `devstral-small-latest`: currently points to `devstral-small-2507`
- `devstral-medium-latest`: currently points to `devstral-medium-2507`
- `mistral-saba-latest`: currently points to `mistral-saba-2502`. 
- `codestral-latest`: currently points to `codestral-2508`.
- `mistral-ocr-latest`: currently points to `mistral-ocr-2505`.
- `voxtral-small-latest`: currently points to `voxtral-small-2507`.
- `voxtral-mini-latest`: currently points to `voxtral-mini-2507`.

## Model deprecation
### Overview
Our model offering is continuously refreshed with newer, better models. As part of this process, we deprecate and retire older models. This document provides information about which models are currently available, deprecated, or retired.

### Terminology
- Deprecation date: The date to mark the model as deprecated. When a model is deprecated, it continues to be available for use by customers with existing deployments until the model is retired. 
- Retirement date: The date to mark the model as retired. When a model is retired from la Plateforme, it is no longer available for use, and when prompted, it will return an error response.

### How to Prepare for Model Retirements and Version Upgrades
To prepare for model retirements and version upgrades, we recommend that customers evaluate their applications with the new models and versions and assess their behavior. We also recommend that customers update their applications to use the new models and versions before the retirement date

### Legacy models

| Model               | Weight availability|API Endpoints|Version|Deprecation date|Retirement date|Alternative model|
|--------------------|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
| Mistral 7B    | :heavy_check_mark: <br/> Apache2| `open-mistral-7b`| v0.3|2024/11/30|2025/03/30| `ministral-8b-latest`|
| Mixtral 8x7B  |:heavy_check_mark: <br/> Apache2| `open-mixtral-8x7b`| v0.1| 2024/11/30|2025/03/30| `mistral-small-latest`|
| Mixtral 8x22B  |:heavy_check_mark: <br/> Apache2| `open-mixtral-8x22b`| v0.1|2024/11/30|2025/03/30| `mistral-small-latest`|
| Mistral Medium 2312  |  | `mistral-medium-2312`| 23.12 |2024/11/30|2025/06/16|`mistral-medium-latest`|
| Mistral Small 2402|  | `mistral-small-2402` | 24.02|2024/11/30|2025/06/16| `mistral-small-latest`|
| Mistral Large 2402  | | `mistral-large-2402`| 24.02|2024/11/30|2025/06/16| `mistral-medium-latest` | 
| Mistral Large 2407  | :heavy_check_mark: <br/> [Mistral Research License](https://mistral.ai/licenses/MRL-0.1.md)  | `mistral-large-2407`| 24.02|2024/11/30|2025/03/30| `mistral-medium-latest`|
| Codestral 2405 |:heavy_check_mark: <br/> [Mistral Non-Production License](https://mistral.ai/licenses/MNPL-0.1.md) | `codestral-2405` | 24.05|2024/12/02|2025/06/16| `codestral-latest`|
| Mistral OCR 2503 | | `mistral-ocr-2503` | 25.03| 2025/06/10|2026/03/31| `mistral-ocr-latest`|
| Mistral Saba 2502 | | `mistral-saba-2502` | 25.02| 2025/06/10|2025/09/30| `mistral-small-latest`|
| Mathstral 7B | :heavy_check_mark: <br/> Apache2 |  | v0.1| || `magistral-small-latest`|
| Codestral Mamba | :heavy_check_mark: <br/> Apache2 |`open-codestral-mamba` | v0.1|2525/06/06 |2525/06/06| `codestral-latest`|


[Model weights]
Source: https://docs.mistral.ai/docs/getting-started/models/weights

We open-source both pre-trained models and instruction-tuned models. These models are not tuned for safety as we want to empower users to test and refine moderation based on their use cases. For safer models, follow our [guardrailing tutorial](/capabilities/guardrailing).

## License
- Mistral 7B, Mixtral 8x7B, Mixtral 8x22B, Codestral Mamba, Mathstral, Mistral Nemo, Pixtral 12B, Mistral Small, Magistral Small and Devstral Small are under [Apache 2 License](https://choosealicense.com/licenses/apache-2.0/), which permits their use without any constraints.
- Codestral is under [Mistral AI Non-Production (MNPL) License](https://mistral.ai/licences/MNPL-0.1.md).
- Ministral 8B, Mistral Large, and Pixtral Large are under [Mistral Research License](https://mistral.ai/licenses/MRL-0.1.md). 

:::note[ ]
If you are interested in purchasing a commercial license for our models, please [contact our team](https://mistral.ai/contact/)
:::

## Downloading

| Model               |Download links|Features|
|--------------------|:--------------------|:--------------------|
| Magistral-Small-2507  | [Hugging Face](https://huggingface.co/mistralai/Magistral-Small-2507)| - 128k vocabulary size <br/> - Supports v7 tekken.json tokenizer |
| Voxtral-Small-24B-2507  | [Hugging Face](https://huggingface.co/mistralai/Voxtral-Small-24B-2507)| - 128k vocabulary size <br/> - Supports v11 tekken.json tokenizer <br/> - Supports function calling <br/> - Supports audio |
| Voxtral-Mini-3B-2507  | [Hugging Face](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507)| - 128k vocabulary size <br/> - Supports v11 tekken.json tokenizer <br/> - Supports function calling <br/> - Supports audio |
| Devstral-Small-2507  | [Hugging Face](https://huggingface.co/mistralai/Devstral-Small-2507)| - 128k vocabulary size <br/> - Supports v7 tekken.json tokenizer <br/> - Supports function calling |
| Mistral-Small-Instruct-2506  | [Hugging Face](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506)| - 128k vocabulary size <br/> - Supports v11 tekken.json tokenizer <br/> - Supports function calling <br/> - Supports images |
| Magistral-Small-2506  | [Hugging Face](https://huggingface.co/mistralai/Magistral-Small-2506)| - 128k vocabulary size <br/> - Supports v7 tekken.json tokenizer |
| Devstral-Small-2505  | [Hugging Face](https://huggingface.co/mistralai/Devstral-Small-2505)| - 128k vocabulary size <br/> - Supports v7 tekken.json tokenizer <br/> - Supports function calling |
| Mistral-Small-Instruct-2503  | [Hugging Face](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)| - 128k vocabulary size <br/> - Supports v7 tekken.json tokenizer <br/> - Supports function calling <br/> - Supports images |
| Mistral-Small-Base-2503  | [Hugging Face](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Base-2503)| - 128k vocabulary size <br/> - Supports v7 tekken.json tokenizer <br/> - Supports function calling <br/> - Supports images |
| Mistral-Small-Instruct-2501  | [Hugging Face](https://huggingface.co/mistralai/Mistral-Small-Instruct-2501)| - 128k vocabulary size <br/> - Supports v7 tekken.json tokenizer <br/> - Supports function calling |
| Mistral-Small-Base-2501  | [Hugging Face](https://huggingface.co/mistralai/Mistral-Small-Base-2501)| - 128k vocabulary size <br/> - Supports v7 tekken.json tokenizer <br/> - Supports function calling |
| Pixtral-Large-Instruct-2411  | [Hugging Face](https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411)| - 32768 vocabulary size <br/> - Supports v7 tokenizer <br/> - Supports function calling <br/> - Supports images |
| Mistral-Large-Instruct-2411  | [Hugging Face](https://huggingface.co/mistralai/Mistral-Large-Instruct-2411)| - 32768 vocabulary size <br/> - Supports v7 tokenizer <br/> - Supports function calling |
| Ministral-8B-Instruct-2410 | [Hugging Face](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) | - 128k vocabulary size <br/> - Supports v3 tekken.json tokenizer <br/> - Supports function calling |
| Mistral-Small-Instruct-2409 | [Hugging Face](https://huggingface.co/mistralai/Mistral-Small-Instruct-2409) | - 32768 vocabulary size <br/> - Supports v3 Tokenizer <br/> - Supports function calling |
| Pixtral-2409 | [Hugging Face](https://huggingface.co/mistralai/Pixtral-12B-2409) | - 128k vocabulary size <br/> - Supports v3 tekken.json tokenizer <br/> - Supports function calling <br/> - Supports images |
| Mistral-Large-Instruct-2407  | [Hugging Face](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407) <br/> [raw_weights](https://models.mistralcdn.com/mistral-large-2407/mistral-large-instruct-2407.tar) (md5sum: `fc602155f9e39151fba81fcaab2fa7c4`)| - 32768 vocabulary size <br/> - Supports v3 Tokenizer <br/> - Supports function calling |
| Mistral-Nemo-Instruct-2407  | [Hugging Face](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) <br/> [raw_weights](https://models.mistralcdn.com/mistral-nemo-2407/mistral-nemo-instruct-2407.tar) (md5sum: `296fbdf911cb88e6f0be74cd04827fe7`) | - 128k vocabulary size <br/> - Supports v3 tekken.json tokenizer <br/> - Supports function calling |
| Mistral-Nemo-Base-2407  | [Hugging Face](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407) <br/> [raw_weights](https://models.mistralcdn.com/mistral-nemo-2407/mistral-nemo-base-2407.tar) (md5sum: `c5d079ac4b55fc1ae35f51f0a3c0eb83`) | - 128k vocabulary size <br/> - Supports v3 tekken.json tokenizer |  
| Mathstral-7B-v0.1  | [Hugging Face](https://huggingface.co/mistralai/mathstral-7B-v0.1) <br/> [raw_weights](https://models.mistralcdn.com/mathstral-7b-v0-1/mathstral-7B-v0.1.tar) (md5sum: `5f05443e94489c261462794b1016f10b`) | - 32768 vocabulary size <br/> - Supports v3 Tokenizer |
| Codestral-Mamba-7B-v0.1  | [Hugging Face](https://huggingface.co/mistralai/mamba-codestral-7B-v0.1) <br/> [raw_weights](https://models.mistralcdn.com/codestral-mamba-7b-v0-1/codestral-mamba-7B-v0.1.tar) (md5sum: `d3993e4024d1395910c55db0d11db163`) | - 32768 vocabulary size <br/> - Supports v3 Tokenizer |
| Codestral-22B-v0.1  | [Hugging Face](https://huggingface.co/mistralai/Codestral-22B-v0.1) <br/> [raw_weights](https://models.mistralcdn.com/codestral-22b-v0-1/codestral-22B-v0.1.tar) (md5sum: `1ea95d474a1d374b1d1b20a8e0159de3`) | - 32768 vocabulary size <br/> - Supports v3 Tokenizer |
| Mixtral-8x22B-v0.3  | [raw_weights](https://models.mistralcdn.com/mixtral-8x22b-v0-3/mixtral-8x22B-v0.3.tar) (md5sum: `a2fa75117174f87d1197e3a4eb50371a`) | - 32768 vocabulary size <br/> - Supports v3 Tokenizer |
| Mixtral-8x22B-Instruct-v0.1/ <br/> Mixtral-8x22B-Instruct-v0.3 | [Hugging Face](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) <br/> [raw_weights](https://models.mistralcdn.com/mixtral-8x22b-v0-3/mixtral-8x22B-Instruct-v0.3.tar) (md5sum: `471a02a6902706a2f1e44a693813855b`)|- 32768 vocabulary size |
| Mixtral-8x22B-v0.1  | [Hugging Face](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1) <br/> [raw_weights](magnet:?xt=urn:btih:9238b09245d0d8cd915be09927769d5f7584c1c9&dn=mixtral-8x22b&tr=udp%3A%2F%http://2Fopen.demonii.com%3A1337%2Fannounce&tr=http%3A%2F%https://t.co/OdtBUsbeV5%3A1337%2Fannounce) (md5sum: `0535902c85ddbb04d4bebbf4371c6341`) |- 32k vocabulary size |
| Mixtral-8x7B-Instruct-v0.1  | [Hugging Face](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) <br/> [raw_weights](https://models.mistralcdn.com/mixtral-8x7b-v0-1/Mixtral-8x7B-v0.1-Instruct.tar) (md5sum: `8e2d3930145dc43d3084396f49d38a3f`) |- 32k vocabulary size <br/> - Rope Theta = 1e6|
| Mixtral-8x7B-v0.1   | [Hugging Face](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) |- 32k vocabulary size <br/> - Rope Theta = 1e6|
| Mistral-7B-Instruct-v0.3  | [Hugging Face](https://huggingface.co/mistralai/Mistral-7B-v0.3) <br/> [raw_weights](https://models.mistralcdn.com/mistral-7b-v0-3/mistral-7B-v0.3.tar) (md5sum: `80b71fcb6416085bcb4efad86dfb4d52`) |- Extended vocabulary to 32768 <br/> - Supports v3 Tokenizer <br/> - Supports function calling|
| Mistral-7B-v0.3  | [Hugging Face](https://huggingface.co/mistralai/Mistral-7B-v0.3) <br/> [raw_weights](https://models.mistralcdn.com/mistral-7b-v0-3/mistral-7B-v0.3.tar) (md5sum: `0663b293810d7571dad25dae2f2a5806`) |- Extended vocabulary to 32768 <br/> |
| Mistral-7B-Instruct-v0.2  | [Hugging Face](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) <br/> [raw_weights](https://models.mistralcdn.com/mistral-7b-v0-2/Mistral-7B-v0.2-Instruct.tar) (md5sum: `fbae55bc038f12f010b4251326e73d39`) | - 32k vocabulary size <br/> - Rope Theta = 1e6 <br/> - No sliding window |
| Mistral-7B-Instruct-v0.1  | [Hugging Face](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) |- 32k vocabulary size <br/> - Rope Theta = 1e4 <br/> - With sliding window|
| Mistral-7B-v0.1  | [Hugging Face](https://huggingface.co/mistralai/Mistral-7B-v0.1) <br/> [raw_weights](https://models.mistralcdn.com/mistral-7b-v0-1/mistral-7B-v0.1.tar) (md5sum: `37dab53973db2d56b2da0a033a15307f`) |- 32k vocabulary size <br/> - Rope Theta = 1e4 <br/> - With sliding window|

## Sizes

| Name               | Number of parameters | Number of active parameters | Min. GPU RAM for inference (GB) |
|--------------------|:--------------------:|:---------------------------:|:-------------------------------:|
| Mistral-7B-v0.3    | 7.3B                 | 7.3B                        | 16                              |
| Mixtral-8x7B-v0.1  | 46.7B                  | 12.9B                         | 100                             |
| Mixtral-8x22B-v0.3  | 140.6B                  | 39.1B                         | 300                             |
| Codestral-22B-v0.1  | 22.2B | 22.2B | 60 |
| Codestral-Mamba-7B-v0.1  | 7.3B | 7.3B | 16 |
| Mathstral-7B-v0.1  | 7.3B | 7.3B | 16 |
| Mistral-Nemo-Instruct-2407  | 12B | 12B | 28 - bf16 <br/> 16 - fp8 |
| Mistral-Large-Instruct-2407  | 123B | 123B | 250 |
| Pixtral-2409 |  12B | 12B | 28 - bf16 <br/> 16 - fp8 |
| Mistral-Small-2409 | 22B | 22B | 60 |
| Ministral-8B-2410 | 8B | 8B | 24 |
| Mistral-Large-Instruct-2411  | 123B | 123B | 250 |
| Pixtral-Large-Instruct-2411  | 124B | 124B | 250 |
| Mistral-Small-Base-2501  | 24B | 24B | 60 |
| Mistral-Small-Instruct-2501  | 24B | 24B | 60 |
| Mistral-Small-Base-2503  | 24B | 24B | 60 |
| Mistral-Small-Instruct-2503  | 24B | 24B | 60 |
| Devstral-Small-2505  | 24B | 24B | 60 |
| Mistral-Small-Instruct-2506  | 24B | 24B | 60 |
| Devstral-Small-2507  | 24B | 24B | 60 |
| Voxtral-Small  | 24B | 24B | 60 |
| Voxtral-Mini  | 3B | 3B | 8 |

## How to run? 
Check out [mistral-inference](https://github.com/mistralai/mistral-inference/), a Python package for running our models. You can install `mistral-inference` by
```
pip install mistral-inference
``` 

To learn more about how to use mistral-inference, take a look at the [README](https://github.com/mistralai/mistral-inference/blob/main/README.md) and dive into this colab notebook to get started:

<a target="_blank" href="https://colab.research.google.com/github/mistralai/mistral-inference/blob/main/tutorials/getting_started.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


[Quickstart]
Source: https://docs.mistral.ai/docs/getting-started/quickstart

[platform_url]: https://console.mistral.ai/


:::tip[ ]
Looking for La Plateforme? Head to [console.mistral.ai][platform_url]
:::

## Account setup

- To get started, create a Mistral account or sign in at https://console.mistral.ai.
- Then, navigate to your "Organization" settings at https://admin.mistral.ai.
- To add your payment information and activate payments on your account, find the [billing](https://admin.mistral.ai/organization/billing) section under Administration.
- You can now manage all your [Workspaces](https://admin.mistral.ai/organization/workspaces) and Organization via this page.
- Return to https://console.mistral.ai once everything is settled.
- After that, go to the [API keys](https://console.mistral.ai/api-keys) page under your Workspace and create a new API key by clicking "Create new key". Make sure to copy the API key, save it securely, and do not share it with anyone.

## Getting started with Mistral AI API

<a target="_blank" href="https://colab.research.google.com/github/mistralai/cookbook/blob/main/quickstart.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Mistral AI API provides a seamless way for developers to integrate Mistral's state-of-the-art 
models into their applications and production workflows with just a few lines of code. 
Our API is currently available through [La Plateforme][platform_url]. 
You need to activate payments on your account to enable your API keys.
After a few moments, you will be able to use our `chat` endpoint:

<Tabs groupId="code">
  <TabItem value="python" label="python" default>
```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)
print(chat_response.choices[0].message.content)
```

  </TabItem>

  <TabItem value="typescript" label="typescript">
```typescript


const apiKey = process.env.MISTRAL_API_KEY;

const client = new Mistral({apiKey: apiKey});

const chatResponse = await client.chat.complete({
  model: 'mistral-large-latest',
  messages: [{role: 'user', content: 'What is the best French cheese?'}],
});

console.log('Chat:', chatResponse.choices[0].message.content);
```
  </TabItem>

  <TabItem value="curl" label="curl">
```bash
curl --location "https://api.mistral.ai/v1/chat/completions" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
    "model": "mistral-large-latest",
    "messages": [{"role": "user", "content": "Who is the most renowned French painter?"}]
  }'
```
  </TabItem>
</Tabs>

To generate text embeddings using Mistral AI's embeddings API, we can make a request to the API 
endpoint and specify the embedding model `mistral-embed`, along with providing a list of input texts. 
The API will then return the corresponding embeddings as numerical vectors, which can be used for
further analysis or processing in NLP applications.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>
```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-embed"

client = Mistral(api_key=api_key)

embeddings_response = client.embeddings.create(
    model=model,
    inputs=["Embed this sentence.", "As well as this one."]
)

print(embeddings_response)
```

  </TabItem>

  <TabItem value="typescript" label="typescript">
```typescript


const apiKey = process.env.MISTRAL_API_KEY;

const client = new Mistral({apiKey: apiKey});

const embeddingsResponse = await client.embeddings.create({
  model: 'mistral-embed',
  inputs: ["Embed this sentence.", "As well as this one."],
});

console.log(embeddingsResponse);
```
  </TabItem>

  <TabItem value="curl" label="curl">
```bash
curl --location "https://api.mistral.ai/v1/embeddings" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
    "model": "mistral-embed",
    "input": ["Embed this sentence.", "As well as this one."]
  }'
```
  </TabItem>
</Tabs>


For a full description of the models offered on the API, head on to the **[model documentation](../models/models_overview)**.


[Basic RAG]
Source: https://docs.mistral.ai/docs/guides/basic-RAG