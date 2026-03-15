# Source: https://posthog.com/docs/session-replay/privacy.md

# Source: https://posthog.com/docs/product-analytics/privacy.md

# Source: https://posthog.com/docs/privacy.md

# Privacy compliance - Docs

Posthog gives you privacy controls at different levels to protect user privacy and comply with regulations. This guide covers the different privacy controls we provide and guidance on how to use them.

-   **What you're responsible for**: It's your responsibility to decide what data you collect, if it complies with regulations, and communicate with your users.
-   **What PostHog does for you**: We provide tools and features to help you manage what's collected and store the collected data securely.

## Privacy control features

You can control data collection, ingestion, and storage at different levels. Explore the guides below to learn more about the different privacy control features:

-   [Manage data collection](/docs/privacy/data-collection.md)
-   [Manage data processing](/docs/privacy/data-storage.md#processing-data-before-storage)
-   [Manage data storage](/docs/privacy/data-storage.md)

## Guidance on navigating regulations

In these guides, we offer advice for using PostHog in a compliant manner under the following legal frameworks:

-   [The General Data Protection Regulation](/docs/privacy/gdpr-compliance.md) (GDPR), which applies to all businesses collecting data on EU citizens

-   [The Health Insurance Portability and Accountability Act](/docs/privacy/hipaa-compliance.md) (HIPAA), which applies to businesses capturing and processing health data in the US

-   [The California Consumer Privacy Act](/docs/privacy/ccpa-compliance.md) (CCPA), which applies to qualifying for-profit businesses collecting personal information on residents of California

**These are not legal advice**

It is up to you to ensure you're compliant with regulations. We strongly recommend reading the relevant regulations in full and seeking independent legal advice regarding your obligations.

## Frequently asked questions

This overview covers some frequently asked questions about PostHog and privacy. Have a question not covered here? Use the 'Ask a question' box at the bottom of the page.

### Is it ok for my API key to be exposed and public?

It is **ok** for your **project token** (starts with `phc_`) to be public. It is used to initialize PostHog, capture events, evaluate feature flags, and more, but doesn't have access to your private data.

Your **personal API key** (starts with `phx_`), however, should **NOT** be public as it enables reading and writing potentially private data.

### What is and isn't considered personal data?

It's hard to have a single legal definition of personal data because every legal privacy framework has different ideas, and even names, for it. The GDPR calls it 'personal data' but the US uses the term 'personally identifiable information' (PII) and others refer to it as 'personal information'.

According to the GDPR, personal data is any information which:

1.  Identifies a 'data subject' directly
2.  Can be used to identify a 'data subject' when combined with other information

Read our [simple guide to personal data and PII](/blog/what-is-personal-data-pii.md) for more specific examples to help you identify what personal data you are collecting.

### How does the GDPR impact analytics?

There are three key GDPR principles that impact your use PostHog and analytics in general:

1.  You need to have a good reason to collect personal data
2.  You need to acquire unambiguous consent
3.  Data must be handled securely

Our [guide to personal data](/blog/what-is-personal-data-pii.md) provides an overview of what's considered personal data under the GDPR, but suffice it to say that its definition is broad.

### Is PostHog GDPR compliant?

We have [in-depth GDPR guidance documentation](/docs/privacy/gdpr-compliance.md) for advice on deploying PostHog in a GDPR-compliant way, including [how to configure GDPR consent in PostHog](/docs/privacy/gdpr-compliance.md#step-4-configure-consent) and complying with ['right to be forgotten' requests](/docs/privacy/gdpr-compliance.md#complying-with-right-to-be-forgotten-requests).

We also offer [PostHog Cloud EU](https://eu.posthog.com/signup) – a managed version of PostHog with servers hosted in Frankfurt, ensuring user data never leaves EU jurisdiction.

### Can I use PostHog Cloud under HIPAA?

Yes, we can provide a Business Associate Agreement (BAA) to enable HIPAA-compliant usage of PostHog Cloud. Please [contact us to arrange a BAA and discuss your requirements](/talk-to-a-human.md).

### Is Google Analytics HIPAA compliant?

No, [Google Analytics isn't HIPAA compliant](/blog/is-google-analytics-hipaa-compliant.md), so it can't be used in any context where you're collecting or processing personal health information. PostHog can be used to collect user data under HIPAA. Read our [HIPAA guidance](/docs/privacy/hipaa-compliance.md) for more information.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better