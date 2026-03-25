# Source: https://docs.axonius.com/docs/open-ai.md

# OpenAI

OpenAI is a research and deployment AI platform that provides large language and multimodal models such as GPT and Sora for generative and reasoning capabilities.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the <Anchor label="OpenAI API" target="_blank" href="https://platform.openai.com/docs/api-reference/introduction">OpenAI API</Anchor>.

### Permissions

The following permissions are required:

The API key must have read permission or higher (`All`).

#### Supported From Version

Supported from Axonius version 8.0.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the OpenAI server.

2. **API Key**  - An API Key associated with a user account that has the Required Permissions to fetch assets. For more information, see <Anchor label="Authentication" target="_blank" href="https://platform.openai.com/docs/api-reference/authentication">Authentication</Anchor>.

<Image alt="OpenAI connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/OpenAI_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).