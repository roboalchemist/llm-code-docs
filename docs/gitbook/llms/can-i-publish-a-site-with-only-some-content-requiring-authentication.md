# Source: https://gitbook.com/docs/help-center/published-documentation/adaptive-content/can-i-publish-a-site-with-only-some-content-requiring-authentication.md

# Can I publish a site with only  some content requiring authentication?

Yes! You can have a public site with some authenticated sections using Adaptive Content without requiring login for the entire site.

**Recommended Approach:**

1. Keep your site audience as Public, Unlisted or Share link
2. Enable Adaptive content in site settings
3. Use **signed cookies** to pass user claims after they log in to your main application
4. Set conditions on specific pages/sections to show only for authenticated users

See our [signed cookie documentation](https://gitbook.com/docs/publishing-documentation/adaptive-content/enabling-adaptive-content/cookies#signed-cookie) for implementation details.
