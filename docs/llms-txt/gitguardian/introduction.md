# Source: https://docs.gitguardian.com/api-docs/introduction.md

# Introduction

> Overview of the GitGuardian API, its use cases for managing dashboard data, using the secrets detection engine, and key limitations.

The GitGuardian API gives you full creative control to **manage your dashboard** data and also to **use GitGuardian secrets detection engine**, whether through ggshield or in a custom way. All API calls need to be authenticated.

### Use cases

- Export your incidents to build custom reports.
- Manage your incidents programmatically.
- Perform your users and teams management programmatically.
- Plug GitGuardian easily into your existing services.
- Build your own integration for secrets detection.
- You want to use ggshield to shift left.

### Considerations

- The GitGuardian API is versioned.
- All requests to the GitGuardian API must be authenticated.
- The GitGuardian API enforces rate limits on all requests.

### Limitations

- Only secret incidents are available through the API.

[Start to use the API by creating your API key ->](./authentication.md)
