# Source: https://gofastmcp.com/integrations/scalekit.md

# Scalekit 🤝 FastMCP

> Secure your FastMCP server with Scalekit

export const VersionBadge = ({version}) => {
  return <code className="version-badge-container">
            <p className="version-badge">
                <span className="version-badge-label">New in version:</span> 
                <code className="version-badge-version">{version}</code>
            </p>
        </code>;
};

<VersionBadge version="2.12.5" />

Install auth stack to your FastMCP server with [Scalekit](https://scalekit.com) using the [Remote OAuth](/servers/auth/remote-oauth) pattern: Scalekit handles user authentication, and the MCP server validates issued tokens.

## Configuration

### Prerequisites

Before you begin

1. Get a [Scalekit account](https://app.scalekit.com/) and grab API credentials such as **Client ID**, **Client Secret** and **Environment URL** from *Dashboard > Developers > Settings*.
2. Have your FastMCP server's endpoint ready (can be localhost for development, e.g., `http://localhost:8000/mcp`)

### Step 1: Configure MCP server in Scalekit environment

<Steps>
  <Step title="Register MCP server and set environment">
    In your Scalekit dashboard:

    1. Open the **MCP Servers** section, then select **Create new server**
    2. Enter server details: a name, a resource identifier, and the desired MCP client authentication settings
    3. Save, then copy the **Resource ID** (for example, res\_92015146095)

    In your FastMCP project's `.env`:

    ```sh  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
    SCALEKIT_ENVIRONMENT_URL=<YOUR_APP_ENVIRONMENT_URL>
    SCALEKIT_CLIENT_ID=<YOUR_APP_CLIENT_ID> # skc_7008EXAMPLE46
    SCALEKIT_RESOURCE_ID=<YOUR_APP_RESOURCE_ID> # res_926EXAMPLE5878
    MCP_URL=http://localhost:8000/mcp
    ```
  </Step>
</Steps>

### Step 2: Add auth to FastMCP server

Create your FastMCP server file and use the ScalekitProvider to handle all the OAuth integration automatically:

```python server.py theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
from fastmcp import FastMCP
from fastmcp.server.auth.providers.scalekit import ScalekitProvider

# Discovers Scalekit endpoints and set up JWT token validation
auth_provider = ScalekitProvider(
    environment_url=SCALEKIT_ENVIRONMENT_URL,    # Scalekit environment URL
    client_id=SCALEKIT_CLIENT_ID,                # OAuth client ID
    resource_id=SCALEKIT_RESOURCE_ID,            # Resource server ID
    mcp_url=SERVER_URL,                          # Is also aud claim
)

# Create FastMCP server with auth
mcp = FastMCP(name="My Scalekit Protected Server", auth=auth_provider)

@mcp.tool
def auth_status() -> dict:
    """Show Scalekit authentication status."""
    # Extract user claims from the JWT
    return {
        "message": "This tool requires authentication via Scalekit",
        "authenticated": True,
        "provider": "Scalekit"
    }

```

## Testing

### Start the MCP server

```sh  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
uv run python server.py
```

Use any MCP client (for example, mcp-inspector, Claude, VS Code, or Windsurf) to connect to the running serve. Verify that authentication succeeds and requests are authorized as expected.

### Provider selection

Setting this environment variable allows the Scalekit provider to be used automatically without explicitly instantiating it in code.

<Card>
  <ParamField path="FASTMCP_SERVER_AUTH" default="Not set">
    Set to `fastmcp.server.auth.providers.scalekit.ScalekitProvider` to use Scalekit authentication.
  </ParamField>
</Card>

### Scalekit-specific configuration

These environment variables provide default values for the Scalekit provider, whether it's instantiated manually or configured via `FASTMCP_SERVER_AUTH`.

<Card>
  <ParamField path="FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_ENVIRONMENT_URL" required>
    Your Scalekit environment URL from the Admin Portal (e.g., `https://your-env.scalekit.com`)
  </ParamField>

  <ParamField path="FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_CLIENT_ID" required>
    Your Scalekit OAuth application client ID from the Applications section
  </ParamField>

  <ParamField path="FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_RESOURCE_ID" required>
    Your Scalekit resource server ID from the Resources section
  </ParamField>

  <ParamField path="FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_MCP_URL" required>
    Public URL of your FastMCP server (e.g., `https://your-server.com` or `http://localhost:8000/mcp` for development)
  </ParamField>
</Card>

Example `.env`:

```bash  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
# Use the Scalekit provider
FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.scalekit.ScalekitProvider

# Scalekit configuration
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_ENVIRONMENT_URL=https://your-env.scalekit.com
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_CLIENT_ID=skc_123
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_RESOURCE_ID=res_456
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_MCP_URL=https://your-server.com/mcp
```

With environment variables set, your server code simplifies to:

```python server.py theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
from fastmcp import FastMCP

# Authentication is automatically configured from environment
mcp = FastMCP(name="My Scalekit Protected Server")

@mcp.tool
def protected_action() -> str:
    """A tool that requires authentication."""
    return "Access granted via Scalekit!"
```

## Capabilities

Scalekit supports OAuth 2.1 with Dynamic Client Registration for MCP clients and enterprise SSO, and provides built‑in JWT validation and security controls.

**OAuth 2.1/DCR**: clients self‑register, use PKCE, and work with the Remote OAuth pattern without pre‑provisioned credentials.

**Validation and SSO**: tokens are verified (keys, RS256, issuer, audience, expiry), and SAML, OIDC, OAuth 2.0, ADFS, Azure AD, and Google Workspace are supported; use HTTPS in production and review auth logs as needed.

## Debugging

Enable detailed logging to troubleshoot authentication issues:

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Token inspection

You can inspect JWT tokens in your tools to understand the user context:

```python  theme={"theme":{"light":"snazzy-light","dark":"dark-plus"}}
from fastmcp.server.context import request_ctx
import jwt

@mcp.tool
def inspect_token() -> dict:
    """Inspect the current JWT token claims."""
    context = request_ctx.get()

    # Extract token from Authorization header
    if hasattr(context, 'request') and hasattr(context.request, 'headers'):
        auth_header = context.request.headers.get('authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header[7:]
            # Decode without verification (already verified by provider)
            claims = jwt.decode(token, options={"verify_signature": False})
            return claims

    return {"error": "No token found"}
```
