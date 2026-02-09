# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/integrations/llms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# LLMs

> Integrate large language models (LLMs) into Galileo Evaluate to assess performance, refine outputs, and enhance generative AI model capabilities.

<Info>
  This section only applies if you want to:

  * Query your LLMs via the Galileo Playground or via promptquality.runs()
  * Or leverage any of our the metrics that are powered by OpenAI / Azure models. If you have an application or prototype where you're querying a model in code you can integrate Galileo into your code. Jump to [Evaluating and Optimizing Agents, Chains, or multi-stage workflows](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-agents--chains-or-multi-step-workflows) to learn more.
</Info>

Galileo integrates with publicly accessible LLM APIs as well as Open Source LLMs (privately hosted). Before you start using **Evaluate** on your own LLMs, you need to set up your models on the system.

* Go to the 'Galileo Home Page'.
* Click on your 'Profile' (bottom left).
* Client on 'Settings & Permissions'.
* Click on 'Integrations'.

You can set up and manage all your LLM API and Custom Model integrations from the 'Integrations' page.

<Info>*Note:* These integrations are user-specific to ensure that different users in an organization can use their own API keys when interacting with the LLMs.</Info>

## Public APIs supported

### OpenAI

We support both the [Chat](https://platform.openai.com/docs/api-reference/chat) and [Completions](https://platform.openai.com/docs/api-reference/completions) APIs from OpenAI, with all of the active models. This can be set up from the Galileo console or from the [Python client](https://promptquality.docs.rungalileo.io/#promptquality.add_openai_integration).

<Info>
  *Note:* OpenAI Models power a few of Galileo's Guardrail Metrics (e.g. Correctness, Context Adherence, Chunk Attribution, Chunk Utilization, Completeness). To improve your evaluation experience, we recommend setting up this integration
  even if the model you're prompting or testing is a different one.
</Info>

### Azure OpenAI

If you use OpenAI models through Azure, you can set up your Azure integration. This can be set up from the Galileo console or from the [Python client](https://promptquality.docs.rungalileo.io/#promptquality.add_azure_integration).

### Google Vertex AI

For integrating with models served by Google via Vertex AI (like PaLM 2 and Gemini), we recommend setting up a Service Account within your Google Cloud project that has [Vertex AI enabled](/galileo/gen-ai-studio-products/galileo-evaluate/integrations/llms). This service account requires at minimum [the 'Vertex AI User (roles/aiplatform.user)' role's policies](https://cloud.google.com/vertex-ai/docs/generative-ai/access-control) to be attached.

Once the role is created, create a new key for this service account. The contents of the JSON file provided are what you'll copy over into the Integrations page for Galileo.

<Info>by Google Vertex AI. Galileo's ChainPoll metrics **are** available, but perplexity and uncertainty scores are not available for model predictions from Google Vertex AI.</Info>

### AWS Bedrock

Add your AWS Bedrock integration in the Galileo Integrations page. You should see a green light indicating a successful integration. Now, you should see new **Bedrock models** show up in the Prompt Playground.

<Info>Uncertainty and Galileo ChainPoll metrics cannot be generated using models served by AWS Bedrock.</Info>

### AWS Sagemaker

If you're hosting models on AWS Sagemaker, you can query them via Galileo. Set up your AWS Sagemaker integration via the Integrations page.

You'll need to enter your authentication credentials (as an access key \<> secret pair or an AWS role that can be assumed) alongwith the AWS region in which your endpoints are hosted. For each endpoint, you can configure the name of the endpoint and an alias alongwith the schema mapping in [`dpath notation`](https://pypi.org/project/dpath/).

Required parameters for each endpoint are:

* Prompt: To pass the prompt to the payload.

* Response: To parse the response from the response.

Optional parameters, which are included in the payload if set, are:

* Temperature
* Max tokens
* Top K
* Top P
* Frequency penalty
* Presence penalty

Check out [this video](https://www.loom.com/share/27a11ceb14b94c84a6248c67515edee8) for step-by-step instructions.

<Info>Uncertainty and Galileo ChainPoll metrics cannot be generated using models served by AWS Sagemaker.</Info>

### Other Custom Models

If you are prompting via [Langchain](https://python.langchain.com/docs/get_started/introduction), Galileo can use custom models through Langchain the same way you might use OpenAI in Langchain. Check out '[Using Prompt with Chains or multi-step workflows](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-agents--chains-or-multi-step-workflows)' for more details on how to integrate Galileo into your Langchain application.

To prompt your custom models through the Galileo UI, they need to be hosted on AWS Sagemaker ([see above](/galileo/gen-ai-studio-products/galileo-evaluate/integrations/llms#aws-sagemaker)).
