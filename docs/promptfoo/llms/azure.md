# Source: https://www.promptfoo.dev/docs/providers/azure/

# Azure OpenAI Provider | Promptfoo

## Main Content

### Setup

There are three ways to authenticate with Azure OpenAI:

#### Option 1: API Key Authentication

Set the `AZURE_API_KEY` environment variable and configure your deployment:

```yaml
providers:
  - id: azure:chat:deploymentNameHere
    config:
      apiHost: xxxxxxxx.openai.azure.com
      apiKey: your-api-key
      azureClientId: your-azure-client-id
      azureClientSecret: your-azure-client-secret
      azureTenantId: your-azure-tenant-id
      azureAuthorityHost: https://login.microsoftonline.com
      azureTokenScope: https://cognitiveservices.azure.com/.default
```

#### Option 2: Client Credentials

Install the `@azure/identity` package:

```sh
npm i @azure/identity
```

Set the following configuration variables:

```yaml
providers:
  - id: azure:chat:deploymentNameHere
    config:
      apiHost: xxxxxxxx.openai.azure.com
      azureClientId: your-azure-client-id
      azureClientSecret: your-azure-client-secret
      azureTenantId: your-azure-tenant-id
      azureAuthorityHost: https://login.microsoftonline.com
      azureTokenScope: https://cognitiveservices.azure.com/.default
      temperature: 0.7
```

#### Option 3: Azure AD Authentication

Install the `@azure/identity` package:

```sh
npm i @azure/identity
```

Set the following configuration variables:

```yaml
providers:
  - id: azure:chat:deploymentNameHere
    config:
      apiHost: xxxxxxxx.openai.azure.com
      azureClientId: your-azure-client-id
      azureClientSecret: your-azure-client-secret
      azureTenantId: your-azure-tenant-id
      azureAuthorityHost: https://login.microsoftonline.com
      azureTokenScope: https://cognitiveservices.azure.com/.default
      temperature: 0.7
```

### Provider Types

Azure OpenAI provides access to OpenAI models through the Azure OpenAI Service. It supports two main types of models: chat and completion.

#### Chat Models

Chat models are used for conversational interactions, such as chatbots and chat assistants.

- `azure:chat:deploymentNameHere` - Deployment name for chat models
- `azure:chat:deploymentNameHere` - Deployment name for chat models

#### Completion Models

Completion models are used for generating text, such as summaries, translations, and code generation.

- `azure:completion:deploymentNameHere` - Deployment name for completion models
- `azure:completion:deploymentNameHere` - Deployment name for completion models

### Available Models

Azure OpenAI provides access to a variety of models, including:

- `gpt-4o` - Most capable model
- `gpt-4o-mini` - Balanced performance
- `gpt-3.5-turbo-instruct` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0125` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0613` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-16k` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-1106` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-10125` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0681` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0158` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0149` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0138` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0127` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0118` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0107` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0089` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0070` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0060` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0050` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0040` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0030` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0020` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0010` - Turbo version of GPT-3.5
- `gpt-3.5-turbo-0000` - Turbo version of GPT-3.5
- `gpt-4` - Most capable model
- `gpt-4-mini` - Balanced performance
- `gpt-4-pro` - Pro version of GPT-4
- `gpt-4-32k` - 32K context version of GPT-4
- `gpt-4-8k` - 8K context version of GPT-4
- `gpt-4-64k` - 64K context version of GPT-4
- `gpt-4-128k` - 128K context version of GPT-4
- `gpt-4-128k-0125` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0138` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0149` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0158` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0160` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0175` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0185` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0190` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0200` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0210` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0220` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0230` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0240` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0250` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0260` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0270` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0280` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0290` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0300` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0310` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0320` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0330` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0340` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0350` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0360` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0370` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0380` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0390` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0400` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0410` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0420` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0430` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0440` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0450` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0460` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0470` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0480` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0490` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0500` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0510` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0520` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0530` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0540` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0550` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0560` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0570` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0580` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0590` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0600` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0610` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0620` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0630` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0640` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0650` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0660` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0670` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0680` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0690` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0700` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0710` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0720` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0730` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0740` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0750` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0760` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0770` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0780` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0790` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0800` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0810` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0820` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0830` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0840` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0850` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0860` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0870` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0880` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0890` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0900` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0910` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0920` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0930` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0940` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0950` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0960` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0970` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0980` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-0990` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1000` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1010` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1020` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1030` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1040` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1050` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1060` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1070` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1080` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1090` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1100` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1110` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1120` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1130` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1140` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1150` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1160` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1170` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1180` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1190` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1200` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1210` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1220` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1230` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1240` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1250` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1260` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1270` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1280` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1290` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1300` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1310` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1320` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1330` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1340` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1350` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1360` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1370` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1380` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1390` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1400` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1410` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1420` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1430` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1440` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1450` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1460` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1470` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1480` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1490` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1500` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1510` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1520` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1530` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1540` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1550` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1560` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1570` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1580` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1590` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1600` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1610` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1620` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1630` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1640` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1650` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1660` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1670` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1680` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1690` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1700` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1710` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1720` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1730` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1740` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1750` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1760` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1770` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1780` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1790` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1800` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1810` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1820` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1830` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1840` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1850` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1860` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1870` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1880` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1890` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1900` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1910` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1920` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1930` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1940` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1950` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1960` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1970` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1980` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-1990` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2000` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2010` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2020` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2030` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2040` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2050` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2060` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2070` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2080` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2090` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2100` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2110` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2120` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2130` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2140` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2150` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2160` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2170` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2180` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2190` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2200` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2210` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2220` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2230` - 128K context version of GPT-4 Turbo
- `gpt-4-128k-2240` - 128K context version of GPT-4 Turbo
- `gpt-