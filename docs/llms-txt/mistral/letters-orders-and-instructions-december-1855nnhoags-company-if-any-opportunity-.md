# Letters Orders and Instructions December 1855\n\n**Hoag's Company, if any opportunity offers.**\n\nYou are to be particularly exact and careful in these pagineries, that there is no disgrace meet between the Returns and you Pay Roll, or those who will be strict examining into it hereafter.\n\nI am & c.\n\n*[Signed]*\nEff.
```

</details>

<details>
<summary><b>OCR with structured output</b></summary>

![](https://i.imghippo.com/files/kgXi81726851246.jpg)

```bash
curl https://api.mistral.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -d '{
    "model": "pixtral-12b-2409",
    "messages": [
            {
                "role": "system",
                "content": [
                    {"type": "text",
                     "text" : "Extract the text elements described by the user from the picture, and return the result formatted as a json in the following format : {name_of_element : [value]}"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "From this restaurant bill, extract the bill number, item names and associated prices, and total price and return it as a string in a Json object"
                    },
                    {
                        "type": "image_url",
                        "image_url": "https://i.imghippo.com/files/kgXi81726851246.jpg"
                    }
                ]
            }
        ],
    "response_format": 
      {
        "type": "json_object"
      }
  }'

```

Model output: 
```json
{'bill_number': '566548',
 'items': [{'item_name': 'BURGER - MED RARE', 'price': 10},
  {'item_name': 'WH/SUB POUTINE', 'price': 2},
  {'item_name': 'BURGER - MED RARE', 'price': 10},
  {'item_name': 'WH/SUB BSL - MUSH', 'price': 4},
  {'item_name': 'BURGER - MED WELL', 'price': 10},
  {'item_name': 'WH BREAD/NO ONION', 'price': 2},
  {'item_name': 'SUB POUTINE - MUSH', 'price': 2},
  {'item_name': 'CHK PESTO/BR', 'price': 9},
  {'item_name': 'SUB POUTINE', 'price': 2},
  {'item_name': 'SPEC OMELET/BR', 'price': 9},
  {'item_name': 'SUB POUTINE', 'price': 2},
  {'item_name': 'BSL', 'price': 8}],
 'total_price': 68}
```

</details>

## FAQ

- **What is the price per image?**

    The price is calculated using the same pricing as input tokens per image, with each image being tokenized.

- **How many tokens correspond to an image and/or what is the maximum resolution?**

    Depending on the model and resolution, an image will be tokenized differently. Below is a summary.

    | Model | Max Resolution | ≈ Formula | ≈ N Max Tokens |
    | - | - | - | - |
    | Mistral Small 3.2 | 1540x1540 | `≈ (ResolutionX * ResolutionY) / 784` | ≈ 3025 |
    | Mistral Medium 3 | 1540x1540 | `≈ (ResolutionX * ResolutionY) / 784` | ≈ 3025 |
    | Mistral Small 3.1 | 1540x1540 | `≈ (ResolutionX * ResolutionY) / 784` | ≈ 3025 |
    | Pixtral Large | 1024x1024 | `≈ (ResolutionX * ResolutionY) / 256` | ≈ 4096 |
    | Pixtral 12B | 1024x1024 | `≈ (ResolutionX * ResolutionY) / 256` | ≈ 4096 |

    If the resolution of the image sent is higher than the maximum resolution of the model, the image will be downscaled to its maximum resolution. An error will be sent if the resolution is higher than **10000x10000**.

- **Can I fine-tune the image capabilities?**

    Yes, you can fine-tune pixtral-12b.

- **Can I use them to generate images?**

    No, they are designed to understand and analyze images, not to generate them.

- **What types of image files are supported?**
    
    We currently support the following image formats:

    - PNG (.png)
    - JPEG (.jpeg and .jpg)
    - WEBP (.webp) 
    - Non-animated GIF with only one frame (.gif) 

- **Is there a limit to the size of the image?**

    The current file size limit is 10Mb. 

- **What's the maximum number images per request?** 

    The maximum number images per request via API is 8.

- **What is the rate limit?**

    For information on rate limits, please visit https://console.mistral.ai/limits/.


[AWS Bedrock]
Source: https://docs.mistral.ai/docs/deployment/cloud/aws

## Introduction

Mistral AI's open and commercial models can be deployed on the AWS Bedrock cloud platform as
fully managed endpoints. AWS Bedrock is a serverless service so you don't have
to manage any infrastructure.

As of today, the following models are available:

- Mistral Large (24.07, 24.02)
- Mistral Small (24.02)
- Mixtral 8x7B
- Mistral 7B

For more details, visit the [models](../../../getting-started/models/models_overview/) page.

## Getting started

The following sections outline the steps to deploy and query a Mistral model on the
AWS Bedrock platform.

The following items are required:

- Access to an **AWS account** within a region that supports the AWS Bedrock service and 
  offers access to your model of choice: see 
  [the AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) 
  for model availability per region.
- An AWS **IAM principal** (user, role) with sufficient permissions, see
  [the AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html)
  for more details.
- A local **code environment** set up with the relevant AWS SDK components, namely:
    - the AWS CLI: see [the AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
      for the installation procedure.
    - the `boto3` Python library: see the [AWS documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) 
      for the installation procedure.

### Requesting access to the model

Follow the instructions on
[the AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
to unlock access to the Mistral model of your choice.

### Querying the model

AWS Bedrock models are accessible through the Converse API.

Before running the examples below, make sure to sure to :

- Properly configure the authentication
credentials for your development environment. 
[The AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
provides an in-depth explanation on the required steps. 
- Create a Python virtual environment with the `boto3` package (version >= `1.34.131`).
- Set the following environment variables:
    - `AWS_REGION`: The region where the model is deployed (e.g. `us-west-2`),
    - `AWS_BEDROCK_MODEL_ID`: The model ID (e.g. `mistral.mistral-large-2407-v1:0`).

<Tabs>
    <TabItem value="python" label="Python">

        ```python
        import boto3
        import os

        region = os.environ.get("AWS_REGION")
        model_id = os.environ.get("AWS_BEDROCK_MODEL_ID")

        bedrock_client = boto3.client(service_name='bedrock-runtime', region_name=region)

        user_msg = "Who is the best French painter? Answer in one short sentence."
        messages = [{"role": "user", "content": [{"text": user_msg}]}]
        temperature = 0.0
        max_tokens = 1024

        params = {"modelId": model_id,
                  "messages": messages,
                  "inferenceConfig": {"temperature": temperature,
                                      "maxTokens": max_tokens}}

        resp = bedrock_client.converse(**params)

        print(resp["output"]["message"]["content"][0]["text"])
        ```
    </TabItem>
        <TabItem value="cli" label="AWS CLI">
            ```shell
             aws bedrock-runtime converse \
             --region $AWS_REGION \
             --model-id $AWS_BEDROCK_MODEL_ID \
             --messages '[{"role": "user", "content": [{"text": "Who is the best French painter? Answer in one short sentence."}]}]'
            ```
    </TabItem>
</Tabs>

## Going further

For more details and examples, refer to the following resources:

- [AWS GitHub repository with multiple examples and use-cases leveraging Mistral models](https://github.com/aws-samples/mistral-on-aws).
- [AWS documentation on the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html).
- [AWS documentation on inference requests for Mistral models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-mistral.html#model-parameters-mistral-request-response).


[Azure AI]
Source: https://docs.mistral.ai/docs/deployment/cloud/azure

## Introduction

Mistral AI's open and commercial models can be deployed on the Microsoft Azure AI cloud platform
in two ways:

- _Pay-as-you-go managed services_: Using Model-as-a-Service (MaaS) serverless API
  deployments billed on endpoint usage. No GPU capacity quota is required for deployment.

- _Real-time endpoints_: With quota-based billing tied to the underlying GPU
  infrastructure you choose to deploy.


This page focuses on the MaaS offering, where the following models are available:

- Mistral Large (24.11, 24.07)
- Mistral Small (24.09)
- Ministral 3B (24.10)
- Mistral Nemo 

For more details, visit the [models](../../../getting-started/models/models_overview) page.


## Getting started

The following sections outline the steps to deploy and query a Mistral model on the Azure AI MaaS platform.

### Deploying the model

Follow the instructions on the [Azure documentation](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-mistral?tabs=mistral-large#create-a-new-deployment)
to create a new deployment for the model of your choice. Once deployed, take
note of its corresponding URL and secret key.


### Querying the model

Deployed endpoints expose a REST API that you can query using Mistral's SDKs or
plain HTTP calls.

To run the examples below, set the following environment variables:
    - `AZUREAI_ENDPOINT`: Your endpoint URL, should be of the form `https://your-endpoint.inference.ai.azure.com/v1/chat/completions`.
    - `AZUREAI_API_KEY`: Your secret key.
<Tabs>
    <TabItem value="curl" label="cURL" default>
        ```bash
        curl --location $AZUREAI_ENDPOINT/v1/chat/completions \
            --header  "Content-Type: application/json" \
            --header "Authorization: Bearer $AZURE_API_KEY" \
            --data '{
          "model": "azureai",
          "messages": [
            {
              "role": "user",
              "content": "Who is the best French painter? Answer in one short sentence."
            }
          ]
        }'
        ```
    </TabItem>
    <TabItem value="python" label="Python">
        This code requires a virtual environment with the following packages:
        - `mistralai-azure>=1.0.0`

        ```python
        from mistralai_azure import MistralAzure
        import os

        endpoint = os.environ.get("AZUREAI_ENDPOINT", "")
        api_key = os.environ.get("AZUREAI_API_KEY", "")

        client = MistralAzure(azure_endpoint=endpoint,
                         azure_api_key=api_key)

        resp = client.chat.complete(messages=[
            {
                "role": "user",
                "content": "Who is the best French painter? Answer in one short sentence."
            },
        ], model="azureai")

        if resp:
            print(resp)
        ```
    </TabItem>
    <TabItem value="ts" label="TypeScript">
        This code requires the following package:
        - `@mistralai/mistralai-azure` (version >= `1.0.0`)

        ```typescript
        import { MistralAzure } from "@mistralai/mistralai-azure";

        const client = new MistralAzure({
            endpoint: process.env.AZUREAI_ENDPOINT || "",
            apiKey: process.env.AZUREAI_API_KEY || ""
        });

        async function chat_completion(user_msg: string) {
            const resp = await client.chat.complete({
                model: "azureai",
                messages: [
                    {
                        content: user_msg,
                        role: "user",
                    },
                ],
            });
            if (resp.choices && resp.choices.length > 0) {
                console.log(resp.choices[0]);
            }
        }

        chat_completion("Who is the best French painter? Answer in one short sentence.");
        ```
    </TabItem>
</Tabs>


## Going further

For more details and examples, refer to the following resources:
- [Release blog post for Mistral Large 2 and Mistral NeMo](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/ai-innovation-continues-introducing-mistral-large-2-and-mistral/ba-p/4200181).
- [Azure documentation for MaaS deployment of Mistral models](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-mistral).
- [Azure ML examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/sdk/python/foundation-models/mistral) with several Mistral-based samples.


[IBM watsonx.ai]
Source: https://docs.mistral.ai/docs/deployment/cloud/ibm-watsonx

## Introduction

Mistral AI's Large model is available on the IBM watsonx.ai platform as a fully managed
solution, as well as an on-premise deployment.

## Getting started

The following solutions outline the steps to query Mistral Large on the SaaS version of
IBM watsonx.ai.

### Pre-requisites

The following items are required:

- An IBM watsonx project (`IBM_CLOUD_PROJECT_ID`)
- A Service ID with an access policy enabling the use of the Watson Lachine Learning service.

To enable access to the API, you must make sure that:
- Your Service ID has been added to the project as `EDITOR`,
- You have generated an API key (`IBM_CLOUD_API_KEY`) for your Service ID.

### Querying the model (chat completion)

You can query Mistral Large using either IBM's SDK or plain HTTP calls.

:::warning

The examples below leverage the `mistral-common` Python package to properly format
the user messages with special tokens. It is **strongly recommended to avoid passing
raw strings and handle special tokens manually**: this might result in silent
tokenization errors that would highly degrade the quality of the model output.

:::

<Tabs>
    <TabItem value="python" label="Python">
        You will need to run your code from a virtual environment with the following
        packages:

        - `httpx` (tested with `0.27.2`)
        - `ibm-watsonx-ai` (tested with `1.1.11`)
        - `mistral-common` (tested with `1.4.4`)

        In the following snippet, your API key will be used to generate an IAM token,
        then the call to the model is performed using this token for authentication.

        ```python
        from ibm_watsonx_ai import Credentials
        from ibm_watsonx_ai.foundation_models import ModelInference
        from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
        from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
        from mistral_common.protocol.instruct.request import ChatCompletionRequest
        from mistral_common.protocol.instruct.messages import UserMessage

        import os
        import httpx

        IBM_CLOUD_REGIONS = {
                "dallas": "us-south",
                "london": "eu-gb",
                "frankfurt": "eu-de",
                "tokyo": "jp-tok"
                }

        IBM_CLOUD_PROJECT_ID = "xxx-xxx-xxx" # Replace with your project id


        def get_iam_token(api_key: str) -> str:
            """
            Return an IAM access token generated from an API key.
            """

            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = f"apikey={api_key}&grant_type=urn:ibm:params:oauth:grant-type:apikey"
            resp = httpx.post(
                url="https://iam.cloud.ibm.com/identity/token",
                headers=headers,
                data=data,
            )
            token = resp.json().get("access_token")
            return token


        def format_user_message(raw_user_msg: str) -> str:
            """
            Return a formatted prompt using the official Mistral tokenizer.
            """

            tokenizer = MistralTokenizer.v3()  # Use v3 for Mistral Large
            tokenized = tokenizer.encode_chat_completion(
                ChatCompletionRequest(
                    messages=[UserMessage(content=raw_user_msg)], model="mistral-large"
                )
            )
            return tokenized.text


        region = "frankfurt" # Define the region of your choice here
        api_key = os.environ["IBM_API_KEY"]
        access_token = get_iam_token(api_key=api_key)
        credentials = Credentials(url=f"https://{IBM_CLOUD_REGIONS[region]}.ml.cloud.ibm.com",
                                  token=access_token)

        params = {GenParams.MAX_NEW_TOKENS: 256, GenParams.TEMPERATURE: 0.0}
        model_inference = ModelInference(
            project_id=IBM_CLOUD_PROJECT_ID,
            model_id="mistralai/mistral-large",
            params=params,
            credentials=credentials,
        )
        user_msg_content = "Who is the best French painter? Answer in one short sentence."
        resp = model_inference.generate_text(prompt=format_user_message(user_msg_content))
        print(resp)

        ```

    </TabItem>
</Tabs>

## Going further

For more information and examples, you can check:

- The [IBM watsonx.ai Python SDK documentation](https://ibm.github.io/watsonx-ai-python-sdk/index.html)
- This [IBM Developer tutorial](https://developer.ibm.com/tutorials/awb-using-mistral-ai-llms-in-watsonx-ai-flows-engine/)
  on how to use Mistral Large with IBM watsonx.ai flows engine.


[Outscale]
Source: https://docs.mistral.ai/docs/deployment/cloud/outscale

## Introduction

Mistral AI models are available on the Outscale platform as managed deployments.
Through the Outscale marketplace, you can subscribe to a Mistral service that will,
on your behalf, provision a virtual machine and a GPU then deploy the model on it.


As of today, the following models are available:

- Mistral Small (24.09)
- Codestral (24.05)
- Ministral 8B (24.10)

For more details, visit the [models](../../../getting-started/models/models_overview) page.

## Getting started

The following sections outline the steps to query a Mistral model on the Outscale platform.

### Deploying the model

Follow the steps described in the
[Outscale documentation](https://docs.outscale.com/en/userguide/Subscribing-To-a-Mistral-Service-and-Deploying-it.html) to deploy a service
with the model of your choice. 

### Querying the model (chat completion)

Deployed models expose a REST API that you can query using Mistral's SDK or plain HTTP calls.
To run the examples below you will need to set the following environment variables:

- `OUTSCALE_SERVER_URL`: the URL of the VM hosting your Mistral model
- `OUTSCALE_MODEL_NAME`: the name of the model to query (e.g. `small-2409`, `codestral-2405`)


<Tabs>
    <TabItem value="curl" label="cURL">
        ```bash
        echo $OUTSCALE_SERVER_URL/v1/chat/completions
        echo $OUTSCALE_MODEL_NAME
        curl --location $OUTSCALE_SRV_URL/v1/chat/completions \
          --header "Content-Type: application/json" \
          --header "Accept: application/json" \
          --data '{
              "model": "'"$OUTSCALE_MODEL_NAME"'",
              "temperature": 0,
              "messages": [
                {"role": "user", "content": "Who is the best French painter? Answer in one short sentence."}
              ],
              "stream": false
            }'
        ```
    </TabItem>
    <TabItem value="python" label="Python">
        ```python
        import os
        from mistralai import Mistral

        client = Mistral(server_url=os.environ["OUTSCALE_SERVER_URL"])

        resp = client.chat.complete(
            model=os.environ["OUTSCALE_MODEL_NAME"],
            messages=[
                {
                    "role": "user",
                    "content": "Who is the best French painter? Answer in one short sentence.",
                }
            ],
            temperature=0
        )

        print(resp.choices[0].message.content)
        ```
    </TabItem>
    <TabItem value="ts" label="TypeScript">
        ```typescript
        import { Mistral } from "@mistralai/mistralai";

        const client = new Mistral({
            serverURL: process.env.OUTSCALE_SERVER_URL || ""
        });

        const modelName = process.env.OUTSCALE_MODEL_NAME|| "";

        async function chatCompletion(user_msg: string) {
            const resp = await client.chat.complete({
                model: modelName,
                messages: [
                    {
                        content: user_msg,
                        role: "user",
                    },
                ],
            });
            if (resp.choices && resp.choices.length > 0) {
                console.log(resp.choices[0]);
            }
        }

        chatCompletion("Who is the best French painter? Answer in one short sentence.");
        ```
    </TabItem>
</Tabs>

### Querying the model (FIM completion)

Codestral can be queried using an additional completion mode called fill-in-the-middle (FIM).
For more information, see the
[code generation section](../../../capabilities/code_generation/#fill-in-the-middle-endpoint).


<Tabs>
    <TabItem value="curl" label="cURL">
       ```bash
        curl --location $OUTSCALE_SERVER_URL/v1/fim/completions \
          --header "Content-Type: application/json" \
          --header "Accept: application/json" \
          --data '{
              "model": "'"$OUTSCALE_MODEL_NAME"'",
              "prompt": "def count_words_in_file(file_path: str) -> int:",
              "suffix": "return n_words",
              "stream": false
            }'
        ```
    </TabItem>
    <TabItem value="python" label="Python">
       ```python
        import os
        from mistralai import Mistral

        client = Mistral(server_url=os.environ["OUTSCALE_SERVER_URL"])

        resp = client.fim.complete(
            model = os.environ["OUTSCALE_MODEL_NAME"],
            prompt="def count_words_in_file(file_path: str) -> int:",
            suffix="return n_words"
        )

        print(resp.choices[0].message.content)
       ```
    </TabItem>
    <TabItem value="ts" label="TypeScript">
       ```typescript
        import { Mistral} from "@mistralai/mistralai";

        const client = new Mistral({
            serverURL: process.env.OUTSCALE_SERVER_URL || ""
        });

        const modelName = "codestral-2405";

        async function fimCompletion(prompt: string, suffix: string) {
            const resp = await client.fim.complete({
                model: modelName,
                prompt: prompt,
                suffix: suffix
            });
            if (resp.choices && resp.choices.length > 0) {
                console.log(resp.choices[0]);
            }
        }

        fimCompletion("def count_words_in_file(file_path: str) -> int:",
                      "return n_words");
       ```
    </TabItem>
</Tabs>

## Going further

For more information and examples, you can check:

- The [Outscale documentation](https://docs.outscale.com/en/userguide/Subscribing-To-a-Mistral-Service-and-Deploying-it.html)
  explaining how to subscribe to a Mistral service and deploy it.


[Cloud]
Source: https://docs.mistral.ai/docs/deployment/cloud/overview

You can access Mistral AI models via your preferred cloud provider and use your cloud credits.
In particular, Mistral's optimized commercial models are available on:

- [Azure AI](../azure)
- [AWS Bedrock](../aws)
- [Google Cloud Vertex AI Model Garden](../vertex)
- [Snowflake Cortex](../sfcortex)
- [IBM watsonx](../ibm-watsonx)
- [Outscale](../outscale)


[Snowflake Cortex]
Source: https://docs.mistral.ai/docs/deployment/cloud/sfcortex

## Introduction

Mistral AI's open and commercial models can be leveraged from the Snowflake Cortex platform
as fully managed endpoints. Mistral models on Snowflake Cortex are serverless services so
you don't have to manage any infrastructure.

As of today, the following models are available:

- Mistral Large
- Mistral 7B

For more details, visit the [models](../../../getting-started/models/models_overview) page.

## Getting started

The following sections outline the steps to query the latest version of Mistral Large 
on the Snowflake Cortex platform.

### Getting access to the model

The following items are required:

- The associated Snowflake account must be in a compatible region (see the
  [region list](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#availability)
  in the Snowflake documentation).
- The principal that is calling the model must have the `CORTEX_USER` database role.

### Querying the model (chat completion)

The model can be called either directly in SQL or in Python using Snowpark ML.
It is exposed via the
[`COMPLETE` _LLM function_](https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex).

<Tabs>
    <TabItem value="sql" label="SQL">
    ```SQL
    SELECT SNOWFLAKE.CORTEX.COMPLETE('mistral-large2', 'Who is the best French painter? Answer in one short sentence.');
    ```
    </TabItem>
    <TabItem value="Python" label="Python">
        Execute this code either from a hosted Snowflake notebook or from your local machine.
        
        For local execution you need to:
            - Create a virtual environment with the following package:
                - `snowflake-ml-python` (tested with version `1.6.1`)
            - Ensure that you have a [configuration file](https://docs.snowflake.com/en/user-guide/snowsql-config)
              with the proper credentials on your system. The example below assumes that you have a named connection
              called `mistral` that is configured appropriately.
        
        ```python
        from snowflake.snowpark import Session
        from snowflake.ml.utils import connection_params
        from snowflake.cortex import Complete

        # Start session (local execution only)
        params = connection_params.SnowflakeLoginOptions(connection_name="mistral")
        session = Session.builder.configs(params).create()

        # Query the model
        prompt = "Who is the best French painter? Answer in one short sentence."
        completion = Complete(model="mistral-large2", prompt=prompt)
        print(completion)
        ```
    </TabItem>
</Tabs>

## Going further

For more information and examples, you can check the Snowflake documentation for:

- [LLM functions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions)
- The API of the `COMPLETE` function in 
  [SQL](https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex)
  and [Python](https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/latest/api/model/snowflake.cortex.Complete).


[Vertex AI]
Source: https://docs.mistral.ai/docs/deployment/cloud/vertex

## Introduction

Mistral AI's open and commercial models can be deployed on the Google Cloud Vertex AI
platform as fully managed endpoints. Mistral models on Vertex AI are serverless services
so you don't have to manage any infrastructure.

As of today, the following models are available:

- Mistral Large (24.11, 24.07)
- Codestral (24.05)
- Mistral Nemo

For more details, visit the [models](../../../getting-started/models/models_overview) page.

## Getting started

The following sections outline the steps to deploy and query a Mistral model on the
Vertex AI platform.

### Requesting access to the model

The following items are required:

- Access to a Google Cloud Project with the Vertex AI API enabled
- Relevant IAM permissions to be able to enable the model and query endpoints through the following roles:
  - [Vertex AI User IAM role](https://cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.user).
  - Consumer Procurement Entitlement Manager role

To enable the model of your choice, navigate to its card in the 
[Vertex Model Garden catalog](https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models),
then click on "Enable".


### Querying the model (chat completion)

Available models expose a REST API that you can query using Mistral's SDKs or plain HTTP calls.

To run the examples below:

- Install the `gcloud` CLI to authenticate against the Google Cloud APIs, please refer to
[this page](https://cloud.google.com/docs/authentication/provide-credentials-adc#google-idp)
for more details.
- Set the following environment variables:
    - `GOOGLE_CLOUD_REGION`: The target cloud region.
    - `GOOGLE_CLOUD_PROJECT_ID`: The name of your project.
    - `VERTEX_MODEL_NAME`: The name of the model to query (e.g. `mistral-large`).
    - `VERTEX_MODEL_VERSION`: The version of the model to query (e.g. `2407`).
    

<Tabs>
    <TabItem value="curl" label="cURL">
        ```bash
        base_url="https://$GOOGLE_CLOUD_REGION-aiplatform.googleapis.com/v1/projects/$GOOGLE_CLOUD_PROJECT_ID/locations/$GOOGLE_CLOUD_REGION/publishers/mistralai/models"
        model_version="$VERTEX_MODEL_NAME@$VERTEX_MODEL_VERSION"
        url="$base_url/$model_version:rawPredict"

        curl --location $url\
          --header "Content-Type: application/json" \
          --header "Authorization: Bearer $(gcloud auth print-access-token)" \
          --data '{
              "model": "'"$VERTEX_MODEL_NAME"'",
              "temperature": 0,
              "messages": [
                {"role": "user", "content": "Who is the best French painter? Answer in one short sentence."}
              ],
              "stream": false
            }'
        ```
    </TabItem>
    <TabItem value="python" label="Python">
        This code requires a virtual environment with the following packages:
        - `mistralai[gcp]>=1.0.0` 

        ```python
        import os
        from mistralai_gcp import MistralGoogleCloud

        region = os.environ.get("GOOGLE_CLOUD_REGION")
        project_id = os.environ.get("GOOGLE_CLOUD_PROJECT_NAME")
        model_name = os.environ.get("VERTEX_MODEL_NAME")
        model_version = os.environ.get("VERTEX_MODEL_VERSION")

        client = MistralGoogleCloud(region=region, project_id=project_id)

        resp = client.chat.complete(
            model = f"{model_name}-{model_version}",
            messages=[
                {
                    "role": "user",
                    "content": "Who is the best French painter? Answer in one short sentence.",
                }
            ],
        )

        print(resp.choices[0].message.content)
        ```
    </TabItem>
    <TabItem value="ts" label="TypeScript">
    This code requires the following package:
    - `@mistralai/mistralai-gcp` (version >= `1.0.0`)

    ```typescript
    import { MistralGoogleCloud } from "@mistralai/mistralai-gcp";

    const client = new MistralGoogleCloud({
        region: process.env.GOOGLE_CLOUD_REGION || "",
        projectId: process.env.GOOGLE_CLOUD_PROJECT_ID || "",
    });

    const modelName = process.env.VERTEX_MODEL_NAME|| "";
    const modelVersion = process.env.VERTEX_MODEL_VERSION || "";

    async function chatCompletion(user_msg: string) {
        const resp = await client.chat.complete({
            model: modelName + "-" + modelVersion,
            messages: [
                {
                    content: user_msg,
                    role: "user",
                },
            ],
        });
        if (resp.choices && resp.choices.length > 0) {
            console.log(resp.choices[0]);
        }
    }

    chatCompletion("Who is the best French painter? Answer in one short sentence.");
    ```
    </TabItem>

</Tabs>

### Querying the model (FIM completion)

Codestral can be queried using an additional completion mode called fill-in-the-middle (FIM).
For more information, see the
[code generation section](../../../capabilities/code_generation/#fill-in-the-middle-endpoint).


<Tabs>
    <TabItem value="curl" label="cURL">
        ```bash
        VERTEX_MODEL_NAME=codestral
        VERTEX_MODEL_VERSION=2405

        base_url="https://$GOOGLE_CLOUD_REGION-aiplatform.googleapis.com/v1/projects/$GOOGLE_CLOUD_PROJECT_ID/locations/$GOOGLE_CLOUD_REGION/publishers/mistralai/models"
        model_version="$VERTEX_MODEL_NAME@$VERTEX_MODEL_VERSION"
        url="$base_url/$model_version:rawPredict"

        curl --location $url\
          --header "Content-Type: application/json" \
          --header "Authorization: Bearer $(gcloud auth print-access-token)" \
          --data '{
              "model":"'"$VERTEX_MODEL_NAME"'",
              "prompt": "def count_words_in_file(file_path: str) -> int:",
              "suffix": "return n_words",
              "stream": false
            }'
        ```
    </TabItem>
    <TabItem value="python" label="Python">

        ```python
        import os
        from mistralai_gcp import MistralGoogleCloud

        region = os.environ.get("GOOGLE_CLOUD_REGION")
        project_id = os.environ.get("GOOGLE_CLOUD_PROJECT_NAME")
        model_name = "codestral"
        model_version = "2405"

        client = MistralGoogleCloud(region=region, project_id=project_id)

        resp = client.fim.complete(
            model = f"{model_name}-{model_version}",
            prompt="def count_words_in_file(file_path: str) -> int:",
            suffix="return n_words"
        )

        print(resp.choices[0].message.content)
        ```

    </TabItem>
    <TabItem value="ts" label="TypeScript">

        ```typescript
        import { MistralGoogleCloud } from "@mistralai/mistralai-gcp";

        const client = new MistralGoogleCloud({
            region: process.env.GOOGLE_CLOUD_REGION || "",
            projectId: process.env.GOOGLE_CLOUD_PROJECT_ID || "",
        });

        const modelName = "codestral";
        const modelVersion = "2405";

        async function fimCompletion(prompt: string, suffix: string) {
            const resp = await client.fim.complete({
                model: modelName + "-" + modelVersion,
                prompt: prompt,
                suffix: suffix
            });
            if (resp.choices && resp.choices.length > 0) {
                console.log(resp.choices[0]);
            }
        }

        fimCompletion("def count_words_in_file(file_path: str) -> int:",
                      "return n_words");
        ```
    </TabItem>
</Tabs>


## Going further

For more information and examples, you can check:

- The Google Cloud [Partner Models](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/mistral)
  documentation page.
- The Vertex Model Cards for [Mistral Large](https://console.cloud.google.com/vertex-ai/publishers/mistralai/model-garden/mistral-large),
  [Mistral-NeMo](https://console.cloud.google.com/vertex-ai/publishers/mistralai/model-garden/mistral-nemo) and
  [Codestral](https://console.cloud.google.com/vertex-ai/publishers/mistralai/model-garden/codestral).
- The [Getting Started Colab Notebook](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/generative_ai/mistralai_intro.ipynb)
  for Mistral models on Vertex, along with the [source file on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/main/notebooks/official/generative_ai/mistralai_intro.ipynb).


[Workspaces]
Source: https://docs.mistral.ai/docs/deployment/laplateforme/organization

A La Plateforme workspace is a collective of accounts, each with a designated set of rights and permissions. Creating a workspace for your team enables you to:
- Manage access and costs
- Share fine-tuneds models among team members 

:::tip[ ]
When you generate an API key from your organization's workspace and use it to create a fine-tuned model, 
your team members will be able to use this model. 
This ensures that the model is accessible and usable by all authorized team members.
:::

## Create a workspace 

When you first join La Plateforme, you can either create or join a workspace. 
Click on "Create workspace" to create and set up your workspace. 

<img src="/img/org_join.png" width="80%"/>

Alternatively, if you are already in La Plateforme, click on your name in the bottom left section, 
followed by selecting "Create or join workspace".
<img src="/img/org_create2.png" width="85%"/>

You can create your workspace for your own or your organization. 

## Switch to a workspace 
You can switch between your personal workspace and your organization workspace. 
<img src="/img/org_switch.png" width="85%"/>


## Invite members to your organization 

To invite members to your organization, navigate to "Workspace - Members"
and click "Invite a new member". 


<img src="/img/org_invite2.png" width="75%"/>


[La Plateforme]
Source: https://docs.mistral.ai/docs/deployment/laplateforme/overview

[platform_url]: https://console.mistral.ai/
[deployment_img]: /img/deployment.png
[deployment_url]: https://console.mistral.ai/


Mistral AI currently provides three types of access to Large Language Models: 
- **La Plateforme**: We provide API endpoints through [La Plateforme][platform_url] providing pay-as-you-go access to our latest models.
- **Cloud**: You can access Mistral AI models via your preferred [cloud platforms](/deployment/cloud/overview/).
- **Self-deployment**: You can self-deploy our open-weights models on your own on-premise infrastructure. Our open weights models are available under the [Apache 2.0](https://github.com/apache/.github/blob/main/LICENSE) License, available on [Hugging Face](https://huggingface.co/mistralai) or directly from [the documentation](/getting-started/models/weights).

[![deployment_img]][deployment_url]

### API Access with the La Plateforme

You will need to activate payments on your account to enable your API keys in the [La Plateforme][platform_url]. Check out the [Quickstart](/getting-started/quickstart/) guide to get started with your first Mistral API request. 

Explore the capabilities of our models:
- [Completion](/capabilities/completion)
- [Embeddings](/capabilities/embeddings/overview)
- [Function calling](/capabilities/function_calling)
- [JSON mode](/capabilities/structured-output/json_mode)
- [Guardrailing](/capabilities/guardrailing)


### Cloud-based deployments

For a comprehensive list of options to deploy and consume Mistral AI models on the cloud, head on to the **[cloud deployment section](/deployment/cloud/overview)**.

### Raw model weights

Raw model weights can be used in several ways: 
- For self-deployment, on cloud or on premise, using either [TensorRT-LLM](/deployment/self-deployment/trt) or [vLLM](/deployment/self-deployment/vllm), head on to **[Deployment](/deployment/self-deployment/skypilot)**
- For research, head-on to our [reference implementation repository](https://github.com/mistralai/mistral-src),
- For local deployment on consumer grade hardware, check out the [llama.cpp](https://github.com/ggerganov/llama.cpp) project or [Ollama](https://ollama.ai/).


[Pricing]
Source: https://docs.mistral.ai/docs/deployment/laplateforme/pricing

:::note[ ]
Please refer to the [pricing page](https://mistral.ai/pricing#api-pricing) for detailed information on costs.
:::


[Rate limit and usage tiers]
Source: https://docs.mistral.ai/docs/deployment/laplateforme/tier

:::note[ ]
Please visit https://admin.mistral.ai/plateforme/limits for detailed information on the current rate limit and usage tiers for your workspace. 
:::

## How does rate limits rate work? 

To prevent misuse and manage the capacity of our API, we have implemented limits on how much a workspace can utilize the Mistral API.

We offer two types of rate limits:

- Requests per second (RPS)
- Tokens per minute/month

Key points to note:

- Rate limits are set at the workspace level.
- Limits are defined by usage tier, where each tier is associated with a different set of rate limits.
- In case you need to raise your usage limits, please feel free to contact us by utilizing the support button, providing details about your specific use case.

## Usage tiers 

You can view the rate and usage limits for your workspace under the [limits](https://admin.mistral.ai/plateforme/limits) section on la Plateforme.

We offer various tiers on the platform, including a **free API tier** with restrictive rate limits. The free API tier is designed to allow you to try and explore our API. For actual projects and production use, we recommend upgrading to a higher tier.


[Deploy with Cerebrium]
Source: https://docs.mistral.ai/docs/deployment/self-deployment/cerebrium

[Cerebrium](https://www.cerebrium.ai/) is a serverless AI infrastructure platform that makes it easier for companies to build and deploy AI based applications. They offer Serverless GPU's with low cold start times with over 12 varieties of GPU chips that auto scale and you only pay for the compute you use.

## Setup Cerebrium

First, we install Cerebrium and login to get authenticated.

```bash
pip install cerebrium
cerebrium login
```

Then let us create our first project

```bash
cerebrium init mistral-vllm
```

## Setup Environment and Hardware

You set up your environment and hardware in the **cerebrium.toml** file that was created using the init function above. Here we are using a Ampere A10 GPU etc.
You can read more [here](https://docs.cerebrium.ai/cerebrium/environments/custom-images)

```toml
[cerebrium.deployment]
name = "mistral-vllm"
python_version = "3.11"
docker_base_image_url = "debian:bookworm-slim"
include = "[./*, main.py, cerebrium.toml]"
exclude = "[.*]"

[cerebrium.hardware]
cpu = 2
memory = 14.0
compute = "AMPERE_A10"
gpu_count = 1
provider = "aws"
region = "us-east-1"

[cerebrium.dependencies.pip]
sentencepiece = "latest"
torch = ">=2.0.0"
vllm = "latest"
transformers = ">=4.35.0"
accelerate = "latest"
xformers = "latest"
```

## Setup inference

Running code in Cerebrium is like writing normal python with no special syntax. In your **main.py** specify the following:

```python
from vllm import LLM, SamplingParams
from huggingface_hub import login
from cerebrium import get_secret