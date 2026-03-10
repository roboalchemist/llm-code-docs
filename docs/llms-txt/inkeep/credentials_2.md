# Source: https://docs.inkeep.com/visual-builder/tools/credentials

# Manage Credentials in Visual Builder (/visual-builder/tools/credentials)

Credentials are used to authenticate MCP servers.



The credentials page allows you to add credentials to your MCP servers.

## Adding a credential

<>
  Make sure your Visual Builder is running (if you haven't set it up yet, see [Quick Start](/get-started/quick-start)). Navigate to the Credentials tab in the left sidebar, click "New credential", and select "Bearer authentication".

  1. Fill in the required credential details:

  | Field     | Description                                                         |
  | --------- | ------------------------------------------------------------------- |
  | `Name`    | A descriptive name for your credential (e.g., "production-api-key") |
  | `API key` | The authentication token or API key for the service                 |

  2. Optionally, configure additional settings:

  | Field                | Description                                                                                                                                                                                               |
  | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `Metadata`           | Additional headers to include with authentication requests (e.g., User-Agent, X-API-Key). Only available for Nango Store.                                                                                 |
  | `Credential store`   | Where to securely store the credential. Choose from available stores ([Nango Store](/typescript-sdk/tools/credentials#nango-store) or [Keychain Store](/typescript-sdk/tools/credentials#keychain-store)) |
  | `Link to MCP server` | Optionally associate this credential with a specific MCP server that does not have a credential configured                                                                                                |

  3. Click "Create Credential" to save the credential.
</>

To use the credential in an MCP server, you can reference it when creating or editing the MCP server. See the [MCP Servers](/visual-builder/tools/mcp-servers) page for more information.

***
