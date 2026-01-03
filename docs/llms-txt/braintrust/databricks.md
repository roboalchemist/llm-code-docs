# Source: https://braintrust.dev/docs/integrations/ai-providers/databricks.md

# Databricks

> Configure Databricks Model Serving to access foundation models

Configure Databricks Model Serving to access foundation models and custom models through Braintrust.

## Authentication

Choose between two authentication methods:

* **Personal Access Token (PAT)**: Use a Databricks personal access token for authentication
* **Service Principal OAuth**: Use OAuth with a service principal for authentication

## Configuration

| Field                                                           | Description                                                                                                                                                                                                  |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **API base URL**<br />URL String                                | Required. Your Databricks workspace URL in the format `https://{workspace-name}.cloud.databricks.com`. [Documentation](https://docs.databricks.com/dev-tools/api/latest/index.html#workspace-instance-names) |
| **Authentication type**<br />`pat` \| `service_principal_oauth` | Optional. Choose between personal access token or service principal OAuth. Default is `pat`. [Documentation](https://docs.databricks.com/dev-tools/api/latest/authentication.html)                           |
| **Secret**<br />String                                          | Required if using `pat` auth type. Your Databricks personal access token. [Documentation](https://docs.databricks.com/dev-tools/api/latest/authentication.html#token-management)                             |
| **Client ID**<br />String                                       | Required if using `service_principal_oauth` auth type. Client ID for service principal authentication. [Documentation](https://docs.databricks.com/dev-tools/api/latest/oauth.html)                          |
| **Client Secret**<br />String                                   | Required if using `service_principal_oauth` auth type. Client secret for service principal authentication. [Documentation](https://docs.databricks.com/dev-tools/api/latest/oauth.html)                      |

## Models

Databricks provides access to several foundation models through Model Serving.

### Foundation models

* Meta Llama 3.1 70B Instruct
* Meta Llama 3.1 8B Instruct
* Mistral 7B Instruct
* Mixtral 8x7B Instruct
* MPT-7B Instruct

### Custom models

Deploy your own fine-tuned models through Databricks Model Serving.

## Setup requirements

1. **Databricks Workspace**: Ensure you have access to a Databricks workspace
2. **Model Serving**: Enable Model Serving in your workspace
3. **Authentication**: Set up either PAT or service principal authentication
4. **Model Endpoints**: Deploy the models you want to use as serving endpoints

## Endpoint configuration

Configure the following for model endpoints in Databricks.

1. **Serving Endpoint Name**: Use this as the model name in Braintrust
2. **Endpoint URL**: Automatically constructed from your workspace URL
3. **Authentication**: Uses the configured authentication method

## Additional resources

* [Databricks Model Serving Documentation](https://docs.databricks.com/machine-learning/model-serving/index.html)
* [Foundation Model APIs](https://docs.databricks.com/machine-learning/foundation-models/index.html)
* [Authentication Guide](https://docs.databricks.com/dev-tools/api/latest/authentication.html)
* [Model Serving Pricing](https://databricks.com/product/pricing/model-serving)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt