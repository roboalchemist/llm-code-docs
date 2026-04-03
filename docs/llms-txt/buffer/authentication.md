# Source: https://developers.buffer.com/guides/authentication.md

# Authentication

Every request to the Buffer API needs an API key. Here's how to get one and start using it.

## Getting your API key

1. Log in to your [Buffer](https://buffer.com) account
2. Go to [Settings → API](https://publish.buffer.com/settings/api)
3. Create a new API key
4. Copy the key

## Using your API key

Include your key in the `Authorization` header of every request:

<!-- AUTH_CODE_EXAMPLES -->

Every request to `https://api.buffer.com` must include this header. Requests without a valid key will return a `401 Unauthorized` error.

## Key permissions and scope

- Your API key acts on behalf of **your account only**
- It can access all organizations and channels in your account
- There is no per-organization scoping at this time
- The key is account-based, not organization-based

If you belong to multiple organizations, your key gives you access to all of them. Use the organization ID in your queries to target a specific one.

## Security best practices

- **Never commit your API key to version control.** Add it to `.gitignore` or use a secrets manager.
- **Don't expose it in client-side code.** API calls should be made from your server, not from a browser or mobile app.
- **Use environment variables.** Store the key in an environment variable like `BUFFER_API_KEY` and reference it in your code.
- **Rotate your key if compromised.** Generate a new one in [Settings → API](https://publish.buffer.com/settings/api) and update your applications.

```javascript
// Good: read from environment variable
const apiKey = process.env.BUFFER_API_KEY;

// Not advised: hardcoded in source code
const apiKey = "buf_abc123...";
```

## OAuth (coming soon)

We're working on OAuth support for third-party apps. Check the [Roadmap](../roadmap.html) for updates. This will let you build apps that access other people's Buffer accounts with their permission.

For now, the API is designed for first-party use: automating your own account or building internal tools for your team.

## Next steps

- [Quick Start](getting-started.html): Make your first API request
- [Your First Post](your-first-post.html): Go from authenticated to a scheduled post
