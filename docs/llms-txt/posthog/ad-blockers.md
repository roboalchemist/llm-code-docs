# Source: https://posthog.com/docs/privacy/ad-blockers.md

# Tracking endpoints and ad blockers - Docs

PostHog provides a range of services that help teams build great products.

Part of that range are web and product analytics, which send usage event reporting back to PostHog. We encourage our customers to be transparent about this reporting, provide several [privacy-preserving options](/docs/product-analytics/privacy.md) in our tools, and fully comply with data privacy laws, including GDPR.

Nevertheless, privacy-focused users of the web may wish to prevent any such data collection. Ad and tracking blockers should target these endpoints:

`https://us.i.posthog.com/i/v0/e`

`https://eu.i.posthog.com/i/v0/e`

PostHog provides other tools unrelated to event reporting and analytics. These can be vital to the sites which rely on them. You **should not block** these endpoints, at risk of breaking site functionality:

`https://us.i.posthog.com/flags`

`https://eu.i.posthog.com/flags`

`https://us-assets.i.posthog.com/static/`

`https://eu-assets.i.posthog.com/static/`

As we may add further endpoints in this category in the future, we encourage you to carefully target any blocking logic, rather than using a blanket approach.

## Further reading

-   [GDPR compliance](/docs/privacy/gdpr-compliance.md)
-   [CCPA compliance](/docs/privacy/ccpa-compliance.md)
-   [HIPAA compliance](/docs/privacy/hipaa-compliance.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better