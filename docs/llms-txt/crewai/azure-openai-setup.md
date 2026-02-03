# Source: https://docs.crewai.com/en/enterprise/guides/azure-openai-setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure OpenAI Setup

> Configure Azure OpenAI with Crew Studio for enterprise LLM connections

This guide walks you through connecting Azure OpenAI with Crew Studio for seamless enterprise AI operations.

## Setup Process

<Steps>
  <Step title="Access Azure AI Foundry">
    1. In Azure, go to [Azure AI Foundry](https://ai.azure.com/) > select your Azure OpenAI deployment.
    2. On the left menu, click `Deployments`. If you don't have one, create a deployment with your desired model.
    3. Once created, select your deployment and locate the `Target URI` and `Key` on the right side of the page. Keep this page open, as you'll need this information.
       <Frame>
         <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a7136eae05529c674ddbda6e8f58eee8" alt="Azure AI Foundry" data-og-width="670" width="670" data-og-height="502" height="502" data-path="images/enterprise/azure-openai-studio.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=79abbdeb76fa4f38ef6614438651744c 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c60da2c7f702a15162111d45996d97ff 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=46d5ab75f601b9a14c53c93e51aa57b4 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=67e2c20ec9785d24bf69279102f564a7 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=342a5e6abe1f0a4b1dadf7865ac4cf27 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=44d5e6cf8120262a1637a4e24858dfcb 2500w" />
       </Frame>
  </Step>

  <Step title="Configure CrewAI AMP Connection">
    4. In another tab, open `CrewAI AMP > LLM Connections`. Name your LLM Connection, select Azure as the provider, and choose the same model you selected in Azure.
    5. On the same page, add environment variables from step 3:
       * One named `AZURE_DEPLOYMENT_TARGET_URL` (using the Target URI). The URL should look like this: [https://your-deployment.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview](https://your-deployment.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview)
       * Another named `AZURE_API_KEY` (using the Key).
    6. Click `Add Connection` to save your LLM Connection.
  </Step>

  <Step title="Set Default Configuration">
    7. In `CrewAI AMP > Settings > Defaults > Crew Studio LLM Settings`, set the new LLM Connection and model as defaults.
  </Step>

  <Step title="Configure Network Access">
    8. Ensure network access settings:
       * In Azure, go to `Azure OpenAI > select your deployment`.
       * Navigate to `Resource Management > Networking`.
       * Ensure that `Allow access from all networks` is enabled. If this setting is restricted, CrewAI may be blocked from accessing your Azure OpenAI endpoint.
  </Step>
</Steps>

## Verification

You're all set! Crew Studio will now use your Azure OpenAI connection. Test the connection by creating a simple crew or task to ensure everything is working properly.

## Troubleshooting

If you encounter issues:

* Verify the Target URI format matches the expected pattern
* Check that the API key is correct and has proper permissions
* Ensure network access is configured to allow CrewAI connections
* Confirm the deployment model matches what you've configured in CrewAI
