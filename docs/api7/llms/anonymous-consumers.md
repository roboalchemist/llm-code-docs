# Source: https://docs.api7.ai/apisix/enterprise-feature/anonymous-consumers.md

# Anonymous Consumers

The anonymous consumer feature in API7 Enterprise enables selective bypass of authentication requirements by allowing the configuration of an anonymous consumer on authentication plugins. This feature allows protected routes to grant access to non-authenticated callers.

Consider a scenario where a company would like to offer certain freemium API access for demonstrating the product, in addition to the paid premium product. Anonymous consumers can be assigned lower rate limiting quotas than authenticated users, helping prioritize resources for premium users while still allowing unauthenticated access where necessary. When there are excessive anonymous requests, requests exceeding the assigned quota will be rejected and the quota will only be reset in the next rate limiting cycle. Authenticated premium users, in contrast, receive higher quotas, ensuring they have priority access and better service reliability.

![diagram of anonymous freemium consumers and premium consumers with different rate limiting quotas](https://static.api7.ai/uploads/2024/11/26/BnoIKodj_anonymous-consumer.png)

## Key Features[â](#key-features "Direct link to Key Features")

* Enhance ease of access for non-critical data or trial features by eliminating authentication steps for public or demo endpoints.
* Ensure higher service availability for authenticated users.
* Support multiple authentication methods, including key authentication, JWT, HMAC, and basic authentication.
* Forward the `X-Consumer-Username` header containing the anonymous consumer name to upstream services, which allows additional business logic to be implemented.
* Maintain security boundaries by encouraging the isolation of anonymous consumer permissions from those fully authenticated, reducing the risk of exposing sensitive data or impacting critical operations.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Implement Different Rate Limiting Quotas[â](#implement-different-rate-limiting-quotas "Direct link to Implement Different Rate Limiting Quotas")

Anonymous consumers can be assigned specific rate limiting policies that differ from those of authenticated users. By design, anonymous consumers often have stricter quotas to limit the amount of data or requests they can access, helping to safeguard resources and maintain service quality. For example, an API might allow unauthenticated users to make up to 100 requests per day, while authenticated users could be permitted several thousand. This distinction protects core resources for paying customers or users with verified identities and helps to mitigate potential abuse or overuse by unknown entities.

### Enable Public Access for Trial or Freemium Models[â](#enable-public-access-for-trial-or-freemium-models "Direct link to Enable Public Access for Trial or Freemium Models")

For businesses offering freemium or trial-based access, the anonymous consumer feature provides a streamlined way to allow access to a limited set of API functionalities without requiring new users to register or authenticate. This setup is particularly useful for lowering onboarding friction and enabling prospective customers to explore features. For instance, a weather API could allow anonymous access to basic forecast data while reserving premium data, such as historical trends or high-resolution radar images, for authenticated users. This encourages users to upgrade if they require more comprehensive or unrestricted access.

### Simplify Onboarding for Demo or Testing Environments[â](#simplify-onboarding-for-demo-or-testing-environments "Direct link to Simplify Onboarding for Demo or Testing Environments")

By designating anonymous consumers for demo environments or testing endpoints, organizations can allow developers to access sample APIs without the need for creating a full account or verifying identity. This can help reduce entry barriers for third-party developers or clients who want to assess API integration feasibility. For example, an e-commerce platform might provide sample product and pricing data via anonymous consumer access in a sandbox environment, making it easy for prospective partners to test integration without onboarding delays or unnecessary account setup steps.
