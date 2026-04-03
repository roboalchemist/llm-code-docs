# Source: https://docs.together.ai/docs/ai-evaluations-ui.md

> Guide to using the AI Evaluations UI for model assessment

# AI Evaluations UI

## Introduction

This guide explains how to perform evaluations using the Together AI UI.

For a comprehensive guide with detailed parameter descriptions, see [AI Evaluations](ai-evaluations).

## Step 1: Upload Your Dataset

Navigate to [https://api.together.ai/evaluations](https://api.together.ai/evaluations) and click "Create Evaluation".

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/54eaf05a3601b9d189126e36b61fcce1eecd94c3e101f1e2ac06b02ba2f4e949-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=4e73123770ae25ac0434396435d7874f" alt="" data-og-width="1455" width="1455" data-og-height="92" height="92" data-path="images/54eaf05a3601b9d189126e36b61fcce1eecd94c3e101f1e2ac06b02ba2f4e949-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/54eaf05a3601b9d189126e36b61fcce1eecd94c3e101f1e2ac06b02ba2f4e949-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5d8d247b3538252773f8daf8e4c02e3a 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/54eaf05a3601b9d189126e36b61fcce1eecd94c3e101f1e2ac06b02ba2f4e949-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=85885fbda671ba06815eb263f439c48a 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/54eaf05a3601b9d189126e36b61fcce1eecd94c3e101f1e2ac06b02ba2f4e949-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=140180a2021477f337fd2645285ceb2b 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/54eaf05a3601b9d189126e36b61fcce1eecd94c3e101f1e2ac06b02ba2f4e949-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=ee273b9fbb558a8a84ddd46fd5f89700 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/54eaf05a3601b9d189126e36b61fcce1eecd94c3e101f1e2ac06b02ba2f4e949-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=7245b2a30835b624f26e1e6ac3234685 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/54eaf05a3601b9d189126e36b61fcce1eecd94c3e101f1e2ac06b02ba2f4e949-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=bfa761f149fb1c19ec273ba7b538f452 2500w" />
</Frame>

Upload your dataset or select one from your library.\
Preview your dataset content in the "Dataset Preview" section.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/09597f1f6f6ea6ddd6538828624f096fe3e9ae7d481304438f182c525979c982-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b1962174476e5bb8b2106f3274980138" alt="" data-og-width="1439" width="1439" data-og-height="667" height="667" data-path="images/09597f1f6f6ea6ddd6538828624f096fe3e9ae7d481304438f182c525979c982-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/09597f1f6f6ea6ddd6538828624f096fe3e9ae7d481304438f182c525979c982-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=3f031b080dcf3cc4d62e8f1bb76d5287 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/09597f1f6f6ea6ddd6538828624f096fe3e9ae7d481304438f182c525979c982-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=1381574f7c98cfc07d3245dbe32fd519 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/09597f1f6f6ea6ddd6538828624f096fe3e9ae7d481304438f182c525979c982-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8d111b157914027a4ca91c8e13634370 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/09597f1f6f6ea6ddd6538828624f096fe3e9ae7d481304438f182c525979c982-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=73e978aaec1949c13a839d91f8849002 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/09597f1f6f6ea6ddd6538828624f096fe3e9ae7d481304438f182c525979c982-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=34672c0d41613d51196a8e9529e1c340 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/09597f1f6f6ea6ddd6538828624f096fe3e9ae7d481304438f182c525979c982-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=e0b355f2103f84da9cc46f53cd77a9d1 2500w" />
</Frame>

## Step 2: Customize Your Evaluation Job

We support three evaluation types:

* **Classify** – Categorizes input into one of the provided categories
* **Score** – Evaluates input and produces a score within a specified range
* **Compare** – Compares responses from two models to determine which performs better according to given criteria

### Judge Configuration

The `judge` object contains two required fields:

* **judge model** – (string) The model used for evaluation
* **system template** – (Jinja template) Provides guidance for the judge to assess the data

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=743b1501300f81d64a5e894af26e1b60" alt="" data-og-width="1444" width="1444" data-og-height="612" height="612" data-path="images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=737e67d9f45af98fa6e3515574204955 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=69388fd95b9d0e4ef9d8273db499a308 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=eac9dda26f97f7168b00968cbd070cbe 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=55bd95040582f77a24ea60c4322bb5e9 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=cda932a1db9dcf828e1ebef025001cf8 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=81d8508ab932f2b9970bd9d56c93cc75 2500w" />
</Frame>

### Model Configuration Parameters

#### Classify

* **labels** – (list of strings) Categories for input classification. For each category, you can specify whether it's considered 'pass' or 'fail' for statistics computation
* **model\_to\_evaluate** – Configuration for the model being evaluated

#### Score

* **min\_score** – (float) Minimum score the judge can assign
* **max\_score** – (float) Maximum score the judge can assign
* **model\_to\_evaluate** – Configuration for the model being evaluated

#### Compare

* Only requires judge setup and two model configurations for comparison

### Model Evaluation Configuration

Choose whether to evaluate existing data or generate new responses:

* **"Configure"** – Generate data using the model for evaluation
* **"Field name"** – Data required for evaluation is already present in your dataset

**Option 1: Model Object**\
Use when generating new responses for evaluation. The object requires:

* **model\_name** – (string) One of our supported models
* **model\_source** – (string) One of: "serverless", "dedicated", or "external"
* **external\_api\_token** – Optional; required when `model_source = "external"`. If you select `external` model source, use this to provide API bearer authentication token (eg. OpenAI token)
* **external\_base\_url** - Optional; when using an `external` model source, you can specify your own base URL. (e.g., `"https://api.openai.com"`). The API must be OpenAI `chat/completions`-compatible.
* **system\_template** – (Jinja2 template) An instruction for generation, e.g., "You are a helpful assistant." (see [Understanding Templates](ai-evaluations#understanding-templates))
* **input\_template** – (Jinja2 template) Input format, e.g., `"{{prompt}}"` (see [Understanding Templates](ai-evaluations#understanding-templates))
* **max\_tokens** – (integer) Maximum tokens for generation
* **temperature** – (float) Temperature setting for generation

**Option 2: Column Reference (String)**\
Use when evaluating pre-existing data from your dataset. Simply specify the column name containing the data to evaluate.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=e2096024a7613749a53d9e30227d0a41" alt="" data-og-width="3198" width="3198" data-og-height="1448" height="1448" data-path="images/together-ai-evaluations-ui-model-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d54e96248608aa438aeebb5abe6d5fee 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=2f958bfe7f5fb112a81be6dc340fdae3 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=8d73f99dc289304e777614cea486ecb2 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9e902cf6083499a4cf93bcbc9ab54dd2 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=30756869fb96066a8ac315f16120f505 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=1b4dd0a67e4b3699c7a8edfbebccca72 2500w" />
</Frame>

### Using external models

When you set `model_source = "external"` (for either the judge or the model being evaluated):

* Enter a supported shortcut in the model field (e.g., `openai/gpt-5`). See [Supported External Models](/docs/evaluations-supported-models).
* Provide `external_api_token` – use your API bearer token for the external provider (e.g., OpenAI token).
* Optionally set `external_base_url` if using a custom endpoint (e.g., `https://api.openai.com`). The API must be OpenAI `chat/completions`-compatible.

For dedicated endpoints, set `model_source = "dedicated"` and paste your endpoint ID into the model field. See [Dedicated Inference](/docs/dedicated-inference).

## Step 3: Monitor Job Progress

Wait for your evaluation job to complete.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ccc97c1597914577f4fadb8e37dfd51b538f19cf06112a4f5eaf50f8147bb51d-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=54bfca393a6172dfd66869489d14b837" alt="" data-og-width="1432" width="1432" data-og-height="449" height="449" data-path="images/ccc97c1597914577f4fadb8e37dfd51b538f19cf06112a4f5eaf50f8147bb51d-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ccc97c1597914577f4fadb8e37dfd51b538f19cf06112a4f5eaf50f8147bb51d-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=64ccb98ffa9838c9081cc3e4b00b3ca1 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ccc97c1597914577f4fadb8e37dfd51b538f19cf06112a4f5eaf50f8147bb51d-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=e1d9195d99cdd93cb0cfe9908422ef50 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ccc97c1597914577f4fadb8e37dfd51b538f19cf06112a4f5eaf50f8147bb51d-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f91eaf1ae00e4e986aae8c8a5eedc612 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ccc97c1597914577f4fadb8e37dfd51b538f19cf06112a4f5eaf50f8147bb51d-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=ca33b90e7a74ed51d3ef91eee3b17b60 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ccc97c1597914577f4fadb8e37dfd51b538f19cf06112a4f5eaf50f8147bb51d-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=eef5dfe70413b846ddad763b67b0f0e1 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ccc97c1597914577f4fadb8e37dfd51b538f19cf06112a4f5eaf50f8147bb51d-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=db202cea1aadc33255e95310eb8f00b8 2500w" />
</Frame>

## Step 4: Review Results

Once complete, you can:

* Preview statistics and responses in the Dataset Preview
* Download the result file using the "Download" button

<Frame>
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/togetherai-52386018/images/8e2ed90ae49e0311bb1fd53374bf41c2eb9b76ec305cc9d707813a248e69432-image.png" alt="" />
</Frame>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt