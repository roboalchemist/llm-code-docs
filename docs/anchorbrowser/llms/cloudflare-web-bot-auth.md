# Source: https://docs.anchorbrowser.io/advanced/cloudflare-web-bot-auth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloudflare Web Bot Auth

> Authenticate browser sessions with Cloudflare Web Bot Auth

Anchor Browser supports Cloudflare Web Bot Auth HTTP message signing for browser sessions. This allows you to identify as Anchor Browser to websites that require Cloudflare's web bot authentication, enabling access to protected content and avoiding bot detection.

<img src="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cloudflare-web-bot-auth.png?fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=b2984b651bdbcdcac0b5de047aaaa235" alt="WebBotAuth.io Test" data-og-width="2312" width="2312" data-og-height="1596" height="1596" data-path="images/cloudflare-web-bot-auth.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cloudflare-web-bot-auth.png?w=280&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=f5da1d90e9b8b83c88479cc09146814f 280w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cloudflare-web-bot-auth.png?w=560&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=56c6267dceb9af68f4f71768c2b71a13 560w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cloudflare-web-bot-auth.png?w=840&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=738dd9761b84d23f7c39212086b44a74 840w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cloudflare-web-bot-auth.png?w=1100&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=3935a01ebbecc250f0eb2b6d4e6c75a6 1100w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cloudflare-web-bot-auth.png?w=1650&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=a36017e34d5aa25d77c33b037a5087b6 1650w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cloudflare-web-bot-auth.png?w=2500&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=a2eb0efd8893fbcc7a441e2769a0bb7c 2500w" />

## How It Works

1. **Session Creation**: Create a browser session with web bot auth enabled
2. **HTTP Message Signing**: All HTTP requests are automatically signed as Anchor Browser
3. **Authentication**: Cloudflare validates the signatures
4. **Access Granted**: Successfully authenticated requests can access protected content

## Using Web Bot Auth

### How Authentication Works

When you enable web bot auth, Anchor Browser automatically identifies all HTTP requests to websites using our registered identity. This allows you to access protected content that requires Cloudflare's web bot authentication without any additional configuration.

### Browser Configuration

```typescript  theme={null}
{
  "browser": {
    "web_bot_auth": {
      "active": boolean  // Enable/disable web bot auth (default: false)
    }
  }
}
```

### SDK Examples

Enable web bot auth by setting the `web_bot_auth.active` flag to `true` in your session configuration:

<CodeGroup>
  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  # Initialize the client
  client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  # Session configuration with web bot auth enabled
  config = {
      "web_bot_auth": {
        "active": True
      }
  }

  # Create session with web bot auth
  session = client.sessions.create(browser=config)
  print(f"Session created: {session.data.id}")
  print(f"CDP URL: {session.data.cdp_url}")
  print(f"Live view URL: {session.data.live_view_url}")
  ```

  ```javascript node.js theme={null}
  import  AnchorBrowser from 'anchorbrowser';

  // Initialize the client
  const client = new AnchorBrowser({ apiKey: process.env.ANCHOR_API_KEY });

  // Session configuration with web bot auth enabled
  const config = {
    browser: {
      web_bot_auth: {
        active: true
      }
    }
  };

  // Create session with web bot auth
  const session = await client.sessions.create(config);

  console.log('Session created:', session);
  ```
</CodeGroup>

## Testing

You can test your web bot auth configuration by visiting [https://webbotauth.io/test](https://webbotauth.io/test) in a browser session with web bot auth enabled. This site will show you whether your requests are being properly signed and authenticated.

## Read More

* [Cloudflare Verified Bots Blog](https://blog.cloudflare.com/verified-bots-with-cryptography/)
* [HTTP Message Signatures (RFC 9421)](https://datatracker.ietf.org/doc/html/rfc9421)
* [Web Bot Auth IETF Draft](https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture)
* [WebBotAuth.io](https://webbotauth.io)
