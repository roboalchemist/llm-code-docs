# Source: https://braintrust.dev/docs/integrations/sdk-integrations/google.md

# Source: https://braintrust.dev/docs/integrations/ai-providers/google.md

# Vertex AI

> Configure Google Cloud Vertex AI to access Google's foundation models

Configure Google Cloud Vertex AI to access Google's foundation models through Braintrust.

## Authentication

Choose between two authentication methods:

* **Access token**: Use a Vertex AI access token for authentication
* **Service account key**: Use a service account key JSON file for authentication

## Configuration

| Field                                                                | Description                                                                                                                                                                                                                     |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Project**<br />String                                              | Required. Your [Google Cloud Project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects) where Vertex AI is enabled.                                                                                 |
| **Authentication type**<br />`access_token` \| `service_account_key` | Required. Choose between access token or service account key authentication. [Documentation](https://cloud.google.com/vertex-ai/docs/authentication)                                                                            |
| **Secret**<br />JSON String                                          | Required if using `service_account_key` auth type. The service account key JSON content. [Documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)                                              |
| **API base**<br />URL String                                         | Optional. Custom API endpoint URL if using a different Vertex AI endpoint. [Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest#service-endpoint). Default is `https://{location}-aiplatform.googleapis.com`. |

## Models

Popular Vertex AI models include:

* Gemini 1.5 Pro (`gemini-1.5-pro`)
* Gemini 1.5 Flash (`gemini-1.5-flash`)
* PaLM 2 (`text-bison`)
* Codey (`code-bison`)

## Setup requirements

1. **Enable Vertex AI API**: Ensure the Vertex AI API is enabled in your Google Cloud project
2. **Service account permissions**: If using service account authentication, ensure the service account has the `AI Platform Developer` role
3. **Quotas**: Check your project's Vertex AI quotas and limits

## Additional resources

* [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
* [Vertex AI Model Garden](https://cloud.google.com/vertex-ai/docs/model-garden/explore-models)
* [Vertex AI Pricing](https://cloud.google.com/vertex-ai/pricing)
* [Authentication Guide](https://cloud.google.com/vertex-ai/docs/authentication)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt