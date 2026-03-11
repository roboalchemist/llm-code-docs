# Source: https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview?pivots=programming-language-javascript

Title: Get started with Microsoft Foundry SDKs and Endpoints - Microsoft Foundry

URL Source: https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview?pivots=programming-language-javascript

Published Time: Mon, 09 Mar 2026 22:19:41 GMT

Markdown Content:
A Foundry resource provides unified access to models, agents, and tools. This article explains which SDK and endpoint to use for your scenario.

| SDK | What it's for | Endpoint |
| --- | --- | --- |
| **Foundry SDK** | Foundry-specific capabilities with OpenAI-compatible interfaces. Includes access to Foundry direct models through the Responses API (not Chat Completions). | `https://<resource-name>.services.ai.azure.com/api/projects/<project-name>` |
| **OpenAI SDK** | Latest OpenAI SDK models and features with the full OpenAI API surface. Foundry direct models available through Chat Completions API (not Responses). | `https://<resource-name>.openai.azure.com/openai/v1` |
| **Foundry Tools SDKs** | Prebuilt solutions (Vision, Speech, Content Safety, and more). | Tool-specific endpoints (varies by service). |
| **Agent Framework** | Multi-agent orchestration in code. Cloud-agnostic. | Uses the project endpoint via the Foundry SDK. |

**Choose your SDK**:

*   Use **Foundry SDK** when building apps with agents, evaluations, or Foundry-specific features
*   Use **OpenAI SDK** when maximum OpenAI compatibility is required, or using Foundry direct models via Chat Completions
*   Use **Foundry Tools SDKs** when working with specific AI services (Vision, Speech, Language, etc.)
*   Use **Agent Framework** when building multi-agent systems in code (local orchestration)

Note

**Resource types:** A Foundry resource provides all endpoints previously listed. An Azure OpenAI resource provides only the `/openai/v1` endpoint.

**Authentication:** Samples here use Microsoft Entra ID (`DefaultAzureCredential`). API keys work on `/openai/v1`. Pass the key as `api_key` instead of a token provider.

*   An Azure account with an active subscription. If you don't have one, create a [free Azure account, which includes a free trial subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

*   Have one of the following Azure RBAC roles to create and manage Foundry resources:

    *   **Azure AI User** (least-privilege role for development)
    *   **Azure AI Project Manager** (for managing Foundry projects)
    *   **Contributor** or **Owner** (for subscription-level permissions)

For details on each role's permissions, see [Role-based access control for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry).

*   Install the required language runtimes, global tools, and VS Code extensions as described in [Prepare your development environment](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/install-cli-sdk).

Important

Before starting, make sure your development environment is ready.

 This article focuses on **scenario-specific steps** like SDK installation, authentication, and running sample code.

Before proceeding, confirm:

*   [ ] Azure subscription is active: `az account show`
*   [ ] You have the required RBAC role: Check Azure portal → Foundry resource → Access control (IAM)
*   [ ] Language runtime installed: 
    *   Python: `python --version` (≥3.8)
    *   Node.js: `node --version` (≥18)
    *   .NET: `dotnet --version` (≥6.0)
    *   Java: `java --version` (≥11)

The Foundry SDK connects to a single project endpoint that provides access to the most popular Foundry capabilities:

```
https://<resource-name>.services.ai.azure.com/api/projects/<project-name>
```

Note

If your organization uses a custom subdomain, replace `<resource-name>` with `<your-custom-subdomain>` in the endpoint URL.

This approach simplifies application configuration. Instead of managing multiple endpoints, you configure one.

Note

**SDK versions:** The 2.x preview SDK targets the new Foundry portal and API. The 1.x GA SDK targets Foundry classic. Make sure the samples you follow match your installed package.

| SDK Version | Portal Version | Status | Python Package |
| --- | --- | --- | --- |
| 2.x (GA) | Foundry (new) | Preview | `azure-ai-projects>=2.0.0` |
| 1.x (GA) | Foundry classic | Stable | `azure-ai-projects==1.0.0` |

The [Azure AI Projects client library for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme?view=azure-python-preview) is a unified library that enables you to use multiple client libraries together by connecting to a single project endpoint.

Run this command to install the preview packages for Foundry projects.

```
pip install azure-ai-projects >=2.0.0
```

| SDK Version | Portal Version | Status | Java Package |
| --- | --- | --- | --- |
| 1.0.0-beta.3 1.0.0-beta.1 | Foundry (new) | Preview | `azure-ai-projects` `azure-ai-agents` |

| SDK Version | Portal Version | Status | JavaScript Package |
| --- | --- | --- | --- |
| 2.0.0-beta.4 (preview) | Foundry (new) | Preview | `@azure/ai-projects 'prerelease'` |
| 1.0.1 | Foundry classic | Stable | `@azure/ai-projects` |

| SDK Version | Portal Version | Status | .NET Package |
| --- | --- | --- | --- |
| 1.2.0-beta.5 (preview) | Foundry (new) | Preview | `Azure.AI.Projects` `Azure.AI.Projects.Openai` |
| 1.x (GA) | Foundry classic | Stable | `Azure.AI.Projects` |

The [Azure AI Projects client library for Java (preview)](https://learn.microsoft.com/en-us/java/api/overview/azure/ai-projects-readme) is a unified library that enables you to use multiple client libraries together by connecting to a single project endpoint.

Important

Items marked (preview) in this article are currently in public preview. This preview is provided without a service-level agreement, and we don't recommend it for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

Add these packages to your installation for Foundry projects.

```
package com.azure.ai.agents;

import com.azure.core.util.Configuration;
import com.azure.identity.DefaultAzureCredentialBuilder;
import com.openai.models.responses.Response;
import com.openai.models.responses.ResponseCreateParams;
```

The [Azure AI Projects client library for JavaScript](https://learn.microsoft.com/en-us/javascript/api/overview/azure/ai-projects-readme) is a unified library that enables you to use multiple client libraries together by connecting to a single project endpoint.

Run this command to install the preview JavaScript packages for Foundry projects.

```
npm install @azure/ai-projects@beta @azure/identity dotenv
```

The [Azure AI Projects client library for .NET](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/ai.projects-readme) is a unified library that enables you to use multiple client libraries together by connecting to a single project endpoint.

Run this command to add the Azure.AI.Projects package to your .NET project.

```
dotnet add package Azure.AI.Projects --prerelease
dotnet add package Azure.AI.Projects.OpenAI --prerelease
dotnet add package Azure.Identity
```

The SDK exposes two client types because Foundry and OpenAI have different API shapes:

*   **Project client** – Use for Foundry-native operations where OpenAI has no equivalent. Examples: listing connections, retrieving project properties, enabling tracing.
*   **OpenAI-compatible client** – Use for Foundry functionality that builds on OpenAI concepts. The Responses API, agents, evaluations, and fine-tuning all use OpenAI-style request/response patterns. This client also gives you access to Foundry direct models (non-Azure-OpenAI models hosted in Foundry). The project endpoint serves this traffic on the `/openai` route.

Most apps use both clients. Use the project client for setup and configuration, then use the OpenAI-compatible client for running agents, evaluations, and calling models (including Foundry direct models).

**Create a project client:**

```
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_client = AIProjectClient(
  endpoint="https://<resource-name>.services.ai.azure.com/api/projects/<project-name>",
  credential=DefaultAzureCredential())
```

**Create an OpenAI-compatible client from your project:**

```
with project_client.get_openai_client() as openai_client:
    response = openai_client.responses.create(
        model="gpt-5.2",
        input="What is the size of France in square miles?",
    )
    print(f"Response output: {response.output_text}")
```

**Expected output**:

```
Response output: France has an area of approximately 213,011 square miles (551,695 square kilometers).
```

**Create a project client:**

```
import com.azure.ai.projects.ProjectsClient;
import com.azure.ai.projects.ProjectsClientBuilder;
import com.azure.identity.DefaultAzureCredentialBuilder;

String endpoint = "https://<resource-name>.services.ai.azure.com/api/projects/<project-name>";

ProjectsClient projectClient = new ProjectsClientBuilder()
    .credential(new DefaultAzureCredentialBuilder().build())
    .endpoint(endpoint)
    .buildClient();
```**Create and use an OpenAI-compatible client from your project:**
```java
OpenAIClient openAIClient = projectClient.getOpenAIClient();
```

**Create a project client:**

```
import { DefaultAzureCredential } from "@azure/identity";
import { AIProjectClient } from "@azure/ai-projects";
import "dotenv/config";

const projectEndpoint = "https://<resource-name>.services.ai.azure.com/api/projects/<project-name>";
const deploymentName = "gpt-5.2";
const project = new AIProjectClient(projectEndpoint, new DefaultAzureCredential());
```

**Create an OpenAI-compatible client from your project:**

```
const openAIClient = await project.getOpenAIClient();
const response = await openAIClient.responses.create({
    model: deploymentName,
    input: "What is the size of France in square miles?",
});
console.log(`Response output: ${response.output_text}`);
```

**Create a project client:**

```
using Azure.AI.Projects.OpenAI; 
using Azure.Identity;
using OpenAI.Responses;

string endpoint = "https://<resource-name>.services.ai.azure.com/api/projects/<project-name>";

AIProjectClient projectClient = new(
    endpoint: new Uri(endpoint), 
    tokenProvider: new DefaultAzureCredential());
```

**Create an OpenAI-compatible client from your project:**

```
#pragma warning disable OPENAI001
OpenAIResponseClient responseClient = projectClient.OpenAI.GetProjectResponsesClientForModel("gpt-5.2");
OpenAIResponse response = responseClient.CreateResponse("What is the speed of light?");
Console.WriteLine(response.GetOutputText());
#pragma warning restore OPENAI001
```

*   [Access Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code), including Azure OpenAI
*   [Use the Foundry Agent Service](https://learn.microsoft.com/en-us/azure/ai-services/agents/quickstart?context=/azure/ai-foundry/context/context)
*   [Run cloud evaluations](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/cloud-evaluation)
*   [Enable app tracing](https://learn.microsoft.com/en-us/azure/foundry-classic/how-to/develop/trace-application)
*   [Fine-tune a model](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning?tabs=azure-openai&pivots=programming-language-python)
*   Get endpoints and keys for Foundry Tools, local orchestration, and more

If you see `DefaultAzureCredential failed to retrieve a token`:

1.   **Verify Azure CLI is authenticated**:

```
az account show
az login  # if not logged in
```
2.   **Check RBAC role assignment**:

    *   Confirm you have at least the Azure AI User role on the Foundry project
    *   See [Assign Azure roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)

3.   **For managed identity in production**:

    *   Ensure the managed identity has the appropriate role assigned
    *   See [Configure managed identities](https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry#identity-types)

If you see `Connection refused` or `404 Not Found`:

*   **Verify resource and project names** match your actual deployment
*   **Check endpoint URL format**: Should be `https://<resource-name>.services.ai.azure.com/api/projects/<project-name>`
*   **For custom subdomains**: Replace `<resource-name>` with your custom subdomain

If code samples fail with `AttributeError` or `ModuleNotFoundError`:

*   **Check SDK version**: 
```
pip show azure-ai-projects  # Python
npm list @azure/ai-projects  # JavaScript
dotnet list package  # .NET
```
*   **Verify moniker alignment**: 2.x SDK requires Foundry portal, 1.x SDK requires Foundry classic
*   **Reinstall with correct version flags**: See installation commands in each language section above

Use the OpenAI SDK when you want the full OpenAI API surface and maximum client compatibility. This endpoint provides access to Azure OpenAI models and Foundry direct models (via Responses API). It doesn't provide access to Foundry-specific features like agents and evaluations.

The following snippet shows how to use the Azure OpenAI `/openai/v1` endpoint directly.

```
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(  
  base_url = "https://<resource-name>.openai.azure.com/openai/v1/",  
  api_key=token_provider,
)

response = client.responses.create(
    model="model_deployment_name",
    input= "What is the size of France in square miles?" 
)

print(response.model_dump_json(indent=2))
```

**Expected output**:

```
{
  "id": "resp_abc123",
  "object": "response",
  "created": 1234567890,
  "model": "gpt-5.2",
  "output_text": "France has an area of approximately 213,011 square miles (551,695 square kilometers)."
}
```

For more information, see [Azure OpenAI supported programming languages](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-entra&pivots=programming-language-python)

Important

Items marked (preview) in this article are currently in public preview. This preview is provided without a service-level agreement, and we don't recommend it for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

The following snippet shows how to use the Azure OpenAI `/openai/v1` endpoint directly.

```
import com.azure.identity.AuthenticationUtil;
import com.azure.identity.DefaultAzureCredential;
import com.azure.identity.DefaultAzureCredentialBuilder;
import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.credential.BearerTokenCredential;

import java.util.function.Supplier;

DefaultAzureCredential tokenCredential = new DefaultAzureCredentialBuilder().build();
String endpoint = "https://<resource-name>.openai.azure.com/openai/v1";
String deploymentName = "gpt-5.2";
Supplier<String> bearerTokenSupplier = AuthenticationUtil.getBearerTokenSupplier(
        tokenCredential, "https://cognitiveservices.azure.com/.default");
OpenAIClient openAIClient = OpenAIOkHttpClient.builder()
        .baseUrl(endpoint)
        .credential(BearerTokenCredential.create(bearerTokenSupplier))
        .build();

ResponseCreateParams responseCreateParams = ResponseCreateParams.builder()
        .input("What is the speed of light?")
        .model(deploymentName) 
        .build();

Response response = openAIClient.responses().create(responseCreateParams);

System.out.println("Response output: " + response.getOutputText());
```

For more information on using the OpenAI SDK, see [Azure OpenAI supported programming languages](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-entra&pivots=programming-language-java)

```
const endpoint = "https://<resource-name>.openai.azure.com/openai/v1";
const scope = "https://cognitiveservices.azure.com/.default";
const azureADTokenProvider = getBearerTokenProvider(new DefaultAzureCredential(), scope);
const client = new OpenAI({ baseURL: endpoint, apiKey: azureADTokenProvider });
const response = await client.responses.create({
        model: deploymentName,
        input: "What is the size of France in square miles?",
    });
console.log(`Response output: ${response.output_text}`);
```

For more information on using the OpenAI SDK, see [Azure OpenAI supported programming languages](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-entra&pivots=programming-language-javascript)

1.   Install the OpenAI package: Run this command to add the OpenAI client library to your .NET project. 
```
dotnet add package OpenAI
```When it succeeds, the .NET CLI confirms that it installed the `OpenAI` package.

This snippet configures `DefaultAzureCredential`, builds `OpenAIClientOptions`, and creates a `ResponseClient` for the Azure OpenAI v1 endpoint.
```csharp
using Azure.Identity;
using Azure.Core;
using OpenAI;
using System;
using System.ClientModel.Primitives;

#pragma warning disable OPENAI001

const string directModelEndpoint  = "https://<resource-name>.openai.azure.com/openai/v1/";
const string deploymentName = "gpt-5.2";    

BearerTokenPolicy tokenPolicy = new(
     new DefaultAzureCredential(),
     "https://cognitiveservices.azure.com/.default");

OpenAIResponseClient client = new(
     model: deploymentName,
     authenticationPolicy: tokenPolicy, // To use Entra 
  // credential: new ApiKeyCredential("<YOUR-AZURE-OPENAI-API-KEY>") // To use APIKEY 
     options: new OpenAIClientOptions()
     {
         Endpoint = new($"{directModelEndpoint}"),
     });
ResponseCreationOptions options = new ResponseCreationOptions
 {
     Temperature = (float)0.7,
 };

OpenAIResponse modelDirectResponse = client.CreateResponse(
      [
         ResponseItem.CreateUserMessageItem("What is the size of France in square miles?"),
      ], options);

Console.WriteLine($"[ASSISTANT]: {modelDirectResponse.GetOutputText()}");
#pragma warning restore OPENAI001
// The ResponseClient lets you interact with models and services in your project.
```

For more information on using the OpenAI SDK, see [Azure OpenAI supported programming languages](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-entra&pivots=programming-language-programming-language-dotnet)

Microsoft Agent Framework is an open-source SDK for building multi-agent systems in code (for example, .NET and Python) with a cloud-provider-agnostic interface.

Use Agent Framework when you want to define and orchestrate agents locally. Pair it with the Foundry SDK when you want those agents to run against Foundry models or when you want Agent Framework to orchestrate agents hosted in Foundry.

For more information, see the [Microsoft Agent Framework overview](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview).

Foundry Tools (formerly Azure AI Services) are prebuilt point solutions with dedicated SDKs. Use the following endpoints to work with Foundry Tools.

Choose an endpoint based on your needs:

Use the Azure AI Services endpoint to access Computer Vision, Content Safety, Document Intelligence, Language, Translation, and Token Foundry Tools.

Foundry Tools endpoint: `https://<your-resource-name>.cognitiveservices.azure.com/`

Note

Endpoints use either your resource name or a custom subdomain. If your organization set up a custom subdomain, replace `your-resource-name` with `your-custom-subdomain` in all endpoint examples.

For Speech and Translation Foundry Tools, use the endpoints in the following tables. Replace placeholders with your resource information.

| Foundry Tool | Endpoint |
| --- | --- |
| Speech to Text (Standard) | `https://<YOUR-RESOURCE-REGION>.stt.speech.microsoft.com` |
| Text to Speech (Neural) | `https://<YOUR-RESOURCE-REGION>.tts.speech.microsoft.com` |
| Custom Voice | `https://<YOUR-RESOURCE-NAME>.cognitiveservices.azure.com/` |

| Foundry Tool | Endpoint |
| --- | --- |
| Text Translation | `https://api.cognitive.microsofttranslator.com/` |
| Document Translation | `https://<YOUR-RESOURCE-NAME>.cognitiveservices.azure.com/` |

The following sections include quickstart links for the Foundry Tools SDKs and reference information.

| Foundry Tool | Description | Quickstarts and reference documentation |
| --- | --- | --- |
| ![Image 1: Speech icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/speech.svg)[Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview) | Add speech to text, text to speech, translation, and speaker recognition capabilities to applications. | •[Speech to text quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text?tabs=windows&pivots=programming-language-csharp) •[Text to speech quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-text-to-speech?tabs=windows&pivots=programming-language-csharp) •[Speech translation quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-translation?tabs=windows&pivots=programming-language-csharp) •[Speech SDK for .NET](https://learn.microsoft.com/en-us/dotnet/api/microsoft.cognitiveservices.speech?view=azure-dotnet&branch=main) •[Speech NuGet package (Speech CLI)](https://www.nuget.org/packages/Microsoft.CognitiveServices.Speech.CLI) |
| ![Image 2: Language icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/language.svg)[Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview) | Build applications with natural language understanding capabilities. | •[Custom question answering (CQA) quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/question-answering/quickstart/sdk?tabs=windows&pivots=programming-language-csharp) •[Entity linking quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/entity-linking/quickstart?tabs=windows&pivots=programming-language-csharp) •[Language detection quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/language-detection/quickstart?tabs=windows&pivots=programming-language-csharp) •[Key Phrase extraction quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/key-phrase-extraction/quickstart?tabs=windows&pivots=programming-language-csharp) •[Detecting named entities (NER) quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/quickstart?&tabs=windows%2Cga-api&pivots=programming-language-csharp) •[Detect Personally Identifiable Information (PII) quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/quickstart?&tabs=windows&pivots=programming-language-csharp) •[Sentiment analysis and opinion mining quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/quickstart?tabs=windows&pivots=programming-language-csharp) •[Using text, document and conversation summarization quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/summarization/quickstart?tabs=text-summarization%2Cwindows&pivots=programming-language-csharp) •[Using Text Analytics for health quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/text-analytics-for-health/quickstart?tabs=windows&pivots=programming-language-csharp) •[Language SDK for .NET (text analysis)](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/ai.textanalytics-readme?view=azure-dotnet) •[Language NuGet package (text analysis)](https://www.nuget.org/packages/Azure.AI.TextAnalytics) •[Language SDK for .NET (Question Answering)](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/ai.language.questionanswering-readme?view=azure-dotnet) •[Language NuGet package (question answering)](https://www.nuget.org/packages/Azure.AI.Language.QuestionAnswering) |
| ![Image 3: Translator icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/translator.svg)[Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/overview) | Use AI-powered translation technology to translate more than 100 in-use, at-risk, and endangered languages and dialects. | •[Translator SDK for .NET (text)](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/ai.translation.text-readme?view=azure-dotnet-preview) •[Translator NuGet package (text)](https://www.nuget.org/packages/Azure.AI.Translation.Text/1.0.0-beta.1) •[Translator SDK for .NET (batch)](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/AI.Translation.Document-readme?view=azure-dotnet) •[Translator NuGet package (batch)](https://www.nuget.org/packages/Azure.AI.Translation.Document) |
| ![Image 4: Azure AI Search icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/search.svg)[Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) | Bring AI-powered cloud search to your mobile and web apps. | •[Use agentic retrieval quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-agentic-retrieval?tabs=search-perms%2Csearch-endpoint&pivots=programming-language-csharp) •[Vector search quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-vector?tabs=keyless&pivots=csharp) •[Classic generative search (RAG) using grounding data quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-rag?pivots=csharp) •[Full-text search quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-text?tabs=keyless%2Cwindows&pivots=csharp) •[Semantic ranking quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-semantic?pivots=csharp) •[Chat with Azure OpenAI models using your own data quickstart](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/use-your-data-quickstart?viewFallbackFrom=foundry&context=%2Fazure%2Fsearch%2Fcontext%2Fcontext&tabs=keyless%2Ctypescript-keyless%2Cpython-new&pivots=programming-language-csharp) •[Azure AI Search SDK for .NET](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/search.documents-readme?view=azure-dotnet) •[Azure AI Search NuGet package](https://www.nuget.org/packages/Azure.Search.Documents/11.6.0-beta.2) |
| ![Image 5: Content Safety icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/content-safety.svg)[Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview) | Detect harmful content in applications and services. | •[Analyze text content quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Cwindows&pivots=programming-language-csharp) •[Use a text blocklist quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-blocklist?tabs=visual-studio%2Cwindows&pivots=programming-language-csharp) •[Analyze image content quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-image?tabs=visual-studio%2Cwindows&pivots=programming-language-csharp) •[Content Safety SDK for .NET](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/ai.contentsafety-readme?view=azure-dotnet) •[Content Safety NuGet package](https://www.nuget.org/packages/Azure.AI.ContentSafety/1.0.0) |
| ![Image 6: Document Intelligence icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/document-intelligence.svg)[Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview) | Turn documents into intelligent data-driven solutions. | •[Document Intelligence quickstart](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?view=doc-intel-4.0.0&pivots=programming-language-csharp) •[Document Intelligence SDK for .NET](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/ai.documentintelligence-readme?view=azure-dotnet-preview) •[Document Intelligence NuGet package](https://www.nuget.org/packages/Azure.AI.DocumentIntelligence/1.0.0-beta.1) |
| ![Image 7: Vision icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/vision.svg)[Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview) | Analyze content in digital images and rich media assets. | •[Azure Vision in Foundry Tools v3.2 GA Read quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/client-library?tabs=windows%2Cvisual-studio&programming-language-csharp) •[Image Analysis quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40?tabs=windows%2Cvisual-studio&programming-language-csharp) •[Use the Face service quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/identity-client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-csharp) •[Vision SDK for .NET](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/AI.Vision.ImageAnalysis-readme?view=azure-dotnet-preview) •[Vision NuGet package](https://www.nuget.org/packages/Azure.AI.Vision.ImageAnalysis) |

| Foundry Tool | Description | Quickstarts and reference documentation |
| --- | --- | --- |
| ![Image 8: Speech icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/speech.svg)[Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview) | Add speech to text, text to speech, translation, and speaker recognition capabilities to applications. | •[Speech to text quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text?tabs=windows&pivots=programming-language-java) •[Text to speech quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-text-to-speech?tabs=windows&pivots=programming-language-java) •[Speech translation quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-translation?tabs=windows&pivots=programming-language-java) •[Speech SDK for Java](https://learn.microsoft.com/en-us/java/api/com.microsoft.cognitiveservices.speech?view=azure-java-stable&branch=main) •[Speech Maven package](https://central.sonatype.com/artifact/com.microsoft.cognitiveservices.speech/client-sdk/1.34.0?smo=true) |
| ![Image 9: Language icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/language.svg)[Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview) | Build applications with natural language understanding capabilities. | •[Entity linking quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/entity-linking/quickstart?tabs=windows&pivots=programming-language-java) •[Language detection quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/language-detection/quickstart?tabs=windows&pivots=programming-language-java) •[Key Phrase extraction quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/key-phrase-extraction/quickstart?tabs=windows&pivots=programming-language-java) •[Detecting named entities (NER) quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/quickstart?&tabs=windows%2Cga-api&pivots=programming-language-java) •[Detect Personally Identifiable Information (PII) quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/quickstart?&tabs=windows&pivots=programming-language-java) •[Sentiment analysis and opinion mining quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/quickstart?tabs=windows&pivots=programming-language-java) •[Using text, document and conversation summarization quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/summarization/quickstart?tabs=text-summarization%2Cwindows&pivots=programming-language-java) •[Using Text Analytics for health quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/text-analytics-for-health/quickstart?tabs=windows&pivots=programming-language-java) •[Language SDK for Java (text analysis)](https://learn.microsoft.com/en-us/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-stable) •[Language Maven package](https://central.sonatype.com/artifact/com.microsoft.azure.cognitiveservices/azure-cognitiveservices-language) |
| ![Image 10: Translator icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/translator.svg)[Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/overview) | Use AI-powered translation technology to translate more than 100 in-use, at-risk, and endangered languages and dialects. | •[Translator SDK for Java (text)](https://learn.microsoft.com/en-us/java/api/overview/azure/ai-translation-text-readme?view=azure-java-preview) •[Translator Maven package (text)](https://central.sonatype.com/artifact/com.azure/azure-ai-translation-text) |
| ![Image 11: Azure AI Search icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/search.svg)[Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) | Bring AI-powered cloud search to your mobile and web apps. | •[Use agentic retrieval quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-agentic-retrieval?tabs=search-perms%2Csearch-endpoint&pivots=programming-language-java) •[Vector search quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-vector?tabs=keyless&pivots=java) •[Classic generative search (RAG) using grounding data quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-rag?pivots=java) •[Full-text search quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-text?tabs=keyless%2Cwindows&pivots=java) •[Semantic ranking quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-semantic?pivots=java) •[Chat with Azure OpenAI models using your own data quickstart](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/use-your-data-quickstart?viewFallbackFrom=foundry&context=%2Fazure%2Fsearch%2Fcontext%2Fcontext&tabs=keyless%2Ctypescript-keyless%2Cpython-new&pivots=programming-language-java) •[Azure AI Search SDK for Java](https://learn.microsoft.com/en-us/java/api/overview/azure/search-documents-readme?view=azure-java-stable) •[Azure AI Search Maven package](https://central.sonatype.com/artifact/com.azure/azure-search-documents/11.7.0-beta.1?smo=true) |
| ![Image 12: Content Safety icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/content-safety.svg)[Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview) | Detect harmful content in applications and services. | •[Analyze text content quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Cwindows&pivots=programming-language-java) •[Use a text blocklist quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-blocklist?tabs=visual-studio%2Cwindows&pivots=programming-language-java) •[Analyze image content quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-image?tabs=visual-studio%2Cwindows&pivots=programming-language-java) •[Content Safety SDK for Java](https://learn.microsoft.com/en-us/java/api/overview/azure/ai-contentsafety-readme?view=azure-java-stable) •[Content Safety Maven package](https://central.sonatype.com/artifact/com.azure/azure-ai-contentsafety) |
| ![Image 13: Document Intelligence icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/document-intelligence.svg)[Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview) | Turn documents into intelligent data-driven solutions. | •[Document Intelligence quickstart](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?view=doc-intel-4.0.0&pivots=programming-language-java) •[Document Intelligence SDK for Java](https://learn.microsoft.com/en-us/java/api/overview/azure/ai-documentintelligence-readme?view=azure-java-preview) •[Document Intelligence Maven package](https://mvnrepository.com/artifact/com.azure/azure-ai-documentintelligence/1.0.0-beta.1) |
| ![Image 14: Vision icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/vision.svg)[Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview) | Analyze content in digital images and rich media assets. | •[Image Analysis quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40?tabs=windows%2Cvisual-studio&pivots=programming-language-java) •[Use the Face service quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/identity-client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-java) •[Vision SDK for Java](https://learn.microsoft.com/en-us/java/api/overview/azure/ai-vision-imageanalysis-readme?view=azure-java-preview) •[Vision Maven package](https://central.sonatype.com/artifact/com.azure/azure-ai-vision-imageanalysis) |

| Foundry Tool | Description | Quickstarts and reference documentation |
| --- | --- | --- |
| ![Image 15: Speech icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/speech.svg)[Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview) | Add speech to text, text to speech, translation, and speaker recognition capabilities to applications. | •[Speech to text quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text?tabs=windows&pivots=programming-language-javascript) •[Text to speech quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-text-to-speech?tabs=windows&pivots=programming-language-javascript) •[Speech translation quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-translation?tabs=windows&pivots=programming-language-javascript) •[Speech SDK for JavaScript](https://learn.microsoft.com/en-us/javascript/api/microsoft-cognitiveservices-speech-sdk/?view=azure-node-latest&branch=main) •[Speech npm package](https://www.npmjs.com/package/microsoft-cognitiveservices-speech-sdk) |
| ![Image 16: Language icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/language.svg)[Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview) | Build applications with natural language understanding capabilities. | •[Entity linking quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/entity-linking/quickstart?tabs=windows&pivots=programming-language-javascript) •[Language detection quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/language-detection/quickstart?tabs=windows&pivots=programming-language-javascript) •[Key Phrase extraction quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/key-phrase-extraction/quickstart?tabs=windows&pivots=programming-language-javascript) •[Detecting named entities (NER) quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/quickstart?&tabs=windows%2Cga-api&pivots=programming-language-javascript) •[Detect Personally Identifiable Information (PII) quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/quickstart?&tabs=windows&pivots=programming-language-javascript) •[Sentiment analysis and opinion mining quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/quickstart?tabs=windows&pivots=programming-language-javascript) •[Using text, document and conversation summarization quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/summarization/quickstart?tabs=text-summarization%2Cwindows&pivots=programming-language-javascript) •[Using Text Analytics for health quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/text-analytics-for-health/quickstart?tabs=windows&pivots=programming-language-javascript) •[Language SDK for JavaScript (text analysis)](https://learn.microsoft.com/en-us/javascript/api/overview/azure/ai-language-text-readme?view=azure-node-latest) •[Language npm package](https://www.npmjs.com/package/@azure/ai-language-text) |
| ![Image 17: Translator icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/translator.svg)[Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/overview) | Use AI-powered translation technology to translate more than 100 in-use, at-risk, and endangered languages and dialects. | •[Translator SDK for JavaScript (text)](https://learn.microsoft.com/en-us/javascript/api/overview/azure/text-translation?view=azure-node-preview) •[Translator npm package (text)](https://www.npmjs.com/package/@azure-rest/ai-translation-text/v/1.0.0-beta.1) |
| ![Image 18: Azure AI Search icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/search.svg)[Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) | Bring AI-powered cloud search to your mobile and web apps. | •[Use agentic retrieval quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-agentic-retrieval?tabs=search-perms%2Csearch-endpoint&pivots=programming-language-javascript) •[Vector search quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-vector?tabs=keyless&pivots=javascript) •[Classic generative search (RAG) using grounding data quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-rag?pivots=javascript) •[Full-text search quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-text?tabs=keyless%2Cwindows&pivots=javascript) •[Semantic ranking quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-semantic?pivots=javascript) •[Chat with Azure OpenAI models using your own data quickstart](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/use-your-data-quickstart?viewFallbackFrom=foundry&context=%2Fazure%2Fsearch%2Fcontext%2Fcontext&tabs=keyless%2Ctypescript-keyless%2Cpython-new&pivots=programming-language-javascript) •[Azure AI Search SDK for JavaScript](https://learn.microsoft.com/en-us/javascript/api/overview/azure/search-documents-readme?view=azure-node-latest) •[Azure AI Search npm package](https://www.npmjs.com/package/@azure/search-documents/v/12.0.0?activeTab=readme) |
| ![Image 19: Content Safety icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/content-safety.svg)[Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview) | Detect harmful content in applications and services. | •[Analyze text content quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Cwindows&pivots=programming-language-javascript) •[Use a text blocklist quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-blocklist?tabs=visual-studio%2Cwindows&pivots=programming-language-javascript) •[Analyze image content quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-image?tabs=visual-studio%2Cwindows&pivots=programming-language-javascript) •[Content Safety npm package](https://www.npmjs.com/package/@azure-rest/ai-content-safety/v/1.0.0-beta.1) |
| ![Image 20: Document Intelligence icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/document-intelligence.svg)[Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview) | Turn documents into intelligent data-driven solutions. | •[Document Intelligence quickstart](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?view=doc-intel-4.0.0&pivots=programming-language-javascript) •[Document Intelligence SDK for JavaScript](https://learn.microsoft.com/en-us/javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-preview) •[Document Intelligence npm package](https://www.npmjs.com/package/@azure-rest/ai-document-intelligence/v/1.0.0-beta.1) |
| ![Image 21: Vision icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/vision.svg)[Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview) | Analyze content in digital images and rich media assets. | •[Azure Vision in Foundry Tools v3.2 GA Read quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-javascript) •[Image Analysis quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40?tabs=windows%2Cvisual-studio&pivots=programming-language-javascript) •[Use the Face service quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/identity-client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-javascript) •[Vision SDK for JavaScript](https://learn.microsoft.com/en-us/javascript/api/overview/azure/ai-vision-image-analysis-rest-readme?view=azure-node-preview) •[Vision npm package](https://www.npmjs.com/package/@azure-rest/ai-vision-image-analysis/v/1.0.0-beta.2) |

| Foundry Tool | Description | Quickstarts and reference documentation |
| --- | --- | --- |
| ![Image 22: Speech icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/speech.svg)[Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview) | Add speech to text, text to speech, translation, and speaker recognition capabilities to applications. | •[Speech to text quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text?tabs=windows&pivots=programming-language-python) •[Text to speech quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-text-to-speech?tabs=windows&pivots=programming-language-python) •[Speech translation quickstart](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-translation?tabs=windows&pivots=programming-language-python) •[Speech SDK for Python](https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-speech/?view=azure-python&branch=main) •[Speech PyPi package](https://pypi.org/project/azure-cognitiveservices-speech/) |
| ![Image 23: Language icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/language.svg)[Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview) | Build applications with natural language understanding capabilities. | •[Custom question answering (CQA) quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/question-answering/quickstart/sdk?tabs=windows&pivots=programming-language-python) •[Entity linking quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/entity-linking/quickstart?tabs=windows&pivots=programming-language-python) •[Language detection quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/language-detection/quickstart?tabs=windows&pivots=programming-language-python) •[Key Phrase extraction quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/key-phrase-extraction/quickstart?tabs=windows&pivots=programming-language-python) •[Detect named entities (NER) quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/quickstart?&tabs=windows%2Cga-api&pivots=programming-language-python) •[Detect Personally Identifiable Information (PII) quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/quickstart?&tabs=windows&pivots=programming-language-python) •[Sentiment analysis and opinion mining quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/quickstart?tabs=windows&pivots=programming-language-python) •[Using text, document and conversation summarization quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/summarization/quickstart?tabs=text-summarization%2Cwindows&pivots=programming-language-python) •[Using Text Analytics for health quickstart](https://learn.microsoft.com/en-us/azure/ai-services/language-service/text-analytics-for-health/quickstart?tabs=windows&pivots=programming-language-python) •[Language SDK for Python (text analysis)](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-textanalytics-readme?view=azure-python) •[Language PyPi package (text analysis)](https://pypi.org/project/azure-cognitiveservices-language-textanalytics/) •[Language SDK for Python (question answering)](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-language-questionanswering-readme?view=azure-python) •[Language PyPi package (question answering)](https://pypi.org/project/azure-ai-language-questionanswering/) •[Language SDK for Python (language conversations)](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-language-conversations-readme?view=azure-python) •[Language PyPi package (language conversations)](https://pypi.org/project/azure-ai-language-conversations/) |
| ![Image 24: Translator icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/translator.svg)[Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/overview) | Use AI-powered translation technology to translate more than 100 in-use, at-risk, and endangered languages and dialects. | •[Translator SDK for Python (text)](https://learn.microsoft.com/en-us/python/api/azure-ai-translation-text/azure.ai.translation.text?view=azure-python-preview) •[Translator PyPi package (text)](https://pypi.org/project/azure-ai-translation-text/1.0.0b1/) •[Translator SDK for Python (batch)](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-translation-document-readme?view=azure-python) •[Translator PyPi package (batch)](https://pypi.org/project/azure-ai-translation-document/1.0.0/) |
| ![Image 25: Azure AI Search icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/search.svg)[Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) | Bring AI-powered cloud search to your mobile and web apps. | •[Connect to a search service quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-rbac?pivots=python) •[Use agentic retrieval quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-agentic-retrieval?tabs=search-perms%2Csearch-endpoint&pivots=programming-language-python) •[Vector search quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-vector?tabs=keyless&pivots=python) •[Classic generative search (RAG) using grounding data quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-rag?pivots=python) •[Full-text search quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-text?tabs=keyless%2Cwindows&pivots=python) •[Semantic ranking quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-semantic?pivots=python) •[Chat with Azure OpenAI models using your own data quickstart](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/use-your-data-quickstart?viewFallbackFrom=foundry&context=%2Fazure%2Fsearch%2Fcontext%2Fcontext&tabs=keyless%2Ctypescript-keyless%2Cpython-new&pivots=programming-language-python) •[Azure AI Search SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/search-documents-readme?view=azure-python) •[Azure AI Search PyPi package](https://pypi.org/project/azure-search-documents/11.6.0b1/) |
| ![Image 26: Content Safety icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/content-safety.svg)[Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview) | Detect harmful content in applications and services. | •[Analyze text content quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Cwindows&pivots=programming-language-python) •[Use a text blocklist quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-blocklist?tabs=visual-studio%2Cwindows&pivots=programming-language-python) •[Analyze image content quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-image?tabs=visual-studio%2Cwindows&pivots=programming-language-python) •[Content Safety SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-contentsafety-readme?view=azure-python) •[Content Safety PyPi package](https://pypi.org/project/azure-ai-contentsafety/1.0.0/) |
| ![Image 27: Document Intelligence icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/document-intelligence.svg)[Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview) | Turn documents into intelligent data-driven solutions. | •[Document Intelligence quickstart](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?view=doc-intel-4.0.0&pivots=programming-language-python) •[Document Intelligence SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview) •[Document Intelligence PyPi package](https://pypi.org/project/azure-ai-documentintelligence/1.0.0b1/) |
| ![Image 28: Vision icon](https://learn.microsoft.com/en-us/azure/reusable-content/ce-skilling/azure/media/ai-services/vision.svg)[Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview) | Analyze content in digital images and rich media assets. | •[Azure Vision in Foundry Tools v3.2 GA Read quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-python) •[Image Analysis quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40?tabs=windows%2Cvisual-studio&pivots=programming-language-python) •[Use the Face service quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/identity-client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-python) •[Vision SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-vision-imageanalysis-readme?view=azure-python-preview) •[Vision PyPi package](https://pypi.org/project/azure-ai-vision-imageanalysis/) |
