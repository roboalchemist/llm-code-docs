# Source: https://docs.together.ai/docs/ai-evaluations-ui.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Guide to using the AI Evaluations UI for model assessment

# AI Evaluations UI

## Introduction

This guide explains how to perform evaluations using the Together AI UI.

<Info>
  For a comprehensive guide with detailed parameter descriptions and API examples, see [AI Evaluations](/docs/ai-evaluations).
</Info>

## Step 1: Upload Your Dataset

Navigate to [https://api.together.ai/evaluations](https://api.together.ai/evaluations) and click "Create Evaluation".

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/54eaf05a3601b9d189126e36b61fcce1eecd94c3e101f1e2ac06b02ba2f4e949-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=4e73123770ae25ac0434396435d7874f" alt="Create Evaluation button" width="1455" height="92" data-path="images/54eaf05a3601b9d189126e36b61fcce1eecd94c3e101f1e2ac06b02ba2f4e949-image.png" />
</Frame>

Upload your dataset or select one from your library. Preview your dataset content in the "Dataset Preview" section.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/09597f1f6f6ea6ddd6538828624f096fe3e9ae7d481304438f182c525979c982-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b1962174476e5bb8b2106f3274980138" alt="Dataset upload interface" width="1439" height="667" data-path="images/09597f1f6f6ea6ddd6538828624f096fe3e9ae7d481304438f182c525979c982-image.png" />
</Frame>

## Step 2: Customize Your Evaluation Job

### Evaluation Types

| Type         | Description                                                           |
| :----------- | :-------------------------------------------------------------------- |
| **Classify** | Categorizes input into one of the provided categories                 |
| **Score**    | Evaluates input and produces a score within a specified range         |
| **Compare**  | Compares responses from two models to determine which performs better |

### Judge Configuration

Configure the judge model that will evaluate your inputs:

| Field             | Type            | Required | Description                                   |
| :---------------- | :-------------- | :------- | :-------------------------------------------- |
| `judge model`     | string          | Yes      | The model used for evaluation                 |
| `system template` | Jinja2 template | Yes      | Instructions for the judge to assess the data |

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=743b1501300f81d64a5e894af26e1b60" alt="Judge configuration interface" width="1444" height="612" data-path="images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png" />
</Frame>

### Evaluation Type Parameters

**Classify parameters:**

| Field               | Type             | Description                                                                 |
| :------------------ | :--------------- | :-------------------------------------------------------------------------- |
| `labels`            | list of strings  | Categories for classification. Mark each as 'pass' or 'fail' for statistics |
| `model_to_evaluate` | object or string | Model configuration or dataset column name                                  |

**Score parameters:**

| Field               | Type             | Description                                                |
| :------------------ | :--------------- | :--------------------------------------------------------- |
| `min_score`         | float            | Minimum score the judge can assign                         |
| `max_score`         | float            | Maximum score the judge can assign                         |
| `pass_threshold`    | float            | Score at or above which is considered "passing" (optional) |
| `model_to_evaluate` | object or string | Model configuration or dataset column name                 |

**Compare parameters:**

| Field     | Type             | Description                                       |
| :-------- | :--------------- | :------------------------------------------------ |
| `model_a` | object or string | First model configuration or dataset column name  |
| `model_b` | object or string | Second model configuration or dataset column name |

### Model Evaluation Configuration

Choose how to provide responses for evaluation:

* **Configure** – Generate new responses using a model
* **Field name** – Use existing responses from your dataset

#### Option 1: Model Configuration Object

Use when generating new responses for evaluation:

| Field                | Type            | Required      | Description                                                                             |
| :------------------- | :-------------- | :------------ | :-------------------------------------------------------------------------------------- |
| `model_name`         | string          | Yes           | One of our [supported models](/docs/evaluations-supported-models)                       |
| `model_source`       | string          | Yes           | `"serverless"`, `"dedicated"`, or `"external"`                                          |
| `system_template`    | Jinja2 template | Yes           | Generation instructions (see [Templates](/docs/ai-evaluations#understanding-templates)) |
| `input_template`     | Jinja2 template | Yes           | Input format, e.g., `"{{prompt}}"`                                                      |
| `max_tokens`         | integer         | No            | Maximum tokens for generation                                                           |
| `temperature`        | float           | No            | Temperature setting for generation                                                      |
| `external_api_token` | string          | When external | API bearer token for external providers                                                 |
| `external_base_url`  | string          | No            | Custom base URL for external APIs                                                       |

#### Option 2: Column Reference

Use when evaluating pre-existing data from your dataset. Simply specify the column name containing the data to evaluate.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=e2096024a7613749a53d9e30227d0a41" alt="Model configuration interface" width="3198" height="1448" data-path="images/together-ai-evaluations-ui-model-config.png" />
</Frame>

### Using External Models

<Info>
  When using `model_source = "external"`:

  * Enter a supported shortcut (e.g., `openai/gpt-5`). See [Supported External Models](/docs/evaluations-supported-models).
  * Provide your `external_api_token` for the provider.
  * Optionally set `external_base_url` for custom OpenAI `chat/completions`-compatible endpoints.
</Info>

For dedicated endpoints, set `model_source = "dedicated"` and paste your endpoint ID into the model field. See [Dedicated Inference](/docs/dedicated-inference).

## Step 3: Monitor Job Progress

Wait for your evaluation job to complete. The UI will show the current status of your job.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ccc97c1597914577f4fadb8e37dfd51b538f19cf06112a4f5eaf50f8147bb51d-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=54bfca393a6172dfd66869489d14b837" alt="Job progress monitoring" width="1432" height="449" data-path="images/ccc97c1597914577f4fadb8e37dfd51b538f19cf06112a4f5eaf50f8147bb51d-image.png" />
</Frame>

## Step 4: Review Results

Once complete, you can:

* Preview statistics and responses in the Dataset Preview
* Download the result file using the "Download" button

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/8e2ed90ae49e0311bb1fd53374bf41c2eb9b276ec305cc9d707813a248e69432-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=18b92170bc1c92835bea2bcaf6a234a0" alt="Results preview" width="1431" height="663" data-path="images/8e2ed90ae49e0311bb1fd53374bf41c2eb9b276ec305cc9d707813a248e69432-image.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).