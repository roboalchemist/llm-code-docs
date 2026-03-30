# Source: https://firebase.google.com/docs/reference/ai-logic/rest.md.txt

# Firebase AI Logic API

The Firebase AI Logic API provides programmatic access for creating, testing, and managing server prompt templates.

> [!NOTE]
> You can try out calling a Firebase AI Logic REST API method on live data using
> the embedded API Explorer. This API Explorer allows you to see the API
> request and response without leaving the API's reference documentation.
>
> Find the embedded explorer in the side-panel of each method's reference
> page (click any method in the tables below).

## Service: firebasevertexai.googleapis.com

> [!NOTE]
> **This service is for the product Firebase AI Logic.**
>
>
> **It can be used to access Google's generative models via either the
> Gemini Developer API or the Vertex AI Gemini API.**
>
>
> Firebase AI Logic and its client SDKs were formerly called
> "Vertex AI in Firebase". In May 2025, we
> [renamed
> and repackaged our services into Firebase AI Logic](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#renamed-product) to better reflect
> our expanded services and features
> (for example, we expanded to support the Gemini Developer API).

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebasevertexai.googleapis.com/$discovery/rest?version=v1beta>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebasevertexai.googleapis.com`

## REST Resource: [v1beta.projects.locations.templates](https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/create` | `POST /v1beta/{parent=projects/*/locations/*}/templates` Creates a new PromptTemplate. |
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/delete` | `DELETE /v1beta/{name=projects/*/locations/*/templates/*}` Deletes a PromptTemplate. |
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/get` | `GET /v1beta/{name=projects/*/locations/*/templates/*}` Gets a PromptTemplate. |
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/list` | `GET /v1beta/{parent=projects/*/locations/*}/templates` Lists PromptTemplates. |
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/modifyLock` | `POST /v1beta/{name=projects/*/locations/*/templates/*}:modifyLock` Updates the Lock state on a PromptTemplate |
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/patch` | `PATCH /v1beta/{promptTemplate.name=projects/*/locations/*/templates/*}` Updates a PromptTemplate. |
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/templateGenerateContent` | `POST /v1beta/{name=projects/*/locations/*/templates/*}:templateGenerateContent` Generate content with multimodal inputs using a server-side prompt template. |
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/templatePredict` | `POST /v1beta/{name=projects/*/locations/*/templates/*}:templatePredict` Perform an online prediction using a server-side prompt template. |
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/templateStreamGenerateContent` | `POST /v1beta/{name=projects/*/locations/*/templates/*}:templateStreamGenerateContent` Generate content with multimodal inputs and streaming outputs using a server-side prompt template. |

## REST Resource: [v1beta.projects.templates](https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.templates)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.templates/templateGenerateContent` | `POST /v1beta/{name=projects/*/templates/*}:templateGenerateContent` Generate content with multimodal inputs using a server-side prompt template. |
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.templates/templatePredict` | `POST /v1beta/{name=projects/*/templates/*}:templatePredict` Perform an online prediction using a server-side prompt template |
| `https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.templates/templateStreamGenerateContent` | `POST /v1beta/{name=projects/*/templates/*}:templateStreamGenerateContent` Generate content with multimodal inputs and streaming outputs using a server-side prompt template. |