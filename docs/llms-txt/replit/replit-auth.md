# Source: https://docs.replit.com/replit-workspace/replit-auth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Replit Auth

> Add user accounts, personalized experiences, and secure access control to your app. Enterprise-grade authentication that works with a single Agent prompt.

Replit Auth lets you create personalized user experiences in your app. With user accounts, you can save user preferences, create custom dashboards, build social features, control access to premium content, and track user activity—all the features that make apps engaging and valuable.

Instead of spending months building authentication from scratch, Replit Auth gives you enterprise-grade capabilities with a single Agent prompt. Powered by the same infrastructure as Fortune 500 companies—Firebase, Google Cloud Identity Platform, reCAPTCHA, Stytch, and Clearout—you get professional-level security, fraud prevention, and global scale built in.

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=279d3e12c4896346485ce5bfe5d893f5" alt="Auth configuration" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/auth/auth-custom.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=1c84c75c3548e5365e45f90c2fe4f7b8 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=e5eb7e41cd658c993dc49af788f8fbbe 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=0f9b75946dc6aeec02b878d27b00568d 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=78bac5b9131cf573156116a962d6a451 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=32c527299a9588cb6c8b86be43fbe7f1 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=9b0f0897278f563c8d756cc542667415 2500w" />
</Frame>

## Why use Replit Auth

Authentication is a challenging problem that entire companies dedicate themselves to solving. Your app's primary purpose likely isn't authentication - it's whatever unique idea or solution you're building.

Replit Auth offers:

* **Zero setup** - Add authentication with a single prompt in Agent
* **Built-in security** - Uses Replit's infrastructure with protections against common attacks
* **User management** - Simplified user administration through the Auth pane
* **Database integration** - Automatic user entries in your database
* **Customizable login page** - Personalize the login experience for your app
* **Password reset** - Replit sends password reset emails for you, so you don't need to set up your own email delivery provider
* **Development and Published Apps** - Replit Auth works seamlessly across development (replit.dev), and published apps (replit.app, and custom domains)

## Enterprise-grade infrastructure

Replit Auth is more than simple user management—it's a fully managed authentication solution built on enterprise-grade infrastructure. This powerful combination gives your app the same authentication capabilities used by Fortune 500 companies:

* **Firebase & Google Cloud Identity Platform** - Enterprise-tier SLA with Google's battle-tested authentication infrastructure
* **Advanced security scanning** - Automatic protection against bots and malicious actors with reCAPTCHA integration
* **Fraud prevention** - Email verification and validation powered by Clearout to prevent fake accounts
* **Multi-factor authentication** - Secure login options backed by Stytch's enterprise authentication platform
* **Global scale** - Built to handle millions of users with automatic scaling and reliability

This enterprise foundation means you can focus on building your app's unique features while knowing your authentication is powered by the same infrastructure that secures billion-dollar companies. Instead of spending months integrating multiple services, you get all these capabilities with a single Agent prompt.

## Getting started with Replit Auth

The only way to implement Replit Auth is by using Agent. Simply include a request for Replit Auth in your prompt:

```
Help me create an app that [your app idea] and should feature Replit Auth.
```

Agent will set up all the necessary code and configurations for authentication. Manual implementation is not supported, as Agent handles all the complexity for you.

<Frame>
  <iframe src="https://www.youtube.com/embed/FepR-sBZKCo?si=RKJjt0e1Gviioxqr" style={{border: "none", borderRadius: "8px"}} width="100%" height="420px" />
</Frame>

To learn more about Agent capabilities, see the [Replit Agent documentation](/replitai/agent) and [Agent integrations](/replitai/integrations).

For tips on writing effective prompts, check out [Effective prompting with Replit](/tutorials/effective-prompting).

## Managing users

Replit Auth provides a built-in user management interface accessible through the Auth pane in your Replit workspace.

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-users.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=ad81201db936e48c0a6b7368d7fb99d3" alt="Auth management pane" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/auth/auth-users.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-users.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=e08608be0e4ce1e140b3dfecea203fac 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-users.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=3bc9acb54d5121919cafbf2ca105386e 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-users.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=4e0bbedd3e2c1fe3c7bcdfe9668c5037 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-users.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=038477048b78fe8514eaa83abc8511af 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-users.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=acff05af46317b85f91a333b15808c85 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-users.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=c39823ee7620ec7b5d121b97c5299613 2500w" />
</Frame>

From this interface, you can:

* View all authenticated users
* Ban users from your application
* View user details
* Track user activity

## Customizing the login page

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-login.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=6bedf7a0a188d10f58477ece05edec2e" alt="Auth configuration" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/auth/auth-login.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-login.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=a20fd57695237573977d5ec8248ad6d3 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-login.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=89264190c3339be176953f201d860182 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-login.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=e96e71b762491f4f8b818fe3f268e936 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-login.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=3e888a058a4c39ee428a93c35213b046 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-login.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=b29bbb171b160456231e8445821c33b0 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-login.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=8baa4935f5b4412cfe92e169b25a2fc0 2500w" />
</Frame>

You can customize the login page to match your app's branding:

1. Navigate to the Auth pane in your Replit workspace
2. Click on **Configure**
3. Customize the following elements:
   * App name
   * App icon
   * Login methods (Google, GitHub, X, Apple, Email)

Your changes will immediately appear on your app's login page.

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=279d3e12c4896346485ce5bfe5d893f5" alt="Auth configuration" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/auth/auth-custom.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=1c84c75c3548e5365e45f90c2fe4f7b8 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=e5eb7e41cd658c993dc49af788f8fbbe 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=0f9b75946dc6aeec02b878d27b00568d 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=78bac5b9131cf573156116a962d6a451 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=32c527299a9588cb6c8b86be43fbe7f1 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-custom.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=9b0f0897278f563c8d756cc542667415 2500w" />
</Frame>

## Connecting user data with your database

Replit Auth automatically creates user entries in your database. This makes it easy to store user-specific data. Agent will guide you on properly connecting user data with your database.

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-db.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=a2a11e8ab5f88f9beeed83e8b2dc09f7" alt="Auth database" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/auth/auth-db.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-db.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=1c1b6086bb1e12903418dd58790dd579 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-db.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=5019b1293af39940ebe63cdf00b3c34b 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-db.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=e897962c1cc8a2ac9dc1ecedd3300711 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-db.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=b5a21dcd0ab9bbfb3da8da90fb10a132 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-db.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=6470b3e1d2a3b6b66ba12ea47d020f4a 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/auth/auth-db.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=0041e684a7279d3734b0ab4b7d266faa 2500w" />
</Frame>

For more information on databases, see the [Replit Database Documentation](/cloud-services/storage-and-databases/replit-database).

## Security considerations

Replit Auth leverages Replit's infrastructure, providing built-in protections against common security threats. However, you should still follow these best practices:

* Always validate user authentication server-side before performing sensitive operations
* Never store sensitive information like passwords in your code
* Use environment variables for any API keys or secrets
* Implement proper access controls for user data

For more information on security, check out:

* [Replit's built-in security features](/tutorials/vibe-code-securely)
* [Security checklist for vibe coding](/tutorials/vibe-code-security-checklist)
* [Secrets management](/replit-workspace/workspace-features/secrets)

## Referrals

To encourage applications that teach people about Replit, any user that signs up via Replit Auth will automatically be added to your pending Replit Referrals. If they later upgrade to Replit Core, you will receive any referral bonus you are entitled to according to the current terms of the referral program.

## Troubleshooting

### Common issues

1. **User not recognized after login**
   * If you're experiencing issues, ask [Replit Agent](/replitai/agent) for help debugging your authentication implementation.

2. **Custom icon not displaying**
   * Make sure the icon URL is accessible and in a supported format (PNG or JPG).

3. **Newly linked custom domain isn't working**
   * Republish to refresh the domain list (REPLIT\_DOMAINS environment variable).

## Additional resources

* [Replit Database Documentation](/cloud-services/storage-and-databases/replit-database)
* [Replit Agent](/replitai/agent)
